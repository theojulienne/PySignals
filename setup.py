from setuptools import setup, find_packages
import os

DESCRIPTION = "Signal dispatcher for Python, extracted from the Django framework."

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass


setup(name='pysignals',
      version='0.1',
      packages=find_packages(),
      author='Theo Julienne',
      author_email='theo.julienne@{nospam}gmail.com',
      url='https://github.com/theojulienne/PySignals',
      include_package_data=True,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      platforms=['any'],
)
