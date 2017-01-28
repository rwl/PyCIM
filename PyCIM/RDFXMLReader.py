# Copyright (C) 2010-2011 Richard Lincoln
# Copyright (C) 2011 Stefan Scherfke
# Copyright (C) 2015 Wouter Labeeuw
# Copyright (C) 2016 Konstantin Krumov Gerasimov, KKG - kkgerasimov@gmail.com
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

from xml.etree.cElementTree import iterparse
from time import time

import logging
logger = logging.getLogger(__name__)


def cimread(source, packageMap=None, nsURI=None, start_dict=None):
    """ CIM RDF/XML parser.

    @type source: File-like object or a path to a file.
    @param source: CIM RDF/XML file.
    @type profile: dict
    @param packageMap: Map of class name to PyCIM package name. All CIM
    classes are under the one namespace, but are arranged into sub-packages
    so a map from class name to package name is required. Defaults to the
    latest CIM version, but may be set to a map from a profile to return
    a profile model.
    @type profile: string
    @param nsURI: CIM namespace URI used in the RDF/XML file. For example:
    http://iec.ch/TC57/2010/CIM-schema-cim15
    @rtype: dict
    @return: Map of UUID to CIM object.

    @author: Richard Lincoln <r.w.lincoln@gmail.com>
    """
    # Start the clock.
    t0 = time()

    #logger.info('##########################################################################')
    logger.info('START of parsing file \"%s\"', source)
    logger_errors_grouped = {}

    # A map of uuids to CIM objects to be returned.
    d = start_dict if start_dict is not None else {}

    # Obtain the namespaces from the input file
    namespaces = xmlns(source)
    ns_rdf = get_rdf_ns(namespaces)
    if bool(nsURI) != bool(packageMap):
        raise ValueError(
                'Either pass "packageMap" AND "nsURI" or none of them.')
    elif (nsURI is None) and (packageMap is None):
        nsURI, packageMap = get_cim_ns(namespaces)

    # CIM element tag base (e.g. {http://iec.ch/TC57/2009/CIM-schema-cim14#}).
    base = "{%s#}" % nsURI
    # Length of element tag base.
    m = len(base)

    # First pass instantiates the classes.
    context = iterparse(source, ("start", "end"))

    # Turn it into an iterator (required for cElementTree).
    context = iter(context)

    # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
    _, root = next(context)

    for event, elem in context:
        # Process 'end' elements in the CIM namespace.
        if event == "end" and elem.tag[:m] == base:

            # Unique resource identifier for the CIM object.
            uuid = elem.get("{%s}ID" % ns_rdf)
            if uuid is not None: # class
                # Element tag without namespace (e.g. VoltageLevel).
                tag = elem.tag[m:]
                try:
                    mname = packageMap[tag]
                except KeyError:
                    logger.error("Unable to locate module for: %s (%s)",
                                 tag, uuid)
                    root.clear()
                    continue
                # Import the module for the CIM object.
                module = __import__(mname, globals(), locals(), [tag], 0)
                # Get the CIM class from the module.
                klass = getattr(module, tag)

                # Instantiate the class and map it to the uuid.
                d[uuid] = klass(UUID=uuid)

        # Clear children of the root element to minimise memory usage.
        root.clear()

    # Reset stream
    if hasattr(source, "seek"):
        source.seek(0)

    ## Second pass sets attributes and references.
    context = iter( iterparse(source, ("start", "end")) )

    # Get the root element ({http://www.w3.org/1999/02/22-rdf-syntax-ns#}RDF).
    _, root = next(context)

    for event, elem in context:
        # Process 'start' elements in the CIM namespace.
        if event == "start" and elem.tag[:m] == base:
            uuid = elem.get("{%s}ID" % ns_rdf)
            if uuid is None:
                uuid = elem.get("{%s}about" % ns_rdf)
                if uuid is not None:
                    uuid = uuid[1:]
            if uuid is not None:
                # Locate the CIM object using the uuid.
                try:
                    obj = d[uuid]
                except KeyError:
                    logger.error("Missing '%s' object with uuid: %s",
                                 elem.tag[m:], uuid)
                    root.clear()
                    continue

                # Iterate over attributes/references.
                for event, elem in context:
                    # Process end events with elements in the CIM namespace.
                    if event == "end" and elem.tag[:m] == base:
                        # Break if class closing element (e.g. </cim:Terminal>).
                        if elem.get("{%s}ID" % ns_rdf) is None and \
                                elem.get("{%s}about" % ns_rdf) is None:
                            # Get the attribute/reference name.
                            attr = elem.tag[m:].rsplit(".")[-1]

                            if not hasattr(obj, attr):
                                error_msg = "'%s' has not attribute '%s'" %(obj.__class__.__name__, attr)
                                try:
                                    logger_errors_grouped[error_msg] += 1
                                except KeyError:
                                    logger_errors_grouped[error_msg] = 1
                                # logger.error("'%s' has not attribute '%s'",
                                #              obj.__class__.__name__, attr)
                                continue

                            # Use the rdf:resource attribute to distinguish
                            # between attributes and references/enums.
                            uuid2 = elem.get("{%s}resource" % ns_rdf)

                            if uuid2 is None: # attribute
                                # Convert value type using the default value.
                                try:
                                    typ = type( getattr(obj, attr) )
                                    if typ == type(True): # KKG: Test if it is boolean value
                                        # KKG: NB: The function bool("false") returns True, because it is called upon non-empty string!
                                        # This means that it wrongly reads "false" value as boolean True and this is why this special case testing is necessary
                                        if str.title(elem.text) == 'True':
                                            setattr(obj, attr, True)
                                        else:
                                            setattr(obj, attr, False)
                                    else:
                                        setattr(obj, attr, typ(elem.text))
                                except TypeError:
                                    pass
                            else:  # reference or enum
                                # Use the '#' prefix to distinguish between
                                # references and enumerations.
                                if uuid2[0] == "#": # reference
                                    try:
                                        val = d[uuid2[1:]] # remove '#' prefix
                                    except KeyError:
                                        logger.error("Referenced '%s' [%s] "
                                                     "object missing.",
                                                     obj.__class__.__name__,
                                                     uuid2[1:])
                                        continue

                                    default = getattr(obj, attr)
                                    if default == None: # 1..1 or 1..n
                                        # Rely on properties to set any
                                        # bi-directional references.
                                        setattr(obj, attr, val)
                                    elif isinstance(default, list): # many
                                        # Use 'add*' method to set reference.
                                        getattr(obj, ("add%s" % attr))(val)
#                                    else:
#                                        logger.error("Reference error [%s].",
#                                                     default)

                                else: # enum
                                    val = uuid2.rsplit(".", 1)[1]
                                    setattr(obj, attr, val)

                        else:
                            # Finished setting object attributes.
                            break

        # Clear children of the root element to minimise memory usage.
        root.clear()

    if logger_errors_grouped:
        for error, count in logger_errors_grouped.items():
            logging_message = '%s : %d times' %(error, count)
            logger.warn(logging_message)

    # logging_message = 'Created totally %d CIM objects in %.2fs.' %(len(d), time() - t0)
    logger.info('Created totally %d CIM objects in %.2fs.' %(len(d), time() - t0))
    # logging_message = 'END of parsing file \"%s\"\n' % source
    logger.info('END of parsing file \"%s\"\n' % source)

    return d


def xmlns(source):
    """
    Returns a map of prefix to namespace for the given XML file.

    """
    namespaces = {}
    events=("end", "start-ns", "end-ns")
    for (event, elem) in iterparse(source, events):
        if event == "start-ns":
            prefix, ns = elem
            namespaces[prefix] = ns
        elif event == "end":
            break

    # Reset stream
    if hasattr(source, "seek"):
        source.seek(0)

    return namespaces


def get_rdf_ns(namespaces):
    try:
        ns = namespaces['rdf']
    except KeyError:
        ns = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
        logger.warn('No rdf namespace found. Using %s' % ns)

    return ns


def get_cim_ns(namespaces):
    """
    Tries to obtain the CIM version from the given map of namespaces and
    returns the appropriate *nsURI* and *packageMap*.

    """
    try:
        ns = namespaces['cim']
        if ns.endswith('#'):
            ns = ns[:-1]
    except KeyError:
        ns = ''
        logger.error('No CIM namespace defined in input file.')

    CIM16nsURI = 'http://iec.ch/TC57/2013/CIM-schema-cim16'

    nsuri = ns

    import CIM14, CIM15
    if ns == CIM14.nsURI:
        ns = 'CIM14'
    elif ns == CIM15.nsURI:
        ns = 'CIM15'
    elif ns == CIM16nsURI:
        ns  = 'CIM15'
    else:
        ns = 'CIM15'
        logger.warn('Could not detect CIM version. Using %s.' % ns)

    cim = __import__(ns, globals(), locals(), ['nsURI', 'packageMap'])

    return nsuri, cim.packageMap


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    cimread("Test/Data/EDF_AIGUE_v9_COMBINED.xml")
