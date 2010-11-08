__author__ = "Richard Lincoln"

from setuptools import setup, find_packages

setup(name="PyCIM",
      description="Python implementation of the Common Information Model.",
      long_description = open('README').read().strip(),
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      url="http://rwl.github.com/PyCIM",
      version="14.15.1",
      license="GNU Lesser General Public License version 2.1",
      include_package_data=False,
      packages=find_packages(),
      zip_safe=True)
