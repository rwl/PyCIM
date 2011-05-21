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

from CIM14.ENTSOE.Equipment.Core.RegularIntervalSchedule import RegularIntervalSchedule

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    def __init__(self, DayType=None, Season=None, *args, **kw_args):
        """Initialises a new 'SeasonDayTypeSchedule' instance.

        @param DayType: DayType for the Schedule.
        @param Season: Season for the Schedule.
        """
        self._DayType = None
        self.DayType = DayType

        self._Season = None
        self.Season = Season

        super(SeasonDayTypeSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["DayType", "Season"]
    _many_refs = []

    def getDayType(self):
        """DayType for the Schedule.
        """
        return self._DayType

    def setDayType(self, value):
        if self._DayType is not None:
            filtered = [x for x in self.DayType.SeasonDayTypeSchedules if x != self]
            self._DayType._SeasonDayTypeSchedules = filtered

        self._DayType = value
        if self._DayType is not None:
            if self not in self._DayType._SeasonDayTypeSchedules:
                self._DayType._SeasonDayTypeSchedules.append(self)

    DayType = property(getDayType, setDayType)

    def getSeason(self):
        """Season for the Schedule.
        """
        return self._Season

    def setSeason(self, value):
        if self._Season is not None:
            filtered = [x for x in self.Season.SeasonDayTypeSchedules if x != self]
            self._Season._SeasonDayTypeSchedules = filtered

        self._Season = value
        if self._Season is not None:
            if self not in self._Season._SeasonDayTypeSchedules:
                self._Season._SeasonDayTypeSchedules.append(self)

    Season = property(getSeason, setSeason)

