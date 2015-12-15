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
__CHEETAH_genTime__ = 1450199512.510675
__CHEETAH_genTimestamp__ = 'Tue Dec 15 11:11:52 2015'
__CHEETAH_src__ = '/home/jeb/Repositories/cFEmdd/src/templates/app_version.tmpl'
__CHEETAH_srcLastModified__ = 'Tue Dec 15 10:48:46 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class app_version(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(app_version, self).__init__(*args, **KWs)
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
**   ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"dollar_id",True) # u'${dollar_id}' on line 3, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'${dollar_id}')) # from line 3, col 6.
        write(u''': ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"application_name",True) # u'${application_name}' on line 3, col 20
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 3, col 20.
        write(u'''_version.h  $
**
** Purpose: 
**  The ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"application_name",True) # u'${application_name}' on line 6, col 9
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 6, col 9.
        write(u''' application header file containing version number
**
** Notes:
**
**
*************************************************************************/
#ifndef _''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"application_name",True) # u'${application_name}' on line 12, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 12, col 11.
        write(u'''_version_h_
#define _''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"application_name",True) # u'${application_name}' on line 13, col 11
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 13, col 11.
        write(u'''_version_h_

''')
        for subversion in VFSL([locals()]+SL+[globals(), builtin],"version_list",True): # generated from line 15, col 1
            write(u'''#define ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"subversion",True) # u'$subversion' on line 16, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'$subversion')) # from line 16, col 10.
            write(u'''
''')
        write(u'''
#endif /* _''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"application_name",True) # u'${application_name}' on line 19, col 13
        if _v is not None: write(_filter(_v, rawExpr=u'${application_name}')) # from line 19, col 13.
        write(u'''_version_h_ */

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

    _mainCheetahMethod_for_app_version= 'respond'

## END CLASS DEFINITION

if not hasattr(app_version, '_initCheetahAttributes'):
    templateAPIClass = getattr(app_version, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(app_version)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=app_version()).run()


