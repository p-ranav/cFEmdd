__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

import os, sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from ext import *
from mission import CFS_Mission
import syntax

class CFSEdit(QtGui.QTextEdit):
    def __init__(self, parent=None):
        super(CFSEdit, self).__init__(parent)
        self.completer = QtGui.QCompleter()
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.activated.connect(self.insertCompletion)

        self.model = QtGui.QStringListModel()
        self.completer.setModel(self.model)
        self.model.setStringList(
            ["application", "apply", "eventIDs", "commandCodes", "msg", "table", 
             'uint8', 'uint16', 'uint32', 'uint64', 'char'
             'CFE_ES_NoArgsCmd_t', 'CFE_ES_RestartCmd_t', 
             'CFE_ES_ShellCmd_t', 'CFE_ES_QueryAllCmd_t', 
             'CFE_ES_QueryAllTasksCmd_t', 'CFE_ES_WriteSyslogCmd_t',
             'CFE_ES_WriteERlogCmd_t', 'CFE_ES_OverWriteSysLogCmd_t', 
             'CFE_ES_StartAppCmd_t', 'CFE_ES_AppNameCmd_t', 
             'CFE_ES_AppReloadCmd_t', 'CFE_ES_SetMaxPRCountCmd_t',
             'CFE_ES_DeleteCDSCmd_t', 'CFE_ES_PerfStartCmd_t',
             'CFE_ES_PerfStopCmd_t', 'CFE_ES_PerfSetFilterMaskCmd_t',
             'CFE_ES_PerfSetTrigMaskCmd_t', 'CFE_ES_TlmPoolStatsCmd_t', 
             'CFE_ES_DumpCDSRegCmd_t', 'CFE_ES_OneAppTlm_t', 
             'CFE_ES_PoolStatsTlm_t', 'CFE_ES_MemHandle_t', 
             'CFE_ES_MemPoolStats_t', 'CFE_ES_HkPacket_t', 
             'CFE_ES_ShellPacket_t'])

    def insertCompletion(self, completion):
        if (self.completer.widget() != self):
            return
        tc = self.textCursor()
        extra = completion.length() - self.completer.completionPrefix().length()
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
        tc.insertText(completion.right(extra))
        self.setTextCursor(tc)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def focusInEvent(self, event):
        if (self.completer):
            self.completer.setWidget(self)
        QtGui.QTextEdit.focusInEvent(self, event)
        
    def keyPressEvent(self, event):
        if (self.completer and self.completer.popup().isVisible()):
            if (event.key() == Qt.Key_Enter):
                event.ignore()
                return
            elif (event.key() == Qt.Key_Return):
                event.ignore()
                return
            elif (event.key() == Qt.Key_Escape):
                event.ignore()
                return
            elif (event.key() == Qt.Key_Tab):
                event.ignore()
                return
            elif (event.key() == Qt.Key_Backtab):
                event.ignore()
                return

        isShortcut = (event.modifiers() and Qt.ControlModifier and event.key() == Qt.Key_E)
        if (not self.completer or not isShortcut):
            QtGui.QTextEdit.keyPressEvent(self, event)
        
        ctrlOrShift = (event.modifiers() and (Qt.ControlModifier or Qt.ShiftModifier))
        if (not self.completer or (not ctrlOrShift and event.text().isEmpty())):
            return

        eow = QtCore.QString("~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-=")
        hasModifier = ((event.modifiers() != Qt.NoModifier) and not ctrlOrShift)
        completionPrefix = self.textUnderCursor()
        
        if (not isShortcut and (hasModifier or event.text().isEmpty() or completionPrefix.length() < 1 or\
                             eow.contains(event.text().right(1)))):
            self.completer.popup().hide()
            return

        if (completionPrefix != self.completer.completionPrefix()):
            self.completer.setCompletionPrefix(completionPrefix)
            self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))
        
        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0) +\
                    self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr)

class Main(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)

        self.filename = ""
        self.changesSaved = True
        self.initUI()

    def initToolbar(self):

        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create a New CFS Mission")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)
        
        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open an Existing CFS Mission")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)
        
        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save Mission")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)
        
        self.toolbar = self.addToolBar("Options")
        
        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print Mission",self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printMission)

        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Preview Mission",self)
        self.previewAction.setStatusTip("Preview Mission before Printing")
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        self.toolbar.addAction(self.printAction)
        self.toolbar.addAction(self.previewAction)
        
        self.toolbar.addSeparator()

        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to Clipboard",self)
        self.cutAction.setStatusTip("Cut to Clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to Clipboard",self)
        self.copyAction.setStatusTip("Copy to Clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from Clipboard",self)
        self.pasteAction.setStatusTip("Paste from Clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo Last Action",self)
        self.undoAction.setStatusTip("Undo Last Action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo Last Undone Action",self)
        self.redoAction.setStatusTip("Redo Last Undone Action")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)
        
        self.toolbar.addSeparator()

        self.findAction = QtGui.QAction(QtGui.QIcon("icons/find.png"),"Find and Replace",self)
        self.findAction.setStatusTip("Find and Replace words in your Mission")
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.triggered.connect(find.Find(self).show)

        self.toolbar.addAction(self.findAction)

        self.toolbar.addSeparator()

        self.generateAction = QtGui.QAction(QtGui.QIcon("icons/generate.png"), "Generate Mission",self)
        self.generateAction.setStatusTip("Generate Mission Files")
        self.generateAction.setShortcut("Ctrl+G")
        self.generateAction.triggered.connect(self.generate)

        self.openmissiondirAction = QtGui.QAction(QtGui.QIcon("icons/openmissiondir.png"), 
                                                  "Open Mission Directory",self)
        self.openmissiondirAction.setStatusTip("Open Mission Directory")
        self.openmissiondirAction.setShortcut("Ctrl+G")
        self.openmissiondirAction.triggered.connect(self.openmissiondir)

        self.toolbar.addAction(self.generateAction)
        self.toolbar.addAction(self.openmissiondirAction)

    def initFormatbar(self):
        
        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")
        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)
        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)
        edit.addAction(self.findAction)

    def initUI(self):

        self.text = CFSEdit(self)
        self.setCentralWidget(self.text)
        
        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()
        
        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()
        
        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)
        
        self.setWindowTitle("CFSEditor")
        self.text.setTabStopWidth(33)
        self.setWindowIcon(QtGui.QIcon("icons/cfs-editor.png"))
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        self.text.textChanged.connect(self.changed)

        self.highlight = syntax.CFSHighlighter(self.text.document())

        font = QtGui.QFont("Ubuntu",15,QtGui.QFont.Normal) 
        font.setLetterSpacing(QtGui.QFont.PercentageSpacing, 120)
        self.text.setCurrentFont(font)

    def new(self):

        spawn = Main(self)
        spawn.show()

    def open(self):

        # Get filename and show only .writer files
        self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open CFS Mission',".","(*.cfs)")

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())
                font = QtGui.QFont("Ubuntu",15,QtGui.QFont.Normal)    
                self.text.setCurrentFont(font)
                self.statusbar.showMessage("Opened Mission: {}".format(self.filename))

    def save(self):
        
        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        if not str(self.filename).endswith(".cfs"):
            self.filename += ".cfs"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
        with open(self.filename,"wt") as file:
            file.write(self.text.toPlainText())
            self.statusbar.showMessage("Saved Mission: {}".format(self.filename))

        self.changesSaved = True

    def preview(self):
        
        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def printMission(self):

        # Open printing dialog
        dialog = QtGui.QPrintDialog()
        
        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def generate(self):
        mission = CFS_Mission(str(self.filename))
        mission.parse_model()
        mission.print_model()
        mission.generate_apps()

    def openmissiondir(self):
        if (self.filename != ""):
            path, name = os.path.split(str(self.filename))
            os.system('xdg-open "%s"' % path)
        else:
            print 'No Active Mission'

    def cursorPosition(self):
                
        cursor = self.text.textCursor()
        
        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        
        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))

    def changed(self):
        self.changesSaved = False

    def closeEvent(self,event):

        if self.changesSaved:
            event.accept()

        else:

            popup = QtGui.QMessageBox(self)
            popup.setIcon(QtGui.QMessageBox.Warning)
            popup.setText("The Mission has been modified")
            popup.setInformativeText("Do you want to save your changes?")
            popup.setStandardButtons(QtGui.QMessageBox.Save    |
                                     QtGui.QMessageBox.Cancel |
                                     QtGui.QMessageBox.Discard)

            popup.setDefaultButton(QtGui.QMessageBox.Save)

            answer = popup.exec_()

            if answer == QtGui.QMessageBox.Save:
                self.save()
            elif answer == QtGui.QMessageBox.Discard:
                event.accept()
            else:
                event.ignore()

def main():

    app = QtGui.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
