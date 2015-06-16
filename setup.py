import os
from setuptools import setup

abspathconfig = '/etc/ee/plugins.d'
abspathplugins = '/usr/lib/ee/plugins'

if not os.path.exists(abspathconfig):
    os.makedirs(abspathconfig)

if not os.path.exists(abspathplugins):
    os.makedirs(abspathplugins)


setup(name='Demo_Plugine',
      version='0.1',
      description='Demo_Plugine',
      url='http://github.com/shitalp',
      author='shitalp',
      author_email='shital.patil@rtcamp.com',
      license='MIT',
      data_files=[(abspathconfig, ['testplugin/monit.conf']),
                  (abspathplugins, ['testplugin/monit.py'])],
      # packages=['cli'],
      install_requires=[
          'ee',
      ],

      zip_safe=False)
