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

"""Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

from CIM15.CDPSM.Connectivity.IEC61970.Core.Terminal import Terminal
from CIM15.CDPSM.Connectivity.IEC61970.Core.Bay import Bay
from CIM15.CDPSM.Connectivity.IEC61970.Core.NameTypeAuthority import NameTypeAuthority
from CIM15.CDPSM.Connectivity.IEC61970.Core.VoltageLevel import VoltageLevel
from CIM15.CDPSM.Connectivity.IEC61970.Core.SubGeographicalRegion import SubGeographicalRegion
from CIM15.CDPSM.Connectivity.IEC61970.Core.PSRType import PSRType
from CIM15.CDPSM.Connectivity.IEC61970.Core.EquipmentContainer import EquipmentContainer
from CIM15.CDPSM.Connectivity.IEC61970.Core.ConductingEquipment import ConductingEquipment
from CIM15.CDPSM.Connectivity.IEC61970.Core.GeographicalRegion import GeographicalRegion
from CIM15.CDPSM.Connectivity.IEC61970.Core.NameType import NameType
from CIM15.CDPSM.Connectivity.IEC61970.Core.Equipment import Equipment
from CIM15.CDPSM.Connectivity.IEC61970.Core.IdentifiedObject import IdentifiedObject
from CIM15.CDPSM.Connectivity.IEC61970.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from CIM15.CDPSM.Connectivity.IEC61970.Core.Substation import Substation
from CIM15.CDPSM.Connectivity.IEC61970.Core.ConnectivityNode import ConnectivityNode
from CIM15.CDPSM.Connectivity.IEC61970.Core.Name import Name
from CIM15.CDPSM.Connectivity.IEC61970.Core.BaseVoltage import BaseVoltage
from CIM15.CDPSM.Connectivity.IEC61970.Core.PowerSystemResource import PowerSystemResource

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-13/CDPSM/Connectivity#Core"
nsPrefix = "cimCore"


class PhaseCode(str):
    """Values are: s12N, BN, BC, ABN, s2N, N, ACN, BCN, ABCN, AC, s1N, AN, B, AB, C, A, CN, ABC
    """
    pass
