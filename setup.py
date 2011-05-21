import os
from setuptools import setup, find_packages

# Read the long description from the README.
thisdir = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(thisdir, "README"))
kwds = {"long_description": f.read()}
f.close()

setup(name="PyCIM",
      version="15.13.1",
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      description="Python implementation of the Common Information Model.",
      license="MIT",
      url="http://www.pycim.com/",
      include_package_data=False,
      packages=find_packages(),
      test_suite="PyCIM.Test",
      zip_safe=True,
      **kwds)

# python setup.py sdist bdist_egg bdist_wininst bdist_msi upload
