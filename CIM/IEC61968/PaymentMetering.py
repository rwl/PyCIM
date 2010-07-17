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

""" This package is an extension of the Metering package and contains the information classes that support specialized applications such as prepayment metering. These classes are generally associated with the collection and control of revenue from the customer for a delivered service.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import Document
from CIM import Element
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Common import Agreement
from CIM.IEC61968.Common import Organisation
from CIM.IEC61970.Domain import Money
from CIM.IEC61970.Domain import RealEnergy
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import Currency
from CIM.IEC61970.Domain import UnitMultiplier
from CIM.IEC61970.Domain import AbsoluteDate



from enthought.traits.api import Instance, List, Property, Enum, Str, Date, Int, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of transaction.
TransactionKind = Enum("auxiliaryChargePayment", "tokenExchange", "tokenCancellation", "transactionReversal", "diversePayment", "tokenFreeIssue", "other", "meterConfigurationToken", "tokenSalePayment", "accountPayment", "taxChargePayment", "serviceChargePayment", "tokenGrant", desc="Kind of transaction.")
# Kind of cheque.
ChequeKind = Enum("bankOrder", "postalOrder", "other", desc="Kind of cheque.")
# Kind of supplier.
SupplierKind = Enum("other", "retailer", "utility", desc="Kind of supplier.")
# Kind of tender.
TenderKind = Enum("cheque", "card", "other", "unspecified", "cash", desc="Kind of tender.")
# Kind of charge.
ChargeKind = Enum("other", "auxiliaryCharge", "demandCharge", "taxCharge", "consumptionCharge", desc="Kind of charge.")
# Kind of credit.
CreditKind = Enum("other", "reserveCredit", "lifelineCredit", "advanceCredit", "tokenCredit", "grantCredit", desc="Kind of credit.")

#------------------------------------------------------------------------------
#  "MerchantAccount" class:
#------------------------------------------------------------------------------

class MerchantAccount(Document):
    """ The operating account controlled by MerchantAgreement, against which Vendor may vend tokens or receipt payments. Transactions via VendorShift debit the account and bank deposits via BankStatement credit the account.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All vendors selling tokens or receipt payments against this merchant account.
    Vendors = List(Instance("CIM.IEC61968.PaymentMetering.Vendor"),
        desc="All vendors selling tokens or receipt payments against this merchant account.")

    # All transactors this merchant account is registered with.
    Transactors = List(Instance("CIM.IEC61968.PaymentMetering.Transactor"),
        desc="All transactors this merchant account is registered with.")

    BankStatements = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.BankStatement"))

    # Merchant agreement that instantiated this merchant account.
    MerchantAgreement = Instance("CIM.IEC61968.PaymentMetering.MerchantAgreement",
        desc="Merchant agreement that instantiated this merchant account.",
        transient=True,
        opposite="MerchantAccounts",
        editor=InstanceEditor(name="_merchantagreements"))

    def _get_merchantagreements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.MerchantAgreement" ]
        else:
            return []

    _merchantagreements = Property(fget=_get_merchantagreements)

    # All vendor shifts that operate on this merchant account.
    VendorShifts = List(Instance("CIM.IEC61968.PaymentMetering.VendorShift"),
        desc="All vendor shifts that operate on this merchant account.")

    # The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes).
    provisionalBalance = Money(desc="The balance of this account after taking into account any pending debits from VendorShift.merchantDebitAmount and pending credits from BankStatement.merchantCreditAmount or credits (see also BankStatement attributes and VendorShift attributes).")

    # The current operating balance of this account.
    currentBalance = Money(desc="The current operating balance of this account.")

    #--------------------------------------------------------------------------
    #  Begin "MerchantAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "provisionalBalance", "currentBalance",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "Vendors", "Transactors", "BankStatements", "MerchantAgreement", "VendorShifts",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.MerchantAccount",
        title="MerchantAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MerchantAccount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AuxiliaryAccount" class:
#------------------------------------------------------------------------------

class AuxiliaryAccount(Document):
    """ Variable and dynamic part of AuxiliaryAgreement, generally representing the current state of the account related to the outstanding balance defined in AuxiliaryAgreement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Details of the last debit transaction performed on this account.
    lastDebit = Instance("CIM.IEC61968.PaymentMetering.AccountMovement",
        desc="Details of the last debit transaction performed on this account.",
        transient=True,
        editor=InstanceEditor(name="_accountmovements"))

    def _get_accountmovements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountMovement" ]
        else:
            return []

    _accountmovements = Property(fget=_get_accountmovements)

    # All charges levied on this account.
    Charges = List(Instance("CIM.IEC61968.PaymentMetering.Charge"),
        desc="All charges levied on this account.")

    # Details of the last credit transaction performed on this account.
    lastCredit = Instance("CIM.IEC61968.PaymentMetering.AccountMovement",
        desc="Details of the last credit transaction performed on this account.",
        transient=True,
        editor=InstanceEditor(name="_accountmovements"))

    def _get_accountmovements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AccountMovement" ]
        else:
            return []

    _accountmovements = Property(fget=_get_accountmovements)

    # Auxiliary agreement regulating this account.
    AuxiliaryAgreement = Instance("CIM.IEC61968.PaymentMetering.AuxiliaryAgreement",
        desc="Auxiliary agreement regulating this account.",
        transient=True,
        opposite="AuxiliaryAccounts",
        editor=InstanceEditor(name="_auxiliaryagreements"))

    def _get_auxiliaryagreements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AuxiliaryAgreement" ]
        else:
            return []

    _auxiliaryagreements = Property(fget=_get_auxiliaryagreements)

    # All payments against this account.
    PaymentTransactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"),
        desc="All payments against this account.")

    # Current amounts now due for payment on this account.
    due = Instance("CIM.IEC61968.PaymentMetering.Due",
        desc="Current amounts now due for payment on this account.",
        transient=True,
        editor=InstanceEditor(name="_dues"))

    def _get_dues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Due" ]
        else:
            return []

    _dues = Property(fget=_get_dues)

    # The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid.
    balance = Money(desc="The total amount currently remaining on this account that is required to be paid in order to settle the account to zero. This excludes any due amounts not yet paid.")

    # The initial principle amount, with which this account was instantiated.
    principleAmount = Money(desc="The initial principle amount, with which this account was instantiated.")

    #--------------------------------------------------------------------------
    #  Begin "AuxiliaryAccount" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "balance", "principleAmount",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "lastDebit", "Charges", "lastCredit", "AuxiliaryAgreement", "PaymentTransactions", "due",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.AuxiliaryAccount",
        title="AuxiliaryAccount",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AuxiliaryAccount" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BankAccountDetail" class:
#------------------------------------------------------------------------------

class BankAccountDetail(Element):
    """ Details of a bank account.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Branch of bank where account is held.
    branchCode = Str(desc="Branch of bank where account is held.")

    # National identity number (or equivalent) of account holder.
    holderID = Str(desc="National identity number (or equivalent) of account holder.")

    # Name of account holder.
    holderName = Str(desc="Name of account holder.")

    # Operational account reference number.
    accountNumber = Str(desc="Operational account reference number.")

    # Name of bank where account is held.
    bankName = Str(desc="Name of bank where account is held.")

    #--------------------------------------------------------------------------
    #  Begin "BankAccountDetail" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "branchCode", "holderID", "holderName", "accountNumber", "bankName",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.BankAccountDetail",
        title="BankAccountDetail",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BankAccountDetail" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccountMovement" class:
#------------------------------------------------------------------------------

class AccountMovement(Element):
    """ Credit/debit movements for an account.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears.
    amount = Money(desc="Amount that was credited to/debited from an account. For example: payment received/interest charge on arrears.")

    # Date and time when the credit/debit transaction was performed.
    dateTime = Date(desc="Date and time when the credit/debit transaction was performed.")

    # Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied.
    reason = Str(desc="Reason for credit/debit transaction on an account. Example: payment received/arrears interest levied.")

    #--------------------------------------------------------------------------
    #  Begin "AccountMovement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "amount", "dateTime", "reason",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.AccountMovement",
        title="AccountMovement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccountMovement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TimeTariffInterval" class:
#------------------------------------------------------------------------------

class TimeTariffInterval(Element):
    """ One of a sequence of time intervals defined in terms of real time. It is typically used in association with TariffProfile to define the intervals in a time of use tariff structure, where startDateTime simultaneously determines the starting point of this interval and the ending point of the previous interval.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All tariff profiles defined by this time tariff interval.
    TariffProfiles = List(Instance("CIM.IEC61968.PaymentMetering.TariffProfile"),
        desc="All tariff profiles defined by this time tariff interval.")

    # All charges used to define this time tariff interval.
    Charges = List(Instance("CIM.IEC61968.PaymentMetering.Charge"),
        desc="All charges used to define this time tariff interval.")

    # A real time marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
    startDateTime = Date(desc="A real time marker that defines the starting time (typically it is the time of day) for this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.")

    # A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
    sequenceNumber = Int(desc="A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.")

    #--------------------------------------------------------------------------
    #  Begin "TimeTariffInterval" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "startDateTime", "sequenceNumber",
                label="Attributes"),
            VGroup("Parent", "TariffProfiles", "Charges",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.TimeTariffInterval",
        title="TimeTariffInterval",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TimeTariffInterval" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Due" class:
#------------------------------------------------------------------------------

class Due(Element):
    """ Details on amounts due for an account.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Part of 'current' that constitutes the portion of the principle amount currently due.
    principle = Money(desc="Part of 'current' that constitutes the portion of the principle amount currently due.")

    # Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues.
    current = Money(desc="Current total amount now due: current = principle + arrears + interest + charges. Typically the rule for settlement priority is: interest dues, then arrears dues, then current dues, then charge dues.")

    # Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'.
    charges = Money(desc="Part of 'current' that constitutes the charge portion: 'charges' = 'Charge.fixedPortion' + 'Charge.variablePortion'.")

    # Part of 'current' that constitutes the arrears portion.
    arrears = Money(desc="Part of 'current' that constitutes the arrears portion.")

    # Part of 'current' that constitutes the interest portion.
    interest = Money(desc="Part of 'current' that constitutes the interest portion.")

    #--------------------------------------------------------------------------
    #  Begin "Due" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "principle", "current", "charges", "arrears", "interest",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Due",
        title="Due",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Due" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConsumptionTariffInterval" class:
#------------------------------------------------------------------------------

class ConsumptionTariffInterval(Element):
    """ One of a sequence of intervals defined in terms of consumption quantity of a service such as electricity, water, gas, etc. It is typically used in association with TariffProfile to define the steps or blocks in a step tariff structure, where startValue simultaneously defines the entry value of this step and the closing value of the previous step. Where consumption is &gt;= startValue it falls within this interval and where consumption is &lt; startValue it falls within the previous interval.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All charges used to define this consumption tariff interval.
    Charges = List(Instance("CIM.IEC61968.PaymentMetering.Charge"),
        desc="All charges used to define this consumption tariff interval.")

    # All tariff profiles defined by this consumption tariff interval.
    TariffProfiles = List(Instance("CIM.IEC61968.PaymentMetering.TariffProfile"),
        desc="All tariff profiles defined by this consumption tariff interval.")

    # A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.
    sequenceNumber = Int(desc="A sequential reference that defines the identity of this interval and its relative position with respect to other intervals in a sequence of intervals.")

    # The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.
    startValue = RealEnergy(desc="The lowest level of consumption that defines the starting point of this interval. The interval extends to the start of the next interval or until it is reset to the start of the first interval by TariffProfile.tariffCycle.")

    #--------------------------------------------------------------------------
    #  Begin "ConsumptionTariffInterval" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "sequenceNumber", "startValue",
                label="Attributes"),
            VGroup("Parent", "Charges", "TariffProfiles",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.ConsumptionTariffInterval",
        title="ConsumptionTariffInterval",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConsumptionTariffInterval" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Cashier" class:
#------------------------------------------------------------------------------

class Cashier(IdentifiedObject):
    """ The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ElectronicAddresses = List(Instance("CIM.IEC61968.Common.ElectronicAddress"))

    # All shifts operated by this cashier.
    CashierShifts = List(Instance("CIM.IEC61968.PaymentMetering.CashierShift"),
        desc="All shifts operated by this cashier.")

    # Vendor that manages this Cachier.
    Vendor = Instance("CIM.IEC61968.PaymentMetering.Vendor",
        desc="Vendor that manages this Cachier.",
        transient=True,
        opposite="Cashiers",
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

    #--------------------------------------------------------------------------
    #  Begin "Cashier" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ElectronicAddresses", "CashierShifts", "Vendor",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Cashier",
        title="Cashier",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Cashier" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Shift" class:
#------------------------------------------------------------------------------

class Shift(IdentifiedObject):
    """ Generally referring to a period of operation or work performed. Whether shift is open/closed can be derived from attributes 'activiryInterval.start' and 'activityInterval.end'. The grand total for receipts (i.e., cumulative total of all actual receipted amounts during this shift; bankable + non-bankable; excludes rounding error totals) can be derived from Receipt attributes: =sum(Receipt.receiptAmount) ; includes bankable and non-bankable receipts. Must also reconcile against: =sum(receiptsGrandTotalBankable + receiptsGrandTotalNonBankable). Must also reconcile against ReceiptSummary: =sum(ReceiptSummary.receiptsTotal). The attributes with 'GrandTotal' defined in this class may need to be used when the source data is periodically flushed from the system and then these cannot be derived.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All receipt summaries for this shift.
    ReceiptSummaries = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.ReceiptSummary"),
        desc="All receipt summaries for this shift.")

    # Interval for activity of this shift.
    activityInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval for activity of this shift.",
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

    # All transaction summaries recorded for this shift.
    TransactionSummaries = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.TransactionSummary"),
        desc="All transaction summaries recorded for this shift.")

    # Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding).
    transactionsGrandTotalRounding = Money(desc="Cumulative amount in error due to process rounding not reflected in transactionsGandTotal. Values are obtained from Transaction attributes: =sum(Transaction.transactionRounding).")

    # Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal).
    transactionsGrandTotal = Money(desc="Cumulative total of transacted amounts during this shift. Values are obtained from Transaction attributes: =sum(Transaction.transactionAmount). It must also reconcile against TransactionSummary: =sum(TransactionSummary.transactionsTotal).")

    # Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true.
    receiptsGrandTotalBankable = Money(desc="Total of amounts receipted during this shift that can be manually banked (cash and cheques for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = true.")

    # Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding).
    receiptsGrandTotalRounding = Money(desc="Cumulative amount in error due to process rounding not reflected in receiptsGrandTotal. Values are obtained from Receipt attributes: =sum(Receipt.receiptRounding).")

    # Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false.
    receiptsGrandTotalNonBankable = Money(desc="Total of amounts receipted during this shift that cannot be manually banked (card payments for example). Values are obtained from Receipt attributes: =sum(Receipt.receiptAmount) for all Receipt.bankable = false.")

    #--------------------------------------------------------------------------
    #  Begin "Shift" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "transactionsGrandTotalRounding", "transactionsGrandTotal", "receiptsGrandTotalBankable", "receiptsGrandTotalRounding", "receiptsGrandTotalNonBankable",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ReceiptSummaries", "activityInterval", "TransactionSummaries",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Shift",
        title="Shift",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Shift" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MerchantAgreement" class:
#------------------------------------------------------------------------------

class MerchantAgreement(Agreement):
    """ A formal controlling contractual agreement between Supplier and Merchant, in terms of which Merchant is authorised to vend tokens and receipt payments on behalf of Supplier. Merchant is accountable to Supplier for revenue collected at PointOfSale.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All merchant accounts instantiated as a result of this merchant agreement.
    MerchantAccounts = List(Instance("CIM.IEC61968.PaymentMetering.MerchantAccount"),
        desc="All merchant accounts instantiated as a result of this merchant agreement.")

    #--------------------------------------------------------------------------
    #  Begin "MerchantAgreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "MerchantAccounts",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.MerchantAgreement",
        title="MerchantAgreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MerchantAgreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Charge" class:
#------------------------------------------------------------------------------

class Charge(IdentifiedObject):
    """ A charge element associated with other entities such as tariff structures, auxiliary agreements or other charge elements. The total charge amount applicable to this instance of Charge is the sum of fixedPortion plus percentagePortion.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Tariff intervals to which this consumption-based charge must be levied.
    ConsumptionTariffIntervals = List(Instance("CIM.IEC61968.PaymentMetering.ConsumptionTariffInterval"),
        desc="Tariff intervals to which this consumption-based charge must be levied.")

    # All auxiliary accounts to which this charge must be levied.
    AuxiliaryAccounts = List(Instance("CIM.IEC61968.PaymentMetering.AuxiliaryAccount"),
        desc="All auxiliary accounts to which this charge must be levied.")

    # Tariff intervals to which this time-based charge must be levied.
    TimeTariffIntervals = List(Instance("CIM.IEC61968.PaymentMetering.TimeTariffInterval"),
        desc="Tariff intervals to which this time-based charge must be levied.")

    ParentCharge = Instance("CIM.IEC61968.PaymentMetering.Charge",
        transient=True,
        opposite="ChildCharges",
        editor=InstanceEditor(name="_charges"))

    def _get_charges(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Charge" ]
        else:
            return []

    _charges = Property(fget=_get_charges)

    # All sub-components of this complex charge.
    ChildCharges = List(Instance("CIM.IEC61968.PaymentMetering.Charge"),
        desc="All sub-components of this complex charge.")

    # The fixed portion of this charge element.
    fixedPortion = Instance("CIM.IEC61968.PaymentMetering.AccountingUnit",
        desc="The fixed portion of this charge element.",
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

    # The kind of charge to be applied.
    kind = ChargeKind(desc="The kind of charge to be applied.")

    # The variable portion of this charge element, calculated as a percentage of the total amount of a parent charge.
    variablePortion = PerCent(desc="The variable portion of this charge element, calculated as a percentage of the total amount of a parent charge.")

    #--------------------------------------------------------------------------
    #  Begin "Charge" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "variablePortion",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConsumptionTariffIntervals", "AuxiliaryAccounts", "TimeTariffIntervals", "ParentCharge", "ChildCharges", "fixedPortion",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Charge",
        title="Charge",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Charge" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ServiceSupplier" class:
#------------------------------------------------------------------------------

class ServiceSupplier(Organisation):
    """ Organisation that provides services to Customers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All service delivery points this service supplier utilises to deliver a service.
    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"),
        desc="All service delivery points this service supplier utilises to deliver a service.")

    # All customer agreements of this service supplier.
    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"),
        desc="All customer agreements of this service supplier.")

    # All BackAccounts this ServiceSupplier owns.
    BankAccounts = List(Instance("CIM.IEC61968.Informative.InfCommon.BankAccount"),
        desc="All BackAccounts this ServiceSupplier owns.")

    # Kind of supplier.
    kind = SupplierKind(desc="Kind of supplier.")

    # Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2.
    issuerIdentificationNumber = Str(desc="Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2.")

    #--------------------------------------------------------------------------
    #  Begin "ServiceSupplier" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "issuerIdentificationNumber",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "BusinessRoles", "TelephoneNumbers", "streetAddress", "MarketRoles", "postalAddress", "ElectronicAddresses", "ServiceDeliveryPoints", "CustomerAgreements", "BankAccounts",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.ServiceSupplier",
        title="ServiceSupplier",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServiceSupplier" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Receipt" class:
#------------------------------------------------------------------------------

class Receipt(IdentifiedObject):
    """ Record of total receipted payment from customer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All transactions recorded for this receipted payment.
    Transactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"),
        desc="All transactions recorded for this receipted payment.")

    # Cashier shift during which this receipt was recorded.
    CashierShift = Instance("CIM.IEC61968.PaymentMetering.CashierShift",
        desc="Cashier shift during which this receipt was recorded.",
        transient=True,
        opposite="Receipts",
        editor=InstanceEditor(name="_cashiershifts"))

    def _get_cashiershifts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.CashierShift" ]
        else:
            return []

    _cashiershifts = Property(fget=_get_cashiershifts)

    # Vendor shift during which this receipt was recorded.
    VendorShift = Instance("CIM.IEC61968.PaymentMetering.VendorShift",
        desc="Vendor shift during which this receipt was recorded.",
        transient=True,
        opposite="Receipts",
        editor=InstanceEditor(name="_vendorshifts"))

    def _get_vendorshifts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.VendorShift" ]
        else:
            return []

    _vendorshifts = Property(fget=_get_vendorshifts)

    # All payments received in the form of tenders recorded by this receipt.
    Tenders = List(Instance("CIM.IEC61968.PaymentMetering.Tender"),
        desc="All payments received in the form of tenders recorded by this receipt.")

    # Receipted amount with rounding, date and note.
    line = Instance("CIM.IEC61968.PaymentMetering.LineDetail",
        desc="Receipted amount with rounding, date and note.",
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

    # True if this receipted payment is manually bankable, otherwise it is an electronic funds transfer.
    isBankable = Bool(desc="True if this receipted payment is manually bankable, otherwise it is an electronic funds transfer.")

    #--------------------------------------------------------------------------
    #  Begin "Receipt" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "isBankable",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Transactions", "CashierShift", "VendorShift", "Tenders", "line",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Receipt",
        title="Receipt",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Receipt" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Tender" class:
#------------------------------------------------------------------------------

class Tender(IdentifiedObject):
    """ Tender is what is 'offered' by the customer towards making a payment and is often more than the required payment (hence the need for 'change'). The payment is thus that part of the Tender that goes towards settlement of a particular transaction. Tender is modelled as an aggregation of Cheque and Card. Both these tender types can exist in a single tender bid thus 'accountHolderName' must exist separately in each of Cheque and Card as each could have a different account holder name.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Cheque used to tender payment.
    Cheque = Instance("CIM.IEC61968.PaymentMetering.Cheque",
        desc="Cheque used to tender payment.",
        transient=True,
        opposite="Tender",
        editor=InstanceEditor(name="_cheques"))

    def _get_cheques(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Cheque" ]
        else:
            return []

    _cheques = Property(fget=_get_cheques)

    # Card used to tender payment.
    Card = Instance("CIM.IEC61968.PaymentMetering.Card",
        desc="Card used to tender payment.",
        transient=True,
        opposite="Tender",
        editor=InstanceEditor(name="_cards"))

    def _get_cards(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Card" ]
        else:
            return []

    _cards = Property(fget=_get_cards)

    # Receipt that recorded this receiving of a payment in the form of tenders.
    Receipt = Instance("CIM.IEC61968.PaymentMetering.Receipt",
        desc="Receipt that recorded this receiving of a payment in the form of tenders.",
        transient=True,
        opposite="Tenders",
        editor=InstanceEditor(name="_receipts"))

    def _get_receipts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Receipt" ]
        else:
            return []

    _receipts = Property(fget=_get_receipts)

    # Kind of tender from customer.
    kind = TenderKind(desc="Kind of tender from customer.")

    # Amount tendered by customer.
    amount = Money(desc="Amount tendered by customer.")

    # Difference between amount tendered by customer and the amount charged by point of sale.
    change = Money(desc="Difference between amount tendered by customer and the amount charged by point of sale.")

    #--------------------------------------------------------------------------
    #  Begin "Tender" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "amount", "change",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Cheque", "Card", "Receipt",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Tender",
        title="Tender",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Tender" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PointOfSale" class:
#------------------------------------------------------------------------------

class PointOfSale(IdentifiedObject):
    """ Logical point where transactions take place with operational interaction between Cashier and the payment system; in certain cases PointOfSale interacts directly with the end customer, in which case Cashier might not be a real person: for example a self-service kiosk or over the internet.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Vendor that controls this PointOfSale.
    Vendor = Instance("CIM.IEC61968.PaymentMetering.Vendor",
        desc="Vendor that controls this PointOfSale.",
        transient=True,
        opposite="PointOfSales",
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

    # All Tokens sold or dispensed at this PointOfSale.
    Tokens = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.Token"),
        desc="All Tokens sold or dispensed at this PointOfSale.")

    # All shifts this point of sale operated in.
    CashierShifts = List(Instance("CIM.IEC61968.PaymentMetering.CashierShift"),
        desc="All shifts this point of sale operated in.")

    # Local description for where this point of sale is physically located.
    location = Str(desc="Local description for where this point of sale is physically located.")

    #--------------------------------------------------------------------------
    #  Begin "PointOfSale" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "location",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Vendor", "Tokens", "CashierShifts",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.PointOfSale",
        title="PointOfSale",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PointOfSale" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Transaction" class:
#------------------------------------------------------------------------------

class Transaction(IdentifiedObject):
    """ The record of details of payment for service or token sale.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Vendor shift during which this transaction was recorded.
    VendorShift = Instance("CIM.IEC61968.PaymentMetering.VendorShift",
        desc="Vendor shift during which this transaction was recorded.",
        transient=True,
        opposite="Transactions",
        editor=InstanceEditor(name="_vendorshifts"))

    def _get_vendorshifts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.VendorShift" ]
        else:
            return []

    _vendorshifts = Property(fget=_get_vendorshifts)

    # The receipted payment for which this transaction has been recorded.
    Receipt = Instance("CIM.IEC61968.PaymentMetering.Receipt",
        desc="The receipted payment for which this transaction has been recorded.",
        transient=True,
        opposite="Transactions",
        editor=InstanceEditor(name="_receipts"))

    def _get_receipts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Receipt" ]
        else:
            return []

    _receipts = Property(fget=_get_receipts)

    # Customer account for this payment transaction.
    CustomerAccount = Instance("CIM.IEC61968.Customers.CustomerAccount",
        desc="Customer account for this payment transaction.",
        transient=True,
        opposite="PaymentTransactions",
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

    # Meter asset for this vending transaction.
    MeterAsset = Instance("CIM.IEC61968.Metering.MeterAsset",
        desc="Meter asset for this vending transaction.",
        transient=True,
        opposite="VendingTransactions",
        editor=InstanceEditor(name="_meterassets"))

    def _get_meterassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.MeterAsset" ]
        else:
            return []

    _meterassets = Property(fget=_get_meterassets)

    # All snapshots of meter parameters recorded at the time of this transaction. Use 'name' and 'value.value' attributes to specify name and value of a parameter from meter.
    UserAttributes = List(Instance("CIM.IEC61968.Common.UserAttribute"),
        desc="All snapshots of meter parameters recorded at the time of this transaction. Use 'name' and 'value.value' attributes to specify name and value of a parameter from meter.")

    # Auxiliary account for this payment transaction.
    AuxiliaryAccount = Instance("CIM.IEC61968.PaymentMetering.AuxiliaryAccount",
        desc="Auxiliary account for this payment transaction.",
        transient=True,
        opposite="PaymentTransactions",
        editor=InstanceEditor(name="_auxiliaryaccounts"))

    def _get_auxiliaryaccounts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.AuxiliaryAccount" ]
        else:
            return []

    _auxiliaryaccounts = Property(fget=_get_auxiliaryaccounts)

    # Pricing structure applicable for this transaction.
    PricingStructure = Instance("CIM.IEC61968.Customers.PricingStructure",
        desc="Pricing structure applicable for this transaction.",
        transient=True,
        opposite="Transactions",
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

    # Cashier shift during which this transaction was recorded.
    CashierShift = Instance("CIM.IEC61968.PaymentMetering.CashierShift",
        desc="Cashier shift during which this transaction was recorded.",
        transient=True,
        opposite="Transactions",
        editor=InstanceEditor(name="_cashiershifts"))

    def _get_cashiershifts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.CashierShift" ]
        else:
            return []

    _cashiershifts = Property(fget=_get_cashiershifts)

    # Transaction amount, rounding, date and note for this transaction line.
    line = Instance("CIM.IEC61968.PaymentMetering.LineDetail",
        desc="Transaction amount, rounding, date and note for this transaction line.",
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

    # Kind of transaction.
    kind = TransactionKind(desc="Kind of transaction.")

    # Actual amount of service units that is being paid for.
    serviceUnitsEnergy = RealEnergy(desc="Actual amount of service units that is being paid for.")

    # Number of service units not reflected in 'serviceUnitsEnergy' due to process rounding or truncating errors.
    serviceUnitsError = RealEnergy(desc="Number of service units not reflected in 'serviceUnitsEnergy' due to process rounding or truncating errors.")

    # (if 'kind' is transactionReversal) Reference to the original transaction that is being reversed by this transaction.
    reversedId = Str(desc="(if 'kind' is transactionReversal) Reference to the original transaction that is being reversed by this transaction.")

    # Reference to the entity that is the recipient of 'amount' (for example, supplier for service charge payment; or tax receiver for VAT).
    receiverReference = Str(desc="Reference to the entity that is the recipient of 'amount' (for example, supplier for service charge payment; or tax receiver for VAT).")

    # Formal reference for use with diverse payment (traffic fine for example).
    diverseReference = Str(desc="Formal reference for use with diverse payment (traffic fine for example).")

    # Reference to the entity that is the source of 'amount' (for example: customer for token purchase; or supplier for free issue token).
    donorReference = Str(desc="Reference to the entity that is the source of 'amount' (for example: customer for token purchase; or supplier for free issue token).")

    #--------------------------------------------------------------------------
    #  Begin "Transaction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "serviceUnitsEnergy", "serviceUnitsError", "reversedId", "receiverReference", "diverseReference", "donorReference",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "VendorShift", "Receipt", "CustomerAccount", "MeterAsset", "UserAttributes", "AuxiliaryAccount", "PricingStructure", "CashierShift", "line",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Transaction",
        title="Transaction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Transaction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Transactor" class:
#------------------------------------------------------------------------------

class Transactor(IdentifiedObject):
    """ The entity that ultimately executes the transaction and who is in control of the process; typically this is embodied in secure software running on a server that may employ secure hardware encryption devices for secure transaction processing.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All merchant accounts registered with this transactor.
    MerchantAccounts = List(Instance("CIM.IEC61968.PaymentMetering.MerchantAccount"),
        desc="All merchant accounts registered with this transactor.")

    #--------------------------------------------------------------------------
    #  Begin "Transactor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MerchantAccounts",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Transactor",
        title="Transactor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Transactor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AccountingUnit" class:
#------------------------------------------------------------------------------

class AccountingUnit(Element):
    """ Unit for accounting; use either 'energyUnit' or 'currencyUnit' to specify the unit for 'value'.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Unit of currency.
    monetaryUnit = Currency(desc="Unit of currency.")

    # Multiplier for the 'energyUnit' or 'monetaryUnit'.
    multiplier = UnitMultiplier(desc="Multiplier for the 'energyUnit' or 'monetaryUnit'.")

    # Unit of service.
    energyUnit = RealEnergy(desc="Unit of service.")

    # Value expressed in applicable units.
    value = Float(desc="Value expressed in applicable units.")

    #--------------------------------------------------------------------------
    #  Begin "AccountingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "monetaryUnit", "multiplier", "energyUnit", "value",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.AccountingUnit",
        title="AccountingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AccountingUnit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TariffProfile" class:
#------------------------------------------------------------------------------

class TariffProfile(Document):
    """ A schedule of charges; structure associated with Tariff that allows the definition of complex tarif structures such as step and time of use when used in conjunction with TimeTariffInterval and Charge. Inherited 'status.value' is defined in the context of the utility's business rules, for example: active, inactive, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All consumption tariff intervals used to define this tariff profile.
    ConsumptionTariffIntervals = List(Instance("CIM.IEC61968.PaymentMetering.ConsumptionTariffInterval"),
        desc="All consumption tariff intervals used to define this tariff profile.")

    # All tariffs defined by this tariff profile.
    Tariffs = List(Instance("CIM.IEC61968.Customers.Tariff"),
        desc="All tariffs defined by this tariff profile.")

    # All time tariff intervals used to define this tariff profile.
    TimeTariffIntervals = List(Instance("CIM.IEC61968.PaymentMetering.TimeTariffInterval"),
        desc="All time tariff intervals used to define this tariff profile.")

    # The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again.
    tariffCycle = Str(desc="The frequency at which the tariff charge schedule is repeated Examples are: once off on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc. At the end of each cycle, the business rules are reset to start from the beginning again.")

    #--------------------------------------------------------------------------
    #  Begin "TariffProfile" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "tariffCycle",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ConsumptionTariffIntervals", "Tariffs", "TimeTariffIntervals",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.TariffProfile",
        title="TariffProfile",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TariffProfile" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LineDetail" class:
#------------------------------------------------------------------------------

class LineDetail(Element):
    """ Details on an amount line, with rounding, date and note.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Amount for this line item.
    amount = Money(desc="Amount for this line item.")

    # Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'.
    rounding = Money(desc="Totalised monetary value of all errors due to process rounding or truncating that is not reflected in 'amount'.")

    # Free format note relevant to this line.
    note = Str(desc="Free format note relevant to this line.")

    # Date and time when this line was created in the application process.
    dateTime = Date(desc="Date and time when this line was created in the application process.")

    #--------------------------------------------------------------------------
    #  Begin "LineDetail" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "amount", "rounding", "note", "dateTime",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.LineDetail",
        title="LineDetail",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LineDetail" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AuxiliaryAgreement" class:
#------------------------------------------------------------------------------

class AuxiliaryAgreement(Agreement):
    """ An ad-hoc auxiliary account agreement associated with a customer agreement, not part of the customer's account, but typically subject to formal agreement between customer and supplier (utility). Typically this is used to collect revenue owing by the customer for other services or arrears accrued with the utility for other services. It is typically linked to a prepaid token purchase transaction, thus forcing the customer to make a payment towards settlement of the auxiliary account balance whenever he needs to purchase a prepaid token for electricity. The present status of AuxiliaryAgreement can be defined in the context of the utility's business rules, for example: enabled, disabled, pending, over recovered, under recovered, written off, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Customer agreement this (non-service related) auxiliary agreement refers to.
    CustomerAgreement = Instance("CIM.IEC61968.Customers.CustomerAgreement",
        desc="Customer agreement this (non-service related) auxiliary agreement refers to.",
        transient=True,
        opposite="AuxiliaryAgreements",
        editor=InstanceEditor(name="_customeragreements"))

    def _get_customeragreements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.CustomerAgreement" ]
        else:
            return []

    _customeragreements = Property(fget=_get_customeragreements)

    # All auxiliary accounts regulated by this agreement.
    AuxiliaryAccounts = List(Instance("CIM.IEC61968.PaymentMetering.AuxiliaryAccount"),
        desc="All auxiliary accounts regulated by this agreement.")

    # The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase.
    auxPriorityCode = Str(desc="The coded priority indicating the priority that this AuxiliaryAgreement has above other AuxiliaryAgreements (associated with the same customer agreement) when it comes to competing for settlement from a payment transaction or token purchase.")

    # The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
    fixedAmount = Money(desc="The fixed amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.")

    # The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.
    payCycle = Str(desc="The contractually expected payment frequency (by the customer). Examples are: ad-hoc; on specified date; hourly, daily, weekly, monthly. etc.")

    # The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
    vendPortion = PerCent(desc="The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are not in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.")

    # The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.
    vendPortionArrear = PerCent(desc="The percentage of the transaction amount that must be collected from each vending transaction towards settlement of this AuxiliaryAgreement when payments are in arrears. Note that there may be multiple tokens vended per vending transaction, but this is not relevant.")

    # The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance.
    minAmount = Money(desc="The minimum amount that must be paid at any transaction towards settling this AuxiliryAgreement or reducing the balance.")

    # The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.
    auxCycle = Str(desc="The frequency for automatically recurring auxiliary charges, where AuxiliaryAccount.initialCharge is recursively added to AuxiliaryAccount.dueCurrent at the start of each auxCycle. For example: on a specified date and time; hourly; daily; weekly; monthly; 3-monthly; 6-monthly; 12-monthly; etc.")

    # A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID.
    auxRef = Str(desc="A local reference to this AuxiliaryAgreement defined in the context of the implementation and not related to IdentifiedObject.mRID.")

    # Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'.
    subCategory = Str(desc="Sub-category of this AuxiliaryAgreement as sub-classification of the inherited 'category'.")

    # The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle.
    arrearsInterest = PerCent(desc="The interest per annum to be charged prorata on AuxiliaryAccount.dueArrears at the end of each payCycle.")

    #--------------------------------------------------------------------------
    #  Begin "AuxiliaryAgreement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "signDate", "auxPriorityCode", "fixedAmount", "payCycle", "vendPortion", "vendPortionArrear", "minAmount", "auxCycle", "auxRef", "subCategory", "arrearsInterest",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "validityInterval", "CustomerAgreement", "AuxiliaryAccounts",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.AuxiliaryAgreement",
        title="AuxiliaryAgreement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AuxiliaryAgreement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Card" class:
#------------------------------------------------------------------------------

class Card(Element):
    """ Documentation of the tender when it is a type of card (credit, debit, etc).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Payment tender this card is being used for.
    Tender = Instance("CIM.IEC61968.PaymentMetering.Tender",
        desc="Payment tender this card is being used for.",
        transient=True,
        opposite="Card",
        editor=InstanceEditor(name="_tenders"))

    def _get_tenders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Tender" ]
        else:
            return []

    _tenders = Property(fget=_get_tenders)

    # The primary account number.
    pan = Str(desc="The primary account number.")

    # The date when this card expires.
    expiryDate = AbsoluteDate(desc="The date when this card expires.")

    # Name of account holder.
    accountHolderName = Str(desc="Name of account holder.")

    # The card verification number.
    cvNumber = Str(desc="The card verification number.")

    #--------------------------------------------------------------------------
    #  Begin "Card" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pan", "expiryDate", "accountHolderName", "cvNumber",
                label="Attributes"),
            VGroup("Parent", "Tender",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Card",
        title="Card",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Card" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Vendor" class:
#------------------------------------------------------------------------------

class Vendor(IdentifiedObject):
    """ The entity that owns PointOfSale and contracts with Cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by Merchant who is a type of Organisation. Vendor is accountable to Merchant for revenue collected, who is in turn accountable to Supplier.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All points of sale this Vendor controls.
    PointOfSales = List(Instance("CIM.IEC61968.PaymentMetering.PointOfSale"),
        desc="All points of sale this Vendor controls.")

    # All BankStatements reflecting deposits made by this Vendor.
    BankStatements = List(Instance("CIM.IEC61968.Informative.InfPaymentMetering.BankStatement"),
        desc="All BankStatements reflecting deposits made by this Vendor.")

    # All Cachiers managed by this Vendor.
    Cashiers = List(Instance("CIM.IEC61968.PaymentMetering.Cashier"),
        desc="All Cachiers managed by this Vendor.")

    # Merchant account against which this vendor sells tokens or recept payments.
    MerchantAccount = Instance("CIM.IEC61968.PaymentMetering.MerchantAccount",
        desc="Merchant account against which this vendor sells tokens or recept payments.",
        transient=True,
        opposite="Vendors",
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

    # All vendor shifts opened and owned by this vendor.
    VendorShifts = List(Instance("CIM.IEC61968.PaymentMetering.VendorShift"),
        desc="All vendor shifts opened and owned by this vendor.")

    #--------------------------------------------------------------------------
    #  Begin "Vendor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PointOfSales", "BankStatements", "Cashiers", "MerchantAccount", "VendorShifts",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Vendor",
        title="Vendor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Vendor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Cheque" class:
#------------------------------------------------------------------------------

class Cheque(Element):
    """ The actual tender when it is a type of cheque.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Payment tender the cheque is being used for.
    Tender = Instance("CIM.IEC61968.PaymentMetering.Tender",
        desc="Payment tender the cheque is being used for.",
        transient=True,
        opposite="Cheque",
        editor=InstanceEditor(name="_tenders"))

    def _get_tenders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.Tender" ]
        else:
            return []

    _tenders = Property(fget=_get_tenders)

    # Details of the account holder and bank.
    bankAccountDetail = Instance("CIM.IEC61968.PaymentMetering.BankAccountDetail",
        desc="Details of the account holder and bank.",
        transient=True,
        editor=InstanceEditor(name="_bankaccountdetails"))

    def _get_bankaccountdetails(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.BankAccountDetail" ]
        else:
            return []

    _bankaccountdetails = Property(fget=_get_bankaccountdetails)

    # Kind of cheque.
    kind = ChequeKind(desc="Kind of cheque.")

    # The magnetic ink character recognition number printed on the cheque.
    micrNumber = Str(desc="The magnetic ink character recognition number printed on the cheque.")

    # Cheque reference number as printed on the cheque.
    chequeNumber = Str(desc="Cheque reference number as printed on the cheque.")

    # Date when cheque becomes valid.
    date = AbsoluteDate(desc="Date when cheque becomes valid.")

    #--------------------------------------------------------------------------
    #  Begin "Cheque" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "kind", "micrNumber", "chequeNumber", "date",
                label="Attributes"),
            VGroup("Parent", "Tender", "bankAccountDetail",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.Cheque",
        title="Cheque",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Cheque" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VendorShift" class:
#------------------------------------------------------------------------------

class VendorShift(Shift):
    """ The operating shift for a vendor during which he may transact against the merchant's account. It aggregates transactions and receipts during the shift and periodically debits a merchant account. The totals in VendorShift should always = sum of totals aggregated in all cashier shifts that were open under the particular vendor shift.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Transactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"))

    Receipts = List(Instance("CIM.IEC61968.PaymentMetering.Receipt"))

    # Merchant account this vendor shift periodically debits (based on aggregated transactions).
    MerchantAccount = Instance("CIM.IEC61968.PaymentMetering.MerchantAccount",
        desc="Merchant account this vendor shift periodically debits (based on aggregated transactions).",
        transient=True,
        opposite="VendorShifts",
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

    # Vendor that opens and owns this vendor shift.
    Vendor = Instance("CIM.IEC61968.PaymentMetering.Vendor",
        desc="Vendor that opens and owns this vendor shift.",
        transient=True,
        opposite="VendorShifts",
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

    # = true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes.
    posted = Bool(desc="= true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes.")

    # The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount).
    merchantDebitAmount = Money(desc="The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount).")

    #--------------------------------------------------------------------------
    #  Begin "VendorShift" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "transactionsGrandTotalRounding", "transactionsGrandTotal", "receiptsGrandTotalBankable", "receiptsGrandTotalRounding", "receiptsGrandTotalNonBankable", "posted", "merchantDebitAmount",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ReceiptSummaries", "activityInterval", "TransactionSummaries", "Transactions", "Receipts", "MerchantAccount", "Vendor",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.VendorShift",
        title="VendorShift",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VendorShift" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CashierShift" class:
#------------------------------------------------------------------------------

class CashierShift(Shift):
    """ The operating shift for a cashier, during which he may transact against the CashierShift, subject to VendorShift being open.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Cashier operating this shift.
    Cashier = Instance("CIM.IEC61968.PaymentMetering.Cashier",
        desc="Cashier operating this shift.",
        transient=True,
        opposite="CashierShifts",
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

    # All Receipts recorded for this Shift.
    Receipts = List(Instance("CIM.IEC61968.PaymentMetering.Receipt"),
        desc="All Receipts recorded for this Shift.")

    # Point of sale that is in operation during this shift.
    PointOfSale = Instance("CIM.IEC61968.PaymentMetering.PointOfSale",
        desc="Point of sale that is in operation during this shift.",
        transient=True,
        opposite="CashierShifts",
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

    Transactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"))

    # The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked.
    cashFloat = Money(desc="The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked.")

    #--------------------------------------------------------------------------
    #  Begin "CashierShift" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "transactionsGrandTotalRounding", "transactionsGrandTotal", "receiptsGrandTotalBankable", "receiptsGrandTotalRounding", "receiptsGrandTotalNonBankable", "cashFloat",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ReceiptSummaries", "activityInterval", "TransactionSummaries", "Cashier", "Receipts", "PointOfSale", "Transactions",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.PaymentMetering.CashierShift",
        title="CashierShift",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CashierShift" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
