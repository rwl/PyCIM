# Copyright (C) 2010-2011 Richard Lincoln
# Copyright (C) 2011 Stefan Scherfke
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

import io
import unittest

from os.path import dirname, join

from PyCIM import cimread, RDFXMLReader

from CIM16 import nsURI as nsURICIM16, packageMap as packageMapCIM16
from CIM16.CDPSM.Asset import packageMap as assetMap
from CIM16.CDPSM.Connectivity import packageMap as connMap
from CIM16.CDPSM.Balanced import packageMap as equipMap
from CIM16.CDPSM.Geographical import packageMap as geoMap

RDFXML_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_COMBINED.xml")

EQUIP_FILE = join(dirname(__file__), "Case6_CSWRG_ES", "Case6_CSWRG_ES_EQ.xml")
TOPO_FIlE= join(dirname(__file__), "Case6_CSWRG_ES", "Case6_CSWRG_ES_TP.xml")
STATEV_FILE= join(dirname(__file__),"Case6_CSWRG_ES", "Case6_CSWRG_ES_SV.xml")

EMPTY_CIM = u'''<?xml version=\'1.0\'?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/2013/CIM-schema-cim16#"
xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" />'''


class RDFXMLReaderTestCase(unittest.TestCase):
    """Test CIM RDF/XML parsing.
    """

    def testCombined(self):
        """Test CIM RDF/XML parsing.
        """
        d = cimread(RDFXML_FILE)

        self.assertEqual(len(d), 5894)

    def test_cim_reads_are_independent(self):
#         cimread(ASSET_FILE, assetMap, nsURICIM15)
#         sio = io.StringIO(EMPTY_CIM)
#         empty_cim_dict = cimread(sio)
#         self.assertEqual(empty_cim_dict, {})
        pass

    def testProfile(self):
        d = {}

        d.update(cimread(EQUIP_FILE, assetMap, nsURICIM16))
        d.update(cimread(TOPO_FIlE, connMap, nsURICIM16))
        d.update(cimread(STATEV_FILE, equipMap, nsURICIM16))

        self.assertEqual(len(d), 5893)

    def testGetNamespaces(self):
        ns = RDFXMLReader.xmlns(EQUIP_FILE)
        self.assertEqual(ns, {
                'cim': 'http://iec.ch/TC57/2013/CIM-schema-cim16#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            })

        self.assertEqual(RDFXMLReader.get_rdf_ns(ns),
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#')

        self.assertEqual(RDFXMLReader.get_cim_ns(ns),
                (nsURICIM16, packageMapCIM16))


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    unittest.main()
