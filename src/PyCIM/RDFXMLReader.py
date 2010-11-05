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

from xml.etree.cElementTree import iterparse

from CIM14v13 import nsURI
from PyCIM.PackageMap.CIM14v13PackageMap import packageMap

from CPSM import nsURI as nsCPSM
from PyCIM.CPSMPackageMap import packageMap as CPSMPackageMap

from ENTSOE import nsURI as nsENTSOE
from PyCIM.ENTSOEPackageMap import packageMap as ENTSOEPackageMap

from CDPSM import nsURI as nsCDPSM
from PyCIM.CDPSMPackageMap import packageMap as CDPSMPackageMap

from Dynamics import nsURI as nsDynamics
from PyCIM.DynamicsPackageMap import packageMap as DynamicsPackageMap

logger = logging.getLogger(__name__)

PKG_MAP = {"CPSM": CPSMPackageMap, "ENTSO-E": ENTSOEPackageMap,
           "CDPSM": CDPSMPackageMap, "Dynamics": DynamicsPackageMap}
NS_MAP = {"CPSM": nsCPSM, "CDPSM": nsCDPSM, "Dynamics": nsDynamics,
          "ENTSO-E": nsENTSOE}

def cimread(file_or_filename, profile=None):
    """ CIM RDF/XML parser.

    @type file_or_filename: File-like-object or a path to a file.
    @param file_or_filename: CIM RDF/XML file.
    @type profile: string
    @param profile: CIM profile. If unspecified classes are imported from
    the full CIM package. Values are: CPSM, ENTSO-E, CDPSM, Dynamics.
    @rtype: dict
    @return: Map of URIs to CIM objects.

    @author: Richard Lincoln <r.w.lincoln@gmail.com>
    """
    nsURI = NS_MAP[profile] if profile is not None else nsURI
    packageMap = PKG_MAP[profile] if profile is not None else packageMap

    d = {}

    # get an iterable
    events = ("start", "end", "start-ns", "end-ns")
    context = iterparse(file_or_filename, events=events)

    # turn it into an iterator
    context = iter(context)

    # get the root element
    event, root = context.next()

    namespaces = []

    for event, elem in context:
        if event == "start-ns":
            namespaces.insert(0, elem)
        elif event == "end-ns":
            namespaces.pop(0)
        elif event == "end" and elem.tag == "record":
            #... process record elements ...
            pass

        root.clear()

    return d
