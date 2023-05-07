from setuptools import setup, find_packages
import codecs
import os
from datetime import datetime

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
# Edit the NAME:
NAME = ''
VERSION = '0.0.1'
DESCRIPTION = 'Collect Restaurant attendees information'
LONG_DESCRIPTION = long_description if long_description else DESCRIPTION

# it generate a package name if you do not specify the NAME 
PACKGE_NAME = NAME if NAME else f'my-first-packge-{datetime.now().strftime("%Y%m%d-%H%M%S")}'

# Setting up
setup(
    name=PACKGE_NAME,
    version=VERSION,
    author="<your name>",
    author_email="<your_email@msn.com>",
    url='https://github.com/odoo-app-dev/pypi-package-creation'
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[  'colorama',
                      ],
    python_requires='>=3.7',
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
