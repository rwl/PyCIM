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

class StringMeasurementValue(MeasurementValue):
    """StringMeasurementValue represents a measurement value of type string.
    """

    def __init__(self, value='', StringMeasurement=None, *args, **kw_args):
        """Initializes a new 'StringMeasurementValue' instance.

        @param value: The value to supervise. 
        @param StringMeasurement: Measurement to which this value is connected.
        """
        #: The value to supervise. 
        self.value = value

        self._StringMeasurement = None
        self.StringMeasurement = StringMeasurement

        super(StringMeasurementValue, self).__init__(*args, **kw_args)

    def getStringMeasurement(self):
        """Measurement to which this value is connected.
        """
        return self._StringMeasurement

    def setStringMeasurement(self, value):
        if self._StringMeasurement is not None:
            filtered = [x for x in self.StringMeasurement.StringMeasurementValues if x != self]
            self._StringMeasurement._StringMeasurementValues = filtered

        self._StringMeasurement = value
        if self._StringMeasurement is not None:
            self._StringMeasurement._StringMeasurementValues.append(self)

    StringMeasurement = property(getStringMeasurement, setStringMeasurement)

