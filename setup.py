from distutils.core import setup
from setuptools import find_packages

setup(name='let_it_snow',
      version='0.1',
      author='Amin in DSSS',
      author_email='amin.olamazadeh@fau.de',
      packages=find_packages(),
      install_requires = ['numpy','turtles']
     )