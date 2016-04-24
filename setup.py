#!/usr/bin/env python
from distutils.core import setup
from os.path import dirname, abspath, join

_src_dir = dirname(abspath(__file__))
with open(join(_src_dir, 'requirements.txt')) as _requirements_file:
    requirements = [line.strip() for line in _requirements_file if line.strip()]

with open(join(_src_dir, 'README.md')) as _readme_file:
    long_description = _readme_file.read()

setup(name='toggl-cli',
      version='0.1',
      py_modules=['toggl'],
      requirements=requirements,
      license='MIT License',
      description='toggl-cli is a command-line interface for toggl.com',
      long_description=long_description,
      url='https://github.com/drobertadams/toggl-cli',
      author='Robert Adams',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
      ],
      )
