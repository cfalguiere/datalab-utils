#-*- coding: utf-8 -*-
from __future__ import print_function

import logging
import datetime
import traceback

class StepMonitor:

      def __init__(self, step):
          self.step = step
          self.status = 'Not Started'
          self.start_ts = None
          self.stop_ts = None
          self.error_message = None
          self.logger = logging.getLogger('easydatalab.monitor.StepMonitor')

      def start(self):
          if self.step.enabled():
              self.start_ts = datetime.datetime.now()
              self.status = 'Started'

      def stop(self, ):
            self.stop_ts = datetime.datetime.now()
            if self.step.enabled():
                self.status = 'Completed'
            else:
                self.status = 'Skipped'

      def fail(self, error_message):
            self.stop_ts = datetime.datetime.now()
            self.logger.error( error_message )
            self.status = 'Aborted'

      def header(self):
          print( '| ')
          print( '===========================================================')
          print( "| STEP %s is starting" % str(self.step) )
          print( '-----------------------------------------------------------')

      def footer(self):
           print( '-----------------------------------------------------------')
           if  self.step.enabled():
               elapsed = self.stop_ts  - self.start_ts
               template = "{0} - {1} in {2}.{3} seconds"
               self.message = template.format( str(self.step), self.status, elapsed.seconds, elapsed.microseconds)
           else:
               self.message  = "{0} - {1}".format( str(self.step), self.status)
           print( "| STEP {0}".format( self.message ) )
           print( '===========================================================')
           print( '| ')

      def summary(self):
           return self.message
       #time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
