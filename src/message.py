__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

from collections import OrderedDict

class cFE_Message():
    def __init__(self):
        self.kind = "Message"
        self.name = ""
        self.msgtype = ""
        self.comment = ""
        self.fields = []

