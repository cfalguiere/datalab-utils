#-*- coding: utf-8 -*-
from __future__ import print_function

from sch.common.app import AppContext

class SCHAppContext(AppContext):

    def __init__(self):
          AppContext.__init__('SCH')
