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

""" TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Documentation package is used for the modeling of business documents. Some of these may be electronic realizations of legacy paper document, and some may be electronic information exchanges or collections. Documents will typically reference or describe one or more CIM objects. The DataSets package is used to describe documents tyically used for exchange of collections of object descriptions (e.g., NetworkDataSet). The operational package is used to define documents related to distribution operations business processes (e.g., OperationalRestriction, SwitchingSchedule). TroubleTickets are used by Customers to report problems related to the elctrical distribution network. TroubleTickets may be grouped and be related to a PlannedOutage, OutageNotification and/or PowerSystemResource. The Outage package defines classes related to outage management (OutageStep, OutageRecord, OutageReport).'
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61968.informative.inf_common import Role
from cim.iec61968.common import Document
from cim.iec61968.common import ActivityRecord
from cim.iec61970.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.infoperations"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#InfOperations"

class SwitchingStep(IdentifiedObject):
    """ A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.
    """
    # <<< switching_step
    # @generated
    def __init__(self, status_kind='confirmed', desired_end_state='', text='', required_control_action='', required_control_action_interval=None, safety_document=None, switching_schedule=None, erp_person_role=None, power_system_resources=None, **kw_args):
        """ Initialises a new 'SwitchingStep' instance.
        """
        # Status of this SwitchingStep. Values are: "confirmed", "skipped", "aborted", "instructed", "proposed"
        self.status_kind = 'confirmed'

        # Desired end state for the associated PowerSystemResource as a result of this schedule step. 
        self.desired_end_state = desired_end_state

        # Information regarding this switching schedule step. 
        self.text = text

        # Control actions required to perform this step. 
        self.required_control_action = required_control_action


        self.required_control_action_interval = required_control_action_interval

        self._safety_document = None
        self.safety_document = safety_document

        self._switching_schedule = None
        self.switching_schedule = switching_schedule

        self._erp_person_role = None
        self.erp_person_role = erp_person_role

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []


        super(SwitchingStep, self).__init__(**kw_args)
    # >>> switching_step

    # <<< required_control_action_interval
    # @generated
    # Interval between 'requiredControlAction' was issued and completed.
    required_control_action_interval = None
    # >>> required_control_action_interval

    # <<< safety_document
    # @generated
    def get_safety_document(self):
        """ 
        """
        return self._safety_document

    def set_safety_document(self, value):
        if self._safety_document is not None:
            filtered = [x for x in self.safety_document.schedule_steps if x != self]
            self._safety_document._schedule_steps = filtered

        self._safety_document = value
        if self._safety_document is not None:
            self._safety_document._schedule_steps.append(self)

    safety_document = property(get_safety_document, set_safety_document)
    # >>> safety_document

    # <<< switching_schedule
    # @generated
    def get_switching_schedule(self):
        """ 
        """
        return self._switching_schedule

    def set_switching_schedule(self, value):
        if self._switching_schedule is not None:
            filtered = [x for x in self.switching_schedule.schedule_steps if x != self]
            self._switching_schedule._schedule_steps = filtered

        self._switching_schedule = value
        if self._switching_schedule is not None:
            self._switching_schedule._schedule_steps.append(self)

    switching_schedule = property(get_switching_schedule, set_switching_schedule)
    # >>> switching_schedule

    # <<< erp_person_role
    # @generated
    def get_erp_person_role(self):
        """ 
        """
        return self._erp_person_role

    def set_erp_person_role(self, value):
        if self._erp_person_role is not None:
            self._erp_person_role._switching_step = None

        self._erp_person_role = value
        if self._erp_person_role is not None:
            self._erp_person_role._switching_step = self

    erp_person_role = property(get_erp_person_role, set_erp_person_role)
    # >>> erp_person_role

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ 
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for p in self._power_system_resources:
            filtered = [q for q in p.schedule_steps if q != self]
            self._power_system_resources._schedule_steps = filtered
        for r in value:
            if self not in r._schedule_steps:
                r._schedule_steps.append(self)
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self not in obj._schedule_steps:
                obj._schedule_steps.append(self)
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self in obj._schedule_steps:
                obj._schedule_steps.remove(self)
            self._power_system_resources.remove(obj)
    # >>> power_system_resources


    def __str__(self):
        """ Returns a string representation of the SwitchingStep.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switching_step.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SwitchingStep.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SwitchingStep", self.uri)
        if format:
            indent += ' ' * depth

        if self.required_control_action_interval is not None:
            s += '%s<%s:SwitchingStep.required_control_action_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.required_control_action_interval.uri)
        if self.safety_document is not None:
            s += '%s<%s:SwitchingStep.safety_document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.safety_document.uri)
        if self.switching_schedule is not None:
            s += '%s<%s:SwitchingStep.switching_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switching_schedule.uri)
        if self.erp_person_role is not None:
            s += '%s<%s:SwitchingStep.erp_person_role rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person_role.uri)
        for obj in self.power_system_resources:
            s += '%s<%s:SwitchingStep.power_system_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SwitchingStep.status_kind>%s</%s:SwitchingStep.status_kind>' % \
            (indent, ns_prefix, self.status_kind, ns_prefix)
        s += '%s<%s:SwitchingStep.desired_end_state>%s</%s:SwitchingStep.desired_end_state>' % \
            (indent, ns_prefix, self.desired_end_state, ns_prefix)
        s += '%s<%s:SwitchingStep.text>%s</%s:SwitchingStep.text>' % \
            (indent, ns_prefix, self.text, ns_prefix)
        s += '%s<%s:SwitchingStep.required_control_action>%s</%s:SwitchingStep.required_control_action>' % \
            (indent, ns_prefix, self.required_control_action, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SwitchingStep")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switching_step.serialize


class ErpPersonScheduleStepRole(Role):
    """ Roles played between Persons and Schedule Steps.
    """
    # <<< erp_person_schedule_step_role
    # @generated
    def __init__(self, switching_step=None, erp_person=None, **kw_args):
        """ Initialises a new 'ErpPersonScheduleStepRole' instance.
        """

        self._switching_step = None
        self.switching_step = switching_step

        self._erp_person = None
        self.erp_person = erp_person


        super(ErpPersonScheduleStepRole, self).__init__(**kw_args)
    # >>> erp_person_schedule_step_role

    # <<< switching_step
    # @generated
    def get_switching_step(self):
        """ 
        """
        return self._switching_step

    def set_switching_step(self, value):
        if self._switching_step is not None:
            self._switching_step._erp_person_role = None

        self._switching_step = value
        if self._switching_step is not None:
            self._switching_step._erp_person_role = self

    switching_step = property(get_switching_step, set_switching_step)
    # >>> switching_step

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.switching_step_roles if x != self]
            self._erp_person._switching_step_roles = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._switching_step_roles.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person


    def __str__(self):
        """ Returns a string representation of the ErpPersonScheduleStepRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< erp_person_schedule_step_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ErpPersonScheduleStepRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ErpPersonScheduleStepRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.switching_step is not None:
            s += '%s<%s:ErpPersonScheduleStepRole.switching_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.switching_step.uri)
        if self.erp_person is not None:
            s += '%s<%s:ErpPersonScheduleStepRole.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ErpPersonScheduleStepRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> erp_person_schedule_step_role.serialize


class OperationalRestriction(Document):
    """ A document that can be associated with a device to describe any sort of restrictions compared with the original manufacturer's specification e.g. temporary maximum loadings, maximum switching current, do not operate if bus couplers are open etc etc.  Since it is used in the network operations domain, it is associated with ConductingEquipment. In the UK, for example, if a breaker or switch ever mal-operates, this is reported centrally and utilities use their asset systems to identify all the installed devices of the same manufacturer's type. They then apply operational restrictions in the operational systems to warn operators of potential problems. After appropriate inspection and maintenance, the operational restrictions may be removed.
    """
    # <<< operational_restriction
    # @generated
    def __init__(self, active_period=None, **kw_args):
        """ Initialises a new 'OperationalRestriction' instance.
        """

        self.active_period = active_period


        super(OperationalRestriction, self).__init__(**kw_args)
    # >>> operational_restriction

    # <<< active_period
    # @generated
    # Interval during which the restriction is applied.
    active_period = None
    # >>> active_period


    def __str__(self):
        """ Returns a string representation of the OperationalRestriction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< operational_restriction.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OperationalRestriction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OperationalRestriction", self.uri)
        if format:
            indent += ' ' * depth

        if self.active_period is not None:
            s += '%s<%s:OperationalRestriction.active_period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.active_period.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OperationalRestriction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> operational_restriction.serialize


class SafetyDocument(Document):
    """ A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.
    """
    # <<< safety_document
    # @generated
    def __init__(self, power_system_resource=None, schedule_steps=None, clearance_tags=None, **kw_args):
        """ Initialises a new 'SafetyDocument' instance.
        """

        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._schedule_steps = []
        if schedule_steps is not None:
            self.schedule_steps = schedule_steps
        else:
            self.schedule_steps = []

        self._clearance_tags = []
        if clearance_tags is not None:
            self.clearance_tags = clearance_tags
        else:
            self.clearance_tags = []


        super(SafetyDocument, self).__init__(**kw_args)
    # >>> safety_document

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ 
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.safety_documents if x != self]
            self._power_system_resource._safety_documents = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._safety_documents.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< schedule_steps
    # @generated
    def get_schedule_steps(self):
        """ 
        """
        return self._schedule_steps

    def set_schedule_steps(self, value):
        for x in self._schedule_steps:
            x._safety_document = None
        for y in value:
            y._safety_document = self
        self._schedule_steps = value

    schedule_steps = property(get_schedule_steps, set_schedule_steps)

    def add_schedule_steps(self, *schedule_steps):
        for obj in schedule_steps:
            obj._safety_document = self
            self._schedule_steps.append(obj)

    def remove_schedule_steps(self, *schedule_steps):
        for obj in schedule_steps:
            obj._safety_document = None
            self._schedule_steps.remove(obj)
    # >>> schedule_steps

    # <<< clearance_tags
    # @generated
    def get_clearance_tags(self):
        """ 
        """
        return self._clearance_tags

    def set_clearance_tags(self, value):
        for x in self._clearance_tags:
            x._safety_document = None
        for y in value:
            y._safety_document = self
        self._clearance_tags = value

    clearance_tags = property(get_clearance_tags, set_clearance_tags)

    def add_clearance_tags(self, *clearance_tags):
        for obj in clearance_tags:
            obj._safety_document = self
            self._clearance_tags.append(obj)

    def remove_clearance_tags(self, *clearance_tags):
        for obj in clearance_tags:
            obj._safety_document = None
            self._clearance_tags.remove(obj)
    # >>> clearance_tags


    def __str__(self):
        """ Returns a string representation of the SafetyDocument.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< safety_document.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SafetyDocument.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SafetyDocument", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:SafetyDocument.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:SafetyDocument.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.clearance_tags:
            s += '%s<%s:SafetyDocument.clearance_tags rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SafetyDocument")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> safety_document.serialize


class OutageStep(IdentifiedObject):
    """ Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.
    """
    # <<< outage_step
    # @generated
    def __init__(self, job_priority='', total_cml=0.0, estimated_restore_date_time='', average_cml=0.0, shock_reported=False, special_customer_count=0, caller_count=0, damage=False, critical_customer_count=0, fatality=False, total_customer_count=0, injury=False, crews=None, outage_codes=None, outage_record=None, status=None, no_power_interval=None, conducting_equipment_roles=None, **kw_args):
        """ Initialises a new 'OutageStep' instance.
        """
 
        self.job_priority = job_priority

        # Total Customer Minutes Lost (CML) for this supply point for this outage. 
        self.total_cml = total_cml

        # Estimated time of restoration. 
        self.estimated_restore_date_time = estimated_restore_date_time

        # Average Customer Minutes Lost (CML) for this supply point for this outage. 
        self.average_cml = average_cml

        # True if shocks reported by caller or engineer. 
        self.shock_reported = shock_reported

        # Number of customers with high reliability required. 
        self.special_customer_count = special_customer_count

        # Number of customers phoning in. 
        self.caller_count = caller_count

        # True if damage reported by caller or engineer. 
        self.damage = damage

        # Number of customers with critical needs, e.g., with a dialysis machine. 
        self.critical_customer_count = critical_customer_count

        # True if fatalities reported by caller or engineer. 
        self.fatality = fatality

        # Number of customers connected to the PowerSystemResource. 
        self.total_customer_count = total_customer_count

        # True if injuries reported by caller or engineer. 
        self.injury = injury


        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self._outage_codes = []
        if outage_codes is not None:
            self.outage_codes = outage_codes
        else:
            self.outage_codes = []

        self._outage_record = None
        self.outage_record = outage_record

        self.status = status

        self.no_power_interval = no_power_interval

        self._conducting_equipment_roles = []
        if conducting_equipment_roles is not None:
            self.conducting_equipment_roles = conducting_equipment_roles
        else:
            self.conducting_equipment_roles = []


        super(OutageStep, self).__init__(**kw_args)
    # >>> outage_step

    # <<< crews
    # @generated
    def get_crews(self):
        """ 
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.outage_steps if q != self]
            self._crews._outage_steps = filtered
        for r in value:
            if self not in r._outage_steps:
                r._outage_steps.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._outage_steps:
                obj._outage_steps.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._outage_steps:
                obj._outage_steps.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< outage_codes
    # @generated
    def get_outage_codes(self):
        """ Multiple outage codes may apply to an outage step.
        """
        return self._outage_codes

    def set_outage_codes(self, value):
        for p in self._outage_codes:
            filtered = [q for q in p.outage_steps if q != self]
            self._outage_codes._outage_steps = filtered
        for r in value:
            if self not in r._outage_steps:
                r._outage_steps.append(self)
        self._outage_codes = value

    outage_codes = property(get_outage_codes, set_outage_codes)

    def add_outage_codes(self, *outage_codes):
        for obj in outage_codes:
            if self not in obj._outage_steps:
                obj._outage_steps.append(self)
            self._outage_codes.append(obj)

    def remove_outage_codes(self, *outage_codes):
        for obj in outage_codes:
            if self in obj._outage_steps:
                obj._outage_steps.remove(self)
            self._outage_codes.remove(obj)
    # >>> outage_codes

    # <<< outage_record
    # @generated
    def get_outage_record(self):
        """ 
        """
        return self._outage_record

    def set_outage_record(self, value):
        if self._outage_record is not None:
            filtered = [x for x in self.outage_record.outage_steps if x != self]
            self._outage_record._outage_steps = filtered

        self._outage_record = value
        if self._outage_record is not None:
            self._outage_record._outage_steps.append(self)

    outage_record = property(get_outage_record, set_outage_record)
    # >>> outage_record

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< no_power_interval
    # @generated
    # Date and time interval between loss and restoration of power.
    no_power_interval = None
    # >>> no_power_interval

    # <<< conducting_equipment_roles
    # @generated
    def get_conducting_equipment_roles(self):
        """ 
        """
        return self._conducting_equipment_roles

    def set_conducting_equipment_roles(self, value):
        for x in self._conducting_equipment_roles:
            x._outage_step = None
        for y in value:
            y._outage_step = self
        self._conducting_equipment_roles = value

    conducting_equipment_roles = property(get_conducting_equipment_roles, set_conducting_equipment_roles)

    def add_conducting_equipment_roles(self, *conducting_equipment_roles):
        for obj in conducting_equipment_roles:
            obj._outage_step = self
            self._conducting_equipment_roles.append(obj)

    def remove_conducting_equipment_roles(self, *conducting_equipment_roles):
        for obj in conducting_equipment_roles:
            obj._outage_step = None
            self._conducting_equipment_roles.remove(obj)
    # >>> conducting_equipment_roles


    def __str__(self):
        """ Returns a string representation of the OutageStep.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_step.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageStep.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageStep", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.crews:
            s += '%s<%s:OutageStep.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_codes:
            s += '%s<%s:OutageStep.outage_codes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_record is not None:
            s += '%s<%s:OutageStep.outage_record rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_record.uri)
        if self.status is not None:
            s += '%s<%s:OutageStep.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.no_power_interval is not None:
            s += '%s<%s:OutageStep.no_power_interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.no_power_interval.uri)
        for obj in self.conducting_equipment_roles:
            s += '%s<%s:OutageStep.conducting_equipment_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OutageStep.job_priority>%s</%s:OutageStep.job_priority>' % \
            (indent, ns_prefix, self.job_priority, ns_prefix)
        s += '%s<%s:OutageStep.total_cml>%s</%s:OutageStep.total_cml>' % \
            (indent, ns_prefix, self.total_cml, ns_prefix)
        s += '%s<%s:OutageStep.estimated_restore_date_time>%s</%s:OutageStep.estimated_restore_date_time>' % \
            (indent, ns_prefix, self.estimated_restore_date_time, ns_prefix)
        s += '%s<%s:OutageStep.average_cml>%s</%s:OutageStep.average_cml>' % \
            (indent, ns_prefix, self.average_cml, ns_prefix)
        s += '%s<%s:OutageStep.shock_reported>%s</%s:OutageStep.shock_reported>' % \
            (indent, ns_prefix, self.shock_reported, ns_prefix)
        s += '%s<%s:OutageStep.special_customer_count>%s</%s:OutageStep.special_customer_count>' % \
            (indent, ns_prefix, self.special_customer_count, ns_prefix)
        s += '%s<%s:OutageStep.caller_count>%s</%s:OutageStep.caller_count>' % \
            (indent, ns_prefix, self.caller_count, ns_prefix)
        s += '%s<%s:OutageStep.damage>%s</%s:OutageStep.damage>' % \
            (indent, ns_prefix, self.damage, ns_prefix)
        s += '%s<%s:OutageStep.critical_customer_count>%s</%s:OutageStep.critical_customer_count>' % \
            (indent, ns_prefix, self.critical_customer_count, ns_prefix)
        s += '%s<%s:OutageStep.fatality>%s</%s:OutageStep.fatality>' % \
            (indent, ns_prefix, self.fatality, ns_prefix)
        s += '%s<%s:OutageStep.total_customer_count>%s</%s:OutageStep.total_customer_count>' % \
            (indent, ns_prefix, self.total_customer_count, ns_prefix)
        s += '%s<%s:OutageStep.injury>%s</%s:OutageStep.injury>' % \
            (indent, ns_prefix, self.injury, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageStep")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_step.serialize


class ComplianceEvent(ActivityRecord):
    """ Compliance events are used for reporting regulatory or contract compliance issues and/or variances. These might be created as a consequence of local business processes and associated rules. It is anticipated that this class will be customised extensively to meet local implementation needs. Use inherited 'category' to indicate that, for example, expected performance will not be met or reported as mandated.
    """
    # <<< compliance_event
    # @generated
    def __init__(self, compliance_type='', deadline='', **kw_args):
        """ Initialises a new 'ComplianceEvent' instance.
        """
        # Type of compliance event indicating, for example, types of regulatory and/or contractual compliance events where expected performance will not be met or reported as mandated. 
        self.compliance_type = compliance_type

        # The deadline for compliance. 
        self.deadline = deadline



        super(ComplianceEvent, self).__init__(**kw_args)
    # >>> compliance_event


    def __str__(self):
        """ Returns a string representation of the ComplianceEvent.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< compliance_event.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ComplianceEvent.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ComplianceEvent", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ComplianceEvent.compliance_type>%s</%s:ComplianceEvent.compliance_type>' % \
            (indent, ns_prefix, self.compliance_type, ns_prefix)
        s += '%s<%s:ComplianceEvent.deadline>%s</%s:ComplianceEvent.deadline>' % \
            (indent, ns_prefix, self.deadline, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ComplianceEvent")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> compliance_event.serialize


class PSREvent(ActivityRecord):
    """ Event recording the change in operational status of a PowerSystemResource.
    """
    # <<< psrevent
    # @generated
    def __init__(self, kind='in_service', power_system_resource=None, **kw_args):
        """ Initialises a new 'PSREvent' instance.
        """
        # Kind of event. Values are: "in_service", "unknown", "pending_add", "out_of_service", "pending_remove", "other", "pending_replace"
        self.kind = 'in_service'


        self._power_system_resource = None
        self.power_system_resource = power_system_resource


        super(PSREvent, self).__init__(**kw_args)
    # >>> psrevent

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ Power system resource that generated this event.
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.psrevent if x != self]
            self._power_system_resource._psrevent = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._psrevent.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource


    def __str__(self):
        """ Returns a string representation of the PSREvent.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< psrevent.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PSREvent.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PSREvent", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:PSREvent.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        s += '%s<%s:PSREvent.kind>%s</%s:PSREvent.kind>' % \
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PSREvent")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> psrevent.serialize


class OutageCode(IdentifiedObject):
    """ Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in OutageRecord.outageType. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical 'outage code' is in the inherited 'name' attribute. The code is described in the inherited 'description' attribute.
    """
    # <<< outage_code
    # @generated
    def __init__(self, sub_code='', outage_records=None, outage_steps=None, **kw_args):
        """ Initialises a new 'OutageCode' instance.
        """
        # The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail. 
        self.sub_code = sub_code


        self._outage_records = []
        if outage_records is not None:
            self.outage_records = outage_records
        else:
            self.outage_records = []

        self._outage_steps = []
        if outage_steps is not None:
            self.outage_steps = outage_steps
        else:
            self.outage_steps = []


        super(OutageCode, self).__init__(**kw_args)
    # >>> outage_code

    # <<< outage_records
    # @generated
    def get_outage_records(self):
        """ 
        """
        return self._outage_records

    def set_outage_records(self, value):
        for p in self._outage_records:
            filtered = [q for q in p.outage_codes if q != self]
            self._outage_records._outage_codes = filtered
        for r in value:
            if self not in r._outage_codes:
                r._outage_codes.append(self)
        self._outage_records = value

    outage_records = property(get_outage_records, set_outage_records)

    def add_outage_records(self, *outage_records):
        for obj in outage_records:
            if self not in obj._outage_codes:
                obj._outage_codes.append(self)
            self._outage_records.append(obj)

    def remove_outage_records(self, *outage_records):
        for obj in outage_records:
            if self in obj._outage_codes:
                obj._outage_codes.remove(self)
            self._outage_records.remove(obj)
    # >>> outage_records

    # <<< outage_steps
    # @generated
    def get_outage_steps(self):
        """ 
        """
        return self._outage_steps

    def set_outage_steps(self, value):
        for p in self._outage_steps:
            filtered = [q for q in p.outage_codes if q != self]
            self._outage_steps._outage_codes = filtered
        for r in value:
            if self not in r._outage_codes:
                r._outage_codes.append(self)
        self._outage_steps = value

    outage_steps = property(get_outage_steps, set_outage_steps)

    def add_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            if self not in obj._outage_codes:
                obj._outage_codes.append(self)
            self._outage_steps.append(obj)

    def remove_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            if self in obj._outage_codes:
                obj._outage_codes.remove(self)
            self._outage_steps.remove(obj)
    # >>> outage_steps


    def __str__(self):
        """ Returns a string representation of the OutageCode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_code.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageCode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageCode", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.outage_records:
            s += '%s<%s:OutageCode.outage_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_steps:
            s += '%s<%s:OutageCode.outage_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OutageCode.sub_code>%s</%s:OutageCode.sub_code>' % \
            (indent, ns_prefix, self.sub_code, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageCode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_code.serialize


class OutageStepPsrRole(Role):
    """ Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.
    """
    # <<< outage_step_psr_role
    # @generated
    def __init__(self, conducting_equipment=None, outage_step=None, **kw_args):
        """ Initialises a new 'OutageStepPsrRole' instance.
        """

        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._outage_step = None
        self.outage_step = outage_step


        super(OutageStepPsrRole, self).__init__(**kw_args)
    # >>> outage_step_psr_role

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ 
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        if self._conducting_equipment is not None:
            filtered = [x for x in self.conducting_equipment.outage_step_roles if x != self]
            self._conducting_equipment._outage_step_roles = filtered

        self._conducting_equipment = value
        if self._conducting_equipment is not None:
            self._conducting_equipment._outage_step_roles.append(self)

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)
    # >>> conducting_equipment

    # <<< outage_step
    # @generated
    def get_outage_step(self):
        """ 
        """
        return self._outage_step

    def set_outage_step(self, value):
        if self._outage_step is not None:
            filtered = [x for x in self.outage_step.conducting_equipment_roles if x != self]
            self._outage_step._conducting_equipment_roles = filtered

        self._outage_step = value
        if self._outage_step is not None:
            self._outage_step._conducting_equipment_roles.append(self)

    outage_step = property(get_outage_step, set_outage_step)
    # >>> outage_step


    def __str__(self):
        """ Returns a string representation of the OutageStepPsrRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_step_psr_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageStepPsrRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageStepPsrRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.conducting_equipment is not None:
            s += '%s<%s:OutageStepPsrRole.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        if self.outage_step is not None:
            s += '%s<%s:OutageStepPsrRole.outage_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_step.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageStepPsrRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_step_psr_role.serialize


class NetworkDataSet(IdentifiedObject):
    """ Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.
    """
    # <<< network_data_set
    # @generated
    def __init__(self, category='', documents=None, circuit_sections=None, land_bases=None, change_sets=None, power_system_resources=None, change_items=None, status=None, **kw_args):
        """ Initialises a new 'NetworkDataSet' instance.
        """
        # Category of network data set. 
        self.category = category


        self._documents = []
        if documents is not None:
            self.documents = documents
        else:
            self.documents = []

        self._circuit_sections = []
        if circuit_sections is not None:
            self.circuit_sections = circuit_sections
        else:
            self.circuit_sections = []

        if land_bases is not None:
            self.land_bases = land_bases
        else:
            self.land_bases = []

        self._change_sets = []
        if change_sets is not None:
            self.change_sets = change_sets
        else:
            self.change_sets = []

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self.status = status


        super(NetworkDataSet, self).__init__(**kw_args)
    # >>> network_data_set

    # <<< documents
    # @generated
    def get_documents(self):
        """ 
        """
        return self._documents

    def set_documents(self, value):
        for p in self._documents:
            filtered = [q for q in p.network_data_sets if q != self]
            self._documents._network_data_sets = filtered
        for r in value:
            if self not in r._network_data_sets:
                r._network_data_sets.append(self)
        self._documents = value

    documents = property(get_documents, set_documents)

    def add_documents(self, *documents):
        for obj in documents:
            if self not in obj._network_data_sets:
                obj._network_data_sets.append(self)
            self._documents.append(obj)

    def remove_documents(self, *documents):
        for obj in documents:
            if self in obj._network_data_sets:
                obj._network_data_sets.remove(self)
            self._documents.remove(obj)
    # >>> documents

    # <<< circuit_sections
    # @generated
    def get_circuit_sections(self):
        """ A NetworkDataSet may contain sections of circuits (vs. whole circuits).
        """
        return self._circuit_sections

    def set_circuit_sections(self, value):
        for p in self._circuit_sections:
            filtered = [q for q in p.network_data_sets if q != self]
            self._circuit_sections._network_data_sets = filtered
        for r in value:
            if self not in r._network_data_sets:
                r._network_data_sets.append(self)
        self._circuit_sections = value

    circuit_sections = property(get_circuit_sections, set_circuit_sections)

    def add_circuit_sections(self, *circuit_sections):
        for obj in circuit_sections:
            if self not in obj._network_data_sets:
                obj._network_data_sets.append(self)
            self._circuit_sections.append(obj)

    def remove_circuit_sections(self, *circuit_sections):
        for obj in circuit_sections:
            if self in obj._network_data_sets:
                obj._network_data_sets.remove(self)
            self._circuit_sections.remove(obj)
    # >>> circuit_sections

    # <<< land_bases
    # @generated
    def add_land_bases(self, *land_bases):
        for obj in land_bases:
            self.land_bases.append(obj)

    def remove_land_bases(self, *land_bases):
        for obj in land_bases:
            self.land_bases.remove(obj)
    # >>> land_bases

    # <<< change_sets
    # @generated
    def get_change_sets(self):
        """ 
        """
        return self._change_sets

    def set_change_sets(self, value):
        for p in self._change_sets:
            filtered = [q for q in p.network_data_sets if q != self]
            self._change_sets._network_data_sets = filtered
        for r in value:
            if self not in r._network_data_sets:
                r._network_data_sets.append(self)
        self._change_sets = value

    change_sets = property(get_change_sets, set_change_sets)

    def add_change_sets(self, *change_sets):
        for obj in change_sets:
            if self not in obj._network_data_sets:
                obj._network_data_sets.append(self)
            self._change_sets.append(obj)

    def remove_change_sets(self, *change_sets):
        for obj in change_sets:
            if self in obj._network_data_sets:
                obj._network_data_sets.remove(self)
            self._change_sets.remove(obj)
    # >>> change_sets

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ 
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for p in self._power_system_resources:
            filtered = [q for q in p.network_data_sets if q != self]
            self._power_system_resources._network_data_sets = filtered
        for r in value:
            if self not in r._network_data_sets:
                r._network_data_sets.append(self)
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self not in obj._network_data_sets:
                obj._network_data_sets.append(self)
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self in obj._network_data_sets:
                obj._network_data_sets.remove(self)
            self._power_system_resources.remove(obj)
    # >>> power_system_resources

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._network_data_set = None
        for y in value:
            y._network_data_set = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._network_data_set = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._network_data_set = None
            self._change_items.remove(obj)
    # >>> change_items

    # <<< status
    # @generated
    status = None
    # >>> status


    def __str__(self):
        """ Returns a string representation of the NetworkDataSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< network_data_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NetworkDataSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NetworkDataSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.documents:
            s += '%s<%s:NetworkDataSet.documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:NetworkDataSet.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.land_bases:
            s += '%s<%s:NetworkDataSet.land_bases rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_sets:
            s += '%s<%s:NetworkDataSet.change_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resources:
            s += '%s<%s:NetworkDataSet.power_system_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:NetworkDataSet.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:NetworkDataSet.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        s += '%s<%s:NetworkDataSet.category>%s</%s:NetworkDataSet.category>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "NetworkDataSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> network_data_set.serialize


class CircuitSection(IdentifiedObject):
    """ Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.
    """
    # <<< circuit_section
    # @generated
    def __init__(self, connection_kind='electrically_connected', conductor_assets=None, network_data_sets=None, power_system_resources=None, circuits=None, **kw_args):
        """ Initialises a new 'CircuitSection' instance.
        """
        # Kind of this circuit section. Values are: "electrically_connected", "nominally_connected", "other", "as_built"
        self.connection_kind = 'electrically_connected'


        self._conductor_assets = []
        if conductor_assets is not None:
            self.conductor_assets = conductor_assets
        else:
            self.conductor_assets = []

        self._network_data_sets = []
        if network_data_sets is not None:
            self.network_data_sets = network_data_sets
        else:
            self.network_data_sets = []

        self._power_system_resources = []
        if power_system_resources is not None:
            self.power_system_resources = power_system_resources
        else:
            self.power_system_resources = []

        if circuits is not None:
            self.circuits = circuits
        else:
            self.circuits = []


        super(CircuitSection, self).__init__(**kw_args)
    # >>> circuit_section

    # <<< conductor_assets
    # @generated
    def get_conductor_assets(self):
        """ 
        """
        return self._conductor_assets

    def set_conductor_assets(self, value):
        for x in self._conductor_assets:
            x._circuit_section = None
        for y in value:
            y._circuit_section = self
        self._conductor_assets = value

    conductor_assets = property(get_conductor_assets, set_conductor_assets)

    def add_conductor_assets(self, *conductor_assets):
        for obj in conductor_assets:
            obj._circuit_section = self
            self._conductor_assets.append(obj)

    def remove_conductor_assets(self, *conductor_assets):
        for obj in conductor_assets:
            obj._circuit_section = None
            self._conductor_assets.remove(obj)
    # >>> conductor_assets

    # <<< network_data_sets
    # @generated
    def get_network_data_sets(self):
        """ 
        """
        return self._network_data_sets

    def set_network_data_sets(self, value):
        for p in self._network_data_sets:
            filtered = [q for q in p.circuit_sections if q != self]
            self._network_data_sets._circuit_sections = filtered
        for r in value:
            if self not in r._circuit_sections:
                r._circuit_sections.append(self)
        self._network_data_sets = value

    network_data_sets = property(get_network_data_sets, set_network_data_sets)

    def add_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self not in obj._circuit_sections:
                obj._circuit_sections.append(self)
            self._network_data_sets.append(obj)

    def remove_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self in obj._circuit_sections:
                obj._circuit_sections.remove(self)
            self._network_data_sets.remove(obj)
    # >>> network_data_sets

    # <<< power_system_resources
    # @generated
    def get_power_system_resources(self):
        """ 
        """
        return self._power_system_resources

    def set_power_system_resources(self, value):
        for p in self._power_system_resources:
            filtered = [q for q in p.circuit_sections if q != self]
            self._power_system_resources._circuit_sections = filtered
        for r in value:
            if self not in r._circuit_sections:
                r._circuit_sections.append(self)
        self._power_system_resources = value

    power_system_resources = property(get_power_system_resources, set_power_system_resources)

    def add_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self not in obj._circuit_sections:
                obj._circuit_sections.append(self)
            self._power_system_resources.append(obj)

    def remove_power_system_resources(self, *power_system_resources):
        for obj in power_system_resources:
            if self in obj._circuit_sections:
                obj._circuit_sections.remove(self)
            self._power_system_resources.remove(obj)
    # >>> power_system_resources

    # <<< circuits
    # @generated
    def add_circuits(self, *circuits):
        for obj in circuits:
            self.circuits.append(obj)

    def remove_circuits(self, *circuits):
        for obj in circuits:
            self.circuits.remove(obj)
    # >>> circuits


    def __str__(self):
        """ Returns a string representation of the CircuitSection.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< circuit_section.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CircuitSection.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CircuitSection", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.conductor_assets:
            s += '%s<%s:CircuitSection.conductor_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:CircuitSection.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.power_system_resources:
            s += '%s<%s:CircuitSection.power_system_resources rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuits:
            s += '%s<%s:CircuitSection.circuits rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:CircuitSection.connection_kind>%s</%s:CircuitSection.connection_kind>' % \
            (indent, ns_prefix, self.connection_kind, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CircuitSection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> circuit_section.serialize


class OutageRecord(Document):
    """ A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a Trouble Call System by grouping customer calls. This has an associated OutageStep for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a SwitchingSchedule which complements the OutageRecord and records the ErpPersons (crew) and any planned Work. In other systems, it may be acceptable to manage outages including new WorkTasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.
    """
    # <<< outage_record
    # @generated
    def __init__(self, mode='', damage_code='', action_taken='', end_date_time='', is_planned=False, outage_report=None, outage_codes=None, outage_steps=None, **kw_args):
        """ Initialises a new 'OutageRecord' instance.
        """
        # Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime. 
        self.mode = mode

        # The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none. 
        self.damage_code = damage_code

        # Overall action taken to resolve outage (details are in 'WorkTasks'). 
        self.action_taken = action_taken

        # Date and time restoration was completed for all customers impacted by this outage. 
        self.end_date_time = end_date_time

        # True if planned, false otherwise (for example due to a breaker trip). 
        self.is_planned = is_planned


        self._outage_report = None
        self.outage_report = outage_report

        self._outage_codes = []
        if outage_codes is not None:
            self.outage_codes = outage_codes
        else:
            self.outage_codes = []

        self._outage_steps = []
        if outage_steps is not None:
            self.outage_steps = outage_steps
        else:
            self.outage_steps = []


        super(OutageRecord, self).__init__(**kw_args)
    # >>> outage_record

    # <<< outage_report
    # @generated
    def get_outage_report(self):
        """ 
        """
        return self._outage_report

    def set_outage_report(self, value):
        if self._outage_report is not None:
            self._outage_report._outage_record = None

        self._outage_report = value
        if self._outage_report is not None:
            self._outage_report._outage_record = self

    outage_report = property(get_outage_report, set_outage_report)
    # >>> outage_report

    # <<< outage_codes
    # @generated
    def get_outage_codes(self):
        """ Multiple outage codes may apply to an outage record.
        """
        return self._outage_codes

    def set_outage_codes(self, value):
        for p in self._outage_codes:
            filtered = [q for q in p.outage_records if q != self]
            self._outage_codes._outage_records = filtered
        for r in value:
            if self not in r._outage_records:
                r._outage_records.append(self)
        self._outage_codes = value

    outage_codes = property(get_outage_codes, set_outage_codes)

    def add_outage_codes(self, *outage_codes):
        for obj in outage_codes:
            if self not in obj._outage_records:
                obj._outage_records.append(self)
            self._outage_codes.append(obj)

    def remove_outage_codes(self, *outage_codes):
        for obj in outage_codes:
            if self in obj._outage_records:
                obj._outage_records.remove(self)
            self._outage_codes.remove(obj)
    # >>> outage_codes

    # <<< outage_steps
    # @generated
    def get_outage_steps(self):
        """ 
        """
        return self._outage_steps

    def set_outage_steps(self, value):
        for x in self._outage_steps:
            x._outage_record = None
        for y in value:
            y._outage_record = self
        self._outage_steps = value

    outage_steps = property(get_outage_steps, set_outage_steps)

    def add_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            obj._outage_record = self
            self._outage_steps.append(obj)

    def remove_outage_steps(self, *outage_steps):
        for obj in outage_steps:
            obj._outage_record = None
            self._outage_steps.remove(obj)
    # >>> outage_steps


    def __str__(self):
        """ Returns a string representation of the OutageRecord.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_record.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageRecord.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageRecord", self.uri)
        if format:
            indent += ' ' * depth

        if self.outage_report is not None:
            s += '%s<%s:OutageRecord.outage_report rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_report.uri)
        for obj in self.outage_codes:
            s += '%s<%s:OutageRecord.outage_codes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_steps:
            s += '%s<%s:OutageRecord.outage_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OutageRecord.mode>%s</%s:OutageRecord.mode>' % \
            (indent, ns_prefix, self.mode, ns_prefix)
        s += '%s<%s:OutageRecord.damage_code>%s</%s:OutageRecord.damage_code>' % \
            (indent, ns_prefix, self.damage_code, ns_prefix)
        s += '%s<%s:OutageRecord.action_taken>%s</%s:OutageRecord.action_taken>' % \
            (indent, ns_prefix, self.action_taken, ns_prefix)
        s += '%s<%s:OutageRecord.end_date_time>%s</%s:OutageRecord.end_date_time>' % \
            (indent, ns_prefix, self.end_date_time, ns_prefix)
        s += '%s<%s:OutageRecord.is_planned>%s</%s:OutageRecord.is_planned>' % \
            (indent, ns_prefix, self.is_planned, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageRecord")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_record.serialize


class CallBack(IdentifiedObject):
    """ Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.
    """
    # <<< call_back
    # @generated
    def __init__(self, advice='', contact_detail='', comment='', problem_info='', date_time='', erp_persons=None, appointments=None, status=None, trouble_tickets=None, **kw_args):
        """ Initialises a new 'CallBack' instance.
        """
        # Advice already given to the customer during this call back. 
        self.advice = advice

        # Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber. 
        self.contact_detail = contact_detail

        # Comments by customer during this call back. 
        self.comment = comment

        # Descriptiion of the problem reported during this call back. 
        self.problem_info = problem_info

        # (if callback already occured) Date and time when this call back occurred. 
        self.date_time = date_time


        self._erp_persons = []
        if erp_persons is not None:
            self.erp_persons = erp_persons
        else:
            self.erp_persons = []

        self._appointments = []
        if appointments is not None:
            self.appointments = appointments
        else:
            self.appointments = []

        self.status = status

        self._trouble_tickets = []
        if trouble_tickets is not None:
            self.trouble_tickets = trouble_tickets
        else:
            self.trouble_tickets = []


        super(CallBack, self).__init__(**kw_args)
    # >>> call_back

    # <<< erp_persons
    # @generated
    def get_erp_persons(self):
        """ 
        """
        return self._erp_persons

    def set_erp_persons(self, value):
        for p in self._erp_persons:
            filtered = [q for q in p.call_backs if q != self]
            self._erp_persons._call_backs = filtered
        for r in value:
            if self not in r._call_backs:
                r._call_backs.append(self)
        self._erp_persons = value

    erp_persons = property(get_erp_persons, set_erp_persons)

    def add_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self not in obj._call_backs:
                obj._call_backs.append(self)
            self._erp_persons.append(obj)

    def remove_erp_persons(self, *erp_persons):
        for obj in erp_persons:
            if self in obj._call_backs:
                obj._call_backs.remove(self)
            self._erp_persons.remove(obj)
    # >>> erp_persons

    # <<< appointments
    # @generated
    def get_appointments(self):
        """ 
        """
        return self._appointments

    def set_appointments(self, value):
        for x in self._appointments:
            x._call_back = None
        for y in value:
            y._call_back = self
        self._appointments = value

    appointments = property(get_appointments, set_appointments)

    def add_appointments(self, *appointments):
        for obj in appointments:
            obj._call_back = self
            self._appointments.append(obj)

    def remove_appointments(self, *appointments):
        for obj in appointments:
            obj._call_back = None
            self._appointments.remove(obj)
    # >>> appointments

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< trouble_tickets
    # @generated
    def get_trouble_tickets(self):
        """ 
        """
        return self._trouble_tickets

    def set_trouble_tickets(self, value):
        for p in self._trouble_tickets:
            filtered = [q for q in p.call_backs if q != self]
            self._trouble_tickets._call_backs = filtered
        for r in value:
            if self not in r._call_backs:
                r._call_backs.append(self)
        self._trouble_tickets = value

    trouble_tickets = property(get_trouble_tickets, set_trouble_tickets)

    def add_trouble_tickets(self, *trouble_tickets):
        for obj in trouble_tickets:
            if self not in obj._call_backs:
                obj._call_backs.append(self)
            self._trouble_tickets.append(obj)

    def remove_trouble_tickets(self, *trouble_tickets):
        for obj in trouble_tickets:
            if self in obj._call_backs:
                obj._call_backs.remove(self)
            self._trouble_tickets.remove(obj)
    # >>> trouble_tickets


    def __str__(self):
        """ Returns a string representation of the CallBack.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< call_back.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CallBack.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CallBack", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.erp_persons:
            s += '%s<%s:CallBack.erp_persons rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.appointments:
            s += '%s<%s:CallBack.appointments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:CallBack.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.trouble_tickets:
            s += '%s<%s:CallBack.trouble_tickets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:CallBack.advice>%s</%s:CallBack.advice>' % \
            (indent, ns_prefix, self.advice, ns_prefix)
        s += '%s<%s:CallBack.contact_detail>%s</%s:CallBack.contact_detail>' % \
            (indent, ns_prefix, self.contact_detail, ns_prefix)
        s += '%s<%s:CallBack.comment>%s</%s:CallBack.comment>' % \
            (indent, ns_prefix, self.comment, ns_prefix)
        s += '%s<%s:CallBack.problem_info>%s</%s:CallBack.problem_info>' % \
            (indent, ns_prefix, self.problem_info, ns_prefix)
        s += '%s<%s:CallBack.date_time>%s</%s:CallBack.date_time>' % \
            (indent, ns_prefix, self.date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "CallBack")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> call_back.serialize


class ChangeItem(IdentifiedObject):
    """ Description for a single change within an ordered list of changes.
    """
    # <<< change_item
    # @generated
    def __init__(self, kind='add', sequence_number=0, power_system_resource=None, location=None, organisation=None, status=None, asset=None, document=None, gml_observation=None, erp_person=None, measurement=None, gml_selector=None, change_set=None, network_data_set=None, **kw_args):
        """ Initialises a new 'ChangeItem' instance.
        """
        # Kind of change for the associated object. Values are: "add", "modify", "delete"
        self.kind = 'add'

        # Relative order of this ChangeItem in an ordered sequence of changes. 
        self.sequence_number = sequence_number


        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._location = None
        self.location = location

        self._organisation = None
        self.organisation = organisation

        self.status = status

        self._asset = None
        self.asset = asset

        self._document = None
        self.document = document

        self._gml_observation = None
        self.gml_observation = gml_observation

        self._erp_person = None
        self.erp_person = erp_person

        self._measurement = None
        self.measurement = measurement

        self._gml_selector = None
        self.gml_selector = gml_selector

        self._change_set = None
        self.change_set = change_set

        self._network_data_set = None
        self.network_data_set = network_data_set


        super(ChangeItem, self).__init__(**kw_args)
    # >>> change_item

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ 
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.change_items if x != self]
            self._power_system_resource._change_items = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._change_items.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< location
    # @generated
    def get_location(self):
        """ 
        """
        return self._location

    def set_location(self, value):
        if self._location is not None:
            filtered = [x for x in self.location.change_items if x != self]
            self._location._change_items = filtered

        self._location = value
        if self._location is not None:
            self._location._change_items.append(self)

    location = property(get_location, set_location)
    # >>> location

    # <<< organisation
    # @generated
    def get_organisation(self):
        """ 
        """
        return self._organisation

    def set_organisation(self, value):
        if self._organisation is not None:
            filtered = [x for x in self.organisation.change_items if x != self]
            self._organisation._change_items = filtered

        self._organisation = value
        if self._organisation is not None:
            self._organisation._change_items.append(self)

    organisation = property(get_organisation, set_organisation)
    # >>> organisation

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< asset
    # @generated
    def get_asset(self):
        """ 
        """
        return self._asset

    def set_asset(self, value):
        if self._asset is not None:
            filtered = [x for x in self.asset.change_items if x != self]
            self._asset._change_items = filtered

        self._asset = value
        if self._asset is not None:
            self._asset._change_items.append(self)

    asset = property(get_asset, set_asset)
    # >>> asset

    # <<< document
    # @generated
    def get_document(self):
        """ 
        """
        return self._document

    def set_document(self, value):
        if self._document is not None:
            filtered = [x for x in self.document.change_items if x != self]
            self._document._change_items = filtered

        self._document = value
        if self._document is not None:
            self._document._change_items.append(self)

    document = property(get_document, set_document)
    # >>> document

    # <<< gml_observation
    # @generated
    def get_gml_observation(self):
        """ 
        """
        return self._gml_observation

    def set_gml_observation(self, value):
        if self._gml_observation is not None:
            filtered = [x for x in self.gml_observation.change_items if x != self]
            self._gml_observation._change_items = filtered

        self._gml_observation = value
        if self._gml_observation is not None:
            self._gml_observation._change_items.append(self)

    gml_observation = property(get_gml_observation, set_gml_observation)
    # >>> gml_observation

    # <<< erp_person
    # @generated
    def get_erp_person(self):
        """ 
        """
        return self._erp_person

    def set_erp_person(self, value):
        if self._erp_person is not None:
            filtered = [x for x in self.erp_person.change_items if x != self]
            self._erp_person._change_items = filtered

        self._erp_person = value
        if self._erp_person is not None:
            self._erp_person._change_items.append(self)

    erp_person = property(get_erp_person, set_erp_person)
    # >>> erp_person

    # <<< measurement
    # @generated
    def get_measurement(self):
        """ 
        """
        return self._measurement

    def set_measurement(self, value):
        if self._measurement is not None:
            filtered = [x for x in self.measurement.change_items if x != self]
            self._measurement._change_items = filtered

        self._measurement = value
        if self._measurement is not None:
            self._measurement._change_items.append(self)

    measurement = property(get_measurement, set_measurement)
    # >>> measurement

    # <<< gml_selector
    # @generated
    def get_gml_selector(self):
        """ 
        """
        return self._gml_selector

    def set_gml_selector(self, value):
        if self._gml_selector is not None:
            filtered = [x for x in self.gml_selector.change_items if x != self]
            self._gml_selector._change_items = filtered

        self._gml_selector = value
        if self._gml_selector is not None:
            self._gml_selector._change_items.append(self)

    gml_selector = property(get_gml_selector, set_gml_selector)
    # >>> gml_selector

    # <<< change_set
    # @generated
    def get_change_set(self):
        """ 
        """
        return self._change_set

    def set_change_set(self, value):
        if self._change_set is not None:
            filtered = [x for x in self.change_set.change_items if x != self]
            self._change_set._change_items = filtered

        self._change_set = value
        if self._change_set is not None:
            self._change_set._change_items.append(self)

    change_set = property(get_change_set, set_change_set)
    # >>> change_set

    # <<< network_data_set
    # @generated
    def get_network_data_set(self):
        """ 
        """
        return self._network_data_set

    def set_network_data_set(self, value):
        if self._network_data_set is not None:
            filtered = [x for x in self.network_data_set.change_items if x != self]
            self._network_data_set._change_items = filtered

        self._network_data_set = value
        if self._network_data_set is not None:
            self._network_data_set._change_items.append(self)

    network_data_set = property(get_network_data_set, set_network_data_set)
    # >>> network_data_set


    def __str__(self):
        """ Returns a string representation of the ChangeItem.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< change_item.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ChangeItem.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ChangeItem", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:ChangeItem.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        if self.location is not None:
            s += '%s<%s:ChangeItem.location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.location.uri)
        if self.organisation is not None:
            s += '%s<%s:ChangeItem.organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.organisation.uri)
        if self.status is not None:
            s += '%s<%s:ChangeItem.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        if self.asset is not None:
            s += '%s<%s:ChangeItem.asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.asset.uri)
        if self.document is not None:
            s += '%s<%s:ChangeItem.document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.document.uri)
        if self.gml_observation is not None:
            s += '%s<%s:ChangeItem.gml_observation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_observation.uri)
        if self.erp_person is not None:
            s += '%s<%s:ChangeItem.erp_person rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_person.uri)
        if self.measurement is not None:
            s += '%s<%s:ChangeItem.measurement rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.measurement.uri)
        if self.gml_selector is not None:
            s += '%s<%s:ChangeItem.gml_selector rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.gml_selector.uri)
        if self.change_set is not None:
            s += '%s<%s:ChangeItem.change_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.change_set.uri)
        if self.network_data_set is not None:
            s += '%s<%s:ChangeItem.network_data_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.network_data_set.uri)
        s += '%s<%s:ChangeItem.kind>%s</%s:ChangeItem.kind>' % \
            (indent, ns_prefix, self.kind, ns_prefix)
        s += '%s<%s:ChangeItem.sequence_number>%s</%s:ChangeItem.sequence_number>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ChangeItem")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> change_item.serialize


class OrgPsrRole(Role):
    """ Roles played between Organisations and Power System Resources.
    """
    # <<< org_psr_role
    # @generated
    def __init__(self, power_system_resource=None, erp_organisation=None, **kw_args):
        """ Initialises a new 'OrgPsrRole' instance.
        """

        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._erp_organisation = None
        self.erp_organisation = erp_organisation


        super(OrgPsrRole, self).__init__(**kw_args)
    # >>> org_psr_role

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ 
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            filtered = [x for x in self.power_system_resource.erp_organisation_roles if x != self]
            self._power_system_resource._erp_organisation_roles = filtered

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._erp_organisation_roles.append(self)

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< erp_organisation
    # @generated
    def get_erp_organisation(self):
        """ 
        """
        return self._erp_organisation

    def set_erp_organisation(self, value):
        if self._erp_organisation is not None:
            filtered = [x for x in self.erp_organisation.power_system_resource_roles if x != self]
            self._erp_organisation._power_system_resource_roles = filtered

        self._erp_organisation = value
        if self._erp_organisation is not None:
            self._erp_organisation._power_system_resource_roles.append(self)

    erp_organisation = property(get_erp_organisation, set_erp_organisation)
    # >>> erp_organisation


    def __str__(self):
        """ Returns a string representation of the OrgPsrRole.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< org_psr_role.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OrgPsrRole.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OrgPsrRole", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:OrgPsrRole.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        if self.erp_organisation is not None:
            s += '%s<%s:OrgPsrRole.erp_organisation rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.erp_organisation.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OrgPsrRole")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> org_psr_role.serialize


class OutageNotification(Document):
    """ A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.
    """
    # <<< outage_notification
    # @generated
    def __init__(self, duration=0.0, reason='', expected_interruption_count=0, customer_datas=None, **kw_args):
        """ Initialises a new 'OutageNotification' instance.
        """
        # Likely duration of the interruption(s). 
        self.duration = duration

        # Details of the outage 'reason'. 
        self.reason = reason

        # Number of possible interruptions that the customer may expect for this event. 
        self.expected_interruption_count = expected_interruption_count


        self._customer_datas = []
        if customer_datas is not None:
            self.customer_datas = customer_datas
        else:
            self.customer_datas = []


        super(OutageNotification, self).__init__(**kw_args)
    # >>> outage_notification

    # <<< customer_datas
    # @generated
    def get_customer_datas(self):
        """ 
        """
        return self._customer_datas

    def set_customer_datas(self, value):
        for p in self._customer_datas:
            filtered = [q for q in p.outage_notifications if q != self]
            self._customer_datas._outage_notifications = filtered
        for r in value:
            if self not in r._outage_notifications:
                r._outage_notifications.append(self)
        self._customer_datas = value

    customer_datas = property(get_customer_datas, set_customer_datas)

    def add_customer_datas(self, *customer_datas):
        for obj in customer_datas:
            if self not in obj._outage_notifications:
                obj._outage_notifications.append(self)
            self._customer_datas.append(obj)

    def remove_customer_datas(self, *customer_datas):
        for obj in customer_datas:
            if self in obj._outage_notifications:
                obj._outage_notifications.remove(self)
            self._customer_datas.remove(obj)
    # >>> customer_datas


    def __str__(self):
        """ Returns a string representation of the OutageNotification.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_notification.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageNotification.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageNotification", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.customer_datas:
            s += '%s<%s:OutageNotification.customer_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:OutageNotification.duration>%s</%s:OutageNotification.duration>' % \
            (indent, ns_prefix, self.duration, ns_prefix)
        s += '%s<%s:OutageNotification.reason>%s</%s:OutageNotification.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
        s += '%s<%s:OutageNotification.expected_interruption_count>%s</%s:OutageNotification.expected_interruption_count>' % \
            (indent, ns_prefix, self.expected_interruption_count, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageNotification")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_notification.serialize


class SwitchingSchedule(Document):
    """ Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.
    """
    # <<< switching_schedule
    # @generated
    def __init__(self, reason='', interval=None, schedule_steps=None, crews=None, work_task=None, **kw_args):
        """ Initialises a new 'SwitchingSchedule' instance.
        """
        # Reason for switching. 
        self.reason = reason


        self.interval = interval

        self._schedule_steps = []
        if schedule_steps is not None:
            self.schedule_steps = schedule_steps
        else:
            self.schedule_steps = []

        self._crews = []
        if crews is not None:
            self.crews = crews
        else:
            self.crews = []

        self._work_task = None
        self.work_task = work_task


        super(SwitchingSchedule, self).__init__(**kw_args)
    # >>> switching_schedule

    # <<< interval
    # @generated
    # Interval between starting and completion of the switching.
    interval = None
    # >>> interval

    # <<< schedule_steps
    # @generated
    def get_schedule_steps(self):
        """ 
        """
        return self._schedule_steps

    def set_schedule_steps(self, value):
        for x in self._schedule_steps:
            x._switching_schedule = None
        for y in value:
            y._switching_schedule = self
        self._schedule_steps = value

    schedule_steps = property(get_schedule_steps, set_schedule_steps)

    def add_schedule_steps(self, *schedule_steps):
        for obj in schedule_steps:
            obj._switching_schedule = self
            self._schedule_steps.append(obj)

    def remove_schedule_steps(self, *schedule_steps):
        for obj in schedule_steps:
            obj._switching_schedule = None
            self._schedule_steps.remove(obj)
    # >>> schedule_steps

    # <<< crews
    # @generated
    def get_crews(self):
        """ All Crews executing this SwitchingSchedule.
        """
        return self._crews

    def set_crews(self, value):
        for p in self._crews:
            filtered = [q for q in p.switching_schedules if q != self]
            self._crews._switching_schedules = filtered
        for r in value:
            if self not in r._switching_schedules:
                r._switching_schedules.append(self)
        self._crews = value

    crews = property(get_crews, set_crews)

    def add_crews(self, *crews):
        for obj in crews:
            if self not in obj._switching_schedules:
                obj._switching_schedules.append(self)
            self._crews.append(obj)

    def remove_crews(self, *crews):
        for obj in crews:
            if self in obj._switching_schedules:
                obj._switching_schedules.remove(self)
            self._crews.remove(obj)
    # >>> crews

    # <<< work_task
    # @generated
    def get_work_task(self):
        """ 
        """
        return self._work_task

    def set_work_task(self, value):
        if self._work_task is not None:
            filtered = [x for x in self.work_task.switching_schedules if x != self]
            self._work_task._switching_schedules = filtered

        self._work_task = value
        if self._work_task is not None:
            self._work_task._switching_schedules.append(self)

    work_task = property(get_work_task, set_work_task)
    # >>> work_task


    def __str__(self):
        """ Returns a string representation of the SwitchingSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switching_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SwitchingSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SwitchingSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.interval is not None:
            s += '%s<%s:SwitchingSchedule.interval rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.interval.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:SwitchingSchedule.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.crews:
            s += '%s<%s:SwitchingSchedule.crews rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.work_task is not None:
            s += '%s<%s:SwitchingSchedule.work_task rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.work_task.uri)
        s += '%s<%s:SwitchingSchedule.reason>%s</%s:SwitchingSchedule.reason>' % \
            (indent, ns_prefix, self.reason, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SwitchingSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switching_schedule.serialize


class IncidentCode(IdentifiedObject):
    """ Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in 'name'.
    """
    # <<< incident_code
    # @generated
    def __init__(self, sub_code='', incident_records=None, **kw_args):
        """ Initialises a new 'IncidentCode' instance.
        """
        # Additional level of classification detail (as extension to the main code found in 'name'). 
        self.sub_code = sub_code


        self._incident_records = []
        if incident_records is not None:
            self.incident_records = incident_records
        else:
            self.incident_records = []


        super(IncidentCode, self).__init__(**kw_args)
    # >>> incident_code

    # <<< incident_records
    # @generated
    def get_incident_records(self):
        """ 
        """
        return self._incident_records

    def set_incident_records(self, value):
        for p in self._incident_records:
            filtered = [q for q in p.incident_codes if q != self]
            self._incident_records._incident_codes = filtered
        for r in value:
            if self not in r._incident_codes:
                r._incident_codes.append(self)
        self._incident_records = value

    incident_records = property(get_incident_records, set_incident_records)

    def add_incident_records(self, *incident_records):
        for obj in incident_records:
            if self not in obj._incident_codes:
                obj._incident_codes.append(self)
            self._incident_records.append(obj)

    def remove_incident_records(self, *incident_records):
        for obj in incident_records:
            if self in obj._incident_codes:
                obj._incident_codes.remove(self)
            self._incident_records.remove(obj)
    # >>> incident_records


    def __str__(self):
        """ Returns a string representation of the IncidentCode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< incident_code.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IncidentCode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IncidentCode", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.incident_records:
            s += '%s<%s:IncidentCode.incident_records rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:IncidentCode.sub_code>%s</%s:IncidentCode.sub_code>' % \
            (indent, ns_prefix, self.sub_code, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "IncidentCode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> incident_code.serialize


class PlannedOutage(Document):
    """ Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.
    """
    # <<< planned_outage
    # @generated
    def __init__(self, kind='flexible', customer_datas=None, outage_schedules=None, **kw_args):
        """ Initialises a new 'PlannedOutage' instance.
        """
        # Kind of outage. Values are: "flexible", "fixed", "forced"
        self.kind = 'flexible'


        self._customer_datas = []
        if customer_datas is not None:
            self.customer_datas = customer_datas
        else:
            self.customer_datas = []

        self._outage_schedules = []
        if outage_schedules is not None:
            self.outage_schedules = outage_schedules
        else:
            self.outage_schedules = []


        super(PlannedOutage, self).__init__(**kw_args)
    # >>> planned_outage

    # <<< customer_datas
    # @generated
    def get_customer_datas(self):
        """ All customers affected by this work. Derived from WorkOrder.connectedCustomers
        """
        return self._customer_datas

    def set_customer_datas(self, value):
        for x in self._customer_datas:
            x._planned_outage = None
        for y in value:
            y._planned_outage = self
        self._customer_datas = value

    customer_datas = property(get_customer_datas, set_customer_datas)

    def add_customer_datas(self, *customer_datas):
        for obj in customer_datas:
            obj._planned_outage = self
            self._customer_datas.append(obj)

    def remove_customer_datas(self, *customer_datas):
        for obj in customer_datas:
            obj._planned_outage = None
            self._customer_datas.remove(obj)
    # >>> customer_datas

    # <<< outage_schedules
    # @generated
    def get_outage_schedules(self):
        """ 
        """
        return self._outage_schedules

    def set_outage_schedules(self, value):
        for x in self._outage_schedules:
            x._planned_outage = None
        for y in value:
            y._planned_outage = self
        self._outage_schedules = value

    outage_schedules = property(get_outage_schedules, set_outage_schedules)

    def add_outage_schedules(self, *outage_schedules):
        for obj in outage_schedules:
            obj._planned_outage = self
            self._outage_schedules.append(obj)

    def remove_outage_schedules(self, *outage_schedules):
        for obj in outage_schedules:
            obj._planned_outage = None
            self._outage_schedules.remove(obj)
    # >>> outage_schedules


    def __str__(self):
        """ Returns a string representation of the PlannedOutage.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< planned_outage.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PlannedOutage.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PlannedOutage", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.customer_datas:
            s += '%s<%s:PlannedOutage.customer_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.outage_schedules:
            s += '%s<%s:PlannedOutage.outage_schedules rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PlannedOutage.kind>%s</%s:PlannedOutage.kind>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "PlannedOutage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> planned_outage.serialize


class TroubleTicket(Document):
    """ A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an Incident Record. Note that a separate Activity Record is created for each call associated with an instance of Trouble Ticket. The time of a call is stored in ActivityRecord.createdOn and comments are recorded in ActivityRecord.remarks.
    """
    # <<< trouble_ticket
    # @generated
    def __init__(self, reporting_kind='letter', advice='', call_back=False, priority='', inform_after_restored=False, estimated_restore_date_time='', inform_before_restored=False, hazard_code='', first_call_date_time='', customer_data=None, trouble_period=None, call_backs=None, incident_record=None, **kw_args):
        """ Initialises a new 'TroubleTicket' instance.
        """
        # Means the customer used to report trouble (default is 'call'). Values are: "letter", "other", "call", "email"
        self.reporting_kind = 'letter'

        # Advice already given to the customer at time when trouble was first reported. 
        self.advice = advice

        # True if requested to customer when someone is about to arrive at their premises. 
        self.call_back = call_back

        # Priority of trouble call. 
        self.priority = priority

        # True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        self.inform_after_restored = inform_after_restored

        # Estimated restoration date and time last provided to the customer. 
        self.estimated_restore_date_time = estimated_restore_date_time

        # True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        self.inform_before_restored = inform_before_restored

        # Code for a reported hazard condition. 
        self.hazard_code = hazard_code

        # Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records. 
        self.first_call_date_time = first_call_date_time


        self._customer_data = None
        self.customer_data = customer_data

        self.trouble_period = trouble_period

        self._call_backs = []
        if call_backs is not None:
            self.call_backs = call_backs
        else:
            self.call_backs = []

        self._incident_record = None
        self.incident_record = incident_record


        super(TroubleTicket, self).__init__(**kw_args)
    # >>> trouble_ticket

    # <<< customer_data
    # @generated
    def get_customer_data(self):
        """ 
        """
        return self._customer_data

    def set_customer_data(self, value):
        if self._customer_data is not None:
            filtered = [x for x in self.customer_data.trouble_tickets if x != self]
            self._customer_data._trouble_tickets = filtered

        self._customer_data = value
        if self._customer_data is not None:
            self._customer_data._trouble_tickets.append(self)

    customer_data = property(get_customer_data, set_customer_data)
    # >>> customer_data

    # <<< trouble_period
    # @generated
    # Period between this source of trouble started and was resolved.
    trouble_period = None
    # >>> trouble_period

    # <<< call_backs
    # @generated
    def get_call_backs(self):
        """ 
        """
        return self._call_backs

    def set_call_backs(self, value):
        for p in self._call_backs:
            filtered = [q for q in p.trouble_tickets if q != self]
            self._call_backs._trouble_tickets = filtered
        for r in value:
            if self not in r._trouble_tickets:
                r._trouble_tickets.append(self)
        self._call_backs = value

    call_backs = property(get_call_backs, set_call_backs)

    def add_call_backs(self, *call_backs):
        for obj in call_backs:
            if self not in obj._trouble_tickets:
                obj._trouble_tickets.append(self)
            self._call_backs.append(obj)

    def remove_call_backs(self, *call_backs):
        for obj in call_backs:
            if self in obj._trouble_tickets:
                obj._trouble_tickets.remove(self)
            self._call_backs.remove(obj)
    # >>> call_backs

    # <<< incident_record
    # @generated
    def get_incident_record(self):
        """ 
        """
        return self._incident_record

    def set_incident_record(self, value):
        if self._incident_record is not None:
            filtered = [x for x in self.incident_record.trouble_tickets if x != self]
            self._incident_record._trouble_tickets = filtered

        self._incident_record = value
        if self._incident_record is not None:
            self._incident_record._trouble_tickets.append(self)

    incident_record = property(get_incident_record, set_incident_record)
    # >>> incident_record


    def __str__(self):
        """ Returns a string representation of the TroubleTicket.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< trouble_ticket.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TroubleTicket.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TroubleTicket", self.uri)
        if format:
            indent += ' ' * depth

        if self.customer_data is not None:
            s += '%s<%s:TroubleTicket.customer_data rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.customer_data.uri)
        if self.trouble_period is not None:
            s += '%s<%s:TroubleTicket.trouble_period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.trouble_period.uri)
        for obj in self.call_backs:
            s += '%s<%s:TroubleTicket.call_backs rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.incident_record is not None:
            s += '%s<%s:TroubleTicket.incident_record rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.incident_record.uri)
        s += '%s<%s:TroubleTicket.reporting_kind>%s</%s:TroubleTicket.reporting_kind>' % \
            (indent, ns_prefix, self.reporting_kind, ns_prefix)
        s += '%s<%s:TroubleTicket.advice>%s</%s:TroubleTicket.advice>' % \
            (indent, ns_prefix, self.advice, ns_prefix)
        s += '%s<%s:TroubleTicket.call_back>%s</%s:TroubleTicket.call_back>' % \
            (indent, ns_prefix, self.call_back, ns_prefix)
        s += '%s<%s:TroubleTicket.priority>%s</%s:TroubleTicket.priority>' % \
            (indent, ns_prefix, self.priority, ns_prefix)
        s += '%s<%s:TroubleTicket.inform_after_restored>%s</%s:TroubleTicket.inform_after_restored>' % \
            (indent, ns_prefix, self.inform_after_restored, ns_prefix)
        s += '%s<%s:TroubleTicket.estimated_restore_date_time>%s</%s:TroubleTicket.estimated_restore_date_time>' % \
            (indent, ns_prefix, self.estimated_restore_date_time, ns_prefix)
        s += '%s<%s:TroubleTicket.inform_before_restored>%s</%s:TroubleTicket.inform_before_restored>' % \
            (indent, ns_prefix, self.inform_before_restored, ns_prefix)
        s += '%s<%s:TroubleTicket.hazard_code>%s</%s:TroubleTicket.hazard_code>' % \
            (indent, ns_prefix, self.hazard_code, ns_prefix)
        s += '%s<%s:TroubleTicket.first_call_date_time>%s</%s:TroubleTicket.first_call_date_time>' % \
            (indent, ns_prefix, self.first_call_date_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "TroubleTicket")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> trouble_ticket.serialize


class IncidentRecord(Document):
    """ Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.
    """
    # <<< incident_record
    # @generated
    def __init__(self, incident_codes=None, period=None, trouble_tickets=None, **kw_args):
        """ Initialises a new 'IncidentRecord' instance.
        """

        self._incident_codes = []
        if incident_codes is not None:
            self.incident_codes = incident_codes
        else:
            self.incident_codes = []

        self.period = period

        self._trouble_tickets = []
        if trouble_tickets is not None:
            self.trouble_tickets = trouble_tickets
        else:
            self.trouble_tickets = []


        super(IncidentRecord, self).__init__(**kw_args)
    # >>> incident_record

    # <<< incident_codes
    # @generated
    def get_incident_codes(self):
        """ 
        """
        return self._incident_codes

    def set_incident_codes(self, value):
        for p in self._incident_codes:
            filtered = [q for q in p.incident_records if q != self]
            self._incident_codes._incident_records = filtered
        for r in value:
            if self not in r._incident_records:
                r._incident_records.append(self)
        self._incident_codes = value

    incident_codes = property(get_incident_codes, set_incident_codes)

    def add_incident_codes(self, *incident_codes):
        for obj in incident_codes:
            if self not in obj._incident_records:
                obj._incident_records.append(self)
            self._incident_codes.append(obj)

    def remove_incident_codes(self, *incident_codes):
        for obj in incident_codes:
            if self in obj._incident_records:
                obj._incident_records.remove(self)
            self._incident_codes.remove(obj)
    # >>> incident_codes

    # <<< period
    # @generated
    # Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
    period = None
    # >>> period

    # <<< trouble_tickets
    # @generated
    def get_trouble_tickets(self):
        """ 
        """
        return self._trouble_tickets

    def set_trouble_tickets(self, value):
        for x in self._trouble_tickets:
            x._incident_record = None
        for y in value:
            y._incident_record = self
        self._trouble_tickets = value

    trouble_tickets = property(get_trouble_tickets, set_trouble_tickets)

    def add_trouble_tickets(self, *trouble_tickets):
        for obj in trouble_tickets:
            obj._incident_record = self
            self._trouble_tickets.append(obj)

    def remove_trouble_tickets(self, *trouble_tickets):
        for obj in trouble_tickets:
            obj._incident_record = None
            self._trouble_tickets.remove(obj)
    # >>> trouble_tickets


    def __str__(self):
        """ Returns a string representation of the IncidentRecord.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< incident_record.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the IncidentRecord.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "IncidentRecord", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.incident_codes:
            s += '%s<%s:IncidentRecord.incident_codes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.period is not None:
            s += '%s<%s:IncidentRecord.period rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.period.uri)
        for obj in self.trouble_tickets:
            s += '%s<%s:IncidentRecord.trouble_tickets rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "IncidentRecord")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> incident_record.serialize


class ChangeSet(IdentifiedObject):
    """ The updates required in a transaction for an existing data set are grouped into a single ChangeSet. In data sets (e.g., NetworkDataSet), each major step in the ChangeSet is described through a separate ChangeItem associated with the data set. Within each data set, each inidividual object change is described with a seperate ChangeItem associated with the object.
    """
    # <<< change_set
    # @generated
    def __init__(self, land_bases=None, network_data_sets=None, change_items=None, status=None, documents=None, **kw_args):
        """ Initialises a new 'ChangeSet' instance.
        """

        if land_bases is not None:
            self.land_bases = land_bases
        else:
            self.land_bases = []

        self._network_data_sets = []
        if network_data_sets is not None:
            self.network_data_sets = network_data_sets
        else:
            self.network_data_sets = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self.status = status

        self._documents = []
        if documents is not None:
            self.documents = documents
        else:
            self.documents = []


        super(ChangeSet, self).__init__(**kw_args)
    # >>> change_set

    # <<< land_bases
    # @generated
    def add_land_bases(self, *land_bases):
        for obj in land_bases:
            self.land_bases.append(obj)

    def remove_land_bases(self, *land_bases):
        for obj in land_bases:
            self.land_bases.remove(obj)
    # >>> land_bases

    # <<< network_data_sets
    # @generated
    def get_network_data_sets(self):
        """ 
        """
        return self._network_data_sets

    def set_network_data_sets(self, value):
        for p in self._network_data_sets:
            filtered = [q for q in p.change_sets if q != self]
            self._network_data_sets._change_sets = filtered
        for r in value:
            if self not in r._change_sets:
                r._change_sets.append(self)
        self._network_data_sets = value

    network_data_sets = property(get_network_data_sets, set_network_data_sets)

    def add_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self not in obj._change_sets:
                obj._change_sets.append(self)
            self._network_data_sets.append(obj)

    def remove_network_data_sets(self, *network_data_sets):
        for obj in network_data_sets:
            if self in obj._change_sets:
                obj._change_sets.remove(self)
            self._network_data_sets.remove(obj)
    # >>> network_data_sets

    # <<< change_items
    # @generated
    def get_change_items(self):
        """ 
        """
        return self._change_items

    def set_change_items(self, value):
        for x in self._change_items:
            x._change_set = None
        for y in value:
            y._change_set = self
        self._change_items = value

    change_items = property(get_change_items, set_change_items)

    def add_change_items(self, *change_items):
        for obj in change_items:
            obj._change_set = self
            self._change_items.append(obj)

    def remove_change_items(self, *change_items):
        for obj in change_items:
            obj._change_set = None
            self._change_items.remove(obj)
    # >>> change_items

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
            filtered = [q for q in p.change_sets if q != self]
            self._documents._change_sets = filtered
        for r in value:
            if self not in r._change_sets:
                r._change_sets.append(self)
        self._documents = value

    documents = property(get_documents, set_documents)

    def add_documents(self, *documents):
        for obj in documents:
            if self not in obj._change_sets:
                obj._change_sets.append(self)
            self._documents.append(obj)

    def remove_documents(self, *documents):
        for obj in documents:
            if self in obj._change_sets:
                obj._change_sets.remove(self)
            self._documents.remove(obj)
    # >>> documents


    def __str__(self):
        """ Returns a string representation of the ChangeSet.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< change_set.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ChangeSet.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ChangeSet", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.land_bases:
            s += '%s<%s:ChangeSet.land_bases rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:ChangeSet.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.change_items:
            s += '%s<%s:ChangeSet.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.status is not None:
            s += '%s<%s:ChangeSet.status rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.status.uri)
        for obj in self.documents:
            s += '%s<%s:ChangeSet.documents rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ChangeSet")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> change_set.serialize


class OutageReport(Document):
    """ Document with statistics of an outage.
    """
    # <<< outage_report
    # @generated
    def __init__(self, average_cml=0.0, outage_duration=0.0, customer_count=0, total_cml=0.0, outage_record=None, outage_history=None, **kw_args):
        """ Initialises a new 'OutageReport' instance.
        """
        # Average Customer Minutes Lost (CML) for this outage. 
        self.average_cml = average_cml

        # Total outage duration. 
        self.outage_duration = outage_duration

        # Total number of outaged customers. 
        self.customer_count = customer_count

        # Total Customer Minutes Lost (CML). 
        self.total_cml = total_cml


        self._outage_record = None
        self.outage_record = outage_record

        self._outage_history = None
        self.outage_history = outage_history


        super(OutageReport, self).__init__(**kw_args)
    # >>> outage_report

    # <<< outage_record
    # @generated
    def get_outage_record(self):
        """ reference to related document
        """
        return self._outage_record

    def set_outage_record(self, value):
        if self._outage_record is not None:
            self._outage_record._outage_report = None

        self._outage_record = value
        if self._outage_record is not None:
            self._outage_record._outage_report = self

    outage_record = property(get_outage_record, set_outage_record)
    # >>> outage_record

    # <<< outage_history
    # @generated
    def get_outage_history(self):
        """ OutageHistory of a customer, which may include this OutageReport.
        """
        return self._outage_history

    def set_outage_history(self, value):
        if self._outage_history is not None:
            filtered = [x for x in self.outage_history.outage_reports if x != self]
            self._outage_history._outage_reports = filtered

        self._outage_history = value
        if self._outage_history is not None:
            self._outage_history._outage_reports.append(self)

    outage_history = property(get_outage_history, set_outage_history)
    # >>> outage_history


    def __str__(self):
        """ Returns a string representation of the OutageReport.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_report.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageReport.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageReport", self.uri)
        if format:
            indent += ' ' * depth

        if self.outage_record is not None:
            s += '%s<%s:OutageReport.outage_record rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_record.uri)
        if self.outage_history is not None:
            s += '%s<%s:OutageReport.outage_history rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_history.uri)
        s += '%s<%s:OutageReport.average_cml>%s</%s:OutageReport.average_cml>' % \
            (indent, ns_prefix, self.average_cml, ns_prefix)
        s += '%s<%s:OutageReport.outage_duration>%s</%s:OutageReport.outage_duration>' % \
            (indent, ns_prefix, self.outage_duration, ns_prefix)
        s += '%s<%s:OutageReport.customer_count>%s</%s:OutageReport.customer_count>' % \
            (indent, ns_prefix, self.customer_count, ns_prefix)
        s += '%s<%s:OutageReport.total_cml>%s</%s:OutageReport.total_cml>' % \
            (indent, ns_prefix, self.total_cml, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageReport")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_report.serialize


class LandBase(Document):
    """ Land base data.
    """
    pass
    # <<< land_base
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'LandBase' instance.
        """


        super(LandBase, self).__init__(**kw_args)
    # >>> land_base


    def __str__(self):
        """ Returns a string representation of the LandBase.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< land_base.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LandBase.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LandBase", self.uri)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "LandBase")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> land_base.serialize


class Circuit(EquipmentContainer):
    """ EquipmentContainer that will typically include conductors, energy consumers, transformers and transformer windings, switches, shunt compensators, etc., likely at different voltages. Circuit extends from a substation to a set of open points (radial circuit), or to a second substation (looped circuit). It generally starts with a switching device, located in a substation. Membership in a Circuit is based on the nominal or design system configuration, but the electrical connectivity will change during switching operations.
    """
    pass
    # <<< circuit
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Circuit' instance.
        """


        super(Circuit, self).__init__(**kw_args)
    # >>> circuit


    def __str__(self):
        """ Returns a string representation of the Circuit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< circuit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Circuit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Circuit", self.uri)
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
        for obj in self.change_items:
            s += '%s<%s:PowerSystemResource.change_items rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.asset_roles:
            s += '%s<%s:PowerSystemResource.asset_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        for obj in self.safety_documents:
            s += '%s<%s:PowerSystemResource.safety_documents rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.measurements:
            s += '%s<%s:PowerSystemResource.measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.erp_organisation_roles:
            s += '%s<%s:PowerSystemResource.erp_organisation_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psrevent:
            s += '%s<%s:PowerSystemResource.psrevent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.schedule_steps:
            s += '%s<%s:PowerSystemResource.schedule_steps rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.document_roles:
            s += '%s<%s:PowerSystemResource.document_roles rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.circuit_sections:
            s += '%s<%s:PowerSystemResource.circuit_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.network_data_sets:
            s += '%s<%s:PowerSystemResource.network_data_sets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipments:
            s += '%s<%s:EquipmentContainer.equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Circuit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> circuit.serialize


# <<< inf_operations
# @generated
# >>> inf_operations
