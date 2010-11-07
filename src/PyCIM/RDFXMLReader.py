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

from xml.etree.cElementTree import iterparse

#from CIM14 import nsPrefix as cimPrefix
from CIM14 import nsURI as nsCIM
from CIM14 import packageMap as packageMapCIM

#from CPSM import nsURI as nsCPSM
#from PyCIM.CPSMPackageMap import packageMap as packageMapCPSM
#
#from ENTSOE import nsURI as nsENTSOE
#from PyCIM.ENTSOEPackageMap import packageMap as packageMapENTSOE
#
#from CDPSM import nsURI as nsCDPSM
#from PyCIM.CDPSMPackageMap import packageMap as packageMapCDPSM
#
#from Dynamics import nsURI as nsDynamics
#from PyCIM.DynamicsPackageMap import packageMap as packageMapDynamics

logger = logging.getLogger(__name__)

PKG_MAP = {
#    "CPSM": CPSMPackageMap, "ENTSO-E": ENTSOEPackageMap,
#    "CDPSM": CDPSMPackageMap, "Dynamics": DynamicsPackageMap
}

NS_MAP = {
#    "CPSM": nsCPSM, "CDPSM": nsCDPSM, "Dynamics": nsDynamics,
#    "ENTSO-E": nsENTSOE
}

# TODO: Extract RDF namespace from file.
NS_RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

def cimread(source, profile=None):
    """ CIM RDF/XML parser.

    @type source: File-like object or a path to a file.
    @param source: CIM RDF/XML file.
    @type profile: string
    @param profile: CIM profile. If unspecified classes are imported from
    the full CIM package. Values are: CPSM, ENTSO-E, CDPSM, Dynamics.
    @rtype: dict
    @return: Map of URI to CIM object.

    @author: Richard Lincoln <r.w.lincoln@gmail.com>
    """
    # Start the clock.
    t0 = time()

    # Default to the latest CIM version if no profile is specified.
    nsURI = NS_MAP[profile] if profile is not None else nsCIM

    # All CIM classes are under the one namespace, but are arranged into
    # sub-packages so we need a map from class name to package.
    packageMap = PKG_MAP[profile] if profile is not None else packageMapCIM

    # A map of URIs to CIM objects to be returned.
    d = {}

    # CIM element tag base (e.g. {http://iec.ch/TC57/2009/CIM-schema-cim14#}).
    base = "{%s#}" % nsURI
    # Length of element tag base.
    m = len(base)

    ## First pass instantiates the classes.
    context = iterparse(source, ("start", "end"))

    # Turn it into an iterator (required for cElementTree).
    context = iter(context)

    # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
    _, root = context.next()

    for event, elem in context:
        # Process elements in the CIM namespace.
        if event == "end" and elem.tag[:m] == base:
#            print elem.tag[m:], elem.get("{%s}ID" % NS_RDF), elem.get("{%s}resource" % NS_RDF)

            # Unique resource identifier for the CIM object.
            uri = elem.get("{%s}ID" % NS_RDF)
            if uri != None: # class
                # Element tag without namespace (e.g. VoltageLevel).
                tag = elem.tag[m:]
                try:
                    mname = packageMap[tag]
                except KeyError:
                    logger.error("Unable to locate module for: %s (%s)", tag, uri)
                    root.clear()
                    continue
                # Import the module for the CIM object.
                module = __import__(mname, globals(), locals(), [tag], 0)
                # Get the CIM class from the module.
                klass = getattr(module, tag)

#                print "PKG:", tag, klass
                # Instantiate the class and map it to the URI.
                d[uri] = klass()

        # Clear child elements to reduce memory usage.
        root.clear()


    ## Second pass sets attributes and references.
    context = iter( iterparse(source, ("start", "end")) )

    _, root = context.next()

    for event, elem in context:

        if event == "start" and elem.tag[:m] == base:
            uri = elem.get("{%s}ID" % NS_RDF)
            if uri != None:
                # Locate the CIM object using the URI.
                try:
                    obj = d[uri]
                except KeyError:
                    logger.error("Missing '%s' object with URI: %s", elem.tag[m:], uri)
                    root.clear()
                    continue

                # Iterate over attributes/references.
                for event, elem in context:
                    # Process end events with elements in the CIM namespace.
                    if event == "end" and elem.tag[:m] == base:
                        # Break if class closing element (e.g. </cim:Terminal>).
                        if elem.get("{%s}ID" % NS_RDF) == None:
                            # Get the attribute/reference name.
                            attr = elem.tag[m:].rsplit(".")[1]

                            if not hasattr(obj, attr):
                                logger.error("'%s' has not attribute '%s'",
                                             obj.__class__.__name__, attr)
                                continue

                            # Use the rdf:resource attribute to distinguish
                            # between attributes and references/enums.
                            uri2 = elem.get("{%s}resource" % NS_RDF)

                            if uri2 == None: # attribute
                                # Convert value type using the default value.
                                typ = type( getattr(obj, attr) )
                                setattr(obj, attr, typ(elem.text))
                            else: # reference or enum
                                # Use the '#' prefix to distinguish between
                                # references and enumerations.
                                if uri2[0] == "#": # reference
                                    try:
                                        val = d[uri2[1:]] # remove '#' prefix
                                    except KeyError:
                                        logger.error("Referenced '%s' [%s] object missing.",
                                                     obj.__class__.__name__, uri2[1:])
                                        continue

                                    default = getattr(obj, attr)
                                    if default == None: # 1..1 or 1..n
                                        # Rely on property to set any
                                        # bi-directional references.
                                        setattr(obj, attr, val)
                                    elif isinstance(default, list): # n..1 or n..n
                                        # Use the 'add...' method to set reference.
                                        getattr(obj, ("add%s" % attr))(val)

                                    else:
#                                        logger.error("Unrecognised reference type [%s].", default)
                                        pass

                                else: # enum
                                    # http://iec.ch/TC57/2009/CIM-schema-cim14#RegulatingControlModeKind.voltage
                                    val = uri2.rsplit(".")[1]
                                    setattr(obj, attr, val)

                        else:
                            # Finished setting object attributes.
                            break

        root.clear()

    logger.info("Created %d CIM objects in %.3f seconds.", len(d), time() - t0)

    return d


def xmlns(source):
    """Returns a map of prefix to namespace for the given XML file.
    """
    namespaces = {}
    events=("end", "start-ns", "end-ns")
    for (event, elem) in iterparse(source, events):
        if event == "start-ns":
            prefix, ns = elem
            namespaces[prefix] = ns
        elif event == "end":
            break
    return namespaces


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    cimread("Test/Data/EDF_AIGUE_v9.xml")
