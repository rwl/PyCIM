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

class TimePoint(IdentifiedObject):
    """A point in time within a sequence of points in time relative to a TimeSchedule.
    """

    def __init__(self, relativeTimeInterval=0.0, absoluteTime='', sequenceNumber=0, window=None, ScheduledEvents=None, TimeSchedule=None, status=None, **kw_args):
        """Initializes a new 'TimePoint' instance.

        @param relativeTimeInterval: (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'. 
        @param absoluteTime: Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived. 
        @param sequenceNumber: (if sequence-based) Relative sequence number for this time point. 
        @param window: Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
        @param ScheduledEvents:
        @param TimeSchedule: Time schedule owning this time point.
        @param status: Status of this time point.
        """
        #: (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'.
        self.relativeTimeInterval = relativeTimeInterval

        #: Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived.
        self.absoluteTime = absoluteTime

        #: (if sequence-based) Relative sequence number for this time point.
        self.sequenceNumber = sequenceNumber

        self.window = window

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self._TimeSchedule = None
        self.TimeSchedule = TimeSchedule

        self.status = status

        super(TimePoint, self).__init__(**kw_args)

    # Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
    window = None

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for x in self._ScheduledEvents:
            x._TimePoint = None
        for y in value:
            y._TimePoint = self
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj._TimePoint = self
            self._ScheduledEvents.append(obj)

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj._TimePoint = None
            self._ScheduledEvents.remove(obj)

    def getTimeSchedule(self):
        """Time schedule owning this time point.
        """
        return self._TimeSchedule

    def setTimeSchedule(self, value):
        if self._TimeSchedule is not None:
            filtered = [x for x in self.TimeSchedule.TimePoints if x != self]
            self._TimeSchedule._TimePoints = filtered

        self._TimeSchedule = value
        if self._TimeSchedule is not None:
            self._TimeSchedule._TimePoints.append(self)

    TimeSchedule = property(getTimeSchedule, setTimeSchedule)

    # Status of this time point.
    status = None

