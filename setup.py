import os
from distutils.core import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='vectortools',
    version='0.0.6',
    long_description=long_description,
    url='https://bitbucket.org/slavas/vectortools/',
    packages=['vectortools', 'vectortools.django'],
    description='Tools for processing different vector formats',
    install_requires=[
        'cchardet',
        'GDAL==3.0.4',
    ],
)
