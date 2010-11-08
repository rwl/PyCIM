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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time.
    """

    def __init__(self, value2Multiplier="k", value2Unit="N", value1Multiplier="k", value1Unit="N", startTime='', *args, **kw_args):
        """Initialises a new 'BasicIntervalSchedule' instance.

        @param value2Multiplier: Multiplier for value2. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param value2Unit: Value2 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "_C", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param value1Multiplier: Multiplier for value1. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        @param value1Unit: Value1 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "_C", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        @param startTime: The time for the first time point. 
        """
        #: Multiplier for value2. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.value2Multiplier = value2Multiplier

        #: Value2 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "_C", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
        self.value2Unit = value2Unit

        #: Multiplier for value1. Values are: "k", "d", "n", "M", "none", "G", "micro", "T", "c", "m", "p"
        self.value1Multiplier = value1Multiplier

        #: Value1 units of measure. Values are: "N", "VArh", "VA", "none", "m3", "kg/J", "deg", "W/Hz", "g", "Wh", "W/s", "Pa", "V/VAr", "ohm", "h", "F", "H", "m2", "VAr", "A", "rad", "s", "S", "VAh", "Hz", "_C", "s-1", "min", "J", "Hz-1", "J/s", "m", "W", "V"
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

