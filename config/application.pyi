# This file was generated by Nuitka

# Stubs included by default
from __future__ import annotations
from masonite.environment import env

HASHING = {'default': env('HASHING_FUNCTION', 'bcrypt'), 'bcrypt': {'rounds': 10}, 'argon2': {'memory': 1024, 'threads': 2, 'time': 2}}

__name__ = ...



# Modules used internally, to allow implicit dependencies to be seen:
import masonite
import masonite.environment
import masonite.environment.env