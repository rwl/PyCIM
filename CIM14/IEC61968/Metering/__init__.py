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

"""This package contains the core information classes that support end device applications with specialized classes for metering equipment and remote reading functions. These classes are generally associated with the point where a service is delivered to the customer.
"""

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

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Metering"
nsPrefix = "cimMetering"


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
