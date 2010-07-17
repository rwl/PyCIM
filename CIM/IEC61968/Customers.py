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

""" This package contains the core information classes that support customer billing applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Document
from CIM.IEC61968.Common import Organisation
from CIM.IEC61968.Common import Agreement
from CIM.IEC61968.Common import Location
from CIM.IEC61970.Domain import AbsoluteDate



from enthought.traits.api import Instance, List, Property, Enum, Str, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of customer.
CustomerKind = Enum("windMachine", "residentialFarmService", "residential", "energyServiceSupplier", "residentialStreetlightOthers", "other", "pumpingLoad", "commercialIndustrial", "residentialAndStreetlight", "residentialAndCommercial", "energyServiceScheduler", "internalUse", desc="Kind of customer.")
# Accounting classification of the type of revenue collected for the CustomerAgreement, typically used to break down accounts for revenue accounting.
RevenueKind = Enum("streetLight", "commercial", "other", "irrigation", "nonResidential", "industrial", "residential", desc="Accounting classification of the type of revenue collected for the CustomerAgreement, typically used to break down accounts for revenue accounting.")
# Kind of service.
ServiceKind = Enum("refuse", "other", "tvLicence", "internet", "electricty", "water", "heat", "rates", "gas", "sewerage", "time", desc="Kind of service.")

#------------------------------------------------------------------------------
#  "ServiceCategory" class:
#------------------------------------------------------------------------------

class ServiceCategory(IdentifiedObject):
    """ Category of service provided to the customer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"))

    # All service delivery points that deliver this category of service.
    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"),
        desc="All service delivery points that deliver this category of service.")

    SPAccountingFunctions = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.SDPAccountingFunction"))

    # All pricing structures applicable to this service category.
    PricingStructures = List(Instance("CIM.IEC61968.Customers.PricingStructure"),
        desc="All pricing structures applicable to this service category.")

    # Kind of service.
    kind = ServiceKind(desc="Kind of service.")

    #--------------------------------------------------------------------------
    #  Begin "ServiceCategory" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CustomerAgreements", "ServiceDeliveryPoints", "SPAccountingFunctions", "PricingStructures",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Customers.ServiceCategory",
        title="ServiceCategory",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServiceCategory" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerAccount" class:
#------------------------------------------------------------------------------

class CustomerAccount(Document):
    """ Assignment of a group of products and services purchased by the Customer through a CustomerAgreement, used as a mechanism for customer billing and payment. It contains common information from the various types of CustomerAgreements to create billings (invoices) for a Customer and receive payment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    WorkBillingInfos = List(Instance("CIM.IEC61968.Informative.InfCustomers.WorkBillingInfo"))

    # All payment transactions for this customer account.
    PaymentTransactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"),
        desc="All payment transactions for this customer account.")

    # All agreements for this customer account.
    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"),
        desc="All agreements for this customer account.")

    CustomerBillingInfos = List(Instance("CIM.IEC61968.Informative.InfCustomers.CustomerBillingInfo"))

    ErpInvoicees = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoice"))

    # Budget bill code.
    budgetBill = Str(desc="Budget bill code.")

    # Cycle day on which this customer account will normally be billed, used to determine when to produce the CustomerBillingInfo for this customer account.
    billingCycle = Str(desc="Cycle day on which this customer account will normally be billed, used to determine when to produce the CustomerBillingInfo for this customer account.")

    #--------------------------------------------------------------------------
    #  Begin "CustomerAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "budgetBill", "billingCycle",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "WorkBillingInfos", "PaymentTransactions", "CustomerAgreements", "CustomerBillingInfos", "ErpInvoicees",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Customers.CustomerAccount",
        title="CustomerAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerAccount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Tariff" class:
#------------------------------------------------------------------------------

class Tariff(Document):
    """ Document, approved by the responsible regulatory agency, listing the terms and conditions, including a schedule of prices, under which utility services will be provided. It has a unique number within the state or province. For Rate Schedules it is frequently allocated by the affiliated Public Utilities Commission.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All pricing structures using this tariff.
    PricingStructures = List(Instance("CIM.IEC61968.Customers.PricingStructure"),
        desc="All pricing structures using this tariff.")

    # All tariff profiles using this tariff.
    TariffProfiles = List(Instance("CIM.IEC61968.PaymentMetering.TariffProfile"),
        desc="All tariff profiles using this tariff.")

    # Date tariff was activated.
    startDate = AbsoluteDate(desc="Date tariff was activated.")

    # (if tariff became inactive) Date tariff was terminated.
    endDate = AbsoluteDate(desc="(if tariff became inactive) Date tariff was terminated.")

    #--------------------------------------------------------------------------
    #  Begin "Tariff" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "startDate", "endDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "PricingStructures", "TariffProfiles",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Customers.Tariff",
        title="Tariff",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Tariff" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PricingStructure" class:
#------------------------------------------------------------------------------

class PricingStructure(Document):
    """ Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All tariffs used by this pricing structure.
    Tariffs = List(Instance("CIM.IEC61968.Customers.Tariff"),
        desc="All tariffs used by this pricing structure.")

    PowerQualityPricings = List(Instance("CIM.IEC61968.Informative.InfCustomers.PowerQualityPricing"))

    # All transactions applying this pricing structure.
    Transactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"),
        desc="All transactions applying this pricing structure.")

    # All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.
    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"),
        desc="All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.")

    # All customer agreements with this pricing structure.
    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"),
        desc="All customer agreements with this pricing structure.")

    # SubscribePowerCurve specifies the cost according to a prcing structure.
    SubscribePowerCurve = Instance("CIM.IEC61968.Informative.InfCustomers.SubscribePowerCurve",
        desc="SubscribePowerCurve specifies the cost according to a prcing structure.",
        transient=True,
        opposite="PricingStructure",
        editor=InstanceEditor(name="_subscribepowercurves"))

    def _get_subscribepowercurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCustomers.SubscribePowerCurve" ]
        else:
            return []

    _subscribepowercurves = Property(fget=_get_subscribepowercurves)

    # Service category to which this pricing structure applies.
    ServiceCategory = Instance("CIM.IEC61968.Customers.ServiceCategory",
        desc="Service category to which this pricing structure applies.",
        transient=True,
        opposite="PricingStructures",
        editor=InstanceEditor(name="_servicecategorys"))

    def _get_servicecategorys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.ServiceCategory" ]
        else:
            return []

    _servicecategorys = Property(fget=_get_servicecategorys)

    # (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes).
    revenueKind = RevenueKind(desc="(Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes).")

    # Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code.
    code = Str(desc="Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code.")

    # Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
    dailyFloorUsage = Int(desc="Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage.")

    # True if this pricing structure is not taxable.
    taxExemption = Bool(desc="True if this pricing structure is not taxable.")

    # Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
    dailyCeilingUsage = Int(desc="Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage.")

    # Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting.
    dailyEstimatedUsage = Int(desc="Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting.")

    #--------------------------------------------------------------------------
    #  Begin "PricingStructure" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "revenueKind", "code", "dailyFloorUsage", "taxExemption", "dailyCeilingUsage", "dailyEstimatedUsage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Tariffs", "PowerQualityPricings", "Transactions", "ServiceDeliveryPoints", "CustomerAgreements", "SubscribePowerCurve", "ServiceCategory",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Customers.PricingStructure",
        title="PricingStructure",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PricingStructure" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Customer" class:
#------------------------------------------------------------------------------

class Customer(Organisation):
    """ Organisation receiving services from ServiceSupplier.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TroubleTickets = List(Instance("CIM.IEC61968.Informative.InfOperations.TroubleTicket"))

    # All the works performed for this customer.
    Works = List(Instance("CIM.IEC61968.Work.Work"),
        desc="All the works performed for this customer.")

    OutageNotifications = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageNotification"))

    ErpPersons = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpPerson"))

    # All end device assets of this customer.
    EndDeviceAssets = List(Instance("CIM.IEC61968.Metering.EndDeviceAsset"),
        desc="All end device assets of this customer.")

    # All agreements of this customer.
    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"),
        desc="All agreements of this customer.")

    PlannedOutage = Instance("CIM.IEC61968.Informative.InfOperations.PlannedOutage",
        transient=True,
        opposite="CustomerDatas",
        editor=InstanceEditor(name="_plannedoutages"))

    def _get_plannedoutages(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfOperations.PlannedOutage" ]
        else:
            return []

    _plannedoutages = Property(fget=_get_plannedoutages)

    # Status of this customer.
    status = Instance("CIM.IEC61968.Common.Status",
        desc="Status of this customer.",
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

    # Kind of customer.
    kind = CustomerKind(desc="Kind of customer.")

    # (if applicable) Public Utility Commission identification number.
    pucNumber = Str(desc="(if applicable) Public Utility Commission identification number.")

    # True if customer organisation has special service needs such as life support, hospitals, etc.
    specialNeed = Str(desc="True if customer organisation has special service needs such as life support, hospitals, etc.")

    # True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute.
    vip = Bool(desc="True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute.")

    #--------------------------------------------------------------------------
    #  Begin "Customer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "pucNumber", "specialNeed", "vip",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "TroubleTickets", "Works", "OutageNotifications", "ErpPersons", "EndDeviceAssets", "CustomerAgreements", "PlannedOutage", "status",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Customers.Customer",
        title="Customer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Customer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerAgreement" class:
#------------------------------------------------------------------------------

class CustomerAgreement(Agreement):
    """ Agreement between the Customer and the ServiceSupplier to pay for service at a specific ServiceLocation. It records certain billing information about the type of service provided at the ServiceLocation and is used during charge creation to determine the type of service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Service supplier for this customer agreement.
    ServiceSupplier = Instance("CIM.IEC61968.PaymentMetering.ServiceSupplier",
        desc="Service supplier for this customer agreement.",
        transient=True,
        opposite="CustomerAgreements",
        editor=InstanceEditor(name="_servicesuppliers"))

    def _get_servicesuppliers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.ServiceSupplier" ]
        else:
            return []

    _servicesuppliers = Property(fget=_get_servicesuppliers)

    # All service locations regulated by this customer agreement.
    ServiceLocations = List(Instance("CIM.IEC61968.Customers.ServiceLocation"),
        desc="All service locations regulated by this customer agreement.")

    ServiceCategory = Instance("CIM.IEC61968.Customers.ServiceCategory",
        transient=True,
        opposite="CustomerAgreements",
        editor=InstanceEditor(name="_servicecategorys"))

    def _get_servicecategorys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.ServiceCategory" ]
        else:
            return []

    _servicecategorys = Property(fget=_get_servicecategorys)

    # All service delivery points regulated by this customer agreement.
    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"),
        desc="All service delivery points regulated by this customer agreement.")

    # Demand response program for this customer agreement.
    DemandResponseProgram = Instance("CIM.IEC61968.Metering.DemandResponseProgram",
        desc="Demand response program for this customer agreement.",
        transient=True,
        opposite="CustomerAgreements",
        editor=InstanceEditor(name="_demandresponseprograms"))

    def _get_demandresponseprograms(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.DemandResponseProgram" ]
        else:
            return []

    _demandresponseprograms = Property(fget=_get_demandresponseprograms)

    # (could be deprecated in the future) All meter readings for this customer agreement.
    MeterReadings = List(Instance("CIM.IEC61968.Metering.MeterReading"),
        desc="(could be deprecated in the future) All meter readings for this customer agreement.")

    # All (non-service related) auxiliary agreements that refer to this customer agreement.
    AuxiliaryAgreements = List(Instance("CIM.IEC61968.PaymentMetering.AuxiliaryAgreement"),
        desc="All (non-service related) auxiliary agreements that refer to this customer agreement.")

    Equipments = List(Instance("CIM.IEC61970.Core.Equipment"))

    # Could be deprecated in the future.
    EndDeviceControls = List(Instance("CIM.IEC61968.Metering.EndDeviceControl"),
        desc="Could be deprecated in the future.")

    # Customer account owning this agreement.
    CustomerAccount = Instance("CIM.IEC61968.Customers.CustomerAccount",
        desc="Customer account owning this agreement.",
        transient=True,
        opposite="CustomerAgreements",
        editor=InstanceEditor(name="_customeraccounts"))

    def _get_customeraccounts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.CustomerAccount" ]
        else:
            return []

    _customeraccounts = Property(fget=_get_customeraccounts)

    # Customer for this agreement.
    Customer = Instance("CIM.IEC61968.Customers.Customer",
        desc="Customer for this agreement.",
        transient=True,
        opposite="CustomerAgreements",
        editor=InstanceEditor(name="_customers"))

    def _get_customers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.Customer" ]
        else:
            return []

    _customers = Property(fget=_get_customers)

    StandardIndustryCode = Instance("CIM.IEC61968.Informative.InfCustomers.StandardIndustryCode",
        transient=True,
        opposite="CustomerAgreements",
        editor=InstanceEditor(name="_standardindustrycodes"))

    def _get_standardindustrycodes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCustomers.StandardIndustryCode" ]
        else:
            return []

    _standardindustrycodes = Property(fget=_get_standardindustrycodes)

    # All pricing structures applicable to this customer agreement.
    PricingStructures = List(Instance("CIM.IEC61968.Customers.PricingStructure"),
        desc="All pricing structures applicable to this customer agreement.")

    #--------------------------------------------------------------------------
    #  Begin "CustomerAgreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "ServiceSupplier", "ServiceLocations", "ServiceCategory", "ServiceDeliveryPoints", "DemandResponseProgram", "MeterReadings", "AuxiliaryAgreements", "Equipments", "EndDeviceControls", "CustomerAccount", "Customer", "StandardIndustryCode", "PricingStructures",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Customers.CustomerAgreement",
        title="CustomerAgreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerAgreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ServiceLocation" class:
#------------------------------------------------------------------------------

class ServiceLocation(Location):
    """ A customer ServiceLocation has one or more ServiceDeliveryPoint(s), which in turn relate to Meters. The location may be a point or a polygon, depending on the specific circumstances. For distribution, the ServiceLocation is typically the location of the utility customer's premise. Because a customer's premise may have one or more meters, the ServiceDeliveryPoint is used to define the actual conducting equipment that the EndDeviceAsset attaches to at the utility customer's ServiceLocation. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All customer agreements regulating this service location.
    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"),
        desc="All customer agreements regulating this service location.")

    # All end device assets that measure the service delivered to this service location.
    EndDeviceAssets = List(Instance("CIM.IEC61968.Metering.EndDeviceAsset"),
        desc="All end device assets that measure the service delivered to this service location.")

    # All service delivery points delivering service (of the same type) to this service location.
    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"),
        desc="All service delivery points delivering service (of the same type) to this service location.")

    # True if inspection is needed of facilities at this service location. This could be requested by a customer, due to suspected tampering, environmental concerns (e.g., a fire in the vicinity), or to correct incompatible data.
    needsInspection = Bool(desc="True if inspection is needed of facilities at this service location. This could be requested by a customer, due to suspected tampering, environmental concerns (e.g., a fire in the vicinity), or to correct incompatible data.")

    # Method for the service person to access the appropriate service locations. For example, a description of where to obtain a key if the facility is unmanned and secured.
    accessMethod = Str(desc="Method for the service person to access the appropriate service locations. For example, a description of where to obtain a key if the facility is unmanned and secured.")

    # Problems previously encountered when visiting or performing work on this site. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.
    siteAccessProblem = Str(desc="Problems previously encountered when visiting or performing work on this site. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.")

    #--------------------------------------------------------------------------
    #  Begin "ServiceLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference", "needsInspection", "accessMethod", "siteAccessProblem",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "CustomerAgreements", "EndDeviceAssets", "ServiceDeliveryPoints",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Customers.ServiceLocation",
        title="ServiceLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServiceLocation" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
