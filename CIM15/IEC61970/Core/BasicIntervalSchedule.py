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

class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time.Schedule of values at points in time.
    """

    def __init__(self, startTime='', value1Multiplier="M", value2Unit="N", value1Unit="N", value2Multiplier="M", *args, **kw_args):
        """Initialises a new 'BasicIntervalSchedule' instance.

        @param startTime: The time for the first time point. 
        @param value1Multiplier: Multiplier for value1. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        @param value2Unit: Value2 units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param value1Unit: Value1 units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        @param value2Multiplier: Multiplier for value2. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        """
        #: The time for the first time point.
        self.startTime = startTime

        #: Multiplier for value1. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.value1Multiplier = value1Multiplier

        #: Value2 units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.value2Unit = value2Unit

        #: Value1 units of measure. Values are: "N", "A", "rad", "VAh", "Pa", "J", "h", "Hz", "VArh", "ohm", "H", "m3", "deg", "V", "oC", "F", "Wh", "s", "g", "min", "S", "none", "W", "VAr", "m2", "m", "VA"
        self.value1Unit = value1Unit

        #: Multiplier for value2. Values are: "M", "G", "d", "micro", "c", "p", "n", "T", "k", "m", "none"
        self.value2Multiplier = value2Multiplier

        super(BasicIntervalSchedule, self).__init__(*args, **kw_args)

    _attrs = ["startTime", "value1Multiplier", "value2Unit", "value1Unit", "value2Multiplier"]
    _attr_types = {"startTime": str, "value1Multiplier": str, "value2Unit": str, "value1Unit": str, "value2Multiplier": str}
    _defaults = {"startTime": '', "value1Multiplier": "M", "value2Unit": "N", "value1Unit": "N", "value2Multiplier": "M"}
    _enums = {"value1Multiplier": "UnitMultiplier", "value2Unit": "UnitSymbol", "value1Unit": "UnitSymbol", "value2Multiplier": "UnitMultiplier"}
    _refs = []
    _many_refs = []

