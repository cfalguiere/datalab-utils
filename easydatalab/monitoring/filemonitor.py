#-*- coding: utf-8 -*-
from __future__ import print_function

import logging
import csv


class FileMonitor:

      def __init__(self):
            self.items = [ ]
            self.logger = logging.getLogger('monitor.FileMonitor')

      def track(self, step, input_file, output_file ):
            monitor = FileMonitorItem( step, input_file, output_file )
            self.items.append( monitor )
            self.logger = logging.getLogger('monitor.FileMonitor')
            return monitor


      def report(self, monitor ):
            print( '===========================================================')
            print( '|')
            print( '| File Monitor Report')
            print( '|')
            print( '| Number of files: %s' % len(self.items) )
            for item in self.items:
                print( '| {0} {1} -> {2} - {3} '.format( item.status, item.input_file, item.output_file, item.input_size ))
            print( '===========================================================')


      def exportToCsv(self, filename ):
            headers =   [  'step', 'input_file', 'output_file', 'status', 'input_checksum', 'input_nb_lines', 'input_size' ]
            with open( filename, 'wb') as csvfile:
                  reportwriter = csv.DictWriter(csvfile, fieldnames=headers, delimiter='; ', quoting=csv.QUOTE_MINIMAL)
                  reportwriter.writeheader()
                  writer.writerow( vars(item) )



class FileMonitorItem:

      def __init__(self, step, input_file, output_file):
          self.step = step
          self.input_file = input_file
          self.output_file = output_file
          self.status = 'Tracked'
          self.input_checksum = None
          self.input_nb_lines = None
          self.input_size = None
          self.output_nb_lines = None
          self.output_size = None

      def pre_condition(self):
            self.status = 'Started'
            #TODO check

      def post_condition(self):
            self.status = 'Done'
            #TODO check

