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

class OutageRecord(Document):
    """A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a Trouble Call System by grouping customer calls. This has an associated OutageStep for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a SwitchingSchedule which complements the OutageRecord and records the ErpPersons (crew) and any planned Work. In other systems, it may be acceptable to manage outages including new WorkTasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.
    """

    def __init__(self, mode='', damageCode='', actionTaken='', endDateTime='', isPlanned=False, OutageReport=None, OutageCodes=None, OutageSteps=None, *args, **kw_args):
        """Initializes a new 'OutageRecord' instance.

        @param mode: Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime. 
        @param damageCode: The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none. 
        @param actionTaken: Overall action taken to resolve outage (details are in 'WorkTasks'). 
        @param endDateTime: Date and time restoration was completed for all customers impacted by this outage. 
        @param isPlanned: True if planned, false otherwise (for example due to a breaker trip). 
        @param OutageReport:
        @param OutageCodes: Multiple outage codes may apply to an outage record.
        @param OutageSteps:
        """
        #: Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime.
        self.mode = mode

        #: The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none.
        self.damageCode = damageCode

        #: Overall action taken to resolve outage (details are in 'WorkTasks').
        self.actionTaken = actionTaken

        #: Date and time restoration was completed for all customers impacted by this outage.
        self.endDateTime = endDateTime

        #: True if planned, false otherwise (for example due to a breaker trip).
        self.isPlanned = isPlanned

        self._OutageReport = None
        self.OutageReport = OutageReport

        self._OutageCodes = []
        self.OutageCodes = [] if OutageCodes is None else OutageCodes

        self._OutageSteps = []
        self.OutageSteps = [] if OutageSteps is None else OutageSteps

        super(OutageRecord, self).__init__(*args, **kw_args)

    def getOutageReport(self):
        
        return self._OutageReport

    def setOutageReport(self, value):
        if self._OutageReport is not None:
            self._OutageReport._OutageRecord = None

        self._OutageReport = value
        if self._OutageReport is not None:
            self._OutageReport._OutageRecord = self

    OutageReport = property(getOutageReport, setOutageReport)

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

    def getOutageSteps(self):
        
        return self._OutageSteps

    def setOutageSteps(self, value):
        for x in self._OutageSteps:
            x._OutageRecord = None
        for y in value:
            y._OutageRecord = self
        self._OutageSteps = value

    OutageSteps = property(getOutageSteps, setOutageSteps)

    def addOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            obj._OutageRecord = self
            self._OutageSteps.append(obj)

    def removeOutageSteps(self, *OutageSteps):
        for obj in OutageSteps:
            obj._OutageRecord = None
            self._OutageSteps.remove(obj)

