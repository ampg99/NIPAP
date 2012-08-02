#!/usr/bin/env python

from distutils.core import setup

import nipap_cli

# This is a bloody hack to circumvent a lack of feature with Python distutils.
# Files specified in the data_files list cannot be renamed upon installation
# and we don't want to keep two copies of the .nipaprc file in git
import shutil
shutil.copyfile('nipaprc', '.nipaprc')

setup(
    name = 'nipap-cli',
    version = nipap_cli.__version__,
    description = "NIPAP shell command",
    long_description = "A shell command to interact with NIPAP.",
    author = nipap_cli.__author__,
    author_email = nipap_cli.__author_email__,
    license = nipap_cli.__license__,
    url = nipap_cli.__url__,
    packages = [ 'nipap_cli', ],
    keywords = ['nipap_cli', ],
    requires = ['pynipap', ],
    data_files = [
				('/etc/skel/', ['.nipaprc']),
				('/usr/bin/', ['helper-nipap', 'nipap']),
                ('/usr/share/doc/nipap-cli/', ['bash_complete', 'nipaprc'])
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Topic :: Internet'
    ]
)

# Remove the .nipaprc put the by the above hack.
import os
os.remove('.nipaprc')