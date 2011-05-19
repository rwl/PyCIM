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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ScheduledEvent(IdentifiedObject):
    """Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.
    """

    def __init__(self, duration=0.0, category='', Document=None, ActivityRecord=None, status=None, TimePoint=None, ScheduleParameterInfo=None, Assets=None, *args, **kw_args):
        """Initialises a new 'ScheduledEvent' instance.

        @param duration: Duration of the scheduled event, for example, the time to ramp between values. 
        @param category: Category of scheduled event. 
        @param Document:
        @param ActivityRecord:
        @param status:
        @param TimePoint:
        @param ScheduleParameterInfo:
        @param Assets:
        """
        #: Duration of the scheduled event, for example, the time to ramp between values.
        self.duration = duration

        #: Category of scheduled event.
        self.category = category

        self._Document = None
        self.Document = Document

        self._ActivityRecord = None
        self.ActivityRecord = ActivityRecord

        self.status = status

        self._TimePoint = None
        self.TimePoint = TimePoint

        self._ScheduleParameterInfo = None
        self.ScheduleParameterInfo = ScheduleParameterInfo

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(ScheduledEvent, self).__init__(*args, **kw_args)

    _attrs = ["duration", "category"]
    _attr_types = {"duration": float, "category": str}
    _defaults = {"duration": 0.0, "category": ''}
    _enums = {}
    _refs = ["Document", "ActivityRecord", "status", "TimePoint", "ScheduleParameterInfo", "Assets"]
    _many_refs = ["Assets"]

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ScheduledEvents if x != self]
            self._Document._ScheduledEvents = filtered

        self._Document = value
        if self._Document is not None:
            if self not in self._Document._ScheduledEvents:
                self._Document._ScheduledEvents.append(self)

    Document = property(getDocument, setDocument)

    def getActivityRecord(self):
        
        return self._ActivityRecord

    def setActivityRecord(self, value):
        if self._ActivityRecord is not None:
            self._ActivityRecord._ScheduledEvent = None

        self._ActivityRecord = value
        if self._ActivityRecord is not None:
            self._ActivityRecord.ScheduledEvent = None
            self._ActivityRecord._ScheduledEvent = self

    ActivityRecord = property(getActivityRecord, setActivityRecord)

    status = None

    def getTimePoint(self):
        
        return self._TimePoint

    def setTimePoint(self, value):
        if self._TimePoint is not None:
            filtered = [x for x in self.TimePoint.ScheduledEvents if x != self]
            self._TimePoint._ScheduledEvents = filtered

        self._TimePoint = value
        if self._TimePoint is not None:
            if self not in self._TimePoint._ScheduledEvents:
                self._TimePoint._ScheduledEvents.append(self)

    TimePoint = property(getTimePoint, setTimePoint)

    def getScheduleParameterInfo(self):
        
        return self._ScheduleParameterInfo

    def setScheduleParameterInfo(self, value):
        if self._ScheduleParameterInfo is not None:
            filtered = [x for x in self.ScheduleParameterInfo.ScheduledEvents if x != self]
            self._ScheduleParameterInfo._ScheduledEvents = filtered

        self._ScheduleParameterInfo = value
        if self._ScheduleParameterInfo is not None:
            if self not in self._ScheduleParameterInfo._ScheduledEvents:
                self._ScheduleParameterInfo._ScheduledEvents.append(self)

    ScheduleParameterInfo = property(getScheduleParameterInfo, setScheduleParameterInfo)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.ScheduledEvents if q != self]
            self._Assets._ScheduledEvents = filtered
        for r in value:
            if self not in r._ScheduledEvents:
                r._ScheduledEvents.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._ScheduledEvents:
                obj._ScheduledEvents.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._ScheduledEvents:
                obj._ScheduledEvents.remove(self)
            self._Assets.remove(obj)

