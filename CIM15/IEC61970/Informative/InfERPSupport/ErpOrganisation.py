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

from CIM15.IEC61968.Common.Organisation import Organisation

class ErpOrganisation(Organisation):
    """Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.Identifies organisations that might have roles as utilities, contractors, suppliers, manufacturers, customers, etc. Organisations may also have parent-child relationships to identify departments within an organisation, or parent company relationships. The organization may be internal (e.g., departments) or external to the utility. There may be multiple organizations of a given 'category', each with a unique 'code'.
    """

    def __init__(self, category='', code='', industryID='', governmentID='', optOut=False, isCostCenter=False, isProfitCenter=False, mode='', AssetRoles=None, Requests=None, Crews=None, ChangeItems=None, ErpPersonRoles=None, ActivityRecords=None, ParentOrganisationRoles=None, Locations=None, ChildOrganisationRoles=None, PowerSystemResourceRoles=None, LandPropertyRoles=None, DocumentRoles=None, *args, **kw_args):
        """Initialises a new 'ErpOrganisation' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param code: Designated code for organisation. 
        @param industryID: Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location. 
        @param governmentID: Unique identifier for organisation relative to its governing authority, for example a federal tax identifier. 
        @param optOut: True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation. 
        @param isCostCenter: True if organisation is cost center. 
        @param isProfitCenter: True if organisation is profit center. 
        @param mode: Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition). 
        @param AssetRoles:
        @param Requests:
        @param Crews:
        @param ChangeItems:
        @param ErpPersonRoles:
        @param ActivityRecords:
        @param ParentOrganisationRoles:
        @param Locations:
        @param ChildOrganisationRoles:
        @param PowerSystemResourceRoles:
        @param LandPropertyRoles:
        @param DocumentRoles:
        """
        #: Category by utility's corporate standards and practices.
        self.category = category

        #: Designated code for organisation.
        self.code = code

        #: Unique identifier for a given organisation (business). In the USA, this is a 'Dunns' or D&amp;B number. This identifier is typically in addition to the identifiers that organizations assign (on an internal basis) to each of their locations. Note that a unique identifier can be set up for each location of an organisation. This requirement is supported through the recursive Organisation-Organisation relationship, where each child Organisation can have a specified physical location.
        self.industryID = industryID

        #: Unique identifier for organisation relative to its governing authority, for example a federal tax identifier.
        self.governmentID = governmentID

        #: True if organisation 'opted out', i.e., has requested that their contact information not be shared with other organisations for purposes of solicitation.
        self.optOut = optOut

        #: True if organisation is cost center.
        self.isCostCenter = isCostCenter

        #: True if organisation is profit center.
        self.isProfitCenter = isProfitCenter

        #: Operational mode of the organisation, often required for outage reporting purposes. Some utilities use text to describe various modes (like nominal, emergency, storm, other), while others use severity ratings (for example, 0 is a nominal condition and 5 is the most severe condition).
        self.mode = mode

        self._AssetRoles = []
        self.AssetRoles = [] if AssetRoles is None else AssetRoles

        self._Requests = []
        self.Requests = [] if Requests is None else Requests

        self._Crews = []
        self.Crews = [] if Crews is None else Crews

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._ActivityRecords = []
        self.ActivityRecords = [] if ActivityRecords is None else ActivityRecords

        self._ParentOrganisationRoles = []
        self.ParentOrganisationRoles = [] if ParentOrganisationRoles is None else ParentOrganisationRoles

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._ChildOrganisationRoles = []
        self.ChildOrganisationRoles = [] if ChildOrganisationRoles is None else ChildOrganisationRoles

        self._PowerSystemResourceRoles = []
        self.PowerSystemResourceRoles = [] if PowerSystemResourceRoles is None else PowerSystemResourceRoles

        self._LandPropertyRoles = []
        self.LandPropertyRoles = [] if LandPropertyRoles is None else LandPropertyRoles

        self._DocumentRoles = []
        self.DocumentRoles = [] if DocumentRoles is None else DocumentRoles

        super(ErpOrganisation, self).__init__(*args, **kw_args)

    _attrs = ["category", "code", "industryID", "governmentID", "optOut", "isCostCenter", "isProfitCenter", "mode"]
    _attr_types = {"category": str, "code": str, "industryID": str, "governmentID": str, "optOut": bool, "isCostCenter": bool, "isProfitCenter": bool, "mode": str}
    _defaults = {"category": '', "code": '', "industryID": '', "governmentID": '', "optOut": False, "isCostCenter": False, "isProfitCenter": False, "mode": ''}
    _enums = {}
    _refs = ["AssetRoles", "Requests", "Crews", "ChangeItems", "ErpPersonRoles", "ActivityRecords", "ParentOrganisationRoles", "Locations", "ChildOrganisationRoles", "PowerSystemResourceRoles", "LandPropertyRoles", "DocumentRoles"]
    _many_refs = ["AssetRoles", "Requests", "Crews", "ChangeItems", "ErpPersonRoles", "ActivityRecords", "ParentOrganisationRoles", "Locations", "ChildOrganisationRoles", "PowerSystemResourceRoles", "LandPropertyRoles", "DocumentRoles"]

    def getAssetRoles(self):
        
        return self._AssetRoles

    def setAssetRoles(self, value):
        for x in self._AssetRoles:
            x.ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._AssetRoles = value

    AssetRoles = property(getAssetRoles, setAssetRoles)

    def addAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj.ErpOrganisation = self

    def removeAssetRoles(self, *AssetRoles):
        for obj in AssetRoles:
            obj.ErpOrganisation = None

    def getRequests(self):
        
        return self._Requests

    def setRequests(self, value):
        for x in self._Requests:
            x.Organisation = None
        for y in value:
            y._Organisation = self
        self._Requests = value

    Requests = property(getRequests, setRequests)

    def addRequests(self, *Requests):
        for obj in Requests:
            obj.Organisation = self

    def removeRequests(self, *Requests):
        for obj in Requests:
            obj.Organisation = None

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

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.Organisation = None
        for y in value:
            y._Organisation = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Organisation = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.Organisation = None

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x.ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj.ErpOrganisation = self

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj.ErpOrganisation = None

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

    def getParentOrganisationRoles(self):
        
        return self._ParentOrganisationRoles

    def setParentOrganisationRoles(self, value):
        for x in self._ParentOrganisationRoles:
            x.ChildOrganisation = None
        for y in value:
            y._ChildOrganisation = self
        self._ParentOrganisationRoles = value

    ParentOrganisationRoles = property(getParentOrganisationRoles, setParentOrganisationRoles)

    def addParentOrganisationRoles(self, *ParentOrganisationRoles):
        for obj in ParentOrganisationRoles:
            obj.ChildOrganisation = self

    def removeParentOrganisationRoles(self, *ParentOrganisationRoles):
        for obj in ParentOrganisationRoles:
            obj.ChildOrganisation = None

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.ErpOrganisations if q != self]
            self._Locations._ErpOrganisations = filtered
        for r in value:
            if self not in r._ErpOrganisations:
                r._ErpOrganisations.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._ErpOrganisations:
                obj._ErpOrganisations.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._ErpOrganisations:
                obj._ErpOrganisations.remove(self)
            self._Locations.remove(obj)

    def getChildOrganisationRoles(self):
        
        return self._ChildOrganisationRoles

    def setChildOrganisationRoles(self, value):
        for x in self._ChildOrganisationRoles:
            x.ParentOrganisation = None
        for y in value:
            y._ParentOrganisation = self
        self._ChildOrganisationRoles = value

    ChildOrganisationRoles = property(getChildOrganisationRoles, setChildOrganisationRoles)

    def addChildOrganisationRoles(self, *ChildOrganisationRoles):
        for obj in ChildOrganisationRoles:
            obj.ParentOrganisation = self

    def removeChildOrganisationRoles(self, *ChildOrganisationRoles):
        for obj in ChildOrganisationRoles:
            obj.ParentOrganisation = None

    def getPowerSystemResourceRoles(self):
        
        return self._PowerSystemResourceRoles

    def setPowerSystemResourceRoles(self, value):
        for x in self._PowerSystemResourceRoles:
            x.ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._PowerSystemResourceRoles = value

    PowerSystemResourceRoles = property(getPowerSystemResourceRoles, setPowerSystemResourceRoles)

    def addPowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj.ErpOrganisation = self

    def removePowerSystemResourceRoles(self, *PowerSystemResourceRoles):
        for obj in PowerSystemResourceRoles:
            obj.ErpOrganisation = None

    def getLandPropertyRoles(self):
        
        return self._LandPropertyRoles

    def setLandPropertyRoles(self, value):
        for x in self._LandPropertyRoles:
            x.ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._LandPropertyRoles = value

    LandPropertyRoles = property(getLandPropertyRoles, setLandPropertyRoles)

    def addLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj.ErpOrganisation = self

    def removeLandPropertyRoles(self, *LandPropertyRoles):
        for obj in LandPropertyRoles:
            obj.ErpOrganisation = None

    def getDocumentRoles(self):
        
        return self._DocumentRoles

    def setDocumentRoles(self, value):
        for x in self._DocumentRoles:
            x.ErpOrganisation = None
        for y in value:
            y._ErpOrganisation = self
        self._DocumentRoles = value

    DocumentRoles = property(getDocumentRoles, setDocumentRoles)

    def addDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.ErpOrganisation = self

    def removeDocumentRoles(self, *DocumentRoles):
        for obj in DocumentRoles:
            obj.ErpOrganisation = None

