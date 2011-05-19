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

from CIM15.IEC61968.Common.Document import Document

class TimeSchedule(Document):
    """Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).
    """

    def __init__(self, recurrencePeriod=0.0, disabled=False, offset=0.0, recurrencePattern='', TimePoints=None, scheduleInterval=None, *args, **kw_args):
        """Initialises a new 'TimeSchedule' instance.

        @param recurrencePeriod: Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min). 
        @param disabled: True if this schedule is deactivated (disabled). 
        @param offset: The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour. 
        @param recurrencePattern: Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.). 
        @param TimePoints: Sequence of time points belonging to this time schedule.
        @param scheduleInterval: Schedule date and time interval.
        """
        #: Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min).
        self.recurrencePeriod = recurrencePeriod

        #: True if this schedule is deactivated (disabled).
        self.disabled = disabled

        #: The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour.
        self.offset = offset

        #: Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.).
        self.recurrencePattern = recurrencePattern

        self._TimePoints = []
        self.TimePoints = [] if TimePoints is None else TimePoints

        self.scheduleInterval = scheduleInterval

        super(TimeSchedule, self).__init__(*args, **kw_args)

    _attrs = ["recurrencePeriod", "disabled", "offset", "recurrencePattern"]
    _attr_types = {"recurrencePeriod": float, "disabled": bool, "offset": float, "recurrencePattern": str}
    _defaults = {"recurrencePeriod": 0.0, "disabled": False, "offset": 0.0, "recurrencePattern": ''}
    _enums = {}
    _refs = ["TimePoints", "scheduleInterval"]
    _many_refs = ["TimePoints"]

    def getTimePoints(self):
        """Sequence of time points belonging to this time schedule.
        """
        return self._TimePoints

    def setTimePoints(self, value):
        for x in self._TimePoints:
            x.TimeSchedule = None
        for y in value:
            y._TimeSchedule = self
        self._TimePoints = value

    TimePoints = property(getTimePoints, setTimePoints)

    def addTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj.TimeSchedule = self

    def removeTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj.TimeSchedule = None

    # Schedule date and time interval.
    scheduleInterval = None

