#-*- coding: utf-8 -*-
from __future__ import print_function

import os

class Validator:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def nb_errors(self) :
        return len(self.errors)

    def nb_warnings(self) :
        return len(self.warnings)

    def list_errors(self) :
        print( '-----------------------------------------------------------')
        print( '| ')
        print( '| ERRORS')
        print( '| ')
        i=1
        print( self )
        for error in self.errors:
           print( '| [{0}] {1}'.format( i, error) )
        print( '-----------------------------------------------------------')

    def list_warnings(self) :
        print( '-----------------------------------------------------------')
        print( '| ')
        print( '| ERRORS')
        print( '| ')
        i=1
        print( self )
        for warning in self.warnings:
           print( '| [{0}] {1}'.format( i, warning) )
        print( '-----------------------------------------------------------')

    def __str__(self):
        template = 'Validation has detected {0} error(s) and {1} warning(s)'
        return template.format( self.nb_errors(), self.nb_warnings() )

class PathValidator(Validator):
    def check_path_for_existence(self, path) :
        if not os.path.exists(path):
            msg = 'folder %s does not exist' % path
            self.errors.append(msg)
            return False
        else:
            return True
