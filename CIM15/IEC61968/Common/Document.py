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

class Document(IdentifiedObject):
    """Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """

    def __init__(self, revisionNumber='', createdDateTime='', lastModifiedDateTime='', subject='', title='', category='', ChangeItems=None, ToDocumentRoles=None, electronicAddress=None, NetworkDataSets=None, FromDocumentRoles=None, ScheduleParameterInfos=None, ErpOrganisationRoles=None, Measurements=None, ActivityRecords=None, ChangeSets=None, ErpPersonRoles=None, ScheduledEvents=None, docStatus=None, AssetRoles=None, status=None, PowerSystemResourceRoles=None, *args, **kw_args):
        """Initialises a new 'Document' instance.

        @param revisionNumber: Revision number for this document. 
        @param createdDateTime: Date and time that this document was created. 
        @param lastModifiedDateTime: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. 
        @param subject: Document subject. 
        @param title: Document title. 
        @param category: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param ChangeItems:
        @param ToDocumentRoles:
        @param electronicAddress: Electronic address.
        @param NetworkDataSets:
        @param FromDocumentRoles:
        @param ScheduleParameterInfos:
        @param ErpOrganisationRoles:
        @param Measurements: Measurements are specified in types of documents, such as procedures.
        @param ActivityRecords: All activity records created for this document.
        @param ChangeSets:
        @param ErpPersonRoles:
        @param ScheduledEvents:
        @param docStatus: Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
        @param AssetRoles:
        @param status: Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
        @param PowerSystemResourceRoles:
        """
        #: Revision number for this document.
        self.revisionNumber = revisionNumber

        #: Date and time that this document was created.
        self.createdDateTime = createdDateTime

        #: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime.
        self.lastModifiedDateTime = lastModifiedDateTime

        #: Document subject.
        self.subject = subject

        #: Document title.
        self.title = title

        #: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
        self.category = category

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ToDocumentRoles = []
        self.ToDocumentRoles = [] if ToDocumentRoles is None else ToDocumentRoles

        self.electronicAddress = electronicAddress

        self._NetworkDataSets = []
        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        self._FromDocumentRoles = []
        self.FromDocumentRoles = [] if FromDocumentRoles is None else FromDocumentRoles

        self._ScheduleParameterInfos = []
        self.ScheduleParameterInfos = [] if ScheduleParameterInfos is None else ScheduleParameterInfos

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._ChangeSets = []
        self.ChangeSets = [] if ChangeSets is None else ChangeSets

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self.docStatus = docStatus

        self._AssetRoles = []
        self.AssetRoles = [] if AssetRoles is None else AssetRoles

        self.status = status

        self._PowerSystemResourceRoles = []
        self.PowerSystemResourceRoles = [] if PowerSystemResourceRoles is None else PowerSystemResourceRoles

        super(Document, self).__init__(*args, **kw_args)

    _attrs = ["revisionNumber", "createdDateTime", "lastModifiedDateTime", "subject", "title", "category"]
    _attr_types = {"revisionNumber": str, "createdDateTime": str, "lastModifiedDateTime": str, "subject": str, "title": str, "category": str}
    _defaults = {"revisionNumber": '', "createdDateTime": '', "lastModifiedDateTime": '', "subject": '', "title": '', "category": ''}
    _enums = {}
    _refs = ["ChangeItems", "ToDocumentRoles", "electronicAddress", "NetworkDataSets", "FromDocumentRoles", "ScheduleParameterInfos", "ErpOrganisationRoles", "Measurements", "ActivityRecords", "ChangeSets", "ErpPersonRoles", "ScheduledEvents", "docStatus", "AssetRoles", "status", "PowerSystemResourceRoles"]
    _many_refs = ["ChangeItems", "ToDocumentRoles", "NetworkDataSets", "FromDocumentRoles", "ScheduleParameterInfos", "ErpOrganisationRoles", "Measurements", "ActivityRecords", "ChangeSets", "ErpPersonRoles", "ScheduledEvents", "AssetRoles", "PowerSystemResourceRoles"]

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.Document = None
        for y in value:
            y._Document = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Document = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Document = None

    def getToDocumentRoles(self):
        
        return self._ToDocumentRoles

    def setToDocumentRoles(self, value):
        for x in self._ToDocumentRoles:
            x.FromDocument = None
        for y in value:
            y._FromDocument = self
        self._ToDocumentRoles = value

    ToDocumentRoles = property(getToDocumentRoles, setToDocumentRoles)

    def addToDocumentRoles(self, *ToDocumentRoles):
        for obj in ToDocumentRoles:
            obj.FromDocument = self

    def removeToDocumentRoles(self, *ToDocumentRoles):
        for obj in ToDocumentRoles:
            obj.FromDocument = None

    # Electronic address.
    electronicAddress = None

    def getNetworkDataSets(self):
        
        return self._NetworkDataSets

    def setNetworkDataSets(self, value):
        for p in self._NetworkDataSets:
            filtered = [q for q in p.Documents if q != self]
            self._NetworkDataSets._Documents = filtered
        for r in value:
            if self not in r._Documents:
                r._Documents.append(self)
        self._NetworkDataSets = value

    NetworkDataSets = property(getNetworkDataSets, setNetworkDataSets)

    def addNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self not in obj._Documents:
                obj._Documents.append(self)
            self._NetworkDataSets.append(obj)

    def removeNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self in obj._Documents:
                obj._Documents.remove(self)
            self._NetworkDataSets.remove(obj)

    def getFromDocumentRoles(self):
        
        return self._FromDocumentRoles

    def setFromDocumentRoles(self, value):
        for x in self._FromDocumentRoles:
            x.ToDocument = None
        for y in value:
            y._ToDocument = self
        self._FromDocumentRoles = value

    FromDocumentRoles = property(getFromDocumentRoles, setFromDocumentRoles)

    def addFromDocumentRoles(self, *FromDocumentRoles):
        for obj in FromDocumentRoles:
            obj.ToDocument = self

    def removeFromDocumentRoles(self, *FromDocumentRoles):
        for obj in FromDocumentRoles:
            obj.ToDocument = None

    def getScheduleParameterInfos(self):
        
        return self._ScheduleParameterInfos

    def setScheduleParameterInfos(self, value):
        for p in self._ScheduleParameterInfos:
            filtered = [q for q in p.Documents if q != self]
            self._ScheduleParameterInfos._Documents = filtered
        for r in value:
            if self not in r._Documents:
                r._Documents.append(self)
        self._ScheduleParameterInfos = value

    ScheduleParameterInfos = property(getScheduleParameterInfos, setScheduleParameterInfos)

    def addScheduleParameterInfos(self, *ScheduleParameterInfos):
        for obj in ScheduleParameterInfos:
            if self not in obj._Documents:
                obj._Documents.append(self)
            self._ScheduleParameterInfos.append(obj)

    def removeScheduleParameterInfos(self, *ScheduleParameterInfos):
        for obj in ScheduleParameterInfos:
            if self in obj._Documents:
                obj._Documents.remove(self)
            self._ScheduleParameterInfos.remove(obj)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x.Document = None
        for y in value:
            y._Document = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.Document = self

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.Document = None

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

    def getChangeSets(self):
        
        return self._ChangeSets

    def setChangeSets(self, value):
        for p in self._ChangeSets:
            filtered = [q for q in p.Documents if q != self]
            self._ChangeSets._Documents = filtered
        for r in value:
            if self not in r._Documents:
                r._Documents.append(self)
        self._ChangeSets = value

    ChangeSets = property(getChangeSets, setChangeSets)

    def addChangeSets(self, *ChangeSets):
        for obj in ChangeSets:
            if self not in obj._Documents:
                obj._Documents.append(self)
            self._ChangeSets.append(obj)

    def removeChangeSets(self, *ChangeSets):
        for obj in ChangeSets:
            if self in obj._Documents:
                obj._Documents.remove(self)
            self._ChangeSets.remove(obj)

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x.Document = None
        for y in value:
            y._Document = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj.Document = self

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj.Document = None

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for x in self._ScheduledEvents:
            x.Document = None
        for y in value:
            y._Document = self
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj.Document = self

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj.Document = None

    # Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
    docStatus = None

    def getAssetRoles(self):
        
        return self._AssetRoles

    def setAssetRoles(self, value):
        for x in self._AssetRoles:
            x.Document = None
        for y in value:
            y._Document = self
        self._AssetRoles = value

    AssetRoles = property(getAssetRoles, setAssetRoles)

    def addAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj.Document = self

    def removeAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj.Document = None

    # Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
    status = None

    def getPowerSystemResourceRoles(self):
        
        return self._PowerSystemResourceRoles

    def setPowerSystemResourceRoles(self, value):
        for x in self._PowerSystemResourceRoles:
            x.Document = None
        for y in value:
            y._Document = self
        self._PowerSystemResourceRoles = value

    PowerSystemResourceRoles = property(getPowerSystemResourceRoles, setPowerSystemResourceRoles)

    def addPowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj.Document = self

    def removePowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj.Document = None

