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

class SwitchingSchedule(Document):
    """Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.
    """

    def __init__(self, reason='', ScheduleSteps=None, WorkTask=None, Crews=None, interval=None, *args, **kw_args):
        """Initialises a new 'SwitchingSchedule' instance.

        @param reason: Reason for switching. 
        @param ScheduleSteps:
        @param WorkTask:
        @param Crews: All Crews executing this SwitchingSchedule.
        @param interval: Interval between starting and completion of the switching.
        """
        #: Reason for switching.
        self.reason = reason

        self._ScheduleSteps = []
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self.interval = interval

        super(SwitchingSchedule, self).__init__(*args, **kw_args)

    _attrs = ["reason"]
    _attr_types = {"reason": str}
    _defaults = {"reason": ''}
    _enums = {}
    _refs = ["ScheduleSteps", "WorkTask", "Crews", "interval"]
    _many_refs = ["ScheduleSteps", "Crews"]

    def getScheduleSteps(self):
        
        return self._ScheduleSteps

    def setScheduleSteps(self, value):
        for x in self._ScheduleSteps:
            x.SwitchingSchedule = None
        for y in value:
            y._SwitchingSchedule = self
        self._ScheduleSteps = value

    ScheduleSteps = property(getScheduleSteps, setScheduleSteps)

    def addScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj.SwitchingSchedule = self

    def removeScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            obj.SwitchingSchedule = None

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.SwitchingSchedules if x != self]
            self._WorkTask._SwitchingSchedules = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._SwitchingSchedules:
                self._WorkTask._SwitchingSchedules.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

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

    # Interval between starting and completion of the switching.
    interval = None

