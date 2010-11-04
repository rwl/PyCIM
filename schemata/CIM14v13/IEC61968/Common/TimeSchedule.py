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

from CIM14v13.IEC61968.Common.Document import Document

class TimeSchedule(Document):
    """Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).
    """

    def __init__(self, disabled=False, offset=0.0, recurrencePattern='', recurrencePeriod=0.0, TimePoints=None, scheduleInterval=None, **kw_args):
        """Initializes a new 'TimeSchedule' instance.

        @param disabled: True if this schedule is deactivated (disabled). 
        @param offset: The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour. 
        @param recurrencePattern: Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.). 
        @param recurrencePeriod: Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min). 
        @param TimePoints: Sequence of time points belonging to this time schedule.
        @param scheduleInterval: Schedule date and time interval.
        """
        #: True if this schedule is deactivated (disabled).
        self.disabled = disabled

        #: The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour.
        self.offset = offset

        #: Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.).
        self.recurrencePattern = recurrencePattern

        #: Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min).
        self.recurrencePeriod = recurrencePeriod

        self._TimePoints = []
        self.TimePoints = [] if TimePoints is None else TimePoints

        self.scheduleInterval = scheduleInterval

        super(TimeSchedule, self).__init__(**kw_args)

    def getTimePoints(self):
        """Sequence of time points belonging to this time schedule.
        """
        return self._TimePoints

    def setTimePoints(self, value):
        for x in self._TimePoints:
            x._TimeSchedule = None
        for y in value:
            y._TimeSchedule = self
        self._TimePoints = value

    TimePoints = property(getTimePoints, setTimePoints)

    def addTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj._TimeSchedule = self
            self._TimePoints.append(obj)

    def removeTimePoints(self, *TimePoints):
        for obj in TimePoints:
            obj._TimeSchedule = None
            self._TimePoints.remove(obj)

    # Schedule date and time interval.
    scheduleInterval = None

