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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time.
    """

    def __init__(self, startTime='', value1Unit="A", value2Unit="A", *args, **kw_args):
        """Initialises a new 'BasicIntervalSchedule' instance.

        @param startTime: The time for the first time point. 
        @param value1Unit: Value1 units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        @param value2Unit: Value2 units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        """
        #: The time for the first time point.
        self.startTime = startTime

        #: Value1 units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        self.value1Unit = value1Unit

        #: Value2 units of measure. Values are: "A", "rad", "none", "g", "W/Hz", "V", "m2", "VA", "VArh", "N", "Pa", "VAh", "F", "H", "Hz-1", "W/s", "J", "m", "S", "min", "deg", "J/s", "s", "Wh", "m3", "oC", "V/VAr", "s-1", "h", "W", "ohm", "Hz", "VAr", "kg/J"
        self.value2Unit = value2Unit

        super(BasicIntervalSchedule, self).__init__(*args, **kw_args)

    _attrs = ["startTime", "value1Unit", "value2Unit"]
    _attr_types = {"startTime": str, "value1Unit": str, "value2Unit": str}
    _defaults = {"startTime": '', "value1Unit": "A", "value2Unit": "A"}
    _enums = {"value1Unit": "UnitSymbol", "value2Unit": "UnitSymbol"}
    _refs = []
    _many_refs = []

