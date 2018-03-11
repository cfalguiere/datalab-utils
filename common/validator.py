#-*- coding: utf-8 -*-
"""App commons"""

import os

class PathValidator:
    def __init__(self):
        self.errors = []

    def check_path_for_existence(self, path) :
        if not os.path.exists(path):
            msg = 'folder %s does not exist' % path
            self.errors.append(msg)
            return False
        else:
            return True

    def nb_errors(self) :
        return len(self.errors)

    def list_errors(self) :
        i=1
        print( self )
        for error in self.errors:
           print( '[{0}] {1}'.format( i, error) )

    def __str__(self):
        return 'Validation has detected {0} error(s)'.format( self.nb_errors() )
