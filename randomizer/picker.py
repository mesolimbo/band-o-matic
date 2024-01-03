import importlib
import inspect
import pkgutil
import random

from randomizer import generators


def is_valid_generator(name):
    match name:
        case 'AbstractGenerator':
            return False
        case _ if name.startswith('Test'):
            return False
    return True


GENERATORS = []
"""Iterate through each module in the generators package and instantiate all concrete classes"""
for loader, name, is_pkg in pkgutil.iter_modules(path=generators.__path__):
    module = importlib.import_module('.' + name, 'randomizer.generators')
    for name, value in inspect.getmembers(module):
        if inspect.isclass(value) \
                and value.__module__ == module.__name__ \
                and is_valid_generator(name):
            GENERATORS.append(value())


def generate_band_name():
    # Logic to generate a band name
    return random.choice(GENERATORS).generate_name()
