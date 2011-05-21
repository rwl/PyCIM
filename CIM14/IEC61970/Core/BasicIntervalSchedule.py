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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time.
    """

    def __init__(self, value2Multiplier="k", value2Unit="N", value1Multiplier="k", value1Unit="N", startTime='', *args, **kw_args):
        """Initialises a new 'BasicIntervalSchedule' instance.

        @param value2Multiplier: Multiplier for value2. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param value2Unit: Value2 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param value1Multiplier: Multiplier for value1. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param value1Unit: Value1 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param startTime: The time for the first time point. 
        """
        #: Multiplier for value2. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.value2Multiplier = value2Multiplier

        #: Value2 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.value2Unit = value2Unit

        #: Multiplier for value1. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.value1Multiplier = value1Multiplier

        #: Value1 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "oC", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.value1Unit = value1Unit

        #: The time for the first time point.
        self.startTime = startTime

        super(BasicIntervalSchedule, self).__init__(*args, **kw_args)

    _attrs = ["value2Multiplier", "value2Unit", "value1Multiplier", "value1Unit", "startTime"]
    _attr_types = {"value2Multiplier": str, "value2Unit": str, "value1Multiplier": str, "value1Unit": str, "startTime": str}
    _defaults = {"value2Multiplier": "k", "value2Unit": "N", "value1Multiplier": "k", "value1Unit": "N", "startTime": ''}
    _enums = {"value2Multiplier": "UnitMultiplier", "value2Unit": "UnitSymbol", "value1Multiplier": "UnitMultiplier", "value1Unit": "UnitSymbol"}
    _refs = []
    _many_refs = []

