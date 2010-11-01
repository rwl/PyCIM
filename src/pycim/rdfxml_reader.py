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

from cim15v01 import ns_uri
from pycim.cim15v01_pkg_map import pkg_map

from cpsm import ns_uri as ns_cpsm
from pycim.cpsm_pkg_map import pkg_map as cpsm_pkg_map

from entsoe import ns_uri as ns_ucte
from pycim.entsoe_pkg_map import pkg_map as entsoe_pkg_map

from cdpsm import ns_uri as ns_cdpsm
from pycim.cdpsm_pkg_map import pkg_map as cdpsm_pkg_map

from dynamics import ns_uri as ns_dyn
from pycim.dynamics_pkg_map import pkg_map as dynamics_pkg_map

logger = logging.getLogger(__name__)

PKG_MAP = {"cpsm": cpsm_pkg_map, "ucte": entsoe_pkg_map,
           "cdpsm": cdpsm_pkg_map, "dynamics": dynamics_pkg_map}
NS_MAP = {"cpsm": ns_cpsm, "cdpsm": ns_cdpsm, "dynamics": ns_dyn,
          "ucte": ns_ucte}

def cimread(file_or_filename, profile=None):
    """ CIM RDF/XML parser.

    @type file_or_filename: File-like-object or a path to a file.
    @param file_or_filename: CIM RDF/XML file.
    @type profile: string
    @param profile: CIM profile. If unspecified classes are imported from
    the full CIM package. Values are: cpsm, ucte, cdpsm, dynamics.
    @rtype: dict
    @return: Map of URIs to CIM objects.

    @author: Richard Lincoln <r.w.lincoln@gmail.com>
    """
    ns_uri = NS_MAP[profile] if profile is not None else ns_uri
    pkg_map = PKG_MAP[profile] if profile is not None else pkg_map

    d = {}
    iterparse

    return d
