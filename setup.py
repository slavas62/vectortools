import os
from distutils.core import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='vectortools',
    version='3.0.0',
    long_description=long_description,
    url='https://github.com/slavas62/vectortools/',
    packages=['vectortools', 'vectortools.django'],
    description='Tools for processing different vector formats',
    install_requires=[
        'cchardet',
        'GDAL>=1.7.0,<4.2.0',
    ],
)
