__author__ = "Richard Lincoln"

from setuptools import setup, find_packages

setup(name="cim",
      description="Python implementation of the Common Information Model.",
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      url="http://rwl.github.com/cim",
      version="0.1.1",
      license="Apache 2.0",
      install_requires=["rdflib"],
      include_package_data=True,
      packages=find_packages(),
      zip_safe=False)
