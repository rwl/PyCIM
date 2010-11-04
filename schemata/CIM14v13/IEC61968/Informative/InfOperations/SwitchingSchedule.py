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

class SwitchingSchedule(Document):
    """Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.
    """

    def __init__(self, reason='', interval=None, ScheduleSteps=None, Crews=None, WorkTask=None, *args, **kw_args):
        """Initializes a new 'SwitchingSchedule' instance.

        @param reason: Reason for switching. 
        @param interval: Interval between starting and completion of the switching.
        @param ScheduleSteps:
        @param Crews: All Crews executing this SwitchingSchedule.
        @param WorkTask:
        """
        #: Reason for switching.
        self.reason = reason

        self.interval = interval

        self._ScheduleSteps = []
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._WorkTask = None
        self.WorkTask = WorkTask

        super(SwitchingSchedule, self).__init__(*args, **kw_args)

    # Interval between starting and completion of the switching.
    interval = None

    def getScheduleSteps(self):
        
        return self._ScheduleSteps

    def setScheduleSteps(self, value):
        for x in self._ScheduleSteps:
            x._SwitchingSchedule = None
        for y in value:
            y._SwitchingSchedule = self
        self._ScheduleSteps = value

    ScheduleSteps = property(getScheduleSteps, setScheduleSteps)

    def addScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj._SwitchingSchedule = self
            self._ScheduleSteps.append(obj)

    def removeScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj._SwitchingSchedule = None
            self._ScheduleSteps.remove(obj)

    def getCrews(self):
        """All Crews executing this SwitchingSchedule.
        """
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.SwitchingSchedules if q != self]
            self._Crews._SwitchingSchedules = filtered
        for r in value:
            if self not in r._SwitchingSchedules:
                r._SwitchingSchedules.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._SwitchingSchedules:
                obj._SwitchingSchedules.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._SwitchingSchedules:
                obj._SwitchingSchedules.remove(self)
            self._Crews.remove(obj)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.SwitchingSchedules if x != self]
            self._WorkTask._SwitchingSchedules = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._SwitchingSchedules.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

