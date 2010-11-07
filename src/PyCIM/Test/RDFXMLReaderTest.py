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

import unittest

from PyCIM import cimread

from os.path import dirname, join

RDFXML_FILE = join(dirname(__file__), "Data", "UCTE10P_EQ_r3.xml")

class RDFXMLReaderTestCase(unittest.TestCase):
    """Test CIM RDF/XML parsing.
    """

    def setUp(self):
        """The test runner will execute this method prior to each test.
        """
        pass


    def testParse(self):
        """Test CIM RDF/XML parsing.
        """
        d = cimread(RDFXML_FILE)

        print "Created %d CIM element(s)." % len(d)

if __name__ == "__main__":
    unittest.main()
