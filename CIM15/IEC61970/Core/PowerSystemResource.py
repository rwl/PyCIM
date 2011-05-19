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

class PowerSystemResource(IdentifiedObject):
    """A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.
    """

    def __init__(self, ChangeItems=None, ScheduleSteps=None, SafetyDocuments=None, OperatingShare=None, DocumentRoles=None, PsrLists=None, Measurements=None, ReportingGroup=None, PSRType=None, Assets=None, ErpOrganisationRoles=None, Location=None, PSREvent=None, NetworkDataSets=None, OutageSchedule=None, *args, **kw_args):
        """Initialises a new 'PowerSystemResource' instance.

        @param ChangeItems:
        @param ScheduleSteps:
        @param SafetyDocuments:
        @param OperatingShare: The linkage to any number of operating share objects.
        @param DocumentRoles:
        @param PsrLists:
        @param Measurements: The Measurements that are included in the naming hierarchy where the PSR is the containing object
        @param ReportingGroup: Reporting groups to which this PSR belongs.
        @param PSRType: PSRType (custom classification) for this PowerSystemResource.
        @param Assets: All assets represented by this power system resource. For example, multiple conductor assets are electrically modelled as a single AC line segment.
        @param ErpOrganisationRoles:
        @param Location: Location of this power system resource.
        @param PSREvent: All events associated with this power system resource.
        @param NetworkDataSets:
        @param OutageSchedule: A power system resource may have an outage schedule
        """
        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ScheduleSteps = []
        self.ScheduleSteps = [] if ScheduleSteps is None else ScheduleSteps

        self._SafetyDocuments = []
        self.SafetyDocuments = [] if SafetyDocuments is None else SafetyDocuments

        self._OperatingShare = []
        self.OperatingShare = [] if OperatingShare is None else OperatingShare

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._PsrLists = []
        self.PsrLists = [] if PsrLists is None else PsrLists

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._ReportingGroup = []
        self.ReportingGroup = [] if ReportingGroup is None else ReportingGroup

        self._PSRType = None
        self.PSRType = PSRType

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._Location = None
        self.Location = Location

        self._PSREvent = []
        self.PSREvent = [] if PSREvent is None else PSREvent

        self._NetworkDataSets = []
        self.NetworkDataSets = [] if NetworkDataSets is None else NetworkDataSets

        self._OutageSchedule = None
        self.OutageSchedule = OutageSchedule

        super(PowerSystemResource, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ChangeItems", "ScheduleSteps", "SafetyDocuments", "OperatingShare", "DocumentRoles", "PsrLists", "Measurements", "ReportingGroup", "PSRType", "Assets", "ErpOrganisationRoles", "Location", "PSREvent", "NetworkDataSets", "OutageSchedule"]
    _many_refs = ["ChangeItems", "ScheduleSteps", "SafetyDocuments", "OperatingShare", "DocumentRoles", "PsrLists", "Measurements", "ReportingGroup", "Assets", "ErpOrganisationRoles", "PSREvent", "NetworkDataSets"]

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.PowerSystemResource = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.PowerSystemResource = None

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

    def getSafetyDocuments(self):
        
        return self._SafetyDocuments

    def setSafetyDocuments(self, value):
        for x in self._SafetyDocuments:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._SafetyDocuments = value

    SafetyDocuments = property(getSafetyDocuments, setSafetyDocuments)

    def addSafetyDocuments(self, *SafetyDocuments):
        for obj in SafetyDocuments:
            obj.PowerSystemResource = self

    def removeSafetyDocuments(self, *SafetyDocuments):
        for obj in SafetyDocuments:
            obj.PowerSystemResource = None

    def getOperatingShare(self):
        """The linkage to any number of operating share objects.
        """
        return self._OperatingShare

    def setOperatingShare(self, value):
        for x in self._OperatingShare:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._OperatingShare = value

    OperatingShare = property(getOperatingShare, setOperatingShare)

    def addOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj.PowerSystemResource = self

    def removeOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj.PowerSystemResource = None

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.PowerSystemResource = self

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.PowerSystemResource = None

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

    def getMeasurements(self):
        """The Measurements that are included in the naming hierarchy where the PSR is the containing object
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.PowerSystemResource = self

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.PowerSystemResource = None

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
            if self not in self._PSRType._PowerSystemResources:
                self._PSRType._PowerSystemResources.append(self)

    PSRType = property(getPSRType, setPSRType)

    def getAssets(self):
        """All assets represented by this power system resource. For example, multiple conductor assets are electrically modelled as a single AC line segment.
        """
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._Assets._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._Assets.remove(obj)

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for x in self._ErpOrganisationRoles:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.PowerSystemResource = self

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            obj.PowerSystemResource = None

    def getLocation(self):
        """Location of this power system resource.
        """
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.PowerSystemResources if x != self]
            self._Location._PowerSystemResources = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._PowerSystemResources:
                self._Location._PowerSystemResources.append(self)

    Location = property(getLocation, setLocation)

    def getPSREvent(self):
        """All events associated with this power system resource.
        """
        return self._PSREvent

    def setPSREvent(self, value):
        for x in self._PSREvent:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._PSREvent = value

    PSREvent = property(getPSREvent, setPSREvent)

    def addPSREvent(self, *PSREvent):
        for obj in PSREvent:
            obj.PowerSystemResource = self

    def removePSREvent(self, *PSREvent):
        for obj in PSREvent:
            obj.PowerSystemResource = None

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

    def getOutageSchedule(self):
        """A power system resource may have an outage schedule
        """
        return self._OutageSchedule

    def setOutageSchedule(self, value):
        if self._OutageSchedule is not None:
            self._OutageSchedule._PowerSystemResource = None

        self._OutageSchedule = value
        if self._OutageSchedule is not None:
            self._OutageSchedule.PowerSystemResource = None
            self._OutageSchedule._PowerSystemResource = self

    OutageSchedule = property(getOutageSchedule, setOutageSchedule)

