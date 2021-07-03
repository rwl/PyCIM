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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TimePoint(IdentifiedObject):
    """A point in time within a sequence of points in time relative to a TimeSchedule.A point in time within a sequence of points in time relative to a TimeSchedule.
    """

    def __init__(self, dateTime='', sequenceNumber=0, relativeTimeInterval=0.0, status=None, window=None, TimeSchedule=None, ScheduledEvents=None, *args, **kw_args):
        """Initialises a new 'TimePoint' instance.

        @param dateTime: Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived. 
        @param sequenceNumber: (if sequence-based) Relative sequence number for this time point. 
        @param relativeTimeInterval: (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'. 
        @param status: Status of this time point.
        @param window: Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
        @param TimeSchedule: Time schedule owning this time point.
        @param ScheduledEvents:
        """
        #: Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived.
        self.dateTime = dateTime

        #: (if sequence-based) Relative sequence number for this time point.
        self.sequenceNumber = sequenceNumber

        #: (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'.
        self.relativeTimeInterval = relativeTimeInterval

        self.status = status

        self.window = window

        self._TimeSchedule = None
        self.TimeSchedule = TimeSchedule

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        super(TimePoint, self).__init__(*args, **kw_args)

    _attrs = ["dateTime", "sequenceNumber", "relativeTimeInterval"]
    _attr_types = {"dateTime": str, "sequenceNumber": int, "relativeTimeInterval": float}
    _defaults = {"dateTime": '', "sequenceNumber": 0, "relativeTimeInterval": 0.0}
    _enums = {}
    _refs = ["status", "window", "TimeSchedule", "ScheduledEvents"]
    _many_refs = ["ScheduledEvents"]

    # Status of this time point.
    status = None

    # Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
    window = None

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
            if self not in self._TimeSchedule._TimePoints:
                self._TimeSchedule._TimePoints.append(self)

    TimeSchedule = property(getTimeSchedule, setTimeSchedule)

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for x in self._ScheduledEvents:
            x.TimePoint = None
        for y in value:
            y._TimePoint = self
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj.TimePoint = self

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj.TimePoint = None

