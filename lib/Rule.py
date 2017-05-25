from abc import ABCMeta, abstractmethod


class Rule(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_targets(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self, target):
        raise NotImplementedError
