|travis| |pythons| |wheel|

============
Introduction
============

PyCIM is a Python implementation of the IEC Common Information Model.

Current features include:

- Support for IEC 61970 15v13 and IEC 61968 11v05,
- Legacy support for IEC 61970 14v15 and IEC 61968 10v31,
- Profiles of the CIM, including:
  - Common Power Systems Model (CPSM) (CIM v14)
  - Common Distribution Power System Model (CDPSM) (CIM v14 and v15)
  - European Network of Transmission System Operators for Electricity
  (ENTSO-E) (CIM v14),
- Class and attribute documentation integrated as Python doc-strings,
- Transparent bi-directional reference handling using Python properties,
- CIM RDF/XML parsing and serialisation according to IEC 61970-552.

Installation
------------

PyCIM has no dependencies beyond Python_ 2.6 or later. It can be easy_installed
using setuptools_::

  $ easy_install PyCIM

Alternatively, download and unpack the tarball and install::

  $ tar zxf PyCIM-XX.XX.tar.gz
  $ python setup.py install

On UNIX systems, use sudo for the latter command if you need to install the
scripts to a directory that requires root privileges::

  $ sudo python setup.py install

The development Git_ repository can be cloned from GitHub_::

  $ git clone https://github.com/rwl/PyCIM.git

Quick start
-----------

To parse a CIM RDF/XML file::

  In[1]: import logging

  In[2]: logging.basicConfig(level=logging.INFO)

  In[3]: from PyCIM import cimread

  In[4]: d = cimread('path/to/input_file.xml')
  INFO:PyCIM.RDFXMLReader:Created 5660 CIM objects in 1.04s.

The ``cimread`` function returns a Python dictionary that maps UUIDs to CIM
objects.  To serialise the dictionary of objects::

  In[5]: from PyCIM import cimwrite

  In[6]: cimwrite(d, 'path/to/output_file.xml')
  INFO:PyCIM.RDFXMLWriter:5660 CIM objects serialised in 1.14s.

For further information refer to the website_ and the `API documentation`_.

License
-------

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

Credits
-------

PyCIM is developed by Richard Lincoln (r.w.lincoln@gmail.com).

.. _Python: http://www.python.org/
.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools/
.. _Git: http://git-scm.com/
.. _GitHub: http://github.com/
.. _iPython: http://ipython.scipy.org
.. _`website`: http://www.pycim.com/
.. _`API documentation`: http://packages.python.org/PyCIM

.. more shields at http://shields.io
.. |travis| image:: https://travis-ci.org/rwl/PyCIM.svg?branch=master
    :target: https://travis-ci.org/rwl/PyCIM
.. |pythons| image:: https://img.shields.io/pypi/pyversions/PyCIM.svg
    :target: https://pypi.python.org/pypi/PyCIM
.. |wheel| image:: https://img.shields.io/pypi/format/PyCIM.svg
    :target: https://pypi.python.org/pypi/PyCIM
