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

from CIM import Element
from CIM.IEC61968.Common import Document
from CIM.IEC61968.Common import Agreement
from CIM.IEC61968.Common import Organisation
from CIM.IEC61968.Metering import DeviceFunction
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.PaymentMetering import TenderKind
from CIM.IEC61970.Domain import Money
from CIM.IEC61968.PaymentMetering import TransactionKind
from CIM.IEC61968.PaymentMetering import CreditKind
from CIM.IEC61968.PaymentMetering import ChargeKind



from enthought.traits.api import Instance, List, Property, Bool, Date, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ReceiptSummary" class:
#------------------------------------------------------------------------------

class ReceiptSummary(Element):
    """ Record of detail of receipts pertaining to one shift of operation (one record per 'tenderKind').
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Shift for which this summary is given.
    Shift = Instance("CIM.IEC61968.PaymentMetering.Shift",
        desc="Shift for which this summary is given.",
        transient=True,
        opposite="ReceiptSummaries",
        editor=InstanceEditor(name="_shifts"))

    def _get_shifts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Shift" ]
        else:
            return []

    _shifts = Property(fget=_get_shifts)

    # Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.
    line = Instance("CIM.IEC61968.PaymentMetering.LineDetail",
        desc="Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.",
        transient=True,
        editor=InstanceEditor(name="_linedetails"))

    def _get_linedetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.LineDetail" ]
        else:
            return []

    _linedetails = Property(fget=_get_linedetails)

    # 'Tender.kind' for which 'receiptsTotal' is given.
    tenderKind = TenderKind(desc="'Tender.kind' for which 'receiptsTotal' is given.")

    #--------------------------------------------------------------------------
    #  Begin "ReceiptSummary" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "tenderKind",
                label="Attributes"),
            VGroup("Parent", "Shift", "line",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.ReceiptSummary",
        title="ReceiptSummary",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReceiptSummary" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BankStatement" class:
#------------------------------------------------------------------------------

class BankStatement(Document):
    """ A type of Document that records bank deposits made by Vendor of revenue collected at PointOfSale.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The Vendor that made this BankStatement (by making deposit).
    Vendor = Instance("CIM.IEC61968.PaymentMetering.Vendor",
        desc="The Vendor that made this BankStatement (by making deposit).",
        transient=True,
        opposite="BankStatements",
        editor=InstanceEditor(name="_vendors"))

    def _get_vendors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Vendor" ]
        else:
            return []

    _vendors = Property(fget=_get_vendors)

    MerchantAccount = Instance("CIM.IEC61968.PaymentMetering.MerchantAccount",
        transient=True,
        opposite="BankStatements",
        editor=InstanceEditor(name="_merchantaccounts"))

    def _get_merchantaccounts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.MerchantAccount" ]
        else:
            return []

    _merchantaccounts = Property(fget=_get_merchantaccounts)

    # BankAccount that generated this bank statement.
    BankAccount = Instance("CIM.IEC61968.Informative.InfCommon.BankAccount",
        desc="BankAccount that generated this bank statement.",
        transient=True,
        opposite="BankStatements",
        editor=InstanceEditor(name="_bankaccounts"))

    def _get_bankaccounts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfCommon.BankAccount" ]
        else:
            return []

    _bankaccounts = Property(fget=_get_bankaccounts)

    # The amount that is deposited into the bank via BankAccount.
    depositAmount = Money(desc="The amount that is deposited into the bank via BankAccount.")

    # True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system.
    posted = Bool(desc="True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system.")

    # The date and time the deposit is made.
    depositDateTime = Date(desc="The date and time the deposit is made.")

    # The amount on this statement that is to be credited to MerchantAccount.
    merchantCreditAmount = Money(desc="The amount on this statement that is to be credited to MerchantAccount.")

    #--------------------------------------------------------------------------
    #  Begin "BankStatement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "depositAmount", "posted", "depositDateTime", "merchantCreditAmount",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Vendor", "MerchantAccount", "BankAccount",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.BankStatement",
        title="BankStatement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BankStatement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TSPAgreement" class:
#------------------------------------------------------------------------------

class TSPAgreement(Agreement):
    """ A contractual agreement between a supplier (utility) and a transaction service provider (a type of organisation) that governs the terms and conditions, under which authorisation the transaction service provider may process transactions on behalf of the supplier.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "TSPAgreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.TSPAgreement",
        title="TSPAgreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TSPAgreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransactionSummary" class:
#------------------------------------------------------------------------------

class TransactionSummary(Element):
    """ The record of detail of payment transactions pertaining to one shift of operation (one record per 'transactionKind').
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Shift to which this summary applies.
    Shift = Instance("CIM.IEC61968.PaymentMetering.Shift",
        desc="Shift to which this summary applies.",
        transient=True,
        opposite="TransactionSummaries",
        editor=InstanceEditor(name="_shifts"))

    def _get_shifts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Shift" ]
        else:
            return []

    _shifts = Property(fget=_get_shifts)

    # Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.
    line = Instance("CIM.IEC61968.PaymentMetering.LineDetail",
        desc="Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.",
        transient=True,
        editor=InstanceEditor(name="_linedetails"))

    def _get_linedetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.LineDetail" ]
        else:
            return []

    _linedetails = Property(fget=_get_linedetails)

    # 'Transaction.kind' for which 'transactionsTotal' is given.
    transactionKind = TransactionKind(desc="'Transaction.kind' for which 'transactionsTotal' is given.")

    #--------------------------------------------------------------------------
    #  Begin "TransactionSummary" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "transactionKind",
                label="Attributes"),
            VGroup("Parent", "Shift", "line",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.TransactionSummary",
        title="TransactionSummary",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransactionSummary" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Bank" class:
#------------------------------------------------------------------------------

class Bank(Organisation):
    """ Organisation that is a commercial bank, agency, or other institution that offers a similar service.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All BankAccounts this Bank provides.
    BankAccounts = List(Instance("CIM.IEC61968.Informative.InfCommon.BankAccount"),
        desc="All BankAccounts this Bank provides.")

    # International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362).
    iban = Str(desc="International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362).")

    # Codified reference to the particular branch of the bank where BankAccount is held.
    branchCode = Str(desc="Codified reference to the particular branch of the bank where BankAccount is held.")

    # Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation.
    bic = Str(desc="Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation.")

    #--------------------------------------------------------------------------
    #  Begin "Bank" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "iban", "branchCode", "bic",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "BankAccounts",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.Bank",
        title="Bank",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Bank" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SDPAccountingFunction" class:
#------------------------------------------------------------------------------

class SDPAccountingFunction(DeviceFunction):
    """ Service delivery point accounting function, particularly for payment meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ChargeRegisters = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.ChargeRegister"))

    # The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.
    availableCredit = Instance("CIM.IEC61968.PaymentMetering.AccountingUnit",
        desc="The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.",
        transient=True,
        editor=InstanceEditor(name="_accountingunits"))

    def _get_accountingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountingUnit" ]
        else:
            return []

    _accountingunits = Property(fget=_get_accountingunits)

    # The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.
    creditExpiryLevel = Instance("CIM.IEC61968.PaymentMetering.AccountingUnit",
        desc="The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.",
        transient=True,
        editor=InstanceEditor(name="_accountingunits"))

    def _get_accountingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountingUnit" ]
        else:
            return []

    _accountingunits = Property(fget=_get_accountingunits)

    CreditRegisters = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.CreditRegister"))

    ServiceKind = Instance("CIM.IEC61968.Customers.ServiceCategory",
        transient=True,
        opposite="SPAccountingFunctions",
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

    # The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.
    lowCreditWarningLevel = Instance("CIM.IEC61968.PaymentMetering.AccountingUnit",
        desc="The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.",
        transient=True,
        editor=InstanceEditor(name="_accountingunits"))

    def _get_accountingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountingUnit" ]
        else:
            return []

    _accountingunits = Property(fget=_get_accountingunits)

    #--------------------------------------------------------------------------
    #  Begin "SDPAccountingFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents", "ChargeRegisters", "availableCredit", "creditExpiryLevel", "CreditRegisters", "ServiceKind", "lowCreditWarningLevel",
                label="References", columns=4),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.SDPAccountingFunction",
        title="SDPAccountingFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SDPAccountingFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CreditRegister" class:
#------------------------------------------------------------------------------

class CreditRegister(IdentifiedObject):
    """ Accumulated credits transacted per CreditKind for a given function. There could be several of these registers, one for each CreditKind; depending on the application.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    creditAmount = Instance("CIM.IEC61968.PaymentMetering.AccountingUnit",
        desc="Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.",
        transient=True,
        editor=InstanceEditor(name="_accountingunits"))

    def _get_accountingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountingUnit" ]
        else:
            return []

    _accountingunits = Property(fget=_get_accountingunits)

    SDPAccountingFunction = Instance("CIM.IEC61968.Informative.InfPaymentMetering.SDPAccountingFunction",
        transient=True,
        opposite="CreditRegisters",
        editor=InstanceEditor(name="_sdpaccountingfunctions"))

    def _get_sdpaccountingfunctions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfPaymentMetering.SDPAccountingFunction" ]
        else:
            return []

    _sdpaccountingfunctions = Property(fget=_get_sdpaccountingfunctions)

    # Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend.
    creditKind = CreditKind(desc="Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend.")

    #--------------------------------------------------------------------------
    #  Begin "CreditRegister" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "creditKind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "creditAmount", "SDPAccountingFunction",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.CreditRegister",
        title="CreditRegister",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CreditRegister" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Token" class:
#------------------------------------------------------------------------------

class Token(IdentifiedObject):
    """ The token that is transferred to the payment meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # PointOfSale tha sold or dispensed this Token.
    PointOfSale = Instance("CIM.IEC61968.PaymentMetering.PointOfSale",
        desc="PointOfSale tha sold or dispensed this Token.",
        transient=True,
        opposite="Tokens",
        editor=InstanceEditor(name="_pointofsales"))

    def _get_pointofsales(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.PointOfSale" ]
        else:
            return []

    _pointofsales = Property(fget=_get_pointofsales)

    # Coded representation of the token that is transferred to the payment meter.
    code = Str(desc="Coded representation of the token that is transferred to the payment meter.")

    # Free-format note relevant to this token.
    comment = Str(desc="Free-format note relevant to this token.")

    #--------------------------------------------------------------------------
    #  Begin "Token" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "code", "comment",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PointOfSale",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.Token",
        title="Token",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Token" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ChargeRegister" class:
#------------------------------------------------------------------------------

class ChargeRegister(IdentifiedObject):
    """ Accumulated charges transacted per ChargeKind for a given function. There could be several of these registers, one for each ChargeKind; depending on the application.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    chargeAmount = Instance("CIM.IEC61968.PaymentMetering.AccountingUnit",
        desc="Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.",
        transient=True,
        editor=InstanceEditor(name="_accountingunits"))

    def _get_accountingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountingUnit" ]
        else:
            return []

    _accountingunits = Property(fget=_get_accountingunits)

    SPAccountingFunction = Instance("CIM.IEC61968.Informative.InfPaymentMetering.SDPAccountingFunction",
        transient=True,
        opposite="ChargeRegisters",
        editor=InstanceEditor(name="_sdpaccountingfunctions"))

    def _get_sdpaccountingfunctions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfPaymentMetering.SDPAccountingFunction" ]
        else:
            return []

    _sdpaccountingfunctions = Property(fget=_get_sdpaccountingfunctions)

    # Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis.
    chargeKind = ChargeKind(desc="Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis.")

    #--------------------------------------------------------------------------
    #  Begin "ChargeRegister" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "chargeKind",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "chargeAmount", "SPAccountingFunction",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.InfPaymentMetering.ChargeRegister",
        title="ChargeRegister",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ChargeRegister" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
