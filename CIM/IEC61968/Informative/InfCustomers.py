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

""" The package is used to define detailed customer models.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import Agreement
from CIM.IEC61968.Common import Document
from CIM.IEC61970.Core import Curve
from CIM.IEC61970.Domain import AbsoluteDate
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import Voltage



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of customer billing.
CustomerBillingKind = Enum("separateEssUdc", "other", "consolidatedEss", "consolidatedUdc", desc="Kind of customer billing.")

#------------------------------------------------------------------------------
#  "ExternalCustomerAgreement" class:
#------------------------------------------------------------------------------

class ExternalCustomerAgreement(Agreement):
    """ A type of customer agreement involving an external agency. For example, a customer may form a contracts with an Energy Service Supplier if Direct Access is permitted.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ExternalCustomerAgreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.ExternalCustomerAgreement",
        title="ExternalCustomerAgreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ExternalCustomerAgreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StandardIndustryCode" class:
#------------------------------------------------------------------------------

class StandardIndustryCode(Document):
    """ The Standard Industrial Classification (SIC) are the codes that identify the type of products/service an industry is involved in, and used for statutory reporting purposes. For example, in the USA these codes are located by the federal government, and then published in a book entitled 'The Standard Industrial Classification Manual'. The codes are arranged in a hierarchical structure. Note that Residential Service Agreements are not classified according to the SIC codes.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"))

    # Standard alphanumeric code assigned to a particular product/service within an industry.
    code = Str(desc="Standard alphanumeric code assigned to a particular product/service within an industry.")

    #--------------------------------------------------------------------------
    #  Begin "StandardIndustryCode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "code",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "CustomerAgreements",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.StandardIndustryCode",
        title="StandardIndustryCode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StandardIndustryCode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CustomerBillingInfo" class:
#------------------------------------------------------------------------------

class CustomerBillingInfo(Document):
    """ The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpInvoiceLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    CustomerAccount = Instance("CIM.IEC61968.Customers.CustomerAccount",
        transient=True,
        opposite="CustomerBillingInfos",
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

    # Kind of bill customer receives.
    kind = CustomerBillingKind(desc="Kind of bill customer receives.")

    # Type of payment plan.
    pymtPlanType = Str(desc="Type of payment plan.")

    # Business date designated for the billing run which produced this CustomerBillingInfo.
    billingDate = AbsoluteDate(desc="Business date designated for the billing run which produced this CustomerBillingInfo.")

    # Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up.
    pymtPlanAmt = Money(desc="Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up.")

    # Outstanding balance on the CustomerAccount as of the statement date.
    outBalance = Money(desc="Outstanding balance on the CustomerAccount as of the statement date.")

    # Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.
    lastPaymentAmt = Money(desc="Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.")

    # Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.
    lastPaymentDate = AbsoluteDate(desc="Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system.")

    # Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'.
    dueDate = AbsoluteDate(desc="Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'.")

    #--------------------------------------------------------------------------
    #  Begin "CustomerBillingInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "pymtPlanType", "billingDate", "pymtPlanAmt", "outBalance", "lastPaymentAmt", "lastPaymentDate", "dueDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInvoiceLineItems", "CustomerAccount",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.CustomerBillingInfo",
        title="CustomerBillingInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CustomerBillingInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OutageHistory" class:
#------------------------------------------------------------------------------

class OutageHistory(Document):
    """ A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # OutageReports per customer for which this OutageHistory is created.
    OutageReports = List(Instance("CIM.IEC61968.Informative.InfOperations.OutageReport"),
        desc="OutageReports per customer for which this OutageHistory is created.")

    #--------------------------------------------------------------------------
    #  Begin "OutageHistory" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "OutageReports",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.OutageHistory",
        title="OutageHistory",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OutageHistory" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WorkBillingInfo" class:
#------------------------------------------------------------------------------

class WorkBillingInfo(Document):
    """ Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpLineItems = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInvoiceLineItem"))

    CustomerAccount = Instance("CIM.IEC61968.Customers.CustomerAccount",
        transient=True,
        opposite="WorkBillingInfos",
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

    Works = List(Instance("CIM.IEC61968.Work.Work"))

    # Date and time by which payment for bill is expected from client.
    dueDateTime = Date(desc="Date and time by which payment for bill is expected from client.")

    # Date payment was received from client.
    receivedDateTime = Date(desc="Date payment was received from client.")

    # Amount of price on deposit.
    deposit = Money(desc="Amount of price on deposit.")

    # Amount of bill.
    workPrice = Money(desc="Amount of bill.")

    # Discount from standard price.
    discount = Float(desc="Discount from standard price.")

    # Estimated cost for work.
    costEstimate = Money(desc="Estimated cost for work.")

    # Date and time bill was issued to client.
    issueDateTime = Date(desc="Date and time bill was issued to client.")

    #--------------------------------------------------------------------------
    #  Begin "WorkBillingInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "dueDateTime", "receivedDateTime", "deposit", "workPrice", "discount", "costEstimate", "issueDateTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpLineItems", "CustomerAccount", "Works",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.WorkBillingInfo",
        title="WorkBillingInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WorkBillingInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerQualityPricing" class:
#------------------------------------------------------------------------------

class PowerQualityPricing(Document):
    """ Pricing can be based on power quality.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PricingStructure = Instance("CIM.IEC61968.Customers.PricingStructure",
        transient=True,
        opposite="PowerQualityPricings",
        editor=InstanceEditor(name="_pricingstructures"))

    def _get_pricingstructures(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.PricingStructure" ]
        else:
            return []

    _pricingstructures = Property(fget=_get_pricingstructures)

    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"))

    # Emergency low voltage limit.
    emergencyLowVoltLimit = Voltage(desc="Emergency low voltage limit.")

    # Emergency high voltage limit.
    emergencyHighVoltLimit = Voltage(desc="Emergency high voltage limit.")

    # Voltage limit violation cost (Cost per unit Voltage).
    voltLimitViolCost = Float(desc="Voltage limit violation cost (Cost per unit Voltage).")

    # Value of uninterrupted service (Cost per active power).
    valueUninterruptedServiceP = Float(desc="Value of uninterrupted service (Cost per active power).")

    # Normal low voltage limit.
    normalLowVoltLimit = Voltage(desc="Normal low voltage limit.")

    # Voltage imbalance violation cost (Cost per unit Voltage).
    voltImbalanceViolCost = Float(desc="Voltage imbalance violation cost (Cost per unit Voltage).")

    # Normal high voltage limit.
    normalHighVoltLimit = Voltage(desc="Normal high voltage limit.")

    # Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here.
    powerFactorMin = Float(desc="Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here.")

    # Value of uninterrupted service (Cost per energy).
    valueUninterruptedServiceEnergy = Float(desc="Value of uninterrupted service (Cost per energy).")

    #--------------------------------------------------------------------------
    #  Begin "PowerQualityPricing" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "emergencyLowVoltLimit", "emergencyHighVoltLimit", "voltLimitViolCost", "valueUninterruptedServiceP", "normalLowVoltLimit", "voltImbalanceViolCost", "normalHighVoltLimit", "powerFactorMin", "valueUninterruptedServiceEnergy",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "PricingStructure", "ServiceDeliveryPoints",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.PowerQualityPricing",
        title="PowerQualityPricing",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerQualityPricing" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ServiceGuarantee" class:
#------------------------------------------------------------------------------

class ServiceGuarantee(Document):
    """ A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Period in which this service guantee applies.
    applicationPeriod = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Period in which this service guantee applies.",
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

    # True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment.
    automaticPay = Bool(desc="True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment.")

    # Explanation of the requirement and conditions for satisfying it.
    serviceRequirement = Str(desc="Explanation of the requirement and conditions for satisfying it.")

    # Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'.
    payAmount = Money(desc="Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'.")

    #--------------------------------------------------------------------------
    #  Begin "ServiceGuarantee" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "automaticPay", "serviceRequirement", "payAmount",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "applicationPeriod",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.ServiceGuarantee",
        title="ServiceGuarantee",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServiceGuarantee" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SubscribePowerCurve" class:
#------------------------------------------------------------------------------

class SubscribePowerCurve(Curve):
    """ Price curve for specifying the cost of energy (X) at points in time (y1) according to a prcing structure, which is based on a tariff.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    PricingStructure = Instance("CIM.IEC61968.Customers.PricingStructure",
        transient=True,
        opposite="SubscribePowerCurve",
        editor=InstanceEditor(name="_pricingstructures"))

    def _get_pricingstructures(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.PricingStructure" ]
        else:
            return []

    _pricingstructures = Property(fget=_get_pricingstructures)

    #--------------------------------------------------------------------------
    #  Begin "SubscribePowerCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "PricingStructure",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfCustomers.SubscribePowerCurve",
        title="SubscribePowerCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SubscribePowerCurve" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
