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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BasicIntervalSchedule(IdentifiedObject):
    """Schedule of values at points in time.
    """

    def __init__(self, value2Multiplier='m', value1Unit='m2', value2Unit='m2', value1Multiplier='m', startTime='', *args, **kw_args):
        """Initializes a new 'BasicIntervalSchedule' instance.

        @param value2Multiplier: Multiplier for value2. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param value1Unit: Value1 units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param value2Unit: Value2 units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        @param value1Multiplier: Multiplier for value1. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        @param startTime: The time for the first time point. 
        """
        #: Multiplier for value2. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.value2Multiplier = value2Multiplier

        #: Value1 units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.value1Unit = value1Unit

        #: Value2 units of measure. Values are: "m2", "VAr", "m3", "g", "VArh", "F", "Hz", "deg", "W/s", "V", "V/VAr", "rad", "min", "ohm", "m", "H", "s", "W/Hz", "kg/J", "Wh", "VA", "S", "none", "ºC", "s-1", "J", "N", "h", "J/s", "Hz-1", "Pa", "W", "A", "VAh"
        self.value2Unit = value2Unit

        #: Multiplier for value1. Values are: "m", "T", "p", "k", "M", "micro", "n", "d", "G", "c", "none"
        self.value1Multiplier = value1Multiplier

        #: The time for the first time point. 
        self.startTime = startTime

        super(BasicIntervalSchedule, self).__init__(*args, **kw_args)

