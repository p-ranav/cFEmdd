__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

import sys, os, inspect
from application import cFE_Application
from message import cFE_Message

# Find ANTLR4 python runtime
antlr4 = os.path.realpath(os.path.abspath
                          (os.path.join
                           (os.path.split
                            (inspect.getfile
                             (inspect.currentframe()
                          )
                         )[0], "Antlr4")
                       ))
if antlr4 not in sys.path:
    sys.path.insert(0, antlr4)
from antlr4 import *

# Find CFS Mission Lexer, Parser and Visitor
cfs_grammar = os.path.realpath(os.path.abspath
                               (os.path.join
                                (os.path.split
                                 (inspect.getfile
                                  (inspect.currentframe()
                               )
                              )[0], "grammar/")
                            ))

if cfs_grammar not in sys.path:
    sys.path.insert(0, cfs_grammar)
from CFS_MissionLexer import CFS_MissionLexer
from CFS_MissionParser import CFS_MissionParser
from CFS_MissionListener import CFS_MissionListener
from CFS_MissionVisitor import CFS_MissionVisitor

# cFE Application Builder
# Builds a cFE Application Object from .cfs file
class cFE_Application_Builder(CFS_MissionListener):
    def __init__(self, parent_mission):
        self.parent = parent_mission
        self.apps = []

    def enterApplication(self, ctx):
        self.application = cFE_Application()
        self.application.parent = self.parent

    def exitApplication(self, ctx):
        self.apps.append(self.application)

    def enterApp_name(self, ctx):
        self.application.name = ctx.getText()

    def enterEvent_id(self, ctx):
        id_name = ""
        id_value = -1
        for child in ctx.getChildren():
            context = str(type(child))
            if 'Id_nameContext' in context:
                id_name = child.getText()
            if 'Id_valueContext' in context:
                id_value = child.getText()
        if id_name != "":
            if id_value != -1:
                self.application.event_ids[id_name] = id_value

    def enterCommand_code(self, ctx):
        cmd_name = ""
        cmd_value = -1
        for child in ctx.getChildren():
            context = str(type(child))
            if 'Cmd_nameContext' in context:
                cmd_name = child.getText()
            if 'Cmd_valueContext' in context:
                cmd_value = child.getText()
        if cmd_name != "":
            if cmd_value != -1:
                self.application.command_codes[cmd_name] = cmd_value

    def enterMsg(self, ctx):
        self.message = cFE_Message()

    def enterMsgname(self, ctx):
        self.message.name = ctx.getText()

    def enterMsgtype(self, ctx):
        self.message.msgtype = ctx.getText()
        if self.message.msgtype == "table":
            self.message.comment = "Definition of Table Data Structure"
        elif self.message.msgtype == "critical":
            self.message.comment = "Type definition Critical Data Store"
        elif self.message.msgtype == "command":
            self.message.comment\
                ="Type definition (generic \"no arguments\" command)"
        elif self.message.msgtype == "hosuekeeping":
            self.message.comment = "Type definition (housekeeping)"
        elif self.message.msgtype == "global":
            self.message.comment = "Type definition (global data)"

    def enterField(self, ctx):
        datatype = ""
        fieldname = ""
        for child in ctx.getChildren():
            context = str(type(child))
            if 'DatatypeContext' in context:
                datatype = child.getText()
            if 'Fieldname' in context:
                fieldname = child.getText()
        if datatype != "":
            if fieldname != "":
                self.message.fields[datatype] = fieldname
                
    def exitMsg(self, ctx):
        self.application.messages.append(self.message)

    def enterVersion(self, ctx):
        version_name = ""
        version_value = -1
        for child in ctx.getChildren():
            context = str(type(child))
            if 'Version_nameContext' in context:
                version_name = child.getText()
            if 'Version_valueContext' in context:
                version_value = child.getText()
        if version_name != "":
            if version_value != -1:
                self.application.version[version_name] = version_value
