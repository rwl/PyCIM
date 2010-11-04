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

from CIM14v13.IEC61970.Meas.Measurement import Measurement

class StringMeasurement(Measurement):
    """StringMeasurement represents a measurement with values of type string.
    """

    def __init__(self, StringMeasurementValues=None, **kw_args):
        """Initializes a new 'StringMeasurement' instance.

        @param StringMeasurementValues: The values connected to this measurement.
        """
        self._StringMeasurementValues = []
        self.StringMeasurementValues = [] if StringMeasurementValues is None else StringMeasurementValues

        super(StringMeasurement, self).__init__(**kw_args)

    def getStringMeasurementValues(self):
        """The values connected to this measurement.
        """
        return self._StringMeasurementValues

    def setStringMeasurementValues(self, value):
        for x in self._StringMeasurementValues:
            x._StringMeasurement = None
        for y in value:
            y._StringMeasurement = self
        self._StringMeasurementValues = value

    StringMeasurementValues = property(getStringMeasurementValues, setStringMeasurementValues)

    def addStringMeasurementValues(self, *StringMeasurementValues):
        for obj in StringMeasurementValues:
            obj._StringMeasurement = self
            self._StringMeasurementValues.append(obj)

    def removeStringMeasurementValues(self, *StringMeasurementValues):
        for obj in StringMeasurementValues:
            obj._StringMeasurement = None
            self._StringMeasurementValues.remove(obj)

