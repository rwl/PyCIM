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
""" Update: 30/08/2017 
author: Francis J. Gomez """

from CIM16.IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from CIM16.IEC61970.Base.Core.NameTypeAuthority import NameTypeAuthority
from CIM16.IEC61970.Base.Core.Equipment import Equipment
from CIM16.IEC61970.Base.Core.ConductingEquipment import ConductingEquipment
from CIM16.IEC61970.Base.Core.RegularTimePoint import RegularTimePoint
from CIM16.IEC61970.Base.Core.ConnectivityNode import ConnectivityNode
from CIM16.IEC61970.Base.Core.PSRType import PSRType
from CIM16.IEC61970.Base.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from CIM16.IEC61970.Base.Core.Bay import Bay
from CIM16.IEC61970.Base.Core.EquipmentContainer import EquipmentContainer
from CIM16.IEC61970.Base.Core.ReportingGroup import ReportingGroup
from CIM16.IEC61970.Base.Core.BasePower import BasePower
from CIM16.IEC61970.Base.Core.PsrList import PsrList
from CIM16.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM16.IEC61970.Base.Core.BasicIntervalSchedule import BasicIntervalSchedule
from CIM16.IEC61970.Base.Core.Curve import Curve
from CIM16.IEC61970.Base.Core.GeographicalRegion import GeographicalRegion
from CIM16.IEC61970.Base.Core.CurveData import CurveData
from CIM16.IEC61970.Base.Core.SubGeographicalRegion import SubGeographicalRegion
from CIM16.IEC61970.Base.Core.NameType import NameType
from CIM16.IEC61970.Base.Core.Substation import Substation
from CIM16.IEC61970.Base.Core.Name import Name
from CIM16.IEC61970.Base.Core.BaseVoltage import BaseVoltage
from CIM16.IEC61970.Base.Core.Terminal import Terminal
from CIM16.IEC61970.Base.Core.IrregularIntervalSchedule import IrregularIntervalSchedule
from CIM16.IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule
from CIM16.IEC61970.Base.Core.OperatingParticipant import OperatingParticipant
from CIM16.IEC61970.Base.Core.OperatingShare import OperatingShare
from CIM16.IEC61970.Base.Core.VoltageLevel import VoltageLevel
from CIM16.IEC61970.Base.Core.ReportingSuperGroup import ReportingSuperGroup
from CIM16.IEC61970.Base.Core.IrregularTimePoint import IrregularTimePoint

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#Core"
nsPrefix = "cim"


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
