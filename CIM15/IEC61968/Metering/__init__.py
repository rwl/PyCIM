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

"""This package contains only diagrams, drawn by hand from Metering-related XSDs that are in Part 9 document. Entry points into the schema are filled with green. Non-used associations are light grey.
"""

from CIM15.IEC61968.Metering.SDPLocation import SDPLocation
from CIM15.IEC61968.Metering.Reading import Reading
from CIM15.IEC61968.Metering.ServiceDeliveryPoint import ServiceDeliveryPoint
from CIM15.IEC61968.Metering.ElectricMeteringFunction import ElectricMeteringFunction
from CIM15.IEC61968.Metering.DemandResponseProgram import DemandResponseProgram
from CIM15.IEC61968.Metering.ReadingMultiplier import ReadingMultiplier
from CIM15.IEC61968.Metering.MeterReading import MeterReading
from CIM15.IEC61968.Metering.ReadingQuality import ReadingQuality
from CIM15.IEC61968.Metering.EndDeviceEvent import EndDeviceEvent
from CIM15.IEC61968.Metering.IntervalReading import IntervalReading
from CIM15.IEC61968.Metering.Meter import Meter
from CIM15.IEC61968.Metering.MeterServiceWork import MeterServiceWork
from CIM15.IEC61968.Metering.PendingCalculation import PendingCalculation
from CIM15.IEC61968.Metering.IntervalBlock import IntervalBlock
from CIM15.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction
from CIM15.IEC61968.Metering.ComFunction import ComFunction
from CIM15.IEC61968.Metering.EndDevice import EndDevice
from CIM15.IEC61968.Metering.SimpleEndDeviceFunction import SimpleEndDeviceFunction
from CIM15.IEC61968.Metering.EndDeviceGroup import EndDeviceGroup
from CIM15.IEC61968.Metering.Register import Register
from CIM15.IEC61968.Metering.EndDeviceControl import EndDeviceControl
from CIM15.IEC61968.Metering.DynamicDemand import DynamicDemand
from CIM15.IEC61968.Metering.ReadingType import ReadingType

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Metering"
nsPrefix = "cimMetering"


class EndDeviceFunctionKind(str):
    """Values are: onRequestRead, relaysProgramming, demandResponse, metrology, outageHistory, autonomousDst, reverseFlow
    """
    pass

class ReadingKind(str):
    """Values are: phaseAngle, volume, frequency, energy, currentAngle, powerFactor, date, other, demand, power, pressure, voltage, voltageAngle, time, current
    """
    pass

class DemandKind(str):
    """Values are: fixedBlock, rollingBlock, logarithmic
    """
    pass
