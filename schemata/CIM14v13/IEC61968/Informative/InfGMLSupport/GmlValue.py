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

class GmlValue(IdentifiedObject):
    """Used for direct representation of values.
    """

    def __init__(self, value=0.0, timePeriod='', dateTime='', MeasurementValue=None, GmlObservation=None, *args, **kw_args):
        """Initializes a new 'GmlValue' instance.

        @param value: 
        @param timePeriod: 
        @param dateTime: 
        @param MeasurementValue:
        @param GmlObservation:
        """
 
        self.value = value

 
        self.timePeriod = timePeriod

 
        self.dateTime = dateTime

        self._MeasurementValue = None
        self.MeasurementValue = MeasurementValue

        self._GmlObservation = None
        self.GmlObservation = GmlObservation

        super(GmlValue, self).__init__(*args, **kw_args)

    def getMeasurementValue(self):
        
        return self._MeasurementValue

    def setMeasurementValue(self, value):
        if self._MeasurementValue is not None:
            filtered = [x for x in self.MeasurementValue.GmlValues if x != self]
            self._MeasurementValue._GmlValues = filtered

        self._MeasurementValue = value
        if self._MeasurementValue is not None:
            self._MeasurementValue._GmlValues.append(self)

    MeasurementValue = property(getMeasurementValue, setMeasurementValue)

    def getGmlObservation(self):
        
        return self._GmlObservation

    def setGmlObservation(self, value):
        if self._GmlObservation is not None:
            filtered = [x for x in self.GmlObservation.GmlValues if x != self]
            self._GmlObservation._GmlValues = filtered

        self._GmlObservation = value
        if self._GmlObservation is not None:
            self._GmlObservation._GmlValues.append(self)

    GmlObservation = property(getGmlObservation, setGmlObservation)

