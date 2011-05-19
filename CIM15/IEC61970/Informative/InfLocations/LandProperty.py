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

class LandProperty(IdentifiedObject):
    """Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.
    """

    def __init__(self, kind="store", externalRecordReference='', demographicKind="other", status=None, LocationGrants=None, ErpSiteLevelDatas=None, ErpPersonRoles=None, ErpOrganisationRoles=None, AssetContainers=None, Locations=None, RightOfWays=None, *args, **kw_args):
        """Initialises a new 'LandProperty' instance.

        @param kind: Kind of (land) property, categorised according to its main functional use from the utility's perspective. Values are: "store", "customerPremise", "building", "external", "gridSupplyPoint", "substation", "depot"
        @param externalRecordReference: Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation. 
        @param demographicKind: Demographics around the site. Values are: "other", "urban", "rural"
        @param status:
        @param LocationGrants: All location grants this land property has.
        @param ErpSiteLevelDatas:
        @param ErpPersonRoles:
        @param ErpOrganisationRoles:
        @param AssetContainers:
        @param Locations: The spatail description of a piece of property.
        @param RightOfWays: All rights of way this land property has.
        """
        #: Kind of (land) property, categorised according to its main functional use from the utility's perspective. Values are: "store", "customerPremise", "building", "external", "gridSupplyPoint", "substation", "depot"
        self.kind = kind

        #: Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation.
        self.externalRecordReference = externalRecordReference

        #: Demographics around the site. Values are: "other", "urban", "rural"
        self.demographicKind = demographicKind

        self.status = status

        self._LocationGrants = []
        self.LocationGrants = [] if LocationGrants is None else LocationGrants

        self._ErpSiteLevelDatas = []
        self.ErpSiteLevelDatas = [] if ErpSiteLevelDatas is None else ErpSiteLevelDatas

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self._AssetContainers = []
        self.AssetContainers = [] if AssetContainers is None else AssetContainers

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._RightOfWays = []
        self.RightOfWays = [] if RightOfWays is None else RightOfWays

        super(LandProperty, self).__init__(*args, **kw_args)

    _attrs = ["kind", "externalRecordReference", "demographicKind"]
    _attr_types = {"kind": str, "externalRecordReference": str, "demographicKind": str}
    _defaults = {"kind": "store", "externalRecordReference": '', "demographicKind": "other"}
    _enums = {"kind": "LandPropertyKind", "demographicKind": "DemographicKind"}
    _refs = ["status", "LocationGrants", "ErpSiteLevelDatas", "ErpPersonRoles", "ErpOrganisationRoles", "AssetContainers", "Locations", "RightOfWays"]
    _many_refs = ["LocationGrants", "ErpSiteLevelDatas", "ErpPersonRoles", "ErpOrganisationRoles", "AssetContainers", "Locations", "RightOfWays"]

    status = None

    def getLocationGrants(self):
        """All location grants this land property has.
        """
        return self._LocationGrants

    def setLocationGrants(self, value):
        for x in self._LocationGrants:
            x.LandProperty = None
        for y in value:
            y._LandProperty = self
        self._LocationGrants = value

    LocationGrants = property(getLocationGrants, setLocationGrants)

    def addLocationGrants(self, *LocationGrants):
        for obj in LocationGrants:
            obj.LandProperty = self

    def removeLocationGrants(self, *LocationGrants):
        for obj in LocationGrants:
            obj.LandProperty = None

    def getErpSiteLevelDatas(self):
        
        return self._ErpSiteLevelDatas

    def setErpSiteLevelDatas(self, value):
        for x in self._ErpSiteLevelDatas:
            x.LandProperty = None
        for y in value:
            y._LandProperty = self
        self._ErpSiteLevelDatas = value

    ErpSiteLevelDatas = property(getErpSiteLevelDatas, setErpSiteLevelDatas)

    def addErpSiteLevelDatas(self, *ErpSiteLevelDatas):
        for obj in ErpSiteLevelDatas:
            obj.LandProperty = self

    def removeErpSiteLevelDatas(self, *ErpSiteLevelDatas):
        for obj in ErpSiteLevelDatas:
            obj.LandProperty = None

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x.LandProperty = None
        for y in value:
            y._LandProperty = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj.LandProperty = self

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj.LandProperty = None

    def getErpOrganisationRoles(self):
        
        return self._ErpOrganisationRoles

    def setErpOrganisationRoles(self, value):
        for p in self._ErpOrganisationRoles:
            filtered = [q for q in p.LandProperty if q != self]
            self._ErpOrganisationRoles._LandProperty = filtered
        for r in value:
            if self not in r._LandProperty:
                r._LandProperty.append(self)
        self._ErpOrganisationRoles = value

    ErpOrganisationRoles = property(getErpOrganisationRoles, setErpOrganisationRoles)

    def addErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            if self not in obj._LandProperty:
                obj._LandProperty.append(self)
            self._ErpOrganisationRoles.append(obj)

    def removeErpOrganisationRoles(self, *ErpOrganisationRoles):
        for obj in ErpOrganisationRoles:
            if self in obj._LandProperty:
                obj._LandProperty.remove(self)
            self._ErpOrganisationRoles.remove(obj)

    def getAssetContainers(self):
        
        return self._AssetContainers

    def setAssetContainers(self, value):
        for p in self._AssetContainers:
            filtered = [q for q in p.LandProperties if q != self]
            self._AssetContainers._LandProperties = filtered
        for r in value:
            if self not in r._LandProperties:
                r._LandProperties.append(self)
        self._AssetContainers = value

    AssetContainers = property(getAssetContainers, setAssetContainers)

    def addAssetContainers(self, *AssetContainers):
        for obj in AssetContainers:
            if self not in obj._LandProperties:
                obj._LandProperties.append(self)
            self._AssetContainers.append(obj)

    def removeAssetContainers(self, *AssetContainers):
        for obj in AssetContainers:
            if self in obj._LandProperties:
                obj._LandProperties.remove(self)
            self._AssetContainers.remove(obj)

    def getLocations(self):
        """The spatail description of a piece of property.
        """
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.LandProperties if q != self]
            self._Locations._LandProperties = filtered
        for r in value:
            if self not in r._LandProperties:
                r._LandProperties.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._LandProperties:
                obj._LandProperties.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._LandProperties:
                obj._LandProperties.remove(self)
            self._Locations.remove(obj)

    def getRightOfWays(self):
        """All rights of way this land property has.
        """
        return self._RightOfWays

    def setRightOfWays(self, value):
        for p in self._RightOfWays:
            filtered = [q for q in p.LandProperties if q != self]
            self._RightOfWays._LandProperties = filtered
        for r in value:
            if self not in r._LandProperties:
                r._LandProperties.append(self)
        self._RightOfWays = value

    RightOfWays = property(getRightOfWays, setRightOfWays)

    def addRightOfWays(self, *RightOfWays):
        for obj in RightOfWays:
            if self not in obj._LandProperties:
                obj._LandProperties.append(self)
            self._RightOfWays.append(obj)

    def removeRightOfWays(self, *RightOfWays):
        for obj in RightOfWays:
            if self in obj._LandProperties:
                obj._LandProperties.remove(self)
            self._RightOfWays.remove(obj)

