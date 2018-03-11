#!/usr/bin/python
#-*- coding: utf-8 -*-

from __future__ import print_function

import subprocess
import os, sys
import traceback

from sch.common.exceptions import ExecutionError
from sch.init.configuration import AppConfiguration


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
        self.pathToRScript = self.configuration.get_parameter('pathToRScript')
        print( "..........................................................." )
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
          path = '{0}/{1}'.format(self.configuration.get_path_to_code(), scriptPath)
          if not os.path.exists(path):
              raise ExecutionError(self.stepName, 'R program not found at %s' % path )
          return path

    def call( self, scriptPath, requiredParams):
        print( "INFO - Calling script {0} with required parameters %s".format(self.scriptName), str(requiredParams) )
        config = self.theAppContext.get_configuration()

        c = self.theAppContext.get_configuration()
        argsList = c.get_parameters_as_map(requiredParams)

        pathToProgram = self.get_full_path(scriptPath)
        sys.stdout.flush()
        subprocess.check_call( [ self.pathToRScript, pathToProgram ]  + argsList + [ 'stepName=%s' % self.stepName ])
