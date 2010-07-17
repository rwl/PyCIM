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

""" This package contains the information classes that support distribution management in general.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM import Element
from CIM.IEC61970.Domain import AbsoluteDate
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import StringQuantity



from enthought.traits.api import Instance, List, Property, Str, Date, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Organisation" class:
#------------------------------------------------------------------------------

class Organisation(IdentifiedObject):
    """ Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BusinessRoles = List(Instance("CIM.IEC61968.Informative.InfCommon.BusinessRole"))

    # All telephone numbers of this organisation.
    TelephoneNumbers = List(Instance("CIM.IEC61968.Common.TelephoneNumber"),
        desc="All telephone numbers of this organisation.")

    # Street address.
    streetAddress = Instance("CIM.IEC61968.Common.StreetAddress",
        desc="Street address.",
        transient=True,
        editor=InstanceEditor(name="_streetaddresss"))

    def _get_streetaddresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.StreetAddress" ]
        else:
            return []

    _streetaddresss = Property(fget=_get_streetaddresss)

    MarketRoles = List(Instance("CIM.IEC61968.Informative.InfCommon.MarketRole"))

    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postalAddress = Instance("CIM.IEC61968.Common.PostalAddress",
        desc="Postal address, potentially different than 'streetAddress' (e.g., another city).",
        transient=True,
        editor=InstanceEditor(name="_postaladdresss"))

    def _get_postaladdresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.PostalAddress" ]
        else:
            return []

    _postaladdresss = Property(fget=_get_postaladdresss)

    # All electronic addresses of this organisation.
    ElectronicAddresses = List(Instance("CIM.IEC61968.Common.ElectronicAddress"),
        desc="All electronic addresses of this organisation.")

    #--------------------------------------------------------------------------
    #  Begin "Organisation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.Organisation",
        title="Organisation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Organisation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ActivityRecord" class:
#------------------------------------------------------------------------------

class ActivityRecord(IdentifiedObject):
    """ Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MarketFactors = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketFactors"))

    # All documents for which this activity record has been created.
    Documents = List(Instance("CIM.IEC61968.Common.Document"),
        desc="All documents for which this activity record has been created.")

    Organisations = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation"))

    ScheduledEvent = Instance("CIM.IEC61968.Informative.InfCommon.ScheduledEvent",
        transient=True,
        opposite="ActivityRecord",
        editor=InstanceEditor(name="_scheduledevents"))

    def _get_scheduledevents(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCommon.ScheduledEvent" ]
        else:
            return []

    _scheduledevents = Property(fget=_get_scheduledevents)

    # All assets for which this activity record has been created.
    Assets = List(Instance("CIM.IEC61968.Assets.Asset"),
        desc="All assets for which this activity record has been created.")

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    Locations = List(Instance("CIM.IEC61968.Common.Location"))

    # Information on consequence of event resulting in this activity record.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Information on consequence of event resulting in this activity record.",
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

    # Reason for event resulting in this activity record, typically supplied when user initiated.
    reason = Str(desc="Reason for event resulting in this activity record, typically supplied when user initiated.")

    # Category of event resulting in this activity record.
    category = Str(desc="Category of event resulting in this activity record.")

    # Severity level of event resulting in this activity record.
    severity = Str(desc="Severity level of event resulting in this activity record.")

    # Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable).
    createdDateTime = Date(desc="Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable).")

    #--------------------------------------------------------------------------
    #  Begin "ActivityRecord" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.ActivityRecord",
        title="ActivityRecord",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ActivityRecord" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Document" class:
#------------------------------------------------------------------------------

class Document(IdentifiedObject):
    """ Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All activity records created for this document.
    ActivityRecords = List(Instance("CIM.IEC61968.Common.ActivityRecord"),
        desc="All activity records created for this document.")

    ErpOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.DocOrgRole"))

    ScheduledEvents = List(Instance("CIM.IEC61968.Informative.InfCommon.ScheduledEvent"))

    FromDocumentRoles = List(Instance("CIM.IEC61968.Informative.InfCommon.DocDocRole"))

    LocationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.DocLocRole"))

    PowerSystemResourceRoles = List(Instance("CIM.IEC61968.Informative.InfCommon.DocPsrRole"))

    NetworkDataSets = List(Instance("CIM.IEC61968.Informative.InfOperations.NetworkDataSet"))

    ErpPersonRoles = List(Instance("CIM.IEC61968.Informative.InfERPSupport.DocErpPersonRole"))

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    # Measurements are specified in types of documents, such as procedures.
    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"),
        desc="Measurements are specified in types of documents, such as procedures.")

    # Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
    docStatus = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.",
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

    ScheduleParameterInfos = List(Instance("CIM.IEC61968.Informative.InfCommon.ScheduleParameterInfo"))

    ElectronicAddress = Instance("CIM.IEC61968.Common.ElectronicAddress",
        transient=True,
        opposite="Document",
        editor=InstanceEditor(name="_electronicaddresss"))

    def _get_electronicaddresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.ElectronicAddress" ]
        else:
            return []

    _electronicaddresss = Property(fget=_get_electronicaddresss)

    ToDocumentRoles = List(Instance("CIM.IEC61968.Informative.InfCommon.DocDocRole"))

    # Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.",
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

    AssetRoles = List(Instance("CIM.IEC61968.Informative.InfAssets.DocAssetRole"))

    ChangeSets = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeSet"))

    # Document subject.
    subject = Str(desc="Document subject.")

    # Revision number for this document.
    revisionNumber = Str(desc="Revision number for this document.")

    # Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).
    category = Str(desc="Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.).")

    # Date and time this document was last modified. Documents may potentially be modified many times during their lifetime.
    lastModifiedDateTime = Date(desc="Date and time this document was last modified. Documents may potentially be modified many times during their lifetime.")

    # Document title.
    title = Str(desc="Document title.")

    # Date and time that this document was created.
    createdDateTime = Date(desc="Date and time that this document was created.")

    #--------------------------------------------------------------------------
    #  Begin "Document" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Common.Document",
        title="Document",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Document" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PositionPoint" class:
#------------------------------------------------------------------------------

class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Location that this position point describes.
    Location = Instance("CIM.IEC61968.Common.Location",
        desc="Location that this position point describes.",
        transient=True,
        opposite="PositionPoints",
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

    # Zero-relative sequence number of this point within a series of points.
    sequenceNumber = Int(desc="Zero-relative sequence number of this point within a series of points.")

    # (if applicable) Z axis position.
    zPosition = Str(desc="(if applicable) Z axis position.")

    # X axis position.
    xPosition = Str(desc="X axis position.")

    # Y axis position.
    yPosition = Str(desc="Y axis position.")

    #--------------------------------------------------------------------------
    #  Begin "PositionPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sequenceNumber", "zPosition", "xPosition", "yPosition",
                label="Attributes"),
            VGroup("Parent", "Location",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.PositionPoint",
        title="PositionPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PositionPoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Location" class:
#------------------------------------------------------------------------------

class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    DocumentRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.DocLocRole"))

    ErpPersonRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.ErpPersonLocRole"))

    # All electronic addresses of this location.
    ElectronicAddresses = List(Instance("CIM.IEC61968.Common.ElectronicAddress"),
        desc="All electronic addresses of this location.")

    ChangeItems = List(Instance("CIM.IEC61968.Informative.InfOperations.ChangeItem"))

    Routes = List(Instance("CIM.IEC61968.Informative.InfLocations.Route"))

    # Sequence of position points describing this location.
    PositionPoints = List(Instance("CIM.IEC61968.Common.PositionPoint"),
        desc="Sequence of position points describing this location.")

    GmlSelectors = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlSelector"))

    # Main address of the location.
    mainAddress = Instance("CIM.IEC61968.Common.StreetAddress",
        desc="Main address of the location.",
        transient=True,
        editor=InstanceEditor(name="_streetaddresss"))

    def _get_streetaddresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.StreetAddress" ]
        else:
            return []

    _streetaddresss = Property(fget=_get_streetaddresss)

    FromLocationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.LocLocRole"))

    # Status of this location.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this location.",
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

    ToLocationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.LocLocRole"))

    # All telephone numbers of this location.
    TelephoneNumbers = List(Instance("CIM.IEC61968.Common.TelephoneNumber"),
        desc="All telephone numbers of this location.")

    # Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
    secondaryAddress = Instance("CIM.IEC61968.Common.StreetAddress",
        desc="Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.",
        transient=True,
        editor=InstanceEditor(name="_streetaddresss"))

    def _get_streetaddresss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.StreetAddress" ]
        else:
            return []

    _streetaddresss = Property(fget=_get_streetaddresss)

    LandProperties = List(Instance("CIM.IEC61968.Informative.InfLocations.LandProperty"))

    Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"))

    ErpOrganisationRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.OrgLocRole"))

    DimensionsInfo = Instance("CIM.IEC61968.Informative.InfAssets.DimensionsInfo",
        transient=True,
        opposite="Locations",
        editor=InstanceEditor(name="_dimensionsinfos"))

    def _get_dimensionsinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.DimensionsInfo" ]
        else:
            return []

    _dimensionsinfos = Property(fget=_get_dimensionsinfos)

    AssetRoles = List(Instance("CIM.IEC61968.Informative.InfLocations.AssetLocRole"))

    Crews = List(Instance("CIM.IEC61968.Informative.InfWork.Crew"))

    RedLines = List(Instance("CIM.IEC61968.Informative.InfLocations.RedLine"))

    GmlObservatins = List(Instance("CIM.IEC61968.Informative.InfGMLSupport.GmlObservation"))

    Hazards = List(Instance("CIM.IEC61968.Informative.InfLocations.Hazard"))

    ActivityRecords = List(Instance("CIM.IEC61968.Common.ActivityRecord"))

    # Utility-specific code for the location.
    corporateCode = Str(desc="Utility-specific code for the location.")

    # (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building.
    direction = Str(desc="(if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building.")

    # True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments.
    isPolygon = Bool(desc="True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments.")

    # Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location).
    category = Str(desc="Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location).")

    # (if applicable) Reference to geographical information source, often external to the utility.
    geoInfoReference = Str(desc="(if applicable) Reference to geographical information source, often external to the utility.")

    #--------------------------------------------------------------------------
    #  Begin "Location" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Common.Location",
        title="Location",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Location" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StreetAddress" class:
#------------------------------------------------------------------------------

class StreetAddress(Element):
    """ General purpose street address information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Status of this address.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this address.",
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

    # Town detail.
    townDetail = Instance("CIM.IEC61968.Common.TownDetail",
        desc="Town detail.",
        transient=True,
        editor=InstanceEditor(name="_towndetails"))

    def _get_towndetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.TownDetail" ]
        else:
            return []

    _towndetails = Property(fget=_get_towndetails)

    # Street detail.
    streetDetail = Instance("CIM.IEC61968.Common.StreetDetail",
        desc="Street detail.",
        transient=True,
        editor=InstanceEditor(name="_streetdetails"))

    def _get_streetdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.StreetDetail" ]
        else:
            return []

    _streetdetails = Property(fget=_get_streetdetails)

    #--------------------------------------------------------------------------
    #  Begin "StreetAddress" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent", "status", "townDetail", "streetDetail",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.StreetAddress",
        title="StreetAddress",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StreetAddress" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TelephoneNumber" class:
#------------------------------------------------------------------------------

class TelephoneNumber(IdentifiedObject):
    """ Telephone number.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Organisation owning this telephone number.
    Organisation = Instance("CIM.IEC61968.Common.Organisation",
        desc="Organisation owning this telephone number.",
        transient=True,
        opposite="TelephoneNumbers",
        editor=InstanceEditor(name="_organisations"))

    def _get_organisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Organisation" ]
        else:
            return []

    _organisations = Property(fget=_get_organisations)

    # Location owning this telephone number.
    Location = Instance("CIM.IEC61968.Common.Location",
        desc="Location owning this telephone number.",
        transient=True,
        opposite="TelephoneNumbers",
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

    # (if applicable) City code.
    cityCode = Str(desc="(if applicable) City code.")

    # Country code.
    countryCode = Str(desc="Country code.")

    # (if applicable) Extension for this telephone number.
    extension = Str(desc="(if applicable) Extension for this telephone number.")

    # Area or region code.
    areaCode = Str(desc="Area or region code.")

    # Main (local) part of this telephone number.
    localNumber = Str(desc="Main (local) part of this telephone number.")

    #--------------------------------------------------------------------------
    #  Begin "TelephoneNumber" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "cityCode", "countryCode", "extension", "areaCode", "localNumber",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Organisation", "Location",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.TelephoneNumber",
        title="TelephoneNumber",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TelephoneNumber" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DateTimeInterval" class:
#------------------------------------------------------------------------------

class DateTimeInterval(Element):
    """ Interval of date and time.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date and time that this interval ended.
    end = Date(desc="Date and time that this interval ended.")

    # Date and time that this interval started.
    start = Date(desc="Date and time that this interval started.")

    #--------------------------------------------------------------------------
    #  Begin "DateTimeInterval" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "end", "start",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.DateTimeInterval",
        title="DateTimeInterval",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DateTimeInterval" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PostalAddress" class:
#------------------------------------------------------------------------------

class PostalAddress(Element):
    """ General purpose postal address information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Street detail.
    streetDetail = Instance("CIM.IEC61968.Common.StreetDetail",
        desc="Street detail.",
        transient=True,
        editor=InstanceEditor(name="_streetdetails"))

    def _get_streetdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.StreetDetail" ]
        else:
            return []

    _streetdetails = Property(fget=_get_streetdetails)

    # Town detail.
    townDetail = Instance("CIM.IEC61968.Common.TownDetail",
        desc="Town detail.",
        transient=True,
        editor=InstanceEditor(name="_towndetails"))

    def _get_towndetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.TownDetail" ]
        else:
            return []

    _towndetails = Property(fget=_get_towndetails)

    # Post office box.
    poBox = Str(desc="Post office box.")

    # Postal code for the address.
    postalCode = Str(desc="Postal code for the address.")

    #--------------------------------------------------------------------------
    #  Begin "PostalAddress" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "poBox", "postalCode",
                label="Attributes"),
            VGroup("Parent", "streetDetail", "townDetail",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.PostalAddress",
        title="PostalAddress",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PostalAddress" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TownDetail" class:
#------------------------------------------------------------------------------

class TownDetail(Element):
    """ Town details, in the context of address.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Name of the state or province.
    stateOrProvince = Str(desc="Name of the state or province.")

    # Town code.
    code = Str(desc="Town code.")

    # Town name.
    name = Str(desc="Town name.")

    # Town section. For example, it is common for there to be 36 sections per township.
    section = Str(desc="Town section. For example, it is common for there to be 36 sections per township.")

    # Name of the country.
    country = Str(desc="Name of the country.")

    #--------------------------------------------------------------------------
    #  Begin "TownDetail" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "stateOrProvince", "code", "name", "section", "country",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.TownDetail",
        title="TownDetail",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TownDetail" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ElectronicAddress" class:
#------------------------------------------------------------------------------

class ElectronicAddress(IdentifiedObject):
    """ Electronic address information.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpTelephoneNumbers = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpTelephoneNumber"))

    # All locations having this electronic address.
    Locations = List(Instance("CIM.IEC61968.Common.Location"),
        desc="All locations having this electronic address.")

    Cashier = Instance("CIM.IEC61968.PaymentMetering.Cashier",
        transient=True,
        opposite="ElectronicAddresses",
        editor=InstanceEditor(name="_cashiers"))

    def _get_cashiers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Cashier" ]
        else:
            return []

    _cashiers = Property(fget=_get_cashiers)

    ErpPerson = Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson",
        transient=True,
        opposite="ElectronicAddresses",
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

    # Asset owning this electronic address.
    Asset = Instance("CIM.IEC61968.Assets.Asset",
        desc="Asset owning this electronic address.",
        transient=True,
        opposite="ElectronicAddresses",
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

    # Status of this electronic address.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this electronic address.",
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

    Document = Instance("CIM.IEC61968.Common.Document",
        transient=True,
        opposite="ElectronicAddress",
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

    # Organisation owning this electronic address.
    Organisation = Instance("CIM.IEC61968.Common.Organisation",
        desc="Organisation owning this electronic address.",
        transient=True,
        opposite="ElectronicAddresses",
        editor=InstanceEditor(name="_organisations"))

    def _get_organisations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.Organisation" ]
        else:
            return []

    _organisations = Property(fget=_get_organisations)

    # World Wide Web address.
    web = Str(desc="World Wide Web address.")

    # Email address.
    email = Str(desc="Email address.")

    # Password needed to log in.
    password = Str(desc="Password needed to log in.")

    # Address on local area network.
    lan = Str(desc="Address on local area network.")

    # User ID needed to log in, which can be for an individual person, an organisation, a location, etc.
    userID = Str(desc="User ID needed to log in, which can be for an individual person, an organisation, a location, etc.")

    # Radio address.
    radio = Str(desc="Radio address.")

    #--------------------------------------------------------------------------
    #  Begin "ElectronicAddress" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "web", "email", "password", "lan", "userID", "radio",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ErpTelephoneNumbers", "Locations", "Cashier", "ErpPerson", "Asset", "status", "Document", "Organisation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.ElectronicAddress",
        title="ElectronicAddress",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ElectronicAddress" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TimePoint" class:
#------------------------------------------------------------------------------

class TimePoint(IdentifiedObject):
    """ A point in time within a sequence of points in time relative to a TimeSchedule.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
    window = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    ScheduledEvents = List(Instance("CIM.IEC61968.Informative.InfCommon.ScheduledEvent"))

    # Time schedule owning this time point.
    TimeSchedule = Instance("CIM.IEC61968.Common.TimeSchedule",
        desc="Time schedule owning this time point.",
        transient=True,
        opposite="TimePoints",
        editor=InstanceEditor(name="_timeschedules"))

    def _get_timeschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.TimeSchedule" ]
        else:
            return []

    _timeschedules = Property(fget=_get_timeschedules)

    # Status of this time point.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this time point.",
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

    # (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'.
    relativeTimeInterval = Seconds(desc="(if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'.")

    # Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived.
    absoluteTime = Date(desc="Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived.")

    # (if sequence-based) Relative sequence number for this time point.
    sequenceNumber = Int(desc="(if sequence-based) Relative sequence number for this time point.")

    #--------------------------------------------------------------------------
    #  Begin "TimePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "relativeTimeInterval", "absoluteTime", "sequenceNumber",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "window", "ScheduledEvents", "TimeSchedule", "status",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.TimePoint",
        title="TimePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TimePoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "UserAttribute" class:
#------------------------------------------------------------------------------

class UserAttribute(Element):
    """ Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PropertySpecification = Instance("CIM.IEC61968.Informative.InfAssets.Specification",
        transient=True,
        opposite="AssetProperites",
        editor=InstanceEditor(name="_specifications"))

    def _get_specifications(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Specification" ]
        else:
            return []

    _specifications = Property(fget=_get_specifications)

    RatingSpecification = Instance("CIM.IEC61968.Informative.InfAssets.Specification",
        transient=True,
        opposite="Ratings",
        editor=InstanceEditor(name="_specifications"))

    def _get_specifications(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Specification" ]
        else:
            return []

    _specifications = Property(fget=_get_specifications)

    PropertyAssets = List(Instance("CIM.IEC61968.Assets.Asset"))

    RatingAssets = List(Instance("CIM.IEC61968.Assets.Asset"))

    ErpLedgerEntries = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpLedgerEntry"))

    ProcedureDataSets = List(Instance("CIM.IEC61968.Informative.InfAssets.ProcedureDataSet"))

    # Transaction for which this snapshot has been recorded.
    Transaction = Instance("CIM.IEC61968.PaymentMetering.Transaction",
        desc="Transaction for which this snapshot has been recorded.",
        transient=True,
        opposite="UserAttributes",
        editor=InstanceEditor(name="_transactions"))

    def _get_transactions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Transaction" ]
        else:
            return []

    _transactions = Property(fget=_get_transactions)

    Procedure = Instance("CIM.IEC61968.Informative.InfAssets.Procedure",
        transient=True,
        opposite="ProcedureValues",
        editor=InstanceEditor(name="_procedures"))

    def _get_procedures(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.Procedure" ]
        else:
            return []

    _procedures = Property(fget=_get_procedures)

    PassThroughBills = List(Instance("CIM.IEC61968.Informative.MarketOperations.PassThroughBill"))

    ErpInvoiceLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    BillDeterminants = List(Instance("CIM.IEC61968.Informative.MarketOperations.BillDeterminant"))

    ErpStatementLineItems = List(Instance("CIM.IEC61968.Informative.MarketOperations.MarketStatementLineItem"))

    # Sequence number for this attribute in a list of attributes.
    sequenceNumber = Int(desc="Sequence number for this attribute in a list of attributes.")

    # Value of an attribute, including unit information.
    value = StringQuantity(desc="Value of an attribute, including unit information.")

    # Name of an attribute.
    name = Str(desc="Name of an attribute.")

    #--------------------------------------------------------------------------
    #  Begin "UserAttribute" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sequenceNumber", "value", "name",
                label="Attributes"),
            VGroup("Parent", "PropertySpecification", "RatingSpecification", "PropertyAssets", "RatingAssets", "ErpLedgerEntries", "ProcedureDataSets", "Transaction", "Procedure", "PassThroughBills", "ErpInvoiceLineItems", "BillDeterminants", "ErpStatementLineItems",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Common.UserAttribute",
        title="UserAttribute",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "UserAttribute" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Status" class:
#------------------------------------------------------------------------------

class Status(Element):
    """ Current status information relevant to an entity.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date and time for which status 'value' applies.
    dateTime = Date(desc="Date and time for which status 'value' applies.")

    # Reason code or explanation for why an object went to the current status 'value'.
    reason = Str(desc="Reason code or explanation for why an object went to the current status 'value'.")

    # Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies.
    value = Str(desc="Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies.")

    # Pertinent information regarding the current 'value', as free form text.
    remark = Str(desc="Pertinent information regarding the current 'value', as free form text.")

    #--------------------------------------------------------------------------
    #  Begin "Status" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "dateTime", "reason", "value", "remark",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.Status",
        title="Status",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Status" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StreetDetail" class:
#------------------------------------------------------------------------------

class StreetDetail(Element):
    """ Street details, in the context of address.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc.
    buildingName = Str(desc="(if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc.")

    # Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.
    type = Str(desc="Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc.")

    # Name of the street.
    name = Str(desc="Name of the street.")

    # True if this street is within the legal geographical boundaries of the specified town (default).
    withinTownLimits = Bool(desc="True if this street is within the legal geographical boundaries of the specified town (default).")

    # Designator of the specific location on the street.
    number = Str(desc="Designator of the specific location on the street.")

    # Suffix to the street name. For example: North, South, East, West.
    suffix = Str(desc="Suffix to the street name. For example: North, South, East, West.")

    # Prefix to the street name. For example: North, South, East, West.
    prefix = Str(desc="Prefix to the street name. For example: North, South, East, West.")

    # (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets.
    code = Str(desc="(if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets.")

    # Additional address information, for example a mailstop.
    addressGeneral = Str(desc="Additional address information, for example a mailstop.")

    # Number of the apartment or suite.
    suiteNumber = Str(desc="Number of the apartment or suite.")

    #--------------------------------------------------------------------------
    #  Begin "StreetDetail" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "buildingName", "type", "name", "withinTownLimits", "number", "suffix", "prefix", "code", "addressGeneral", "suiteNumber",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Common.StreetDetail",
        title="StreetDetail",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StreetDetail" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Agreement" class:
#------------------------------------------------------------------------------

class Agreement(Document):
    """ Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Date and time interval this agreement is valid (from going into effect to termination).
    validityInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Date and time interval this agreement is valid (from going into effect to termination).",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # Date this agreement was consummated among associated persons and/or organisations.
    signDate = AbsoluteDate(desc="Date this agreement was consummated among associated persons and/or organisations.")

    #--------------------------------------------------------------------------
    #  Begin "Agreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Common.Agreement",
        title="Agreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Agreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TimeSchedule" class:
#------------------------------------------------------------------------------

class TimeSchedule(Document):
    """ Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sequence of time points belonging to this time schedule.
    TimePoints = List(Instance("CIM.IEC61968.Common.TimePoint"),
        desc="Sequence of time points belonging to this time schedule.")

    # Schedule date and time interval.
    scheduleInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Schedule date and time interval.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # True if this schedule is deactivated (disabled).
    disabled = Bool(desc="True if this schedule is deactivated (disabled).")

    # The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour.
    offset = Seconds(desc="The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour.")

    # Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.).
    recurrencePattern = Str(desc="Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.).")

    # Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min).
    recurrencePeriod = Seconds(desc="Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min).")

    #--------------------------------------------------------------------------
    #  Begin "TimeSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "disabled", "offset", "recurrencePattern", "recurrencePeriod",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "TimePoints", "scheduleInterval",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Common.TimeSchedule",
        title="TimeSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TimeSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GeoLocation" class:
#------------------------------------------------------------------------------

class GeoLocation(Location):
    """ Geographical location.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All power system resources at this geographical location.
    PowerSystemResources = List(Instance("CIM.IEC61970.Core.PowerSystemResource"),
        desc="All power system resources at this geographical location.")

    #--------------------------------------------------------------------------
    #  Begin "GeoLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "PowerSystemResources",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Common.GeoLocation",
        title="GeoLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GeoLocation" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
