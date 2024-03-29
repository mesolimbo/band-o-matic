from abc import ABC, abstractmethod

from randomizer import util


class AbstractGenerator(ABC):
    util = util

    @abstractmethod
    def generate_name(self):
        pass

    @staticmethod
    def assemble_name(*args):
        pass
