#-*- coding: utf-8 -*-
from __future__ import print_function

import logging
import datetime
import traceback

class AppMonitor:

      def __init__(self, step):
          self.step = step
          self.status = 'Not Started'
          self.start_ts = None
          self.stop_ts = None
          self.logger = logging.getLogger('easydatalab.monitor.AppMonitor')

      def start(self):
          self.start_ts = datetime.datetime.now()
          self.status = 'Started'

      def stop(self, ):
            self.stop_ts = datetime.datetime.now()
            self.status = 'Completed'

      def fail(self, error_message):
            self.stop_ts = datetime.datetime.now()
            self.logger.error( error_message )
            self.status = 'Aborted'

      def report(self, steps):
          elapsed = self.stop_ts  - self.start_ts
          i = 1
          print( '===========================================================')
          print( '| REPORT ')
          print( '|')
          print( '| ==== %s Steps ====' % len(steps) )
          for step in steps:
              print( '| [{0}] {1}'.format( i, step.summary() ) )
              i += 1
          print( '|')
          print( '| Application {0} in {1} seconds'.format( self.status, elapsed ))
          print( '| {0} - {1}'.format( self.start_ts, self.stop_ts))
          print( '===========================================================')

          #if  AppContext.file_monitor:
          #   AppContext.file_monitor.report()


      def summary(self):
          elapsed = self.stop_ts  - self.start_ts
          print( '| Application {0} in {1} seconds'.format( self.status, elapsed ))

          #if  AppContext.file_monitor:
          #   AppContext.file_monitor.report()

