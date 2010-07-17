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

""" The package is used to define detailed customer models.
"""

from cim.iec61968.common import Agreement
from cim.iec61968.common import Document
from cim.iec61970.core import Curve

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infcustomers"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfCustomers"

class ExternalCustomerAgreement(Agreement):
    """ A type of customer agreement involving an external agency. For example, a customer may form a contracts with an Energy Service Supplier if Direct Access is permitted.
    """
    pass
    # <<< external_customer_agreement
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ExternalCustomerAgreement' instance.
        """


        super(ExternalCustomerAgreement, self).__init__(**kw_args)
    # >>> external_customer_agreement


    def __str__(self):
        """ Returns a string representation of the ExternalCustomerAgreement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< external_customer_agreement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ExternalCustomerAgreement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ExternalCustomerAgreement", self.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ExternalCustomerAgreement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> external_customer_agreement.serialize


class StandardIndustryCode(Document):
    """ The Standard Industrial Classification (SIC) are the codes that identify the type of products/service an industry is involved in, and used for statutory reporting purposes. For example, in the USA these codes are located by the federal government, and then published in a book entitled 'The Standard Industrial Classification Manual'. The codes are arranged in a hierarchical structure. Note that Residential Service Agreements are not classified according to the SIC codes.
    """
    # <<< standard_industry_code
    # @generated
    def __init__(self, code='', customer_agreements=None, **kw_args):
        """ Initialises a new 'StandardIndustryCode' instance.
        """
        # Standard alphanumeric code assigned to a particular product/service within an industry. 
        self.code = code


        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []


        super(StandardIndustryCode, self).__init__(**kw_args)
    # >>> standard_industry_code

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ 
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for x in self._customer_agreements:
            x._standard_industry_code = None
        for y in value:
            y._standard_industry_code = self
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._standard_industry_code = self
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._standard_industry_code = None
            self._customer_agreements.remove(obj)
    # >>> customer_agreements


    def __str__(self):
        """ Returns a string representation of the StandardIndustryCode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< standard_industry_code.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StandardIndustryCode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StandardIndustryCode", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.customer_agreements:
            s += '%s<%s:StandardIndustryCode.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:StandardIndustryCode.code>%s</%s:StandardIndustryCode.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "StandardIndustryCode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> standard_industry_code.serialize


class CustomerBillingInfo(Document):
    """ The creation of the monthly customer billing statements is the method employed to notify Customers of charges, adjustments and credits applied to their account for Services and Products. The actuall billing occurs through an ErpInvoice. The CustomerBillingInfo includes information from the payment, collection, meter reading, installed meter, service, site, customer, customer account, customer agreement, services and pricing subject areas. Each component price shows up as a separate line item on the ErpInvoice. The Customer Billing Statement may include collection and account messages, marketing/civic event messages and bill inserts. One Customer Billing Statement is produced for all Agreements under a CustomerAccount per billing cycle date defined in 'CustomerAccount.billingCycle'. The history of CustomerBillingInfo, Invoices and Payments is to be maintained in associated ActivityRecords.
    """
    # <<< customer_billing_info
    # @generated
    def __init__(self, kind='separate_ess_udc', pymt_plan_type='', billing_date='', pymt_plan_amt=0.0, out_balance=0.0, last_payment_amt=0.0, last_payment_date='', due_date='', erp_invoice_line_items=None, customer_account=None, **kw_args):
        """ Initialises a new 'CustomerBillingInfo' instance.
        """
        # Kind of bill customer receives. Values are: "separate_ess_udc", "other", "consolidated_ess", "consolidated_udc"
        self.kind = 'separate_ess_udc'

        # Type of payment plan. 
        self.pymt_plan_type = pymt_plan_type

        # Business date designated for the billing run which produced this CustomerBillingInfo. 
        self.billing_date = billing_date

        # Monthly amortized amount due during each billing cycle for the CustomerAccount balance for which the Payment Plan is set-up. 
        self.pymt_plan_amt = pymt_plan_amt

        # Outstanding balance on the CustomerAccount as of the statement date. 
        self.out_balance = out_balance

        # Amount of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        self.last_payment_amt = last_payment_amt

        # Date of the last payment received from the customer. It is retained in the Customer Billing system, although the details of each payment are tracked in the ERP system. 
        self.last_payment_date = last_payment_date

        # Calculated date upon which a customer billing amount is due, used in the invoicing process to determine when a Customer's Payment is delinquent. It takes into consideration the regulatory criteria and the Customer's requested due date. In the absence of a Customer requested due date, the due date is typically calculated from the regulated number of days and the 'billingDate'. 
        self.due_date = due_date


        self._erp_invoice_line_items = []
        if erp_invoice_line_items is not None:
            self.erp_invoice_line_items = erp_invoice_line_items
        else:
            self.erp_invoice_line_items = []

        self._customer_account = None
        self.customer_account = customer_account


        super(CustomerBillingInfo, self).__init__(**kw_args)
    # >>> customer_billing_info

    # <<< erp_invoice_line_items
    # @generated
    def get_erp_invoice_line_items(self):
        """ 
        """
        return self._erp_invoice_line_items

    def set_erp_invoice_line_items(self, value):
        for p in self._erp_invoice_line_items:
            filtered = [q for q in p.customer_billing_infos if q != self]
            self._erp_invoice_line_items._customer_billing_infos = filtered
        for r in value:
            if self not in r._customer_billing_infos:
                r._customer_billing_infos.append(self)
        self._erp_invoice_line_items = value

    erp_invoice_line_items = property(get_erp_invoice_line_items, set_erp_invoice_line_items)

    def add_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self not in obj._customer_billing_infos:
                obj._customer_billing_infos.append(self)
            self._erp_invoice_line_items.append(obj)

    def remove_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self in obj._customer_billing_infos:
                obj._customer_billing_infos.remove(self)
            self._erp_invoice_line_items.remove(obj)
    # >>> erp_invoice_line_items

    # <<< customer_account
    # @generated
    def get_customer_account(self):
        """ 
        """
        return self._customer_account

    def set_customer_account(self, value):
        if self._customer_account is not None:
            filtered = [x for x in self.customer_account.customer_billing_infos if x != self]
            self._customer_account._customer_billing_infos = filtered

        self._customer_account = value
        if self._customer_account is not None:
            self._customer_account._customer_billing_infos.append(self)

    customer_account = property(get_customer_account, set_customer_account)
    # >>> customer_account


    def __str__(self):
        """ Returns a string representation of the CustomerBillingInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< customer_billing_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CustomerBillingInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CustomerBillingInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_invoice_line_items:
            s += '%s<%s:CustomerBillingInfo.erp_invoice_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.customer_account is not None:
            s += '%s<%s:CustomerBillingInfo.customer_account rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_account.uri)
        s += '%s<%s:CustomerBillingInfo.kind>%s</%s:CustomerBillingInfo.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.pymt_plan_type>%s</%s:CustomerBillingInfo.pymt_plan_type>' % \
            (indent, ns_prefix, self.pymt_plan_type, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.billing_date>%s</%s:CustomerBillingInfo.billing_date>' % \
            (indent, ns_prefix, self.billing_date, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.pymt_plan_amt>%s</%s:CustomerBillingInfo.pymt_plan_amt>' % \
            (indent, ns_prefix, self.pymt_plan_amt, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.out_balance>%s</%s:CustomerBillingInfo.out_balance>' % \
            (indent, ns_prefix, self.out_balance, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.last_payment_amt>%s</%s:CustomerBillingInfo.last_payment_amt>' % \
            (indent, ns_prefix, self.last_payment_amt, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.last_payment_date>%s</%s:CustomerBillingInfo.last_payment_date>' % \
            (indent, ns_prefix, self.last_payment_date, ns_prefix)
        s += '%s<%s:CustomerBillingInfo.due_date>%s</%s:CustomerBillingInfo.due_date>' % \
            (indent, ns_prefix, self.due_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CustomerBillingInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> customer_billing_info.serialize


class OutageHistory(Document):
    """ A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.
    """
    # <<< outage_history
    # @generated
    def __init__(self, outage_reports=None, **kw_args):
        """ Initialises a new 'OutageHistory' instance.
        """

        self._outage_reports = []
        if outage_reports is not None:
            self.outage_reports = outage_reports
        else:
            self.outage_reports = []


        super(OutageHistory, self).__init__(**kw_args)
    # >>> outage_history

    # <<< outage_reports
    # @generated
    def get_outage_reports(self):
        """ OutageReports per customer for which this OutageHistory is created.
        """
        return self._outage_reports

    def set_outage_reports(self, value):
        for x in self._outage_reports:
            x._outage_history = None
        for y in value:
            y._outage_history = self
        self._outage_reports = value

    outage_reports = property(get_outage_reports, set_outage_reports)

    def add_outage_reports(self, *outage_reports):
        for obj in outage_reports:
            obj._outage_history = self
            self._outage_reports.append(obj)

    def remove_outage_reports(self, *outage_reports):
        for obj in outage_reports:
            obj._outage_history = None
            self._outage_reports.remove(obj)
    # >>> outage_reports


    def __str__(self):
        """ Returns a string representation of the OutageHistory.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_history.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageHistory.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageHistory", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.outage_reports:
            s += '%s<%s:OutageHistory.outage_reports rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageHistory")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_history.serialize


class WorkBillingInfo(Document):
    """ Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.
    """
    # <<< work_billing_info
    # @generated
    def __init__(self, due_date_time='', received_date_time='', deposit=0.0, work_price=0.0, discount=0.0, cost_estimate=0.0, issue_date_time='', erp_line_items=None, customer_account=None, works=None, **kw_args):
        """ Initialises a new 'WorkBillingInfo' instance.
        """
        # Date and time by which payment for bill is expected from client. 
        self.due_date_time = due_date_time

        # Date payment was received from client. 
        self.received_date_time = received_date_time

        # Amount of price on deposit. 
        self.deposit = deposit

        # Amount of bill. 
        self.work_price = work_price

        # Discount from standard price. 
        self.discount = discount

        # Estimated cost for work. 
        self.cost_estimate = cost_estimate

        # Date and time bill was issued to client. 
        self.issue_date_time = issue_date_time


        self._erp_line_items = []
        if erp_line_items is not None:
            self.erp_line_items = erp_line_items
        else:
            self.erp_line_items = []

        self._customer_account = None
        self.customer_account = customer_account

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []


        super(WorkBillingInfo, self).__init__(**kw_args)
    # >>> work_billing_info

    # <<< erp_line_items
    # @generated
    def get_erp_line_items(self):
        """ 
        """
        return self._erp_line_items

    def set_erp_line_items(self, value):
        for p in self._erp_line_items:
            filtered = [q for q in p.work_billing_infos if q != self]
            self._erp_line_items._work_billing_infos = filtered
        for r in value:
            if self not in r._work_billing_infos:
                r._work_billing_infos.append(self)
        self._erp_line_items = value

    erp_line_items = property(get_erp_line_items, set_erp_line_items)

    def add_erp_line_items(self, *erp_line_items):
        for obj in erp_line_items:
            if self not in obj._work_billing_infos:
                obj._work_billing_infos.append(self)
            self._erp_line_items.append(obj)

    def remove_erp_line_items(self, *erp_line_items):
        for obj in erp_line_items:
            if self in obj._work_billing_infos:
                obj._work_billing_infos.remove(self)
            self._erp_line_items.remove(obj)
    # >>> erp_line_items

    # <<< customer_account
    # @generated
    def get_customer_account(self):
        """ 
        """
        return self._customer_account

    def set_customer_account(self, value):
        if self._customer_account is not None:
            filtered = [x for x in self.customer_account.work_billing_infos if x != self]
            self._customer_account._work_billing_infos = filtered

        self._customer_account = value
        if self._customer_account is not None:
            self._customer_account._work_billing_infos.append(self)

    customer_account = property(get_customer_account, set_customer_account)
    # >>> customer_account

    # <<< works
    # @generated
    def get_works(self):
        """ 
        """
        return self._works

    def set_works(self, value):
        for x in self._works:
            x._work_billing_info = None
        for y in value:
            y._work_billing_info = self
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            obj._work_billing_info = self
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            obj._work_billing_info = None
            self._works.remove(obj)
    # >>> works


    def __str__(self):
        """ Returns a string representation of the WorkBillingInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< work_billing_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WorkBillingInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WorkBillingInfo", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_line_items:
            s += '%s<%s:WorkBillingInfo.erp_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.customer_account is not None:
            s += '%s<%s:WorkBillingInfo.customer_account rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_account.uri)
        for obj in self.works:
            s += '%s<%s:WorkBillingInfo.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:WorkBillingInfo.due_date_time>%s</%s:WorkBillingInfo.due_date_time>' % \
            (indent, ns_prefix, self.due_date_time, ns_prefix)
        s += '%s<%s:WorkBillingInfo.received_date_time>%s</%s:WorkBillingInfo.received_date_time>' % \
            (indent, ns_prefix, self.received_date_time, ns_prefix)
        s += '%s<%s:WorkBillingInfo.deposit>%s</%s:WorkBillingInfo.deposit>' % \
            (indent, ns_prefix, self.deposit, ns_prefix)
        s += '%s<%s:WorkBillingInfo.work_price>%s</%s:WorkBillingInfo.work_price>' % \
            (indent, ns_prefix, self.work_price, ns_prefix)
        s += '%s<%s:WorkBillingInfo.discount>%s</%s:WorkBillingInfo.discount>' % \
            (indent, ns_prefix, self.discount, ns_prefix)
        s += '%s<%s:WorkBillingInfo.cost_estimate>%s</%s:WorkBillingInfo.cost_estimate>' % \
            (indent, ns_prefix, self.cost_estimate, ns_prefix)
        s += '%s<%s:WorkBillingInfo.issue_date_time>%s</%s:WorkBillingInfo.issue_date_time>' % \
            (indent, ns_prefix, self.issue_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "WorkBillingInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> work_billing_info.serialize


class PowerQualityPricing(Document):
    """ Pricing can be based on power quality.
    """
    # <<< power_quality_pricing
    # @generated
    def __init__(self, emergency_low_volt_limit=0.0, emergency_high_volt_limit=0.0, volt_limit_viol_cost=0.0, value_uninterrupted_service_p=0.0, normal_low_volt_limit=0.0, volt_imbalance_viol_cost=0.0, normal_high_volt_limit=0.0, power_factor_min=0.0, value_uninterrupted_service_energy=0.0, pricing_structure=None, service_delivery_points=None, **kw_args):
        """ Initialises a new 'PowerQualityPricing' instance.
        """
        # Emergency low voltage limit. 
        self.emergency_low_volt_limit = emergency_low_volt_limit

        # Emergency high voltage limit. 
        self.emergency_high_volt_limit = emergency_high_volt_limit

        # Voltage limit violation cost (Cost per unit Voltage). 
        self.volt_limit_viol_cost = volt_limit_viol_cost

        # Value of uninterrupted service (Cost per active power). 
        self.value_uninterrupted_service_p = value_uninterrupted_service_p

        # Normal low voltage limit. 
        self.normal_low_volt_limit = normal_low_volt_limit

        # Voltage imbalance violation cost (Cost per unit Voltage). 
        self.volt_imbalance_viol_cost = volt_imbalance_viol_cost

        # Normal high voltage limit. 
        self.normal_high_volt_limit = normal_high_volt_limit

        # Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here. 
        self.power_factor_min = power_factor_min

        # Value of uninterrupted service (Cost per energy). 
        self.value_uninterrupted_service_energy = value_uninterrupted_service_energy


        self._pricing_structure = None
        self.pricing_structure = pricing_structure

        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []


        super(PowerQualityPricing, self).__init__(**kw_args)
    # >>> power_quality_pricing

    # <<< pricing_structure
    # @generated
    def get_pricing_structure(self):
        """ 
        """
        return self._pricing_structure

    def set_pricing_structure(self, value):
        if self._pricing_structure is not None:
            filtered = [x for x in self.pricing_structure.power_quality_pricings if x != self]
            self._pricing_structure._power_quality_pricings = filtered

        self._pricing_structure = value
        if self._pricing_structure is not None:
            self._pricing_structure._power_quality_pricings.append(self)

    pricing_structure = property(get_pricing_structure, set_pricing_structure)
    # >>> pricing_structure

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ 
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for p in self._service_delivery_points:
            filtered = [q for q in p.power_quality_pricings if q != self]
            self._service_delivery_points._power_quality_pricings = filtered
        for r in value:
            if self not in r._power_quality_pricings:
                r._power_quality_pricings.append(self)
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self not in obj._power_quality_pricings:
                obj._power_quality_pricings.append(self)
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self in obj._power_quality_pricings:
                obj._power_quality_pricings.remove(self)
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points


    def __str__(self):
        """ Returns a string representation of the PowerQualityPricing.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_quality_pricing.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerQualityPricing.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerQualityPricing", self.uri)
        if format:
            indent += ' ' * depth

        if self.pricing_structure is not None:
            s += '%s<%s:PowerQualityPricing.pricing_structure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pricing_structure.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:PowerQualityPricing.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PowerQualityPricing.emergency_low_volt_limit>%s</%s:PowerQualityPricing.emergency_low_volt_limit>' % \
            (indent, ns_prefix, self.emergency_low_volt_limit, ns_prefix)
        s += '%s<%s:PowerQualityPricing.emergency_high_volt_limit>%s</%s:PowerQualityPricing.emergency_high_volt_limit>' % \
            (indent, ns_prefix, self.emergency_high_volt_limit, ns_prefix)
        s += '%s<%s:PowerQualityPricing.volt_limit_viol_cost>%s</%s:PowerQualityPricing.volt_limit_viol_cost>' % \
            (indent, ns_prefix, self.volt_limit_viol_cost, ns_prefix)
        s += '%s<%s:PowerQualityPricing.value_uninterrupted_service_p>%s</%s:PowerQualityPricing.value_uninterrupted_service_p>' % \
            (indent, ns_prefix, self.value_uninterrupted_service_p, ns_prefix)
        s += '%s<%s:PowerQualityPricing.normal_low_volt_limit>%s</%s:PowerQualityPricing.normal_low_volt_limit>' % \
            (indent, ns_prefix, self.normal_low_volt_limit, ns_prefix)
        s += '%s<%s:PowerQualityPricing.volt_imbalance_viol_cost>%s</%s:PowerQualityPricing.volt_imbalance_viol_cost>' % \
            (indent, ns_prefix, self.volt_imbalance_viol_cost, ns_prefix)
        s += '%s<%s:PowerQualityPricing.normal_high_volt_limit>%s</%s:PowerQualityPricing.normal_high_volt_limit>' % \
            (indent, ns_prefix, self.normal_high_volt_limit, ns_prefix)
        s += '%s<%s:PowerQualityPricing.power_factor_min>%s</%s:PowerQualityPricing.power_factor_min>' % \
            (indent, ns_prefix, self.power_factor_min, ns_prefix)
        s += '%s<%s:PowerQualityPricing.value_uninterrupted_service_energy>%s</%s:PowerQualityPricing.value_uninterrupted_service_energy>' % \
            (indent, ns_prefix, self.value_uninterrupted_service_energy, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerQualityPricing")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_quality_pricing.serialize


class ServiceGuarantee(Document):
    """ A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.
    """
    # <<< service_guarantee
    # @generated
    def __init__(self, automatic_pay=False, service_requirement='', pay_amount=0.0, application_period=None, **kw_args):
        """ Initialises a new 'ServiceGuarantee' instance.
        """
        # True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment. 
        self.automatic_pay = automatic_pay

        # Explanation of the requirement and conditions for satisfying it. 
        self.service_requirement = service_requirement

        # Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'. 
        self.pay_amount = pay_amount


        self.application_period = application_period


        super(ServiceGuarantee, self).__init__(**kw_args)
    # >>> service_guarantee

    # <<< application_period
    # @generated
    # Period in which this service guantee applies.
    application_period = None
    # >>> application_period


    def __str__(self):
        """ Returns a string representation of the ServiceGuarantee.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< service_guarantee.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ServiceGuarantee.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ServiceGuarantee", self.uri)
        if format:
            indent += ' ' * depth

        if self.application_period is not None:
            s += '%s<%s:ServiceGuarantee.application_period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.application_period.uri)
        s += '%s<%s:ServiceGuarantee.automatic_pay>%s</%s:ServiceGuarantee.automatic_pay>' % \
            (indent, ns_prefix, self.automatic_pay, ns_prefix)
        s += '%s<%s:ServiceGuarantee.service_requirement>%s</%s:ServiceGuarantee.service_requirement>' % \
            (indent, ns_prefix, self.service_requirement, ns_prefix)
        s += '%s<%s:ServiceGuarantee.pay_amount>%s</%s:ServiceGuarantee.pay_amount>' % \
            (indent, ns_prefix, self.pay_amount, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ServiceGuarantee")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> service_guarantee.serialize


class SubscribePowerCurve(Curve):
    """ Price curve for specifying the cost of energy (X) at points in time (y1) according to a prcing structure, which is based on a tariff.
    """
    # <<< subscribe_power_curve
    # @generated
    def __init__(self, pricing_structure=None, **kw_args):
        """ Initialises a new 'SubscribePowerCurve' instance.
        """

        self._pricing_structure = None
        self.pricing_structure = pricing_structure


        super(SubscribePowerCurve, self).__init__(**kw_args)
    # >>> subscribe_power_curve

    # <<< pricing_structure
    # @generated
    def get_pricing_structure(self):
        """ 
        """
        return self._pricing_structure

    def set_pricing_structure(self, value):
        if self._pricing_structure is not None:
            self._pricing_structure._subscribe_power_curve = None

        self._pricing_structure = value
        if self._pricing_structure is not None:
            self._pricing_structure._subscribe_power_curve = self

    pricing_structure = property(get_pricing_structure, set_pricing_structure)
    # >>> pricing_structure


    def __str__(self):
        """ Returns a string representation of the SubscribePowerCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< subscribe_power_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SubscribePowerCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SubscribePowerCurve", self.uri)
        if format:
            indent += ' ' * depth

        if self.pricing_structure is not None:
            s += '%s<%s:SubscribePowerCurve.pricing_structure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.pricing_structure.uri)
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
        for obj in self.curve_datas:
            s += '%s<%s:Curve.curve_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Curve.y3_multiplier>%s</%s:Curve.y3_multiplier>' % \
            (indent, ns_prefix, self.y3_multiplier, ns_prefix)
        s += '%s<%s:Curve.y2_multiplier>%s</%s:Curve.y2_multiplier>' % \
            (indent, ns_prefix, self.y2_multiplier, ns_prefix)
        s += '%s<%s:Curve.x_multiplier>%s</%s:Curve.x_multiplier>' % \
            (indent, ns_prefix, self.x_multiplier, ns_prefix)
        s += '%s<%s:Curve.y2_unit>%s</%s:Curve.y2_unit>' % \
            (indent, ns_prefix, self.y2_unit, ns_prefix)
        s += '%s<%s:Curve.curve_style>%s</%s:Curve.curve_style>' % \
            (indent, ns_prefix, self.curve_style, ns_prefix)
        s += '%s<%s:Curve.y1_unit>%s</%s:Curve.y1_unit>' % \
            (indent, ns_prefix, self.y1_unit, ns_prefix)
        s += '%s<%s:Curve.y1_multiplier>%s</%s:Curve.y1_multiplier>' % \
            (indent, ns_prefix, self.y1_multiplier, ns_prefix)
        s += '%s<%s:Curve.y3_unit>%s</%s:Curve.y3_unit>' % \
            (indent, ns_prefix, self.y3_unit, ns_prefix)
        s += '%s<%s:Curve.x_unit>%s</%s:Curve.x_unit>' % \
            (indent, ns_prefix, self.x_unit, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SubscribePowerCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> subscribe_power_curve.serialize


# <<< inf_customers
# @generated
# >>> inf_customers
