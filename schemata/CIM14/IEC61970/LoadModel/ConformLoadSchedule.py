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

from CIM14.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class ConformLoadSchedule(SeasonDayTypeSchedule):
    """A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.
    """

    def __init__(self, ConformLoadGroup=None, **kw_args):
        """Initializes a new 'ConformLoadSchedule' instance.

        @param ConformLoadGroup: The ConformLoadGroup where the ConformLoadSchedule belongs.
        """
        self._ConformLoadGroup = None
        self.ConformLoadGroup = ConformLoadGroup

        super(ConformLoadSchedule, self).__init__(**kw_args)

    def getConformLoadGroup(self):
        """The ConformLoadGroup where the ConformLoadSchedule belongs.
        """
        return self._ConformLoadGroup

    def setConformLoadGroup(self, value):
        if self._ConformLoadGroup is not None:
            filtered = [x for x in self.ConformLoadGroup.ConformLoadSchedules if x != self]
            self._ConformLoadGroup._ConformLoadSchedules = filtered

        self._ConformLoadGroup = value
        if self._ConformLoadGroup is not None:
            self._ConformLoadGroup._ConformLoadSchedules.append(self)

    ConformLoadGroup = property(getConformLoadGroup, setConformLoadGroup)

