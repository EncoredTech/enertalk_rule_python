#!/usr/bin/env python

import os
import sys
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'enertalk_rule'
]

requires = []

test_requires = []

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='enertalk_rule_python',
    version='0.1.0',
    description='EnerTalk\'s public interface library for EnerTalk Rule.,
    long_description=readme + '\n\n' + history,
    author='Encored developers',
    author_email='edev@encoredtech.com',
    url='http://www.encoredtech.com',
    packages=packages,
    package_dir={'enertalk_rule': 'lib'},
    setup_requires=requires,
    include_package_data=True,
    install_requires=requires,
    tests_require=test_requires,
    license='Apache License 2.0',
    zip_safe=False,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7'
    ),
)
