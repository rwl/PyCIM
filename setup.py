__author__ = "Richard Lincoln"

from setuptools import setup, find_packages

setup(name="cim",
      description="Python implementation of the Common Information Model.",
      long_description = open('README').read().strip(),
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      url="http://rwl.github.com/cim",
      version="14.12a1",
      license="Apache License version 2.0",
#      include_package_data=True,
      packages=find_packages(),
      zip_safe=True)

