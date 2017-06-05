from abc import ABCMeta, abstractmethod


class Rule:

    __metaclass__ = ABCMeta

    @abstractmethod
    def get_targets(self):
        raise NotImplementedError

    @abstractmethod
    def execute(self, target):
        raise NotImplementedError
