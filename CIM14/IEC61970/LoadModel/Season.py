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

from CIM14.Element import Element

class Season(Element):
    """A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    def __init__(self, name="fall", startDate='', endDate='', SeasonDayTypeSchedules=None, *args, **kw_args):
        """Initialises a new 'Season' instance.

        @param name: Name of the Season Values are: "fall", "winter", "summer", "spring"
        @param startDate: Date season starts 
        @param endDate: Date season ends 
        @param SeasonDayTypeSchedules: Schedules that use this Season.
        """
        #: Name of the Season Values are: "fall", "winter", "summer", "spring"
        self.name = name

        #: Date season starts
        self.startDate = startDate

        #: Date season ends
        self.endDate = endDate

        self._SeasonDayTypeSchedules = []
        self.SeasonDayTypeSchedules = [] if SeasonDayTypeSchedules is None else SeasonDayTypeSchedules

        super(Season, self).__init__(*args, **kw_args)

    _attrs = ["name", "startDate", "endDate"]
    _attr_types = {"name": str, "startDate": str, "endDate": str}
    _defaults = {"name": "fall", "startDate": '', "endDate": ''}
    _enums = {"name": "SeasonName"}
    _refs = ["SeasonDayTypeSchedules"]
    _many_refs = ["SeasonDayTypeSchedules"]

    def getSeasonDayTypeSchedules(self):
        """Schedules that use this Season.
        """
        return self._SeasonDayTypeSchedules

    def setSeasonDayTypeSchedules(self, value):
        for x in self._SeasonDayTypeSchedules:
            x.Season = None
        for y in value:
            y._Season = self
        self._SeasonDayTypeSchedules = value

    SeasonDayTypeSchedules = property(getSeasonDayTypeSchedules, setSeasonDayTypeSchedules)

    def addSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj.Season = self

    def removeSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj.Season = None

