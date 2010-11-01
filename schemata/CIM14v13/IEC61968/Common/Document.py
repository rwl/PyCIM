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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Document(IdentifiedObject):
    """Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """

    def __init__(self, subject='', revisionNumber='', category='', lastModifiedDateTime='', title='', createdDateTime='', ActivityRecords=None, ErpOrganisationRoles=None, ScheduledEvents=None, FromDocumentRoles=None, LocationRoles=None, PowerSystemResourceRoles=None, NetworkDataSets=None, ErpPersonRoles=None, ChangeItems=None, Measurements=None, docStatus=None, ScheduleParameterInfos=None, ElectronicAddress=None, ToDocumentRoles=None, status=None, AssetRoles=None, ChangeSets=None, *args, **kw_args):
        """Initializes a new 'Document' instance.

        @param subject: Document subject. 
        @param revisionNumber: Revision number for this document. 
        @param category: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param lastModifiedDateTime: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. 
        @param title: Document title. 
        @param createdDateTime: Date and time that this document was created. 
        @param ActivityRecords: All activity records created for this document.
        @param ErpOrganisationRoles:
        @param ScheduledEvents:
        @param FromDocumentRoles:
        @param LocationRoles:
        @param PowerSystemResourceRoles:
        @param NetworkDataSets:
        @param ErpPersonRoles:
        @param ChangeItems:
        @param Measurements: Measurements are specified in types of documents, such as procedures.
        @param docStatus: Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
        @param ScheduleParameterInfos:
        @param ElectronicAddress:
        @param ToDocumentRoles:
        @param status: Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
        @param AssetRoles:
        @param ChangeSets:
        """
        #: Document subject. 
        self.subject = subject

        #: Revision number for this document. 
        self.revisionNumber = revisionNumber

        #: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        self.category = category

        #: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. 
        self.lastModifiedDateTime = lastModifiedDateTime

        #: Document title. 
        self.title = title

        #: Date and time that this document was created. 
        self.createdDateTime = createdDateTime

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._ScheduledEvents = []
        self.ScheduledEvents = [] if ScheduledEvents is None else ScheduledEvents

        self._FromDocumentRoles = []
        self.FromDocumentRoles = [] if FromDocumentRoles is None else FromDocumentRoles

        self._LocationRoles = []
        self.LocationRoles = [] if LocationRoles is None else LocationRoles

        self._PowerSystemResourceRoles = []
        self.PowerSystemResourceRoles = [] if PowerSystemResourceRoles is None else PowerSystemResourceRoles

        self._NetworkDataSets = []
        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self.docStatus = docStatus

        self._ScheduleParameterInfos = []
        self.ScheduleParameterInfos = [] if ScheduleParameterInfos is None else ScheduleParameterInfos

        self._ElectronicAddress = None
        self.ElectronicAddress = ElectronicAddress

        self._ToDocumentRoles = []
        self.ToDocumentRoles = [] if ToDocumentRoles is None else ToDocumentRoles

        self.status = status

        self._AssetRoles = []
        self.AssetRoles = [] if AssetRoles is None else AssetRoles

        self._ChangeSets = []
        self.ChangeSets = [] if ChangeSets is None else ChangeSets

        super(Document, self).__init__(*args, **kw_args)

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

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x._Document = None
        for y in value:
            y._Document = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._Document = self
            self._ErpOrganisationRoles.append(obj)

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._Document = None
            self._ErpOrganisationRoles.remove(obj)

    def getScheduledEvents(self):
        
        return self._ScheduledEvents

    def setScheduledEvents(self, value):
        for x in self._ScheduledEvents:
            x._Document = None
        for y in value:
            y._Document = self
        self._ScheduledEvents = value

    ScheduledEvents = property(getScheduledEvents, setScheduledEvents)

    def addScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj._Document = self
            self._ScheduledEvents.append(obj)

    def removeScheduledEvents(self, *ScheduledEvents):
        for obj in ScheduledEvents:
            obj._Document = None
            self._ScheduledEvents.remove(obj)

    def getFromDocumentRoles(self):
        
        return self._FromDocumentRoles

    def setFromDocumentRoles(self, value):
        for x in self._FromDocumentRoles:
            x._ToDocument = None
        for y in value:
            y._ToDocument = self
        self._FromDocumentRoles = value

    FromDocumentRoles = property(getFromDocumentRoles, setFromDocumentRoles)

    def addFromDocumentRoles(self, *FromDocumentRoles):
        for obj in FromDocumentRoles:
            obj._ToDocument = self
            self._FromDocumentRoles.append(obj)

    def removeFromDocumentRoles(self, *FromDocumentRoles):
        for obj in FromDocumentRoles:
            obj._ToDocument = None
            self._FromDocumentRoles.remove(obj)

    def getLocationRoles(self):
        
        return self._LocationRoles

    def setLocationRoles(self, value):
        for x in self._LocationRoles:
            x._Document = None
        for y in value:
            y._Document = self
        self._LocationRoles = value

    LocationRoles = property(getLocationRoles, setLocationRoles)

    def addLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._Document = self
            self._LocationRoles.append(obj)

    def removeLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._Document = None
            self._LocationRoles.remove(obj)

    def getPowerSystemResourceRoles(self):
        
        return self._PowerSystemResourceRoles

    def setPowerSystemResourceRoles(self, value):
        for x in self._PowerSystemResourceRoles:
            x._Document = None
        for y in value:
            y._Document = self
        self._PowerSystemResourceRoles = value

    PowerSystemResourceRoles = property(getPowerSystemResourceRoles, setPowerSystemResourceRoles)

    def addPowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj._Document = self
            self._PowerSystemResourceRoles.append(obj)

    def removePowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj._Document = None
            self._PowerSystemResourceRoles.remove(obj)

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

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x._Document = None
        for y in value:
            y._Document = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._Document = self
            self._ErpPersonRoles.append(obj)

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._Document = None
            self._ErpPersonRoles.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._Document = None
        for y in value:
            y._Document = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Document = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Document = None
            self._ChangeItems.remove(obj)

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

    # Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
    docStatus = None

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

    def getElectronicAddress(self):
        
        return self._ElectronicAddress

    def setElectronicAddress(self, value):
        if self._ElectronicAddress is not None:
            self._ElectronicAddress._Document = None

        self._ElectronicAddress = value
        if self._ElectronicAddress is not None:
            self._ElectronicAddress._Document = self

    ElectronicAddress = property(getElectronicAddress, setElectronicAddress)

    def getToDocumentRoles(self):
        
        return self._ToDocumentRoles

    def setToDocumentRoles(self, value):
        for x in self._ToDocumentRoles:
            x._FromDocument = None
        for y in value:
            y._FromDocument = self
        self._ToDocumentRoles = value

    ToDocumentRoles = property(getToDocumentRoles, setToDocumentRoles)

    def addToDocumentRoles(self, *ToDocumentRoles):
        for obj in ToDocumentRoles:
            obj._FromDocument = self
            self._ToDocumentRoles.append(obj)

    def removeToDocumentRoles(self, *ToDocumentRoles):
        for obj in ToDocumentRoles:
            obj._FromDocument = None
            self._ToDocumentRoles.remove(obj)

    # Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
    status = None

    def getAssetRoles(self):
        
        return self._AssetRoles

    def setAssetRoles(self, value):
        for x in self._AssetRoles:
            x._Document = None
        for y in value:
            y._Document = self
        self._AssetRoles = value

    AssetRoles = property(getAssetRoles, setAssetRoles)

    def addAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._Document = self
            self._AssetRoles.append(obj)

    def removeAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._Document = None
            self._AssetRoles.remove(obj)

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

