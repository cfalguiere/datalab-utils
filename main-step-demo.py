#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Run Score Credit Habitat"""
from __future__ import print_function

import sys
from easydatalab.common.app import AppContext
from easydatalab.common.app import SkippedStepException
import logging

def main():
    """Main entry point for the script."""

    cfgFile = 'easydatalab/tests/resources/config/config_for_unittests.cfg'
    logCfgFile = 'easydatalab/resources/log_config.yml'

    with AppContext(log_config_file=logCfgFile) as appContext:
        appContext.logger.info("default logger for %s" % str( appContext) )
        appContext.skip_steps( [ 'skipped step' ] )

        with appContext.new_configuration(cfgFile) as appConfiguration:
            appConfiguration.show()

            with appContext.new_step ('something') as step:
                if step.enabled():
                    print("does something")

            with appContext.new_step ('skipped step') as step:
                if step.enabled():
                    print("does skipped")

            with appContext.new_step ('something else') as step:
                if step.enabled():
                    print("does something else")


if __name__ == '__main__':
    sys.exit(main())
