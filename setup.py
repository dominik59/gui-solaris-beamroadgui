#!/usr/local/bin/python2.7
from distutils.core import setup
 
setup(
    name = 'taurusGui-BeamRoadGui',
    version = '1.0.0',
    description = 'Tango Gui for viewing Valves, YagScreens and Scarpers.',
    author='Dominik Pawlik',
    author_email='osemka59@gmail.com',
    packages = ['beamroad'],
    package_dir = {'beamroad' : 'beamroad'})
