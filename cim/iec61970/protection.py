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

from cim.iec61970.core import Equipment
from cim.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.protection"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Protection"

class FaultIndicator(Equipment):
    """ A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and Restoration) purposes, assisting with the dispatch of crews to 'most likely' part of the network (i.e. assists with determining circuit section where the fault most likely happened).
    """
    # <<< fault_indicator
    # @generated
    def __init__(self, fault_indicator_assets=None, fault_indicator_type_asset=None, **kw_args):
        """ Initialises a new 'FaultIndicator' instance.
        """

        self._fault_indicator_assets = []
        if fault_indicator_assets is not None:
            self.fault_indicator_assets = fault_indicator_assets
        else:
            self.fault_indicator_assets = []

        self._fault_indicator_type_asset = None
        self.fault_indicator_type_asset = fault_indicator_type_asset


        super(FaultIndicator, self).__init__(**kw_args)
    # >>> fault_indicator

    # <<< fault_indicator_assets
    # @generated
    def get_fault_indicator_assets(self):
        """ 
        """
        return self._fault_indicator_assets

    def set_fault_indicator_assets(self, value):
        for x in self._fault_indicator_assets:
            x._fault_indicator = None
        for y in value:
            y._fault_indicator = self
        self._fault_indicator_assets = value

    fault_indicator_assets = property(get_fault_indicator_assets, set_fault_indicator_assets)

    def add_fault_indicator_assets(self, *fault_indicator_assets):
        for obj in fault_indicator_assets:
            obj._fault_indicator = self
            self._fault_indicator_assets.append(obj)

    def remove_fault_indicator_assets(self, *fault_indicator_assets):
        for obj in fault_indicator_assets:
            obj._fault_indicator = None
            self._fault_indicator_assets.remove(obj)
    # >>> fault_indicator_assets

    # <<< fault_indicator_type_asset
    # @generated
    def get_fault_indicator_type_asset(self):
        """ 
        """
        return self._fault_indicator_type_asset

    def set_fault_indicator_type_asset(self, value):
        if self._fault_indicator_type_asset is not None:
            filtered = [x for x in self.fault_indicator_type_asset.fault_indicators if x != self]
            self._fault_indicator_type_asset._fault_indicators = filtered

        self._fault_indicator_type_asset = value
        if self._fault_indicator_type_asset is not None:
            self._fault_indicator_type_asset._fault_indicators.append(self)

    fault_indicator_type_asset = property(get_fault_indicator_type_asset, set_fault_indicator_type_asset)
    # >>> fault_indicator_type_asset


    def __str__(self):
        """ Returns a string representation of the FaultIndicator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< fault_indicator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FaultIndicator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FaultIndicator", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.fault_indicator_assets:
            s += '%s<%s:FaultIndicator.fault_indicator_assets rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.fault_indicator_type_asset is not None:
            s += '%s<%s:FaultIndicator.fault_indicator_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.fault_indicator_type_asset.uri)
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
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FaultIndicator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> fault_indicator.serialize


class SurgeProtector(Equipment):
    """ Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.
    """
    # <<< surge_protector
    # @generated
    def __init__(self, surge_protector_type_asset=None, surge_protector_asset=None, **kw_args):
        """ Initialises a new 'SurgeProtector' instance.
        """

        self._surge_protector_type_asset = None
        self.surge_protector_type_asset = surge_protector_type_asset

        self._surge_protector_asset = None
        self.surge_protector_asset = surge_protector_asset


        super(SurgeProtector, self).__init__(**kw_args)
    # >>> surge_protector

    # <<< surge_protector_type_asset
    # @generated
    def get_surge_protector_type_asset(self):
        """ 
        """
        return self._surge_protector_type_asset

    def set_surge_protector_type_asset(self, value):
        if self._surge_protector_type_asset is not None:
            filtered = [x for x in self.surge_protector_type_asset.surge_protectors if x != self]
            self._surge_protector_type_asset._surge_protectors = filtered

        self._surge_protector_type_asset = value
        if self._surge_protector_type_asset is not None:
            self._surge_protector_type_asset._surge_protectors.append(self)

    surge_protector_type_asset = property(get_surge_protector_type_asset, set_surge_protector_type_asset)
    # >>> surge_protector_type_asset

    # <<< surge_protector_asset
    # @generated
    def get_surge_protector_asset(self):
        """ 
        """
        return self._surge_protector_asset

    def set_surge_protector_asset(self, value):
        if self._surge_protector_asset is not None:
            self._surge_protector_asset._surge_protector = None

        self._surge_protector_asset = value
        if self._surge_protector_asset is not None:
            self._surge_protector_asset._surge_protector = self

    surge_protector_asset = property(get_surge_protector_asset, set_surge_protector_asset)
    # >>> surge_protector_asset


    def __str__(self):
        """ Returns a string representation of the SurgeProtector.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< surge_protector.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SurgeProtector.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SurgeProtector", self.uri)
        if format:
            indent += ' ' * depth

        if self.surge_protector_type_asset is not None:
            s += '%s<%s:SurgeProtector.surge_protector_type_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.surge_protector_type_asset.uri)
        if self.surge_protector_asset is not None:
            s += '%s<%s:SurgeProtector.surge_protector_asset rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.surge_protector_asset.uri)
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
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SurgeProtector")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> surge_protector.serialize


class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """
    # <<< reclose_sequence
    # @generated
    def __init__(self, reclose_step=0, reclose_delay=0.0, protected_switch=None, **kw_args):
        """ Initialises a new 'RecloseSequence' instance.
        """
        # Indicates the ordinal position of the reclose step relative to other steps in the sequence. 
        self.reclose_step = reclose_step

        # Indicates the time lapse before the reclose step will execute a reclose. 
        self.reclose_delay = reclose_delay


        self._protected_switch = None
        self.protected_switch = protected_switch


        super(RecloseSequence, self).__init__(**kw_args)
    # >>> reclose_sequence

    # <<< protected_switch
    # @generated
    def get_protected_switch(self):
        """ A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._protected_switch

    def set_protected_switch(self, value):
        if self._protected_switch is not None:
            filtered = [x for x in self.protected_switch.reclose_sequences if x != self]
            self._protected_switch._reclose_sequences = filtered

        self._protected_switch = value
        if self._protected_switch is not None:
            self._protected_switch._reclose_sequences.append(self)

    protected_switch = property(get_protected_switch, set_protected_switch)
    # >>> protected_switch


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

        if self.protected_switch is not None:
            s += '%s<%s:RecloseSequence.protected_switch rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.protected_switch.uri)
        s += '%s<%s:RecloseSequence.reclose_step>%s</%s:RecloseSequence.reclose_step>' % \
            (indent, ns_prefix, self.reclose_step, ns_prefix)
        s += '%s<%s:RecloseSequence.reclose_delay>%s</%s:RecloseSequence.reclose_delay>' % \
            (indent, ns_prefix, self.reclose_delay, ns_prefix)
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
    def __init__(self, high_limit=0.0, power_direction_flag=False, low_limit=0.0, relay_delay_time=0.0, protected_switches=None, unit=None, conducting_equipments=None, **kw_args):
        """ Initialises a new 'ProtectionEquipment' instance.
        """
        # The maximum allowable value. 
        self.high_limit = high_limit

        # Direction same as positive active power flow value. 
        self.power_direction_flag = power_direction_flag

        # The minimum allowable value. 
        self.low_limit = low_limit

        # The time delay from detection of abnormal conditions to relay operation. 
        self.relay_delay_time = relay_delay_time


        if protected_switches is not None:
            self.protected_switches = protected_switches
        else:
            self.protected_switches = []

        self._unit = None
        self.unit = unit

        self._conducting_equipments = []
        if conducting_equipments is not None:
            self.conducting_equipments = conducting_equipments
        else:
            self.conducting_equipments = []


        super(ProtectionEquipment, self).__init__(**kw_args)
    # >>> protection_equipment

    # <<< protected_switches
    # @generated
    def add_protected_switches(self, *protected_switches):
        for obj in protected_switches:
            self.protected_switches.append(obj)

    def remove_protected_switches(self, *protected_switches):
        for obj in protected_switches:
            self.protected_switches.remove(obj)
    # >>> protected_switches

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

        for obj in self.protected_switches:
            s += '%s<%s:ProtectionEquipment.protected_switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.unit is not None:
            s += '%s<%s:ProtectionEquipment.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        for obj in self.conducting_equipments:
            s += '%s<%s:ProtectionEquipment.conducting_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProtectionEquipment.high_limit>%s</%s:ProtectionEquipment.high_limit>' % \
            (indent, ns_prefix, self.high_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.power_direction_flag>%s</%s:ProtectionEquipment.power_direction_flag>' % \
            (indent, ns_prefix, self.power_direction_flag, ns_prefix)
        s += '%s<%s:ProtectionEquipment.low_limit>%s</%s:ProtectionEquipment.low_limit>' % \
            (indent, ns_prefix, self.low_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.relay_delay_time>%s</%s:ProtectionEquipment.relay_delay_time>' % \
            (indent, ns_prefix, self.relay_delay_time, ns_prefix)
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
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ProtectionEquipment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> protection_equipment.serialize


class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """
    # <<< synchrocheck_relay
    # @generated
    def __init__(self, max_freq_diff=0.0, max_volt_diff=0.0, max_angle_diff=0.0, **kw_args):
        """ Initialises a new 'SynchrocheckRelay' instance.
        """
        # The maximum allowable frequency difference across the open device 
        self.max_freq_diff = max_freq_diff

        # The maximum allowable difference voltage across the open device 
        self.max_volt_diff = max_volt_diff

        # The maximum allowable voltage vector phase angle difference across the open device 
        self.max_angle_diff = max_angle_diff



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

        s += '%s<%s:SynchrocheckRelay.max_freq_diff>%s</%s:SynchrocheckRelay.max_freq_diff>' % \
            (indent, ns_prefix, self.max_freq_diff, ns_prefix)
        s += '%s<%s:SynchrocheckRelay.max_volt_diff>%s</%s:SynchrocheckRelay.max_volt_diff>' % \
            (indent, ns_prefix, self.max_volt_diff, ns_prefix)
        s += '%s<%s:SynchrocheckRelay.max_angle_diff>%s</%s:SynchrocheckRelay.max_angle_diff>' % \
            (indent, ns_prefix, self.max_angle_diff, ns_prefix)
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
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.protected_switches:
            s += '%s<%s:ProtectionEquipment.protected_switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.unit is not None:
            s += '%s<%s:ProtectionEquipment.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        for obj in self.conducting_equipments:
            s += '%s<%s:ProtectionEquipment.conducting_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProtectionEquipment.high_limit>%s</%s:ProtectionEquipment.high_limit>' % \
            (indent, ns_prefix, self.high_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.power_direction_flag>%s</%s:ProtectionEquipment.power_direction_flag>' % \
            (indent, ns_prefix, self.power_direction_flag, ns_prefix)
        s += '%s<%s:ProtectionEquipment.low_limit>%s</%s:ProtectionEquipment.low_limit>' % \
            (indent, ns_prefix, self.low_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.relay_delay_time>%s</%s:ProtectionEquipment.relay_delay_time>' % \
            (indent, ns_prefix, self.relay_delay_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SynchrocheckRelay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> synchrocheck_relay.serialize


class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """
    # <<< current_relay
    # @generated
    def __init__(self, time_delay2=0.0, current_limit2=0.0, current_limit3=0.0, inverse_time_flag=False, time_delay3=0.0, current_limit1=0.0, time_delay1=0.0, **kw_args):
        """ Initialises a new 'CurrentRelay' instance.
        """
        # Inverse time delay #2 for current limit #2 
        self.time_delay2 = time_delay2

        # Current limit #2 for inverse time pickup 
        self.current_limit2 = current_limit2

        # Current limit #3 for inverse time pickup 
        self.current_limit3 = current_limit3

        # Set true if the current relay has inverse time characteristic. 
        self.inverse_time_flag = inverse_time_flag

        # Inverse time delay #3 for current limit #3 
        self.time_delay3 = time_delay3

        # Current limit #1 for inverse time pickup 
        self.current_limit1 = current_limit1

        # Inverse time delay #1 for current limit #1 
        self.time_delay1 = time_delay1



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

        s += '%s<%s:CurrentRelay.time_delay2>%s</%s:CurrentRelay.time_delay2>' % \
            (indent, ns_prefix, self.time_delay2, ns_prefix)
        s += '%s<%s:CurrentRelay.current_limit2>%s</%s:CurrentRelay.current_limit2>' % \
            (indent, ns_prefix, self.current_limit2, ns_prefix)
        s += '%s<%s:CurrentRelay.current_limit3>%s</%s:CurrentRelay.current_limit3>' % \
            (indent, ns_prefix, self.current_limit3, ns_prefix)
        s += '%s<%s:CurrentRelay.inverse_time_flag>%s</%s:CurrentRelay.inverse_time_flag>' % \
            (indent, ns_prefix, self.inverse_time_flag, ns_prefix)
        s += '%s<%s:CurrentRelay.time_delay3>%s</%s:CurrentRelay.time_delay3>' % \
            (indent, ns_prefix, self.time_delay3, ns_prefix)
        s += '%s<%s:CurrentRelay.current_limit1>%s</%s:CurrentRelay.current_limit1>' % \
            (indent, ns_prefix, self.current_limit1, ns_prefix)
        s += '%s<%s:CurrentRelay.time_delay1>%s</%s:CurrentRelay.time_delay1>' % \
            (indent, ns_prefix, self.time_delay1, ns_prefix)
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
        for obj in self.contingency_equipment:
            s += '%s<%s:Equipment.contingency_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.customer_agreements:
            s += '%s<%s:Equipment.customer_agreements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.protected_switches:
            s += '%s<%s:ProtectionEquipment.protected_switches rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.unit is not None:
            s += '%s<%s:ProtectionEquipment.unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.unit.uri)
        for obj in self.conducting_equipments:
            s += '%s<%s:ProtectionEquipment.conducting_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:ProtectionEquipment.high_limit>%s</%s:ProtectionEquipment.high_limit>' % \
            (indent, ns_prefix, self.high_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.power_direction_flag>%s</%s:ProtectionEquipment.power_direction_flag>' % \
            (indent, ns_prefix, self.power_direction_flag, ns_prefix)
        s += '%s<%s:ProtectionEquipment.low_limit>%s</%s:ProtectionEquipment.low_limit>' % \
            (indent, ns_prefix, self.low_limit, ns_prefix)
        s += '%s<%s:ProtectionEquipment.relay_delay_time>%s</%s:ProtectionEquipment.relay_delay_time>' % \
            (indent, ns_prefix, self.relay_delay_time, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CurrentRelay")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> current_relay.serialize


# <<< protection
# @generated
# >>> protection
