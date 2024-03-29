#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
from os.path import getmtime, exists
import time
import types
import __builtin__
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import DummyTransaction
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers

##################################################
## MODULE CONSTANTS
try:
    True, False
except NameError:
    True, False = (1==1), (1==0)
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.0.1'
__CHEETAH_versionTuple__ = (2, 0, 1, 'final', 0)
__CHEETAH_genTime__ = 1241539198.718806
__CHEETAH_genTimestamp__ = 'Tue May  5 17:59:58 2009'
__CHEETAH_src__ = 'src/aon/update/PackageListsTemplate.tmpl'
__CHEETAH_srcLastModified__ = 'Tue May  5 17:31:24 2009'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class PackageListsTemplate(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        Template.__init__(self, *args, **KWs)
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
        
        write('''    <span class="aon-update-help" />
    <table class="aon-update-table" cellpadding="0" cellspacing="0" >

\t\t<thead>
\t\t</thead>

\t\t<tbody > 
''')
        step = 0
        for package in VFFSL(SL,"packages",True): # generated from line 9, col 4
            step += 1
            if VFFSL(SL,"step",True) % 2 > 0: # generated from line 11, col 5
                write('''            \t<tr >
''')
            else: # generated from line 13, col 5
                write('''            \t<tr style="background:#eee" >
''')
            write('''                  \t\t<td class="aon-update-cell" >
                    \t\t<input type="checkbox" id="package" name="package" class="aon-update-input" value="''')
            _v = VFFSL(SL,"package.name",True) # '$package.name' on line 17, col 106
            if _v is not None: write(_filter(_v, rawExpr='$package.name')) # from line 17, col 106.
            write('''" checked="checked" />
                  \t\t</td>
                  \t\t<td class="aon-update-cell" >
                    \t\t<label class="aon-update-label"  >''')
            _v = VFFSL(SL,"package.name",True) # '$package.name' on line 20, col 57
            if _v is not None: write(_filter(_v, rawExpr='$package.name')) # from line 20, col 57.
            write('''</label>
                  \t\t</td>
                  \t\t<td class="aon-update-cell" >
                    \t\t<label class="aon-update-label"  >''')
            _v = VFFSL(SL,"package.version",True) # '$package.version' on line 23, col 57
            if _v is not None: write(_filter(_v, rawExpr='$package.version')) # from line 23, col 57.
            write('''</label>
                  \t\t</td>
                  \t\t<td class="aon-update-cell" >
                    \t\t<label class="aon-update-label"  >''')
            _v = VFFSL(SL,"package.version",True) # '$package.version' on line 26, col 57
            if _v is not None: write(_filter(_v, rawExpr='$package.version')) # from line 26, col 57.
            write('''</label>
                  \t\t</td>
            \t</tr>
''')
        write('''
\t\t</tbody>

\t\t<tfoot>
        \t<tr pattern="listItem">
          \t\t<td class="">
          \t\t</td>
          \t\t<td class="" colspan="3">
            \t\t<input id="" name="login_btn" type="submit" value="Actualizar" onclick="" class="aon-update-button"/>
          \t\t</td>
        \t</tr>
\t\t</tfoot>

    </table>
                    
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

    _mainCheetahMethod_for_PackageListsTemplate= 'respond'

## END CLASS DEFINITION

if not hasattr(PackageListsTemplate, '_initCheetahAttributes'):
    templateAPIClass = getattr(PackageListsTemplate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(PackageListsTemplate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=PackageListsTemplate()).run()


