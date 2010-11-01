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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ReadingType(IdentifiedObject):
    """Type of data conveyed by a specific Reading.
    """

    def __init__(self, kind='power', unit='m2', multiplier='m', channelNumber=0, defaultQuality='', dynamicConfiguration='', intervalLength=0.0, reverseChronology=False, defaultValueDataType='', Pending=None, Readings=None, IntervalBlocks=None, Register=None, *args, **kw_args):
        """Initializes a new 'ReadingType' instance.

        @param kind: Kind of reading. Values are: "power", "voltageAngle", "other", "energy", "phaseAngle", "date", "time", "volume", "voltage", "demand", "powerFactor", "currentAngle", "pressure", "current"
        @param unit: Unit for the reading value. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param multiplier: Multiplier for 'unit'. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param channelNumber: Logical positioning of this measurement data. 
        @param defaultQuality: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted. 
        @param dynamicConfiguration: Demand configuration such as block, rolling, logarithmic and sizes such as 15 min, 30 min, 5 min subinterval. 
        @param intervalLength: (if incremental reading value) Length of increment interval. 
        @param reverseChronology: True for systems that must operate in 'reverse' chronological order. 
        @param defaultValueDataType: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger). 
        @param Pending: Pending conversion that produced this reading type.
        @param Readings: All reading values with this type information.
        @param IntervalBlocks: All blocks containing interval reading values with this type information.
        @param Register: Register displaying values with this type information.
        """
        #: Kind of reading. Values are: "power", "voltageAngle", "other", "energy", "phaseAngle", "date", "time", "volume", "voltage", "demand", "powerFactor", "currentAngle", "pressure", "current"
        self.kind = kind

        #: Unit for the reading value. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.unit = unit

        #: Multiplier for 'unit'. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.multiplier = multiplier

        #: Logical positioning of this measurement data. 
        self.channelNumber = channelNumber

        #: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted. 
        self.defaultQuality = defaultQuality

        #: Demand configuration such as block, rolling, logarithmic and sizes such as 15 min, 30 min, 5 min subinterval. 
        self.dynamicConfiguration = dynamicConfiguration

        #: (if incremental reading value) Length of increment interval. 
        self.intervalLength = intervalLength

        #: True for systems that must operate in 'reverse' chronological order. 
        self.reverseChronology = reverseChronology

        #: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger). 
        self.defaultValueDataType = defaultValueDataType

        self._Pending = None
        self.Pending = Pending

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self._Register = None
        self.Register = Register

        super(ReadingType, self).__init__(*args, **kw_args)

    def getPending(self):
        """Pending conversion that produced this reading type.
        """
        return self._Pending

    def setPending(self, value):
        if self._Pending is not None:
            self._Pending._ReadingType = None

        self._Pending = value
        if self._Pending is not None:
            self._Pending._ReadingType = self

    Pending = property(getPending, setPending)

    def getReadings(self):
        """All reading values with this type information.
        """
        return self._Readings

    def setReadings(self, value):
        for x in self._Readings:
            x._ReadingType = None
        for y in value:
            y._ReadingType = self
        self._Readings = value

    Readings = property(getReadings, setReadings)

    def addReadings(self, *Readings):
        for obj in Readings:
            obj._ReadingType = self
            self._Readings.append(obj)

    def removeReadings(self, *Readings):
        for obj in Readings:
            obj._ReadingType = None
            self._Readings.remove(obj)

    def getIntervalBlocks(self):
        """All blocks containing interval reading values with this type information.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for x in self._IntervalBlocks:
            x._ReadingType = None
        for y in value:
            y._ReadingType = self
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj._ReadingType = self
            self._IntervalBlocks.append(obj)

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj._ReadingType = None
            self._IntervalBlocks.remove(obj)

    def getRegister(self):
        """Register displaying values with this type information.
        """
        return self._Register

    def setRegister(self, value):
        if self._Register is not None:
            self._Register._ReadingType = None

        self._Register = value
        if self._Register is not None:
            self._Register._ReadingType = self

    Register = property(getRegister, setRegister)

