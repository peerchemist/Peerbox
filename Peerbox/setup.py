from setuptools import setup

setup(name='peerbox',
      version='0.5.5',
      description='Peerbox control scripts',
      url='https://github.com/peerchemist/Peerbox',
      author='Peerchemist',
      author_email='peerchemist@protonmail.ch',
      license='GLP',
      packages=['peerbox'],
      install_requires=["requests", "sh"],
      scripts=['bin/peerbox'],
      zip_safe=False)
