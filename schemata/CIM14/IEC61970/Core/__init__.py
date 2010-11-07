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

"""Contains the core PowerSystemResource and ConductingEquipment entities shared by all applications plus common collections of those entities. Not all applications require all the Core entities.  This package does not depend on any other package except the Domain package, but most of the other packages have associations and generalizations that depend on it.
"""

nsPrefix = "cimCore"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Core"

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject
from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource
from CIM14.IEC61970.Core.Equipment import Equipment
from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment
from CIM14.IEC61970.Core.Curve import Curve
from CIM14.IEC61970.Core.BasicIntervalSchedule import BasicIntervalSchedule
from CIM14.IEC61970.Core.IrregularIntervalSchedule import IrregularIntervalSchedule
from CIM14.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule
from CIM14.IEC61970.Core.ConnectivityNodeContainer import ConnectivityNodeContainer
from CIM14.IEC61970.Core.EquipmentContainer import EquipmentContainer
from CIM14.IEC61970.Core.CurveData import CurveData
from CIM14.IEC61970.Core.Bay import Bay
from CIM14.IEC61970.Core.PSRType import PSRType
from CIM14.IEC61970.Core.GeographicalRegion import GeographicalRegion
from CIM14.IEC61970.Core.Terminal import Terminal
from CIM14.IEC61970.Core.OperatingParticipant import OperatingParticipant
from CIM14.IEC61970.Core.VoltageLevel import VoltageLevel
from CIM14.IEC61970.Core.ConnectivityNode import ConnectivityNode
from CIM14.IEC61970.Core.BasePower import BasePower
from CIM14.IEC61970.Core.Unit import Unit
from CIM14.IEC61970.Core.BaseVoltage import BaseVoltage
from CIM14.IEC61970.Core.SubGeographicalRegion import SubGeographicalRegion
from CIM14.IEC61970.Core.PsrList import PsrList
from CIM14.IEC61970.Core.Substation import Substation
from CIM14.IEC61970.Core.ReportingGroup import ReportingGroup
from CIM14.IEC61970.Core.ReportingSuperGroup import ReportingSuperGroup
from CIM14.IEC61970.Core.RegularTimePoint import RegularTimePoint
from CIM14.IEC61970.Core.IrregularTimePoint import IrregularTimePoint
from CIM14.IEC61970.Core.OperatingShare import OperatingShare

