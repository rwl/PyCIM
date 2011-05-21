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

