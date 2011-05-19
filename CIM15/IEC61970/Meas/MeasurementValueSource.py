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

class MeasurementValueSource(IdentifiedObject):
    """MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.
    """

    def __init__(self, MeasurementValues=None, *args, **kw_args):
        """Initialises a new 'MeasurementValueSource' instance.

        @param MeasurementValues: The MeasurementValues updated by the source
        """
        self._MeasurementValues = []
        self.MeasurementValues = [] if MeasurementValues is None else MeasurementValues

        super(MeasurementValueSource, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MeasurementValues"]
    _many_refs = ["MeasurementValues"]

    def getMeasurementValues(self):
        """The MeasurementValues updated by the source
        """
        return self._MeasurementValues

    def setMeasurementValues(self, value):
        for x in self._MeasurementValues:
            x.MeasurementValueSource = None
        for y in value:
            y._MeasurementValueSource = self
        self._MeasurementValues = value

    MeasurementValues = property(getMeasurementValues, setMeasurementValues)

    def addMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj.MeasurementValueSource = self

    def removeMeasurementValues(self, *MeasurementValues):
        for obj in MeasurementValues:
            obj.MeasurementValueSource = None

