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

        mro = obj.__class__.mro()
        mro.reverse()

        # Serialise attributes.
        for klass in mro[2:]: # skip 'object' and 'Element'
            attrs = [a for a in klass._attrs if a not in klass._enums]
            for attr in attrs:
                val = getattr(obj, attr)
                if val != klass._defaults[attr]:
                    w.element(u"%s:%s.%s" % (nsPrefix, klass.__name__, attr),
                              str(val))

        # Serialise enumeration data-types.
        for klass in mro[2:]: # skip 'object' and 'Element'
            enums = [a for a in klass._attrs if a in klass._enums]
            for enum in enums:
                val = getattr(obj, enum)
                dt = klass._enums[enum]
                w.element(u"%s:%s.%s" % (nsPrefix, klass.__name__, enum),
                          attrib={u"%s:resource" % nsPrefixRDF:
                                  u"%s%s.%s" % (nsCIM, dt, val)})

        # Serialise references.
        for klass in mro[2:]: # skip 'object' and 'Element'
            # FIXME: serialise 'many' references.
            refs = [r for r in klass._refs if r not in klass._many_refs]
            for ref in refs:
                val = getattr(obj, ref)
                if val is not None:
                    w.element(u"%s:%s.%s" % (nsPrefix, klass.__name__, ref),
                          attrib={u"%s:resource" % nsPrefixRDF:
                                  u"#%s" % obj.UUID})

        w.end()

    # Close the root RDF element.
    w.close(rdf)

    # Flush the output stream.
    w.flush()

    logger.info("%d CIM objects serialised in %.2fs.", len(d), time() - t0)


if __name__ == "__main__":
    from RDFXMLReader import cimread
    from PrettyPrintXML import xmlpp

    logging.basicConfig(level=logging.INFO)

    d = cimread("Test/Data/EDF_AIGUE_v9.xml")
#    d = cimread("Test/Data/ENTSOE_16_BE_EQ.xml")
    tmp = "/tmp/cimwrite.xml"
    cimwrite(d, tmp)

    print xmlpp(tmp)
