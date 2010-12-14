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

class SwitchSchedule(SeasonDayTypeSchedule):
    """A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.
    """

    def __init__(self, Switch=None, *args, **kw_args):
        """Initialises a new 'SwitchSchedule' instance.

        @param Switch: A SwitchSchedule is associated with a Switch.
        """
        self._Switch = None
        self.Switch = Switch

        super(SwitchSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Switch"]
    _many_refs = []

    def getSwitch(self):
        """A SwitchSchedule is associated with a Switch.
        """
        return self._Switch

    def setSwitch(self, value):
        if self._Switch is not None:
            filtered = [x for x in self.Switch.SwitchSchedules if x != self]
            self._Switch._SwitchSchedules = filtered

        self._Switch = value
        if self._Switch is not None:
            if self not in self._Switch._SwitchSchedules:
                self._Switch._SwitchSchedules.append(self)

    Switch = property(getSwitch, setSwitch)

