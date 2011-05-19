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

class ScheduleParameterInfo(IdentifiedObject):
    """Schedule parameters for an activity that is to occur, is occurring, or has completed.Schedule parameters for an activity that is to occur, is occurring, or has completed.
    """

    def __init__(self, ForInspectionDataSet=None, requestedWindow=None, Documents=None, estimatedWindow=None, ScheduledEvents=None, status=None, *args, **kw_args):
        """Initialises a new 'ScheduleParameterInfo' instance.

        @param ForInspectionDataSet:
        @param requestedWindow: Requested date and time interval for activity execution.
        @param Documents:
        @param estimatedWindow: Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
        @param ScheduledEvents:
        @param status:
        """
        self._ForInspectionDataSet = None
        self.ForInspectionDataSet = ForInspectionDataSet

        self.requestedWindow = requestedWindow

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self.estimatedWindow = estimatedWindow

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self.status = status

        super(ScheduleParameterInfo, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ForInspectionDataSet", "requestedWindow", "Documents", "estimatedWindow", "ScheduledEvents", "status"]
    _many_refs = ["Documents", "ScheduledEvents"]

    def getForInspectionDataSet(self):
        
        return self._ForInspectionDataSet

    def setForInspectionDataSet(self, value):
        if self._ForInspectionDataSet is not None:
            filtered = [x for x in self.ForInspectionDataSet.AccordingToSchedules if x != self]
            self._ForInspectionDataSet._AccordingToSchedules = filtered

        self._ForInspectionDataSet = value
        if self._ForInspectionDataSet is not None:
            if self not in self._ForInspectionDataSet._AccordingToSchedules:
                self._ForInspectionDataSet._AccordingToSchedules.append(self)

    ForInspectionDataSet = property(getForInspectionDataSet, setForInspectionDataSet)

    # Requested date and time interval for activity execution.
    requestedWindow = None

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

    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    estimatedWindow = None

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for x in self._ScheduledEvents:
            x.ScheduleParameterInfo = None
        for y in value:
            y._ScheduleParameterInfo = self
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj.ScheduleParameterInfo = self

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj.ScheduleParameterInfo = None

    status = None

