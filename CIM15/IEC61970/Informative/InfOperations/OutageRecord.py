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

class OutageRecord(Document):
    """A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a trouble call system by grouping customer calls. This has an associated outage step for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a switching schedule which complements the outage record and records the crew and any planned work. In other systems, it may be acceptable to manage outages including new work tasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a trouble call system by grouping customer calls. This has an associated outage step for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a switching schedule which complements the outage record and records the crew and any planned work. In other systems, it may be acceptable to manage outages including new work tasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.
    """

    def __init__(self, endDateTime='', isPlanned=False, damageCode='', actionTaken='', mode='', OutageCodes=None, OutageReport=None, OutageSteps=None, *args, **kw_args):
        """Initialises a new 'OutageRecord' instance.

        @param endDateTime: Date and time restoration was completed for all customers impacted by this outage. 
        @param isPlanned: True if planned, false otherwise (for example due to a breaker trip). 
        @param damageCode: The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none. 
        @param actionTaken: Overall action taken to resolve outage (details are in 'WorkTasks'). 
        @param mode: Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime. 
        @param OutageCodes: Multiple outage codes may apply to an outage record.
        @param OutageReport:
        @param OutageSteps:
        """
        #: Date and time restoration was completed for all customers impacted by this outage.
        self.endDateTime = endDateTime

        #: True if planned, false otherwise (for example due to a breaker trip).
        self.isPlanned = isPlanned

        #: The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none.
        self.damageCode = damageCode

        #: Overall action taken to resolve outage (details are in 'WorkTasks').
        self.actionTaken = actionTaken

        #: Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime.
        self.mode = mode

        self._OutageCodes = []
        self.OutageCodes = [] if OutageCodes is None else OutageCodes

        self._OutageReport = None
        self.OutageReport = OutageReport

        self._OutageSteps = []
        self.OutageSteps = [] if OutageSteps is None else OutageSteps

        super(OutageRecord, self).__init__(*args, **kw_args)

    _attrs = ["endDateTime", "isPlanned", "damageCode", "actionTaken", "mode"]
    _attr_types = {"endDateTime": str, "isPlanned": bool, "damageCode": str, "actionTaken": str, "mode": str}
    _defaults = {"endDateTime": '', "isPlanned": False, "damageCode": '', "actionTaken": '', "mode": ''}
    _enums = {}
    _refs = ["OutageCodes", "OutageReport", "OutageSteps"]
    _many_refs = ["OutageCodes", "OutageSteps"]

    def getOutageCodes(self):
        """Multiple outage codes may apply to an outage record.
        """
        return self._OutageCodes

    def setOutageCodes(self, value):
        for p in self._OutageCodes:
            filtered = [q for q in p.OutageRecords if q != self]
            self._OutageCodes._OutageRecords = filtered
        for r in value:
            if self not in r._OutageRecords:
                r._OutageRecords.append(self)
        self._OutageCodes = value

    OutageCodes = property(getOutageCodes, setOutageCodes)

    def addOutageCodes(self, *OutageCodes):
        for obj in OutageCodes:
            if self not in obj._OutageRecords:
                obj._OutageRecords.append(self)
            self._OutageCodes.append(obj)

    def removeOutageCodes(self, *OutageCodes):
        for obj in OutageCodes:
            if self in obj._OutageRecords:
                obj._OutageRecords.remove(self)
            self._OutageCodes.remove(obj)

    def getOutageReport(self):
        
        return self._OutageReport

    def setOutageReport(self, value):
        if self._OutageReport is not None:
            self._OutageReport._OutageRecord = None

        self._OutageReport = value
        if self._OutageReport is not None:
            self._OutageReport.OutageRecord = None
            self._OutageReport._OutageRecord = self

    OutageReport = property(getOutageReport, setOutageReport)

    def getOutageSteps(self):
        
        return self._OutageSteps

    def setOutageSteps(self, value):
        for x in self._OutageSteps:
            x.OutageRecord = None
        for y in value:
            y._OutageRecord = self
        self._OutageSteps = value

    OutageSteps = property(getOutageSteps, setOutageSteps)

    def addOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            obj.OutageRecord = self

    def removeOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            obj.OutageRecord = None

