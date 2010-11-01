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

""" This package contains the information classes that support distribution management in general.
"""

from cim15v01.iec61970.core import IdentifiedObject
from cim15v01 import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimCommon"

ns_uri = "http://iec.ch/TC57/CIM-generic#Common"

class Organisation(IdentifiedObject):
    """ Organisation that might have roles as utility, contractor, supplier, manufacturer, customer, etc.
    """
    # <<< organisation
    # @generated
    def __init__(self, business_roles=None, street_address=None, market_roles=None, electronic_address=None, postal_address=None, phone2=None, phone1=None, *args, **kw_args):
        """ Initialises a new 'Organisation' instance.

        @param business_roles:
        @param street_address: Street address.
        @param market_roles:
        @param electronic_address: Electronic address.
        @param postal_address: Postal address, potentially different than 'streetAddress' (e.g., another city).
        @param phone2: Additional phone number.
        @param phone1: Phone number.
        """

        self._business_roles = []
        if business_roles is not None:
            self.business_roles = business_roles
        else:
            self.business_roles = []

        self.street_address = street_address

        self._market_roles = []
        if market_roles is not None:
            self.market_roles = market_roles
        else:
            self.market_roles = []

        self.electronic_address = electronic_address

        self.postal_address = postal_address

        self.phone2 = phone2

        self.phone1 = phone1


        super(Organisation, self).__init__(*args, **kw_args)
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

    # <<< electronic_address
    # @generated
    # Electronic address.
    electronic_address = None
    # >>> electronic_address

    # <<< postal_address
    # @generated
    # Postal address, potentially different than 'streetAddress' (e.g., another city).
    postal_address = None
    # >>> postal_address

    # <<< phone2
    # @generated
    # Additional phone number.
    phone2 = None
    # >>> phone2

    # <<< phone1
    # @generated
    # Phone number.
    phone1 = None
    # >>> phone1



class ActivityRecord(IdentifiedObject):
    """ Records activity for an entity at a point in time; activity may be for an event that has already occurred or for a planned activity.
    """
    # <<< activity_record
    # @generated
    def __init__(self, reason='', category='', severity='', created_date_time='', market_factors=None, documents=None, organisations=None, scheduled_event=None, assets=None, erp_persons=None, locations=None, status=None, *args, **kw_args):
        """ Initialises a new 'ActivityRecord' instance.

        @param reason: Reason for event resulting in this activity record, typically supplied when user initiated. 
        @param category: Category of event resulting in this activity record. 
        @param severity: Severity level of event resulting in this activity record. 
        @param created_date_time: Date and time this activity record has been created (different from the 'status.dateTime', which is the time of a status change of the associated object, if applicable). 
        @param market_factors:
        @param documents: All documents for which this activity record has been created.
        @param organisations:
        @param scheduled_event:
        @param assets: All assets for which this activity record has been created.
        @param erp_persons:
        @param locations:
        @param status: Information on consequence of event resulting in this activity record.
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


        super(ActivityRecord, self).__init__(*args, **kw_args)
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



class Document(IdentifiedObject):
    """ Parent class for different groupings of information collected and managed as a part of a business process. It will frequently contain references to other objects, such as assets, people and power system resources.
    """
    # <<< document
    # @generated
    def __init__(self, subject='', revision_number='', category='', last_modified_date_time='', title='', created_date_time='', activity_records=None, electronic_address=None, erp_organisation_roles=None, scheduled_events=None, from_document_roles=None, power_system_resource_roles=None, network_data_sets=None, erp_person_roles=None, change_items=None, measurements=None, doc_status=None, schedule_parameter_infos=None, to_document_roles=None, status=None, asset_roles=None, change_sets=None, *args, **kw_args):
        """ Initialises a new 'Document' instance.

        @param subject: Document subject. 
        @param revision_number: Revision number for this document. 
        @param category: Utility-specific categorisation of this document, according to their corporate standards, practices, and existing IT systems (e.g., for management of assets, maintenance, work, outage, customers, etc.). 
        @param last_modified_date_time: Date and time this document was last modified. Documents may potentially be modified many times during their lifetime. 
        @param title: Document title. 
        @param created_date_time: Date and time that this document was created. 
        @param activity_records: All activity records created for this document.
        @param electronic_address: Electronic address.
        @param erp_organisation_roles:
        @param scheduled_events:
        @param from_document_roles:
        @param power_system_resource_roles:
        @param network_data_sets:
        @param erp_person_roles:
        @param change_items:
        @param measurements: Measurements are specified in types of documents, such as procedures.
        @param doc_status: Status of this document. For status of subject matter this document represents (e.g., Agreement, Work), use 'status' attribute. Example values for 'docStatus.status' are draft, approved, cancelled, etc.
        @param schedule_parameter_infos:
        @param to_document_roles:
        @param status: Status of subject matter (e.g., Agreement, Work) this document represents. For status of the document itself, use 'docStatus' attribute.
        @param asset_roles:
        @param change_sets:
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

        self.electronic_address = electronic_address

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


        super(Document, self).__init__(*args, **kw_args)
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

    # <<< electronic_address
    # @generated
    # Electronic address.
    electronic_address = None
    # >>> electronic_address

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



class PositionPoint(Element):
    """ Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.
    """
    # <<< position_point
    # @generated
    def __init__(self, sequence_number=0, z_position='', x_position='', y_position='', location=None, *args, **kw_args):
        """ Initialises a new 'PositionPoint' instance.

        @param sequence_number: Zero-relative sequence number of this point within a series of points. 
        @param z_position: (if applicable) Z axis position. 
        @param x_position: X axis position. 
        @param y_position: Y axis position. 
        @param location: Location that this position point describes.
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


        super(PositionPoint, self).__init__(*args, **kw_args)
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



class Location(IdentifiedObject):
    """ The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.
    """
    # <<< location
    # @generated
    def __init__(self, is_polygon=False, position_points=None, *args, **kw_args):
        """ Initialises a new 'Location' instance.

        @param is_polygon: True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments. 
        @param position_points: Sequence of position points describing this location.
        """
        # True if the first and last point in the sequence of associated PositionPoints are to be connected, thus forming a polygon rather than merely a sequence of line segments. 
        self.is_polygon = is_polygon


        self._position_points = []
        if position_points is not None:
            self.position_points = position_points
        else:
            self.position_points = []


        super(Location, self).__init__(*args, **kw_args)
    # >>> location

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



class StreetAddress(Element):
    """ General purpose street address information.
    """
    # <<< street_address
    # @generated
    def __init__(self, status=None, town_detail=None, street_detail=None, *args, **kw_args):
        """ Initialises a new 'StreetAddress' instance.

        @param status: Status of this address.
        @param town_detail: Town detail.
        @param street_detail: Street detail.
        """

        self.status = status

        self.town_detail = town_detail

        self.street_detail = street_detail


        super(StreetAddress, self).__init__(*args, **kw_args)
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



class TelephoneNumber(Element):
    """ Telephone number.
    """
    # <<< telephone_number
    # @generated
    def __init__(self, city_code='', country_code='', extension='', area_code='', local_number='', *args, **kw_args):
        """ Initialises a new 'TelephoneNumber' instance.

        @param city_code: (if applicable) City code. 
        @param country_code: Country code. 
        @param extension: (if applicable) Extension for this telephone number. 
        @param area_code: Area or region code. 
        @param local_number: Main (local) part of this telephone number. 
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



        super(TelephoneNumber, self).__init__(*args, **kw_args)
    # >>> telephone_number



class DateTimeInterval(Element):
    """ Interval of date and time.
    """
    # <<< date_time_interval
    # @generated
    def __init__(self, end='', start='', *args, **kw_args):
        """ Initialises a new 'DateTimeInterval' instance.

        @param end: Date and time that this interval ended. 
        @param start: Date and time that this interval started. 
        """
        # Date and time that this interval ended. 
        self.end = end

        # Date and time that this interval started. 
        self.start = start



        super(DateTimeInterval, self).__init__(*args, **kw_args)
    # >>> date_time_interval



class PostalAddress(Element):
    """ General purpose postal address information.
    """
    # <<< postal_address
    # @generated
    def __init__(self, po_box='', postal_code='', street_detail=None, town_detail=None, *args, **kw_args):
        """ Initialises a new 'PostalAddress' instance.

        @param po_box: Post office box. 
        @param postal_code: Postal code for the address. 
        @param street_detail: Street detail.
        @param town_detail: Town detail.
        """
        # Post office box. 
        self.po_box = po_box

        # Postal code for the address. 
        self.postal_code = postal_code


        self.street_detail = street_detail

        self.town_detail = town_detail


        super(PostalAddress, self).__init__(*args, **kw_args)
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



class TownDetail(Element):
    """ Town details, in the context of address.
    """
    # <<< town_detail
    # @generated
    def __init__(self, state_or_province='', code='', name='', section='', country='', *args, **kw_args):
        """ Initialises a new 'TownDetail' instance.

        @param state_or_province: Name of the state or province. 
        @param code: Town code. 
        @param name: Town name. 
        @param section: Town section. For example, it is common for there to be 36 sections per township. 
        @param country: Name of the country. 
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



        super(TownDetail, self).__init__(*args, **kw_args)
    # >>> town_detail



class ElectronicAddress(Element):
    """ Electronic address information.
    """
    # <<< electronic_address
    # @generated
    def __init__(self, web='', email='', password='', lan='', user_id='', radio='', status=None, *args, **kw_args):
        """ Initialises a new 'ElectronicAddress' instance.

        @param web: World Wide Web address. 
        @param email: Email address. 
        @param password: Password needed to log in. 
        @param lan: Address on local area network. 
        @param user_id: User ID needed to log in, which can be for an individual person, an organisation, a location, etc. 
        @param radio: Radio address. 
        @param status: Status of this electronic address.
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


        self.status = status


        super(ElectronicAddress, self).__init__(*args, **kw_args)
    # >>> electronic_address

    # <<< status
    # @generated
    # Status of this electronic address.
    status = None
    # >>> status



class TimePoint(IdentifiedObject):
    """ A point in time within a sequence of points in time relative to a TimeSchedule.
    """
    # <<< time_point
    # @generated
    def __init__(self, relative_time_interval=0.0, date_time='', sequence_number=0, window=None, scheduled_events=None, time_schedule=None, status=None, *args, **kw_args):
        """ Initialises a new 'TimePoint' instance.

        @param relative_time_interval: (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'. 
        @param date_time: Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived. 
        @param sequence_number: (if sequence-based) Relative sequence number for this time point. 
        @param window: Interval defining the window of time that this time point is valid (for example, seasonal, only on weekends, not on weekends, only 8:00 to 5:00, etc.).
        @param scheduled_events:
        @param time_schedule: Time schedule owning this time point.
        @param status: Status of this time point.
        """
        # (if interval-based) A point in time relative to scheduled start time in 'TimeSchedule.scheduleInterval.start'. 
        self.relative_time_interval = relative_time_interval

        # Absolute date and time for this time point. For calendar-based time point, it is typically manually entered, while for interval-based or sequence-based time point it is derived. 
        self.date_time = date_time

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


        super(TimePoint, self).__init__(*args, **kw_args)
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



class UserAttribute(Element):
    """ Generic name-value pair class, with optional sequence number and units for value; can be used to model parts of information exchange when concrete types are not known in advance.
    """
    # <<< user_attribute
    # @generated
    def __init__(self, sequence_number=0, value='', name='', property_specification=None, rating_specification=None, property_assets=None, rating_assets=None, erp_ledger_entries=None, procedure_data_sets=None, transaction=None, procedure=None, pass_through_bills=None, erp_invoice_line_items=None, bill_determinants=None, erp_statement_line_items=None, *args, **kw_args):
        """ Initialises a new 'UserAttribute' instance.

        @param sequence_number: Sequence number for this attribute in a list of attributes. 
        @param value: Value of an attribute, including unit information. 
        @param name: Name of an attribute. 
        @param property_specification:
        @param rating_specification:
        @param property_assets:
        @param rating_assets:
        @param erp_ledger_entries:
        @param procedure_data_sets:
        @param transaction: Transaction for which this snapshot has been recorded.
        @param procedure:
        @param pass_through_bills:
        @param erp_invoice_line_items:
        @param bill_determinants:
        @param erp_statement_line_items:
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


        super(UserAttribute, self).__init__(*args, **kw_args)
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



class Status(Element):
    """ Current status information relevant to an entity.
    """
    # <<< status
    # @generated
    def __init__(self, date_time='', reason='', value='', remark='', *args, **kw_args):
        """ Initialises a new 'Status' instance.

        @param date_time: Date and time for which status 'value' applies. 
        @param reason: Reason code or explanation for why an object went to the current status 'value'. 
        @param value: Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies. 
        @param remark: Pertinent information regarding the current 'value', as free form text. 
        """
        # Date and time for which status 'value' applies. 
        self.date_time = date_time

        # Reason code or explanation for why an object went to the current status 'value'. 
        self.reason = reason

        # Status value at 'dateTime'; prior status changes may have been kept in instances of ActivityRecords associated with the object to which this Status applies. 
        self.value = value

        # Pertinent information regarding the current 'value', as free form text. 
        self.remark = remark



        super(Status, self).__init__(*args, **kw_args)
    # >>> status



class StreetDetail(Element):
    """ Street details, in the context of address.
    """
    # <<< street_detail
    # @generated
    def __init__(self, building_name='', type='', name='', within_town_limits=False, number='', suffix='', prefix='', code='', address_general='', suite_number='', *args, **kw_args):
        """ Initialises a new 'StreetDetail' instance.

        @param building_name: (if applicable) In certain cases the physical location of the place of interest does not have a direct point of entry from the street, but may be located inside a larger structure such as a building, complex, office block, apartment, etc. 
        @param type: Type of street. Examples include: street, circle, boulevard, avenue, road, drive, etc. 
        @param name: Name of the street. 
        @param within_town_limits: True if this street is within the legal geographical boundaries of the specified town (default). 
        @param number: Designator of the specific location on the street. 
        @param suffix: Suffix to the street name. For example: North, South, East, West. 
        @param prefix: Prefix to the street name. For example: North, South, East, West. 
        @param code: (if applicable) Utilities often make use of external reference systems, such as those of the town-planner's department or surveyor general's mapping system, that allocate global reference codes to streets. 
        @param address_general: Additional address information, for example a mailstop. 
        @param suite_number: Number of the apartment or suite. 
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



        super(StreetDetail, self).__init__(*args, **kw_args)
    # >>> street_detail



class Agreement(Document):
    """ Formal agreement between two parties defining the terms and conditions for a set of services. The specifics of the services are, in turn, defined via one or more service agreements.
    """
    # <<< agreement
    # @generated
    def __init__(self, sign_date='', validity_interval=None, *args, **kw_args):
        """ Initialises a new 'Agreement' instance.

        @param sign_date: Date this agreement was consummated among associated persons and/or organisations. 
        @param validity_interval: Date and time interval this agreement is valid (from going into effect to termination).
        """
        # Date this agreement was consummated among associated persons and/or organisations. 
        self.sign_date = sign_date


        self.validity_interval = validity_interval


        super(Agreement, self).__init__(*args, **kw_args)
    # >>> agreement

    # <<< validity_interval
    # @generated
    # Date and time interval this agreement is valid (from going into effect to termination).
    validity_interval = None
    # >>> validity_interval



class GeoLocation(Location):
    """ Geographical location.
    """
    # <<< geo_location
    # @generated
    def __init__(self, corporate_code='', direction='', geo_info_reference='', category='', routes=None, power_system_resources=None, phone2=None, measurements=None, change_items=None, erp_organisations=None, assets=None, hazards=None, main_address=None, activity_records=None, dimensions_info=None, directions=None, crews=None, secondary_address=None, red_lines=None, phone1=None, land_properties=None, electronic_address=None, status=None, *args, **kw_args):
        """ Initialises a new 'GeoLocation' instance.

        @param corporate_code: Utility-specific code for the location. 
        @param direction: (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building. 
        @param geo_info_reference: (if applicable) Reference to geographical information source, often external to the utility. 
        @param category: Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location). 
        @param routes:
        @param power_system_resources: All power system resources at this geographical location.
        @param phone2: Additional phone number.
        @param measurements:
        @param change_items:
        @param erp_organisations:
        @param assets: All assets at this geographical location.
        @param hazards:
        @param main_address: Main address of the location.
        @param activity_records:
        @param dimensions_info:
        @param directions:
        @param crews:
        @param secondary_address: Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
        @param red_lines:
        @param phone1: Phone number.
        @param land_properties:
        @param electronic_address: Electronic address.
        @param status: Status of this location.
        """
        # Utility-specific code for the location. 
        self.corporate_code = corporate_code

        # (if applicable) Direction that allows field crews to quickly find a given asset. For a given location, such as a street address, this is the relative direction in which to find the asset. For example, a Streetlight may be located at the 'NW' (northwest) corner of the customer's site, or a ServiceDeliveryPoint may be located on the second floor of an apartment building. 
        self.direction = direction

        # (if applicable) Reference to geographical information source, often external to the utility. 
        self.geo_info_reference = geo_info_reference

        # Category by utility's corporate standards and practices, relative to the location itself (e.g., geographical, functional accounting, etc., not a given property that happens to exist at that location). 
        self.category = category


        self._routes = []
        if routes is not None:
            self.routes = routes
        else:
            self.routes = []

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []

        self.phone2 = phone2

        self._measurements = []
        if measurements is not None:
            self.measurements = measurements
        else:
            self.measurements = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self._erp_organisations = []
        if erp_organisations is not None:
            self.erp_organisations = erp_organisations
        else:
            self.erp_organisations = []

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._hazards = []
        if hazards is not None:
            self.hazards = hazards
        else:
            self.hazards = []

        self.main_address = main_address

        self._activity_records = []
        if activity_records is not None:
            self.activity_records = activity_records
        else:
            self.activity_records = []

        self._dimensions_info = None
        self.dimensions_info = dimensions_info

        self._directions = []
        if directions is not None:
            self.directions = directions
        else:
            self.directions = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self.secondary_address = secondary_address

        self._red_lines = []
        if red_lines is not None:
            self.red_lines = red_lines
        else:
            self.red_lines = []

        self.phone1 = phone1

        self._land_properties = []
        if land_properties is not None:
            self.land_properties = land_properties
        else:
            self.land_properties = []

        self.electronic_address = electronic_address

        self.status = status


        super(GeoLocation, self).__init__(*args, **kw_args)
    # >>> geo_location

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

    # <<< phone2
    # @generated
    # Additional phone number.
    phone2 = None
    # >>> phone2

    # <<< measurements
    # @generated
    def get_measurements(self):
        """ 
        """
        return self._measurements

    def set_measurements(self, value):
        for p in self._measurements:
            filtered = [q for q in p.geo_locations if q != self]
            self._measurements._geo_locations = filtered
        for r in value:
            if self not in r._geo_locations:
                r._geo_locations.append(self)
        self._measurements = value

    measurements = property(get_measurements, set_measurements)

    def add_measurements(self, *measurements):
        for obj in measurements:
            if self not in obj._geo_locations:
                obj._geo_locations.append(self)
            self._measurements.append(obj)

    def remove_measurements(self, *measurements):
        for obj in measurements:
            if self in obj._geo_locations:
                obj._geo_locations.remove(self)
            self._measurements.remove(obj)
    # >>> measurements

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

    # <<< erp_organisations
    # @generated
    def get_erp_organisations(self):
        """ 
        """
        return self._erp_organisations

    def set_erp_organisations(self, value):
        for p in self._erp_organisations:
            filtered = [q for q in p.locations if q != self]
            self._erp_organisations._locations = filtered
        for r in value:
            if self not in r._locations:
                r._locations.append(self)
        self._erp_organisations = value

    erp_organisations = property(get_erp_organisations, set_erp_organisations)

    def add_erp_organisations(self, *erp_organisations):
        for obj in erp_organisations:
            if self not in obj._locations:
                obj._locations.append(self)
            self._erp_organisations.append(obj)

    def remove_erp_organisations(self, *erp_organisations):
        for obj in erp_organisations:
            if self in obj._locations:
                obj._locations.remove(self)
            self._erp_organisations.remove(obj)
    # >>> erp_organisations

    # <<< assets
    # @generated
    def get_assets(self):
        """ All assets at this geographical location.
        """
        return self._assets

    def set_assets(self, value):
        for x in self._assets:
            x._geo_location = None
        for y in value:
            y._geo_location = self
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            obj._geo_location = self
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            obj._geo_location = None
            self._assets.remove(obj)
    # >>> assets

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

    # <<< main_address
    # @generated
    # Main address of the location.
    main_address = None
    # >>> main_address

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

    # <<< directions
    # @generated
    def get_directions(self):
        """ 
        """
        return self._directions

    def set_directions(self, value):
        for x in self._directions:
            x._location = None
        for y in value:
            y._location = self
        self._directions = value

    directions = property(get_directions, set_directions)

    def add_directions(self, *directions):
        for obj in directions:
            obj._location = self
            self._directions.append(obj)

    def remove_directions(self, *directions):
        for obj in directions:
            obj._location = None
            self._directions.remove(obj)
    # >>> directions

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

    # <<< secondary_address
    # @generated
    # Secondary address of the location. For example, PO Box address may have different ZIP code than that in the 'mainAddress'.
    secondary_address = None
    # >>> secondary_address

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

    # <<< phone1
    # @generated
    # Phone number.
    phone1 = None
    # >>> phone1

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

    # <<< electronic_address
    # @generated
    # Electronic address.
    electronic_address = None
    # >>> electronic_address

    # <<< status
    # @generated
    # Status of this location.
    status = None
    # >>> status



class TimeSchedule(Document):
    """ Description of anything that changes through time. Time schedule is used to perform a single-valued function of time. Use inherited 'category' attribute to give additional information on this schedule, such as: periodic (hourly, daily, weekly, monthly, etc.), day of the month, by date, calendar (specific times and dates).
    """
    # <<< time_schedule
    # @generated
    def __init__(self, disabled=False, offset=0.0, recurrence_pattern='', recurrence_period=0.0, time_points=None, schedule_interval=None, *args, **kw_args):
        """ Initialises a new 'TimeSchedule' instance.

        @param disabled: True if this schedule is deactivated (disabled). 
        @param offset: The offset from midnight (i.e., 0 h, 0 min, 0 s) for the periodic time points to begin. For example, for an interval meter that is set up for five minute intervals ('recurrencePeriod'=300=5 min), setting 'offset'=120=2 min would result in scheduled events to read the meter executing at 2 min, 7 min, 12 min, 17 min, 22 min, 27 min, 32 min, 37 min, 42 min, 47 min, 52 min, and 57 min past each hour. 
        @param recurrence_pattern: Interval at which the scheduled action repeats (e.g., first Monday of every month, last day of the month, etc.). 
        @param recurrence_period: Duration between time points, from the beginning of one period to the beginning of the next period. Note that a device like a meter may have multiple interval periods (e.g., 1 min, 5 min, 15 min, 30 min, or 60 min). 
        @param time_points: Sequence of time points belonging to this time schedule.
        @param schedule_interval: Schedule date and time interval.
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


        super(TimeSchedule, self).__init__(*args, **kw_args)
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



# <<< common
# @generated
# >>> common
