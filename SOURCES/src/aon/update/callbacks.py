
'''
Created on May 6, 2009

@author: rtrepiana
'''

import rpm
import os
import sys
import yum
import logging
from yum.constants import *


# yum callback handlers





class RPMDisplay:
    
    def __init__(self):
        
        self.erased = []
        self.updated = []
        self.cleanup = []
        self.obsoloted = []
        self.installed = []
    
        self.fileaction = { TS_UPDATE: self.updated, 
                           TS_ERASE: self.erased,
                           TS_INSTALL: self.installed, 
                           TS_TRUEINSTALL: self.installed, 
                           TS_OBSOLETED: self.obsoloted,
                           TS_OBSOLETING: self.installed,
                           TS_UPDATED: self.cleanup}  

    def event(self, package, action, te_current, te_total, ts_current, ts_total):
        """
        @param package: A yum package object or simple string of a package name
        @param action: A yum.constant transaction set state or in the obscure 
                       rpm repackage case it could be the string 'repackaging'
        @param te_current: Current number of bytes processed in the transaction
                           element being processed
        @param te_total: Total number of bytes in the transaction element being
                         processed
        @param ts_current: number of processes completed in whole transaction
        @param ts_total: total number of processes in the transaction.
        """
        pass

    def filelog(self, package, action):
        # If the action is not in the fileaction list then dump it as a string
        # hurky but, sadly, not much else 
        if self.fileaction.has_key(action):
            self.fileaction[action].append(package)

    def errorlog(self, msg):
        """takes a simple error msg string"""
        
        pass

    def scriptout(self, package, msgs):
        """package is the package.  msgs is the messages that were
        output (if any)."""
        pass

