__author__ = "Pranav Srinivas Kumar"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Pranav Srinivas Kumar"
__email__ = "pkumar@isis.vanderbilt.edu"
__status__ = "Production"

from cfs import CFS_Mission

if __name__ == "__main__":
    mission = CFS_Mission('/home/jeb/Desktop/missionxyz.cfs')
    mission.parse_model()
