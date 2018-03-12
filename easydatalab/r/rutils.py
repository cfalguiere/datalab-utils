#!/usr/bin/python
#-*- coding: utf-8 -*-

from __future__ import print_function

import subprocess
import os, sys
import traceback

from easydatalab.common.exceptions import ExecutionError

class RScript:
    def __init__(self, theAppContext, stepName, scriptName=None):
        self.theAppContext = theAppContext
        self.stepName = stepName
        self.configuration = theAppContext.get_configuration()
        if scriptName == None:
              self.scriptName = stepName
        else:
              self.scriptName = scriptName

    def __enter__(self):
        print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
        print( "| RScript {0} is starting".format(self.scriptName) )
        self.pathToRScript = self.configuration.get_parameter('PATH:rscript')
        if not os.path.exists(self.pathToRScript):
           raise ExecutionError(self.stepName, 'Rscript  not found at %s' % self.pathToRScript )
        print( "..........................................................." )
        self.pathToCode = self.configuration.get_parameter('PATH:rcode')
        if not os.path.exists(self.pathToCode):
           raise ExecutionError(self.stepName, 'Base directory to R scripts (rcode) not found at %s' % self.pathToCode )
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print( "..........................................................." )
        if exc_type == None:
            print( '| RScript %s completed' %   self.scriptName )
            print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
        else:
            print( '| RScript %s Aborted' %  (self.scriptName) )
            print( "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" )
            raise ExecutionError('RScript', 'error during %s execution - %s' % (self.scriptName, traceback.format_exc() ) )

    def get_full_path(self, scriptPath):
        path = '{0}/{1}'.format(self.pathToCode , scriptPath)
        if not os.path.exists(path):
           raise ExecutionError(self.stepName, 'R program not found at %s' % path )
        return path

    def get_parameters_as_map(self, keyList):
        params = []
        params.append( '{0}={1}'.format('pathToCode', self.pathToCode) )
        for key in keyList:
            if key != 'pathToCode':
                try:
                    params.append( "%s=%s" % (key,  self.configuration.get_parameter(key) ) )
                except:
                    raise ExecutionError("Missing parameter", key)
        return params

    def call( self, scriptPath, requiredParams):
        print( "INFO - Calling script {0} with required parameters %s".format(self.scriptName), str(requiredParams) )

        argsList = self.get_parameters_as_map(requiredParams)

        pathToProgram = self.get_full_path(scriptPath)
        sys.stdout.flush()
        subprocess.check_call( [ self.pathToRScript, pathToProgram ]  + argsList + [ 'stepName=%s' % self.stepName ])
