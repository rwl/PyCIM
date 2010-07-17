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


from cim import Element
from cim.iec61968.common import Document
from cim.iec61968.common import Agreement
from cim.iec61968.common import Organisation
from cim.iec61968.metering import DeviceFunction
from cim.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infpaymentmetering"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfPaymentMetering"

class ReceiptSummary(Element):
    """ Record of detail of receipts pertaining to one shift of operation (one record per 'tenderKind').
    """
    # <<< receipt_summary
    # @generated
    def __init__(self, tender_kind='cheque', shift=None, line=None, **kw_args):
        """ Initialises a new 'ReceiptSummary' instance.
        """
        # 'Tender.kind' for which 'receiptsTotal' is given. Values are: "cheque", "card", "other", "unspecified", "cash"
        self.tender_kind = 'cheque'


        self._shift = None
        self.shift = shift

        self.line = line


        super(ReceiptSummary, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the ReceiptSummary.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< receipt_summary.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReceiptSummary.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReceiptSummary", self.uri)
        if format:
            indent += ' ' * depth

        if self.shift is not None:
            s += '%s<%s:ReceiptSummary.shift rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shift.uri)
        if self.line is not None:
            s += '%s<%s:ReceiptSummary.line rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.line.uri)
        s += '%s<%s:ReceiptSummary.tender_kind>%s</%s:ReceiptSummary.tender_kind>' % \
            (indent, ns_prefix, self.tender_kind, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReceiptSummary")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> receipt_summary.serialize


class BankStatement(Document):
    """ A type of Document that records bank deposits made by Vendor of revenue collected at PointOfSale.
    """
    # <<< bank_statement
    # @generated
    def __init__(self, deposit_amount=0.0, posted=False, deposit_date_time='', merchant_credit_amount=0.0, vendor=None, merchant_account=None, bank_account=None, **kw_args):
        """ Initialises a new 'BankStatement' instance.
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


        super(BankStatement, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the BankStatement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bank_statement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BankStatement.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BankStatement", self.uri)
        if format:
            indent += ' ' * depth

        if self.vendor is not None:
            s += '%s<%s:BankStatement.vendor rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.vendor.uri)
        if self.merchant_account is not None:
            s += '%s<%s:BankStatement.merchant_account rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.merchant_account.uri)
        if self.bank_account is not None:
            s += '%s<%s:BankStatement.bank_account rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bank_account.uri)
        s += '%s<%s:BankStatement.deposit_amount>%s</%s:BankStatement.deposit_amount>' % \
            (indent, ns_prefix, self.deposit_amount, ns_prefix)
        s += '%s<%s:BankStatement.posted>%s</%s:BankStatement.posted>' % \
            (indent, ns_prefix, self.posted, ns_prefix)
        s += '%s<%s:BankStatement.deposit_date_time>%s</%s:BankStatement.deposit_date_time>' % \
            (indent, ns_prefix, self.deposit_date_time, ns_prefix)
        s += '%s<%s:BankStatement.merchant_credit_amount>%s</%s:BankStatement.merchant_credit_amount>' % \
            (indent, ns_prefix, self.merchant_credit_amount, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BankStatement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bank_statement.serialize


class TSPAgreement(Agreement):
    """ A contractual agreement between a supplier (utility) and a transaction service provider (a type of organisation) that governs the terms and conditions, under which authorisation the transaction service provider may process transactions on behalf of the supplier.
    """
    pass
    # <<< tspagreement
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'TSPAgreement' instance.
        """


        super(TSPAgreement, self).__init__(**kw_args)
    # >>> tspagreement


    def __str__(self):
        """ Returns a string representation of the TSPAgreement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tspagreement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TSPAgreement.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TSPAgreement", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.activity_records:
            s += '%s<%s:Document.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Document.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Document.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_document_roles:
            s += '%s<%s:Document.from_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Document.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Document.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:Document.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Document.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Document.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Document.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.doc_status is not None:
            s += '%s<%s:Document.doc_status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.doc_status.uri)
        for obj in self.schedule_parameter_infos:
            s += '%s<%s:Document.schedule_parameter_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.electronic_address is not None:
            s += '%s<%s:Document.electronic_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.electronic_address.uri)
        for obj in self.to_document_roles:
            s += '%s<%s:Document.to_document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Document.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Document.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:Document.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Document.subject>%s</%s:Document.subject>' % \
            (indent, ns_prefix, self.subject, ns_prefix)
        s += '%s<%s:Document.revision_number>%s</%s:Document.revision_number>' % \
            (indent, ns_prefix, self.revision_number, ns_prefix)
        s += '%s<%s:Document.category>%s</%s:Document.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Document.last_modified_date_time>%s</%s:Document.last_modified_date_time>' % \
            (indent, ns_prefix, self.last_modified_date_time, ns_prefix)
        s += '%s<%s:Document.title>%s</%s:Document.title>' % \
            (indent, ns_prefix, self.title, ns_prefix)
        s += '%s<%s:Document.created_date_time>%s</%s:Document.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
        if self.validity_interval is not None:
            s += '%s<%s:Agreement.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        s += '%s<%s:Agreement.sign_date>%s</%s:Agreement.sign_date>' % \
            (indent, ns_prefix, self.sign_date, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TSPAgreement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tspagreement.serialize


class TransactionSummary(Element):
    """ The record of detail of payment transactions pertaining to one shift of operation (one record per 'transactionKind').
    """
    # <<< transaction_summary
    # @generated
    def __init__(self, transaction_kind='auxiliary_charge_payment', shift=None, line=None, **kw_args):
        """ Initialises a new 'TransactionSummary' instance.
        """
        # 'Transaction.kind' for which 'transactionsTotal' is given. Values are: "auxiliary_charge_payment", "token_exchange", "token_cancellation", "transaction_reversal", "diverse_payment", "token_free_issue", "other", "meter_configuration_token", "token_sale_payment", "account_payment", "tax_charge_payment", "service_charge_payment", "token_grant"
        self.transaction_kind = 'auxiliary_charge_payment'


        self._shift = None
        self.shift = shift

        self.line = line


        super(TransactionSummary, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the TransactionSummary.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transaction_summary.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransactionSummary.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransactionSummary", self.uri)
        if format:
            indent += ' ' * depth

        if self.shift is not None:
            s += '%s<%s:TransactionSummary.shift rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shift.uri)
        if self.line is not None:
            s += '%s<%s:TransactionSummary.line rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.line.uri)
        s += '%s<%s:TransactionSummary.transaction_kind>%s</%s:TransactionSummary.transaction_kind>' % \
            (indent, ns_prefix, self.transaction_kind, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransactionSummary")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transaction_summary.serialize


class Bank(Organisation):
    """ Organisation that is a commercial bank, agency, or other institution that offers a similar service.
    """
    # <<< bank
    # @generated
    def __init__(self, iban='', branch_code='', bic='', bank_accounts=None, **kw_args):
        """ Initialises a new 'Bank' instance.
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


        super(Bank, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the Bank.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bank.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Bank.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Bank", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.bank_accounts:
            s += '%s<%s:Bank.bank_accounts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Bank.iban>%s</%s:Bank.iban>' % \
            (indent, ns_prefix, self.iban, ns_prefix)
        s += '%s<%s:Bank.branch_code>%s</%s:Bank.branch_code>' % \
            (indent, ns_prefix, self.branch_code, ns_prefix)
        s += '%s<%s:Bank.bic>%s</%s:Bank.bic>' % \
            (indent, ns_prefix, self.bic, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.business_roles:
            s += '%s<%s:Organisation.business_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Organisation.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.street_address is not None:
            s += '%s<%s:Organisation.street_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.street_address.uri)
        for obj in self.market_roles:
            s += '%s<%s:Organisation.market_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.postal_address is not None:
            s += '%s<%s:Organisation.postal_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.postal_address.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Organisation.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Bank")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bank.serialize


class SDPAccountingFunction(DeviceFunction):
    """ Service delivery point accounting function, particularly for payment meter.
    """
    # <<< sdpaccounting_function
    # @generated
    def __init__(self, charge_registers=None, available_credit=None, credit_expiry_level=None, credit_registers=None, service_kind=None, low_credit_warning_level=None, **kw_args):
        """ Initialises a new 'SDPAccountingFunction' instance.
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


        super(SDPAccountingFunction, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the SDPAccountingFunction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sdpaccounting_function.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SDPAccountingFunction.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SDPAccountingFunction", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.charge_registers:
            s += '%s<%s:SDPAccountingFunction.charge_registers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.available_credit is not None:
            s += '%s<%s:SDPAccountingFunction.available_credit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.available_credit.uri)
        if self.credit_expiry_level is not None:
            s += '%s<%s:SDPAccountingFunction.credit_expiry_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.credit_expiry_level.uri)
        for obj in self.credit_registers:
            s += '%s<%s:SDPAccountingFunction.credit_registers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.service_kind is not None:
            s += '%s<%s:SDPAccountingFunction.service_kind rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.service_kind.uri)
        if self.low_credit_warning_level is not None:
            s += '%s<%s:SDPAccountingFunction.low_credit_warning_level rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.low_credit_warning_level.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.measurements:
            s += '%s<%s:Asset.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Asset.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Asset.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Asset.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:Asset.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.mediums:
            s += '%s<%s:Asset.mediums rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_functions:
            s += '%s<%s:Asset.asset_functions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.properties:
            s += '%s<%s:Asset.properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.asset_container is not None:
            s += '%s<%s:Asset.asset_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_container.uri)
        for obj in self.ratings:
            s += '%s<%s:Asset.ratings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Asset.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.from_asset_roles:
            s += '%s<%s:Asset.from_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.location_roles:
            s += '%s<%s:Asset.location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resource_roles:
            s += '%s<%s:Asset.power_system_resource_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:Asset.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Asset.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_item_master is not None:
            s += '%s<%s:Asset.erp_item_master rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_item_master.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Asset.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_task is not None:
            s += '%s<%s:Asset.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        for obj in self.erp_rec_delivery_items:
            s += '%s<%s:Asset.erp_rec_delivery_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reliability_infos:
            s += '%s<%s:Asset.reliability_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.to_asset_roles:
            s += '%s<%s:Asset.to_asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_property_curves:
            s += '%s<%s:Asset.asset_property_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.financial_info is not None:
            s += '%s<%s:Asset.financial_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.financial_info.uri)
        if self.erp_inventory is not None:
            s += '%s<%s:Asset.erp_inventory rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_inventory.uri)
        if self.acceptance_test is not None:
            s += '%s<%s:Asset.acceptance_test rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.acceptance_test.uri)
        if self.status is not None:
            s += '%s<%s:Asset.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Asset.initial_condition>%s</%s:Asset.initial_condition>' % \
            (indent, ns_prefix, self.initial_condition, ns_prefix)
        s += '%s<%s:Asset.category>%s</%s:Asset.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Asset.lot_number>%s</%s:Asset.lot_number>' % \
            (indent, ns_prefix, self.lot_number, ns_prefix)
        s += '%s<%s:Asset.application>%s</%s:Asset.application>' % \
            (indent, ns_prefix, self.application, ns_prefix)
        s += '%s<%s:Asset.serial_number>%s</%s:Asset.serial_number>' % \
            (indent, ns_prefix, self.serial_number, ns_prefix)
        s += '%s<%s:Asset.installation_date>%s</%s:Asset.installation_date>' % \
            (indent, ns_prefix, self.installation_date, ns_prefix)
        s += '%s<%s:Asset.corporate_code>%s</%s:Asset.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Asset.purchase_price>%s</%s:Asset.purchase_price>' % \
            (indent, ns_prefix, self.purchase_price, ns_prefix)
        s += '%s<%s:Asset.manufactured_date>%s</%s:Asset.manufactured_date>' % \
            (indent, ns_prefix, self.manufactured_date, ns_prefix)
        s += '%s<%s:Asset.initial_loss_of_life>%s</%s:Asset.initial_loss_of_life>' % \
            (indent, ns_prefix, self.initial_loss_of_life, ns_prefix)
        s += '%s<%s:Asset.utc_number>%s</%s:Asset.utc_number>' % \
            (indent, ns_prefix, self.utc_number, ns_prefix)
        s += '%s<%s:Asset.critical>%s</%s:Asset.critical>' % \
            (indent, ns_prefix, self.critical, ns_prefix)
        if self.asset is not None:
            s += '%s<%s:AssetFunction.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.asset_function_asset_model is not None:
            s += '%s<%s:AssetFunction.asset_function_asset_model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset_function_asset_model.uri)
        s += '%s<%s:AssetFunction.hardware_id>%s</%s:AssetFunction.hardware_id>' % \
            (indent, ns_prefix, self.hardware_id, ns_prefix)
        s += '%s<%s:AssetFunction.config_id>%s</%s:AssetFunction.config_id>' % \
            (indent, ns_prefix, self.config_id, ns_prefix)
        s += '%s<%s:AssetFunction.program_id>%s</%s:AssetFunction.program_id>' % \
            (indent, ns_prefix, self.program_id, ns_prefix)
        s += '%s<%s:AssetFunction.password>%s</%s:AssetFunction.password>' % \
            (indent, ns_prefix, self.password, ns_prefix)
        s += '%s<%s:AssetFunction.firmware_id>%s</%s:AssetFunction.firmware_id>' % \
            (indent, ns_prefix, self.firmware_id, ns_prefix)
        if self.com_equipment_asset is not None:
            s += '%s<%s:DeviceFunction.com_equipment_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.com_equipment_asset.uri)
        if self.end_device_asset is not None:
            s += '%s<%s:DeviceFunction.end_device_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.end_device_asset.uri)
        for obj in self.registers:
            s += '%s<%s:DeviceFunction.registers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_events:
            s += '%s<%s:DeviceFunction.end_device_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:DeviceFunction.disabled>%s</%s:DeviceFunction.disabled>' % \
            (indent, ns_prefix, self.disabled, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SDPAccountingFunction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sdpaccounting_function.serialize


class CreditRegister(IdentifiedObject):
    """ Accumulated credits transacted per CreditKind for a given function. There could be several of these registers, one for each CreditKind; depending on the application.
    """
    # <<< credit_register
    # @generated
    def __init__(self, credit_kind='other', credit_amount=None, sdpaccounting_function=None, **kw_args):
        """ Initialises a new 'CreditRegister' instance.
        """
        # Several different types of credit are typically implemented in the case of a prepayment meter.  For example: credit transferred by means of a token carrier, or credit advanced automatically inside the meter under certain conditions, or credit held in reserved to be released under emergency conditions, or credit granted by local authority as a basic life support mechanism and may be dispensed automatically by the meter under certain conditions or credit available under severe climate conditions such as during winter over a weekend. Values are: "other", "reserve_credit", "lifeline_credit", "advance_credit", "token_credit", "grant_credit"
        self.credit_kind = 'other'


        self.credit_amount = credit_amount

        self._sdpaccounting_function = None
        self.sdpaccounting_function = sdpaccounting_function


        super(CreditRegister, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the CreditRegister.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< credit_register.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CreditRegister.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CreditRegister", self.uri)
        if format:
            indent += ' ' * depth

        if self.credit_amount is not None:
            s += '%s<%s:CreditRegister.credit_amount rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.credit_amount.uri)
        if self.sdpaccounting_function is not None:
            s += '%s<%s:CreditRegister.sdpaccounting_function rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sdpaccounting_function.uri)
        s += '%s<%s:CreditRegister.credit_kind>%s</%s:CreditRegister.credit_kind>' % \
            (indent, ns_prefix, self.credit_kind, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CreditRegister")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> credit_register.serialize


class Token(IdentifiedObject):
    """ The token that is transferred to the payment meter.
    """
    # <<< token
    # @generated
    def __init__(self, code='', comment='', point_of_sale=None, **kw_args):
        """ Initialises a new 'Token' instance.
        """
        # Coded representation of the token that is transferred to the payment meter. 
        self.code = code

        # Free-format note relevant to this token. 
        self.comment = comment


        self._point_of_sale = None
        self.point_of_sale = point_of_sale


        super(Token, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the Token.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< token.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Token.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Token", self.uri)
        if format:
            indent += ' ' * depth

        if self.point_of_sale is not None:
            s += '%s<%s:Token.point_of_sale rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.point_of_sale.uri)
        s += '%s<%s:Token.code>%s</%s:Token.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:Token.comment>%s</%s:Token.comment>' % \
            (indent, ns_prefix, self.comment, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Token")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> token.serialize


class ChargeRegister(IdentifiedObject):
    """ Accumulated charges transacted per ChargeKind for a given function. There could be several of these registers, one for each ChargeKind; depending on the application.
    """
    # <<< charge_register
    # @generated
    def __init__(self, charge_kind='other', charge_amount=None, spaccounting_function=None, **kw_args):
        """ Initialises a new 'ChargeRegister' instance.
        """
        # Several different types of charges are typically implemented in the case of a prepayment meter. For example: a charge according to a tariff for consumption and possibly a demand component, or a charge for a debt that is loaded in the meter to be recovered on a time basis, or a standing charge to be levied at the end of each billing period, or a tax charge loaded in the meter to be recovered on a consumption basis or a time basis. Values are: "other", "auxiliary_charge", "demand_charge", "tax_charge", "consumption_charge"
        self.charge_kind = 'other'


        self.charge_amount = charge_amount

        self._spaccounting_function = None
        self.spaccounting_function = spaccounting_function


        super(ChargeRegister, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the ChargeRegister.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< charge_register.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ChargeRegister.
        """
        s = ''
        indent = ' ' * depth if depth else ''
        if format:
            indent = '\n' + indent
        if header:
            s += '<?xml version="1.0" encoding="UTF-8"?>\n'
            s += '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:%s="%s">' % \
                (ns_prefix, ns_uri)
            if format:
                indent += ' ' * depth

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ChargeRegister", self.uri)
        if format:
            indent += ' ' * depth

        if self.charge_amount is not None:
            s += '%s<%s:ChargeRegister.charge_amount rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.charge_amount.uri)
        if self.spaccounting_function is not None:
            s += '%s<%s:ChargeRegister.spaccounting_function rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.spaccounting_function.uri)
        s += '%s<%s:ChargeRegister.charge_kind>%s</%s:ChargeRegister.charge_kind>' % \
            (indent, ns_prefix, self.charge_kind, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ChargeRegister")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> charge_register.serialize


# <<< inf_payment_metering
# @generated
# >>> inf_payment_metering
