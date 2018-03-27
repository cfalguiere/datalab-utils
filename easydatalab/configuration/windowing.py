#-*- coding: utf-8 -*-
from __future__ import print_function

import logging

from easydatalab.common.exceptions import ConfigurationError
from datetime import date, timedelta

class Windowing:

      def __init__(self, current_period,  window_length=4, nb_available_periods=36, nb_selected_periods=34, nb_staging_periods=2):
            # current_period is AAAAMM
            self.logger = logging.getLogger('configuration.Windowing')

            current_year = int(current_period[0:4])
            current_month = int(current_period[4:6])
            current_date = date(current_year, current_month, 15)

            window_days = window_length * 30
            window_delta = timedelta(days=window_days)

            available_days = nb_available_periods * 30
            available_delta = timedelta(days=available_days)
            self.min_available_date = (current_date - available_delta).strftime("%Y%m")
            self.max_available_date = current_period

            staging_days = nb_staging_periods * 30
            staging_delta = timedelta(days=staging_days)
            d = current_date - staging_delta
            self.max_selected_date = d.strftime("%Y%m")

            selected_days = nb_selected_periods * 30
            selected_delta = timedelta(days=selected_days)
            self.min_selected_date = (d - selected_delta).strftime("%Y%m")


      def available_periods(self):
          return ( self.min_available_date,  self.max_available_date )

      def selected_periods(self):
          return ( self.min_selected_date,self.max_selected_date)

