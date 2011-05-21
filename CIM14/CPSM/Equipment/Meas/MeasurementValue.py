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

from CIM14.CPSM.Equipment.Core.IdentifiedObject import IdentifiedObject

class MeasurementValue(IdentifiedObject):
    """The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.
    """

    def __init__(self, MeasurementValueSource=None, *args, **kw_args):
        """Initialises a new 'MeasurementValue' instance.

        @param MeasurementValueSource: A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        """
        self._MeasurementValueSource = None
        self.MeasurementValueSource = MeasurementValueSource

        super(MeasurementValue, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MeasurementValueSource"]
    _many_refs = []

    def getMeasurementValueSource(self):
        """A reference to the type of source that updates the MeasurementValue, e.g. SCADA, CCLink, manual, etc. User conventions for the names of sources are contained in the introduction to IEC 61970-301.
        """
        return self._MeasurementValueSource

    def setMeasurementValueSource(self, value):
        if self._MeasurementValueSource is not None:
            filtered = [x for x in self.MeasurementValueSource.MeasurementValues if x != self]
            self._MeasurementValueSource._MeasurementValues = filtered

        self._MeasurementValueSource = value
        if self._MeasurementValueSource is not None:
            if self not in self._MeasurementValueSource._MeasurementValues:
                self._MeasurementValueSource._MeasurementValues.append(self)

    MeasurementValueSource = property(getMeasurementValueSource, setMeasurementValueSource)

