__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

import sys, os, inspect, collections, shutil, errno
from collections import OrderedDict

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

working_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(working_dir, "/templates")
# Recursively compile on template files in templates directory
os.system("/usr/local/bin/cheetah compile " + template_dir + "/*.tmpl > /dev/null 2>&1")
cfs_templates = os.path.realpath(os.path.abspath
                                 (os.path.join
                                  (os.path.split
                                   (inspect.getfile
                                    (inspect.currentframe()
                                 )
                                )[0], "templates")
                              ))
if cfs_templates not in sys.path:
    sys.path.insert(0, cfs_templates)
# From template import *    
# ...

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
                
class CFS_Mission():
    def __init__(self, model):
        self.kind = "Mission"

        # Mission Name and Path
        self.path, self.name = os.path.split(model)
        self.name = self.name.split('.')[0]

        # Applications
        self.apps = []

        # Prepare directory structure
        self.prepare_dir()

        self.builder = cFE_Application_Builder(self)

    def prepare_dir(self):
        self.mission_home = os.path.join(self.path, self.name)
        if not os.path.exists(self.mission_home):
            os.makedirs(self.mission_home)
        self.working_dir = os.path.dirname(os.path.realpath(__file__))
        self.cfe_tree = (os.path.join(self.working_dir, "cfe"))
        self.osal_tree = (os.path.join(self.working_dir, "osal"))
        self.psp_tree = (os.path.join(self.working_dir, "psp"))
        self.docs_tree = (os.path.join(self.working_dir, "docs"))
        if not os.path.exists(os.path.join(self.mission_home, "cfe")):
            self.copy_dir_tree(self.cfe_tree,
                               os.path.join(self.mission_home, "cfe"))
        if not os.path.exists(os.path.join(self.mission_home, "osal")):
            self.copy_dir_tree(self.osal_tree,
                               os.path.join(self.mission_home, "osal"))
        if not os.path.exists(os.path.join(self.mission_home, "docs")):
            self.copy_dir_tree(self.docs_tree,
                               os.path.join(self.mission_home, "docs"))
        if not os.path.exists(os.path.join(self.mission_home, "psp")):
            self.copy_dir_tree(self.psp_tree,
                               os.path.join(self.mission_home, "psp"))            
        if not os.path.exists(os.path.join(self.mission_home, "cfe-OSS-readme.txt")):
            self.copy_file(os.path.join(self.working_dir, "cfe-OSS-readme.txt"),
                           self.mission_home)
        if not os.path.exists(os.path.join(self.mission_home, "setvars.sh")):
            self.copy_file(os.path.join(self.working_dir, "setvars.sh"),
                           self.mission_home)
        if not os.path.exists(os.path.join(self.mission_home,
                                           "SUA_Open_Source_cFE 6 1_GSC-16232.pdf")):
            self.copy_file(os.path.join(self.working_dir,
                                        "SUA_Open_Source_cFE 6 1_GSC-16232.pdf"),
                           self.mission_home)

        self.apps_dir = os.path.join(self.mission_home, "apps")
        if not os.path.exists(self.apps_dir):
            os.makedirs(self.apps_dir)
        if not os.path.exists(os.path.join(self.mission_home, "build")):
            os.makedirs(os.path.join(self.mission_home, "build"))
        
    def copy_dir_tree(self, src, dest):
        try:
            shutil.copytree(src, dest)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
            else:
                print("wARNING::Directory not copied::%s" % e)
              
    def copy_file(self, src, dest):
        try:
            shutil.copy(src, dest)
        except IOError:
            os.chmod(dest, 777)
            shutil.copy(src, dest)

    def parse_model(self):
        print "CFS Mission Model:", self.name
        # Read the input model
        model = FileStream(os.path.join(self.path, self.name + '.cfs'))
        # Instantiate the CFS_Mission Lexer
        lexer = CFS_MissionLexer(model)
        # Generate Tokens
        stream = CommonTokenStream(lexer)
        # Instantiate the CFS_Mission Parser
        parser = CFS_MissionParser(stream)
        # Parse from starting point of grammar
        tree = parser.start()
        # Instantiate a Parse Tree Walker
        walker = ParseTreeWalker()
        walker.walk(self.builder, tree)
        
class cFE_Application():
    def __init__(self):
        self.kind = "Application"
        self.parent = None
        self.name = ""
        self.path = ""
        self.event_ids = OrderedDict()
        self.command_codes = OrderedDict()
        self.messages = []

class cFE_Message():
    def __init__(self):
        self.kind = "Message"
        self.msgtype = ""
        self.fields = OrderedDict()
