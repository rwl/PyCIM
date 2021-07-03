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

"""Contains entities that describe dynamic measurement data exchanged between applications.
"""

from CIM16.IEC61970.Meas.AccumulatorLimit import AccumulatorLimit
from CIM16.IEC61970.Meas.ValueToAlias import ValueToAlias
from CIM16.IEC61970.Meas.MeasurementValueSource import MeasurementValueSource
from CIM16.IEC61970.Meas.Analog import Analog
from CIM16.IEC61970.Meas.AnalogValue import AnalogValue
from CIM16.IEC61970.Meas.Measurement import Measurement
from CIM16.IEC61970.Meas.ControlType import ControlType
from CIM16.IEC61970.Meas.StringMeasurementValue import StringMeasurementValue
from CIM16.IEC61970.Meas.StringMeasurement import StringMeasurement
from CIM16.IEC61970.Meas.AnalogLimit import AnalogLimit
from CIM16.IEC61970.Meas.SetPoint import SetPoint
from CIM16.IEC61970.Meas.Limit import Limit
from CIM16.IEC61970.Meas.Discrete import Discrete
from CIM16.IEC61970.Meas.ValueAliasSet import ValueAliasSet
from CIM16.IEC61970.Meas.Quality61850 import Quality61850
from CIM16.IEC61970.Meas.AccumulatorValue import AccumulatorValue
from CIM16.IEC61970.Meas.Command import Command
from CIM16.IEC61970.Meas.Accumulator import Accumulator
from CIM16.IEC61970.Meas.MeasurementValueQuality import MeasurementValueQuality
from CIM16.IEC61970.Meas.MeasurementValue import MeasurementValue
from CIM16.IEC61970.Meas.DiscreteValue import DiscreteValue
from CIM16.IEC61970.Meas.AnalogLimitSet import AnalogLimitSet
from CIM16.IEC61970.Meas.LimitSet import LimitSet
from CIM16.IEC61970.Meas.AccumulatorLimitSet import AccumulatorLimitSet
from CIM16.IEC61970.Meas.Control import Control

nsURI = "http://iec.ch/TC57/2013/CIM-schema-cim16#Meas"
nsPrefix = "cimMeas"


class Validity(str):
    """Values are: QUESTIONABLE, INVALID, GOOD
    """
    pass
