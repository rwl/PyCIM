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

""" An extension to the Core and Wires packages that models information for protection equipment such as relays. These entities are used within training simulators and distribution network fault location applications.
"""

from cim.core import IdentifiedObject
from cim.core import Equipment

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimProtection"

ns_uri = "http://iec.ch/TC57/CIM-generic#Protection"

class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """
    # <<< reclose_sequence
    # @generated
    def __init__(self, reclose_step=0, reclose_delay=0.0, breaker=None, **kw_args):
        """ Initialises a new 'RecloseSequence' instance.
        """
        # Indicates the ordinal position of the reclose step relative to other steps in the sequence. 
        self.reclose_step = reclose_step

        # Indicates the time lapse before the reclose step will execute a reclose. 
        self.reclose_delay = reclose_delay


        self._breaker = None
        self.breaker = breaker


        super(RecloseSequence, self).__init__(**kw_args)
    # >>> reclose_sequence

    # <<< breaker
    # @generated
    def get_breaker(self):
        """ A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._breaker

    def set_breaker(self, value):
        if self._breaker is not None:
            filtered = [x for x in self.breaker.reclose_sequences if x != self]
            self._breaker._reclose_sequences = filtered

        self._breaker = value
        if self._breaker is not None:
            self._breaker._reclose_sequences.append(self)

    breaker = property(get_breaker, set_breaker)
    # >>> breaker


    def __str__(self):
        """ Returns a string representation of the RecloseSequence.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reclose_sequence.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RecloseSequence.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RecloseSequence", self.uri)
        if format:
            indent += ' ' * depth

        if self.breaker is not None:
            s += '%s<%s:RecloseSequence.breaker rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.breaker.uri)
        s += '%s<%s:RecloseSequence.reclose_step>%s</%s:RecloseSequence.reclose_step>' % \
            (indent, ns_prefix, self.reclose_step, ns_prefix)
        s += '%s<%s:RecloseSequence.reclose_delay>%s</%s:RecloseSequence.reclose_delay>' % \
            (indent, ns_prefix, self.reclose_delay, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RecloseSequence")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reclose_sequence.serialize


class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """
    # <<< protection_equipment
    # @generated
    def __init__(self, power_direction_flag=False, relay_delay_time=0.0, low_limit=0.0, high_limit=0.0, operates_breakers=None, conducting_equipments=None, unit=None, **kw_args):
        """ Initialises a new 'ProtectionEquipment' instance.
        """
        # Direction same as positive active power flow value. 
        self.power_direction_flag = power_direction_flag

        # The time delay from detection of abnormal conditions to relay operation. 
        self.relay_delay_time = relay_delay_time

        # The minimum allowable value. 
        self.low_limit = low_limit

        # The maximum allowable value. 
        self.high_limit = high_limit


        self._operates_breakers = []
        if operates_breakers is not None:
            self.operates_breakers = operates_breakers
        else:
            self.operates_breakers = []

        self._conducting_equipments = []
        if conducting_equipments is not None:
            self.conducting_equipments = conducting_equipments
        else:
            self.conducting_equipments = []

        self._unit = None
        self.unit = unit


        super(ProtectionEquipment, self).__init__(**kw_args)
    # >>> protection_equipment

    # <<< operates_breakers
    # @generated
    def get_operates_breakers(self):
        """ Protected switches operated by this ProtectionEquipment.
        """
        return self._operates_breakers

    def set_operates_breakers(self, value):
        for p in self._operates_breakers:
            filtered = [q for q in p.operated_by_protection_equipments if q != self]
            self._operates_breakers._operated_by_protection_equipments = filtered
        for r in value:
            if self not in r._operated_by_protection_equipments:
                r._operated_by_protection_equipments.append(self)
        self._operates_breakers = value

    operates_breakers = property(get_operates_breakers, set_operates_breakers)

    def add_operates_breakers(self, *operates_breakers):
        for obj in operates_breakers:
            if self not in obj._operated_by_protection_equipments:
                obj._operated_by_protection_equipments.append(self)
            self._operates_breakers.append(obj)

    def remove_operates_breakers(self, *operates_breakers):
        for obj in operates_breakers:
            if self in obj._operated_by_protection_equipments:
                obj._operated_by_protection_equipments.remove(self)
            self._operates_breakers.remove(obj)
    # >>> operates_breakers

    # <<< conducting_equipments
    # @generated
    def get_conducting_equipments(self):
        """ Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        return self._conducting_equipments

    def set_conducting_equipments(self, value):
        for p in self._conducting_equipments:
            filtered = [q for q in p.protection_equipments if q != self]
            self._conducting_equipments._protection_equipments = filtered
        for r in value:
            if self not in r._protection_equipments:
                r._protection_equipments.append(self)
        self._conducting_equipments = value

    conducting_equipments = property(get_conducting_equipments, set_conducting_equipments)

    def add_conducting_equipments(self, *conducting_equipments):
        for obj in conducting_equipments:
            if self not in obj._protection_equipments:
                obj._protection_equipments.append(self)
            self._conducting_equipments.append(obj)

    def remove_conducting_equipments(self, *conducting_equipments):
        for obj in conducting_equipments:
            if self in obj._protection_equipments:
                obj._protection_equipments.remove(self)
            self._conducting_equipments.remove(obj)
    # >>> conducting_equipments

    # <<< unit
    # @generated
    def get_unit(self):
        """ The Unit for the Protection Equipment.
        """
        return self._unit

    def set_unit(self, value):
        if self._unit is not None:
            filtered = [x for x in self.unit.protection_equipments if x != self]
            self._unit._protection_equipments = filtered

        self._unit = value
        if self._unit is not None:
            self._unit._protection_equipments.append(self)

    unit = property(get_unit, set_unit)
    # >>> unit


    def __str__(self):
        """ Returns a string representation of the ProtectionEquipment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< protection_equipment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ProtectionEquipment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ProtectionEquipment", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.operates_breakers:
            s += '%s<%s:ProtectionEquipment.operates_breakers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conducting_equipments:
            s += '%s<%s:ProtectionEquipment.conducting_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.unit is not None:
            s += '%s<%s:ProtectionEquipment.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:ProtectionEquipment.power_direction_flag>%s</%s:ProtectionEquipment.power_direction_flag>' % \
            (indent, ns_prefix, self.power_direction_flag, ns_prefix)
        s += '%s<%s:ProtectionEquipment.relay_delay_time>%s</%s:ProtectionEquipment.relay_delay_time>' % \
            (indent, ns_prefix, self.relay_delay_time, ns_prefix)
        s += '%s<%s:ProtectionEquipment.low_limit>%s</%s:ProtectionEquipment.low_limit>' % \
            (indent, ns_prefix, self.low_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.high_limit>%s</%s:ProtectionEquipment.high_limit>' % \
            (indent, ns_prefix, self.high_limit, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        s += '%s<%s:Equipment.normal_ily_in_service>%s</%s:Equipment.normal_ily_in_service>' % \
            (indent, ns_prefix, self.normal_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProtectionEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> protection_equipment.serialize


class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """
    # <<< current_relay
    # @generated
    def __init__(self, inverse_time_flag=False, time_delay2=0.0, current_limit1=0.0, current_limit3=0.0, current_limit2=0.0, time_delay1=0.0, time_delay3=0.0, **kw_args):
        """ Initialises a new 'CurrentRelay' instance.
        """
        # Set true if the current relay has inverse time characteristic. 
        self.inverse_time_flag = inverse_time_flag

        # Inverse time delay #2 for current limit #2 
        self.time_delay2 = time_delay2

        # Current limit #1 for inverse time pickup 
        self.current_limit1 = current_limit1

        # Current limit #3 for inverse time pickup 
        self.current_limit3 = current_limit3

        # Current limit #2 for inverse time pickup 
        self.current_limit2 = current_limit2

        # Inverse time delay #1 for current limit #1 
        self.time_delay1 = time_delay1

        # Inverse time delay #3 for current limit #3 
        self.time_delay3 = time_delay3



        super(CurrentRelay, self).__init__(**kw_args)
    # >>> current_relay


    def __str__(self):
        """ Returns a string representation of the CurrentRelay.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< current_relay.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CurrentRelay.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CurrentRelay", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:CurrentRelay.inverse_time_flag>%s</%s:CurrentRelay.inverse_time_flag>' % \
            (indent, ns_prefix, self.inverse_time_flag, ns_prefix)
        s += '%s<%s:CurrentRelay.time_delay2>%s</%s:CurrentRelay.time_delay2>' % \
            (indent, ns_prefix, self.time_delay2, ns_prefix)
        s += '%s<%s:CurrentRelay.current_limit1>%s</%s:CurrentRelay.current_limit1>' % \
            (indent, ns_prefix, self.current_limit1, ns_prefix)
        s += '%s<%s:CurrentRelay.current_limit3>%s</%s:CurrentRelay.current_limit3>' % \
            (indent, ns_prefix, self.current_limit3, ns_prefix)
        s += '%s<%s:CurrentRelay.current_limit2>%s</%s:CurrentRelay.current_limit2>' % \
            (indent, ns_prefix, self.current_limit2, ns_prefix)
        s += '%s<%s:CurrentRelay.time_delay1>%s</%s:CurrentRelay.time_delay1>' % \
            (indent, ns_prefix, self.time_delay1, ns_prefix)
        s += '%s<%s:CurrentRelay.time_delay3>%s</%s:CurrentRelay.time_delay3>' % \
            (indent, ns_prefix, self.time_delay3, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        s += '%s<%s:Equipment.normal_ily_in_service>%s</%s:Equipment.normal_ily_in_service>' % \
            (indent, ns_prefix, self.normal_ily_in_service, ns_prefix)
        for obj in self.operates_breakers:
            s += '%s<%s:ProtectionEquipment.operates_breakers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conducting_equipments:
            s += '%s<%s:ProtectionEquipment.conducting_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.unit is not None:
            s += '%s<%s:ProtectionEquipment.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:ProtectionEquipment.power_direction_flag>%s</%s:ProtectionEquipment.power_direction_flag>' % \
            (indent, ns_prefix, self.power_direction_flag, ns_prefix)
        s += '%s<%s:ProtectionEquipment.relay_delay_time>%s</%s:ProtectionEquipment.relay_delay_time>' % \
            (indent, ns_prefix, self.relay_delay_time, ns_prefix)
        s += '%s<%s:ProtectionEquipment.low_limit>%s</%s:ProtectionEquipment.low_limit>' % \
            (indent, ns_prefix, self.low_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.high_limit>%s</%s:ProtectionEquipment.high_limit>' % \
            (indent, ns_prefix, self.high_limit, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentRelay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_relay.serialize


class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """
    # <<< synchrocheck_relay
    # @generated
    def __init__(self, max_volt_diff=0.0, max_angle_diff=0.0, max_freq_diff=0.0, **kw_args):
        """ Initialises a new 'SynchrocheckRelay' instance.
        """
        # The maximum allowable difference voltage across the open device 
        self.max_volt_diff = max_volt_diff

        # The maximum allowable voltage vector phase angle difference across the open device 
        self.max_angle_diff = max_angle_diff

        # The maximum allowable frequency difference across the open device 
        self.max_freq_diff = max_freq_diff



        super(SynchrocheckRelay, self).__init__(**kw_args)
    # >>> synchrocheck_relay


    def __str__(self):
        """ Returns a string representation of the SynchrocheckRelay.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< synchrocheck_relay.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SynchrocheckRelay.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SynchrocheckRelay", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:SynchrocheckRelay.max_volt_diff>%s</%s:SynchrocheckRelay.max_volt_diff>' % \
            (indent, ns_prefix, self.max_volt_diff, ns_prefix)
        s += '%s<%s:SynchrocheckRelay.max_angle_diff>%s</%s:SynchrocheckRelay.max_angle_diff>' % \
            (indent, ns_prefix, self.max_angle_diff, ns_prefix)
        s += '%s<%s:SynchrocheckRelay.max_freq_diff>%s</%s:SynchrocheckRelay.max_freq_diff>' % \
            (indent, ns_prefix, self.max_freq_diff, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        s += '%s<%s:Equipment.normal_ily_in_service>%s</%s:Equipment.normal_ily_in_service>' % \
            (indent, ns_prefix, self.normal_ily_in_service, ns_prefix)
        for obj in self.operates_breakers:
            s += '%s<%s:ProtectionEquipment.operates_breakers rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.conducting_equipments:
            s += '%s<%s:ProtectionEquipment.conducting_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.unit is not None:
            s += '%s<%s:ProtectionEquipment.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        s += '%s<%s:ProtectionEquipment.power_direction_flag>%s</%s:ProtectionEquipment.power_direction_flag>' % \
            (indent, ns_prefix, self.power_direction_flag, ns_prefix)
        s += '%s<%s:ProtectionEquipment.relay_delay_time>%s</%s:ProtectionEquipment.relay_delay_time>' % \
            (indent, ns_prefix, self.relay_delay_time, ns_prefix)
        s += '%s<%s:ProtectionEquipment.low_limit>%s</%s:ProtectionEquipment.low_limit>' % \
            (indent, ns_prefix, self.low_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.high_limit>%s</%s:ProtectionEquipment.high_limit>' % \
            (indent, ns_prefix, self.high_limit, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SynchrocheckRelay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> synchrocheck_relay.serialize


# <<< protection
# @generated
# >>> protection
