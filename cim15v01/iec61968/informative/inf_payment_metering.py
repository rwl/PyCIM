# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from cim15v01 import Element
from cim15v01.iec61968.common import Document
from cim15v01.iec61968.common import Agreement
from cim15v01.iec61968.common import Organisation
from cim15v01.iec61968.metering import DeviceFunction
from cim15v01.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfPaymentMetering"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfPaymentMetering"

class ReceiptSummary(Element):
    """ Record of detail of receipts pertaining to one shift of operation (one record per 'tenderKind').
    """
    # <<< receipt_summary
    # @generated
    def __init__(self, tender_kind='cheque', shift=None, line=None, *args, **kw_args):
        """ Initialises a new 'ReceiptSummary' instance.

        @param tender_kind: 'Tender.kind' for which 'receiptsTotal' is given. Values are: "cheque", "card", "other", "unspecified", "cash"
        @param shift: Shift for which this summary is given.
        @param line: Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.
        """
        # 'Tender.kind' for which 'receiptsTotal' is given. Values are: "cheque", "card", "other", "unspecified", "cash"
        self.tender_kind = tender_kind


        self._shift = None
        self.shift = shift

        self.line = line


        super(ReceiptSummary, self).__init__(*args, **kw_args)
    # >>> receipt_summary

    # <<< shift
    # @generated
    def get_shift(self):
        """ Shift for which this summary is given.
        """
        return self._shift

    def set_shift(self, value):
        if self._shift is not None:
            filtered = [x for x in self.shift.receipt_summaries if x != self]
            self._shift._receipt_summaries = filtered

        self._shift = value
        if self._shift is not None:
            self._shift._receipt_summaries.append(self)

    shift = property(get_shift, set_shift)
    # >>> shift

    # <<< line
    # @generated
    # Totalised amount receipted during the shift for 'tenderKind', i.e., sum of ('Tender.amount' - 'Tender.change') per 'Tender.kind'.
    line = None
    # >>> line



class BankStatement(Document):
    """ A type of Document that records bank deposits made by Vendor of revenue collected at PointOfSale.
    """
    # <<< bank_statement
    # @generated
    def __init__(self, deposit_amount=0.0, posted=False, deposit_date_time='', merchant_credit_amount=0.0, vendor=None, merchant_account=None, bank_account=None, *args, **kw_args):
        """ Initialises a new 'BankStatement' instance.

        @param deposit_amount: The amount that is deposited into the bank via BankAccount. 
        @param posted: True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system. 
        @param deposit_date_time: The date and time the deposit is made. 
        @param merchant_credit_amount: The amount on this statement that is to be credited to MerchantAccount. 
        @param vendor: The Vendor that made this BankStatement (by making deposit).
        @param merchant_account:
        @param bank_account: BankAccount that generated this bank statement.
        """
        # The amount that is deposited into the bank via BankAccount. 
        self.deposit_amount = deposit_amount

        # True if mechantCreditAmount has been cerdited to MerchantAccount; typically happens when bank statement details are captured into payment system. 
        self.posted = posted

        # The date and time the deposit is made. 
        self.deposit_date_time = deposit_date_time

        # The amount on this statement that is to be credited to MerchantAccount. 
        self.merchant_credit_amount = merchant_credit_amount


        self._vendor = None
        self.vendor = vendor

        self._merchant_account = None
        self.merchant_account = merchant_account

        self._bank_account = None
        self.bank_account = bank_account


        super(BankStatement, self).__init__(*args, **kw_args)
    # >>> bank_statement

    # <<< vendor
    # @generated
    def get_vendor(self):
        """ The Vendor that made this BankStatement (by making deposit).
        """
        return self._vendor

    def set_vendor(self, value):
        if self._vendor is not None:
            filtered = [x for x in self.vendor.bank_statements if x != self]
            self._vendor._bank_statements = filtered

        self._vendor = value
        if self._vendor is not None:
            self._vendor._bank_statements.append(self)

    vendor = property(get_vendor, set_vendor)
    # >>> vendor

    # <<< merchant_account
    # @generated
    def get_merchant_account(self):
        """ 
        """
        return self._merchant_account

    def set_merchant_account(self, value):
        if self._merchant_account is not None:
            filtered = [x for x in self.merchant_account.bank_statements if x != self]
            self._merchant_account._bank_statements = filtered

        self._merchant_account = value
        if self._merchant_account is not None:
            self._merchant_account._bank_statements.append(self)

    merchant_account = property(get_merchant_account, set_merchant_account)
    # >>> merchant_account

    # <<< bank_account
    # @generated
    def get_bank_account(self):
        """ BankAccount that generated this bank statement.
        """
        return self._bank_account

    def set_bank_account(self, value):
        if self._bank_account is not None:
            filtered = [x for x in self.bank_account.bank_statements if x != self]
            self._bank_account._bank_statements = filtered

        self._bank_account = value
        if self._bank_account is not None:
            self._bank_account._bank_statements.append(self)

    bank_account = property(get_bank_account, set_bank_account)
    # >>> bank_account



class TSPAgreement(Agreement):
    """ A contractual agreement between a supplier (utility) and a transaction service provider (a type of organisation) that governs the terms and conditions, under which authorisation the transaction service provider may process transactions on behalf of the supplier.
    """
    pass
    # <<< tspagreement
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'TSPAgreement' instance.

        """


        super(TSPAgreement, self).__init__(*args, **kw_args)
    # >>> tspagreement



class TransactionSummary(Element):
    """ The record of detail of payment transactions pertaining to one shift of operation (one record per 'transactionKind').
    """
    # <<< transaction_summary
    # @generated
    def __init__(self, transaction_kind='auxiliary_charge_payment', shift=None, line=None, *args, **kw_args):
        """ Initialises a new 'TransactionSummary' instance.

        @param transaction_kind: 'Transaction.kind' for which 'transactionsTotal' is given. Values are: "auxiliary_charge_payment", "token_exchange", "token_cancellation", "transaction_reversal", "diverse_payment", "token_free_issue", "other", "meter_configuration_token", "token_sale_payment", "account_payment", "tax_charge_payment", "service_charge_payment", "token_grant"
        @param shift: Shift to which this summary applies.
        @param line: Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.
        """
        # 'Transaction.kind' for which 'transactionsTotal' is given. Values are: "auxiliary_charge_payment", "token_exchange", "token_cancellation", "transaction_reversal", "diverse_payment", "token_free_issue", "other", "meter_configuration_token", "token_sale_payment", "account_payment", "tax_charge_payment", "service_charge_payment", "token_grant"
        self.transaction_kind = transaction_kind


        self._shift = None
        self.shift = shift

        self.line = line


        super(TransactionSummary, self).__init__(*args, **kw_args)
    # >>> transaction_summary

    # <<< shift
    # @generated
    def get_shift(self):
        """ Shift to which this summary applies.
        """
        return self._shift

    def set_shift(self, value):
        if self._shift is not None:
            filtered = [x for x in self.shift.transaction_summaries if x != self]
            self._shift._transaction_summaries = filtered

        self._shift = value
        if self._shift is not None:
            self._shift._transaction_summaries.append(self)

    shift = property(get_shift, set_shift)
    # >>> shift

    # <<< line
    # @generated
    # Totalised amount transacted during the shift for this specific 'transactionKind', i.e., sum of 'Transaction.line.amount' per 'Transaction.kind'. Cumulative amount of rounding errors due to process rounding not reflected in 'LineDetail.amount' for 'transactionKind', i.e., sum of 'Transaction.line.rounding' per 'Transaction.kind'.
    line = None
    # >>> line



class Bank(Organisation):
    """ Organisation that is a commercial bank, agency, or other institution that offers a similar service.
    """
    # <<< bank
    # @generated
    def __init__(self, iban='', branch_code='', bic='', bank_accounts=None, *args, **kw_args):
        """ Initialises a new 'Bank' instance.

        @param iban: International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362). 
        @param branch_code: Codified reference to the particular branch of the bank where BankAccount is held. 
        @param bic: Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation. 
        @param bank_accounts: All BankAccounts this Bank provides.
        """
        # International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362). 
        self.iban = iban

        # Codified reference to the particular branch of the bank where BankAccount is held. 
        self.branch_code = branch_code

        # Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation. 
        self.bic = bic


        self._bank_accounts = []
        if bank_accounts is not None:
            self.bank_accounts = bank_accounts
        else:
            self.bank_accounts = []


        super(Bank, self).__init__(*args, **kw_args)
    # >>> bank

    # <<< bank_accounts
    # @generated
    def get_bank_accounts(self):
        """ All BankAccounts this Bank provides.
        """
        return self._bank_accounts

    def set_bank_accounts(self, value):
        for x in self._bank_accounts:
            x._bank = None
        for y in value:
            y._bank = self
        self._bank_accounts = value

    bank_accounts = property(get_bank_accounts, set_bank_accounts)

    def add_bank_accounts(self, *bank_accounts):
        for obj in bank_accounts:
            obj._bank = self
            self._bank_accounts.append(obj)

    def remove_bank_accounts(self, *bank_accounts):
        for obj in bank_accounts:
            obj._bank = None
            self._bank_accounts.remove(obj)
    # >>> bank_accounts



class SDPAccountingFunction(DeviceFunction):
    """ Service delivery point accounting function, particularly for payment meter.
    """
    # <<< sdpaccounting_function
    # @generated
    def __init__(self, charge_registers=None, available_credit=None, credit_expiry_level=None, credit_registers=None, service_kind=None, low_credit_warning_level=None, *args, **kw_args):
        """ Initialises a new 'SDPAccountingFunction' instance.

        @param charge_registers:
        @param available_credit: The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.
        @param credit_expiry_level: The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.
        @param credit_registers:
        @param service_kind:
        @param low_credit_warning_level: The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.
        """

        self._charge_registers = []
        if charge_registers is not None:
            self.charge_registers = charge_registers
        else:
            self.charge_registers = []

        self.available_credit = available_credit

        self.credit_expiry_level = credit_expiry_level

        self._credit_registers = []
        if credit_registers is not None:
            self.credit_registers = credit_registers
        else:
            self.credit_registers = []

        self._service_kind = None
        self.service_kind = service_kind

        self.low_credit_warning_level = low_credit_warning_level


        super(SDPAccountingFunction, self).__init__(*args, **kw_args)
    # >>> sdpaccounting_function

    # <<< charge_registers
    # @generated
    def get_charge_registers(self):
        """ 
        """
        return self._charge_registers

    def set_charge_registers(self, value):
        for x in self._charge_registers:
            x._spaccounting_function = None
        for y in value:
            y._spaccounting_function = self
        self._charge_registers = value

    charge_registers = property(get_charge_registers, set_charge_registers)

    def add_charge_registers(self, *charge_registers):
        for obj in charge_registers:
            obj._spaccounting_function = self
            self._charge_registers.append(obj)

    def remove_charge_registers(self, *charge_registers):
        for obj in charge_registers:
            obj._spaccounting_function = None
            self._charge_registers.remove(obj)
    # >>> charge_registers

    # <<< available_credit
    # @generated
    # The value is the balance of the sum of credits minus the sum of charges from the CreditRegisters and the ChargeRegisters. The sum might be complex function. The units are either in currency units or service units, depending on the value of accountingMode.
    available_credit = None
    # >>> available_credit

    # <<< credit_expiry_level
    # @generated
    # The value is a predefined set point for the level of the availableCredit to reach when the service will be interrupted. In the case of a prepayment meter the interruption is typically implemented by means of an electro-mechanical switch and the value is typically set = 0. The units are either in currency units or service units, depending on the value of accountingMode.
    credit_expiry_level = None
    # >>> credit_expiry_level

    # <<< credit_registers
    # @generated
    def get_credit_registers(self):
        """ 
        """
        return self._credit_registers

    def set_credit_registers(self, value):
        for x in self._credit_registers:
            x._sdpaccounting_function = None
        for y in value:
            y._sdpaccounting_function = self
        self._credit_registers = value

    credit_registers = property(get_credit_registers, set_credit_registers)

    def add_credit_registers(self, *credit_registers):
        for obj in credit_registers:
            obj._sdpaccounting_function = self
            self._credit_registers.append(obj)

    def remove_credit_registers(self, *credit_registers):
        for obj in credit_registers:
            obj._sdpaccounting_function = None
            self._credit_registers.remove(obj)
    # >>> credit_registers

    # <<< service_kind
    # @generated
    def get_service_kind(self):
        """ 
        """
        return self._service_kind

    def set_service_kind(self, value):
        if self._service_kind is not None:
            filtered = [x for x in self.service_kind.spaccounting_functions if x != self]
            self._service_kind._spaccounting_functions = filtered

        self._service_kind = value
        if self._service_kind is not None:
            self._service_kind._spaccounting_functions.append(self)

    service_kind = property(get_service_kind, set_service_kind)
    # >>> service_kind

    # <<< low_credit_warning_level
    # @generated
    # The value is a predefined set point for the level of the availableCredit to reach when a warning will be indicated to the customer. It serves to warn the customer that it is time to purchase more credit in the case of a prepayment meter implementation. The units are either in currency units or service units, depending on the value of accountingMode.
    low_credit_warning_level = None
    # >>> low_credit_warning_level



class CreditRegister(IdentifiedObject):
    """ Accumulated credits transacted per CreditKind for a given function. There could be several of these registers, one for each CreditKind; depending on the application.
    """
    # <<< credit_register
    # @generated
    def __init__(self, credit_kind='other', credit_amount=None, sdpaccounting_function=None, *args, **kw_args):
        """ Initialises a new 'CreditRegister' instance.

        @param credit_kind: Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend. Values are: "other", "reserve_credit", "lifeline_credit", "advance_credit", "token_credit", "grant_credit"
        @param credit_amount: Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
        @param sdpaccounting_function:
        """
        # Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend. Values are: "other", "reserve_credit", "lifeline_credit", "advance_credit", "token_credit", "grant_credit"
        self.credit_kind = credit_kind


        self.credit_amount = credit_amount

        self._sdpaccounting_function = None
        self.sdpaccounting_function = sdpaccounting_function


        super(CreditRegister, self).__init__(*args, **kw_args)
    # >>> credit_register

    # <<< credit_amount
    # @generated
    # Credit amount in favour of the customer. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    credit_amount = None
    # >>> credit_amount

    # <<< sdpaccounting_function
    # @generated
    def get_sdpaccounting_function(self):
        """ 
        """
        return self._sdpaccounting_function

    def set_sdpaccounting_function(self, value):
        if self._sdpaccounting_function is not None:
            filtered = [x for x in self.sdpaccounting_function.credit_registers if x != self]
            self._sdpaccounting_function._credit_registers = filtered

        self._sdpaccounting_function = value
        if self._sdpaccounting_function is not None:
            self._sdpaccounting_function._credit_registers.append(self)

    sdpaccounting_function = property(get_sdpaccounting_function, set_sdpaccounting_function)
    # >>> sdpaccounting_function



class Token(IdentifiedObject):
    """ The token that is transferred to the payment meter.
    """
    # <<< token
    # @generated
    def __init__(self, code='', comment='', point_of_sale=None, *args, **kw_args):
        """ Initialises a new 'Token' instance.

        @param code: Coded representation of the token that is transferred to the payment meter. 
        @param comment: Free-format note relevant to this token. 
        @param point_of_sale: PointOfSale tha sold or dispensed this Token.
        """
        # Coded representation of the token that is transferred to the payment meter. 
        self.code = code

        # Free-format note relevant to this token. 
        self.comment = comment


        self._point_of_sale = None
        self.point_of_sale = point_of_sale


        super(Token, self).__init__(*args, **kw_args)
    # >>> token

    # <<< point_of_sale
    # @generated
    def get_point_of_sale(self):
        """ PointOfSale tha sold or dispensed this Token.
        """
        return self._point_of_sale

    def set_point_of_sale(self, value):
        if self._point_of_sale is not None:
            filtered = [x for x in self.point_of_sale.tokens if x != self]
            self._point_of_sale._tokens = filtered

        self._point_of_sale = value
        if self._point_of_sale is not None:
            self._point_of_sale._tokens.append(self)

    point_of_sale = property(get_point_of_sale, set_point_of_sale)
    # >>> point_of_sale



class ChargeRegister(IdentifiedObject):
    """ Accumulated charges transacted per ChargeKind for a given function. There could be several of these registers, one for each ChargeKind; depending on the application.
    """
    # <<< charge_register
    # @generated
    def __init__(self, charge_kind='other', charge_amount=None, spaccounting_function=None, *args, **kw_args):
        """ Initialises a new 'ChargeRegister' instance.

        @param charge_kind: Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis. Values are: "other", "auxiliary_charge", "demand_charge", "tax_charge", "consumption_charge"
        @param charge_amount: Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
        @param spaccounting_function:
        """
        # Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis. Values are: "other", "auxiliary_charge", "demand_charge", "tax_charge", "consumption_charge"
        self.charge_kind = charge_kind


        self.charge_amount = charge_amount

        self._spaccounting_function = None
        self.spaccounting_function = spaccounting_function


        super(ChargeRegister, self).__init__(*args, **kw_args)
    # >>> charge_register

    # <<< charge_amount
    # @generated
    # Charge amount in favour of the supplier. The units are either in currency units or service units, depending on the value of 'AccountingUnit.accountingMode'.
    charge_amount = None
    # >>> charge_amount

    # <<< spaccounting_function
    # @generated
    def get_spaccounting_function(self):
        """ 
        """
        return self._spaccounting_function

    def set_spaccounting_function(self, value):
        if self._spaccounting_function is not None:
            filtered = [x for x in self.spaccounting_function.charge_registers if x != self]
            self._spaccounting_function._charge_registers = filtered

        self._spaccounting_function = value
        if self._spaccounting_function is not None:
            self._spaccounting_function._charge_registers.append(self)

    spaccounting_function = property(get_spaccounting_function, set_spaccounting_function)
    # >>> spaccounting_function



# <<< inf_payment_metering
# @generated
# >>> inf_payment_metering
