__author__ = "Richard Lincoln (r.w.lincoln@gmail.com)"

import logging

from rdflib import Graph, RDF, Namespace, Literal

from cpsm_pkg_map import cpsm_pkg_map
#from ucte_pkg_map import ucte_pkg_map
#from cdpsm_pkg_map import cdpsm_pkg_map
#from dynamics_pkg_map import dynamics_pkg_map

from cpsm import ns_uri as ns_cpsm
#from ucte import ns_uri as ns_ucte
#from cdpsm import ns_uri as ns_cdpsm
#from dynamics import ns_uri as ns_dyn

logger = logging.getLogger(__name__)

PKG_MAP = {"cpsm": cpsm_pkg_map}#, "ucte": ucte_pkg_map, "cdpsm": cdpsm_pkg_map, "dynamics": dynamics_pkg_map}

NS_MAP = {"cpsm": ns_cpsm}#, "cdpsm": ns_cdpsm, "dynamics": ns_dyn, "ucte": ns_ucte}

def read(path, profile):
    """ Returns a dictionary of CIM objects.
    """
    ns = Namespace(NS_MAP[profile])
    urimap = PKG_MAP[profile]

    g = Graph()
    g.parse(path)

    result = {}

    for sub, obj in g.subject_objects(RDF.type):
        # sub = file:///path/to/instance.xml#_88f0288c16dc11deb60900059a3c7800
        # obj = http://iec.ch/TC57/2009/CIM-schema-cim14#PowerTransformer

        if urimap.has_key(obj):
            mod = urimap[obj]
            exec "import %s" % mod
            element = eval("%s.%s()" % (mod, obj))
        else:
            logger.error("Unknown class: %s" % obj)
            return

        urifrag = sub.rsplit("#", 1)[1]
        result[urifrag] = element

        if hasattr(element, "uri"):
            setattr(element, "uri", urifrag)

        for pred, obj2 in g.predicate_objects(sub):
            if (pred.defrag() == ns):
                if isinstance(obj2, Literal):
                    # pred = http://iec.ch/TC57/2009/CIM-schema-cim14#SynchronousMachine.x
                    # obj2 = 484.0
                    val = obj2.toPython()
                elif (obj2.defrag() == ns): # enumeration
                    # pred = http://iec.ch/TC57/2009/CIM-schema-cim14#SynchronousMachine.type
                    # obj2 = http://iec.ch/TC57/2009/CIM-schema-cim14#SynchronousMachineType.generator
                    val = obj2.rsplit(".", 1)[1]
                else:
                    continue # Set references in second pass.

                attr = pred.rsplit(".", 1)[1]
                if hasattr(element, attr):
                    setattr(element, attr, val)
                else:
                    logger.error("Unknown attr: %s (%s)" % (attr, obj))

    for sub, obj in g.subject_objects(RDF.type):
        urifrag = sub.rsplit("#", 1)[1]
        if result.has_key(urifrag):
            element = result[urifrag]
        else:
            logger.error("Element [%s] not found." % urifrag)
            continue

        for pred, obj2 in g.predicate_objects(sub):
            if (pred.defrag() == ns):
                for context in g.contexts():
                    if obj2.defrag() == context.defrag():
                        # pred = http://iec.ch/TC57/2009/CIM-schema-cim14#SynchronousMachine.MemberOf_GeneratingUnit
                        # obj2 = file:///path/to/instance.xml#_88f0284a16dc11deb60900059a3c7800
                        ref_frag = obj2.rsplit("#", 1)
                        if result.has_key(ref_frag):
                            ref_element = result[ref_frag]
                        else:
                            logger.error("Referenced element [%s] not found." %
                                         ref_frag)
                            continue

                        ref = pred.rsplit(".", 1)[1]
                        if hasattr(element, ref):
                            setattr(element, ref, ref_element)
                        else:
                            logger.error("Unknown ref: %s (%s)" % (ref, obj))
