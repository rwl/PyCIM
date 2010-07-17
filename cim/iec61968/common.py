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

""" This package contains the information classes that support distribution management in general.
"""

from cim.iec61970.core import IdentifiedObject
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.common"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Common"

class Organisation(IdentifiedObject):
    """ Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """
    # <<< organisation
    # @generated
    def __init__(self, business_roles=None, telephone_numbers=None, street_address=None, market_roles=None, postal_address=None, electronic_addresses=None, **kw_args):
        """ Initialises a new 'Organisation' instance.
        """

        self._business_roles = []
        if business_roles is not None:
            self.business_roles = business_roles
        else:
            self.business_roles = []

        self._telephone_numbers = []
        if telephone_numbers is not None:
            self.telephone_numbers = telephone_numbers
        else:
            self.telephone_numbers = []

        self.street_address = street_address

        self._market_roles = []
        if market_roles is not None:
            self.market_roles = market_roles
        else:
            self.market_roles = []

        self.postal_address = postal_address

        self._electronic_addresses = []
        if electronic_addresses is not None:
            self.electronic_addresses = electronic_addresses
        else:
            self.electronic_addresses = []


        super(Organisation, self).__init__(**kw_args)
    # >>> organisation

    # <<< business_roles
    # @generated
    def get_business_roles(self):
        """ 
        """
        return self._business_roles

    def set_business_roles(self, value):
        for p in self._business_roles:
            filtered = [q for q in p.organisations if q != self]
            self._business_roles._organisations = filtered
        for r in value:
            if self not in r._organisations:
                r._organisations.append(self)
        self._business_roles = value

    business_roles = property(get_business_roles, set_business_roles)

    def add_business_roles(self, *business_roles):
        for obj in business_roles:
            if self not in obj._organisations:
                obj._organisations.append(self)
            self._business_roles.append(obj)

    def remove_business_roles(self, *business_roles):
        for obj in business_roles:
            if self in obj._organisations:
                obj._organisations.remove(self)
            self._business_roles.remove(obj)
    # >>> business_roles

    # <<< telephone_numbers
    # @generated
    def get_telephone_numbers(self):
        """ All telephone numbers of this organisation.
        """
        return self._telephone_numbers

    def set_telephone_numbers(self, value):
        for x in self._telephone_numbers:
            x._organisation = None
        for y in value:
            y._organisation = self
        self._telephone_numbers = value

    telephone_numbers = property(get_telephone_numbers, set_telephone_numbers)

    def add_telephone_numbers(self, *telephone_numbers):
        for obj in telephone_numbers:
            obj._organisation = self
            self._telephone_numbers.append(obj)

    def remove_telephone_numbers(self, *telephone_numbers):
        for obj in telephone_numbers:
            obj._organisation = None
            self._telephone_numbers.remove(obj)
    # >>> telephone_numbers

    # <<< street_address
    # @generated
    # Street address.
    street_address = None
    # >>> street_address

    # <<< market_roles
    # @generated
    def get_market_roles(self):
        """ 
        """
        return self._market_roles

    def set_market_roles(self, value):
        for p in self._market_roles:
            filtered = [q for q in p.organisations if q != self]
            self._market_roles._organisations = filtered
        for r in value:
            if self not in r._organisations:
                r._organisations.append(self)
        self._market_roles = value

    market_roles = property(get_market_roles, set_market_roles)

    def add_market_roles(self, *market_roles):
        for obj in market_roles:
            if self not in obj._organisations:
                obj._organisations.append(self)
            self._market_roles.append(obj)

    def remove_market_roles(self, *market_roles):
        for obj in market_roles:
            if self in obj._organisations:
                obj._organisations.remove(self)
            self._market_roles.remove(obj)
    # >>> market_roles

    # <<< postal_address
    # @generated
    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postal_address = None
    # >>> postal_address

    # <<< electronic_addresses
    # @generated
    def get_electronic_addresses(self):
        """ All electronic addresses of this organisation.
        """
        return self._electronic_addresses

    def set_electronic_addresses(self, value):
        for x in self._electronic_addresses:
            x._organisation = None
        for y in value:
            y._organisation = self
        self._electronic_addresses = value

    electronic_addresses = property(get_electronic_addresses, set_electronic_addresses)

    def add_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            obj._organisation = self
            self._electronic_addresses.append(obj)

    def remove_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            obj._organisation = None
            self._electronic_addresses.remove(obj)
    # >>> electronic_addresses


    def __str__(self):
        """ Returns a string representation of the Organisation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< organisation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Organisation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Organisation", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Organisation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> organisation.serialize


class ActivityRecord(IdentifiedObject):
    """ Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """
    # <<< activity_record
    # @generated
    def __init__(self, reason='', category='', severity='', created_date_time='', market_factors=None, documents=None, organisations=None, scheduled_event=None, assets=None, erp_persons=None, locations=None, status=None, **kw_args):
        """ Initialises a new 'ActivityRecord' instance.
        """
        # Reason for event resulting in this activity record, typically supplied when user initiated. 
        self.reason = reason

        # Category of event resulting in this activity record. 
        self.category = category

        # Severity level of event resulting in this activity record. 
        self.severity = severity

        # Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable). 
        self.created_date_time = created_date_time


        if market_factors is not None:
            self.market_factors = market_factors
        else:
            self.market_factors = []

        self._documents = []
        if documents is not None:
            self.documents = documents
        else:
            self.documents = []

        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []

        self._scheduled_event = None
        self.scheduled_event = scheduled_event

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self.status = status


        super(ActivityRecord, self).__init__(**kw_args)
    # >>> activity_record

    # <<< market_factors
    # @generated
    def add_market_factors(self, *market_factors):
        for obj in market_factors:
            self.market_factors.append(obj)

    def remove_market_factors(self, *market_factors):
        for obj in market_factors:
            self.market_factors.remove(obj)
    # >>> market_factors

    # <<< documents
    # @generated
    def get_documents(self):
        """ All documents for which this activity record has been created.
        """
        return self._documents

    def set_documents(self, value):
        for p in self._documents:
            filtered = [q for q in p.activity_records if q != self]
            self._documents._activity_records = filtered
        for r in value:
            if self not in r._activity_records:
                r._activity_records.append(self)
        self._documents = value

    documents = property(get_documents, set_documents)

    def add_documents(self, *documents):
        for obj in documents:
            if self not in obj._activity_records:
                obj._activity_records.append(self)
            self._documents.append(obj)

    def remove_documents(self, *documents):
        for obj in documents:
            if self in obj._activity_records:
                obj._activity_records.remove(self)
            self._documents.remove(obj)
    # >>> documents

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.activity_records if q != self]
            self._organisations._activity_records = filtered
        for r in value:
            if self not in r._activity_records:
                r._activity_records.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._activity_records:
                obj._activity_records.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._activity_records:
                obj._activity_records.remove(self)
            self._organisations.remove(obj)
    # >>> organisations

    # <<< scheduled_event
    # @generated
    def get_scheduled_event(self):
        """ 
        """
        return self._scheduled_event

    def set_scheduled_event(self, value):
        if self._scheduled_event is not None:
            self._scheduled_event._activity_record = None

        self._scheduled_event = value
        if self._scheduled_event is not None:
            self._scheduled_event._activity_record = self

    scheduled_event = property(get_scheduled_event, set_scheduled_event)
    # >>> scheduled_event

    # <<< assets
    # @generated
    def get_assets(self):
        """ All assets for which this activity record has been created.
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.activity_records if q != self]
            self._assets._activity_records = filtered
        for r in value:
            if self not in r._activity_records:
                r._activity_records.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._activity_records:
                obj._activity_records.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._activity_records:
                obj._activity_records.remove(self)
            self._assets.remove(obj)
    # >>> assets

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.activity_records if q != self]
            self._erp_persons._activity_records = filtered
        for r in value:
            if self not in r._activity_records:
                r._activity_records.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._activity_records:
                obj._activity_records.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._activity_records:
                obj._activity_records.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< locations
    # @generated
    def get_locations(self):
        """ 
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.activity_records if q != self]
            self._locations._activity_records = filtered
        for r in value:
            if self not in r._activity_records:
                r._activity_records.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._activity_records:
                obj._activity_records.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._activity_records:
                obj._activity_records.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< status
    # @generated
    # Information on consequence of event resulting in this activity record.
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the ActivityRecord.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< activity_record.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ActivityRecord.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ActivityRecord", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.market_factors:
            s += '%s<%s:ActivityRecord.market_factors rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.documents:
            s += '%s<%s:ActivityRecord.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.organisations:
            s += '%s<%s:ActivityRecord.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.scheduled_event is not None:
            s += '%s<%s:ActivityRecord.scheduled_event rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.scheduled_event.uri)
        for obj in self.assets:
            s += '%s<%s:ActivityRecord.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_persons:
            s += '%s<%s:ActivityRecord.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:ActivityRecord.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ActivityRecord.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:ActivityRecord.reason>%s</%s:ActivityRecord.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:ActivityRecord.category>%s</%s:ActivityRecord.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
        s += '%s<%s:ActivityRecord.severity>%s</%s:ActivityRecord.severity>' % \
            (indent, ns_prefix, self.severity, ns_prefix)
        s += '%s<%s:ActivityRecord.created_date_time>%s</%s:ActivityRecord.created_date_time>' % \
            (indent, ns_prefix, self.created_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ActivityRecord")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> activity_record.serialize


class Document(IdentifiedObject):
    """ Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """
    # <<< document
    # @generated
    def __init__(self, subject='', revision_number='', category='', last_modified_date_time='', title='', created_date_time='', activity_records=None, erp_organisation_roles=None, scheduled_events=None, from_document_roles=None, location_roles=None, power_system_resource_roles=None, network_data_sets=None, erp_person_roles=None, change_items=None, measurements=None, doc_status=None, schedule_parameter_infos=None, electronic_address=None, to_document_roles=None, status=None, asset_roles=None, change_sets=None, **kw_args):
        """ Initialises a new 'Document' instance.
        """
        # Document subject. 
        self.subject = subject

        # Revision number for this document. 
        self.revision_number = revision_number

        # Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        self.category = category

        # Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. 
        self.last_modified_date_time = last_modified_date_time

        # Document title. 
        self.title = title

        # Date and time that this document was created. 
        self.created_date_time = created_date_time


        self._activity_records = []
        if activity_records is not None:
            self.activity_records = activity_records
        else:
            self.activity_records = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self._scheduled_events = []
        if scheduled_events is not None:
            self.scheduled_events = scheduled_events
        else:
            self.scheduled_events = []

        self._from_document_roles = []
        if from_document_roles is not None:
            self.from_document_roles = from_document_roles
        else:
            self.from_document_roles = []

        self._location_roles = []
        if location_roles is not None:
            self.location_roles = location_roles
        else:
            self.location_roles = []

        self._power_system_resource_roles = []
        if power_system_resource_roles is not None:
            self.power_system_resource_roles = power_system_resource_roles
        else:
            self.power_system_resource_roles = []

        self._network_data_sets = []
        if network_data_sets is not None:
            self.network_data_sets = network_data_sets
        else:
            self.network_data_sets = []

        self._erp_person_roles = []
        if erp_person_roles is not None:
            self.erp_person_roles = erp_person_roles
        else:
            self.erp_person_roles = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self.doc_status = doc_status

        self._schedule_parameter_infos = []
        if schedule_parameter_infos is not None:
            self.schedule_parameter_infos = schedule_parameter_infos
        else:
            self.schedule_parameter_infos = []

        self._electronic_address = None
        self.electronic_address = electronic_address

        self._to_document_roles = []
        if to_document_roles is not None:
            self.to_document_roles = to_document_roles
        else:
            self.to_document_roles = []

        self.status = status

        self._asset_roles = []
        if asset_roles is not None:
            self.asset_roles = asset_roles
        else:
            self.asset_roles = []

        self._change_sets = []
        if change_sets is not None:
            self.change_sets = change_sets
        else:
            self.change_sets = []


        super(Document, self).__init__(**kw_args)
    # >>> document

    # <<< activity_records
    # @generated
    def get_activity_records(self):
        """ All activity records created for this document.
        """
        return self._activity_records

    def set_activity_records(self, value):
        for p in self._activity_records:
            filtered = [q for q in p.documents if q != self]
            self._activity_records._documents = filtered
        for r in value:
            if self not in r._documents:
                r._documents.append(self)
        self._activity_records = value

    activity_records = property(get_activity_records, set_activity_records)

    def add_activity_records(self, *activity_records):
        for obj in activity_records:
            if self not in obj._documents:
                obj._documents.append(self)
            self._activity_records.append(obj)

    def remove_activity_records(self, *activity_records):
        for obj in activity_records:
            if self in obj._documents:
                obj._documents.remove(self)
            self._activity_records.remove(obj)
    # >>> activity_records

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for x in self._erp_organisation_roles:
            x._document = None
        for y in value:
            y._document = self
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._document = self
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._document = None
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< scheduled_events
    # @generated
    def get_scheduled_events(self):
        """ 
        """
        return self._scheduled_events

    def set_scheduled_events(self, value):
        for x in self._scheduled_events:
            x._document = None
        for y in value:
            y._document = self
        self._scheduled_events = value

    scheduled_events = property(get_scheduled_events, set_scheduled_events)

    def add_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._document = self
            self._scheduled_events.append(obj)

    def remove_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._document = None
            self._scheduled_events.remove(obj)
    # >>> scheduled_events

    # <<< from_document_roles
    # @generated
    def get_from_document_roles(self):
        """ 
        """
        return self._from_document_roles

    def set_from_document_roles(self, value):
        for x in self._from_document_roles:
            x._to_document = None
        for y in value:
            y._to_document = self
        self._from_document_roles = value

    from_document_roles = property(get_from_document_roles, set_from_document_roles)

    def add_from_document_roles(self, *from_document_roles):
        for obj in from_document_roles:
            obj._to_document = self
            self._from_document_roles.append(obj)

    def remove_from_document_roles(self, *from_document_roles):
        for obj in from_document_roles:
            obj._to_document = None
            self._from_document_roles.remove(obj)
    # >>> from_document_roles

    # <<< location_roles
    # @generated
    def get_location_roles(self):
        """ 
        """
        return self._location_roles

    def set_location_roles(self, value):
        for x in self._location_roles:
            x._document = None
        for y in value:
            y._document = self
        self._location_roles = value

    location_roles = property(get_location_roles, set_location_roles)

    def add_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._document = self
            self._location_roles.append(obj)

    def remove_location_roles(self, *location_roles):
        for obj in location_roles:
            obj._document = None
            self._location_roles.remove(obj)
    # >>> location_roles

    # <<< power_system_resource_roles
    # @generated
    def get_power_system_resource_roles(self):
        """ 
        """
        return self._power_system_resource_roles

    def set_power_system_resource_roles(self, value):
        for x in self._power_system_resource_roles:
            x._document = None
        for y in value:
            y._document = self
        self._power_system_resource_roles = value

    power_system_resource_roles = property(get_power_system_resource_roles, set_power_system_resource_roles)

    def add_power_system_resource_roles(self, *power_system_resource_roles):
        for obj in power_system_resource_roles:
            obj._document = self
            self._power_system_resource_roles.append(obj)

    def remove_power_system_resource_roles(self, *power_system_resource_roles):
        for obj in power_system_resource_roles:
            obj._document = None
            self._power_system_resource_roles.remove(obj)
    # >>> power_system_resource_roles

    # <<< network_data_sets
    # @generated
    def get_network_data_sets(self):
        """ 
        """
        return self._network_data_sets

    def set_network_data_sets(self, value):
        for p in self._network_data_sets:
            filtered = [q for q in p.documents if q != self]
            self._network_data_sets._documents = filtered
        for r in value:
            if self not in r._documents:
                r._documents.append(self)
        self._network_data_sets = value

    network_data_sets = property(get_network_data_sets, set_network_data_sets)

    def add_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self not in obj._documents:
                obj._documents.append(self)
            self._network_data_sets.append(obj)

    def remove_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self in obj._documents:
                obj._documents.remove(self)
            self._network_data_sets.remove(obj)
    # >>> network_data_sets

    # <<< erp_person_roles
    # @generated
    def get_erp_person_roles(self):
        """ 
        """
        return self._erp_person_roles

    def set_erp_person_roles(self, value):
        for x in self._erp_person_roles:
            x._document = None
        for y in value:
            y._document = self
        self._erp_person_roles = value

    erp_person_roles = property(get_erp_person_roles, set_erp_person_roles)

    def add_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._document = self
            self._erp_person_roles.append(obj)

    def remove_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._document = None
            self._erp_person_roles.remove(obj)
    # >>> erp_person_roles

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._document = None
        for y in value:
            y._document = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._document = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._document = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ Measurements are specified in types of documents, such as procedures.
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.documents if q != self]
            self._measurements._documents = filtered
        for r in value:
            if self not in r._documents:
                r._documents.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._documents:
                obj._documents.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._documents:
                obj._documents.remove(self)
            self._measurements.remove(obj)
    # >>> measurements

    # <<< doc_status
    # @generated
    # Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
    doc_status = None
    # >>> doc_status

    # <<< schedule_parameter_infos
    # @generated
    def get_schedule_parameter_infos(self):
        """ 
        """
        return self._schedule_parameter_infos

    def set_schedule_parameter_infos(self, value):
        for p in self._schedule_parameter_infos:
            filtered = [q for q in p.documents if q != self]
            self._schedule_parameter_infos._documents = filtered
        for r in value:
            if self not in r._documents:
                r._documents.append(self)
        self._schedule_parameter_infos = value

    schedule_parameter_infos = property(get_schedule_parameter_infos, set_schedule_parameter_infos)

    def add_schedule_parameter_infos(self, *schedule_parameter_infos):
        for obj in schedule_parameter_infos:
            if self not in obj._documents:
                obj._documents.append(self)
            self._schedule_parameter_infos.append(obj)

    def remove_schedule_parameter_infos(self, *schedule_parameter_infos):
        for obj in schedule_parameter_infos:
            if self in obj._documents:
                obj._documents.remove(self)
            self._schedule_parameter_infos.remove(obj)
    # >>> schedule_parameter_infos

    # <<< electronic_address
    # @generated
    def get_electronic_address(self):
        """ 
        """
        return self._electronic_address

    def set_electronic_address(self, value):
        if self._electronic_address is not None:
            self._electronic_address._document = None

        self._electronic_address = value
        if self._electronic_address is not None:
            self._electronic_address._document = self

    electronic_address = property(get_electronic_address, set_electronic_address)
    # >>> electronic_address

    # <<< to_document_roles
    # @generated
    def get_to_document_roles(self):
        """ 
        """
        return self._to_document_roles

    def set_to_document_roles(self, value):
        for x in self._to_document_roles:
            x._from_document = None
        for y in value:
            y._from_document = self
        self._to_document_roles = value

    to_document_roles = property(get_to_document_roles, set_to_document_roles)

    def add_to_document_roles(self, *to_document_roles):
        for obj in to_document_roles:
            obj._from_document = self
            self._to_document_roles.append(obj)

    def remove_to_document_roles(self, *to_document_roles):
        for obj in to_document_roles:
            obj._from_document = None
            self._to_document_roles.remove(obj)
    # >>> to_document_roles

    # <<< status
    # @generated
    # Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
    status = None
    # >>> status

    # <<< asset_roles
    # @generated
    def get_asset_roles(self):
        """ 
        """
        return self._asset_roles

    def set_asset_roles(self, value):
        for x in self._asset_roles:
            x._document = None
        for y in value:
            y._document = self
        self._asset_roles = value

    asset_roles = property(get_asset_roles, set_asset_roles)

    def add_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._document = self
            self._asset_roles.append(obj)

    def remove_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._document = None
            self._asset_roles.remove(obj)
    # >>> asset_roles

    # <<< change_sets
    # @generated
    def get_change_sets(self):
        """ 
        """
        return self._change_sets

    def set_change_sets(self, value):
        for p in self._change_sets:
            filtered = [q for q in p.documents if q != self]
            self._change_sets._documents = filtered
        for r in value:
            if self not in r._documents:
                r._documents.append(self)
        self._change_sets = value

    change_sets = property(get_change_sets, set_change_sets)

    def add_change_sets(self, *change_sets):
        for obj in change_sets:
            if self not in obj._documents:
                obj._documents.append(self)
            self._change_sets.append(obj)

    def remove_change_sets(self, *change_sets):
        for obj in change_sets:
            if self in obj._documents:
                obj._documents.remove(self)
            self._change_sets.remove(obj)
    # >>> change_sets


    def __str__(self):
        """ Returns a string representation of the Document.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< document.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Document.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Document", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Document")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> document.serialize


class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """
    # <<< position_point
    # @generated
    def __init__(self, sequence_number=0, z_position='', x_position='', y_position='', location=None, **kw_args):
        """ Initialises a new 'PositionPoint' instance.
        """
        # Zero-relative sequence number of this point within a series of points. 
        self.sequence_number = sequence_number

        # (if applicable) Z axis position. 
        self.z_position = z_position

        # X axis position. 
        self.x_position = x_position

        # Y axis position. 
        self.y_position = y_position


        self._location = None
        self.location = location


        super(PositionPoint, self).__init__(**kw_args)
    # >>> position_point

    # <<< location
    # @generated
    def get_location(self):
        """ Location that this position point describes.
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.position_points if x != self]
            self._location._position_points = filtered

        self._location = value
        if self._location is not None:
            self._location._position_points.append(self)

    location = property(get_location, set_location)
    # >>> location


    def __str__(self):
        """ Returns a string representation of the PositionPoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< position_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PositionPoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PositionPoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.location is not None:
            s += '%s<%s:PositionPoint.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        s += '%s<%s:PositionPoint.sequence_number>%s</%s:PositionPoint.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:PositionPoint.z_position>%s</%s:PositionPoint.z_position>' % \
            (indent, ns_prefix, self.z_position, ns_prefix)
        s += '%s<%s:PositionPoint.x_position>%s</%s:PositionPoint.x_position>' % \
            (indent, ns_prefix, self.x_position, ns_prefix)
        s += '%s<%s:PositionPoint.y_position>%s</%s:PositionPoint.y_position>' % \
            (indent, ns_prefix, self.y_position, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PositionPoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> position_point.serialize


class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """
    # <<< location
    # @generated
    def __init__(self, corporate_code='', direction='', is_polygon=False, category='', geo_info_reference='', document_roles=None, erp_person_roles=None, electronic_addresses=None, change_items=None, routes=None, position_points=None, gml_selectors=None, main_address=None, from_location_roles=None, status=None, to_location_roles=None, telephone_numbers=None, secondary_address=None, land_properties=None, measurements=None, erp_organisation_roles=None, dimensions_info=None, asset_roles=None, crews=None, red_lines=None, gml_observatins=None, hazards=None, activity_records=None, **kw_args):
        """ Initialises a new 'Location' instance.
        """
        # Utility-specific code for the location. 
        self.corporate_code = corporate_code

        # (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building. 
        self.direction = direction

        # True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments. 
        self.is_polygon = is_polygon

        # Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location). 
        self.category = category

        # (if applicable) Reference to geographical information source, often external to the utility. 
        self.geo_info_reference = geo_info_reference


        self._document_roles = []
        if document_roles is not None:
            self.document_roles = document_roles
        else:
            self.document_roles = []

        self._erp_person_roles = []
        if erp_person_roles is not None:
            self.erp_person_roles = erp_person_roles
        else:
            self.erp_person_roles = []

        self._electronic_addresses = []
        if electronic_addresses is not None:
            self.electronic_addresses = electronic_addresses
        else:
            self.electronic_addresses = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._routes = []
        if routes is not None:
            self.routes = routes
        else:
            self.routes = []

        self._position_points = []
        if position_points is not None:
            self.position_points = position_points
        else:
            self.position_points = []

        self._gml_selectors = []
        if gml_selectors is not None:
            self.gml_selectors = gml_selectors
        else:
            self.gml_selectors = []

        self.main_address = main_address

        self._from_location_roles = []
        if from_location_roles is not None:
            self.from_location_roles = from_location_roles
        else:
            self.from_location_roles = []

        self.status = status

        self._to_location_roles = []
        if to_location_roles is not None:
            self.to_location_roles = to_location_roles
        else:
            self.to_location_roles = []

        self._telephone_numbers = []
        if telephone_numbers is not None:
            self.telephone_numbers = telephone_numbers
        else:
            self.telephone_numbers = []

        self.secondary_address = secondary_address

        self._land_properties = []
        if land_properties is not None:
            self.land_properties = land_properties
        else:
            self.land_properties = []

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._erp_organisation_roles = []
        if erp_organisation_roles is not None:
            self.erp_organisation_roles = erp_organisation_roles
        else:
            self.erp_organisation_roles = []

        self._dimensions_info = None
        self.dimensions_info = dimensions_info

        self._asset_roles = []
        if asset_roles is not None:
            self.asset_roles = asset_roles
        else:
            self.asset_roles = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self._red_lines = []
        if red_lines is not None:
            self.red_lines = red_lines
        else:
            self.red_lines = []

        self._gml_observatins = []
        if gml_observatins is not None:
            self.gml_observatins = gml_observatins
        else:
            self.gml_observatins = []

        self._hazards = []
        if hazards is not None:
            self.hazards = hazards
        else:
            self.hazards = []

        self._activity_records = []
        if activity_records is not None:
            self.activity_records = activity_records
        else:
            self.activity_records = []


        super(Location, self).__init__(**kw_args)
    # >>> location

    # <<< document_roles
    # @generated
    def get_document_roles(self):
        """ 
        """
        return self._document_roles

    def set_document_roles(self, value):
        for x in self._document_roles:
            x._location = None
        for y in value:
            y._location = self
        self._document_roles = value

    document_roles = property(get_document_roles, set_document_roles)

    def add_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._location = self
            self._document_roles.append(obj)

    def remove_document_roles(self, *document_roles):
        for obj in document_roles:
            obj._location = None
            self._document_roles.remove(obj)
    # >>> document_roles

    # <<< erp_person_roles
    # @generated
    def get_erp_person_roles(self):
        """ 
        """
        return self._erp_person_roles

    def set_erp_person_roles(self, value):
        for x in self._erp_person_roles:
            x._location = None
        for y in value:
            y._location = self
        self._erp_person_roles = value

    erp_person_roles = property(get_erp_person_roles, set_erp_person_roles)

    def add_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._location = self
            self._erp_person_roles.append(obj)

    def remove_erp_person_roles(self, *erp_person_roles):
        for obj in erp_person_roles:
            obj._location = None
            self._erp_person_roles.remove(obj)
    # >>> erp_person_roles

    # <<< electronic_addresses
    # @generated
    def get_electronic_addresses(self):
        """ All electronic addresses of this location.
        """
        return self._electronic_addresses

    def set_electronic_addresses(self, value):
        for p in self._electronic_addresses:
            filtered = [q for q in p.locations if q != self]
            self._electronic_addresses._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._electronic_addresses = value

    electronic_addresses = property(get_electronic_addresses, set_electronic_addresses)

    def add_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            if self not in obj._locations:
                obj._locations.append(self)
            self._electronic_addresses.append(obj)

    def remove_electronic_addresses(self, *electronic_addresses):
        for obj in electronic_addresses:
            if self in obj._locations:
                obj._locations.remove(self)
            self._electronic_addresses.remove(obj)
    # >>> electronic_addresses

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._location = None
        for y in value:
            y._location = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._location = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._location = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< routes
    # @generated
    def get_routes(self):
        """ 
        """
        return self._routes

    def set_routes(self, value):
        for p in self._routes:
            filtered = [q for q in p.locations if q != self]
            self._routes._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._routes = value

    routes = property(get_routes, set_routes)

    def add_routes(self, *routes):
        for obj in routes:
            if self not in obj._locations:
                obj._locations.append(self)
            self._routes.append(obj)

    def remove_routes(self, *routes):
        for obj in routes:
            if self in obj._locations:
                obj._locations.remove(self)
            self._routes.remove(obj)
    # >>> routes

    # <<< position_points
    # @generated
    def get_position_points(self):
        """ Sequence of position points describing this location.
        """
        return self._position_points

    def set_position_points(self, value):
        for x in self._position_points:
            x._location = None
        for y in value:
            y._location = self
        self._position_points = value

    position_points = property(get_position_points, set_position_points)

    def add_position_points(self, *position_points):
        for obj in position_points:
            obj._location = self
            self._position_points.append(obj)

    def remove_position_points(self, *position_points):
        for obj in position_points:
            obj._location = None
            self._position_points.remove(obj)
    # >>> position_points

    # <<< gml_selectors
    # @generated
    def get_gml_selectors(self):
        """ 
        """
        return self._gml_selectors

    def set_gml_selectors(self, value):
        for p in self._gml_selectors:
            filtered = [q for q in p.locations if q != self]
            self._gml_selectors._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._gml_selectors = value

    gml_selectors = property(get_gml_selectors, set_gml_selectors)

    def add_gml_selectors(self, *gml_selectors):
        for obj in gml_selectors:
            if self not in obj._locations:
                obj._locations.append(self)
            self._gml_selectors.append(obj)

    def remove_gml_selectors(self, *gml_selectors):
        for obj in gml_selectors:
            if self in obj._locations:
                obj._locations.remove(self)
            self._gml_selectors.remove(obj)
    # >>> gml_selectors

    # <<< main_address
    # @generated
    # Main address of the location.
    main_address = None
    # >>> main_address

    # <<< from_location_roles
    # @generated
    def get_from_location_roles(self):
        """ 
        """
        return self._from_location_roles

    def set_from_location_roles(self, value):
        for x in self._from_location_roles:
            x._to_location = None
        for y in value:
            y._to_location = self
        self._from_location_roles = value

    from_location_roles = property(get_from_location_roles, set_from_location_roles)

    def add_from_location_roles(self, *from_location_roles):
        for obj in from_location_roles:
            obj._to_location = self
            self._from_location_roles.append(obj)

    def remove_from_location_roles(self, *from_location_roles):
        for obj in from_location_roles:
            obj._to_location = None
            self._from_location_roles.remove(obj)
    # >>> from_location_roles

    # <<< status
    # @generated
    # Status of this location.
    status = None
    # >>> status

    # <<< to_location_roles
    # @generated
    def get_to_location_roles(self):
        """ 
        """
        return self._to_location_roles

    def set_to_location_roles(self, value):
        for x in self._to_location_roles:
            x._from_location = None
        for y in value:
            y._from_location = self
        self._to_location_roles = value

    to_location_roles = property(get_to_location_roles, set_to_location_roles)

    def add_to_location_roles(self, *to_location_roles):
        for obj in to_location_roles:
            obj._from_location = self
            self._to_location_roles.append(obj)

    def remove_to_location_roles(self, *to_location_roles):
        for obj in to_location_roles:
            obj._from_location = None
            self._to_location_roles.remove(obj)
    # >>> to_location_roles

    # <<< telephone_numbers
    # @generated
    def get_telephone_numbers(self):
        """ All telephone numbers of this location.
        """
        return self._telephone_numbers

    def set_telephone_numbers(self, value):
        for x in self._telephone_numbers:
            x._location = None
        for y in value:
            y._location = self
        self._telephone_numbers = value

    telephone_numbers = property(get_telephone_numbers, set_telephone_numbers)

    def add_telephone_numbers(self, *telephone_numbers):
        for obj in telephone_numbers:
            obj._location = self
            self._telephone_numbers.append(obj)

    def remove_telephone_numbers(self, *telephone_numbers):
        for obj in telephone_numbers:
            obj._location = None
            self._telephone_numbers.remove(obj)
    # >>> telephone_numbers

    # <<< secondary_address
    # @generated
    # Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
    secondary_address = None
    # >>> secondary_address

    # <<< land_properties
    # @generated
    def get_land_properties(self):
        """ 
        """
        return self._land_properties

    def set_land_properties(self, value):
        for p in self._land_properties:
            filtered = [q for q in p.locations if q != self]
            self._land_properties._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._land_properties = value

    land_properties = property(get_land_properties, set_land_properties)

    def add_land_properties(self, *land_properties):
        for obj in land_properties:
            if self not in obj._locations:
                obj._locations.append(self)
            self._land_properties.append(obj)

    def remove_land_properties(self, *land_properties):
        for obj in land_properties:
            if self in obj._locations:
                obj._locations.remove(self)
            self._land_properties.remove(obj)
    # >>> land_properties

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ 
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.locations if q != self]
            self._measurements._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._locations:
                obj._locations.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._locations:
                obj._locations.remove(self)
            self._measurements.remove(obj)
    # >>> measurements

    # <<< erp_organisation_roles
    # @generated
    def get_erp_organisation_roles(self):
        """ 
        """
        return self._erp_organisation_roles

    def set_erp_organisation_roles(self, value):
        for x in self._erp_organisation_roles:
            x._location = None
        for y in value:
            y._location = self
        self._erp_organisation_roles = value

    erp_organisation_roles = property(get_erp_organisation_roles, set_erp_organisation_roles)

    def add_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._location = self
            self._erp_organisation_roles.append(obj)

    def remove_erp_organisation_roles(self, *erp_organisation_roles):
        for obj in erp_organisation_roles:
            obj._location = None
            self._erp_organisation_roles.remove(obj)
    # >>> erp_organisation_roles

    # <<< dimensions_info
    # @generated
    def get_dimensions_info(self):
        """ 
        """
        return self._dimensions_info

    def set_dimensions_info(self, value):
        if self._dimensions_info is not None:
            filtered = [x for x in self.dimensions_info.locations if x != self]
            self._dimensions_info._locations = filtered

        self._dimensions_info = value
        if self._dimensions_info is not None:
            self._dimensions_info._locations.append(self)

    dimensions_info = property(get_dimensions_info, set_dimensions_info)
    # >>> dimensions_info

    # <<< asset_roles
    # @generated
    def get_asset_roles(self):
        """ 
        """
        return self._asset_roles

    def set_asset_roles(self, value):
        for x in self._asset_roles:
            x._location = None
        for y in value:
            y._location = self
        self._asset_roles = value

    asset_roles = property(get_asset_roles, set_asset_roles)

    def add_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._location = self
            self._asset_roles.append(obj)

    def remove_asset_roles(self, *asset_roles):
        for obj in asset_roles:
            obj._location = None
            self._asset_roles.remove(obj)
    # >>> asset_roles

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.locations if q != self]
            self._crews._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._locations:
                obj._locations.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._locations:
                obj._locations.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< red_lines
    # @generated
    def get_red_lines(self):
        """ 
        """
        return self._red_lines

    def set_red_lines(self, value):
        for p in self._red_lines:
            filtered = [q for q in p.locations if q != self]
            self._red_lines._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._red_lines = value

    red_lines = property(get_red_lines, set_red_lines)

    def add_red_lines(self, *red_lines):
        for obj in red_lines:
            if self not in obj._locations:
                obj._locations.append(self)
            self._red_lines.append(obj)

    def remove_red_lines(self, *red_lines):
        for obj in red_lines:
            if self in obj._locations:
                obj._locations.remove(self)
            self._red_lines.remove(obj)
    # >>> red_lines

    # <<< gml_observatins
    # @generated
    def get_gml_observatins(self):
        """ 
        """
        return self._gml_observatins

    def set_gml_observatins(self, value):
        for p in self._gml_observatins:
            filtered = [q for q in p.locations if q != self]
            self._gml_observatins._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._gml_observatins = value

    gml_observatins = property(get_gml_observatins, set_gml_observatins)

    def add_gml_observatins(self, *gml_observatins):
        for obj in gml_observatins:
            if self not in obj._locations:
                obj._locations.append(self)
            self._gml_observatins.append(obj)

    def remove_gml_observatins(self, *gml_observatins):
        for obj in gml_observatins:
            if self in obj._locations:
                obj._locations.remove(self)
            self._gml_observatins.remove(obj)
    # >>> gml_observatins

    # <<< hazards
    # @generated
    def get_hazards(self):
        """ 
        """
        return self._hazards

    def set_hazards(self, value):
        for p in self._hazards:
            filtered = [q for q in p.locations if q != self]
            self._hazards._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._hazards = value

    hazards = property(get_hazards, set_hazards)

    def add_hazards(self, *hazards):
        for obj in hazards:
            if self not in obj._locations:
                obj._locations.append(self)
            self._hazards.append(obj)

    def remove_hazards(self, *hazards):
        for obj in hazards:
            if self in obj._locations:
                obj._locations.remove(self)
            self._hazards.remove(obj)
    # >>> hazards

    # <<< activity_records
    # @generated
    def get_activity_records(self):
        """ 
        """
        return self._activity_records

    def set_activity_records(self, value):
        for p in self._activity_records:
            filtered = [q for q in p.locations if q != self]
            self._activity_records._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._activity_records = value

    activity_records = property(get_activity_records, set_activity_records)

    def add_activity_records(self, *activity_records):
        for obj in activity_records:
            if self not in obj._locations:
                obj._locations.append(self)
            self._activity_records.append(obj)

    def remove_activity_records(self, *activity_records):
        for obj in activity_records:
            if self in obj._locations:
                obj._locations.remove(self)
            self._activity_records.remove(obj)
    # >>> activity_records


    def __str__(self):
        """ Returns a string representation of the Location.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Location.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Location", self.uri)
        if format:
            indent += ' ' * depth

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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Location")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> location.serialize


class StreetAddress(Element):
    """ General purpose street address information.
    """
    # <<< street_address
    # @generated
    def __init__(self, status=None, town_detail=None, street_detail=None, **kw_args):
        """ Initialises a new 'StreetAddress' instance.
        """

        self.status = status

        self.town_detail = town_detail

        self.street_detail = street_detail


        super(StreetAddress, self).__init__(**kw_args)
    # >>> street_address

    # <<< status
    # @generated
    # Status of this address.
    status = None
    # >>> status

    # <<< town_detail
    # @generated
    # Town detail.
    town_detail = None
    # >>> town_detail

    # <<< street_detail
    # @generated
    # Street detail.
    street_detail = None
    # >>> street_detail


    def __str__(self):
        """ Returns a string representation of the StreetAddress.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< street_address.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StreetAddress.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StreetAddress", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:StreetAddress.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.town_detail is not None:
            s += '%s<%s:StreetAddress.town_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.town_detail.uri)
        if self.street_detail is not None:
            s += '%s<%s:StreetAddress.street_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.street_detail.uri)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StreetAddress")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> street_address.serialize


class TelephoneNumber(IdentifiedObject):
    """ Telephone number.
    """
    # <<< telephone_number
    # @generated
    def __init__(self, city_code='', country_code='', extension='', area_code='', local_number='', organisation=None, location=None, **kw_args):
        """ Initialises a new 'TelephoneNumber' instance.
        """
        # (if applicable) City code. 
        self.city_code = city_code

        # Country code. 
        self.country_code = country_code

        # (if applicable) Extension for this telephone number. 
        self.extension = extension

        # Area or region code. 
        self.area_code = area_code

        # Main (local) part of this telephone number. 
        self.local_number = local_number


        self._organisation = None
        self.organisation = organisation

        self._location = None
        self.location = location


        super(TelephoneNumber, self).__init__(**kw_args)
    # >>> telephone_number

    # <<< organisation
    # @generated
    def get_organisation(self):
        """ Organisation owning this telephone number.
        """
        return self._organisation

    def set_organisation(self, value):
        if self._organisation is not None:
            filtered = [x for x in self.organisation.telephone_numbers if x != self]
            self._organisation._telephone_numbers = filtered

        self._organisation = value
        if self._organisation is not None:
            self._organisation._telephone_numbers.append(self)

    organisation = property(get_organisation, set_organisation)
    # >>> organisation

    # <<< location
    # @generated
    def get_location(self):
        """ Location owning this telephone number.
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.telephone_numbers if x != self]
            self._location._telephone_numbers = filtered

        self._location = value
        if self._location is not None:
            self._location._telephone_numbers.append(self)

    location = property(get_location, set_location)
    # >>> location


    def __str__(self):
        """ Returns a string representation of the TelephoneNumber.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< telephone_number.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TelephoneNumber.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TelephoneNumber", self.uri)
        if format:
            indent += ' ' * depth

        if self.organisation is not None:
            s += '%s<%s:TelephoneNumber.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        if self.location is not None:
            s += '%s<%s:TelephoneNumber.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        s += '%s<%s:TelephoneNumber.city_code>%s</%s:TelephoneNumber.city_code>' % \
            (indent, ns_prefix, self.city_code, ns_prefix)
        s += '%s<%s:TelephoneNumber.country_code>%s</%s:TelephoneNumber.country_code>' % \
            (indent, ns_prefix, self.country_code, ns_prefix)
        s += '%s<%s:TelephoneNumber.extension>%s</%s:TelephoneNumber.extension>' % \
            (indent, ns_prefix, self.extension, ns_prefix)
        s += '%s<%s:TelephoneNumber.area_code>%s</%s:TelephoneNumber.area_code>' % \
            (indent, ns_prefix, self.area_code, ns_prefix)
        s += '%s<%s:TelephoneNumber.local_number>%s</%s:TelephoneNumber.local_number>' % \
            (indent, ns_prefix, self.local_number, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TelephoneNumber")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> telephone_number.serialize


class DateTimeInterval(Element):
    """ Interval of date and time.
    """
    # <<< date_time_interval
    # @generated
    def __init__(self, end='', start='', **kw_args):
        """ Initialises a new 'DateTimeInterval' instance.
        """
        # Date and time that this interval ended. 
        self.end = end

        # Date and time that this interval started. 
        self.start = start



        super(DateTimeInterval, self).__init__(**kw_args)
    # >>> date_time_interval


    def __str__(self):
        """ Returns a string representation of the DateTimeInterval.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< date_time_interval.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DateTimeInterval.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DateTimeInterval", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:DateTimeInterval.end>%s</%s:DateTimeInterval.end>' % \
            (indent, ns_prefix, self.end, ns_prefix)
        s += '%s<%s:DateTimeInterval.start>%s</%s:DateTimeInterval.start>' % \
            (indent, ns_prefix, self.start, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DateTimeInterval")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> date_time_interval.serialize


class PostalAddress(Element):
    """ General purpose postal address information.
    """
    # <<< postal_address
    # @generated
    def __init__(self, po_box='', postal_code='', street_detail=None, town_detail=None, **kw_args):
        """ Initialises a new 'PostalAddress' instance.
        """
        # Post office box. 
        self.po_box = po_box

        # Postal code for the address. 
        self.postal_code = postal_code


        self.street_detail = street_detail

        self.town_detail = town_detail


        super(PostalAddress, self).__init__(**kw_args)
    # >>> postal_address

    # <<< street_detail
    # @generated
    # Street detail.
    street_detail = None
    # >>> street_detail

    # <<< town_detail
    # @generated
    # Town detail.
    town_detail = None
    # >>> town_detail


    def __str__(self):
        """ Returns a string representation of the PostalAddress.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< postal_address.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PostalAddress.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PostalAddress", self.uri)
        if format:
            indent += ' ' * depth

        if self.street_detail is not None:
            s += '%s<%s:PostalAddress.street_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.street_detail.uri)
        if self.town_detail is not None:
            s += '%s<%s:PostalAddress.town_detail rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.town_detail.uri)
        s += '%s<%s:PostalAddress.po_box>%s</%s:PostalAddress.po_box>' % \
            (indent, ns_prefix, self.po_box, ns_prefix)
        s += '%s<%s:PostalAddress.postal_code>%s</%s:PostalAddress.postal_code>' % \
            (indent, ns_prefix, self.postal_code, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PostalAddress")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> postal_address.serialize


class TownDetail(Element):
    """ Town details, in the context of address.
    """
    # <<< town_detail
    # @generated
    def __init__(self, state_or_province='', code='', name='', section='', country='', **kw_args):
        """ Initialises a new 'TownDetail' instance.
        """
        # Name of the state or province. 
        self.state_or_province = state_or_province

        # Town code. 
        self.code = code

        # Town name. 
        self.name = name

        # Town section. For example, it is common for there to be 36 sections per township. 
        self.section = section

        # Name of the country. 
        self.country = country



        super(TownDetail, self).__init__(**kw_args)
    # >>> town_detail


    def __str__(self):
        """ Returns a string representation of the TownDetail.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< town_detail.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TownDetail.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TownDetail", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:TownDetail.state_or_province>%s</%s:TownDetail.state_or_province>' % \
            (indent, ns_prefix, self.state_or_province, ns_prefix)
        s += '%s<%s:TownDetail.code>%s</%s:TownDetail.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:TownDetail.name>%s</%s:TownDetail.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:TownDetail.section>%s</%s:TownDetail.section>' % \
            (indent, ns_prefix, self.section, ns_prefix)
        s += '%s<%s:TownDetail.country>%s</%s:TownDetail.country>' % \
            (indent, ns_prefix, self.country, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TownDetail")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> town_detail.serialize


class ElectronicAddress(IdentifiedObject):
    """ Electronic address information.
    """
    # <<< electronic_address
    # @generated
    def __init__(self, web='', email='', password='', lan='', user_id='', radio='', erp_telephone_numbers=None, locations=None, cashier=None, erp_person=None, asset=None, status=None, document=None, organisation=None, **kw_args):
        """ Initialises a new 'ElectronicAddress' instance.
        """
        # World Wide Web address. 
        self.web = web

        # Email address. 
        self.email = email

        # Password needed to log in. 
        self.password = password

        # Address on local area network. 
        self.lan = lan

        # User ID needed to log in, which can be for an individual person, an organisation, a location, etc. 
        self.user_id = user_id

        # Radio address. 
        self.radio = radio


        self._erp_telephone_numbers = []
        if erp_telephone_numbers is not None:
            self.erp_telephone_numbers = erp_telephone_numbers
        else:
            self.erp_telephone_numbers = []

        self._locations = []
        if locations is not None:
            self.locations = locations
        else:
            self.locations = []

        self._cashier = None
        self.cashier = cashier

        self._erp_person = None
        self.erp_person = erp_person

        self._asset = None
        self.asset = asset

        self.status = status

        self._document = None
        self.document = document

        self._organisation = None
        self.organisation = organisation


        super(ElectronicAddress, self).__init__(**kw_args)
    # >>> electronic_address

    # <<< erp_telephone_numbers
    # @generated
    def get_erp_telephone_numbers(self):
        """ 
        """
        return self._erp_telephone_numbers

    def set_erp_telephone_numbers(self, value):
        for x in self._erp_telephone_numbers:
            x._electronic_address = None
        for y in value:
            y._electronic_address = self
        self._erp_telephone_numbers = value

    erp_telephone_numbers = property(get_erp_telephone_numbers, set_erp_telephone_numbers)

    def add_erp_telephone_numbers(self, *erp_telephone_numbers):
        for obj in erp_telephone_numbers:
            obj._electronic_address = self
            self._erp_telephone_numbers.append(obj)

    def remove_erp_telephone_numbers(self, *erp_telephone_numbers):
        for obj in erp_telephone_numbers:
            obj._electronic_address = None
            self._erp_telephone_numbers.remove(obj)
    # >>> erp_telephone_numbers

    # <<< locations
    # @generated
    def get_locations(self):
        """ All locations having this electronic address.
        """
        return self._locations

    def set_locations(self, value):
        for p in self._locations:
            filtered = [q for q in p.electronic_addresses if q != self]
            self._locations._electronic_addresses = filtered
        for r in value:
            if self not in r._electronic_addresses:
                r._electronic_addresses.append(self)
        self._locations = value

    locations = property(get_locations, set_locations)

    def add_locations(self, *locations):
        for obj in locations:
            if self not in obj._electronic_addresses:
                obj._electronic_addresses.append(self)
            self._locations.append(obj)

    def remove_locations(self, *locations):
        for obj in locations:
            if self in obj._electronic_addresses:
                obj._electronic_addresses.remove(self)
            self._locations.remove(obj)
    # >>> locations

    # <<< cashier
    # @generated
    def get_cashier(self):
        """ 
        """
        return self._cashier

    def set_cashier(self, value):
        if self._cashier is not None:
            filtered = [x for x in self.cashier.electronic_addresses if x != self]
            self._cashier._electronic_addresses = filtered

        self._cashier = value
        if self._cashier is not None:
            self._cashier._electronic_addresses.append(self)

    cashier = property(get_cashier, set_cashier)
    # >>> cashier

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.electronic_addresses if x != self]
            self._erp_person._electronic_addresses = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._electronic_addresses.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person

    # <<< asset
    # @generated
    def get_asset(self):
        """ Asset owning this electronic address.
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.electronic_addresses if x != self]
            self._asset._electronic_addresses = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._electronic_addresses.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< status
    # @generated
    # Status of this electronic address.
    status = None
    # >>> status

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            self._document._electronic_address = None

        self._document = value
        if self._document is not None:
            self._document._electronic_address = self

    document = property(get_document, set_document)
    # >>> document

    # <<< organisation
    # @generated
    def get_organisation(self):
        """ Organisation owning this electronic address.
        """
        return self._organisation

    def set_organisation(self, value):
        if self._organisation is not None:
            filtered = [x for x in self.organisation.electronic_addresses if x != self]
            self._organisation._electronic_addresses = filtered

        self._organisation = value
        if self._organisation is not None:
            self._organisation._electronic_addresses.append(self)

    organisation = property(get_organisation, set_organisation)
    # >>> organisation


    def __str__(self):
        """ Returns a string representation of the ElectronicAddress.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< electronic_address.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ElectronicAddress.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ElectronicAddress", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_telephone_numbers:
            s += '%s<%s:ElectronicAddress.erp_telephone_numbers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.locations:
            s += '%s<%s:ElectronicAddress.locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.cashier is not None:
            s += '%s<%s:ElectronicAddress.cashier rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cashier.uri)
        if self.erp_person is not None:
            s += '%s<%s:ElectronicAddress.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        if self.asset is not None:
            s += '%s<%s:ElectronicAddress.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.status is not None:
            s += '%s<%s:ElectronicAddress.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.document is not None:
            s += '%s<%s:ElectronicAddress.document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.document.uri)
        if self.organisation is not None:
            s += '%s<%s:ElectronicAddress.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        s += '%s<%s:ElectronicAddress.web>%s</%s:ElectronicAddress.web>' % \
            (indent, ns_prefix, self.web, ns_prefix)
        s += '%s<%s:ElectronicAddress.email>%s</%s:ElectronicAddress.email>' % \
            (indent, ns_prefix, self.email, ns_prefix)
        s += '%s<%s:ElectronicAddress.password>%s</%s:ElectronicAddress.password>' % \
            (indent, ns_prefix, self.password, ns_prefix)
        s += '%s<%s:ElectronicAddress.lan>%s</%s:ElectronicAddress.lan>' % \
            (indent, ns_prefix, self.lan, ns_prefix)
        s += '%s<%s:ElectronicAddress.user_id>%s</%s:ElectronicAddress.user_id>' % \
            (indent, ns_prefix, self.user_id, ns_prefix)
        s += '%s<%s:ElectronicAddress.radio>%s</%s:ElectronicAddress.radio>' % \
            (indent, ns_prefix, self.radio, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ElectronicAddress")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> electronic_address.serialize


class TimePoint(IdentifiedObject):
    """ A point in time within a sequence of points in time relative to a TimeSchedule.
    """
    # <<< time_point
    # @generated
    def __init__(self, relative_time_interval=0.0, absolute_time='', sequence_number=0, window=None, scheduled_events=None, time_schedule=None, status=None, **kw_args):
        """ Initialises a new 'TimePoint' instance.
        """
        # (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'. 
        self.relative_time_interval = relative_time_interval

        # Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived. 
        self.absolute_time = absolute_time

        # (if sequence-based) Relative sequence number for this time point. 
        self.sequence_number = sequence_number


        self.window = window

        self._scheduled_events = []
        if scheduled_events is not None:
            self.scheduled_events = scheduled_events
        else:
            self.scheduled_events = []

        self._time_schedule = None
        self.time_schedule = time_schedule

        self.status = status


        super(TimePoint, self).__init__(**kw_args)
    # >>> time_point

    # <<< window
    # @generated
    # Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
    window = None
    # >>> window

    # <<< scheduled_events
    # @generated
    def get_scheduled_events(self):
        """ 
        """
        return self._scheduled_events

    def set_scheduled_events(self, value):
        for x in self._scheduled_events:
            x._time_point = None
        for y in value:
            y._time_point = self
        self._scheduled_events = value

    scheduled_events = property(get_scheduled_events, set_scheduled_events)

    def add_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._time_point = self
            self._scheduled_events.append(obj)

    def remove_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._time_point = None
            self._scheduled_events.remove(obj)
    # >>> scheduled_events

    # <<< time_schedule
    # @generated
    def get_time_schedule(self):
        """ Time schedule owning this time point.
        """
        return self._time_schedule

    def set_time_schedule(self, value):
        if self._time_schedule is not None:
            filtered = [x for x in self.time_schedule.time_points if x != self]
            self._time_schedule._time_points = filtered

        self._time_schedule = value
        if self._time_schedule is not None:
            self._time_schedule._time_points.append(self)

    time_schedule = property(get_time_schedule, set_time_schedule)
    # >>> time_schedule

    # <<< status
    # @generated
    # Status of this time point.
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the TimePoint.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< time_point.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TimePoint.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TimePoint", self.uri)
        if format:
            indent += ' ' * depth

        if self.window is not None:
            s += '%s<%s:TimePoint.window rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.window.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:TimePoint.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.time_schedule is not None:
            s += '%s<%s:TimePoint.time_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.time_schedule.uri)
        if self.status is not None:
            s += '%s<%s:TimePoint.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:TimePoint.relative_time_interval>%s</%s:TimePoint.relative_time_interval>' % \
            (indent, ns_prefix, self.relative_time_interval, ns_prefix)
        s += '%s<%s:TimePoint.absolute_time>%s</%s:TimePoint.absolute_time>' % \
            (indent, ns_prefix, self.absolute_time, ns_prefix)
        s += '%s<%s:TimePoint.sequence_number>%s</%s:TimePoint.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TimePoint")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> time_point.serialize


class UserAttribute(Element):
    """ Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """
    # <<< user_attribute
    # @generated
    def __init__(self, sequence_number=0, value='', name='', property_specification=None, rating_specification=None, property_assets=None, rating_assets=None, erp_ledger_entries=None, procedure_data_sets=None, transaction=None, procedure=None, pass_through_bills=None, erp_invoice_line_items=None, bill_determinants=None, erp_statement_line_items=None, **kw_args):
        """ Initialises a new 'UserAttribute' instance.
        """
        # Sequence number for this attribute in a list of attributes. 
        self.sequence_number = sequence_number

        # Value of an attribute, including unit information. 
        self.value = value

        # Name of an attribute. 
        self.name = name


        self._property_specification = None
        self.property_specification = property_specification

        self._rating_specification = None
        self.rating_specification = rating_specification

        self._property_assets = []
        if property_assets is not None:
            self.property_assets = property_assets
        else:
            self.property_assets = []

        self._rating_assets = []
        if rating_assets is not None:
            self.rating_assets = rating_assets
        else:
            self.rating_assets = []

        self._erp_ledger_entries = []
        if erp_ledger_entries is not None:
            self.erp_ledger_entries = erp_ledger_entries
        else:
            self.erp_ledger_entries = []

        self._procedure_data_sets = []
        if procedure_data_sets is not None:
            self.procedure_data_sets = procedure_data_sets
        else:
            self.procedure_data_sets = []

        self._transaction = None
        self.transaction = transaction

        self._procedure = None
        self.procedure = procedure

        self._pass_through_bills = []
        if pass_through_bills is not None:
            self.pass_through_bills = pass_through_bills
        else:
            self.pass_through_bills = []

        self._erp_invoice_line_items = []
        if erp_invoice_line_items is not None:
            self.erp_invoice_line_items = erp_invoice_line_items
        else:
            self.erp_invoice_line_items = []

        self._bill_determinants = []
        if bill_determinants is not None:
            self.bill_determinants = bill_determinants
        else:
            self.bill_determinants = []

        self._erp_statement_line_items = []
        if erp_statement_line_items is not None:
            self.erp_statement_line_items = erp_statement_line_items
        else:
            self.erp_statement_line_items = []


        super(UserAttribute, self).__init__(**kw_args)
    # >>> user_attribute

    # <<< property_specification
    # @generated
    def get_property_specification(self):
        """ 
        """
        return self._property_specification

    def set_property_specification(self, value):
        if self._property_specification is not None:
            filtered = [x for x in self.property_specification.asset_properites if x != self]
            self._property_specification._asset_properites = filtered

        self._property_specification = value
        if self._property_specification is not None:
            self._property_specification._asset_properites.append(self)

    property_specification = property(get_property_specification, set_property_specification)
    # >>> property_specification

    # <<< rating_specification
    # @generated
    def get_rating_specification(self):
        """ 
        """
        return self._rating_specification

    def set_rating_specification(self, value):
        if self._rating_specification is not None:
            filtered = [x for x in self.rating_specification.ratings if x != self]
            self._rating_specification._ratings = filtered

        self._rating_specification = value
        if self._rating_specification is not None:
            self._rating_specification._ratings.append(self)

    rating_specification = property(get_rating_specification, set_rating_specification)
    # >>> rating_specification

    # <<< property_assets
    # @generated
    def get_property_assets(self):
        """ 
        """
        return self._property_assets

    def set_property_assets(self, value):
        for p in self._property_assets:
            filtered = [q for q in p.properties if q != self]
            self._property_assets._properties = filtered
        for r in value:
            if self not in r._properties:
                r._properties.append(self)
        self._property_assets = value

    property_assets = property(get_property_assets, set_property_assets)

    def add_property_assets(self, *property_assets):
        for obj in property_assets:
            if self not in obj._properties:
                obj._properties.append(self)
            self._property_assets.append(obj)

    def remove_property_assets(self, *property_assets):
        for obj in property_assets:
            if self in obj._properties:
                obj._properties.remove(self)
            self._property_assets.remove(obj)
    # >>> property_assets

    # <<< rating_assets
    # @generated
    def get_rating_assets(self):
        """ 
        """
        return self._rating_assets

    def set_rating_assets(self, value):
        for p in self._rating_assets:
            filtered = [q for q in p.ratings if q != self]
            self._rating_assets._ratings = filtered
        for r in value:
            if self not in r._ratings:
                r._ratings.append(self)
        self._rating_assets = value

    rating_assets = property(get_rating_assets, set_rating_assets)

    def add_rating_assets(self, *rating_assets):
        for obj in rating_assets:
            if self not in obj._ratings:
                obj._ratings.append(self)
            self._rating_assets.append(obj)

    def remove_rating_assets(self, *rating_assets):
        for obj in rating_assets:
            if self in obj._ratings:
                obj._ratings.remove(self)
            self._rating_assets.remove(obj)
    # >>> rating_assets

    # <<< erp_ledger_entries
    # @generated
    def get_erp_ledger_entries(self):
        """ 
        """
        return self._erp_ledger_entries

    def set_erp_ledger_entries(self, value):
        for p in self._erp_ledger_entries:
            filtered = [q for q in p.user_attributes if q != self]
            self._erp_ledger_entries._user_attributes = filtered
        for r in value:
            if self not in r._user_attributes:
                r._user_attributes.append(self)
        self._erp_ledger_entries = value

    erp_ledger_entries = property(get_erp_ledger_entries, set_erp_ledger_entries)

    def add_erp_ledger_entries(self, *erp_ledger_entries):
        for obj in erp_ledger_entries:
            if self not in obj._user_attributes:
                obj._user_attributes.append(self)
            self._erp_ledger_entries.append(obj)

    def remove_erp_ledger_entries(self, *erp_ledger_entries):
        for obj in erp_ledger_entries:
            if self in obj._user_attributes:
                obj._user_attributes.remove(self)
            self._erp_ledger_entries.remove(obj)
    # >>> erp_ledger_entries

    # <<< procedure_data_sets
    # @generated
    def get_procedure_data_sets(self):
        """ 
        """
        return self._procedure_data_sets

    def set_procedure_data_sets(self, value):
        for p in self._procedure_data_sets:
            filtered = [q for q in p.properties if q != self]
            self._procedure_data_sets._properties = filtered
        for r in value:
            if self not in r._properties:
                r._properties.append(self)
        self._procedure_data_sets = value

    procedure_data_sets = property(get_procedure_data_sets, set_procedure_data_sets)

    def add_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            if self not in obj._properties:
                obj._properties.append(self)
            self._procedure_data_sets.append(obj)

    def remove_procedure_data_sets(self, *procedure_data_sets):
        for obj in procedure_data_sets:
            if self in obj._properties:
                obj._properties.remove(self)
            self._procedure_data_sets.remove(obj)
    # >>> procedure_data_sets

    # <<< transaction
    # @generated
    def get_transaction(self):
        """ Transaction for which this snapshot has been recorded.
        """
        return self._transaction

    def set_transaction(self, value):
        if self._transaction is not None:
            filtered = [x for x in self.transaction.user_attributes if x != self]
            self._transaction._user_attributes = filtered

        self._transaction = value
        if self._transaction is not None:
            self._transaction._user_attributes.append(self)

    transaction = property(get_transaction, set_transaction)
    # >>> transaction

    # <<< procedure
    # @generated
    def get_procedure(self):
        """ 
        """
        return self._procedure

    def set_procedure(self, value):
        if self._procedure is not None:
            filtered = [x for x in self.procedure.procedure_values if x != self]
            self._procedure._procedure_values = filtered

        self._procedure = value
        if self._procedure is not None:
            self._procedure._procedure_values.append(self)

    procedure = property(get_procedure, set_procedure)
    # >>> procedure

    # <<< pass_through_bills
    # @generated
    def get_pass_through_bills(self):
        """ 
        """
        return self._pass_through_bills

    def set_pass_through_bills(self, value):
        for p in self._pass_through_bills:
            filtered = [q for q in p.user_attributes if q != self]
            self._pass_through_bills._user_attributes = filtered
        for r in value:
            if self not in r._user_attributes:
                r._user_attributes.append(self)
        self._pass_through_bills = value

    pass_through_bills = property(get_pass_through_bills, set_pass_through_bills)

    def add_pass_through_bills(self, *pass_through_bills):
        for obj in pass_through_bills:
            if self not in obj._user_attributes:
                obj._user_attributes.append(self)
            self._pass_through_bills.append(obj)

    def remove_pass_through_bills(self, *pass_through_bills):
        for obj in pass_through_bills:
            if self in obj._user_attributes:
                obj._user_attributes.remove(self)
            self._pass_through_bills.remove(obj)
    # >>> pass_through_bills

    # <<< erp_invoice_line_items
    # @generated
    def get_erp_invoice_line_items(self):
        """ 
        """
        return self._erp_invoice_line_items

    def set_erp_invoice_line_items(self, value):
        for p in self._erp_invoice_line_items:
            filtered = [q for q in p.user_attributes if q != self]
            self._erp_invoice_line_items._user_attributes = filtered
        for r in value:
            if self not in r._user_attributes:
                r._user_attributes.append(self)
        self._erp_invoice_line_items = value

    erp_invoice_line_items = property(get_erp_invoice_line_items, set_erp_invoice_line_items)

    def add_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self not in obj._user_attributes:
                obj._user_attributes.append(self)
            self._erp_invoice_line_items.append(obj)

    def remove_erp_invoice_line_items(self, *erp_invoice_line_items):
        for obj in erp_invoice_line_items:
            if self in obj._user_attributes:
                obj._user_attributes.remove(self)
            self._erp_invoice_line_items.remove(obj)
    # >>> erp_invoice_line_items

    # <<< bill_determinants
    # @generated
    def get_bill_determinants(self):
        """ 
        """
        return self._bill_determinants

    def set_bill_determinants(self, value):
        for p in self._bill_determinants:
            filtered = [q for q in p.user_attributes if q != self]
            self._bill_determinants._user_attributes = filtered
        for r in value:
            if self not in r._user_attributes:
                r._user_attributes.append(self)
        self._bill_determinants = value

    bill_determinants = property(get_bill_determinants, set_bill_determinants)

    def add_bill_determinants(self, *bill_determinants):
        for obj in bill_determinants:
            if self not in obj._user_attributes:
                obj._user_attributes.append(self)
            self._bill_determinants.append(obj)

    def remove_bill_determinants(self, *bill_determinants):
        for obj in bill_determinants:
            if self in obj._user_attributes:
                obj._user_attributes.remove(self)
            self._bill_determinants.remove(obj)
    # >>> bill_determinants

    # <<< erp_statement_line_items
    # @generated
    def get_erp_statement_line_items(self):
        """ 
        """
        return self._erp_statement_line_items

    def set_erp_statement_line_items(self, value):
        for p in self._erp_statement_line_items:
            filtered = [q for q in p.user_attributes if q != self]
            self._erp_statement_line_items._user_attributes = filtered
        for r in value:
            if self not in r._user_attributes:
                r._user_attributes.append(self)
        self._erp_statement_line_items = value

    erp_statement_line_items = property(get_erp_statement_line_items, set_erp_statement_line_items)

    def add_erp_statement_line_items(self, *erp_statement_line_items):
        for obj in erp_statement_line_items:
            if self not in obj._user_attributes:
                obj._user_attributes.append(self)
            self._erp_statement_line_items.append(obj)

    def remove_erp_statement_line_items(self, *erp_statement_line_items):
        for obj in erp_statement_line_items:
            if self in obj._user_attributes:
                obj._user_attributes.remove(self)
            self._erp_statement_line_items.remove(obj)
    # >>> erp_statement_line_items


    def __str__(self):
        """ Returns a string representation of the UserAttribute.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< user_attribute.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the UserAttribute.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "UserAttribute", self.uri)
        if format:
            indent += ' ' * depth

        if self.property_specification is not None:
            s += '%s<%s:UserAttribute.property_specification rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.property_specification.uri)
        if self.rating_specification is not None:
            s += '%s<%s:UserAttribute.rating_specification rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.rating_specification.uri)
        for obj in self.property_assets:
            s += '%s<%s:UserAttribute.property_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.rating_assets:
            s += '%s<%s:UserAttribute.rating_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_ledger_entries:
            s += '%s<%s:UserAttribute.erp_ledger_entries rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.procedure_data_sets:
            s += '%s<%s:UserAttribute.procedure_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.transaction is not None:
            s += '%s<%s:UserAttribute.transaction rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transaction.uri)
        if self.procedure is not None:
            s += '%s<%s:UserAttribute.procedure rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.procedure.uri)
        for obj in self.pass_through_bills:
            s += '%s<%s:UserAttribute.pass_through_bills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_invoice_line_items:
            s += '%s<%s:UserAttribute.erp_invoice_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.bill_determinants:
            s += '%s<%s:UserAttribute.bill_determinants rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_statement_line_items:
            s += '%s<%s:UserAttribute.erp_statement_line_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:UserAttribute.sequence_number>%s</%s:UserAttribute.sequence_number>' % \
            (indent, ns_prefix, self.sequence_number, ns_prefix)
        s += '%s<%s:UserAttribute.value>%s</%s:UserAttribute.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:UserAttribute.name>%s</%s:UserAttribute.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "UserAttribute")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> user_attribute.serialize


class Status(Element):
    """ Current status information relevant to an entity.
    """
    # <<< status
    # @generated
    def __init__(self, date_time='', reason='', value='', remark='', **kw_args):
        """ Initialises a new 'Status' instance.
        """
        # Date and time for which status 'value' applies. 
        self.date_time = date_time

        # Reason code or explanation for why an object went to the current status 'value'. 
        self.reason = reason

        # Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies. 
        self.value = value

        # Pertinent information regarding the current 'value', as free form text. 
        self.remark = remark



        super(Status, self).__init__(**kw_args)
    # >>> status


    def __str__(self):
        """ Returns a string representation of the Status.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< status.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Status.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Status", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Status.date_time>%s</%s:Status.date_time>' % \
            (indent, ns_prefix, self.date_time, ns_prefix)
        s += '%s<%s:Status.reason>%s</%s:Status.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:Status.value>%s</%s:Status.value>' % \
            (indent, ns_prefix, self.value, ns_prefix)
        s += '%s<%s:Status.remark>%s</%s:Status.remark>' % \
            (indent, ns_prefix, self.remark, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Status")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> status.serialize


class StreetDetail(Element):
    """ Street details, in the context of address.
    """
    # <<< street_detail
    # @generated
    def __init__(self, building_name='', type='', name='', within_town_limits=False, number='', suffix='', prefix='', code='', address_general='', suite_number='', **kw_args):
        """ Initialises a new 'StreetDetail' instance.
        """
        # (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. 
        self.building_name = building_name

        # Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. 
        self.type = type

        # Name of the street. 
        self.name = name

        # True if this street is within the legal geographical boundaries of the specified town (default). 
        self.within_town_limits = within_town_limits

        # Designator of the specific location on the street. 
        self.number = number

        # Suffix to the street name. For example: North, South, East, West. 
        self.suffix = suffix

        # Prefix to the street name. For example: North, South, East, West. 
        self.prefix = prefix

        # (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. 
        self.code = code

        # Additional address information, for example a mailstop. 
        self.address_general = address_general

        # Number of the apartment or suite. 
        self.suite_number = suite_number



        super(StreetDetail, self).__init__(**kw_args)
    # >>> street_detail


    def __str__(self):
        """ Returns a string representation of the StreetDetail.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< street_detail.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StreetDetail.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StreetDetail", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:StreetDetail.building_name>%s</%s:StreetDetail.building_name>' % \
            (indent, ns_prefix, self.building_name, ns_prefix)
        s += '%s<%s:StreetDetail.type>%s</%s:StreetDetail.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:StreetDetail.name>%s</%s:StreetDetail.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:StreetDetail.within_town_limits>%s</%s:StreetDetail.within_town_limits>' % \
            (indent, ns_prefix, self.within_town_limits, ns_prefix)
        s += '%s<%s:StreetDetail.number>%s</%s:StreetDetail.number>' % \
            (indent, ns_prefix, self.number, ns_prefix)
        s += '%s<%s:StreetDetail.suffix>%s</%s:StreetDetail.suffix>' % \
            (indent, ns_prefix, self.suffix, ns_prefix)
        s += '%s<%s:StreetDetail.prefix>%s</%s:StreetDetail.prefix>' % \
            (indent, ns_prefix, self.prefix, ns_prefix)
        s += '%s<%s:StreetDetail.code>%s</%s:StreetDetail.code>' % \
            (indent, ns_prefix, self.code, ns_prefix)
        s += '%s<%s:StreetDetail.address_general>%s</%s:StreetDetail.address_general>' % \
            (indent, ns_prefix, self.address_general, ns_prefix)
        s += '%s<%s:StreetDetail.suite_number>%s</%s:StreetDetail.suite_number>' % \
            (indent, ns_prefix, self.suite_number, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StreetDetail")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> street_detail.serialize


class Agreement(Document):
    """ Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.
    """
    # <<< agreement
    # @generated
    def __init__(self, sign_date='', validity_interval=None, **kw_args):
        """ Initialises a new 'Agreement' instance.
        """
        # Date this agreement was consummated among associated persons and/or organisations. 
        self.sign_date = sign_date


        self.validity_interval = validity_interval


        super(Agreement, self).__init__(**kw_args)
    # >>> agreement

    # <<< validity_interval
    # @generated
    # Date and time interval this agreement is valid (from going into effect to termination).
    validity_interval = None
    # >>> validity_interval


    def __str__(self):
        """ Returns a string representation of the Agreement.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< agreement.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Agreement.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Agreement", self.uri)
        if format:
            indent += ' ' * depth

        if self.validity_interval is not None:
            s += '%s<%s:Agreement.validity_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.validity_interval.uri)
        s += '%s<%s:Agreement.sign_date>%s</%s:Agreement.sign_date>' % \
            (indent, ns_prefix, self.sign_date, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Agreement")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> agreement.serialize


class TimeSchedule(Document):
    """ Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).
    """
    # <<< time_schedule
    # @generated
    def __init__(self, disabled=False, offset=0.0, recurrence_pattern='', recurrence_period=0.0, time_points=None, schedule_interval=None, **kw_args):
        """ Initialises a new 'TimeSchedule' instance.
        """
        # True if this schedule is deactivated (disabled). 
        self.disabled = disabled

        # The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour. 
        self.offset = offset

        # Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.). 
        self.recurrence_pattern = recurrence_pattern

        # Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min). 
        self.recurrence_period = recurrence_period


        self._time_points = []
        if time_points is not None:
            self.time_points = time_points
        else:
            self.time_points = []

        self.schedule_interval = schedule_interval


        super(TimeSchedule, self).__init__(**kw_args)
    # >>> time_schedule

    # <<< time_points
    # @generated
    def get_time_points(self):
        """ Sequence of time points belonging to this time schedule.
        """
        return self._time_points

    def set_time_points(self, value):
        for x in self._time_points:
            x._time_schedule = None
        for y in value:
            y._time_schedule = self
        self._time_points = value

    time_points = property(get_time_points, set_time_points)

    def add_time_points(self, *time_points):
        for obj in time_points:
            obj._time_schedule = self
            self._time_points.append(obj)

    def remove_time_points(self, *time_points):
        for obj in time_points:
            obj._time_schedule = None
            self._time_points.remove(obj)
    # >>> time_points

    # <<< schedule_interval
    # @generated
    # Schedule date and time interval.
    schedule_interval = None
    # >>> schedule_interval


    def __str__(self):
        """ Returns a string representation of the TimeSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< time_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TimeSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TimeSchedule", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.time_points:
            s += '%s<%s:TimeSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.schedule_interval is not None:
            s += '%s<%s:TimeSchedule.schedule_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.schedule_interval.uri)
        s += '%s<%s:TimeSchedule.disabled>%s</%s:TimeSchedule.disabled>' % \
            (indent, ns_prefix, self.disabled, ns_prefix)
        s += '%s<%s:TimeSchedule.offset>%s</%s:TimeSchedule.offset>' % \
            (indent, ns_prefix, self.offset, ns_prefix)
        s += '%s<%s:TimeSchedule.recurrence_pattern>%s</%s:TimeSchedule.recurrence_pattern>' % \
            (indent, ns_prefix, self.recurrence_pattern, ns_prefix)
        s += '%s<%s:TimeSchedule.recurrence_period>%s</%s:TimeSchedule.recurrence_period>' % \
            (indent, ns_prefix, self.recurrence_period, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TimeSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> time_schedule.serialize


class GeoLocation(Location):
    """ Geographical location.
    """
    # <<< geo_location
    # @generated
    def __init__(self, power_system_resources=None, **kw_args):
        """ Initialises a new 'GeoLocation' instance.
        """

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(GeoLocation, self).__init__(**kw_args)
    # >>> geo_location

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ All power system resources at this geographical location.
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for x in self._power_system_resources:
            x._geo_location = None
        for y in value:
            y._geo_location = self
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._geo_location = self
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            obj._geo_location = None
            self._power_system_resources.remove(obj)
    # >>> power_system_resources


    def __str__(self):
        """ Returns a string representation of the GeoLocation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< geo_location.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeoLocation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeoLocation", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.power_system_resources:
            s += '%s<%s:GeoLocation.power_system_resources rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeoLocation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> geo_location.serialize


# <<< common
# @generated
# >>> common
