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

from CIM14v13.IEC61970.Core.Curve import Curve

class AvailableTransmissionCapacity(Curve):
    """Amount of possible flow by direction.
    """

    def __init__(self, ScheduleFor=None, **kw_args):
        """Initializes a new 'AvailableTransmissionCapacity' instance.

        @param ScheduleFor: A transmission schedule posts the available transmission capacity for a transmission line.
        """
        self._ScheduleFor = []
        self.ScheduleFor = [] if ScheduleFor is None else ScheduleFor

        super(AvailableTransmissionCapacity, self).__init__(**kw_args)

    def getScheduleFor(self):
        """A transmission schedule posts the available transmission capacity for a transmission line.
        """
        return self._ScheduleFor

    def setScheduleFor(self, value):
        for p in self._ScheduleFor:
            filtered = [q for q in p.ScheduledBy if q != self]
            self._ScheduleFor._ScheduledBy = filtered
        for r in value:
            if self not in r._ScheduledBy:
                r._ScheduledBy.append(self)
        self._ScheduleFor = value

    ScheduleFor = property(getScheduleFor, setScheduleFor)

    def addScheduleFor(self, *ScheduleFor):
        for obj in ScheduleFor:
            if self not in obj._ScheduledBy:
                obj._ScheduledBy.append(self)
            self._ScheduleFor.append(obj)

    def removeScheduleFor(self, *ScheduleFor):
        for obj in ScheduleFor:
            if self in obj._ScheduledBy:
                obj._ScheduledBy.remove(self)
            self._ScheduleFor.remove(obj)

