#!/usr/bin/env python
import codecs
import os
import os.path
import re
import sys

extra = {}

if 'py2exe' in sys.argv:
    import py2exe
    from distutils.core import setup
    extra['console'] = ['batch_scoring.py']
else:
    py2exe = None
    from setuptools import setup

    install_requires = [
        "six>=1.9.0",
        "docopt>=0.6.1",
        "numpy>=1.8.0",
        "pandas>=0.15.1",
        ]
    if sys.version_info < (3, 0):
        install_requires.extend([
            "requests>=2.2.1",
            "gevent>=1.0.2",
            ])
    elif sys.version_info >= (3, 3):
        install_requires.extend([
            "aiohttp>=0.20.2",
            "chardet>=2.3.0",
            "python-dateutil>=2.4.2",
            "pytz>=2015.2",
            "requests>=2.7.0",
            ])
    else:
        print('Python version {} is not supported'.format(sys.version_info))
        sys.exit(1)
    extra['entry_points'] = {
        'console_scripts': [
            'batch_scoring = datarobot_batch_scoring.batch_scoring:main']}
    extra['install_requires'] = install_requires


fname = os.path.join(os.path.abspath(os.path.dirname(
    __file__)), 'datarobot_batch_scoring', '__init__.py')


with codecs.open(fname, 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


setup(
    name='datarobot_batch_scoring',
    version=version,
    description=("A script to support start/resume batch scoring "
                 "via Datarobot API."),
    author='DataRobot',
    author_email='support@datarobot.com',
    maintainer='DataRobot',
    maintainer_email='support@datarobot.com',
    license='BSD',
    url='http://www.datarobot.com/',
    packages=['datarobot_batch_scoring'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    **extra
)
