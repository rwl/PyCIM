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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ReadingType(IdentifiedObject):
    """Type of data conveyed by a specific Reading.Type of data conveyed by a specific Reading.
    """

    def __init__(self, multiplier="M", unit="N", kind="phaseAngle", reverseChronology=False, defaultQuality='', intervalLength=0.0, channelNumber=0, defaultValueDataType='', IntervalBlocks=None, dynamicConfiguration=None, Readings=None, Register=None, PendingCalculation=None, *args, **kw_args):
        """Initialises a new 'ReadingType' instance.

        @param multiplier: Multiplier for 'unit'. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param unit: Unit for the reading value. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param kind: Kind of reading. Values are: "phaseAngle", "volume", "frequency", "energy", "currentAngle", "powerFactor", "date", "other", "demand", "power", "pressure", "voltage", "voltageAngle", "time", "current"
        @param reverseChronology: True for systems that must operate in 'reverse' chronological order. 
        @param defaultQuality: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted. 
        @param intervalLength: (if incremental reading value) Length of increment interval. 
        @param channelNumber: Logical positioning of this measurement data. 
        @param defaultValueDataType: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger). 
        @param IntervalBlocks: All blocks containing interval reading values with this type information.
        @param dynamicConfiguration: Demand configuration.
        @param Readings: All reading values with this type information.
        @param Register: Register displaying values with this type information.
        @param PendingCalculation: Pending conversion that produced this reading type.
        """
        #: Multiplier for 'unit'. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.multiplier = multiplier

        #: Unit for the reading value. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.unit = unit

        #: Kind of reading. Values are: "phaseAngle", "volume", "frequency", "energy", "currentAngle", "powerFactor", "date", "other", "demand", "power", "pressure", "voltage", "voltageAngle", "time", "current"
        self.kind = kind

        #: True for systems that must operate in 'reverse' chronological order.
        self.reverseChronology = reverseChronology

        #: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted.
        self.defaultQuality = defaultQuality

        #: (if incremental reading value) Length of increment interval.
        self.intervalLength = intervalLength

        #: Logical positioning of this measurement data.
        self.channelNumber = channelNumber

        #: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger).
        self.defaultValueDataType = defaultValueDataType

        self._IntervalBlocks = []
        self.IntervalBlocks = [] if IntervalBlocks is None else IntervalBlocks

        self.dynamicConfiguration = dynamicConfiguration

        self._Readings = []
        self.Readings = [] if Readings is None else Readings

        self._Register = None
        self.Register = Register

        self._PendingCalculation = None
        self.PendingCalculation = PendingCalculation

        super(ReadingType, self).__init__(*args, **kw_args)

    _attrs = ["multiplier", "unit", "kind", "reverseChronology", "defaultQuality", "intervalLength", "channelNumber", "defaultValueDataType"]
    _attr_types = {"multiplier": str, "unit": str, "kind": str, "reverseChronology": bool, "defaultQuality": str, "intervalLength": float, "channelNumber": int, "defaultValueDataType": str}
    _defaults = {"multiplier": "M", "unit": "N", "kind": "phaseAngle", "reverseChronology": False, "defaultQuality": '', "intervalLength": 0.0, "channelNumber": 0, "defaultValueDataType": ''}
    _enums = {"multiplier": "UnitMultiplier", "unit": "UnitSymbol", "kind": "ReadingKind"}
    _refs = ["IntervalBlocks", "dynamicConfiguration", "Readings", "Register", "PendingCalculation"]
    _many_refs = ["IntervalBlocks", "Readings"]

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

    # Demand configuration.
    dynamicConfiguration = None

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

    def getPendingCalculation(self):
        """Pending conversion that produced this reading type.
        """
        return self._PendingCalculation

    def setPendingCalculation(self, value):
        if self._PendingCalculation is not None:
            self._PendingCalculation._ReadingType = None

        self._PendingCalculation = value
        if self._PendingCalculation is not None:
            self._PendingCalculation.ReadingType = None
            self._PendingCalculation._ReadingType = self

    PendingCalculation = property(getPendingCalculation, setPendingCalculation)

