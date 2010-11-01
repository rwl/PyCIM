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

""" TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Documentation package is used for the modeling of business documents. Some of these may be electronic realizations of legacy paper document, and some may be electronic information exchanges or collections. Documents will typically reference or describe one or more CIM objects. The DataSets package is used to describe documents tyically used for exchange of collections of object descriptions (e.g., NetworkDataSet). The operational package is used to define documents related to distribution operations business processes (e.g., OperationalRestriction, SwitchingSchedule). TroubleTickets are used by Customers to report problems related to the elctrical distribution network. TroubleTickets may be grouped and be related to a PlannedOutage, OutageNotification and/or PowerSystemResource. The Outage package defines classes related to outage management (OutageStep, OutageRecord, OutageReport).'
"""

from cim15v01.iec61970.core import IdentifiedObject
from cim15v01.iec61968.informative.inf_common import Role
from cim15v01.iec61968.common import Document
from cim15v01.iec61968.common import ActivityRecord
from cim15v01.iec61970.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfOperations"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfOperations"

class SwitchingStep(IdentifiedObject):
    """ A single step within a SwitchingSchedule. Could be a switching operation (applying a network alteration), or issuing a safety document. Note: Inherited attribute IdentifiedObject.name is used to hold the sequence number.
    """
    # <<< switching_step
    # @generated
    def __init__(self, status_kind='confirmed', desired_end_state='', text='', required_control_action='', required_control_action_interval=None, safety_document=None, switching_schedule=None, erp_person_role=None, power_system_resources=None, *args, **kw_args):
        """ Initialises a new 'SwitchingStep' instance.

        @param status_kind: Status of this SwitchingStep. Values are: "confirmed", "skipped", "aborted", "instructed", "proposed"
        @param desired_end_state: Desired end state for the associated PowerSystemResource as a result of this schedule step. 
        @param text: Information regarding this switching schedule step. 
        @param required_control_action: Control actions required to perform this step. 
        @param required_control_action_interval: Interval between 'requiredControlAction' was issued and completed.
        @param safety_document:
        @param switching_schedule:
        @param erp_person_role:
        @param power_system_resources:
        """
        # Status of this SwitchingStep. Values are: "confirmed", "skipped", "aborted", "instructed", "proposed"
        self.status_kind = status_kind

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


        super(SwitchingStep, self).__init__(*args, **kw_args)
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



class ErpPersonScheduleStepRole(Role):
    """ Roles played between Persons and Schedule Steps.
    """
    # <<< erp_person_schedule_step_role
    # @generated
    def __init__(self, switching_step=None, erp_person=None, *args, **kw_args):
        """ Initialises a new 'ErpPersonScheduleStepRole' instance.

        @param switching_step:
        @param erp_person:
        """

        self._switching_step = None
        self.switching_step = switching_step

        self._erp_person = None
        self.erp_person = erp_person


        super(ErpPersonScheduleStepRole, self).__init__(*args, **kw_args)
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



class OperationalRestriction(Document):
    """ A document that can be associated with a device to describe any sort of restrictions compared with the original manufacturer's specification e.g. temporary maximum loadings, maximum switching current, do not operate if bus couplers are open etc etc.  Since it is used in the network operations domain, it is associated with ConductingEquipment. In the UK, for example, if a breaker or switch ever mal-operates, this is reported centrally and utilities use their asset systems to identify all the installed devices of the same manufacturer's type. They then apply operational restrictions in the operational systems to warn operators of potential problems. After appropriate inspection and maintenance, the operational restrictions may be removed.
    """
    # <<< operational_restriction
    # @generated
    def __init__(self, active_period=None, *args, **kw_args):
        """ Initialises a new 'OperationalRestriction' instance.

        @param active_period: Interval during which the restriction is applied.
        """

        self.active_period = active_period


        super(OperationalRestriction, self).__init__(*args, **kw_args)
    # >>> operational_restriction

    # <<< active_period
    # @generated
    # Interval during which the restriction is applied.
    active_period = None
    # >>> active_period



class SafetyDocument(Document):
    """ A document restricting or authorising works on electrical equipment (for example a permit to work, sanction for test, limitation of access, or certificate of isolation), defined based upon organisational practices. Note: SafetyDocument may refer to ClearanceTag-s associated with ConductingEquipment for which the SafetyDocument is issued.
    """
    # <<< safety_document
    # @generated
    def __init__(self, power_system_resource=None, schedule_steps=None, clearance_tags=None, *args, **kw_args):
        """ Initialises a new 'SafetyDocument' instance.

        @param power_system_resource:
        @param schedule_steps:
        @param clearance_tags:
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


        super(SafetyDocument, self).__init__(*args, **kw_args)
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



class OutageStep(IdentifiedObject):
    """ Holds an outage start and end time for each supply point of an outage record. The supply point for a given step is the associated PowerSystemResource instance.
    """
    # <<< outage_step
    # @generated
    def __init__(self, job_priority='', total_cml=0.0, estimated_restore_date_time='', average_cml=0.0, shock_reported=False, special_customer_count=0, caller_count=0, damage=False, critical_customer_count=0, fatality=False, total_customer_count=0, injury=False, crews=None, outage_codes=None, outage_record=None, status=None, no_power_interval=None, conducting_equipment_roles=None, *args, **kw_args):
        """ Initialises a new 'OutageStep' instance.

        @param job_priority: 
        @param total_cml: Total Customer Minutes Lost (CML) for this supply point for this outage. 
        @param estimated_restore_date_time: Estimated time of restoration. 
        @param average_cml: Average Customer Minutes Lost (CML) for this supply point for this outage. 
        @param shock_reported: True if shocks reported by caller or engineer. 
        @param special_customer_count: Number of customers with high reliability required. 
        @param caller_count: Number of customers phoning in. 
        @param damage: True if damage reported by caller or engineer. 
        @param critical_customer_count: Number of customers with critical needs, e.g., with a dialysis machine. 
        @param fatality: True if fatalities reported by caller or engineer. 
        @param total_customer_count: Number of customers connected to the PowerSystemResource. 
        @param injury: True if injuries reported by caller or engineer. 
        @param crews:
        @param outage_codes: Multiple outage codes may apply to an outage step.
        @param outage_record:
        @param status:
        @param no_power_interval: Date and time interval between loss and restoration of power.
        @param conducting_equipment_roles:
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


        super(OutageStep, self).__init__(*args, **kw_args)
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



class ComplianceEvent(ActivityRecord):
    """ Compliance events are used for reporting regulatory or contract compliance issues and/or variances. These might be created as a consequence of local business processes and associated rules. It is anticipated that this class will be customised extensively to meet local implementation needs. Use inherited 'category' to indicate that, for example, expected performance will not be met or reported as mandated.
    """
    # <<< compliance_event
    # @generated
    def __init__(self, compliance_type='', deadline='', *args, **kw_args):
        """ Initialises a new 'ComplianceEvent' instance.

        @param compliance_type: Type of compliance event indicating, for example, types of regulatory and/or contractual compliance events where expected performance will not be met or reported as mandated. 
        @param deadline: The deadline for compliance. 
        """
        # Type of compliance event indicating, for example, types of regulatory and/or contractual compliance events where expected performance will not be met or reported as mandated. 
        self.compliance_type = compliance_type

        # The deadline for compliance. 
        self.deadline = deadline



        super(ComplianceEvent, self).__init__(*args, **kw_args)
    # >>> compliance_event



class PSREvent(ActivityRecord):
    """ Event recording the change in operational status of a PowerSystemResource.
    """
    # <<< psrevent
    # @generated
    def __init__(self, kind='in_service', power_system_resource=None, *args, **kw_args):
        """ Initialises a new 'PSREvent' instance.

        @param kind: Kind of event. Values are: "in_service", "unknown", "pending_add", "out_of_service", "pending_remove", "other", "pending_replace"
        @param power_system_resource: Power system resource that generated this event.
        """
        # Kind of event. Values are: "in_service", "unknown", "pending_add", "out_of_service", "pending_remove", "other", "pending_replace"
        self.kind = kind


        self._power_system_resource = None
        self.power_system_resource = power_system_resource


        super(PSREvent, self).__init__(*args, **kw_args)
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



class OutageCode(IdentifiedObject):
    """ Classification of outage types. Multiple outage codes may apply to a given outage or outage step.The primary overall outage type is recorded in OutageRecord.outageType. There may be more than one classification per outage step and/or per outage record. Example codes/subcodes include: weather/ice, weather/lightning, wildlife/squirrel, wildlife/bird, burned/overload, burned/weather, wire down/accident, wire down/tree, wire down/vandalism, etc. The typical 'outage code' is in the inherited 'name' attribute. The code is described in the inherited 'description' attribute.
    """
    # <<< outage_code
    # @generated
    def __init__(self, sub_code='', outage_records=None, outage_steps=None, *args, **kw_args):
        """ Initialises a new 'OutageCode' instance.

        @param sub_code: The main code is stored in the inherited .name. This sub-code provides an additional level of classification detail. 
        @param outage_records:
        @param outage_steps:
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


        super(OutageCode, self).__init__(*args, **kw_args)
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



class OutageStepPsrRole(Role):
    """ Roles played between Power System Resources and Outage Steps. Examples roles include: normal supply, actual supply, interrupting device, restoration device.
    """
    # <<< outage_step_psr_role
    # @generated
    def __init__(self, conducting_equipment=None, outage_step=None, *args, **kw_args):
        """ Initialises a new 'OutageStepPsrRole' instance.

        @param conducting_equipment:
        @param outage_step:
        """

        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment

        self._outage_step = None
        self.outage_step = outage_step


        super(OutageStepPsrRole, self).__init__(*args, **kw_args)
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



class NetworkDataSet(IdentifiedObject):
    """ Categorized as a type of document, model of a portion of the electrical network that includes a list of the equipment, along with relevant connectivity, electrical characteristics, geographical location, and various parameters associated with the equipment.
    """
    # <<< network_data_set
    # @generated
    def __init__(self, category='', documents=None, circuit_sections=None, change_sets=None, power_system_resources=None, land_bases=None, change_items=None, status=None, *args, **kw_args):
        """ Initialises a new 'NetworkDataSet' instance.

        @param category: Category of network data set. 
        @param documents:
        @param circuit_sections: A NetworkDataSet may contain sections of circuits (vs. whole circuits).
        @param change_sets:
        @param power_system_resources:
        @param land_bases:
        @param change_items:
        @param status:
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

        if land_bases is not None:
            self.land_bases = land_bases
        else:
            self.land_bases = []

        self._change_items = []
        if change_items is not None:
            self.change_items = change_items
        else:
            self.change_items = []

        self.status = status


        super(NetworkDataSet, self).__init__(*args, **kw_args)
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

    # <<< land_bases
    # @generated
    def add_land_bases(self, *land_bases):
        for obj in land_bases:
            self.land_bases.append(obj)

    def remove_land_bases(self, *land_bases):
        for obj in land_bases:
            self.land_bases.remove(obj)
    # >>> land_bases

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



class CircuitSection(IdentifiedObject):
    """ Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.
    """
    # <<< circuit_section
    # @generated
    def __init__(self, connection_kind='electrically_connected', conductor_assets=None, network_data_sets=None, power_system_resources=None, circuits=None, *args, **kw_args):
        """ Initialises a new 'CircuitSection' instance.

        @param connection_kind: Kind of this circuit section. Values are: "electrically_connected", "nominally_connected", "other", "as_built"
        @param conductor_assets:
        @param network_data_sets:
        @param power_system_resources:
        @param circuits:
        """
        # Kind of this circuit section. Values are: "electrically_connected", "nominally_connected", "other", "as_built"
        self.connection_kind = connection_kind


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


        super(CircuitSection, self).__init__(*args, **kw_args)
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



class OutageRecord(Document):
    """ A document describing details of an outage in part of the electrical network, typically produced by a SCADA system following a breaker trip, or within a Trouble Call System by grouping customer calls. This has an associated OutageStep for each supply point. Primary cause of the outage is captured in 'category'. In some countries all outage restoration is performed using a SwitchingSchedule which complements the OutageRecord and records the ErpPersons (crew) and any planned Work. In other systems, it may be acceptable to manage outages including new WorkTasks without switching schedules. Note: The relationship between OutageRecord and ErpPerson and Crew is inherited as each is a type of Document.
    """
    # <<< outage_record
    # @generated
    def __init__(self, mode='', damage_code='', action_taken='', end_date_time='', is_planned=False, outage_report=None, outage_codes=None, outage_steps=None, *args, **kw_args):
        """ Initialises a new 'OutageRecord' instance.

        @param mode: Value of ErpOrganisation.mode at the time of OutageRecord.startDateTime. 
        @param damage_code: The damage code relative to the associated PowerSystemResource(s) and/or Asset(s). Examples include broken, burnout, failure, flashed (burned), manually operated, wire down, no damage - rolling blackout, none. 
        @param action_taken: Overall action taken to resolve outage (details are in 'WorkTasks'). 
        @param end_date_time: Date and time restoration was completed for all customers impacted by this outage. 
        @param is_planned: True if planned, false otherwise (for example due to a breaker trip). 
        @param outage_report:
        @param outage_codes: Multiple outage codes may apply to an outage record.
        @param outage_steps:
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


        super(OutageRecord, self).__init__(*args, **kw_args)
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



class CallBack(IdentifiedObject):
    """ Information about a planned CallBack or a CallBack that has occurred, from the utility to a customer regarding the status and plans about resolving trouble, performing work, etc.
    """
    # <<< call_back
    # @generated
    def __init__(self, advice='', contact_detail='', comment='', problem_info='', date_time='', erp_persons=None, appointments=None, status=None, trouble_tickets=None, *args, **kw_args):
        """ Initialises a new 'CallBack' instance.

        @param advice: Advice already given to the customer during this call back. 
        @param contact_detail: Additional contact details that are not provided for ErpPerson with ErpTelephoneNumber. 
        @param comment: Comments by customer during this call back. 
        @param problem_info: Descriptiion of the problem reported during this call back. 
        @param date_time: (if callback already occured) Date and time when this call back occurred. 
        @param erp_persons:
        @param appointments:
        @param status:
        @param trouble_tickets:
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


        super(CallBack, self).__init__(*args, **kw_args)
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



class ChangeItem(IdentifiedObject):
    """ Description for a single change within an ordered list of changes.
    """
    # <<< change_item
    # @generated
    def __init__(self, kind='add', sequence_number=0, power_system_resource=None, location=None, organisation=None, status=None, asset=None, document=None, gml_observation=None, erp_person=None, gml_selector=None, change_set=None, network_data_set=None, *args, **kw_args):
        """ Initialises a new 'ChangeItem' instance.

        @param kind: Kind of change for the associated object. Values are: "add", "modify", "delete"
        @param sequence_number: Relative order of this ChangeItem in an ordered sequence of changes. 
        @param power_system_resource:
        @param location:
        @param organisation:
        @param status:
        @param asset:
        @param document:
        @param gml_observation:
        @param erp_person:
        @param gml_selector:
        @param change_set:
        @param network_data_set:
        """
        # Kind of change for the associated object. Values are: "add", "modify", "delete"
        self.kind = kind

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

        self._gml_selector = None
        self.gml_selector = gml_selector

        self._change_set = None
        self.change_set = change_set

        self._network_data_set = None
        self.network_data_set = network_data_set


        super(ChangeItem, self).__init__(*args, **kw_args)
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



class OrgPsrRole(Role):
    """ Roles played between Organisations and Power System Resources.
    """
    # <<< org_psr_role
    # @generated
    def __init__(self, power_system_resource=None, erp_organisation=None, *args, **kw_args):
        """ Initialises a new 'OrgPsrRole' instance.

        @param power_system_resource:
        @param erp_organisation:
        """

        self._power_system_resource = None
        self.power_system_resource = power_system_resource

        self._erp_organisation = None
        self.erp_organisation = erp_organisation


        super(OrgPsrRole, self).__init__(*args, **kw_args)
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



class OutageNotification(Document):
    """ A document containing information to be sent to customers notifying that an outage will take place. This is used to generate mailing lists for customers.
    """
    # <<< outage_notification
    # @generated
    def __init__(self, duration=0.0, reason='', expected_interruption_count=0, customer_datas=None, *args, **kw_args):
        """ Initialises a new 'OutageNotification' instance.

        @param duration: Likely duration of the interruption(s). 
        @param reason: Details of the outage 'reason'. 
        @param expected_interruption_count: Number of possible interruptions that the customer may expect for this event. 
        @param customer_datas:
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


        super(OutageNotification, self).__init__(*args, **kw_args)
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



class SwitchingSchedule(Document):
    """ Document describing a sequence of steps to perform an item of work, for example to isolate some plant with regard to safety, equipment ratings, and standards of customer service. Note 1: SwitchingSchedule is intended to describe the full operational details for switching for real time operation which includes other operations such as grounding, applying safety documents etc.  Note 2: The association to ErpPerson suits the UK practice of quoting specific names (e.g the crew foreman). The association to Crew is for US practice.
    """
    # <<< switching_schedule
    # @generated
    def __init__(self, reason='', interval=None, schedule_steps=None, crews=None, work_task=None, *args, **kw_args):
        """ Initialises a new 'SwitchingSchedule' instance.

        @param reason: Reason for switching. 
        @param interval: Interval between starting and completion of the switching.
        @param schedule_steps:
        @param crews: All Crews executing this SwitchingSchedule.
        @param work_task:
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


        super(SwitchingSchedule, self).__init__(*args, **kw_args)
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



class IncidentCode(IdentifiedObject):
    """ Classification of incident types. Multiple incident codes may apply to a given incident. The primary overall incident cause is recorded in 'IncidentRecord.category', and the main code in 'name'.
    """
    # <<< incident_code
    # @generated
    def __init__(self, sub_code='', incident_records=None, *args, **kw_args):
        """ Initialises a new 'IncidentCode' instance.

        @param sub_code: Additional level of classification detail (as extension to the main code found in 'name'). 
        @param incident_records:
        """
        # Additional level of classification detail (as extension to the main code found in 'name'). 
        self.sub_code = sub_code


        self._incident_records = []
        if incident_records is not None:
            self.incident_records = incident_records
        else:
            self.incident_records = []


        super(IncidentCode, self).__init__(*args, **kw_args)
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



class PlannedOutage(Document):
    """ Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.
    """
    # <<< planned_outage
    # @generated
    def __init__(self, kind='flexible', customer_datas=None, outage_schedules=None, *args, **kw_args):
        """ Initialises a new 'PlannedOutage' instance.

        @param kind: Kind of outage. Values are: "flexible", "fixed", "forced"
        @param customer_datas: All customers affected by this work. Derived from WorkOrder.connectedCustomers
        @param outage_schedules:
        """
        # Kind of outage. Values are: "flexible", "fixed", "forced"
        self.kind = kind


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


        super(PlannedOutage, self).__init__(*args, **kw_args)
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



class TroubleTicket(Document):
    """ A document used to report electrical trouble. The trouble may either be an outage or non-outage problem, such as power quality. It must always be associated with an Incident Record. Note that a separate Activity Record is created for each call associated with an instance of Trouble Ticket. The time of a call is stored in ActivityRecord.createdOn and comments are recorded in ActivityRecord.remarks.
    """
    # <<< trouble_ticket
    # @generated
    def __init__(self, reporting_kind='letter', advice='', call_back=False, priority='', inform_after_restored=False, estimated_restore_date_time='', inform_before_restored=False, hazard_code='', first_call_date_time='', customer_data=None, trouble_period=None, call_backs=None, incident_record=None, *args, **kw_args):
        """ Initialises a new 'TroubleTicket' instance.

        @param reporting_kind: Means the customer used to report trouble (default is 'call'). Values are: "letter", "other", "call", "email"
        @param advice: Advice already given to the customer at time when trouble was first reported. 
        @param call_back: True if requested to customer when someone is about to arrive at their premises. 
        @param priority: Priority of trouble call. 
        @param inform_after_restored: True if person reporting trouble requested a call back to confirm power has been restored. The person and their contact information is maintained in the assoicated Customer informaiton. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        @param estimated_restore_date_time: Estimated restoration date and time last provided to the customer. 
        @param inform_before_restored: True if person reporting trouble requested a call back when sigificant information became available about cause of the outage and the estimated restoration time. The person and their contact information are maintained in the assoicated Customer information. Call back results are recorded in assoicated 'ActivityRecord.Status.remarks'. 
        @param hazard_code: Code for a reported hazard condition. 
        @param first_call_date_time: Date and time trouble call first received. The date and time of subsequent calls by the same customer for the same trouble are recorded in associated Activity Records. 
        @param customer_data:
        @param trouble_period: Period between this source of trouble started and was resolved.
        @param call_backs:
        @param incident_record:
        """
        # Means the customer used to report trouble (default is 'call'). Values are: "letter", "other", "call", "email"
        self.reporting_kind = reporting_kind

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


        super(TroubleTicket, self).__init__(*args, **kw_args)
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



class IncidentRecord(Document):
    """ Document describing the incident reported in a TroubleTicket. If the incident has to do with an outage, this will be associated with an OutageRecord. Primary cause of the incident is captured in 'category'.
    """
    # <<< incident_record
    # @generated
    def __init__(self, incident_codes=None, period=None, trouble_tickets=None, *args, **kw_args):
        """ Initialises a new 'IncidentRecord' instance.

        @param incident_codes:
        @param period: Period between the first customer impacted by the incident and the incident resolution for all customers impacted.
        @param trouble_tickets:
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


        super(IncidentRecord, self).__init__(*args, **kw_args)
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



class ChangeSet(IdentifiedObject):
    """ The updates required in a transaction for an existing data set are grouped into a single ChangeSet. In data sets (e.g., NetworkDataSet), each major step in the ChangeSet is described through a separate ChangeItem associated with the data set. Within each data set, each inidividual object change is described with a seperate ChangeItem associated with the object.
    """
    # <<< change_set
    # @generated
    def __init__(self, land_bases=None, network_data_sets=None, change_items=None, status=None, documents=None, *args, **kw_args):
        """ Initialises a new 'ChangeSet' instance.

        @param land_bases:
        @param network_data_sets:
        @param change_items:
        @param status:
        @param documents:
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


        super(ChangeSet, self).__init__(*args, **kw_args)
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



class OutageReport(Document):
    """ Document with statistics of an outage.
    """
    # <<< outage_report
    # @generated
    def __init__(self, average_cml=0.0, outage_duration=0.0, customer_count=0, total_cml=0.0, outage_record=None, outage_history=None, *args, **kw_args):
        """ Initialises a new 'OutageReport' instance.

        @param average_cml: Average Customer Minutes Lost (CML) for this outage. 
        @param outage_duration: Total outage duration. 
        @param customer_count: Total number of outaged customers. 
        @param total_cml: Total Customer Minutes Lost (CML). 
        @param outage_record: reference to related document
        @param outage_history: OutageHistory of a customer, which may include this OutageReport.
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


        super(OutageReport, self).__init__(*args, **kw_args)
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



class LandBase(Document):
    """ Land base data.
    """
    pass
    # <<< land_base
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'LandBase' instance.

        """


        super(LandBase, self).__init__(*args, **kw_args)
    # >>> land_base



class Circuit(EquipmentContainer):
    """ EquipmentContainer that will typically include conductors, energy consumers, transformers and transformer windings, switches, shunt compensators, etc., likely at different voltages. Circuit extends from a substation to a set of open points (radial circuit), or to a second substation (looped circuit). It generally starts with a switching device, located in a substation. Membership in a Circuit is based on the nominal or design system configuration, but the electrical connectivity will change during switching operations.
    """
    pass
    # <<< circuit
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Circuit' instance.

        """


        super(Circuit, self).__init__(*args, **kw_args)
    # >>> circuit



# <<< inf_operations
# @generated
# >>> inf_operations
