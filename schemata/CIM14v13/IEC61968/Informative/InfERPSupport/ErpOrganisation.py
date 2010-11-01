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

from CIM14v13.IEC61968.Common.Organisation import Organisation

class ErpOrganisation(Organisation):
    """Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.
    """

    def __init__(self, code='', category='', mode='', optOut=False, industryID='', isProfitCenter=False, isCostCenter=False, governmentID='', DocumentRoles=None, ActivityRecords=None, LocationRoles=None, ErpPersonRoles=None, ViolationLimits=None, Requests=None, ChangeItems=None, IntSchedAgreement=None, RegisteredResources=None, PowerSystemResourceRoles=None, AssetRoles=None, LandPropertyRoles=None, ParentOrganisationRoles=None, ChildOrganisationRoles=None, Crews=None, *args, **kw_args):
        """Initializes a new 'ErpOrganisation' instance.

        @param code: Designated code for organisation. 
        @param category: Category by utility's corporate standards and practices. 
        @param mode: Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition). 
        @param optOut: True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation. 
        @param industryID: Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location. 
        @param isProfitCenter: True if organisation is profit center. 
        @param isCostCenter: True if organisation is cost center. 
        @param governmentID: Unique identifier for organisation relative to its governing authority, for example a federal tax identifier. 
        @param DocumentRoles:
        @param ActivityRecords:
        @param LocationRoles:
        @param ErpPersonRoles:
        @param ViolationLimits:
        @param Requests:
        @param ChangeItems:
        @param IntSchedAgreement:
        @param RegisteredResources:
        @param PowerSystemResourceRoles:
        @param AssetRoles:
        @param LandPropertyRoles:
        @param ParentOrganisationRoles:
        @param ChildOrganisationRoles:
        @param Crews:
        """
        #: Designated code for organisation. 
        self.code = code

        #: Category by utility's corporate standards and practices. 
        self.category = category

        #: Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition). 
        self.mode = mode

        #: True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation. 
        self.optOut = optOut

        #: Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location. 
        self.industryID = industryID

        #: True if organisation is profit center. 
        self.isProfitCenter = isProfitCenter

        #: True if organisation is cost center. 
        self.isCostCenter = isCostCenter

        #: Unique identifier for organisation relative to its governing authority, for example a federal tax identifier. 
        self.governmentID = governmentID

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._LocationRoles = []
        self.LocationRoles = [] if LocationRoles is None else LocationRoles

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._ViolationLimits = []
        self.ViolationLimits = [] if ViolationLimits is None else ViolationLimits

        self._Requests = []
        self.Requests = [] if Requests is None else Requests

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._IntSchedAgreement = []
        self.IntSchedAgreement = [] if IntSchedAgreement is None else IntSchedAgreement

        self._RegisteredResources = []
        self.RegisteredResources = [] if RegisteredResources is None else RegisteredResources

        self._PowerSystemResourceRoles = []
        self.PowerSystemResourceRoles = [] if PowerSystemResourceRoles is None else PowerSystemResourceRoles

        self._AssetRoles = []
        self.AssetRoles = [] if AssetRoles is None else AssetRoles

        self._LandPropertyRoles = []
        self.LandPropertyRoles = [] if LandPropertyRoles is None else LandPropertyRoles

        self._ParentOrganisationRoles = []
        self.ParentOrganisationRoles = [] if ParentOrganisationRoles is None else ParentOrganisationRoles

        self._ChildOrganisationRoles = []
        self.ChildOrganisationRoles = [] if ChildOrganisationRoles is None else ChildOrganisationRoles

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        super(ErpOrganisation, self).__init__(*args, **kw_args)

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x._ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._ErpOrganisation = self
            self._DocumentRoles.append(obj)

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj._ErpOrganisation = None
            self._DocumentRoles.remove(obj)

    def getActivityRecords(self):
        
        return self._ActivityRecords

    def setActivityRecords(self, value):
        for p in self._ActivityRecords:
            filtered = [q for q in p.Organisations if q != self]
            self._ActivityRecords._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._ActivityRecords = value

    ActivityRecords = property(getActivityRecords, setActivityRecords)

    def addActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._ActivityRecords.append(obj)

    def removeActivityRecords(self, *ActivityRecords):
        for obj in ActivityRecords:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._ActivityRecords.remove(obj)

    def getLocationRoles(self):
        
        return self._LocationRoles

    def setLocationRoles(self, value):
        for x in self._LocationRoles:
            x._ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._LocationRoles = value

    LocationRoles = property(getLocationRoles, setLocationRoles)

    def addLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._ErpOrganisation = self
            self._LocationRoles.append(obj)

    def removeLocationRoles(self, *LocationRoles):
        for obj in LocationRoles:
            obj._ErpOrganisation = None
            self._LocationRoles.remove(obj)

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x._ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._ErpOrganisation = self
            self._ErpPersonRoles.append(obj)

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._ErpOrganisation = None
            self._ErpPersonRoles.remove(obj)

    def getViolationLimits(self):
        
        return self._ViolationLimits

    def setViolationLimits(self, value):
        for p in self._ViolationLimits:
            filtered = [q for q in p.Organisations if q != self]
            self._ViolationLimits._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._ViolationLimits = value

    ViolationLimits = property(getViolationLimits, setViolationLimits)

    def addViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._ViolationLimits.append(obj)

    def removeViolationLimits(self, *ViolationLimits):
        for obj in ViolationLimits:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._ViolationLimits.remove(obj)

    def getRequests(self):
        
        return self._Requests

    def setRequests(self, value):
        for x in self._Requests:
            x._Organisation = None
        for y in value:
            y._Organisation = self
        self._Requests = value

    Requests = property(getRequests, setRequests)

    def addRequests(self, *Requests):
        for obj in Requests:
            obj._Organisation = self
            self._Requests.append(obj)

    def removeRequests(self, *Requests):
        for obj in Requests:
            obj._Organisation = None
            self._Requests.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._Organisation = None
        for y in value:
            y._Organisation = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Organisation = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._Organisation = None
            self._ChangeItems.remove(obj)

    def getIntSchedAgreement(self):
        
        return self._IntSchedAgreement

    def setIntSchedAgreement(self, value):
        for p in self._IntSchedAgreement:
            filtered = [q for q in p.Organisations if q != self]
            self._IntSchedAgreement._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._IntSchedAgreement = value

    IntSchedAgreement = property(getIntSchedAgreement, setIntSchedAgreement)

    def addIntSchedAgreement(self, *IntSchedAgreement):
        for obj in IntSchedAgreement:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._IntSchedAgreement.append(obj)

    def removeIntSchedAgreement(self, *IntSchedAgreement):
        for obj in IntSchedAgreement:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._IntSchedAgreement.remove(obj)

    def getRegisteredResources(self):
        
        return self._RegisteredResources

    def setRegisteredResources(self, value):
        for x in self._RegisteredResources:
            x._Organisation = None
        for y in value:
            y._Organisation = self
        self._RegisteredResources = value

    RegisteredResources = property(getRegisteredResources, setRegisteredResources)

    def addRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            obj._Organisation = self
            self._RegisteredResources.append(obj)

    def removeRegisteredResources(self, *RegisteredResources):
        for obj in RegisteredResources:
            obj._Organisation = None
            self._RegisteredResources.remove(obj)

    def getPowerSystemResourceRoles(self):
        
        return self._PowerSystemResourceRoles

    def setPowerSystemResourceRoles(self, value):
        for x in self._PowerSystemResourceRoles:
            x._ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._PowerSystemResourceRoles = value

    PowerSystemResourceRoles = property(getPowerSystemResourceRoles, setPowerSystemResourceRoles)

    def addPowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj._ErpOrganisation = self
            self._PowerSystemResourceRoles.append(obj)

    def removePowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj._ErpOrganisation = None
            self._PowerSystemResourceRoles.remove(obj)

    def getAssetRoles(self):
        
        return self._AssetRoles

    def setAssetRoles(self, value):
        for x in self._AssetRoles:
            x._ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._AssetRoles = value

    AssetRoles = property(getAssetRoles, setAssetRoles)

    def addAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._ErpOrganisation = self
            self._AssetRoles.append(obj)

    def removeAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj._ErpOrganisation = None
            self._AssetRoles.remove(obj)

    def getLandPropertyRoles(self):
        
        return self._LandPropertyRoles

    def setLandPropertyRoles(self, value):
        for x in self._LandPropertyRoles:
            x._ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._LandPropertyRoles = value

    LandPropertyRoles = property(getLandPropertyRoles, setLandPropertyRoles)

    def addLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj._ErpOrganisation = self
            self._LandPropertyRoles.append(obj)

    def removeLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj._ErpOrganisation = None
            self._LandPropertyRoles.remove(obj)

    def getParentOrganisationRoles(self):
        
        return self._ParentOrganisationRoles

    def setParentOrganisationRoles(self, value):
        for x in self._ParentOrganisationRoles:
            x._ChildOrganisation = None
        for y in value:
            y._ChildOrganisation = self
        self._ParentOrganisationRoles = value

    ParentOrganisationRoles = property(getParentOrganisationRoles, setParentOrganisationRoles)

    def addParentOrganisationRoles(self, *ParentOrganisationRoles):
        for obj in ParentOrganisationRoles:
            obj._ChildOrganisation = self
            self._ParentOrganisationRoles.append(obj)

    def removeParentOrganisationRoles(self, *ParentOrganisationRoles):
        for obj in ParentOrganisationRoles:
            obj._ChildOrganisation = None
            self._ParentOrganisationRoles.remove(obj)

    def getChildOrganisationRoles(self):
        
        return self._ChildOrganisationRoles

    def setChildOrganisationRoles(self, value):
        for x in self._ChildOrganisationRoles:
            x._ParentOrganisation = None
        for y in value:
            y._ParentOrganisation = self
        self._ChildOrganisationRoles = value

    ChildOrganisationRoles = property(getChildOrganisationRoles, setChildOrganisationRoles)

    def addChildOrganisationRoles(self, *ChildOrganisationRoles):
        for obj in ChildOrganisationRoles:
            obj._ParentOrganisation = self
            self._ChildOrganisationRoles.append(obj)

    def removeChildOrganisationRoles(self, *ChildOrganisationRoles):
        for obj in ChildOrganisationRoles:
            obj._ParentOrganisation = None
            self._ChildOrganisationRoles.remove(obj)

    def getCrews(self):
        
        return self._Crews

    def setCrews(self, value):
        for p in self._Crews:
            filtered = [q for q in p.Organisations if q != self]
            self._Crews._Organisations = filtered
        for r in value:
            if self not in r._Organisations:
                r._Organisations.append(self)
        self._Crews = value

    Crews = property(getCrews, setCrews)

    def addCrews(self, *Crews):
        for obj in Crews:
            if self not in obj._Organisations:
                obj._Organisations.append(self)
            self._Crews.append(obj)

    def removeCrews(self, *Crews):
        for obj in Crews:
            if self in obj._Organisations:
                obj._Organisations.remove(self)
            self._Crews.remove(obj)

