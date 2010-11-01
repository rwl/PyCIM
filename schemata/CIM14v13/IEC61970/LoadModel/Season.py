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

from CIM14v13.Element import Element

class Season(Element):
    """A specified time period of the year, e.g., Spring, Summer, Fall, Winter
    """

    def __init__(self, name='spring', startDate='', endDate='', CapacityBenefitMargin=None, ViolationLimits=None, SeasonDayTypeSchedules=None, *args, **kw_args):
        """Initializes a new 'Season' instance.

        @param name: Name of the Season Values are: "spring", "fall", "winter", "summer"
        @param startDate: Date season starts 
        @param endDate: Date season ends 
        @param CapacityBenefitMargin: Capacity Benefit Margin may differ based on the season
        @param ViolationLimits: Limits may differ based on the season
        @param SeasonDayTypeSchedules: Schedules that use this Season.
        """
        #: Name of the Season Values are: "spring", "fall", "winter", "summer"
        self.name = name

        #: Date season starts 
        self.startDate = startDate

        #: Date season ends 
        self.endDate = endDate

        self._CapacityBenefitMargin = []
        self.CapacityBenefitMargin = [] if CapacityBenefitMargin is None else CapacityBenefitMargin

        self._ViolationLimits = []
        self.ViolationLimits = [] if ViolationLimits is None else ViolationLimits

        self._SeasonDayTypeSchedules = []
        self.SeasonDayTypeSchedules = [] if SeasonDayTypeSchedules is None else SeasonDayTypeSchedules

        super(Season, self).__init__(*args, **kw_args)

    def getCapacityBenefitMargin(self):
        """Capacity Benefit Margin may differ based on the season
        """
        return self._CapacityBenefitMargin

    def setCapacityBenefitMargin(self, value):
        for x in self._CapacityBenefitMargin:
            x._Season = None
        for y in value:
            y._Season = self
        self._CapacityBenefitMargin = value

    CapacityBenefitMargin = property(getCapacityBenefitMargin, setCapacityBenefitMargin)

    def addCapacityBenefitMargin(self, *CapacityBenefitMargin):
        for obj in CapacityBenefitMargin:
            obj._Season = self
            self._CapacityBenefitMargin.append(obj)

    def removeCapacityBenefitMargin(self, *CapacityBenefitMargin):
        for obj in CapacityBenefitMargin:
            obj._Season = None
            self._CapacityBenefitMargin.remove(obj)

    def getViolationLimits(self):
        """Limits may differ based on the season
        """
        return self._ViolationLimits

    def setViolationLimits(self, value):
        for x in self._ViolationLimits:
            x._Season = None
        for y in value:
            y._Season = self
        self._ViolationLimits = value

    ViolationLimits = property(getViolationLimits, setViolationLimits)

    def addViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            obj._Season = self
            self._ViolationLimits.append(obj)

    def removeViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            obj._Season = None
            self._ViolationLimits.remove(obj)

    def getSeasonDayTypeSchedules(self):
        """Schedules that use this Season.
        """
        return self._SeasonDayTypeSchedules

    def setSeasonDayTypeSchedules(self, value):
        for x in self._SeasonDayTypeSchedules:
            x._Season = None
        for y in value:
            y._Season = self
        self._SeasonDayTypeSchedules = value

    SeasonDayTypeSchedules = property(getSeasonDayTypeSchedules, setSeasonDayTypeSchedules)

    def addSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj._Season = self
            self._SeasonDayTypeSchedules.append(obj)

    def removeSeasonDayTypeSchedules(self, *SeasonDayTypeSchedules):
        for obj in SeasonDayTypeSchedules:
            obj._Season = None
            self._SeasonDayTypeSchedules.remove(obj)

