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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource
from CIM15.IEC61970.Core.NameTypeAuthority import NameTypeAuthority
from CIM15.IEC61970.Core.Equipment import Equipment
from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment
from CIM15.IEC61970.Core.RegularTimePoint import RegularTimePoint
from CIM15.IEC61970.Core.ConnectivityNode import ConnectivityNode
from CIM15.IEC61970.Core.PSRType import PSRType
from CIM15.IEC61970.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from CIM15.IEC61970.Core.Bay import Bay
from CIM15.IEC61970.Core.EquipmentContainer import EquipmentContainer
from CIM15.IEC61970.Core.ReportingGroup import ReportingGroup
from CIM15.IEC61970.Core.BasePower import BasePower
from CIM15.IEC61970.Core.PsrList import PsrList
from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject
from CIM15.IEC61970.Core.BasicIntervalSchedule import BasicIntervalSchedule
from CIM15.IEC61970.Core.Curve import Curve
from CIM15.IEC61970.Core.GeographicalRegion import GeographicalRegion
from CIM15.IEC61970.Core.CurveData import CurveData
from CIM15.IEC61970.Core.SubGeographicalRegion import SubGeographicalRegion
from CIM15.IEC61970.Core.NameType import NameType
from CIM15.IEC61970.Core.Substation import Substation
from CIM15.IEC61970.Core.Name import Name
from CIM15.IEC61970.Core.BaseVoltage import BaseVoltage
from CIM15.IEC61970.Core.Terminal import Terminal
from CIM15.IEC61970.Core.IrregularIntervalSchedule import IrregularIntervalSchedule
from CIM15.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule
from CIM15.IEC61970.Core.OperatingParticipant import OperatingParticipant
from CIM15.IEC61970.Core.OperatingShare import OperatingShare
from CIM15.IEC61970.Core.VoltageLevel import VoltageLevel
from CIM15.IEC61970.Core.ReportingSuperGroup import ReportingSuperGroup
from CIM15.IEC61970.Core.IrregularTimePoint import IrregularTimePoint

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Core"
nsPrefix = "cimCore"


class BreakerConfiguration(str):
    """Values are: breakerAndAHalf, noBreaker, singleBreaker, doubleBreaker
    """
    pass

class CompanyType(str):
    """Values are: municipal, isPrivate, pool
    """
    pass

class PhaseCode(str):
    """Values are: s12N, BN, BC, ABN, s2N, N, ACN, BCN, ABCN, AC, s1N, AN, B, AB, C, A, CN, ABC
    """
    pass

class CurveStyle(str):
    """Values are: formula, constantYValue, straightLineYValues, rampYValue
    """
    pass

class BusbarConfiguration(str):
    """Values are: doubleBus, ringBus, singleBus, mainWithTransfer
    """
    pass
