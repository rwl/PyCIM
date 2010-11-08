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

from CIM14.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class SeasonDayTypeSchedule(RegularIntervalSchedule):
    """The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.
    """

    def __init__(self, Season=None, DayType=None, *args, **kw_args):
        """Initialises a new 'SeasonDayTypeSchedule' instance.

        @param Season: Season for the Schedule.
        @param DayType: DayType for the Schedule.
        """
        self._Season = None
        self.Season = Season

        self._DayType = None
        self.DayType = DayType

        super(SeasonDayTypeSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Season", "DayType"]
    _many_refs = []

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
            self._Season._SeasonDayTypeSchedules.append(self)

    Season = property(getSeason, setSeason)

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
            self._DayType._SeasonDayTypeSchedules.append(self)

    DayType = property(getDayType, setDayType)

