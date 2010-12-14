import os
from setuptools import setup, find_packages

# Read the long description from the README.
thisdir = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(thisdir, "README"))
kwds = {"long_description": f.read()}
f.close()

setup(name="PyCIM",
      version="14.15.2",
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      description="Python implementation of the Common Information Model.",
      license="LGPL",
      url="http://github.com/rwl/PyCIM",
      include_package_data=False,
      packages=find_packages(),
      zip_safe=True,
      **kwds)
