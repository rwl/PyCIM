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

class ScheduledEvent(IdentifiedObject):
    """Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.
    """

    def __init__(self, duration=0.0, category='', Document=None, Assets=None, ActivityRecord=None, ScheduleParameterInfo=None, status=None, TimePoint=None, *args, **kw_args):
        """Initializes a new 'ScheduledEvent' instance.

        @param duration: Duration of the scheduled event, for example, the time to ramp between values. 
        @param category: Category of scheduled event. 
        @param Document:
        @param Assets:
        @param ActivityRecord:
        @param ScheduleParameterInfo:
        @param status:
        @param TimePoint:
        """
        #: Duration of the scheduled event, for example, the time to ramp between values. 
        self.duration = duration

        #: Category of scheduled event. 
        self.category = category

        self._Document = None
        self.Document = Document

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._ActivityRecord = None
        self.ActivityRecord = ActivityRecord

        self._ScheduleParameterInfo = None
        self.ScheduleParameterInfo = ScheduleParameterInfo

        self.status = status

        self._TimePoint = None
        self.TimePoint = TimePoint

        super(ScheduledEvent, self).__init__(*args, **kw_args)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ScheduledEvents if x != self]
            self._Document._ScheduledEvents = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._ScheduledEvents.append(self)

    Document = property(getDocument, setDocument)

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

    def getActivityRecord(self):
        
        return self._ActivityRecord

    def setActivityRecord(self, value):
        if self._ActivityRecord is not None:
            self._ActivityRecord._ScheduledEvent = None

        self._ActivityRecord = value
        if self._ActivityRecord is not None:
            self._ActivityRecord._ScheduledEvent = self

    ActivityRecord = property(getActivityRecord, setActivityRecord)

    def getScheduleParameterInfo(self):
        
        return self._ScheduleParameterInfo

    def setScheduleParameterInfo(self, value):
        if self._ScheduleParameterInfo is not None:
            filtered = [x for x in self.ScheduleParameterInfo.ScheduledEvents if x != self]
            self._ScheduleParameterInfo._ScheduledEvents = filtered

        self._ScheduleParameterInfo = value
        if self._ScheduleParameterInfo is not None:
            self._ScheduleParameterInfo._ScheduledEvents.append(self)

    ScheduleParameterInfo = property(getScheduleParameterInfo, setScheduleParameterInfo)

    status = None

    def getTimePoint(self):
        
        return self._TimePoint

    def setTimePoint(self, value):
        if self._TimePoint is not None:
            filtered = [x for x in self.TimePoint.ScheduledEvents if x != self]
            self._TimePoint._ScheduledEvents = filtered

        self._TimePoint = value
        if self._TimePoint is not None:
            self._TimePoint._ScheduledEvents.append(self)

    TimePoint = property(getTimePoint, setTimePoint)

