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

class IncidentRecord(Document):
    """Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.
    """

    def __init__(self, TroubleTickets=None, period=None, IncidentCodes=None, *args, **kw_args):
        """Initialises a new 'IncidentRecord' instance.

        @param TroubleTickets:
        @param period: Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
        @param IncidentCodes:
        """
        self._TroubleTickets = []
        self.TroubleTickets = [] if TroubleTickets is None else TroubleTickets

        self.period = period

        self._IncidentCodes = []
        self.IncidentCodes = [] if IncidentCodes is None else IncidentCodes

        super(IncidentRecord, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TroubleTickets", "period", "IncidentCodes"]
    _many_refs = ["TroubleTickets", "IncidentCodes"]

    def getTroubleTickets(self):
        
        return self._TroubleTickets

    def setTroubleTickets(self, value):
        for x in self._TroubleTickets:
            x.IncidentRecord = None
        for y in value:
            y._IncidentRecord = self
        self._TroubleTickets = value

    TroubleTickets = property(getTroubleTickets, setTroubleTickets)

    def addTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj.IncidentRecord = self

    def removeTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj.IncidentRecord = None

    # Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
    period = None

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

