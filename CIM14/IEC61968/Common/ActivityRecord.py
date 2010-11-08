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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ActivityRecord(IdentifiedObject):
    """Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """

    def __init__(self, reason='', createdDateTime='', severity='', category='', Documents=None, Assets=None, status=None, *args, **kw_args):
        """Initialises a new 'ActivityRecord' instance.

        @param reason: Reason for event resulting in this activity record, typically supplied when user initiated. 
        @param createdDateTime: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable). 
        @param severity: Severity level of event resulting in this activity record. 
        @param category: Category of event resulting in this activity record. 
        @param Documents: All documents for which this activity record has been created.
        @param Assets: All assets for which this activity record has been created.
        @param status: Information on consequence of event resulting in this activity record.
        """
        #: Reason for event resulting in this activity record, typically supplied when user initiated.
        self.reason = reason

        #: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable).
        self.createdDateTime = createdDateTime

        #: Severity level of event resulting in this activity record.
        self.severity = severity

        #: Category of event resulting in this activity record.
        self.category = category

        self._Documents = []
        self.Documents = [] if Documents is None else Documents

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self.status = status

        super(ActivityRecord, self).__init__(*args, **kw_args)

    _attrs = ["reason", "createdDateTime", "severity", "category"]
    _attr_types = {"reason": str, "createdDateTime": str, "severity": str, "category": str}
    _defaults = {"reason": '', "createdDateTime": '', "severity": '', "category": ''}
    _enums = {}
    _refs = ["Documents", "Assets", "status"]
    _many_refs = ["Documents", "Assets"]

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

