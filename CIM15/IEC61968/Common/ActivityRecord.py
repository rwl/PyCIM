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

class ActivityRecord(IdentifiedObject):
    """Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """

    def __init__(self, severity='', createdDateTime='', reason='', category='', ErpPersons=None, Organisations=None, Documents=None, Assets=None, status=None, ScheduledEvent=None, *args, **kw_args):
        """Initialises a new 'ActivityRecord' instance.

        @param severity: Severity level of event resulting in this activity record. 
        @param createdDateTime: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable). 
        @param reason: Reason for event resulting in this activity record, typically supplied when user initiated. 
        @param category: Category of event resulting in this activity record. 
        @param ErpPersons:
        @param Organisations:
        @param Documents: All documents for which this activity record has been created.
        @param Assets: All assets for which this activity record has been created.
        @param status: Information on consequence of event resulting in this activity record.
        @param ScheduledEvent:
        """
        #: Severity level of event resulting in this activity record.
        self.severity = severity

        #: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable).
        self.createdDateTime = createdDateTime

        #: Reason for event resulting in this activity record, typically supplied when user initiated.
        self.reason = reason

        #: Category of event resulting in this activity record.
        self.category = category

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self.status = status

        self._ScheduledEvent = None
        self.ScheduledEvent = ScheduledEvent

        super(ActivityRecord, self).__init__(*args, **kw_args)

    _attrs = ["severity", "createdDateTime", "reason", "category"]
    _attr_types = {"severity": str, "createdDateTime": str, "reason": str, "category": str}
    _defaults = {"severity": '', "createdDateTime": '', "reason": '', "category": ''}
    _enums = {}
    _refs = ["ErpPersons", "Organisations", "Documents", "Assets", "status", "ScheduledEvent"]
    _many_refs = ["ErpPersons", "Organisations", "Documents", "Assets"]

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._ErpPersons._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._ErpPersons.remove(obj)

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Organisations._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Organisations.remove(obj)

    def getDocuments(self):
        """All documents for which this activity record has been created.
        """
        return self._Documents

    def setDocuments(self, value):
        for p in self._Documents:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Documents._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Documents = value

    Documents = property(getDocuments, setDocuments)

    def addDocuments(self, *Documents):
        for obj in Documents:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Documents.append(obj)

    def removeDocuments(self, *Documents):
        for obj in Documents:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Documents.remove(obj)

    def getAssets(self):
        """All assets for which this activity record has been created.
        """
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.ActivityRecords if q != self]
            self._Assets._ActivityRecords = filtered
        for r in value:
            if self not in r._ActivityRecords:
                r._ActivityRecords.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._ActivityRecords:
                obj._ActivityRecords.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._ActivityRecords:
                obj._ActivityRecords.remove(self)
            self._Assets.remove(obj)

    # Information on consequence of event resulting in this activity record.
    status = None

    def getScheduledEvent(self):
        
        return self._ScheduledEvent

    def setScheduledEvent(self, value):
        if self._ScheduledEvent is not None:
            self._ScheduledEvent._ActivityRecord = None

        self._ScheduledEvent = value
        if self._ScheduledEvent is not None:
            self._ScheduledEvent.ActivityRecord = None
            self._ScheduledEvent._ActivityRecord = self

    ScheduledEvent = property(getScheduledEvent, setScheduledEvent)

