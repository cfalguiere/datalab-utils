#-*- coding: utf-8 -*-
from __future__ import print_function

class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class ConfigurationError(Error):
    """Exception raised for errors in the configuration.

    Attributes:
        expr -- configuration item in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg

    def __str__(self):
        return 'error on {0} - {1}'.format( self.expr , self.msg )


class ExecutionError(Error):
    """Exception raised for errors during execution.

    Attributes:
        expr -- execution item in which the error occurred
        msg  -- explanation of the error
    """

    def __init__(self, step, msg):
        self.step = step
        self.msg = msg

    def __str__(self):
        return 'error in step {0} - {1}'.format( self.step , self.msg )

