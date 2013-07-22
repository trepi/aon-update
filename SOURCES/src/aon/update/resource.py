# 
#                                           _       _       

'''
Created on Apr 4, 2009

@author: Raúl Trepiana <rtrepiana@eseferalia.com>
'''

import os
import yum
import exceptions

import aon.update
from callbacks import *
from BaseTemplate import *
from ErrorTemplate import *
from PackageListsTemplate import * 
from TransactionLogTemplate import *
from Cheetah.Template import Template

from twisted.web.resource import Resource


_YumBase = aon.update.YumBaseAon()

_YumBase.conf.cache = os.geteuid() != 0


class HasUpdate(Resource):
    
    def render_GET(self, request):
        patterns = 'pattern' in request.args and request.args['pattern'] or None
        pkglists = _YumBase.doPackageLists(pkgnarrow='updates', patterns=patterns)
        return len(pkglists['updates']) and '1' or '0' 

class ResourceBase(Resource):
    
    def render_GET(self, request):
        return self.render_POST(request)

    def render_POST(self, request):
        try :
            body = self.get_BODY(request)
            return  BaseTemplate(searchList=[{'body':body}]).respond()
        except exceptions.Exception, e:
            return ErrorTemplate(searchList=[{'err_msgs':[str(e)]}]).respond()
            

class YumTransaction(ResourceBase):
    
    def __init__(self):
        ResourceBase.__init__(self)

    def get_BODY(self, request):
        try :
            self.do_Action(request)
            _YumBase.resolveDeps()
            rpmDisplay = RPMDisplay()
            _YumBase.processTransaction(rpmDisplay=rpmDisplay)
            return TransactionLogTemplate(searchList=[{'log': rpmDisplay }]).respond()

        except yum.Errors.YumBaseError, e:
            searchList =  [{'err_msgs': hasattr(e.value,'__iter__') and e.value or [str(e)]}]
            return ErrorTemplate(searchList=searchList).respond()


class Install(YumTransaction):
    
    def do_Action(self, request):
        for package in request.args['package']:
            _YumBase.install(pattern=package)

class Update(YumTransaction):
    
    def do_Action(self, request):
        for package in request.args['package']:
            _YumBase.update(pattern=package)

class Remove(YumTransaction):
    
    def do_Action(self, request):
        for package in request.args['package']:
            _YumBase.remove(pattern=package)

class PackageLists(ResourceBase):
    
    def __init__(self, pkgnarrow=None, nopkgsmsg=None, action=None, actionlabel=None):
        self.pkgnarrow = pkgnarrow
        self.nopkgsmsg = nopkgsmsg
        self.action = action
        self.actionlabel = actionlabel
    
    
    def get_BODY(self, request):
        patterns = 'pattern' in request.args and request.args['pattern'] or [] 
        pkglists = _YumBase.doPackageLists(pkgnarrow=self.pkgnarrow, patterns=patterns)
        packages = pkglists.__getitem__(self.pkgnarrow)
        if len(packages) > 0:
            searchList=[{'packages':packages, 
                         'action':self.action , 
                         'actionlabel':self.actionlabel,
                         'pattern':len(patterns) and  patterns[0] or None  }]
            return  PackageListsTemplate(searchList=searchList).respond()
        else :
            return ErrorTemplate(searchList=[{'err_msgs': [self.nopkgsmsg]}]).respond()

