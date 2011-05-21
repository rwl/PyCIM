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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ReadingType(IdentifiedObject):
    """Type of data conveyed by a specific Reading.
    """

    def __init__(self, multiplier="k", kind="voltageAngle", unit="N", reverseChronology=False, defaultQuality='', defaultValueDataType='', channelNumber=0, intervalLength=0.0, Readings=None, dynamicConfiguration=None, IntervalBlocks=None, Pending=None, Register=None, *args, **kw_args):
        """Initialises a new 'ReadingType' instance.

        @param multiplier: Multiplier for 'unit'. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param kind: Kind of reading. Values are: "voltageAngle", "current", "time", "powerFactor", "voltage", "frequency", "power", "other", "energy", "demand", "volume", "date", "phaseAngle", "pressure", "currentAngle"
        @param unit: Unit for the reading value. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param reverseChronology: True for systems that must operate in 'reverse' chronological order. 
        @param defaultQuality: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted. 
        @param defaultValueDataType: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger). 
        @param channelNumber: Logical positioning of this measurement data. 
        @param intervalLength: (if incremental reading value) Length of increment interval. 
        @param Readings: All reading values with this type information.
        @param dynamicConfiguration: Demand configuration.
        @param IntervalBlocks: All blocks containing interval reading values with this type information.
        @param Pending: Pending conversion that produced this reading type.
        @param Register: Register displaying values with this type information.
        """
        #: Multiplier for 'unit'. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.multiplier = multiplier

        #: Kind of reading. Values are: "voltageAngle", "current", "time", "powerFactor", "voltage", "frequency", "power", "other", "energy", "demand", "volume", "date", "phaseAngle", "pressure", "currentAngle"
        self.kind = kind

        #: Unit for the reading value. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.unit = unit

        #: True for systems that must operate in 'reverse' chronological order.
        self.reverseChronology = reverseChronology

        #: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted.
        self.defaultQuality = defaultQuality

        #: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger).
        self.defaultValueDataType = defaultValueDataType

        #: Logical positioning of this measurement data.
        self.channelNumber = channelNumber

        #: (if incremental reading value) Length of increment interval.
        self.intervalLength = intervalLength

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self.dynamicConfiguration = dynamicConfiguration

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self._Pending = None
        self.Pending = Pending

        self._Register = None
        self.Register = Register

        super(ReadingType, self).__init__(*args, **kw_args)

    _attrs = ["multiplier", "kind", "unit", "reverseChronology", "defaultQuality", "defaultValueDataType", "channelNumber", "intervalLength"]
    _attr_types = {"multiplier": str, "kind": str, "unit": str, "reverseChronology": bool, "defaultQuality": str, "defaultValueDataType": str, "channelNumber": int, "intervalLength": float}
    _defaults = {"multiplier": "k", "kind": "voltageAngle", "unit": "N", "reverseChronology": False, "defaultQuality": '', "defaultValueDataType": '', "channelNumber": 0, "intervalLength": 0.0}
    _enums = {"multiplier": "UnitMultiplier", "kind": "ReadingKind", "unit": "UnitSymbol"}
    _refs = ["Readings", "dynamicConfiguration", "IntervalBlocks", "Pending", "Register"]
    _many_refs = ["Readings", "IntervalBlocks"]

    def getReadings(self):
        """All reading values with this type information.
        """
        return self._Readings

    def setReadings(self, value):
        for x in self._Readings:
            x.ReadingType = None
        for y in value:
            y._ReadingType = self
        self._Readings = value

    Readings = property(getReadings, setReadings)

    def addReadings(self, *Readings):
        for obj in Readings:
            obj.ReadingType = self

    def removeReadings(self, *Readings):
        for obj in Readings:
            obj.ReadingType = None

    # Demand configuration.
    dynamicConfiguration = None

    def getIntervalBlocks(self):
        """All blocks containing interval reading values with this type information.
        """
        return self._IntervalBlocks

    def setIntervalBlocks(self, value):
        for x in self._IntervalBlocks:
            x.ReadingType = None
        for y in value:
            y._ReadingType = self
        self._IntervalBlocks = value

    IntervalBlocks = property(getIntervalBlocks, setIntervalBlocks)

    def addIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.ReadingType = self

    def removeIntervalBlocks(self, *IntervalBlocks):
        for obj in IntervalBlocks:
            obj.ReadingType = None

    def getPending(self):
        """Pending conversion that produced this reading type.
        """
        return self._Pending

    def setPending(self, value):
        if self._Pending is not None:
            self._Pending._ReadingType = None

        self._Pending = value
        if self._Pending is not None:
            self._Pending.ReadingType = None
            self._Pending._ReadingType = self

    Pending = property(getPending, setPending)

    def getRegister(self):
        """Register displaying values with this type information.
        """
        return self._Register

    def setRegister(self, value):
        if self._Register is not None:
            self._Register._ReadingType = None

        self._Register = value
        if self._Register is not None:
            self._Register.ReadingType = None
            self._Register._ReadingType = self

    Register = property(getRegister, setRegister)

