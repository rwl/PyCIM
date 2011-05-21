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

from CIM14.CPSM.Equipment.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from CIM14.CPSM.Equipment.Core.RegularIntervalSchedule import RegularIntervalSchedule
from CIM14.CPSM.Equipment.Core.RegularTimePoint import RegularTimePoint
from CIM14.CPSM.Equipment.Core.Bay import Bay
from CIM14.CPSM.Equipment.Core.Equipment import Equipment
from CIM14.CPSM.Equipment.Core.EquipmentContainer import EquipmentContainer
from CIM14.CPSM.Equipment.Core.IdentifiedObject import IdentifiedObject
from CIM14.CPSM.Equipment.Core.SubGeographicalRegion import SubGeographicalRegion
from CIM14.CPSM.Equipment.Core.PowerSystemResource import PowerSystemResource
from CIM14.CPSM.Equipment.Core.BasicIntervalSchedule import BasicIntervalSchedule
from CIM14.CPSM.Equipment.Core.Curve import Curve
from CIM14.CPSM.Equipment.Core.VoltageLevel import VoltageLevel
from CIM14.CPSM.Equipment.Core.Unit import Unit
from CIM14.CPSM.Equipment.Core.BaseVoltage import BaseVoltage
from CIM14.CPSM.Equipment.Core.ConnectivityNode import ConnectivityNode
from CIM14.CPSM.Equipment.Core.Substation import Substation
from CIM14.CPSM.Equipment.Core.ConductingEquipment import ConductingEquipment
from CIM14.CPSM.Equipment.Core.Terminal import Terminal
from CIM14.CPSM.Equipment.Core.GeographicalRegion import GeographicalRegion
from CIM14.CPSM.Equipment.Core.CurveData import CurveData

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Core"
nsPrefix = "cimCore"


class CurveStyle(str):
    """Values are: straightLineYValues, rampYValue, constantYValue, formula
    """
    pass
