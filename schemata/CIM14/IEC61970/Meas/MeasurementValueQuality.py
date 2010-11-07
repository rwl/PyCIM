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

from CIM14.IEC61970.Meas.Quality61850 import Quality61850

class MeasurementValueQuality(Quality61850):
    """Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """

    def __init__(self, MeasurementValue=None, **kw_args):
        """Initializes a new 'MeasurementValueQuality' instance.

        @param MeasurementValue: A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        self._MeasurementValue = None
        self.MeasurementValue = MeasurementValue

        super(MeasurementValueQuality, self).__init__(**kw_args)

    def getMeasurementValue(self):
        """A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._MeasurementValue

    def setMeasurementValue(self, value):
        if self._MeasurementValue is not None:
            self._MeasurementValue._MeasurementValueQuality = None

        self._MeasurementValue = value
        if self._MeasurementValue is not None:
            self._MeasurementValue._MeasurementValueQuality = self

    MeasurementValue = property(getMeasurementValue, setMeasurementValue)

