#!/usr/bin/python
#-*- coding: utf-8 -*-
"""Run Score Credit Habitat"""
from __future__ import print_function

import sys
from easydatalab.common.app import AppContext

def main():
    """Main entry point for the script."""

    cfgFile = 'easydatalab/tests/resources/config_for_unittests.cfg'

    with AppContext() as appContext:
        with appContext.new_configuration(cfgFile) as appConfiguration:
            appConfiguration.show()

            with appContext.new_step ('something') as step:
                 print("does something")

            with appContext.new_step ('something else') as step:
                 print("does something else")


if __name__ == '__main__':
    sys.exit(main())
