#-*- coding: utf-8 -*-
"""App commons"""
from __future__ import print_function

import os
import datetime
import glob
import traceback
import logging.config, yaml

from easydatalab.common.exceptions import ExecutionError
from easydatalab.common.exceptions import Error

from easydatalab.common.configuration import AppConfiguration

from easydatalab.monitoring.filemonitor import FileMonitor
from easydatalab.monitoring.stepmonitor import StepMonitor
from easydatalab.monitoring.appmonitor import AppMonitor

class AppContext:
    logger = None
    file_monitor = None

    def __init__(self, name='App', log_config_file=None):
        self.name = name
        self.status = -1
        #self.attributes = {}
        self.configuration = None
        self.steps = []
        self.app_monitor = AppMonitor(self)

        self.__init_logging(log_config_file)

        self.logger = logging.getLogger('easydatalab.common.AppContext')

    def __init_logging(self, log_config_file):
        if  log_config_file != None:
          with open(log_config_file) as f:
            log_config = yaml.load(f)
            logging.config.dictConfig( log_config )
            logger = logging.getLogger(self.name)
            logger.info('log configuration loaded from %s' % log_config_file)

    def __str__(self):
        return self.name

    def set_configuration(self, configuration):
        self.configuration = configuration

    def get_configuration(self):
        return self.configuration

    def skip_steps(self, skipped_step_names):
        print('INFO - will skip %s' % str(skipped_step_names) )
        self.skipped_step_names = skipped_step_names

    def new_step(self, stepName):
        should_skip = stepName in self.skipped_step_names
        step = AppStep(stepName, self, skipped = should_skip)
        self.steps.append(step)
        return step

    def new_configuration(self, cfgPath):
        self.configuration = AppConfiguration(cfgPath, self)
        return self.configuration


    def __enter__(self):
        self.app_monitor.start()
        file_monitor = FileMonitor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
       status = None
       if exc_type == None:
          self.app_monitor.stop()
          status = True
       else:
          error_message = traceback.format_exception_only(exc_type, exc_value)[0]
          self.app_monitor.fail(error_message)
          status = False

       self.app_monitor.report(self.steps)

       return status


#TODO TU skipped
class AppStep:
    def __init__(self, stepName, theAppContext, skipped=False):
        self.stepName = stepName
        self.theAppContext = theAppContext
        self.skipped = skipped
        self.logger = logging.getLogger('easydatalab.common.AppStep')
        self.step_monitor = StepMonitor(self)

    def __enter__(self):
        self.step_monitor.start()
        self.step_monitor.header()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
       if exc_type == None:
           self.step_monitor.stop()
           self.step_monitor.footer()
           return True
       else:
           error_message = traceback.format_exception_only(exc_type, exc_value)[0]
           self.step_monitor.fail(error_message)
           self.step_monitor.footer()
           return False


    def subprocess(self, subprocessClass):
        instance = subprocessClass(self.theAppContext, self)
        return  instance

    def assert_input_file(self, filePath):
        # TODO factorisation validator
        if '*' in filePath:
           # lookup a matching file
           foundMatch = False
           for filepath_object in glob.glob(filePath):
               if os.path.isfile(filepath_object):
                  foundMatch = True
           if not foundMatch:
              msg = 'not file is matching required pattern %s' % filePath
              raise ExecutionError('Input assertion', msg)
        else:
          # lookup the exact name
          if not os.path.exists(filePath):
              msg = 'required file %s not found' % filePath
              raise ExecutionError('Input assertion', msg)

    def enabled(self):
       return not self.skipped

    def summary(self):
       return self.step_monitor.summary()

    def __del__(self):
        print("__del__")

    def __repr__(self):
        return self.stepName

    def __str__(self):
        return self.stepName


