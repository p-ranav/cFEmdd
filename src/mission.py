__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

import sys, os, inspect, shutil, errno
import builder
import generator

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

        self.builder = builder.cFE_Application_Builder(self)
        self.generator = None

    def prepare_dir(self):
        self.mission_home = os.path.join(self.path, self.name)
        if not os.path.exists(self.mission_home):
            os.makedirs(self.mission_home)
        self.working_dir = os.path.dirname(os.path.realpath(__file__))
        self.cfe_tree = (os.path.join(self.working_dir, "cfe"))
        self.build_tree = (os.path.join(self.working_dir, "build"))
        self.osal_tree = (os.path.join(self.working_dir, "osal"))
        self.psp_tree = (os.path.join(self.working_dir, "psp"))
        self.docs_tree = (os.path.join(self.working_dir, "docs"))
        if not os.path.exists(os.path.join(self.mission_home, "cfe")):
            self.copy_dir_tree(self.cfe_tree,
                               os.path.join(self.mission_home, "cfe"))
        if not os.path.exists(os.path.join(self.mission_home, "build")):
            self.copy_dir_tree(self.build_tree,
                               os.path.join(self.mission_home, "build"))
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
        if not os.path.exists(os.path.join(self.apps_dir, "inc")):
            os.makedirs(os.path.join(self.apps_dir, "inc"))
        
    def copy_dir_tree(self, src, dest):
        try:
            shutil.copytree(src, dest)
        except OSError as e:
            if e.errno == errno.ENOTDIR:
                shutil.copy(src, dest)
            else:
                print ("WARNING::Directory not copied::%s" % e)
              
    def copy_file(self, src, dest):
        try:
            shutil.copy(src, dest)
        except IOError:
            os.chmod(dest, 777)
            shutil.copy(src, dest)

    def parse_model(self):
        # Read the input model
        model = builder.FileStream(os.path.join(self.path, self.name + '.cfs'))
        # Instantiate the CFS_Mission Lexer
        lexer = builder.CFS_MissionLexer(model)
        # Generate Tokens
        stream = builder.CommonTokenStream(lexer)
        # Instantiate the CFS_Mission Parser
        parser = builder.CFS_MissionParser(stream)
        # Parse from starting point of grammar
        tree = parser.start()
        # Instantiate a Parse Tree Walker
        walker = builder.ParseTreeWalker()
        walker.walk(self.builder, tree)

        self.apps = self.builder.apps

    def generate_apps(self):
        self.generator = generator.cFE_Application_Generator()
        self.generator.generate(self)
