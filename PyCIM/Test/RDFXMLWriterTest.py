# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

import sys
import unittest

from PyCIM import cimread, cimwrite

from os.path import dirname, join

RDFXML_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9.xml")

class RDFXMLWriterTestCase(unittest.TestCase):
    """Test CIM RDF/XML serialisation.
    """

    def setUp(self):
        """The test runner will execute this method prior to each test.
        """
        pass


    def testSerialise(self):
        """Test CIM RDF/XML serialisation.
        """
        d = cimread(RDFXML_FILE)

        cimwrite(d, sys.stdout)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    unittest.main()
