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

""" This package is responsible for Settlement and Billing. These classes represent the legal entities who participate in formal or informal agreements.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Informative.InfERPSupport import ErpOrganisation
from CIM import Element
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Agreement



from enthought.traits.api import Instance, List, Property, Str, Date
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "Marketer" class:
#------------------------------------------------------------------------------

class Marketer(ErpOrganisation):
    """ Matches buyers and sellers, and secures transmission (and other ancillary services) needed to complete the energy transaction.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Marketer holds title to a ServiceReservation.
    HeldBy = List(Instance("CIM.IEC61968.Informative.Reservation.ServiceReservation"),
        desc="A Marketer holds title to a ServiceReservation.")

    # A ServiceReservation may be resold by a Marketer.
    ResoldBy = Instance("CIM.IEC61968.Informative.Reservation.ServiceReservation",
        desc="A ServiceReservation may be resold by a Marketer.",
        transient=True,
        opposite="Resells",
        editor=InstanceEditor(name="_servicereservations"))

    def _get_servicereservations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.ServiceReservation" ]
        else:
            return []

    _servicereservations = Property(fget=_get_servicereservations)

    # A Marketer may resell an EnergyProduct.
    Resells_EnergyProduct = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct"),
        desc="A Marketer may resell an EnergyProduct.")

    # A Marketer holds title to an EnergyProduct.
    HoldsTitleTo_EnergyProducts = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct"),
        desc="A Marketer holds title to an EnergyProduct.")

    #--------------------------------------------------------------------------
    #  Begin "Marketer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews", "HeldBy", "ResoldBy", "Resells_EnergyProduct", "HoldsTitleTo_EnergyProducts",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.Marketer",
        title="Marketer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Marketer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FinancialVersion" class:
#------------------------------------------------------------------------------

class FinancialVersion(Element):
    version = Str

    date = Date

    #--------------------------------------------------------------------------
    #  Begin "FinancialVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "version", "date",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.FinancialVersion",
        title="FinancialVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FinancialVersion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerConsumer" class:
#------------------------------------------------------------------------------

class CustomerConsumer(ErpOrganisation):
    """ The energy buyer in the energy marketplace.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A CustomerConsumer may have one or more ServicePoints.
    ServicePoint = List(Instance("CIM.IEC61968.Informative.Reservation.ServicePoint"),
        desc="A CustomerConsumer may have one or more ServicePoints.")

    # A  ControlAreaOperator or CustomerConsumer may ring their perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.
    TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="A  ControlAreaOperator or CustomerConsumer may ring their perimeter with metering, which can create a unique SubControlArea at the collection of metering points, called a TieLine.")

    #--------------------------------------------------------------------------
    #  Begin "CustomerConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews", "ServicePoint", "TieLines",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.CustomerConsumer",
        title="CustomerConsumer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerConsumer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionProvider" class:
#------------------------------------------------------------------------------

class TransmissionProvider(ErpOrganisation):
    """ Provider of the transmission capacity (interconnecting wires between Generation and Consumption) required to fulfill and Energy Transaction's energy exchange. Posts information for transmission paths and AvailableTransmissionCapacities on a reservation node. Buys and sells its products and services on the same reservation node.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A TransmissionProvider offers a TransmissionProduct.
    TransmissionProducts = List(Instance("CIM.IEC61968.Informative.Financial.TransmissionProduct"),
        desc="A TransmissionProvider offers a TransmissionProduct.")

    # A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.
    Flowgate = List(Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate"),
        desc="A flowgate can be reciprocal flowgate for 0 to n transmission providers. A transmission provider may be a reciprocal entity for 0 to n flowgates.")

    # A TransmissionProvider registers one or more ServicePoints.
    ServicePoint = List(Instance("CIM.IEC61968.Informative.Reservation.ServicePoint"),
        desc="A TransmissionProvider registers one or more ServicePoints.")

    # A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
    AncillaryServices = List(Instance("CIM.IEC61968.Informative.Reservation.AncillaryService"),
        desc="A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.")

    # Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
    For = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.LossProfile"),
        desc="Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.")

    # The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
    OfferedBy = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionService"),
        desc="The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).")

    # A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
    SoldBy = List(Instance("CIM.IEC61968.Informative.Reservation.ServiceReservation"),
        desc="A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionProvider" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews", "TransmissionProducts", "Flowgate", "ServicePoint", "AncillaryServices", "For", "OfferedBy", "SoldBy",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.TransmissionProvider",
        title="TransmissionProvider",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionProvider" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionProduct" class:
#------------------------------------------------------------------------------

class TransmissionProduct(IdentifiedObject):
    # A transmission product is offered as a transmission service along a transmission path.
    Offers = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionService"),
        desc="A transmission product is offered as a transmission service along a transmission path.")

    # A TransmissionProvider offers a TransmissionProduct.
    TransmissionProvider = Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider",
        desc="A TransmissionProvider offers a TransmissionProduct.",
        transient=True,
        opposite="TransmissionProducts",
        editor=InstanceEditor(name="_transmissionproviders"))

    def _get_transmissionproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.TransmissionProvider" ]
        else:
            return []

    _transmissionproviders = Property(fget=_get_transmissionproviders)

    # Type of the transmission product. This could be a transmission service class (firm, total transmission capability, or non-firm), transmission service period (on-peak, full-period, off-peak), transmission service increments (yearly extended, hourly fixed, monthly sliding, etc.), transmission service type (network, available transmission capability, or point-to-point, or a transmission service window (fixed hourly, sliding weekly, extended monthly, etc.).
    transmissionProductType = Instance("CIM.EnumeratedType",
        desc="Type of the transmission product. This could be a transmission service class (firm, total transmission capability, or non-firm), transmission service period (on-peak, full-period, off-peak), transmission service increments (yearly extended, hourly fixed, monthly sliding, etc.), transmission service type (network, available transmission capability, or point-to-point, or a transmission service window (fixed hourly, sliding weekly, extended monthly, etc.).",
        transient=True,
        editor=InstanceEditor(name="_enumeratedtypes"))

    def _get_enumeratedtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.EnumeratedType" ]
        else:
            return []

    _enumeratedtypes = Property(fget=_get_enumeratedtypes)

    # A transmission product is located on a transmission path.
    LocationFor = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionPath"),
        desc="A transmission product is located on a transmission path.")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionProduct" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Offers", "TransmissionProvider", "transmissionProductType", "LocationFor",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.TransmissionProduct",
        title="TransmissionProduct",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionProduct" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GenerationProvider" class:
#------------------------------------------------------------------------------

class GenerationProvider(ErpOrganisation):
    """ The energy seller in the energy marketplace.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A GenerationProvider operates one or more GeneratingUnits.
    GeneratingUnits = List(Instance("CIM.IEC61970.Generation.Production.GeneratingUnit"),
        desc="A GenerationProvider operates one or more GeneratingUnits.")

    EnergyProducts = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct"))

    # A GenerationProvider has one or more ServicePoints where energy is injected into the network.
    ServicePoint = List(Instance("CIM.IEC61968.Informative.Reservation.ServicePoint"),
        desc="A GenerationProvider has one or more ServicePoints where energy is injected into the network.")

    #--------------------------------------------------------------------------
    #  Begin "GenerationProvider" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews", "GeneratingUnits", "EnergyProducts", "ServicePoint",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.GenerationProvider",
        title="GenerationProvider",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenerationProvider" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OpenAccessProduct" class:
#------------------------------------------------------------------------------

class OpenAccessProduct(Agreement):
    """ Contracts for services offered commercially.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
    ProvidedBy_TransmissionService = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionService"),
        desc="A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.")

    # AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
    AncillaryServices = List(Instance("CIM.IEC61968.Informative.Reservation.AncillaryService"),
        desc="AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.")

    #--------------------------------------------------------------------------
    #  Begin "OpenAccessProduct" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "ProvidedBy_TransmissionService", "AncillaryServices",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.OpenAccessProduct",
        title="OpenAccessProduct",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OpenAccessProduct" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IntSchedAgreement" class:
#------------------------------------------------------------------------------

class IntSchedAgreement(Agreement):
    """ A type of agreement that provides the default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Organisations = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpOrganisation"))

    # The default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting. Method #1 is to integrate the instantaneous schedule between the hourly boundaries. Method #2 compensates for any up/down ramping that occurs across the hourly boundary (this is called block accounting).
    defaultIntegrationMethod = Instance("CIM.EnumeratedType",
        desc="The default method by which interchange schedules are to be integrated to obtain hourly energy schedules for accounting. Method #1 is to integrate the instantaneous schedule between the hourly boundaries. Method #2 compensates for any up/down ramping that occurs across the hourly boundary (this is called block accounting).",
        transient=True,
        editor=InstanceEditor(name="_enumeratedtypes"))

    def _get_enumeratedtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.EnumeratedType" ]
        else:
            return []

    _enumeratedtypes = Property(fget=_get_enumeratedtypes)

    #--------------------------------------------------------------------------
    #  Begin "IntSchedAgreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "Organisations", "defaultIntegrationMethod",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.IntSchedAgreement",
        title="IntSchedAgreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IntSchedAgreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ControlAreaOperator" class:
#------------------------------------------------------------------------------

class ControlAreaOperator(ErpOrganisation):
    """ Operates the Control Area. Approves and implements energy transactions. Verifies both Inter-Control Area and Intra-Control Area transactions for the power system before granting approval (and implementing) the transactions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sale of ancillary services provided by ControlAreaOperators.
    AncillaryService = List(Instance("CIM.IEC61968.Informative.Reservation.AncillaryService"),
        desc="Sale of ancillary services provided by ControlAreaOperators.")

    # A ControlAreaCompany controls a ControlArea.
    ControlledBy = Instance("CIM.IEC61968.Informative.EnergyScheduling.HostControlArea",
        desc="A ControlAreaCompany controls a ControlArea.",
        transient=True,
        opposite="Controls",
        editor=InstanceEditor(name="_hostcontrolareas"))

    def _get_hostcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.HostControlArea" ]
        else:
            return []

    _hostcontrolareas = Property(fget=_get_hostcontrolareas)

    # A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.
    TieLines = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.TieLine"),
        desc="A ControlAreaOperator has a collection of tie points that ring the ControlArea, called a TieLine.")

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaOperator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "category", "mode", "optOut", "industryID", "isProfitCenter", "isCostCenter", "governmentID",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "DocumentRoles", "ActivityRecords", "LocationRoles", "ErpPersonRoles", "ViolationLimits", "Requests", "ChangeItems", "IntSchedAgreement", "RegisteredResources", "PowerSystemResourceRoles", "AssetRoles", "LandPropertyRoles", "ParentOrganisationRoles", "ChildOrganisationRoles", "Crews", "AncillaryService", "ControlledBy", "TieLines",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.Financial.ControlAreaOperator",
        title="ControlAreaOperator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlAreaOperator" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
