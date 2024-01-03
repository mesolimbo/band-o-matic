from randomizer import util

from abc import ABC, abstractmethod


class AbstractGenerator:
    util = util
    @abstractmethod
    def generate_name(self):
        pass
