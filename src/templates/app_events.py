#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1450479141.10771
__CHEETAH_genTimestamp__ = 'Fri Dec 18 14:52:21 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/cFEmdd/src/templates/app_events.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Dec 15 10:01:58 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class app_events(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(app_events, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''/************************************************************************
** File:
**    ''')
        _v = VFFSL(SL,"application_name",True) # u'${application_name}' on line 3, col 7
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 3, col 7.
        write(u'''_events.h 
**
** Purpose: 
**  Define ''')
        _v = VFFSL(SL,"application_name",True) # u'${application_name}' on line 6, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 6, col 12.
        write(u''' Events IDs
**
** Notes:
**
**
*************************************************************************/
#ifndef _''')
        _v = VFFSL(SL,"application_name",True) # u'${application_name}' on line 12, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 12, col 11.
        write(u'''_events_h_
#define _''')
        _v = VFFSL(SL,"application_name",True) # u'${application_name}' on line 13, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 13, col 11.
        write(u'''_events_h_

''')
        for event_id in VFFSL(SL,"event_ids_list",True): # generated from line 15, col 1
            write(u'''#define ''')
            _v = VFFSL(SL,"event_id",True) # u'$event_id' on line 16, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'$event_id')) # from line 16, col 10.
            write(u'''
''')
        write(u'''
#endif /* _''')
        _v = VFFSL(SL,"application_name",True) # u'${application_name}' on line 19, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 19, col 13.
        write(u'''_events_h_ */
/************************/
/*  End of File Comment */
/************************/
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_app_events= 'respond'

## END CLASS DEFINITION

if not hasattr(app_events, '_initCheetahAttributes'):
    templateAPIClass = getattr(app_events, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(app_events)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=app_events()).run()


