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

class PowerSystemResource(IdentifiedObject):
    """A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    def __init__(self, ChangeItems=None, AssetRoles=None, GeoLocation=None, SafetyDocuments=None, OutageSchedule=None, Measurements=None, ErpOrganisationRoles=None, PSRType=None, PsrLists=None, PSREvent=None, OperatingShare=None, ScheduleSteps=None, DocumentRoles=None, ReportingGroup=None, CircuitSections=None, NetworkDataSets=None, *args, **kw_args):
        """Initializes a new 'PowerSystemResource' instance.

        @param ChangeItems:
        @param AssetRoles:
        @param GeoLocation: Geographical location of this power system resource.
        @param SafetyDocuments:
        @param OutageSchedule: A power system resource may have an outage schedule
        @param Measurements: The Measurements that are included in the naming hierarchy where the PSR is the containing object
        @param ErpOrganisationRoles:
        @param PSRType: PSRType (custom classification) for this PowerSystemResource.
        @param PsrLists:
        @param PSREvent: All events associated with this power system resource.
        @param OperatingShare: The linkage to any number of operating share objects.
        @param ScheduleSteps:
        @param DocumentRoles:
        @param ReportingGroup: Reporting groups to which this PSR belongs.
        @param CircuitSections:
        @param NetworkDataSets:
        """
        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._AssetRoles = []
        self.AssetRoles = [] if AssetRoles is None else AssetRoles

        self._GeoLocation = None
        self.GeoLocation = GeoLocation

        self._SafetyDocuments = []
        self.SafetyDocuments = [] if SafetyDocuments is None else SafetyDocuments

        self._OutageSchedule = None
        self.OutageSchedule = OutageSchedule

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._PSRType = None
        self.PSRType = PSRType

        self._PsrLists = []
        self.PsrLists = [] if PsrLists is None else PsrLists

        self._PSREvent = []
        self.PSREvent = [] if PSREvent is None else PSREvent

        self._OperatingShare = []
        self.OperatingShare = [] if OperatingShare is None else OperatingShare

        self._ScheduleSteps = []
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._ReportingGroup = []
        self.ReportingGroup = [] if ReportingGroup is None else ReportingGroup

        self._CircuitSections = []
        self.CircuitSections = [] if CircuitSections is None else CircuitSections

        self._NetworkDataSets = []
        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        super(PowerSystemResource, self).__init__(*args, **kw_args)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._PowerSystemResource = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._PowerSystemResource = None
            self._ChangeItems.remove(obj)

    def getAssetRoles(self):
        
        return self._AssetRoles

    def setAssetRoles(self, value):
        for x in self._AssetRoles:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._AssetRoles = value

    AssetRoles = property(getAssetRoles, setAssetRoles)

    def addAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._PowerSystemResource = self
            self._AssetRoles.append(obj)

    def removeAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._PowerSystemResource = None
            self._AssetRoles.remove(obj)

    def getGeoLocation(self):
        """Geographical location of this power system resource.
        """
        return self._GeoLocation

    def setGeoLocation(self, value):
        if self._GeoLocation is not None:
            filtered = [x for x in self.GeoLocation.PowerSystemResources if x != self]
            self._GeoLocation._PowerSystemResources = filtered

        self._GeoLocation = value
        if self._GeoLocation is not None:
            self._GeoLocation._PowerSystemResources.append(self)

    GeoLocation = property(getGeoLocation, setGeoLocation)

    def getSafetyDocuments(self):
        
        return self._SafetyDocuments

    def setSafetyDocuments(self, value):
        for x in self._SafetyDocuments:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._SafetyDocuments = value

    SafetyDocuments = property(getSafetyDocuments, setSafetyDocuments)

    def addSafetyDocuments(self, *SafetyDocuments):
        for obj in SafetyDocuments:
            obj._PowerSystemResource = self
            self._SafetyDocuments.append(obj)

    def removeSafetyDocuments(self, *SafetyDocuments):
        for obj in SafetyDocuments:
            obj._PowerSystemResource = None
            self._SafetyDocuments.remove(obj)

    def getOutageSchedule(self):
        """A power system resource may have an outage schedule
        """
        return self._OutageSchedule

    def setOutageSchedule(self, value):
        if self._OutageSchedule is not None:
            self._OutageSchedule._PowerSystemResource = None

        self._OutageSchedule = value
        if self._OutageSchedule is not None:
            self._OutageSchedule._PowerSystemResource = self

    OutageSchedule = property(getOutageSchedule, setOutageSchedule)

    def getMeasurements(self):
        """The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._PowerSystemResource = self
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._PowerSystemResource = None
            self._Measurements.remove(obj)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._PowerSystemResource = self
            self._ErpOrganisationRoles.append(obj)

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj._PowerSystemResource = None
            self._ErpOrganisationRoles.remove(obj)

    def getPSRType(self):
        """PSRType (custom classification) for this PowerSystemResource.
        """
        return self._PSRType

    def setPSRType(self, value):
        if self._PSRType is not None:
            filtered = [x for x in self.PSRType.PowerSystemResources if x != self]
            self._PSRType._PowerSystemResources = filtered

        self._PSRType = value
        if self._PSRType is not None:
            self._PSRType._PowerSystemResources.append(self)

    PSRType = property(getPSRType, setPSRType)

    def getPsrLists(self):
        
        return self._PsrLists

    def setPsrLists(self, value):
        for p in self._PsrLists:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._PsrLists._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._PsrLists = value

    PsrLists = property(getPsrLists, setPsrLists)

    def addPsrLists(self, *PsrLists):
        for obj in PsrLists:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._PsrLists.append(obj)

    def removePsrLists(self, *PsrLists):
        for obj in PsrLists:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._PsrLists.remove(obj)

    def getPSREvent(self):
        """All events associated with this power system resource.
        """
        return self._PSREvent

    def setPSREvent(self, value):
        for x in self._PSREvent:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._PSREvent = value

    PSREvent = property(getPSREvent, setPSREvent)

    def addPSREvent(self, *PSREvent):
        for obj in PSREvent:
            obj._PowerSystemResource = self
            self._PSREvent.append(obj)

    def removePSREvent(self, *PSREvent):
        for obj in PSREvent:
            obj._PowerSystemResource = None
            self._PSREvent.remove(obj)

    def getOperatingShare(self):
        """The linkage to any number of operating share objects.
        """
        return self._OperatingShare

    def setOperatingShare(self, value):
        for x in self._OperatingShare:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._OperatingShare = value

    OperatingShare = property(getOperatingShare, setOperatingShare)

    def addOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj._PowerSystemResource = self
            self._OperatingShare.append(obj)

    def removeOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj._PowerSystemResource = None
            self._OperatingShare.remove(obj)

    def getScheduleSteps(self):
        
        return self._ScheduleSteps

    def setScheduleSteps(self, value):
        for p in self._ScheduleSteps:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._ScheduleSteps._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._ScheduleSteps = value

    ScheduleSteps = property(getScheduleSteps, setScheduleSteps)

    def addScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._ScheduleSteps.append(obj)

    def removeScheduleSteps(self, *ScheduleSteps):
        for obj in ScheduleSteps:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._ScheduleSteps.remove(obj)

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x._PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._PowerSystemResource = self
            self._DocumentRoles.append(obj)

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._PowerSystemResource = None
            self._DocumentRoles.remove(obj)

    def getReportingGroup(self):
        """Reporting groups to which this PSR belongs.
        """
        return self._ReportingGroup

    def setReportingGroup(self, value):
        for p in self._ReportingGroup:
            filtered = [q for q in p.PowerSystemResource if q != self]
            self._ReportingGroup._PowerSystemResource = filtered
        for r in value:
            if self not in r._PowerSystemResource:
                r._PowerSystemResource.append(self)
        self._ReportingGroup = value

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def addReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            if self not in obj._PowerSystemResource:
                obj._PowerSystemResource.append(self)
            self._ReportingGroup.append(obj)

    def removeReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            if self in obj._PowerSystemResource:
                obj._PowerSystemResource.remove(self)
            self._ReportingGroup.remove(obj)

    def getCircuitSections(self):
        
        return self._CircuitSections

    def setCircuitSections(self, value):
        for p in self._CircuitSections:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._CircuitSections._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._CircuitSections = value

    CircuitSections = property(getCircuitSections, setCircuitSections)

    def addCircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._CircuitSections.append(obj)

    def removeCircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._CircuitSections.remove(obj)

    def getNetworkDataSets(self):
        
        return self._NetworkDataSets

    def setNetworkDataSets(self, value):
        for p in self._NetworkDataSets:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._NetworkDataSets._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._NetworkDataSets = value

    NetworkDataSets = property(getNetworkDataSets, setNetworkDataSets)

    def addNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._NetworkDataSets.append(obj)

    def removeNetworkDataSets(self, *NetworkDataSets):
        for obj in NetworkDataSets:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._NetworkDataSets.remove(obj)

