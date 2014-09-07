__author__ = 'satish goda'

import os

class Path(object):
    def __init__(self, path):
        self.__path = path

    @property
    def basename(self):
        return os.path.basename(self.__path)

    @property
    def dirname(self):
        return os.path.dirname(self.__path)
