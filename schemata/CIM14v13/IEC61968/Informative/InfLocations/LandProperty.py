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

class LandProperty(IdentifiedObject):
    """Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.
    """

    def __init__(self, kind='store', demographicKind='other', externalRecordReference='', LocationGrants=None, AssetContainers=None, ErpSiteLevelDatas=None, ErpPersonRoles=None, Locations=None, RightOfWays=None, ErpOrganisationRoles=None, status=None, *args, **kw_args):
        """Initializes a new 'LandProperty' instance.

        @param kind: Kind of (land) property, categorised according to its main functional use from the utility's perspective. Values are: "store", "depot", "customerPremise", "external", "gridSupplyPoint", "substation", "building"
        @param demographicKind: Demographics around the site. Values are: "other", "urban", "rural"
        @param externalRecordReference: Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation. 
        @param LocationGrants: All location grants this land property has.
        @param AssetContainers:
        @param ErpSiteLevelDatas:
        @param ErpPersonRoles:
        @param Locations: The spatail description of a piece of property.
        @param RightOfWays: All rights of way this land property has.
        @param ErpOrganisationRoles:
        @param status:
        """
        #: Kind of (land) property, categorised according to its main functional use from the utility's perspective.Values are: "store", "depot", "customerPremise", "external", "gridSupplyPoint", "substation", "building"
        self.kind = kind

        #: Demographics around the site.Values are: "other", "urban", "rural"
        self.demographicKind = demographicKind

        #: Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation.
        self.externalRecordReference = externalRecordReference

        self._LocationGrants = []
        self.LocationGrants = [] if LocationGrants is None else LocationGrants

        self._AssetContainers = []
        self.AssetContainers = [] if AssetContainers is None else AssetContainers

        self._ErpSiteLevelDatas = []
        self.ErpSiteLevelDatas = [] if ErpSiteLevelDatas is None else ErpSiteLevelDatas

        self._ErpPersonRoles = []
        self.ErpPersonRoles = [] if ErpPersonRoles is None else ErpPersonRoles

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        self._RightOfWays = []
        self.RightOfWays = [] if RightOfWays is None else RightOfWays

        self._ErpOrganisationRoles = []
        self.ErpOrganisationRoles = [] if ErpOrganisationRoles is None else ErpOrganisationRoles

        self.status = status

        super(LandProperty, self).__init__(*args, **kw_args)

    def getLocationGrants(self):
        """All location grants this land property has.
        """
        return self._LocationGrants

    def setLocationGrants(self, value):
        for x in self._LocationGrants:
            x._LandProperty = None
        for y in value:
            y._LandProperty = self
        self._LocationGrants = value

    LocationGrants = property(getLocationGrants, setLocationGrants)

    def addLocationGrants(self, *LocationGrants):
        for obj in LocationGrants:
            obj._LandProperty = self
            self._LocationGrants.append(obj)

    def removeLocationGrants(self, *LocationGrants):
        for obj in LocationGrants:
            obj._LandProperty = None
            self._LocationGrants.remove(obj)

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

    def getErpSiteLevelDatas(self):
        
        return self._ErpSiteLevelDatas

    def setErpSiteLevelDatas(self, value):
        for x in self._ErpSiteLevelDatas:
            x._LandProperty = None
        for y in value:
            y._LandProperty = self
        self._ErpSiteLevelDatas = value

    ErpSiteLevelDatas = property(getErpSiteLevelDatas, setErpSiteLevelDatas)

    def addErpSiteLevelDatas(self, *ErpSiteLevelDatas):
        for obj in ErpSiteLevelDatas:
            obj._LandProperty = self
            self._ErpSiteLevelDatas.append(obj)

    def removeErpSiteLevelDatas(self, *ErpSiteLevelDatas):
        for obj in ErpSiteLevelDatas:
            obj._LandProperty = None
            self._ErpSiteLevelDatas.remove(obj)

    def getErpPersonRoles(self):
        
        return self._ErpPersonRoles

    def setErpPersonRoles(self, value):
        for x in self._ErpPersonRoles:
            x._LandProperty = None
        for y in value:
            y._LandProperty = self
        self._ErpPersonRoles = value

    ErpPersonRoles = property(getErpPersonRoles, setErpPersonRoles)

    def addErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._LandProperty = self
            self._ErpPersonRoles.append(obj)

    def removeErpPersonRoles(self, *ErpPersonRoles):
        for obj in ErpPersonRoles:
            obj._LandProperty = None
            self._ErpPersonRoles.remove(obj)

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

    status = None

