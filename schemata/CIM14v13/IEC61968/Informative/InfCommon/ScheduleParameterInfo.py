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

class ScheduleParameterInfo(IdentifiedObject):
    """Schedule parameters for an activity that is to occur, is occurring, or has completed.
    """

    def __init__(self, ForInspectionDataSet=None, estimatedWindow=None, ScheduledEvents=None, status=None, Documents=None, requestedWindow=None, *args, **kw_args):
        """Initializes a new 'ScheduleParameterInfo' instance.

        @param ForInspectionDataSet:
        @param estimatedWindow: Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
        @param ScheduledEvents:
        @param status:
        @param Documents:
        @param requestedWindow: Requested date and time interval for activity execution.
        """
        self._ForInspectionDataSet = None
        self.ForInspectionDataSet = ForInspectionDataSet

        self.estimatedWindow = estimatedWindow

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self.status = status

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self.requestedWindow = requestedWindow

        super(ScheduleParameterInfo, self).__init__(*args, **kw_args)

    def getForInspectionDataSet(self):
        
        return self._ForInspectionDataSet

    def setForInspectionDataSet(self, value):
        if self._ForInspectionDataSet is not None:
            filtered = [x for x in self.ForInspectionDataSet.AccordingToSchedules if x != self]
            self._ForInspectionDataSet._AccordingToSchedules = filtered

        self._ForInspectionDataSet = value
        if self._ForInspectionDataSet is not None:
            self._ForInspectionDataSet._AccordingToSchedules.append(self)

    ForInspectionDataSet = property(getForInspectionDataSet, setForInspectionDataSet)

    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    estimatedWindow = None

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for x in self._ScheduledEvents:
            x._ScheduleParameterInfo = None
        for y in value:
            y._ScheduleParameterInfo = self
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj._ScheduleParameterInfo = self
            self._ScheduledEvents.append(obj)

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj._ScheduleParameterInfo = None
            self._ScheduledEvents.remove(obj)

    status = None

    def getDocuments(self):
        
        return self._Documents

    def setDocuments(self, value):
        for p in self._Documents:
            filtered = [q for q in p.ScheduleParameterInfos if q != self]
            self._Documents._ScheduleParameterInfos = filtered
        for r in value:
            if self not in r._ScheduleParameterInfos:
                r._ScheduleParameterInfos.append(self)
        self._Documents = value

    Documents = property(getDocuments, setDocuments)

    def addDocuments(self, *Documents):
        for obj in Documents:
            if self not in obj._ScheduleParameterInfos:
                obj._ScheduleParameterInfos.append(self)
            self._Documents.append(obj)

    def removeDocuments(self, *Documents):
        for obj in Documents:
            if self in obj._ScheduleParameterInfos:
                obj._ScheduleParameterInfos.remove(self)
            self._Documents.remove(obj)

    # Requested date and time interval for activity execution.
    requestedWindow = None

