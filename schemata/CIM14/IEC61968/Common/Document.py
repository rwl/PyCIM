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

class Document(IdentifiedObject):
    """Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """

    def __init__(self, revisionNumber='', subject='', createdDateTime='', title='', category='', lastModifiedDateTime='', electronicAddress=None, status=None, ActivityRecords=None, docStatus=None, Measurements=None, **kw_args):
        """Initializes a new 'Document' instance.

        @param revisionNumber: Revision number for this document. 
        @param subject: Document subject. 
        @param createdDateTime: Date and time that this document was created. 
        @param title: Document title. 
        @param category: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param lastModifiedDateTime: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. 
        @param electronicAddress: Electronic address.
        @param status: Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
        @param ActivityRecords: All activity records created for this document.
        @param docStatus: Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
        @param Measurements: Measurements are specified in types of documents, such as procedures.
        """
        #: Revision number for this document.
        self.revisionNumber = revisionNumber

        #: Document subject.
        self.subject = subject

        #: Date and time that this document was created.
        self.createdDateTime = createdDateTime

        #: Document title.
        self.title = title

        #: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
        self.category = category

        #: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime.
        self.lastModifiedDateTime = lastModifiedDateTime

        self.electronicAddress = electronicAddress

        self.status = status

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self.docStatus = docStatus

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        super(Document, self).__init__(**kw_args)

    # Electronic address.
    electronicAddress = None

    # Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
    status = None

    def getActivityRecords(self):
        """All activity records created for this document.
        """
        return self._ActivityRecords

    def setActivityRecords(self, value):
        for p in self._ActivityRecords:
            filtered = [q for q in p.Documents if q != self]
            self._ActivityRecords._Documents = filtered
        for r in value:
            if self not in r._Documents:
                r._Documents.append(self)
        self._ActivityRecords = value

    ActivityRecords = property(getActivityRecords, setActivityRecords)

    def addActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self not in obj._Documents:
                obj._Documents.append(self)
            self._ActivityRecords.append(obj)

    def removeActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self in obj._Documents:
                obj._Documents.remove(self)
            self._ActivityRecords.remove(obj)

    # Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
    docStatus = None

    def getMeasurements(self):
        """Measurements are specified in types of documents, such as procedures.
        """
        return self._Measurements

    def setMeasurements(self, value):
        for p in self._Measurements:
            filtered = [q for q in p.Documents if q != self]
            self._Measurements._Documents = filtered
        for r in value:
            if self not in r._Documents:
                r._Documents.append(self)
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            if self not in obj._Documents:
                obj._Documents.append(self)
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            if self in obj._Documents:
                obj._Documents.remove(self)
            self._Measurements.remove(obj)

