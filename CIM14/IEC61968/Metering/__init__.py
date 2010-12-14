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

"""This package contains the core information classes that support end device applications with specialized classes for metering equipment and remote reading functions. These classes are generally associated with the point where a service is delivered to the customer.
"""

nsPrefix = "cimMetering"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Metering"

from CIM14.IEC61968.Metering.DeviceFunction import DeviceFunction
from CIM14.IEC61968.Metering.ComFunction import ComFunction
from CIM14.IEC61968.Metering.Register import Register
from CIM14.IEC61968.Metering.EndDeviceControl import EndDeviceControl
from CIM14.IEC61968.Metering.Reading import Reading
from CIM14.IEC61968.Metering.EndDeviceAsset import EndDeviceAsset
from CIM14.IEC61968.Metering.MeterAsset import MeterAsset
from CIM14.IEC61968.Metering.ElectricMeteringFunction import ElectricMeteringFunction
from CIM14.IEC61968.Metering.EndDeviceGroup import EndDeviceGroup
from CIM14.IEC61968.Metering.Pending import Pending
from CIM14.IEC61968.Metering.IntervalReading import IntervalReading
from CIM14.IEC61968.Metering.MeterReading import MeterReading
from CIM14.IEC61968.Metering.DemandResponseProgram import DemandResponseProgram
from CIM14.IEC61968.Metering.EndDeviceEvent import EndDeviceEvent
from CIM14.IEC61968.Metering.DynamicDemand import DynamicDemand
from CIM14.IEC61968.Metering.MeterServiceWork import MeterServiceWork
from CIM14.IEC61968.Metering.ServiceDeliveryPoint import ServiceDeliveryPoint
from CIM14.IEC61968.Metering.ReadingType import ReadingType
from CIM14.IEC61968.Metering.SDPLocation import SDPLocation
from CIM14.IEC61968.Metering.ReadingQuality import ReadingQuality
from CIM14.IEC61968.Metering.IntervalBlock import IntervalBlock

class ReadingKind(str):
    """Kind of reading.
    Values are: voltageAngle, current, time, powerFactor, voltage, frequency, power, other, energy, demand, volume, date, phaseAngle, pressure, currentAngle
    """
    pass

class DemandKind(str):
    """Kind of demand for dynamic meter configuration.
    Values are: logarithmic, fixedBlock, rollingBlock
    """
    pass
