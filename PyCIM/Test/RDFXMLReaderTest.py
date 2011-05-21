# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import unittest

from os.path import dirname, join

from PyCIM import cimread

from CIM15.CDPSM.Asset import packageMap as assetMap
from CIM15.CDPSM.Connectivity import packageMap as connMap
from CIM15.CDPSM.Balanced import packageMap as equipMap
from CIM15.CDPSM.Geographical import packageMap as geoMap


RDFXML_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_COMBINED.xml")

ASSET_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_ASSET.xml")
CONN_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_CONN.xml")
EQUIP_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_EQUIP.xml")
GEO_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_GEO.xml")


class RDFXMLReaderTestCase(unittest.TestCase):
    """Test CIM RDF/XML parsing.
    """

    def testCombined(self):
        """Test CIM RDF/XML parsing.
        """
        d = cimread(RDFXML_FILE)

        self.assertEqual(len(d), 5894)

    def testProfile(self):
        d = {}

        d.update(cimread(ASSET_FILE, assetMap))
        d.update(cimread(CONN_FILE, connMap))
        d.update(cimread(EQUIP_FILE, equipMap))
        d.update(cimread(GEO_FILE, geoMap))

        self.assertEqual(len(d), 5894)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    unittest.main()
