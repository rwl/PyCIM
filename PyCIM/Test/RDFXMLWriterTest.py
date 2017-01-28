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
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from PyCIM import cimread, cimwrite

from os.path import dirname, join


RDFXML_FILE = join(dirname(__file__), "Data", "EDF_AIGUE_v9_COMBINED.xml")


class RDFXMLWriterTestCase(unittest.TestCase):
    """Test CIM RDF/XML serialisation.
    """

    def testSerialise(self):
        """Test CIM RDF/XML serialisation.
        """
        d = cimread(RDFXML_FILE)

        output = StringIO()

        cimwrite(d, output)

        output.seek(0)
        dd = cimread(output)
        output.close()

        self.assertEqual(len(dd), 5894)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.INFO)
    unittest.main()
