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

"""This package contains only diagrams, drawn by hand from Metering-related XSDs that are in Part 9 document. Entry points into the schema are filled with green. Non-used associations are light grey.
"""

ns_prefix = "cimMetering"
ns_uri = "http://iec.ch/TC57/CIM-generic#Metering"

from CIM14v13.IEC61968.Metering.SDPLocation import SDPLocation
from CIM14v13.IEC61968.Metering.DeviceFunction import DeviceFunction
from CIM14v13.IEC61968.Metering.ComFunction import ComFunction
from CIM14v13.IEC61968.Metering.IntervalReading import IntervalReading
from CIM14v13.IEC61968.Metering.ReadingType import ReadingType
from CIM14v13.IEC61968.Metering.EndDeviceAsset import EndDeviceAsset
from CIM14v13.IEC61968.Metering.MeterAsset import MeterAsset
from CIM14v13.IEC61968.Metering.ElectricMeteringFunction import ElectricMeteringFunction
from CIM14v13.IEC61968.Metering.Reading import Reading
from CIM14v13.IEC61968.Metering.Register import Register
from CIM14v13.IEC61968.Metering.ReadingQuality import ReadingQuality
from CIM14v13.IEC61968.Metering.MeterServiceWork import MeterServiceWork
from CIM14v13.IEC61968.Metering.IntervalBlock import IntervalBlock
from CIM14v13.IEC61968.Metering.MeterReading import MeterReading
from CIM14v13.IEC61968.Metering.DemandResponseProgram import DemandResponseProgram
from CIM14v13.IEC61968.Metering.EndDeviceEvent import EndDeviceEvent
from CIM14v13.IEC61968.Metering.EndDeviceControl import EndDeviceControl
from CIM14v13.IEC61968.Metering.ServiceDeliveryPoint import ServiceDeliveryPoint
from CIM14v13.IEC61968.Metering.EndDeviceGroup import EndDeviceGroup
from CIM14v13.IEC61968.Metering.Pending import Pending
