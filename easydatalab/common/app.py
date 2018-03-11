#-*- coding: utf-8 -*-
"""App commons"""
from __future__ import print_function


class AppContext:
    def __init__(self, name='App'):
        self.name = name
        self.status = -1
        #self.attributes = {}
        self.configuration = None
        self.steps = []

    def __str__(self):
        return self.name

    def get_status(self):
        return self.status

    def set_configuration(self, configuration):
        self.configuration = configuration
