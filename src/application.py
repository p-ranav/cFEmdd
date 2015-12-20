__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

from collections import OrderedDict

class cFE_Application():
    def __init__(self):
        self.kind = "Application"
        self.parent = None
        self.name = ""
        self.path = ""
        self.perf_ids = OrderedDict()
        self.msg_ids = OrderedDict()
        self.event_ids = OrderedDict()
        self.command_codes = OrderedDict()
        self.messages = []
        self.version = OrderedDict()
