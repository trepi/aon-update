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
__CHEETAH_genTime__ = 1241536213.178705
__CHEETAH_genTimestamp__ = 'Tue May  5 17:10:13 2009'
__CHEETAH_src__ = 'src/aon/update/BaseTemplate.tmpl'
__CHEETAH_srcLastModified__ = 'Tue May  5 17:10:06 2009'
__CHEETAH_docstring__ = 'Autogenerated by CHEETAH: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class BaseTemplate(Template):

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
        
        write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Frameset//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd" >
<html>
  <head>
    <title>Updates</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="shortcut icon" type="image/x-icon" href="images/favicon.ico"/>
    <link class="user" href="css/aon-update.css" rel="stylesheet" type="text/css"/>
  </head>
  <body>
    <div class="aon-update">
    <form id="login" method="post">
      <div class="aon-update-box">

\t\t<div class="aon-update-title">
\t\t  <span> / Updates</span>
\t\t</div>
\t\t
''')
        self._handleCheetahInclude(VFFSL(SL,"body",True)					, trans=trans, includeFrom="str", raw=True)
        write('''        
\t    <div class="aon-update-info">
\t      <div class="aon-update-info-title">
\t        <span class="aon-outputText">Atencio&acute;n al cliente:</span>
\t      </div>
\t      <div class="aon-bold">
\t        <span class="aon-outputText">902.121.009</span>
\t      </div>
\t      <div>
\t        <a href="mailto:rtrepiana@gmail.com" target="_blank">
\t          <span class="aon-outputText">rtrepiana@gmail.com</span>
\t        </a>
\t      </div>
\t    </div>
\t    <div class="aon-update-info2">
\t      <span class="aon-outputText">aon Solutions es una marca registrada de </span>
\t      <span class="aon-update-info2-company">rtrepiana </span>
\t      <span class="aon-update-info2-company">NETWORKS S.A.</span>
\t    </div>
\t\t                    
\t\t</div>
    </form>
    </div>
  </body>
</html>
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

    _mainCheetahMethod_for_BaseTemplate= 'respond'

## END CLASS DEFINITION

if not hasattr(BaseTemplate, '_initCheetahAttributes'):
    templateAPIClass = getattr(BaseTemplate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(BaseTemplate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=BaseTemplate()).run()


