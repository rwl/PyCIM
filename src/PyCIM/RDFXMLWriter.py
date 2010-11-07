# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

import logging

from time import time

from CIM14 import nsURI, nsPrefix

from PyCIM.SimpleXMLWriter import XMLWriter

nsPrefixRDF = "rdf"
nsRDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

logger = logging.getLogger(__name__)

def cimwrite(d, source, encoding="utf-8"):
    """CIM RDF/XML serializer.

    @type d: dict
    @param d: Map of URIs to CIM objects.
    @type source: File or file-like object.
    @param source: This object must implement a C{write} method
    that takes an 8-bit string.
    @type encoding: string
    @param encoding: Character encoding defaults to "utf-8", but can also
    be set to "us-ascii".
    @rtype: bool
    @return: Write success.
    """
    # Start the clock
    t0 = time()

    w = XMLWriter(source, encoding)

    # Write the XML declaration.
    w.declaration()

    # Add a '#' suffix to the CIM namespace URI if not present.
    nsCIM = nsURI if nsURI[-1] == "#" else nsURI + "#"

    # Start the root RDF element and declare namespaces.
    xmlns = {u"xmlns:%s" % nsPrefixRDF: nsRDF, u"xmlns:%s" % nsPrefix: nsCIM}
    rdf = w.start(u"%s:RDF" % nsPrefixRDF, xmlns)

    # Iterate over all UUID, CIM object pairs in the given dictionary.
    for uuid, obj in d.iteritems():
        w.start(u"%s:%s" % (nsPrefix, obj.__class__.__name__),
                {u"%s:ID" % nsPrefixRDF: uuid})
        w.end()

    # Close the root RDF element.
    w.close(rdf)

    # Flush the output stream.
    w.flush()

    logger.info("%d CIM objects serialised in %.2fs.", len(d), time() - t0)


if __name__ == "__main__":
    import sys
    import xmlpp # XML pretty printing by Fredrik Ekholdt.
    from RDFXMLReader import cimread

    logging.basicConfig(level=logging.INFO)

    d = cimread("Test/Data/EDF_AIGUE_v9.xml")
    tmp = "/tmp/cimwrite.xml"
    cimwrite(d, tmp)

    fd = open(tmp, "r")
    xmlpp.pprint(fd.read(), output=sys.stdout)
    fd.close()
