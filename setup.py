"""Setup for DroneQuest app."""
from setuptools import setup, find_packages

REQUIRES = [
    'django',
    'djangorestframework'
]
TEST = [
    'tox',
    'coverage',
]
DEV = [
    'ipython',
]


setup(name='Qwergram API',
      version='0.0',
      description='An API for qwergram.github.io',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Norton Pengra',
      author_email='npengra317@gmail.com',
      url='qwergram.github.io',
      keywords='python API',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='dronequest',
      install_requires=REQUIRES,
      extras_require={
          'test': TEST,
          'dev': DEV
      },
      )
