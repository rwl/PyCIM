#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Informative.InfCommon import Role
from CIM.IEC61968.Common import Agreement
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Location



from enthought.traits.api import Instance, List, Property, Enum, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of zone.
ZoneKind = Enum("specialRestrictionLand", "electricalNetwork", "weatherZone", "other", desc="Kind of zone.")
# Kind of (land) property.
LandPropertyKind = Enum("store", "depot", "customerPremise", "external", "gridSupplyPoint", "substation", "building", desc="Kind of (land) property.")
# Demographic kind of a land property.
DemographicKind = Enum("other", "urban", "rural", desc="Demographic kind of a land property.")

#------------------------------------------------------------------------------
#  "LocLocRole" class:
#------------------------------------------------------------------------------

class LocLocRole(Role):
    """ The relationship between one Location and another Location. One 'roleType' is 'Directions,' for which an additional attribute serves for providing a textual description for navigating from one location to another location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ToLocation = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="FromLocationRoles",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    FromLocation = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="ToLocationRoles",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    # Detailed directional information.
    directionInfo = Str(desc="Detailed directional information.")

    #--------------------------------------------------------------------------
    #  Begin "LocLocRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category", "directionInfo",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ToLocation", "FromLocation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.LocLocRole",
        title="LocLocRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LocLocRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RightOfWay" class:
#------------------------------------------------------------------------------

class RightOfWay(Agreement):
    """ A right-of-way (ROW) is for land where it is lawful to use for a public road, an electric power line, etc. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All land properties this right of way applies to.
    LandProperties = List(Instance("CIM.IEC61968.Informative.InfLocations.LandProperty"),
        desc="All land properties this right of way applies to.")

    # Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
    propertyData = Str(desc="Property related information that describes the ROW's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.")

    #--------------------------------------------------------------------------
    #  Begin "RightOfWay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate", "propertyData",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "LandProperties",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.RightOfWay",
        title="RightOfWay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RightOfWay" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OrgLocRole" class:
#------------------------------------------------------------------------------

class OrgLocRole(Role):
    """ Roles played between Organisations and Locations, for example a service territory or school district. Note that roles dealing with use of a specific piece of property should be defined based on the relationship between OccupationsOfProperty and Location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="LocationRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    Location = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="ErpOrganisationRoles",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    #--------------------------------------------------------------------------
    #  Begin "OrgLocRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ErpOrganisation", "Location",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.OrgLocRole",
        title="OrgLocRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OrgLocRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OrgPropertyRole" class:
#------------------------------------------------------------------------------

class OrgPropertyRole(Role):
    """ Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpOrganisation = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation",
        transient=True,
        opposite="LandPropertyRoles",
        editor=InstanceEditor(name="_erporganisations"))

    def _get_erporganisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation" ]
        else:
            return []

    _erporganisations = Property(fget=_get_erporganisations)

    LandProperty = List(Instance("CIM.IEC61968.Informative.InfLocations.LandProperty"))

    #--------------------------------------------------------------------------
    #  Begin "OrgPropertyRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "ErpOrganisation", "LandProperty",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.OrgPropertyRole",
        title="OrgPropertyRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OrgPropertyRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AssetLocRole" class:
#------------------------------------------------------------------------------

class AssetLocRole(Role):
    """ Roles played between Assets and Locations.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Asset = Instance("CIM.IEC61968.Assets.Asset",
        transient=True,
        opposite="LocationRoles",
        editor=InstanceEditor(name="_assets"))

    def _get_assets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Assets.Asset" ]
        else:
            return []

    _assets = Property(fget=_get_assets)

    Location = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="AssetRoles",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    #--------------------------------------------------------------------------
    #  Begin "AssetLocRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Asset", "Location",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.AssetLocRole",
        title="AssetLocRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetLocRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ErpPersonLocRole" class:
#------------------------------------------------------------------------------

class ErpPersonLocRole(Role):
    """ Roles played between People and Locations. Some Locations are somewhat static, like the person's home address. Other may be dynamic, for example when the person is part of a crew driving around in truck.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Location = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="ErpPersonRoles",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="LocationRoles",
        editor=InstanceEditor(name="_erppersons"))

    def _get_erppersons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPerson" ]
        else:
            return []

    _erppersons = Property(fget=_get_erppersons)

    #--------------------------------------------------------------------------
    #  Begin "ErpPersonLocRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Location", "ErpPerson",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.ErpPersonLocRole",
        title="ErpPersonLocRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ErpPersonLocRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Route" class:
#------------------------------------------------------------------------------

class Route(IdentifiedObject):
    """ Route that is followed, for example by service crews.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Category by utility's work management standards and practices.
    category = Str(desc="Category by utility's work management standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "Route" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Locations", "Crews", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.Route",
        title="Route",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Route" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Zone" class:
#------------------------------------------------------------------------------

class Zone(Location):
    """ Area divided off from other areas. It may be part of the electrical network, a land area where special restrictions apply, weather areas, etc. For weather, it is an area where a set of relatively homogenous weather measurements apply.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Kind of this zone.
    kind = ZoneKind(desc="Kind of this zone.")

    #--------------------------------------------------------------------------
    #  Begin "Zone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference", "kind",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.Zone",
        title="Zone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Zone" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DocLocRole" class:
#------------------------------------------------------------------------------

class DocLocRole(Role):
    """ Roles played between Documents and Locations. For example, as ErpAddress is a type of Location and WorkBilling is a type of Document, a role is the address for which to mail the invoice. As a TroubleTicket is a type of Document, one instance of Location may be the address for which the trouble is reported.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Location = Instance("CIM.IEC61968.Common.Location",
        transient=True,
        opposite="DocumentRoles",
        editor=InstanceEditor(name="_locations"))

    def _get_locations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Location" ]
        else:
            return []

    _locations = Property(fget=_get_locations)

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="LocationRoles",
        editor=InstanceEditor(name="_documents"))

    def _get_documents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Document" ]
        else:
            return []

    _documents = Property(fget=_get_documents)

    #--------------------------------------------------------------------------
    #  Begin "DocLocRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Location", "Document",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.DocLocRole",
        title="DocLocRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DocLocRole" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SchematicLocation" class:
#------------------------------------------------------------------------------

class SchematicLocation(Location):
    """ Schematic location. Intended to be used in the context of diagrams (worked out by WG13 in 2008 and 2009).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "SchematicLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.SchematicLocation",
        title="SchematicLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SchematicLocation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RedLine" class:
#------------------------------------------------------------------------------

class RedLine(IdentifiedObject):
    """ This class is used for handling the accompanying annotations, time stamp, author, etc. of designs, drawings and maps. A red line can be associated with any Location object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    #--------------------------------------------------------------------------
    #  Begin "RedLine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "Locations",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.RedLine",
        title="RedLine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RedLine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LocationGrant" class:
#------------------------------------------------------------------------------

class LocationGrant(Agreement):
    """ A grant provides a right, as defined by type, for a parcel of land. Note that the association to Location, Asset, Organisation, etc. for the Grant is inherited from Agreement, a type of Document.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Land property this location grant applies to.
    LandProperty = Instance("CIM.IEC61968.Informative.InfLocations.LandProperty",
        desc="Land property this location grant applies to.",
        transient=True,
        opposite="LocationGrants",
        editor=InstanceEditor(name="_landpropertys"))

    def _get_landpropertys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfLocations.LandProperty" ]
        else:
            return []

    _landpropertys = Property(fget=_get_landpropertys)

    # Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.
    propertyData = Str(desc="Property related information that describes the Grant's land parcel. For example, it may be a deed book number, deed book page number, and parcel number.")

    #--------------------------------------------------------------------------
    #  Begin "LocationGrant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate", "propertyData",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "LandProperty",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.LocationGrant",
        title="LocationGrant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LocationGrant" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LandProperty" class:
#------------------------------------------------------------------------------

class LandProperty(IdentifiedObject):
    """ Information about a particular piece of (land) property such as its use. Ownership of the property may be determined through associations to Organisations and/or ErpPersons.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All location grants this land property has.
    LocationGrants = List(Instance("CIM.IEC61968.Informative.InfLocations.LocationGrant"),
        desc="All location grants this land property has.")

    AssetContainers = List(Instance("CIM.IEC61968.Assets.AssetContainer"))

    ErpSiteLevelDatas = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpSiteLevelData"))

    ErpPersonRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.PersonPropertyRole"))

    # The spatail description of a piece of property.
    Locations = List(Instance("CIM.IEC61968.Common.Location"),
        desc="The spatail description of a piece of property.")

    # All rights of way this land property has.
    RightOfWays = List(Instance("CIM.IEC61968.Informative.InfLocations.RightOfWay"),
        desc="All rights of way this land property has.")

    ErpOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.OrgPropertyRole"))

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Kind of (land) property, categorised according to its main functional use from the utility's perspective.
    kind = LandPropertyKind(desc="Kind of (land) property, categorised according to its main functional use from the utility's perspective.")

    # Demographics around the site.
    demographicKind = DemographicKind(desc="Demographics around the site.")

    # Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation.
    externalRecordReference = Str(desc="Reference allocated by the governing organisation (such as municipality) to this piece of land that has a formal reference to Surveyor General's records. The governing organisation is specified in associated Organisation.")

    #--------------------------------------------------------------------------
    #  Begin "LandProperty" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "demographicKind", "externalRecordReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "LocationGrants", "AssetContainers", "ErpSiteLevelDatas", "ErpPersonRoles", "Locations", "RightOfWays", "ErpOrganisationRoles", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.LandProperty",
        title="LandProperty",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LandProperty" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Hazard" class:
#------------------------------------------------------------------------------

class Hazard(IdentifiedObject):
    """ A hazard is any object or condition that is a danger for causing loss or perils to an asset and/or people. Examples of hazards are trees growing under overhead power lines, a park being located by a substation (i.e., children climb fence to recover a ball), a lake near an overhead distribution line (fishing pole/line contacting power lines), etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Assets = List(Instance("CIM.IEC61968.Assets.Asset"))

    # The point or polygon location of a given hazard.
    Locations = List(Instance("CIM.IEC61968.Common.Location"),
        desc="The point or polygon location of a given hazard.")

    status = Instance("CIM.IEC61968.Common.Status",
        transient=True,
        editor=InstanceEditor(name="_statuss"))

    def _get_statuss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Status" ]
        else:
            return []

    _statuss = Property(fget=_get_statuss)

    # Category by utility's corporate standards and practices.
    category = Str(desc="Category by utility's corporate standards and practices.")

    #--------------------------------------------------------------------------
    #  Begin "Hazard" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Assets", "Locations", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.Hazard",
        title="Hazard",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Hazard" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PersonPropertyRole" class:
#------------------------------------------------------------------------------

class PersonPropertyRole(Role):
    """ The role of a person relative to a given piece of property. Examples of roles include: owner, renter, contractor, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LandProperty = Instance("CIM.IEC61968.Informative.InfLocations.LandProperty",
        transient=True,
        opposite="ErpPersonRoles",
        editor=InstanceEditor(name="_landpropertys"))

    def _get_landpropertys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfLocations.LandProperty" ]
        else:
            return []

    _landpropertys = Property(fget=_get_landpropertys)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="LandPropertyRoles",
        editor=InstanceEditor(name="_erppersons"))

    def _get_erppersons(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfERPSupport.ErpPerson" ]
        else:
            return []

    _erppersons = Property(fget=_get_erppersons)

    #--------------------------------------------------------------------------
    #  Begin "PersonPropertyRole" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "category",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "status", "LandProperty", "ErpPerson",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfLocations.PersonPropertyRole",
        title="PersonPropertyRole",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PersonPropertyRole" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
