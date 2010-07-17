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

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""

from cim.iec61970.core import IdentifiedObject
from cim.iec61970.core import IrregularIntervalSchedule

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.outage"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Outage"

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """
    # <<< clearance_tag
    # @generated
    def __init__(self, authority_name='', work_end_time='', phase_check_req_flag=False, deenergize_req_flag=False, tag_issue_time='', work_description='', work_start_time='', ground_req_flag=False, conducting_equipment=None, safety_document=None, clearance_tag_type=None, **kw_args):
        """ Initialises a new 'ClearanceTag' instance.
        """
        # The name of the person who is authorized to issue the tag 
        self.authority_name = authority_name

        # The time at which the clearance tag is scheduled to be removed 
        self.work_end_time = work_end_time

        # Set true if equipment phasing must be checked 
        self.phase_check_req_flag = phase_check_req_flag

        # Set true if equipment must be deenergized 
        self.deenergize_req_flag = deenergize_req_flag

        # The time at which the clearance tag was issued 
        self.tag_issue_time = tag_issue_time

        # Description of the work to be performed 
        self.work_description = work_description

        # The time at which the clearance tag is scheduled to be set. 
        self.work_start_time = work_start_time

        # Set true if equipment must be grounded 
        self.ground_req_flag = ground_req_flag


        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._safety_document = None
        self.safety_document = safety_document

        self._clearance_tag_type = None
        self.clearance_tag_type = clearance_tag_type


        super(ClearanceTag, self).__init__(**kw_args)
    # >>> clearance_tag

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ Conducting equipment may have multiple clearance tags for authorized field work
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        if self._conducting_equipment is not None:
            filtered = [x for x in self.conducting_equipment.clearance_tags if x != self]
            self._conducting_equipment._clearance_tags = filtered

        self._conducting_equipment = value
        if self._conducting_equipment is not None:
            self._conducting_equipment._clearance_tags.append(self)

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)
    # >>> conducting_equipment

    # <<< safety_document
    # @generated
    def get_safety_document(self):
        """ 
        """
        return self._safety_document

    def set_safety_document(self, value):
        if self._safety_document is not None:
            filtered = [x for x in self.safety_document.clearance_tags if x != self]
            self._safety_document._clearance_tags = filtered

        self._safety_document = value
        if self._safety_document is not None:
            self._safety_document._clearance_tags.append(self)

    safety_document = property(get_safety_document, set_safety_document)
    # >>> safety_document

    # <<< clearance_tag_type
    # @generated
    def get_clearance_tag_type(self):
        """ The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
        """
        return self._clearance_tag_type

    def set_clearance_tag_type(self, value):
        if self._clearance_tag_type is not None:
            filtered = [x for x in self.clearance_tag_type.clearance_tags if x != self]
            self._clearance_tag_type._clearance_tags = filtered

        self._clearance_tag_type = value
        if self._clearance_tag_type is not None:
            self._clearance_tag_type._clearance_tags.append(self)

    clearance_tag_type = property(get_clearance_tag_type, set_clearance_tag_type)
    # >>> clearance_tag_type


    def __str__(self):
        """ Returns a string representation of the ClearanceTag.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< clearance_tag.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ClearanceTag.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ClearanceTag", self.uri)
        if format:
            indent += ' ' * depth

        if self.conducting_equipment is not None:
            s += '%s<%s:ClearanceTag.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        if self.safety_document is not None:
            s += '%s<%s:ClearanceTag.safety_document rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.safety_document.uri)
        if self.clearance_tag_type is not None:
            s += '%s<%s:ClearanceTag.clearance_tag_type rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.clearance_tag_type.uri)
        s += '%s<%s:ClearanceTag.authority_name>%s</%s:ClearanceTag.authority_name>' % \
            (indent, ns_prefix, self.authority_name, ns_prefix)
        s += '%s<%s:ClearanceTag.work_end_time>%s</%s:ClearanceTag.work_end_time>' % \
            (indent, ns_prefix, self.work_end_time, ns_prefix)
        s += '%s<%s:ClearanceTag.phase_check_req_flag>%s</%s:ClearanceTag.phase_check_req_flag>' % \
            (indent, ns_prefix, self.phase_check_req_flag, ns_prefix)
        s += '%s<%s:ClearanceTag.deenergize_req_flag>%s</%s:ClearanceTag.deenergize_req_flag>' % \
            (indent, ns_prefix, self.deenergize_req_flag, ns_prefix)
        s += '%s<%s:ClearanceTag.tag_issue_time>%s</%s:ClearanceTag.tag_issue_time>' % \
            (indent, ns_prefix, self.tag_issue_time, ns_prefix)
        s += '%s<%s:ClearanceTag.work_description>%s</%s:ClearanceTag.work_description>' % \
            (indent, ns_prefix, self.work_description, ns_prefix)
        s += '%s<%s:ClearanceTag.work_start_time>%s</%s:ClearanceTag.work_start_time>' % \
            (indent, ns_prefix, self.work_start_time, ns_prefix)
        s += '%s<%s:ClearanceTag.ground_req_flag>%s</%s:ClearanceTag.ground_req_flag>' % \
            (indent, ns_prefix, self.ground_req_flag, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ClearanceTag")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> clearance_tag.serialize


class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """
    # <<< clearance_tag_type
    # @generated
    def __init__(self, clearance_tags=None, **kw_args):
        """ Initialises a new 'ClearanceTagType' instance.
        """

        self._clearance_tags = []
        if clearance_tags is not None:
            self.clearance_tags = clearance_tags
        else:
            self.clearance_tags = []


        super(ClearanceTagType, self).__init__(**kw_args)
    # >>> clearance_tag_type

    # <<< clearance_tags
    # @generated
    def get_clearance_tags(self):
        """ The ClearanceTags currently being defined for this type.
        """
        return self._clearance_tags

    def set_clearance_tags(self, value):
        for x in self._clearance_tags:
            x._clearance_tag_type = None
        for y in value:
            y._clearance_tag_type = self
        self._clearance_tags = value

    clearance_tags = property(get_clearance_tags, set_clearance_tags)

    def add_clearance_tags(self, *clearance_tags):
        for obj in clearance_tags:
            obj._clearance_tag_type = self
            self._clearance_tags.append(obj)

    def remove_clearance_tags(self, *clearance_tags):
        for obj in clearance_tags:
            obj._clearance_tag_type = None
            self._clearance_tags.remove(obj)
    # >>> clearance_tags


    def __str__(self):
        """ Returns a string representation of the ClearanceTagType.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< clearance_tag_type.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ClearanceTagType.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ClearanceTagType", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.clearance_tags:
            s += '%s<%s:ClearanceTagType.clearance_tags rdf:resource="#%s"/>' % \
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "ClearanceTagType")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> clearance_tag_type.serialize


class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """
    # <<< outage_schedule
    # @generated
    def __init__(self, power_system_resource=None, switching_operations=None, planned_outage=None, **kw_args):
        """ Initialises a new 'OutageSchedule' instance.
        """

        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._switching_operations = []
        if switching_operations is not None:
            self.switching_operations = switching_operations
        else:
            self.switching_operations = []

        self._planned_outage = None
        self.planned_outage = planned_outage


        super(OutageSchedule, self).__init__(**kw_args)
    # >>> outage_schedule

    # <<< power_system_resource
    # @generated
    def get_power_system_resource(self):
        """ A power system resource may have an outage schedule
        """
        return self._power_system_resource

    def set_power_system_resource(self, value):
        if self._power_system_resource is not None:
            self._power_system_resource._outage_schedule = None

        self._power_system_resource = value
        if self._power_system_resource is not None:
            self._power_system_resource._outage_schedule = self

    power_system_resource = property(get_power_system_resource, set_power_system_resource)
    # >>> power_system_resource

    # <<< switching_operations
    # @generated
    def get_switching_operations(self):
        """ An OutageSchedule may operate many switches.
        """
        return self._switching_operations

    def set_switching_operations(self, value):
        for x in self._switching_operations:
            x._outage_schedule = None
        for y in value:
            y._outage_schedule = self
        self._switching_operations = value

    switching_operations = property(get_switching_operations, set_switching_operations)

    def add_switching_operations(self, *switching_operations):
        for obj in switching_operations:
            obj._outage_schedule = self
            self._switching_operations.append(obj)

    def remove_switching_operations(self, *switching_operations):
        for obj in switching_operations:
            obj._outage_schedule = None
            self._switching_operations.remove(obj)
    # >>> switching_operations

    # <<< planned_outage
    # @generated
    def get_planned_outage(self):
        """ 
        """
        return self._planned_outage

    def set_planned_outage(self, value):
        if self._planned_outage is not None:
            filtered = [x for x in self.planned_outage.outage_schedules if x != self]
            self._planned_outage._outage_schedules = filtered

        self._planned_outage = value
        if self._planned_outage is not None:
            self._planned_outage._outage_schedules.append(self)

    planned_outage = property(get_planned_outage, set_planned_outage)
    # >>> planned_outage


    def __str__(self):
        """ Returns a string representation of the OutageSchedule.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< outage_schedule.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the OutageSchedule.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "OutageSchedule", self.uri)
        if format:
            indent += ' ' * depth

        if self.power_system_resource is not None:
            s += '%s<%s:OutageSchedule.power_system_resource rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.power_system_resource.uri)
        for obj in self.switching_operations:
            s += '%s<%s:OutageSchedule.switching_operations rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.planned_outage is not None:
            s += '%s<%s:OutageSchedule.planned_outage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.planned_outage.uri)
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
        s += '%s<%s:BasicIntervalSchedule.value2_multiplier>%s</%s:BasicIntervalSchedule.value2_multiplier>' % \
            (indent, ns_prefix, self.value2_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_unit>%s</%s:BasicIntervalSchedule.value1_unit>' % \
            (indent, ns_prefix, self.value1_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value2_unit>%s</%s:BasicIntervalSchedule.value2_unit>' % \
            (indent, ns_prefix, self.value2_unit, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.value1_multiplier>%s</%s:BasicIntervalSchedule.value1_multiplier>' % \
            (indent, ns_prefix, self.value1_multiplier, ns_prefix)
        s += '%s<%s:BasicIntervalSchedule.start_time>%s</%s:BasicIntervalSchedule.start_time>' % \
            (indent, ns_prefix, self.start_time, ns_prefix)
        for obj in self.time_points:
            s += '%s<%s:IrregularIntervalSchedule.time_points rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "OutageSchedule")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> outage_schedule.serialize


class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """
    # <<< switching_operation
    # @generated
    def __init__(self, new_state='open', operation_time='', outage_schedule=None, switches=None, **kw_args):
        """ Initialises a new 'SwitchingOperation' instance.
        """
        # The switch position that shall result from this SwitchingOperation Values are: "open", "close"
        self.new_state = 'open'

        # Time of operation in same units as OutageSchedule.xAxixUnits. 
        self.operation_time = operation_time


        self._outage_schedule = None
        self.outage_schedule = outage_schedule

        self._switches = []
        if switches is not None:
            self.switches = switches
        else:
            self.switches = []


        super(SwitchingOperation, self).__init__(**kw_args)
    # >>> switching_operation

    # <<< outage_schedule
    # @generated
    def get_outage_schedule(self):
        """ An OutageSchedule may operate many switches.
        """
        return self._outage_schedule

    def set_outage_schedule(self, value):
        if self._outage_schedule is not None:
            filtered = [x for x in self.outage_schedule.switching_operations if x != self]
            self._outage_schedule._switching_operations = filtered

        self._outage_schedule = value
        if self._outage_schedule is not None:
            self._outage_schedule._switching_operations.append(self)

    outage_schedule = property(get_outage_schedule, set_outage_schedule)
    # >>> outage_schedule

    # <<< switches
    # @generated
    def get_switches(self):
        """ A switch may be operated by many schedules.
        """
        return self._switches

    def set_switches(self, value):
        for p in self._switches:
            filtered = [q for q in p.switching_operations if q != self]
            self._switches._switching_operations = filtered
        for r in value:
            if self not in r._switching_operations:
                r._switching_operations.append(self)
        self._switches = value

    switches = property(get_switches, set_switches)

    def add_switches(self, *switches):
        for obj in switches:
            if self not in obj._switching_operations:
                obj._switching_operations.append(self)
            self._switches.append(obj)

    def remove_switches(self, *switches):
        for obj in switches:
            if self in obj._switching_operations:
                obj._switching_operations.remove(self)
            self._switches.remove(obj)
    # >>> switches


    def __str__(self):
        """ Returns a string representation of the SwitchingOperation.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switching_operation.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SwitchingOperation.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SwitchingOperation", self.uri)
        if format:
            indent += ' ' * depth

        if self.outage_schedule is not None:
            s += '%s<%s:SwitchingOperation.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.switches:
            s += '%s<%s:SwitchingOperation.switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SwitchingOperation.new_state>%s</%s:SwitchingOperation.new_state>' % \
            (indent, ns_prefix, self.new_state, ns_prefix)
        s += '%s<%s:SwitchingOperation.operation_time>%s</%s:SwitchingOperation.operation_time>' % \
            (indent, ns_prefix, self.operation_time, ns_prefix)
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
        s += '%s</%s:%s>' % (indent, ns_prefix, "SwitchingOperation")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switching_operation.serialize


# <<< outage
# @generated
# >>> outage
