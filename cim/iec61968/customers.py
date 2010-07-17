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

""" This package contains the core information classes that support customer billing applications.
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Document
from cim.iec61968.common import Organisation
from cim.iec61968.common import Agreement
from cim.iec61968.common import Location

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.customers"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Customers"

class ServiceCategory(IdentifiedObject):
    """ Category of service provided to the customer.
    """
    # <<< service_category
    # @generated
    def __init__(self, kind='refuse', customer_agreements=None, service_delivery_points=None, spaccounting_functions=None, pricing_structures=None, **kw_args):
        """ Initialises a new 'ServiceCategory' instance.
        """
        # Kind of service. Values are: "refuse", "other", "tv_licence", "internet", "electricty", "water", "heat", "rates", "gas", "sewerage", "time"
        self.kind = 'refuse'


        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []

        self._spaccounting_functions = []
        if spaccounting_functions is not None:
            self.spaccounting_functions = spaccounting_functions
        else:
            self.spaccounting_functions = []

        self._pricing_structures = []
        if pricing_structures is not None:
            self.pricing_structures = pricing_structures
        else:
            self.pricing_structures = []


        super(ServiceCategory, self).__init__(**kw_args)
    # >>> service_category

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ 
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for x in self._customer_agreements:
            x._service_category = None
        for y in value:
            y._service_category = self
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._service_category = self
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._service_category = None
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ All service delivery points that deliver this category of service.
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for x in self._service_delivery_points:
            x._service_category = None
        for y in value:
            y._service_category = self
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            obj._service_category = self
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            obj._service_category = None
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points

    # <<< spaccounting_functions
    # @generated
    def get_spaccounting_functions(self):
        """ 
        """
        return self._spaccounting_functions

    def set_spaccounting_functions(self, value):
        for x in self._spaccounting_functions:
            x._service_kind = None
        for y in value:
            y._service_kind = self
        self._spaccounting_functions = value

    spaccounting_functions = property(get_spaccounting_functions, set_spaccounting_functions)

    def add_spaccounting_functions(self, *spaccounting_functions):
        for obj in spaccounting_functions:
            obj._service_kind = self
            self._spaccounting_functions.append(obj)

    def remove_spaccounting_functions(self, *spaccounting_functions):
        for obj in spaccounting_functions:
            obj._service_kind = None
            self._spaccounting_functions.remove(obj)
    # >>> spaccounting_functions

    # <<< pricing_structures
    # @generated
    def get_pricing_structures(self):
        """ All pricing structures applicable to this service category.
        """
        return self._pricing_structures

    def set_pricing_structures(self, value):
        for x in self._pricing_structures:
            x._service_category = None
        for y in value:
            y._service_category = self
        self._pricing_structures = value

    pricing_structures = property(get_pricing_structures, set_pricing_structures)

    def add_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            obj._service_category = self
            self._pricing_structures.append(obj)

    def remove_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            obj._service_category = None
            self._pricing_structures.remove(obj)
    # >>> pricing_structures


    def __str__(self):
        """ Returns a string representation of the ServiceCategory.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< service_category.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ServiceCategory.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ServiceCategory", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.customer_agreements:
            s += '%s<%s:ServiceCategory.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:ServiceCategory.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.spaccounting_functions:
            s += '%s<%s:ServiceCategory.spaccounting_functions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.pricing_structures:
            s += '%s<%s:ServiceCategory.pricing_structures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ServiceCategory.kind>%s</%s:ServiceCategory.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ServiceCategory")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> service_category.serialize


class CustomerAccount(Document):
    """ Assignment of a group of products and services purchased by the Customer through a CustomerAgreement, used as a mechanism for customer billing and payment. It contains common information from the various types of CustomerAgreements to create billings (invoices) for a Customer and receive payment.
    """
    # <<< customer_account
    # @generated
    def __init__(self, budget_bill='', billing_cycle='', work_billing_infos=None, payment_transactions=None, customer_agreements=None, customer_billing_infos=None, erp_invoicees=None, **kw_args):
        """ Initialises a new 'CustomerAccount' instance.
        """
        # Budget bill code. 
        self.budget_bill = budget_bill

        # Cycle day on which this customer account will normally be billed, used to determine when to produce the CustomerBillingInfo for this customer account. 
        self.billing_cycle = billing_cycle


        self._work_billing_infos = []
        if work_billing_infos is not None:
            self.work_billing_infos = work_billing_infos
        else:
            self.work_billing_infos = []

        self._payment_transactions = []
        if payment_transactions is not None:
            self.payment_transactions = payment_transactions
        else:
            self.payment_transactions = []

        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._customer_billing_infos = []
        if customer_billing_infos is not None:
            self.customer_billing_infos = customer_billing_infos
        else:
            self.customer_billing_infos = []

        self._erp_invoicees = []
        if erp_invoicees is not None:
            self.erp_invoicees = erp_invoicees
        else:
            self.erp_invoicees = []


        super(CustomerAccount, self).__init__(**kw_args)
    # >>> customer_account

    # <<< work_billing_infos
    # @generated
    def get_work_billing_infos(self):
        """ 
        """
        return self._work_billing_infos

    def set_work_billing_infos(self, value):
        for x in self._work_billing_infos:
            x._customer_account = None
        for y in value:
            y._customer_account = self
        self._work_billing_infos = value

    work_billing_infos = property(get_work_billing_infos, set_work_billing_infos)

    def add_work_billing_infos(self, *work_billing_infos):
        for obj in work_billing_infos:
            obj._customer_account = self
            self._work_billing_infos.append(obj)

    def remove_work_billing_infos(self, *work_billing_infos):
        for obj in work_billing_infos:
            obj._customer_account = None
            self._work_billing_infos.remove(obj)
    # >>> work_billing_infos

    # <<< payment_transactions
    # @generated
    def get_payment_transactions(self):
        """ All payment transactions for this customer account.
        """
        return self._payment_transactions

    def set_payment_transactions(self, value):
        for x in self._payment_transactions:
            x._customer_account = None
        for y in value:
            y._customer_account = self
        self._payment_transactions = value

    payment_transactions = property(get_payment_transactions, set_payment_transactions)

    def add_payment_transactions(self, *payment_transactions):
        for obj in payment_transactions:
            obj._customer_account = self
            self._payment_transactions.append(obj)

    def remove_payment_transactions(self, *payment_transactions):
        for obj in payment_transactions:
            obj._customer_account = None
            self._payment_transactions.remove(obj)
    # >>> payment_transactions

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ All agreements for this customer account.
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for x in self._customer_agreements:
            x._customer_account = None
        for y in value:
            y._customer_account = self
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._customer_account = self
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._customer_account = None
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

    # <<< customer_billing_infos
    # @generated
    def get_customer_billing_infos(self):
        """ 
        """
        return self._customer_billing_infos

    def set_customer_billing_infos(self, value):
        for x in self._customer_billing_infos:
            x._customer_account = None
        for y in value:
            y._customer_account = self
        self._customer_billing_infos = value

    customer_billing_infos = property(get_customer_billing_infos, set_customer_billing_infos)

    def add_customer_billing_infos(self, *customer_billing_infos):
        for obj in customer_billing_infos:
            obj._customer_account = self
            self._customer_billing_infos.append(obj)

    def remove_customer_billing_infos(self, *customer_billing_infos):
        for obj in customer_billing_infos:
            obj._customer_account = None
            self._customer_billing_infos.remove(obj)
    # >>> customer_billing_infos

    # <<< erp_invoicees
    # @generated
    def get_erp_invoicees(self):
        """ 
        """
        return self._erp_invoicees

    def set_erp_invoicees(self, value):
        for x in self._erp_invoicees:
            x._customer_account = None
        for y in value:
            y._customer_account = self
        self._erp_invoicees = value

    erp_invoicees = property(get_erp_invoicees, set_erp_invoicees)

    def add_erp_invoicees(self, *erp_invoicees):
        for obj in erp_invoicees:
            obj._customer_account = self
            self._erp_invoicees.append(obj)

    def remove_erp_invoicees(self, *erp_invoicees):
        for obj in erp_invoicees:
            obj._customer_account = None
            self._erp_invoicees.remove(obj)
    # >>> erp_invoicees


    def __str__(self):
        """ Returns a string representation of the CustomerAccount.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< customer_account.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CustomerAccount.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CustomerAccount", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.work_billing_infos:
            s += '%s<%s:CustomerAccount.work_billing_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.payment_transactions:
            s += '%s<%s:CustomerAccount.payment_transactions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:CustomerAccount.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_billing_infos:
            s += '%s<%s:CustomerAccount.customer_billing_infos rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_invoicees:
            s += '%s<%s:CustomerAccount.erp_invoicees rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:CustomerAccount.budget_bill>%s</%s:CustomerAccount.budget_bill>' % \
            (indent, ns_prefix, self.budget_bill, ns_prefix)
        s += '%s<%s:CustomerAccount.billing_cycle>%s</%s:CustomerAccount.billing_cycle>' % \
            (indent, ns_prefix, self.billing_cycle, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CustomerAccount")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> customer_account.serialize


class Tariff(Document):
    """ Document, approved by the responsible regulatory agency, listing the terms and conditions, including a schedule of prices, under which utility services will be provided. It has a unique number within the state or province. For Rate Schedules it is frequently allocated by the affiliated Public Utilities Commission.
    """
    # <<< tariff
    # @generated
    def __init__(self, start_date='', end_date='', pricing_structures=None, tariff_profiles=None, **kw_args):
        """ Initialises a new 'Tariff' instance.
        """
        # Date tariff was activated. 
        self.start_date = start_date

        # (if tariff became inactive) Date tariff was terminated. 
        self.end_date = end_date


        self._pricing_structures = []
        if pricing_structures is not None:
            self.pricing_structures = pricing_structures
        else:
            self.pricing_structures = []

        self._tariff_profiles = []
        if tariff_profiles is not None:
            self.tariff_profiles = tariff_profiles
        else:
            self.tariff_profiles = []


        super(Tariff, self).__init__(**kw_args)
    # >>> tariff

    # <<< pricing_structures
    # @generated
    def get_pricing_structures(self):
        """ All pricing structures using this tariff.
        """
        return self._pricing_structures

    def set_pricing_structures(self, value):
        for p in self._pricing_structures:
            filtered = [q for q in p.tariffs if q != self]
            self._pricing_structures._tariffs = filtered
        for r in value:
            if self not in r._tariffs:
                r._tariffs.append(self)
        self._pricing_structures = value

    pricing_structures = property(get_pricing_structures, set_pricing_structures)

    def add_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            if self not in obj._tariffs:
                obj._tariffs.append(self)
            self._pricing_structures.append(obj)

    def remove_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            if self in obj._tariffs:
                obj._tariffs.remove(self)
            self._pricing_structures.remove(obj)
    # >>> pricing_structures

    # <<< tariff_profiles
    # @generated
    def get_tariff_profiles(self):
        """ All tariff profiles using this tariff.
        """
        return self._tariff_profiles

    def set_tariff_profiles(self, value):
        for p in self._tariff_profiles:
            filtered = [q for q in p.tariffs if q != self]
            self._tariff_profiles._tariffs = filtered
        for r in value:
            if self not in r._tariffs:
                r._tariffs.append(self)
        self._tariff_profiles = value

    tariff_profiles = property(get_tariff_profiles, set_tariff_profiles)

    def add_tariff_profiles(self, *tariff_profiles):
        for obj in tariff_profiles:
            if self not in obj._tariffs:
                obj._tariffs.append(self)
            self._tariff_profiles.append(obj)

    def remove_tariff_profiles(self, *tariff_profiles):
        for obj in tariff_profiles:
            if self in obj._tariffs:
                obj._tariffs.remove(self)
            self._tariff_profiles.remove(obj)
    # >>> tariff_profiles


    def __str__(self):
        """ Returns a string representation of the Tariff.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tariff.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Tariff.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Tariff", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.pricing_structures:
            s += '%s<%s:Tariff.pricing_structures rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.tariff_profiles:
            s += '%s<%s:Tariff.tariff_profiles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Tariff.start_date>%s</%s:Tariff.start_date>' % \
            (indent, ns_prefix, self.start_date, ns_prefix)
        s += '%s<%s:Tariff.end_date>%s</%s:Tariff.end_date>' % \
            (indent, ns_prefix, self.end_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Tariff")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tariff.serialize


class PricingStructure(Document):
    """ Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.
    """
    # <<< pricing_structure
    # @generated
    def __init__(self, revenue_kind='street_light', code='', daily_floor_usage=0, tax_exemption=False, daily_ceiling_usage=0, daily_estimated_usage=0, tariffs=None, power_quality_pricings=None, transactions=None, service_delivery_points=None, customer_agreements=None, subscribe_power_curve=None, service_category=None, **kw_args):
        """ Initialises a new 'PricingStructure' instance.
        """
        # (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes). Values are: "street_light", "commercial", "other", "irrigation", "non_residential", "industrial", "residential"
        self.revenue_kind = 'street_light'

        # Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code. 
        self.code = code

        # Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage. 
        self.daily_floor_usage = daily_floor_usage

        # True if this pricing structure is not taxable. 
        self.tax_exemption = tax_exemption

        # Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage. 
        self.daily_ceiling_usage = daily_ceiling_usage

        # Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting. 
        self.daily_estimated_usage = daily_estimated_usage


        self._tariffs = []
        if tariffs is not None:
            self.tariffs = tariffs
        else:
            self.tariffs = []

        self._power_quality_pricings = []
        if power_quality_pricings is not None:
            self.power_quality_pricings = power_quality_pricings
        else:
            self.power_quality_pricings = []

        self._transactions = []
        if transactions is not None:
            self.transactions = transactions
        else:
            self.transactions = []

        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []

        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._subscribe_power_curve = None
        self.subscribe_power_curve = subscribe_power_curve

        self._service_category = None
        self.service_category = service_category


        super(PricingStructure, self).__init__(**kw_args)
    # >>> pricing_structure

    # <<< tariffs
    # @generated
    def get_tariffs(self):
        """ All tariffs used by this pricing structure.
        """
        return self._tariffs

    def set_tariffs(self, value):
        for p in self._tariffs:
            filtered = [q for q in p.pricing_structures if q != self]
            self._tariffs._pricing_structures = filtered
        for r in value:
            if self not in r._pricing_structures:
                r._pricing_structures.append(self)
        self._tariffs = value

    tariffs = property(get_tariffs, set_tariffs)

    def add_tariffs(self, *tariffs):
        for obj in tariffs:
            if self not in obj._pricing_structures:
                obj._pricing_structures.append(self)
            self._tariffs.append(obj)

    def remove_tariffs(self, *tariffs):
        for obj in tariffs:
            if self in obj._pricing_structures:
                obj._pricing_structures.remove(self)
            self._tariffs.remove(obj)
    # >>> tariffs

    # <<< power_quality_pricings
    # @generated
    def get_power_quality_pricings(self):
        """ 
        """
        return self._power_quality_pricings

    def set_power_quality_pricings(self, value):
        for x in self._power_quality_pricings:
            x._pricing_structure = None
        for y in value:
            y._pricing_structure = self
        self._power_quality_pricings = value

    power_quality_pricings = property(get_power_quality_pricings, set_power_quality_pricings)

    def add_power_quality_pricings(self, *power_quality_pricings):
        for obj in power_quality_pricings:
            obj._pricing_structure = self
            self._power_quality_pricings.append(obj)

    def remove_power_quality_pricings(self, *power_quality_pricings):
        for obj in power_quality_pricings:
            obj._pricing_structure = None
            self._power_quality_pricings.remove(obj)
    # >>> power_quality_pricings

    # <<< transactions
    # @generated
    def get_transactions(self):
        """ All transactions applying this pricing structure.
        """
        return self._transactions

    def set_transactions(self, value):
        for x in self._transactions:
            x._pricing_structure = None
        for y in value:
            y._pricing_structure = self
        self._transactions = value

    transactions = property(get_transactions, set_transactions)

    def add_transactions(self, *transactions):
        for obj in transactions:
            obj._pricing_structure = self
            self._transactions.append(obj)

    def remove_transactions(self, *transactions):
        for obj in transactions:
            obj._pricing_structure = None
            self._transactions.remove(obj)
    # >>> transactions

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for p in self._service_delivery_points:
            filtered = [q for q in p.pricing_structures if q != self]
            self._service_delivery_points._pricing_structures = filtered
        for r in value:
            if self not in r._pricing_structures:
                r._pricing_structures.append(self)
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self not in obj._pricing_structures:
                obj._pricing_structures.append(self)
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self in obj._pricing_structures:
                obj._pricing_structures.remove(self)
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ All customer agreements with this pricing structure.
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for p in self._customer_agreements:
            filtered = [q for q in p.pricing_structures if q != self]
            self._customer_agreements._pricing_structures = filtered
        for r in value:
            if self not in r._pricing_structures:
                r._pricing_structures.append(self)
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            if self not in obj._pricing_structures:
                obj._pricing_structures.append(self)
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            if self in obj._pricing_structures:
                obj._pricing_structures.remove(self)
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

    # <<< subscribe_power_curve
    # @generated
    def get_subscribe_power_curve(self):
        """ SubscribePowerCurve specifies the cost according to a prcing structure.
        """
        return self._subscribe_power_curve

    def set_subscribe_power_curve(self, value):
        if self._subscribe_power_curve is not None:
            self._subscribe_power_curve._pricing_structure = None

        self._subscribe_power_curve = value
        if self._subscribe_power_curve is not None:
            self._subscribe_power_curve._pricing_structure = self

    subscribe_power_curve = property(get_subscribe_power_curve, set_subscribe_power_curve)
    # >>> subscribe_power_curve

    # <<< service_category
    # @generated
    def get_service_category(self):
        """ Service category to which this pricing structure applies.
        """
        return self._service_category

    def set_service_category(self, value):
        if self._service_category is not None:
            filtered = [x for x in self.service_category.pricing_structures if x != self]
            self._service_category._pricing_structures = filtered

        self._service_category = value
        if self._service_category is not None:
            self._service_category._pricing_structures.append(self)

    service_category = property(get_service_category, set_service_category)
    # >>> service_category


    def __str__(self):
        """ Returns a string representation of the PricingStructure.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pricing_structure.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PricingStructure.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PricingStructure", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.tariffs:
            s += '%s<%s:PricingStructure.tariffs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_quality_pricings:
            s += '%s<%s:PricingStructure.power_quality_pricings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.transactions:
            s += '%s<%s:PricingStructure.transactions rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:PricingStructure.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:PricingStructure.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.subscribe_power_curve is not None:
            s += '%s<%s:PricingStructure.subscribe_power_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.subscribe_power_curve.uri)
        if self.service_category is not None:
            s += '%s<%s:PricingStructure.service_category rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.service_category.uri)
        s += '%s<%s:PricingStructure.revenue_kind>%s</%s:PricingStructure.revenue_kind>' % \
            (indent, ns_prefix, self.revenue_kind, ns_prefix)
        s += '%s<%s:PricingStructure.code>%s</%s:PricingStructure.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:PricingStructure.daily_floor_usage>%s</%s:PricingStructure.daily_floor_usage>' % \
            (indent, ns_prefix, self.daily_floor_usage, ns_prefix)
        s += '%s<%s:PricingStructure.tax_exemption>%s</%s:PricingStructure.tax_exemption>' % \
            (indent, ns_prefix, self.tax_exemption, ns_prefix)
        s += '%s<%s:PricingStructure.daily_ceiling_usage>%s</%s:PricingStructure.daily_ceiling_usage>' % \
            (indent, ns_prefix, self.daily_ceiling_usage, ns_prefix)
        s += '%s<%s:PricingStructure.daily_estimated_usage>%s</%s:PricingStructure.daily_estimated_usage>' % \
            (indent, ns_prefix, self.daily_estimated_usage, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PricingStructure")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pricing_structure.serialize


class Customer(Organisation):
    """ Organisation receiving services from ServiceSupplier.
    """
    # <<< customer
    # @generated
    def __init__(self, kind='wind_machine', puc_number='', special_need='', vip=False, trouble_tickets=None, works=None, outage_notifications=None, erp_persons=None, end_device_assets=None, customer_agreements=None, planned_outage=None, status=None, **kw_args):
        """ Initialises a new 'Customer' instance.
        """
        # Kind of customer. Values are: "wind_machine", "residential_farm_service", "residential", "energy_service_supplier", "residential_streetlight_others", "other", "pumping_load", "commercial_industrial", "residential_and_streetlight", "residential_and_commercial", "energy_service_scheduler", "internal_use"
        self.kind = 'wind_machine'

        # (if applicable) Public Utility Commission identification number. 
        self.puc_number = puc_number

        # True if customer organisation has special service needs such as life support, hospitals, etc. 
        self.special_need = special_need

        # True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute. 
        self.vip = vip


        self._trouble_tickets = []
        if trouble_tickets is not None:
            self.trouble_tickets = trouble_tickets
        else:
            self.trouble_tickets = []

        self._works = []
        if works is not None:
            self.works = works
        else:
            self.works = []

        self._outage_notifications = []
        if outage_notifications is not None:
            self.outage_notifications = outage_notifications
        else:
            self.outage_notifications = []

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self._end_device_assets = []
        if end_device_assets is not None:
            self.end_device_assets = end_device_assets
        else:
            self.end_device_assets = []

        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._planned_outage = None
        self.planned_outage = planned_outage

        self.status = status


        super(Customer, self).__init__(**kw_args)
    # >>> customer

    # <<< trouble_tickets
    # @generated
    def get_trouble_tickets(self):
        """ 
        """
        return self._trouble_tickets

    def set_trouble_tickets(self, value):
        for x in self._trouble_tickets:
            x._customer_data = None
        for y in value:
            y._customer_data = self
        self._trouble_tickets = value

    trouble_tickets = property(get_trouble_tickets, set_trouble_tickets)

    def add_trouble_tickets(self, *trouble_tickets):
        for obj in trouble_tickets:
            obj._customer_data = self
            self._trouble_tickets.append(obj)

    def remove_trouble_tickets(self, *trouble_tickets):
        for obj in trouble_tickets:
            obj._customer_data = None
            self._trouble_tickets.remove(obj)
    # >>> trouble_tickets

    # <<< works
    # @generated
    def get_works(self):
        """ All the works performed for this customer.
        """
        return self._works

    def set_works(self, value):
        for p in self._works:
            filtered = [q for q in p.customers if q != self]
            self._works._customers = filtered
        for r in value:
            if self not in r._customers:
                r._customers.append(self)
        self._works = value

    works = property(get_works, set_works)

    def add_works(self, *works):
        for obj in works:
            if self not in obj._customers:
                obj._customers.append(self)
            self._works.append(obj)

    def remove_works(self, *works):
        for obj in works:
            if self in obj._customers:
                obj._customers.remove(self)
            self._works.remove(obj)
    # >>> works

    # <<< outage_notifications
    # @generated
    def get_outage_notifications(self):
        """ 
        """
        return self._outage_notifications

    def set_outage_notifications(self, value):
        for p in self._outage_notifications:
            filtered = [q for q in p.customer_datas if q != self]
            self._outage_notifications._customer_datas = filtered
        for r in value:
            if self not in r._customer_datas:
                r._customer_datas.append(self)
        self._outage_notifications = value

    outage_notifications = property(get_outage_notifications, set_outage_notifications)

    def add_outage_notifications(self, *outage_notifications):
        for obj in outage_notifications:
            if self not in obj._customer_datas:
                obj._customer_datas.append(self)
            self._outage_notifications.append(obj)

    def remove_outage_notifications(self, *outage_notifications):
        for obj in outage_notifications:
            if self in obj._customer_datas:
                obj._customer_datas.remove(self)
            self._outage_notifications.remove(obj)
    # >>> outage_notifications

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for x in self._erp_persons:
            x._customer_data = None
        for y in value:
            y._customer_data = self
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            obj._customer_data = self
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            obj._customer_data = None
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< end_device_assets
    # @generated
    def get_end_device_assets(self):
        """ All end device assets of this customer.
        """
        return self._end_device_assets

    def set_end_device_assets(self, value):
        for x in self._end_device_assets:
            x._customer = None
        for y in value:
            y._customer = self
        self._end_device_assets = value

    end_device_assets = property(get_end_device_assets, set_end_device_assets)

    def add_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._customer = self
            self._end_device_assets.append(obj)

    def remove_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._customer = None
            self._end_device_assets.remove(obj)
    # >>> end_device_assets

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ All agreements of this customer.
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for x in self._customer_agreements:
            x._customer = None
        for y in value:
            y._customer = self
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._customer = self
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._customer = None
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

    # <<< planned_outage
    # @generated
    def get_planned_outage(self):
        """ 
        """
        return self._planned_outage

    def set_planned_outage(self, value):
        if self._planned_outage is not None:
            filtered = [x for x in self.planned_outage.customer_datas if x != self]
            self._planned_outage._customer_datas = filtered

        self._planned_outage = value
        if self._planned_outage is not None:
            self._planned_outage._customer_datas.append(self)

    planned_outage = property(get_planned_outage, set_planned_outage)
    # >>> planned_outage

    # <<< status
    # @generated
    # Status of this customer.
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the Customer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< customer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Customer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Customer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.trouble_tickets:
            s += '%s<%s:Customer.trouble_tickets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.works:
            s += '%s<%s:Customer.works rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_notifications:
            s += '%s<%s:Customer.outage_notifications rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_persons:
            s += '%s<%s:Customer.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_assets:
            s += '%s<%s:Customer.end_device_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Customer.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.planned_outage is not None:
            s += '%s<%s:Customer.planned_outage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.planned_outage.uri)
        if self.status is not None:
            s += '%s<%s:Customer.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Customer.kind>%s</%s:Customer.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:Customer.puc_number>%s</%s:Customer.puc_number>' % \
            (indent, ns_prefix, self.puc_number, ns_prefix)
        s += '%s<%s:Customer.special_need>%s</%s:Customer.special_need>' % \
            (indent, ns_prefix, self.special_need, ns_prefix)
        s += '%s<%s:Customer.vip>%s</%s:Customer.vip>' % \
            (indent, ns_prefix, self.vip, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Customer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> customer.serialize


class CustomerAgreement(Agreement):
    """ Agreement between the Customer and the ServiceSupplier to pay for service at a specific ServiceLocation. It records certain billing information about the type of service provided at the ServiceLocation and is used during charge creation to determine the type of service.
    """
    # <<< customer_agreement
    # @generated
    def __init__(self, service_supplier=None, service_locations=None, service_category=None, service_delivery_points=None, demand_response_program=None, meter_readings=None, auxiliary_agreements=None, equipments=None, end_device_controls=None, customer_account=None, customer=None, standard_industry_code=None, pricing_structures=None, **kw_args):
        """ Initialises a new 'CustomerAgreement' instance.
        """

        self._service_supplier = None
        self.service_supplier = service_supplier

        self._service_locations = []
        if service_locations is not None:
            self.service_locations = service_locations
        else:
            self.service_locations = []

        self._service_category = None
        self.service_category = service_category

        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []

        self._demand_response_program = None
        self.demand_response_program = demand_response_program

        self._meter_readings = []
        if meter_readings is not None:
            self.meter_readings = meter_readings
        else:
            self.meter_readings = []

        self._auxiliary_agreements = []
        if auxiliary_agreements is not None:
            self.auxiliary_agreements = auxiliary_agreements
        else:
            self.auxiliary_agreements = []

        self._equipments = []
        if equipments is not None:
            self.equipments = equipments
        else:
            self.equipments = []

        self._end_device_controls = []
        if end_device_controls is not None:
            self.end_device_controls = end_device_controls
        else:
            self.end_device_controls = []

        self._customer_account = None
        self.customer_account = customer_account

        self._customer = None
        self.customer = customer

        self._standard_industry_code = None
        self.standard_industry_code = standard_industry_code

        self._pricing_structures = []
        if pricing_structures is not None:
            self.pricing_structures = pricing_structures
        else:
            self.pricing_structures = []


        super(CustomerAgreement, self).__init__(**kw_args)
    # >>> customer_agreement

    # <<< service_supplier
    # @generated
    def get_service_supplier(self):
        """ Service supplier for this customer agreement.
        """
        return self._service_supplier

    def set_service_supplier(self, value):
        if self._service_supplier is not None:
            filtered = [x for x in self.service_supplier.customer_agreements if x != self]
            self._service_supplier._customer_agreements = filtered

        self._service_supplier = value
        if self._service_supplier is not None:
            self._service_supplier._customer_agreements.append(self)

    service_supplier = property(get_service_supplier, set_service_supplier)
    # >>> service_supplier

    # <<< service_locations
    # @generated
    def get_service_locations(self):
        """ All service locations regulated by this customer agreement.
        """
        return self._service_locations

    def set_service_locations(self, value):
        for p in self._service_locations:
            filtered = [q for q in p.customer_agreements if q != self]
            self._service_locations._customer_agreements = filtered
        for r in value:
            if self not in r._customer_agreements:
                r._customer_agreements.append(self)
        self._service_locations = value

    service_locations = property(get_service_locations, set_service_locations)

    def add_service_locations(self, *service_locations):
        for obj in service_locations:
            if self not in obj._customer_agreements:
                obj._customer_agreements.append(self)
            self._service_locations.append(obj)

    def remove_service_locations(self, *service_locations):
        for obj in service_locations:
            if self in obj._customer_agreements:
                obj._customer_agreements.remove(self)
            self._service_locations.remove(obj)
    # >>> service_locations

    # <<< service_category
    # @generated
    def get_service_category(self):
        """ 
        """
        return self._service_category

    def set_service_category(self, value):
        if self._service_category is not None:
            filtered = [x for x in self.service_category.customer_agreements if x != self]
            self._service_category._customer_agreements = filtered

        self._service_category = value
        if self._service_category is not None:
            self._service_category._customer_agreements.append(self)

    service_category = property(get_service_category, set_service_category)
    # >>> service_category

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ All service delivery points regulated by this customer agreement.
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for x in self._service_delivery_points:
            x._customer_agreement = None
        for y in value:
            y._customer_agreement = self
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            obj._customer_agreement = self
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            obj._customer_agreement = None
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points

    # <<< demand_response_program
    # @generated
    def get_demand_response_program(self):
        """ Demand response program for this customer agreement.
        """
        return self._demand_response_program

    def set_demand_response_program(self, value):
        if self._demand_response_program is not None:
            filtered = [x for x in self.demand_response_program.customer_agreements if x != self]
            self._demand_response_program._customer_agreements = filtered

        self._demand_response_program = value
        if self._demand_response_program is not None:
            self._demand_response_program._customer_agreements.append(self)

    demand_response_program = property(get_demand_response_program, set_demand_response_program)
    # >>> demand_response_program

    # <<< meter_readings
    # @generated
    def get_meter_readings(self):
        """ (could be deprecated in the future) All meter readings for this customer agreement.
        """
        return self._meter_readings

    def set_meter_readings(self, value):
        for x in self._meter_readings:
            x._customer_agreement = None
        for y in value:
            y._customer_agreement = self
        self._meter_readings = value

    meter_readings = property(get_meter_readings, set_meter_readings)

    def add_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            obj._customer_agreement = self
            self._meter_readings.append(obj)

    def remove_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            obj._customer_agreement = None
            self._meter_readings.remove(obj)
    # >>> meter_readings

    # <<< auxiliary_agreements
    # @generated
    def get_auxiliary_agreements(self):
        """ All (non-service related) auxiliary agreements that refer to this customer agreement.
        """
        return self._auxiliary_agreements

    def set_auxiliary_agreements(self, value):
        for x in self._auxiliary_agreements:
            x._customer_agreement = None
        for y in value:
            y._customer_agreement = self
        self._auxiliary_agreements = value

    auxiliary_agreements = property(get_auxiliary_agreements, set_auxiliary_agreements)

    def add_auxiliary_agreements(self, *auxiliary_agreements):
        for obj in auxiliary_agreements:
            obj._customer_agreement = self
            self._auxiliary_agreements.append(obj)

    def remove_auxiliary_agreements(self, *auxiliary_agreements):
        for obj in auxiliary_agreements:
            obj._customer_agreement = None
            self._auxiliary_agreements.remove(obj)
    # >>> auxiliary_agreements

    # <<< equipments
    # @generated
    def get_equipments(self):
        """ 
        """
        return self._equipments

    def set_equipments(self, value):
        for p in self._equipments:
            filtered = [q for q in p.customer_agreements if q != self]
            self._equipments._customer_agreements = filtered
        for r in value:
            if self not in r._customer_agreements:
                r._customer_agreements.append(self)
        self._equipments = value

    equipments = property(get_equipments, set_equipments)

    def add_equipments(self, *equipments):
        for obj in equipments:
            if self not in obj._customer_agreements:
                obj._customer_agreements.append(self)
            self._equipments.append(obj)

    def remove_equipments(self, *equipments):
        for obj in equipments:
            if self in obj._customer_agreements:
                obj._customer_agreements.remove(self)
            self._equipments.remove(obj)
    # >>> equipments

    # <<< end_device_controls
    # @generated
    def get_end_device_controls(self):
        """ Could be deprecated in the future.
        """
        return self._end_device_controls

    def set_end_device_controls(self, value):
        for x in self._end_device_controls:
            x._customer_agreement = None
        for y in value:
            y._customer_agreement = self
        self._end_device_controls = value

    end_device_controls = property(get_end_device_controls, set_end_device_controls)

    def add_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._customer_agreement = self
            self._end_device_controls.append(obj)

    def remove_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._customer_agreement = None
            self._end_device_controls.remove(obj)
    # >>> end_device_controls

    # <<< customer_account
    # @generated
    def get_customer_account(self):
        """ Customer account owning this agreement.
        """
        return self._customer_account

    def set_customer_account(self, value):
        if self._customer_account is not None:
            filtered = [x for x in self.customer_account.customer_agreements if x != self]
            self._customer_account._customer_agreements = filtered

        self._customer_account = value
        if self._customer_account is not None:
            self._customer_account._customer_agreements.append(self)

    customer_account = property(get_customer_account, set_customer_account)
    # >>> customer_account

    # <<< customer
    # @generated
    def get_customer(self):
        """ Customer for this agreement.
        """
        return self._customer

    def set_customer(self, value):
        if self._customer is not None:
            filtered = [x for x in self.customer.customer_agreements if x != self]
            self._customer._customer_agreements = filtered

        self._customer = value
        if self._customer is not None:
            self._customer._customer_agreements.append(self)

    customer = property(get_customer, set_customer)
    # >>> customer

    # <<< standard_industry_code
    # @generated
    def get_standard_industry_code(self):
        """ 
        """
        return self._standard_industry_code

    def set_standard_industry_code(self, value):
        if self._standard_industry_code is not None:
            filtered = [x for x in self.standard_industry_code.customer_agreements if x != self]
            self._standard_industry_code._customer_agreements = filtered

        self._standard_industry_code = value
        if self._standard_industry_code is not None:
            self._standard_industry_code._customer_agreements.append(self)

    standard_industry_code = property(get_standard_industry_code, set_standard_industry_code)
    # >>> standard_industry_code

    # <<< pricing_structures
    # @generated
    def get_pricing_structures(self):
        """ All pricing structures applicable to this customer agreement.
        """
        return self._pricing_structures

    def set_pricing_structures(self, value):
        for p in self._pricing_structures:
            filtered = [q for q in p.customer_agreements if q != self]
            self._pricing_structures._customer_agreements = filtered
        for r in value:
            if self not in r._customer_agreements:
                r._customer_agreements.append(self)
        self._pricing_structures = value

    pricing_structures = property(get_pricing_structures, set_pricing_structures)

    def add_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            if self not in obj._customer_agreements:
                obj._customer_agreements.append(self)
            self._pricing_structures.append(obj)

    def remove_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            if self in obj._customer_agreements:
                obj._customer_agreements.remove(self)
            self._pricing_structures.remove(obj)
    # >>> pricing_structures


    def __str__(self):
        """ Returns a string representation of the CustomerAgreement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< customer_agreement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CustomerAgreement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CustomerAgreement", self.uri)
        if format:
            indent += ' ' * depth

        if self.service_supplier is not None:
            s += '%s<%s:CustomerAgreement.service_supplier rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.service_supplier.uri)
        for obj in self.service_locations:
            s += '%s<%s:CustomerAgreement.service_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.service_category is not None:
            s += '%s<%s:CustomerAgreement.service_category rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.service_category.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:CustomerAgreement.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.demand_response_program is not None:
            s += '%s<%s:CustomerAgreement.demand_response_program rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.demand_response_program.uri)
        for obj in self.meter_readings:
            s += '%s<%s:CustomerAgreement.meter_readings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.auxiliary_agreements:
            s += '%s<%s:CustomerAgreement.auxiliary_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipments:
            s += '%s<%s:CustomerAgreement.equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_controls:
            s += '%s<%s:CustomerAgreement.end_device_controls rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.customer_account is not None:
            s += '%s<%s:CustomerAgreement.customer_account rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_account.uri)
        if self.customer is not None:
            s += '%s<%s:CustomerAgreement.customer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer.uri)
        if self.standard_industry_code is not None:
            s += '%s<%s:CustomerAgreement.standard_industry_code rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.standard_industry_code.uri)
        for obj in self.pricing_structures:
            s += '%s<%s:CustomerAgreement.pricing_structures rdf:resource="#%s"/>' % \
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
        if self.validity_interval is not None:
            s += '%s<%s:Agreement.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        s += '%s<%s:Agreement.sign_date>%s</%s:Agreement.sign_date>' % \
            (indent, ns_prefix, self.sign_date, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CustomerAgreement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> customer_agreement.serialize


class ServiceLocation(Location):
    """ A customer ServiceLocation has one or more ServiceDeliveryPoint(s), which in turn relate to Meters. The location may be a point or a polygon, depending on the specific circumstances. For distribution, the ServiceLocation is typically the location of the utility customer's premise. Because a customer's premise may have one or more meters, the ServiceDeliveryPoint is used to define the actual conducting equipment that the EndDeviceAsset attaches to at the utility customer's ServiceLocation. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party.
    """
    # <<< service_location
    # @generated
    def __init__(self, needs_inspection=False, access_method='', site_access_problem='', customer_agreements=None, end_device_assets=None, service_delivery_points=None, **kw_args):
        """ Initialises a new 'ServiceLocation' instance.
        """
        # True if inspection is needed of facilities at this service location. This could be requested by a customer, due to suspected tampering, environmental concerns (e.g., a fire in the vicinity), or to correct incompatible data. 
        self.needs_inspection = needs_inspection

        # Method for the service person to access the appropriate service locations. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        self.access_method = access_method

        # Problems previously encountered when visiting or performing work on this site. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        self.site_access_problem = site_access_problem


        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._end_device_assets = []
        if end_device_assets is not None:
            self.end_device_assets = end_device_assets
        else:
            self.end_device_assets = []

        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []


        super(ServiceLocation, self).__init__(**kw_args)
    # >>> service_location

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ All customer agreements regulating this service location.
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for p in self._customer_agreements:
            filtered = [q for q in p.service_locations if q != self]
            self._customer_agreements._service_locations = filtered
        for r in value:
            if self not in r._service_locations:
                r._service_locations.append(self)
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            if self not in obj._service_locations:
                obj._service_locations.append(self)
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            if self in obj._service_locations:
                obj._service_locations.remove(self)
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

    # <<< end_device_assets
    # @generated
    def get_end_device_assets(self):
        """ All end device assets that measure the service delivered to this service location.
        """
        return self._end_device_assets

    def set_end_device_assets(self, value):
        for x in self._end_device_assets:
            x._service_location = None
        for y in value:
            y._service_location = self
        self._end_device_assets = value

    end_device_assets = property(get_end_device_assets, set_end_device_assets)

    def add_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._service_location = self
            self._end_device_assets.append(obj)

    def remove_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._service_location = None
            self._end_device_assets.remove(obj)
    # >>> end_device_assets

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ All service delivery points delivering service (of the same type) to this service location.
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for x in self._service_delivery_points:
            x._service_location = None
        for y in value:
            y._service_location = self
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            obj._service_location = self
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            obj._service_location = None
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points


    def __str__(self):
        """ Returns a string representation of the ServiceLocation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< service_location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ServiceLocation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ServiceLocation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.customer_agreements:
            s += '%s<%s:ServiceLocation.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.end_device_assets:
            s += '%s<%s:ServiceLocation.end_device_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.service_delivery_points:
            s += '%s<%s:ServiceLocation.service_delivery_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ServiceLocation.needs_inspection>%s</%s:ServiceLocation.needs_inspection>' % \
            (indent, ns_prefix, self.needs_inspection, ns_prefix)
        s += '%s<%s:ServiceLocation.access_method>%s</%s:ServiceLocation.access_method>' % \
            (indent, ns_prefix, self.access_method, ns_prefix)
        s += '%s<%s:ServiceLocation.site_access_problem>%s</%s:ServiceLocation.site_access_problem>' % \
            (indent, ns_prefix, self.site_access_problem, ns_prefix)
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
        for obj in self.document_roles:
            s += '%s<%s:Location.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_person_roles:
            s += '%s<%s:Location.erp_person_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.electronic_addresses:
            s += '%s<%s:Location.electronic_addresses rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:Location.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.routes:
            s += '%s<%s:Location.routes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.position_points:
            s += '%s<%s:Location.position_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_selectors:
            s += '%s<%s:Location.gml_selectors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.main_address is not None:
            s += '%s<%s:Location.main_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.main_address.uri)
        for obj in self.from_location_roles:
            s += '%s<%s:Location.from_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Location.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.to_location_roles:
            s += '%s<%s:Location.to_location_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.telephone_numbers:
            s += '%s<%s:Location.telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.secondary_address is not None:
            s += '%s<%s:Location.secondary_address rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.secondary_address.uri)
        for obj in self.land_properties:
            s += '%s<%s:Location.land_properties rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.measurements:
            s += '%s<%s:Location.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:Location.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.dimensions_info is not None:
            s += '%s<%s:Location.dimensions_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.dimensions_info.uri)
        for obj in self.asset_roles:
            s += '%s<%s:Location.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:Location.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.red_lines:
            s += '%s<%s:Location.red_lines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gml_observatins:
            s += '%s<%s:Location.gml_observatins rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.hazards:
            s += '%s<%s:Location.hazards rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.activity_records:
            s += '%s<%s:Location.activity_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Location.corporate_code>%s</%s:Location.corporate_code>' % \
            (indent, ns_prefix, self.corporate_code, ns_prefix)
        s += '%s<%s:Location.direction>%s</%s:Location.direction>' % \
            (indent, ns_prefix, self.direction, ns_prefix)
        s += '%s<%s:Location.is_polygon>%s</%s:Location.is_polygon>' % \
            (indent, ns_prefix, self.is_polygon, ns_prefix)
        s += '%s<%s:Location.category>%s</%s:Location.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:Location.geo_info_reference>%s</%s:Location.geo_info_reference>' % \
            (indent, ns_prefix, self.geo_info_reference, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ServiceLocation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> service_location.serialize


# <<< customers
# @generated
# >>> customers
