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

from CIM14v13.IEC61970.Meas.MeasurementValue import MeasurementValue

class Reading(MeasurementValue):
    """Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.
    """

    def __init__(self, value=0.0, EndDeviceAsset=None, ReadingQualities=None, ReadingType=None, MeterReadings=None, *args, **kw_args):
        """Initializes a new 'Reading' instance.

        @param value: Value of this reading. 
        @param EndDeviceAsset:
        @param ReadingQualities: Used only if quality of this reading value is different than 'Good'.
        @param ReadingType: Type information for this reading value.
        @param MeterReadings: All meter readings (sets of values) containing this reading value.
        """
        #: Value of this reading. 
        self.value = value

        self._EndDeviceAsset = None
        self.EndDeviceAsset = EndDeviceAsset

        self._ReadingQualities = []
        self.ReadingQualities = [] if ReadingQualities is None else ReadingQualities

        self._ReadingType = None
        self.ReadingType = ReadingType

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        super(Reading, self).__init__(*args, **kw_args)

    def getEndDeviceAsset(self):
        
        return self._EndDeviceAsset

    def setEndDeviceAsset(self, value):
        if self._EndDeviceAsset is not None:
            filtered = [x for x in self.EndDeviceAsset.Readings if x != self]
            self._EndDeviceAsset._Readings = filtered

        self._EndDeviceAsset = value
        if self._EndDeviceAsset is not None:
            self._EndDeviceAsset._Readings.append(self)

    EndDeviceAsset = property(getEndDeviceAsset, setEndDeviceAsset)

    def getReadingQualities(self):
        """Used only if quality of this reading value is different than 'Good'.
        """
        return self._ReadingQualities

    def setReadingQualities(self, value):
        for x in self._ReadingQualities:
            x._Reading = None
        for y in value:
            y._Reading = self
        self._ReadingQualities = value

    ReadingQualities = property(getReadingQualities, setReadingQualities)

    def addReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj._Reading = self
            self._ReadingQualities.append(obj)

    def removeReadingQualities(self, *ReadingQualities):
        for obj in ReadingQualities:
            obj._Reading = None
            self._ReadingQualities.remove(obj)

    def getReadingType(self):
        """Type information for this reading value.
        """
        return self._ReadingType

    def setReadingType(self, value):
        if self._ReadingType is not None:
            filtered = [x for x in self.ReadingType.Readings if x != self]
            self._ReadingType._Readings = filtered

        self._ReadingType = value
        if self._ReadingType is not None:
            self._ReadingType._Readings.append(self)

    ReadingType = property(getReadingType, setReadingType)

    def getMeterReadings(self):
        """All meter readings (sets of values) containing this reading value.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for p in self._MeterReadings:
            filtered = [q for q in p.Readings if q != self]
            self._MeterReadings._Readings = filtered
        for r in value:
            if self not in r._Readings:
                r._Readings.append(self)
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            if self not in obj._Readings:
                obj._Readings.append(self)
            self._MeterReadings.append(obj)

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            if self in obj._Readings:
                obj._Readings.remove(self)
            self._MeterReadings.remove(obj)

