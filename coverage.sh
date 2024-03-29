#!/bin/bash
coverage run --omit='*/tests.py,*/test_*.py' manage.py test --parallel --shuffle
coverage report -m
