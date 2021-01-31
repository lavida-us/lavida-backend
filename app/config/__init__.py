from importlib import import_module
from os import environ

phase = environ.get('LAVIDA_PHASE', 'dev')

globals().update(import_module(f'.{phase}', 'app.config').__dict__)