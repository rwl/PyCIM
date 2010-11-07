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

"""Contains entities that describe dynamic measurement data exchanged between applications.
"""

nsPrefix = "cimMeas"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Meas"

from CIM14.IEC61970.Meas.MeasurementValue import MeasurementValue
from CIM14.IEC61970.Meas.Control import Control
from CIM14.IEC61970.Meas.Measurement import Measurement
from CIM14.IEC61970.Meas.StringMeasurement import StringMeasurement
from CIM14.IEC61970.Meas.Discrete import Discrete
from CIM14.IEC61970.Meas.CurrentTransformer import CurrentTransformer
from CIM14.IEC61970.Meas.ValueAliasSet import ValueAliasSet
from CIM14.IEC61970.Meas.DiscreteValue import DiscreteValue
from CIM14.IEC61970.Meas.Limit import Limit
from CIM14.IEC61970.Meas.AnalogLimit import AnalogLimit
from CIM14.IEC61970.Meas.LimitSet import LimitSet
from CIM14.IEC61970.Meas.AccumulatorLimitSet import AccumulatorLimitSet
from CIM14.IEC61970.Meas.SetPoint import SetPoint
from CIM14.IEC61970.Meas.Command import Command
from CIM14.IEC61970.Meas.StringMeasurementValue import StringMeasurementValue
from CIM14.IEC61970.Meas.PotentialTransformer import PotentialTransformer
from CIM14.IEC61970.Meas.ValueToAlias import ValueToAlias
from CIM14.IEC61970.Meas.ControlType import ControlType
from CIM14.IEC61970.Meas.Accumulator import Accumulator
from CIM14.IEC61970.Meas.AnalogLimitSet import AnalogLimitSet
from CIM14.IEC61970.Meas.AccumulatorLimit import AccumulatorLimit
from CIM14.IEC61970.Meas.MeasurementValueSource import MeasurementValueSource
from CIM14.IEC61970.Meas.AnalogValue import AnalogValue
from CIM14.IEC61970.Meas.Analog import Analog
from CIM14.IEC61970.Meas.Quality61850 import Quality61850
from CIM14.IEC61970.Meas.MeasurementValueQuality import MeasurementValueQuality
from CIM14.IEC61970.Meas.AccumulatorValue import AccumulatorValue

