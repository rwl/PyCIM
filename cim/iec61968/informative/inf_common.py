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

""" This package contains functions common for distribution management.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Locations are logical entities which are related to a geographical position. Locations can be defined as points, lines or polygons. Location serves as a parent class for e.g. Zone, WorkLocation or ServiceLocation. Both Assets and PowerSystemResources are typically associated to a location. Aside from coordinates, useful properties of Locations can include Directions (i.e. driving instructions) and relationships to Organizations. ActivityRecord is a generalized class used to track the history of an object (e.g. Asset, PowerSystemResource, Customer, Location, Organisation or ErpContact). An ActivityRecord is a type of Document. Key properties of an ActivityRecord include statusDate, status, statusReason and remarks. TODO: Update attribute names. The graphical and geographical aspects of Assets, Locations and PowerSystemResources are managed using Graphical Markup Language (GML), which was defined by the Open GIS Consortium.  Using GML, a diagram is a collection of presentation objects. This package defines the classes Diagram and Presentation. TODO: These are now under Common package.'
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61968.common import Document
from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infcommon"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfCommon"

class Role(IdentifiedObject):
    """ Enumeration of potential roles that might be played by one object relative to another.
    """
    # <<< role
    # @generated
    def __init__(self, category='', status=None, **kw_args):
        """ Initialises a new 'Role' instance.
        """
        # Category of role. 
        self.category = category


        self.status = status


        super(Role, self).__init__(**kw_args)
    # >>> role

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the Role.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Role.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Role", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Role")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> role.serialize


class ScheduledEvent(IdentifiedObject):
    """ Signifies an event to trigger one or more activities, such as reading a meter, recalculating a bill, requesting work, when generating units must be scheduled for maintenance, when a transformer is scheduled to be refurbished, etc.
    """
    # <<< scheduled_event
    # @generated
    def __init__(self, duration=0.0, category='', document=None, assets=None, activity_record=None, schedule_parameter_info=None, status=None, time_point=None, **kw_args):
        """ Initialises a new 'ScheduledEvent' instance.
        """
        # Duration of the scheduled event, for example, the time to ramp between values. 
        self.duration = duration

        # Category of scheduled event. 
        self.category = category


        self._document = None
        self.document = document

        self._assets = []
        if assets is not None:
            self.assets = assets
        else:
            self.assets = []

        self._activity_record = None
        self.activity_record = activity_record

        self._schedule_parameter_info = None
        self.schedule_parameter_info = schedule_parameter_info

        self.status = status

        self._time_point = None
        self.time_point = time_point


        super(ScheduledEvent, self).__init__(**kw_args)
    # >>> scheduled_event

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.scheduled_events if x != self]
            self._document._scheduled_events = filtered

        self._document = value
        if self._document is not None:
            self._document._scheduled_events.append(self)

    document = property(get_document, set_document)
    # >>> document

    # <<< assets
    # @generated
    def get_assets(self):
        """ 
        """
        return self._assets

    def set_assets(self, value):
        for p in self._assets:
            filtered = [q for q in p.scheduled_events if q != self]
            self._assets._scheduled_events = filtered
        for r in value:
            if self not in r._scheduled_events:
                r._scheduled_events.append(self)
        self._assets = value

    assets = property(get_assets, set_assets)

    def add_assets(self, *assets):
        for obj in assets:
            if self not in obj._scheduled_events:
                obj._scheduled_events.append(self)
            self._assets.append(obj)

    def remove_assets(self, *assets):
        for obj in assets:
            if self in obj._scheduled_events:
                obj._scheduled_events.remove(self)
            self._assets.remove(obj)
    # >>> assets

    # <<< activity_record
    # @generated
    def get_activity_record(self):
        """ 
        """
        return self._activity_record

    def set_activity_record(self, value):
        if self._activity_record is not None:
            self._activity_record._scheduled_event = None

        self._activity_record = value
        if self._activity_record is not None:
            self._activity_record._scheduled_event = self

    activity_record = property(get_activity_record, set_activity_record)
    # >>> activity_record

    # <<< schedule_parameter_info
    # @generated
    def get_schedule_parameter_info(self):
        """ 
        """
        return self._schedule_parameter_info

    def set_schedule_parameter_info(self, value):
        if self._schedule_parameter_info is not None:
            filtered = [x for x in self.schedule_parameter_info.scheduled_events if x != self]
            self._schedule_parameter_info._scheduled_events = filtered

        self._schedule_parameter_info = value
        if self._schedule_parameter_info is not None:
            self._schedule_parameter_info._scheduled_events.append(self)

    schedule_parameter_info = property(get_schedule_parameter_info, set_schedule_parameter_info)
    # >>> schedule_parameter_info

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< time_point
    # @generated
    def get_time_point(self):
        """ 
        """
        return self._time_point

    def set_time_point(self, value):
        if self._time_point is not None:
            filtered = [x for x in self.time_point.scheduled_events if x != self]
            self._time_point._scheduled_events = filtered

        self._time_point = value
        if self._time_point is not None:
            self._time_point._scheduled_events.append(self)

    time_point = property(get_time_point, set_time_point)
    # >>> time_point


    def __str__(self):
        """ Returns a string representation of the ScheduledEvent.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< scheduled_event.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ScheduledEvent.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ScheduledEvent", self.uri)
        if format:
            indent += ' ' * depth

        if self.document is not None:
            s += '%s<%s:ScheduledEvent.document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.document.uri)
        for obj in self.assets:
            s += '%s<%s:ScheduledEvent.assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.activity_record is not None:
            s += '%s<%s:ScheduledEvent.activity_record rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.activity_record.uri)
        if self.schedule_parameter_info is not None:
            s += '%s<%s:ScheduledEvent.schedule_parameter_info rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.schedule_parameter_info.uri)
        if self.status is not None:
            s += '%s<%s:ScheduledEvent.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.time_point is not None:
            s += '%s<%s:ScheduledEvent.time_point rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.time_point.uri)
        s += '%s<%s:ScheduledEvent.duration>%s</%s:ScheduledEvent.duration>' % \
            (indent, ns_prefix, self.duration, ns_prefix)
        s += '%s<%s:ScheduledEvent.category>%s</%s:ScheduledEvent.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ScheduledEvent")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> scheduled_event.serialize


class Skill(Document):
    """ Proficiency level of a craft, which is required to operate or maintain a particular type of asset and/or perform certain types of work.
    """
    # <<< skill
    # @generated
    def __init__(self, level='master', effective_date_time='', crafts=None, qualification_requirements=None, erp_person=None, certification_period=None, **kw_args):
        """ Initialises a new 'Skill' instance.
        """
        # Level of skill for a Craft. Values are: "master", "other", "standard", "apprentice"
        self.level = 'master'

        # Date and time the skill became effective. 
        self.effective_date_time = effective_date_time


        self._crafts = []
        if crafts is not None:
            self.crafts = crafts
        else:
            self.crafts = []

        self._qualification_requirements = []
        if qualification_requirements is not None:
            self.qualification_requirements = qualification_requirements
        else:
            self.qualification_requirements = []

        self._erp_person = None
        self.erp_person = erp_person

        self.certification_period = certification_period


        super(Skill, self).__init__(**kw_args)
    # >>> skill

    # <<< crafts
    # @generated
    def get_crafts(self):
        """ 
        """
        return self._crafts

    def set_crafts(self, value):
        for p in self._crafts:
            filtered = [q for q in p.skills if q != self]
            self._crafts._skills = filtered
        for r in value:
            if self not in r._skills:
                r._skills.append(self)
        self._crafts = value

    crafts = property(get_crafts, set_crafts)

    def add_crafts(self, *crafts):
        for obj in crafts:
            if self not in obj._skills:
                obj._skills.append(self)
            self._crafts.append(obj)

    def remove_crafts(self, *crafts):
        for obj in crafts:
            if self in obj._skills:
                obj._skills.remove(self)
            self._crafts.remove(obj)
    # >>> crafts

    # <<< qualification_requirements
    # @generated
    def get_qualification_requirements(self):
        """ 
        """
        return self._qualification_requirements

    def set_qualification_requirements(self, value):
        for p in self._qualification_requirements:
            filtered = [q for q in p.skills if q != self]
            self._qualification_requirements._skills = filtered
        for r in value:
            if self not in r._skills:
                r._skills.append(self)
        self._qualification_requirements = value

    qualification_requirements = property(get_qualification_requirements, set_qualification_requirements)

    def add_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self not in obj._skills:
                obj._skills.append(self)
            self._qualification_requirements.append(obj)

    def remove_qualification_requirements(self, *qualification_requirements):
        for obj in qualification_requirements:
            if self in obj._skills:
                obj._skills.remove(self)
            self._qualification_requirements.remove(obj)
    # >>> qualification_requirements

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.skills if x != self]
            self._erp_person._skills = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._skills.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person

    # <<< certification_period
    # @generated
    # Interval between the certification and its expiry.
    certification_period = None
    # >>> certification_period


    def __str__(self):
        """ Returns a string representation of the Skill.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< skill.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Skill.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Skill", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.crafts:
            s += '%s<%s:Skill.crafts rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.qualification_requirements:
            s += '%s<%s:Skill.qualification_requirements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.erp_person is not None:
            s += '%s<%s:Skill.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        if self.certification_period is not None:
            s += '%s<%s:Skill.certification_period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.certification_period.uri)
        s += '%s<%s:Skill.level>%s</%s:Skill.level>' % \
            (indent, ns_prefix, self.level, ns_prefix)
        s += '%s<%s:Skill.effective_date_time>%s</%s:Skill.effective_date_time>' % \
            (indent, ns_prefix, self.effective_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Skill")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> skill.serialize


class BankAccount(Document):
    """ Bank account.
    """
    # <<< bank_account
    # @generated
    def __init__(self, account_number='', service_supplier=None, bank=None, bank_statements=None, **kw_args):
        """ Initialises a new 'BankAccount' instance.
        """
        # Account reference number. 
        self.account_number = account_number


        self._service_supplier = None
        self.service_supplier = service_supplier

        self._bank = None
        self.bank = bank

        self._bank_statements = []
        if bank_statements is not None:
            self.bank_statements = bank_statements
        else:
            self.bank_statements = []


        super(BankAccount, self).__init__(**kw_args)
    # >>> bank_account

    # <<< service_supplier
    # @generated
    def get_service_supplier(self):
        """ ServiceSupplier that is owner of this BankAccount.
        """
        return self._service_supplier

    def set_service_supplier(self, value):
        if self._service_supplier is not None:
            filtered = [x for x in self.service_supplier.bank_accounts if x != self]
            self._service_supplier._bank_accounts = filtered

        self._service_supplier = value
        if self._service_supplier is not None:
            self._service_supplier._bank_accounts.append(self)

    service_supplier = property(get_service_supplier, set_service_supplier)
    # >>> service_supplier

    # <<< bank
    # @generated
    def get_bank(self):
        """ Bank that provides this BankAccount.
        """
        return self._bank

    def set_bank(self, value):
        if self._bank is not None:
            filtered = [x for x in self.bank.bank_accounts if x != self]
            self._bank._bank_accounts = filtered

        self._bank = value
        if self._bank is not None:
            self._bank._bank_accounts.append(self)

    bank = property(get_bank, set_bank)
    # >>> bank

    # <<< bank_statements
    # @generated
    def get_bank_statements(self):
        """ All bank statements generated from this bank account.
        """
        return self._bank_statements

    def set_bank_statements(self, value):
        for x in self._bank_statements:
            x._bank_account = None
        for y in value:
            y._bank_account = self
        self._bank_statements = value

    bank_statements = property(get_bank_statements, set_bank_statements)

    def add_bank_statements(self, *bank_statements):
        for obj in bank_statements:
            obj._bank_account = self
            self._bank_statements.append(obj)

    def remove_bank_statements(self, *bank_statements):
        for obj in bank_statements:
            obj._bank_account = None
            self._bank_statements.remove(obj)
    # >>> bank_statements


    def __str__(self):
        """ Returns a string representation of the BankAccount.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bank_account.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BankAccount.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BankAccount", self.uri)
        if format:
            indent += ' ' * depth

        if self.service_supplier is not None:
            s += '%s<%s:BankAccount.service_supplier rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.service_supplier.uri)
        if self.bank is not None:
            s += '%s<%s:BankAccount.bank rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bank.uri)
        for obj in self.bank_statements:
            s += '%s<%s:BankAccount.bank_statements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:BankAccount.account_number>%s</%s:BankAccount.account_number>' % \
            (indent, ns_prefix, self.account_number, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BankAccount")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bank_account.serialize


class MarketRole(IdentifiedObject):
    """ Role an organisation plays in a market. Examples include one or more of values defined in MarketRoleKind.
    """
    # <<< market_role
    # @generated
    def __init__(self, kind='other', status=None, organisations=None, **kw_args):
        """ Initialises a new 'MarketRole' instance.
        """
        # Kind of role an organisation plays in a market. Values are: "other", "transmission_service_provider", "planning_authority", "reliability_authority", "transmission_owner", "transmission_planner", "generator_operator", "energy_service_consumer", "generator_owner", "transmission_operator", "compliance_monitor", "distribution_provider", "load_serving_entity", "interchange_authority", "purchasing_selling_entity", "resource_planner", "balancing_authority", "competitive_retailer", "standards_developer"
        self.kind = 'other'


        self.status = status

        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []


        super(MarketRole, self).__init__(**kw_args)
    # >>> market_role

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.market_roles if q != self]
            self._organisations._market_roles = filtered
        for r in value:
            if self not in r._market_roles:
                r._market_roles.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._market_roles:
                obj._market_roles.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._market_roles:
                obj._market_roles.remove(self)
            self._organisations.remove(obj)
    # >>> organisations


    def __str__(self):
        """ Returns a string representation of the MarketRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< market_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MarketRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MarketRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.status is not None:
            s += '%s<%s:MarketRole.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.organisations:
            s += '%s<%s:MarketRole.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:MarketRole.kind>%s</%s:MarketRole.kind>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "MarketRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> market_role.serialize


class Diagram(Document):
    """ GML and/or other means are used for rendering objects on various types of displays(geographic, schematic, other) and maps associated with various coordinate systems.
    """
    # <<< diagram
    # @generated
    def __init__(self, kind='geographic', gml_diagram_objects=None, design_locations=None, gml_coordinate_system=None, **kw_args):
        """ Initialises a new 'Diagram' instance.
        """
        # Kind of this diagram. Values are: "geographic", "schematic", "design_sketch", "internal_view", "other"
        self.kind = 'geographic'


        self._gml_diagram_objects = []
        if gml_diagram_objects is not None:
            self.gml_diagram_objects = gml_diagram_objects
        else:
            self.gml_diagram_objects = []

        self._design_locations = []
        if design_locations is not None:
            self.design_locations = design_locations
        else:
            self.design_locations = []

        self._gml_coordinate_system = None
        self.gml_coordinate_system = gml_coordinate_system


        super(Diagram, self).__init__(**kw_args)
    # >>> diagram

    # <<< gml_diagram_objects
    # @generated
    def get_gml_diagram_objects(self):
        """ 
        """
        return self._gml_diagram_objects

    def set_gml_diagram_objects(self, value):
        for p in self._gml_diagram_objects:
            filtered = [q for q in p.diagrams if q != self]
            self._gml_diagram_objects._diagrams = filtered
        for r in value:
            if self not in r._diagrams:
                r._diagrams.append(self)
        self._gml_diagram_objects = value

    gml_diagram_objects = property(get_gml_diagram_objects, set_gml_diagram_objects)

    def add_gml_diagram_objects(self, *gml_diagram_objects):
        for obj in gml_diagram_objects:
            if self not in obj._diagrams:
                obj._diagrams.append(self)
            self._gml_diagram_objects.append(obj)

    def remove_gml_diagram_objects(self, *gml_diagram_objects):
        for obj in gml_diagram_objects:
            if self in obj._diagrams:
                obj._diagrams.remove(self)
            self._gml_diagram_objects.remove(obj)
    # >>> gml_diagram_objects

    # <<< design_locations
    # @generated
    def get_design_locations(self):
        """ 
        """
        return self._design_locations

    def set_design_locations(self, value):
        for p in self._design_locations:
            filtered = [q for q in p.diagrams if q != self]
            self._design_locations._diagrams = filtered
        for r in value:
            if self not in r._diagrams:
                r._diagrams.append(self)
        self._design_locations = value

    design_locations = property(get_design_locations, set_design_locations)

    def add_design_locations(self, *design_locations):
        for obj in design_locations:
            if self not in obj._diagrams:
                obj._diagrams.append(self)
            self._design_locations.append(obj)

    def remove_design_locations(self, *design_locations):
        for obj in design_locations:
            if self in obj._diagrams:
                obj._diagrams.remove(self)
            self._design_locations.remove(obj)
    # >>> design_locations

    # <<< gml_coordinate_system
    # @generated
    def get_gml_coordinate_system(self):
        """ 
        """
        return self._gml_coordinate_system

    def set_gml_coordinate_system(self, value):
        if self._gml_coordinate_system is not None:
            filtered = [x for x in self.gml_coordinate_system.diagrams if x != self]
            self._gml_coordinate_system._diagrams = filtered

        self._gml_coordinate_system = value
        if self._gml_coordinate_system is not None:
            self._gml_coordinate_system._diagrams.append(self)

    gml_coordinate_system = property(get_gml_coordinate_system, set_gml_coordinate_system)
    # >>> gml_coordinate_system


    def __str__(self):
        """ Returns a string representation of the Diagram.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< diagram.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Diagram.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Diagram", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.gml_diagram_objects:
            s += '%s<%s:Diagram.gml_diagram_objects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_locations:
            s += '%s<%s:Diagram.design_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_coordinate_system is not None:
            s += '%s<%s:Diagram.gml_coordinate_system rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_coordinate_system.uri)
        s += '%s<%s:Diagram.kind>%s</%s:Diagram.kind>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Diagram")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> diagram.serialize


class Ratio(Element):
    """ Fraction specified explicitly with a numerator and denominator, which can be used to calculate the quotient.
    """
    # <<< ratio
    # @generated
    def __init__(self, denominator=0.0, numerator=0.0, **kw_args):
        """ Initialises a new 'Ratio' instance.
        """
        # The part of a fraction that is below the line and that functions as the divisor of the numerator. 
        self.denominator = denominator

        # The part of a fraction that is above the line and signifies the number to be divided by the denominator. 
        self.numerator = numerator



        super(Ratio, self).__init__(**kw_args)
    # >>> ratio


    def __str__(self):
        """ Returns a string representation of the Ratio.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< ratio.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Ratio.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Ratio", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Ratio.denominator>%s</%s:Ratio.denominator>' % \
            (indent, ns_prefix, self.denominator, ns_prefix)
        s += '%s<%s:Ratio.numerator>%s</%s:Ratio.numerator>' % \
            (indent, ns_prefix, self.numerator, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Ratio")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ratio.serialize


class BusinessPlan(Document):
    """ A BusinessPlan is an organized sequence of predetermined actions required to complete a future organizational objective. It is a type of document that typically references a schedule, physical and/or logical resources (assets and/or PowerSystemResources), locations, etc.
    """
    pass
    # <<< business_plan
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'BusinessPlan' instance.
        """


        super(BusinessPlan, self).__init__(**kw_args)
    # >>> business_plan


    def __str__(self):
        """ Returns a string representation of the BusinessPlan.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< business_plan.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusinessPlan.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusinessPlan", self.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusinessPlan")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> business_plan.serialize


class BusinessRole(IdentifiedObject):
    """ A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.
    """
    # <<< business_role
    # @generated
    def __init__(self, category='', organisations=None, status=None, **kw_args):
        """ Initialises a new 'BusinessRole' instance.
        """
        # Category by utility's corporate standards and practices. 
        self.category = category


        self._organisations = []
        if organisations is not None:
            self.organisations = organisations
        else:
            self.organisations = []

        self.status = status


        super(BusinessRole, self).__init__(**kw_args)
    # >>> business_role

    # <<< organisations
    # @generated
    def get_organisations(self):
        """ 
        """
        return self._organisations

    def set_organisations(self, value):
        for p in self._organisations:
            filtered = [q for q in p.business_roles if q != self]
            self._organisations._business_roles = filtered
        for r in value:
            if self not in r._business_roles:
                r._business_roles.append(self)
        self._organisations = value

    organisations = property(get_organisations, set_organisations)

    def add_organisations(self, *organisations):
        for obj in organisations:
            if self not in obj._business_roles:
                obj._business_roles.append(self)
            self._organisations.append(obj)

    def remove_organisations(self, *organisations):
        for obj in organisations:
            if self in obj._business_roles:
                obj._business_roles.remove(self)
            self._organisations.remove(obj)
    # >>> organisations

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the BusinessRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< business_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusinessRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusinessRole", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.organisations:
            s += '%s<%s:BusinessRole.organisations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:BusinessRole.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:BusinessRole.category>%s</%s:BusinessRole.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusinessRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> business_role.serialize


class Craft(IdentifiedObject):
    """ Craft of a person or a crew. Examples include overhead electric, underground electric, high pressure gas, etc. This ensures necessary knowledge and skills before being allowed to perform certain types of work.
    """
    # <<< craft
    # @generated
    def __init__(self, category='', skills=None, erp_persons=None, status=None, capabilities=None, **kw_args):
        """ Initialises a new 'Craft' instance.
        """
        # Category by utility's work mangement standards and practices. 
        self.category = category


        self._skills = []
        if skills is not None:
            self.skills = skills
        else:
            self.skills = []

        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self.status = status

        self._capabilities = []
        if capabilities is not None:
            self.capabilities = capabilities
        else:
            self.capabilities = []


        super(Craft, self).__init__(**kw_args)
    # >>> craft

    # <<< skills
    # @generated
    def get_skills(self):
        """ 
        """
        return self._skills

    def set_skills(self, value):
        for p in self._skills:
            filtered = [q for q in p.crafts if q != self]
            self._skills._crafts = filtered
        for r in value:
            if self not in r._crafts:
                r._crafts.append(self)
        self._skills = value

    skills = property(get_skills, set_skills)

    def add_skills(self, *skills):
        for obj in skills:
            if self not in obj._crafts:
                obj._crafts.append(self)
            self._skills.append(obj)

    def remove_skills(self, *skills):
        for obj in skills:
            if self in obj._crafts:
                obj._crafts.remove(self)
            self._skills.remove(obj)
    # >>> skills

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.crafts if q != self]
            self._erp_persons._crafts = filtered
        for r in value:
            if self not in r._crafts:
                r._crafts.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._crafts:
                obj._crafts.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._crafts:
                obj._crafts.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< capabilities
    # @generated
    def get_capabilities(self):
        """ 
        """
        return self._capabilities

    def set_capabilities(self, value):
        for p in self._capabilities:
            filtered = [q for q in p.crafts if q != self]
            self._capabilities._crafts = filtered
        for r in value:
            if self not in r._crafts:
                r._crafts.append(self)
        self._capabilities = value

    capabilities = property(get_capabilities, set_capabilities)

    def add_capabilities(self, *capabilities):
        for obj in capabilities:
            if self not in obj._crafts:
                obj._crafts.append(self)
            self._capabilities.append(obj)

    def remove_capabilities(self, *capabilities):
        for obj in capabilities:
            if self in obj._crafts:
                obj._crafts.remove(self)
            self._capabilities.remove(obj)
    # >>> capabilities


    def __str__(self):
        """ Returns a string representation of the Craft.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< craft.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Craft.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Craft", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.skills:
            s += '%s<%s:Craft.skills rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_persons:
            s += '%s<%s:Craft.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:Craft.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.capabilities:
            s += '%s<%s:Craft.capabilities rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Craft.category>%s</%s:Craft.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "Craft")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> craft.serialize


class ScheduleParameterInfo(IdentifiedObject):
    """ Schedule parameters for an activity that is to occur, is occurring, or has completed.
    """
    # <<< schedule_parameter_info
    # @generated
    def __init__(self, for_inspection_data_set=None, estimated_window=None, scheduled_events=None, status=None, documents=None, requested_window=None, **kw_args):
        """ Initialises a new 'ScheduleParameterInfo' instance.
        """

        self._for_inspection_data_set = None
        self.for_inspection_data_set = for_inspection_data_set

        self.estimated_window = estimated_window

        self._scheduled_events = []
        if scheduled_events is not None:
            self.scheduled_events = scheduled_events
        else:
            self.scheduled_events = []

        self.status = status

        self._documents = []
        if documents is not None:
            self.documents = documents
        else:
            self.documents = []

        self.requested_window = requested_window


        super(ScheduleParameterInfo, self).__init__(**kw_args)
    # >>> schedule_parameter_info

    # <<< for_inspection_data_set
    # @generated
    def get_for_inspection_data_set(self):
        """ 
        """
        return self._for_inspection_data_set

    def set_for_inspection_data_set(self, value):
        if self._for_inspection_data_set is not None:
            filtered = [x for x in self.for_inspection_data_set.according_to_schedules if x != self]
            self._for_inspection_data_set._according_to_schedules = filtered

        self._for_inspection_data_set = value
        if self._for_inspection_data_set is not None:
            self._for_inspection_data_set._according_to_schedules.append(self)

    for_inspection_data_set = property(get_for_inspection_data_set, set_for_inspection_data_set)
    # >>> for_inspection_data_set

    # <<< estimated_window
    # @generated
    # Estimated date and time for activity execution (with earliest possibility of activity initiation and latest possibility of activity completion).
    estimated_window = None
    # >>> estimated_window

    # <<< scheduled_events
    # @generated
    def get_scheduled_events(self):
        """ 
        """
        return self._scheduled_events

    def set_scheduled_events(self, value):
        for x in self._scheduled_events:
            x._schedule_parameter_info = None
        for y in value:
            y._schedule_parameter_info = self
        self._scheduled_events = value

    scheduled_events = property(get_scheduled_events, set_scheduled_events)

    def add_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._schedule_parameter_info = self
            self._scheduled_events.append(obj)

    def remove_scheduled_events(self, *scheduled_events):
        for obj in scheduled_events:
            obj._schedule_parameter_info = None
            self._scheduled_events.remove(obj)
    # >>> scheduled_events

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< documents
    # @generated
    def get_documents(self):
        """ 
        """
        return self._documents

    def set_documents(self, value):
        for p in self._documents:
            filtered = [q for q in p.schedule_parameter_infos if q != self]
            self._documents._schedule_parameter_infos = filtered
        for r in value:
            if self not in r._schedule_parameter_infos:
                r._schedule_parameter_infos.append(self)
        self._documents = value

    documents = property(get_documents, set_documents)

    def add_documents(self, *documents):
        for obj in documents:
            if self not in obj._schedule_parameter_infos:
                obj._schedule_parameter_infos.append(self)
            self._documents.append(obj)

    def remove_documents(self, *documents):
        for obj in documents:
            if self in obj._schedule_parameter_infos:
                obj._schedule_parameter_infos.remove(self)
            self._documents.remove(obj)
    # >>> documents

    # <<< requested_window
    # @generated
    # Requested date and time interval for activity execution.
    requested_window = None
    # >>> requested_window


    def __str__(self):
        """ Returns a string representation of the ScheduleParameterInfo.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< schedule_parameter_info.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ScheduleParameterInfo.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ScheduleParameterInfo", self.uri)
        if format:
            indent += ' ' * depth

        if self.for_inspection_data_set is not None:
            s += '%s<%s:ScheduleParameterInfo.for_inspection_data_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.for_inspection_data_set.uri)
        if self.estimated_window is not None:
            s += '%s<%s:ScheduleParameterInfo.estimated_window rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.estimated_window.uri)
        for obj in self.scheduled_events:
            s += '%s<%s:ScheduleParameterInfo.scheduled_events rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ScheduleParameterInfo.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.documents:
            s += '%s<%s:ScheduleParameterInfo.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.requested_window is not None:
            s += '%s<%s:ScheduleParameterInfo.requested_window rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.requested_window.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ScheduleParameterInfo")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> schedule_parameter_info.serialize


class Map(Diagram):
    """ A type of diagram that is usually printed on paper. It normally depicts part of the earth's surface, showing utility assets, right of ways, topological data, coordinates, grids, etc. Maps vary depending on whether they are used for dispatch, design, schematic, etc.
    """
    # <<< map
    # @generated
    def __init__(self, map_loc_grid='', page_number=0, **kw_args):
        """ Initialises a new 'Map' instance.
        """
        # Map grid number. 
        self.map_loc_grid = map_loc_grid

        # Page number for particular set of maps specified by 'category'. 
        self.page_number = page_number



        super(Map, self).__init__(**kw_args)
    # >>> map


    def __str__(self):
        """ Returns a string representation of the Map.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< map.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Map.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Map", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Map.map_loc_grid>%s</%s:Map.map_loc_grid>' % \
            (indent, ns_prefix, self.map_loc_grid, ns_prefix)
        s += '%s<%s:Map.page_number>%s</%s:Map.page_number>' % \
            (indent, ns_prefix, self.page_number, ns_prefix)
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
        for obj in self.gml_diagram_objects:
            s += '%s<%s:Diagram.gml_diagram_objects rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.design_locations:
            s += '%s<%s:Diagram.design_locations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.gml_coordinate_system is not None:
            s += '%s<%s:Diagram.gml_coordinate_system rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_coordinate_system.uri)
        s += '%s<%s:Diagram.kind>%s</%s:Diagram.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Map")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> map.serialize


class DocPsrRole(Role):
    """ Potential roles that might played by a document relative to a type of PowerSystemResource.
    """
    # <<< doc_psr_role
    # @generated
    def __init__(self, document=None, power_system_resource=None, **kw_args):
        """ Initialises a new 'DocPsrRole' instance.
        """

        self._document = None
        self.document = document

        self._power_system_resource = None
        self.power_system_resource = power_system_resource


        super(DocPsrRole, self).__init__(**kw_args)
    # >>> doc_psr_role

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.power_system_resource_roles if x != self]
            self._document._power_system_resource_roles = filtered

        self._document = value
        if self._document is not None:
            self._document._power_system_resource_roles.append(self)

    document = property(get_document, set_document)
    # >>> document

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ 
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.document_roles if x != self]
            self._power_system_resource._document_roles = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._document_roles.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource


    def __str__(self):
        """ Returns a string representation of the DocPsrRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< doc_psr_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DocPsrRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DocPsrRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.document is not None:
            s += '%s<%s:DocPsrRole.document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.document.uri)
        if self.power_system_resource is not None:
            s += '%s<%s:DocPsrRole.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DocPsrRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> doc_psr_role.serialize


class DocDocRole(Role):
    """ Roles played between Documents and other Documents.
    """
    # <<< doc_doc_role
    # @generated
    def __init__(self, to_document=None, from_document=None, **kw_args):
        """ Initialises a new 'DocDocRole' instance.
        """

        self._to_document = None
        self.to_document = to_document

        self._from_document = None
        self.from_document = from_document


        super(DocDocRole, self).__init__(**kw_args)
    # >>> doc_doc_role

    # <<< to_document
    # @generated
    def get_to_document(self):
        """ 
        """
        return self._to_document

    def set_to_document(self, value):
        if self._to_document is not None:
            filtered = [x for x in self.to_document.from_document_roles if x != self]
            self._to_document._from_document_roles = filtered

        self._to_document = value
        if self._to_document is not None:
            self._to_document._from_document_roles.append(self)

    to_document = property(get_to_document, set_to_document)
    # >>> to_document

    # <<< from_document
    # @generated
    def get_from_document(self):
        """ 
        """
        return self._from_document

    def set_from_document(self, value):
        if self._from_document is not None:
            filtered = [x for x in self.from_document.to_document_roles if x != self]
            self._from_document._to_document_roles = filtered

        self._from_document = value
        if self._from_document is not None:
            self._from_document._to_document_roles.append(self)

    from_document = property(get_from_document, set_from_document)
    # >>> from_document


    def __str__(self):
        """ Returns a string representation of the DocDocRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< doc_doc_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DocDocRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DocDocRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.to_document is not None:
            s += '%s<%s:DocDocRole.to_document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.to_document.uri)
        if self.from_document is not None:
            s += '%s<%s:DocDocRole.from_document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.from_document.uri)
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
        if self.status is not None:
            s += '%s<%s:Role.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:Role.category>%s</%s:Role.category>' % \
            (indent, ns_prefix, self.category, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DocDocRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> doc_doc_role.serialize


# <<< inf_common
# @generated
# >>> inf_common
