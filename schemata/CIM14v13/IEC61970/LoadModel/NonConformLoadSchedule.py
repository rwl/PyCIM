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

from CIM14v13.IEC61970.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class NonConformLoadSchedule(SeasonDayTypeSchedule):
    """An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)
    """

    def __init__(self, NonConformLoadGroup=None, **kw_args):
        """Initializes a new 'NonConformLoadSchedule' instance.

        @param NonConformLoadGroup: The NonConformLoadGroup where the NonConformLoadSchedule belongs.
        """
        self._NonConformLoadGroup = None
        self.NonConformLoadGroup = NonConformLoadGroup

        super(NonConformLoadSchedule, self).__init__(**kw_args)

    def getNonConformLoadGroup(self):
        """The NonConformLoadGroup where the NonConformLoadSchedule belongs.
        """
        return self._NonConformLoadGroup

    def setNonConformLoadGroup(self, value):
        if self._NonConformLoadGroup is not None:
            filtered = [x for x in self.NonConformLoadGroup.NonConformLoadSchedules if x != self]
            self._NonConformLoadGroup._NonConformLoadSchedules = filtered

        self._NonConformLoadGroup = value
        if self._NonConformLoadGroup is not None:
            self._NonConformLoadGroup._NonConformLoadSchedules.append(self)

    NonConformLoadGroup = property(getNonConformLoadGroup, setNonConformLoadGroup)

