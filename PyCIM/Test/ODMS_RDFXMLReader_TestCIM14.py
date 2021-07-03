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

from CIM14 import nsURI as nsURICIM14, packageMap as packageMapCIM14
from CIM14.CDPSM.Asset import packageMap as assetMap
from CIM14.CDPSM.Connectivity import packageMap as connMap
from CIM14.CDPSM.Balanced import packageMap as equipMap
#from CIM14.CDPSM.Geographical import packageMap as geoMap

RDFXML_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_COMBINED.xml")

EQUIP_FILE = join(dirname(__file__), "Case6_ODMS", "Case6_ODMS_EQ.xml")
TOPO_FIlE= join(dirname(__file__), "Case6_ODMS", "Case6_ODMS_TP.xml")
STATEV_FILE= join(dirname(__file__),"Case6_ODMS", "Case6_ODMS_SV.xml")

EMPTY_CIM = u'''<?xml version=\'1.0\'?>
<rdf:RDF xmlns:cim="http://iec.ch/TC57/2009/CIM-schema-cim14#"
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
        ''' This test needs to be documented
        What is the comparison with 5893? '''
        d = {}

        d.update(cimread(EQUIP_FILE, assetMap, nsURICIM14))
        d.update(cimread(TOPO_FIlE, connMap, nsURICIM14))
        d.update(cimread(STATEV_FILE, equipMap, nsURICIM14))

        self.assertEqual(len(d), 2303)

    def testGetNamespaces(self):
        ns = RDFXMLReader.xmlns(EQUIP_FILE)
        self.assertEqual(ns, {
                'cim': 'http://iec.ch/TC57/2009/CIM-schema-cim14#',
                'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                'pti': 'http://www.pti-us.com/PTI_CIM-schema-cim14#'
            })

        self.assertEqual(RDFXMLReader.get_rdf_ns(ns),
                'http://www.w3.org/1999/02/22-rdf-syntax-ns#')

        self.assertEqual(RDFXMLReader.get_pti_ns(ns),
                'http://www.pti-us.com/PTI_CIM-schema-cim14#')
        
        self.assertEqual(RDFXMLReader.get_cim_ns(ns),
                (nsURICIM14, packageMapCIM14))


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    unittest.main()
