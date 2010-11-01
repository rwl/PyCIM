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

""" An extension to the Core and Wires packages that models information on the current and planned network configuration. These entities are optional within typical network applications.
"""

from cim14v13.iec61970.core import IdentifiedObject
from cim14v13.iec61970.core import IrregularIntervalSchedule

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimOutage"

ns_uri = "http://iec.ch/TC57/CIM-generic#Outage"

class ClearanceTag(IdentifiedObject):
    """ A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.
    """
    # <<< clearance_tag
    # @generated
    def __init__(self, authority_name='', work_end_time='', phase_check_req_flag=False, deenergize_req_flag=False, tag_issue_time='', work_description='', work_start_time='', ground_req_flag=False, conducting_equipment=None, safety_document=None, clearance_tag_type=None, *args, **kw_args):
        """ Initialises a new 'ClearanceTag' instance.

        @param authority_name: The name of the person who is authorized to issue the tag 
        @param work_end_time: The time at which the clearance tag is scheduled to be removed 
        @param phase_check_req_flag: Set true if equipment phasing must be checked 
        @param deenergize_req_flag: Set true if equipment must be deenergized 
        @param tag_issue_time: The time at which the clearance tag was issued 
        @param work_description: Description of the work to be performed 
        @param work_start_time: The time at which the clearance tag is scheduled to be set. 
        @param ground_req_flag: Set true if equipment must be grounded 
        @param conducting_equipment: Conducting equipment may have multiple clearance tags for authorized field work
        @param safety_document:
        @param clearance_tag_type: The type of tag, depending on the purpose of the work to be performed and/or the type of supervisory control allowed.
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


        super(ClearanceTag, self).__init__(*args, **kw_args)
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



class ClearanceTagType(IdentifiedObject):
    """ Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.
    """
    # <<< clearance_tag_type
    # @generated
    def __init__(self, clearance_tags=None, *args, **kw_args):
        """ Initialises a new 'ClearanceTagType' instance.

        @param clearance_tags: The ClearanceTags currently being defined for this type.
        """

        self._clearance_tags = []
        if clearance_tags is not None:
            self.clearance_tags = clearance_tags
        else:
            self.clearance_tags = []


        super(ClearanceTagType, self).__init__(*args, **kw_args)
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



class OutageSchedule(IrregularIntervalSchedule):
    """ The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.
    """
    # <<< outage_schedule
    # @generated
    def __init__(self, power_system_resource=None, switching_operations=None, planned_outage=None, *args, **kw_args):
        """ Initialises a new 'OutageSchedule' instance.

        @param power_system_resource: A power system resource may have an outage schedule
        @param switching_operations: An OutageSchedule may operate many switches.
        @param planned_outage:
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


        super(OutageSchedule, self).__init__(*args, **kw_args)
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



class SwitchingOperation(IdentifiedObject):
    """ A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """
    # <<< switching_operation
    # @generated
    def __init__(self, new_state='open', operation_time='', outage_schedule=None, switches=None, *args, **kw_args):
        """ Initialises a new 'SwitchingOperation' instance.

        @param new_state: The switch position that shall result from this SwitchingOperation Values are: "open", "close"
        @param operation_time: Time of operation in same units as OutageSchedule.xAxixUnits. 
        @param outage_schedule: An OutageSchedule may operate many switches.
        @param switches: A switch may be operated by many schedules.
        """
        # The switch position that shall result from this SwitchingOperation Values are: "open", "close"
        self.new_state = new_state

        # Time of operation in same units as OutageSchedule.xAxixUnits. 
        self.operation_time = operation_time


        self._outage_schedule = None
        self.outage_schedule = outage_schedule

        self._switches = []
        if switches is not None:
            self.switches = switches
        else:
            self.switches = []


        super(SwitchingOperation, self).__init__(*args, **kw_args)
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



# <<< outage
# @generated
# >>> outage
