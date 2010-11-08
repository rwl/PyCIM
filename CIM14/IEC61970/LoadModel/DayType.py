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

class DayType(IdentifiedObject):
    """Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2
    """

    def __init__(self, SeasonDayTypeSchedules=None, *args, **kw_args):
        """Initialises a new 'DayType' instance.

        @param SeasonDayTypeSchedules: Schedules that use this DayType.
        """
        self._SeasonDayTypeSchedules = []
        self.SeasonDayTypeSchedules = [] if SeasonDayTypeSchedules is None else SeasonDayTypeSchedules

        super(DayType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SeasonDayTypeSchedules"]
    _many_refs = ["SeasonDayTypeSchedules"]

    def getSeasonDayTypeSchedules(self):
        """Schedules that use this DayType.
        """
        return self._SeasonDayTypeSchedules

    def setSeasonDayTypeSchedules(self, value):
        for x in self._SeasonDayTypeSchedules:
            x._DayType = None
        for y in value:
            y._DayType = self
        self._SeasonDayTypeSchedules = value

    SeasonDayTypeSchedules = property(getSeasonDayTypeSchedules, setSeasonDayTypeSchedules)

    def addSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj._DayType = self
            self._SeasonDayTypeSchedules.append(obj)

    def removeSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj._DayType = None
            self._SeasonDayTypeSchedules.remove(obj)

