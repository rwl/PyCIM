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

from CIM14.IEC61970.Meas.Quality61850 import Quality61850

class MeasurementValueQuality(Quality61850):
    """Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.
    """

    def __init__(self, MeasurementValue=None, *args, **kw_args):
        """Initialises a new 'MeasurementValueQuality' instance.

        @param MeasurementValue: A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        self._MeasurementValue = None
        self.MeasurementValue = MeasurementValue

        super(MeasurementValueQuality, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MeasurementValue"]
    _many_refs = []

    def getMeasurementValue(self):
        """A MeasurementValue has a MeasurementValueQuality associated with it.
        """
        return self._MeasurementValue

    def setMeasurementValue(self, value):
        if self._MeasurementValue is not None:
            self._MeasurementValue._MeasurementValueQuality = None

        self._MeasurementValue = value
        if self._MeasurementValue is not None:
            self._MeasurementValue.MeasurementValueQuality = None
            self._MeasurementValue._MeasurementValueQuality = self

    MeasurementValue = property(getMeasurementValue, setMeasurementValue)

