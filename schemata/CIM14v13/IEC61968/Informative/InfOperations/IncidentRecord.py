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

class IncidentRecord(Document):
    """Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.
    """

    def __init__(self, IncidentCodes=None, period=None, TroubleTickets=None, **kw_args):
        """Initializes a new 'IncidentRecord' instance.

        @param IncidentCodes:
        @param period: Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
        @param TroubleTickets:
        """
        self._IncidentCodes = []
        self.IncidentCodes = [] if IncidentCodes is None else IncidentCodes

        self.period = period

        self._TroubleTickets = []
        self.TroubleTickets = [] if TroubleTickets is None else TroubleTickets

        super(IncidentRecord, self).__init__(**kw_args)

    def getIncidentCodes(self):
        
        return self._IncidentCodes

    def setIncidentCodes(self, value):
        for p in self._IncidentCodes:
            filtered = [q for q in p.IncidentRecords if q != self]
            self._IncidentCodes._IncidentRecords = filtered
        for r in value:
            if self not in r._IncidentRecords:
                r._IncidentRecords.append(self)
        self._IncidentCodes = value

    IncidentCodes = property(getIncidentCodes, setIncidentCodes)

    def addIncidentCodes(self, *IncidentCodes):
        for obj in IncidentCodes:
            if self not in obj._IncidentRecords:
                obj._IncidentRecords.append(self)
            self._IncidentCodes.append(obj)

    def removeIncidentCodes(self, *IncidentCodes):
        for obj in IncidentCodes:
            if self in obj._IncidentRecords:
                obj._IncidentRecords.remove(self)
            self._IncidentCodes.remove(obj)

    # Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
    period = None

    def getTroubleTickets(self):
        
        return self._TroubleTickets

    def setTroubleTickets(self, value):
        for x in self._TroubleTickets:
            x._IncidentRecord = None
        for y in value:
            y._IncidentRecord = self
        self._TroubleTickets = value

    TroubleTickets = property(getTroubleTickets, setTroubleTickets)

    def addTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj._IncidentRecord = self
            self._TroubleTickets.append(obj)

    def removeTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj._IncidentRecord = None
            self._TroubleTickets.remove(obj)

