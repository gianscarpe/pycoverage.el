# Copyright (c) 2009 Matt Harrison
#from distutils.core import setup
import re
from setuptools import setup

def get_attr(attr: str):
    version = re.search(  # type: ignore
        r'^__version__\s*=\s*"(.*)"',
        open("cov2emacslib/meta.py").read(),
        re.MULTILINE,
    ).group(1)
    return version

version = 0.1

setup(name='cov2emacs',
      version=version,
      description='FILL IN',
      scripts=['bin/cov2emacs'],
      package_dir={'cov2emacslib': 'cov2emacslib'},
      packages=['cov2emacslib'],
      install_requires=['coverage']
)
