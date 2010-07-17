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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

from cdpsm.iec61970.core import ConductingEquipment
from cdpsm.iec61970.core import PowerSystemResource
from cdpsm.iec61970.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Wires"

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """
    pass
    # <<< busbar_section
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'BusbarSection' instance.
        """


        super(BusbarSection, self).__init__(**kw_args)
    # >>> busbar_section


    def __str__(self):
        """ Returns a string representation of the BusbarSection.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< busbar_section.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusbarSection.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusbarSection", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusbarSection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> busbar_section.serialize


class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """
    # <<< tap_changer
    # @generated
    def __init__(self, step_voltage_increment=0.0, subsequent_delay=0.0, neutral_step=0, normal_step=0, ltc_flag=False, neutral_u=0.0, low_step=0, initial_delay=0.0, regulation_status=False, high_step=0, sv_tap_step=None, **kw_args):
        """ Initialises a new 'TapChanger' instance.
        """
        # Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        self.step_voltage_increment = step_voltage_increment

        # For an LTC, the delay for subsequent tap changer operation (second and later step changes)For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        self.subsequent_delay = subsequent_delay

        # The neutral tap step position for this winding.The neutral tap step position for this winding. 
        self.neutral_step = neutral_step

        # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        self.normal_step = normal_step

        # Specifies whether or not a TapChanger has load tap changing capabilities.Specifies whether or not a TapChanger has load tap changing capabilities. 
        self.ltc_flag = ltc_flag

        # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting. 
        self.neutral_u = neutral_u

        # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral 
        self.low_step = low_step

        # For an LTC, the delay for initial tap changer operation (first step change)For an LTC, the delay for initial tap changer operation (first step change) 
        self.initial_delay = initial_delay

        # Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        self.regulation_status = regulation_status

        # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral 
        self.high_step = high_step


        self._sv_tap_step = None
        self.sv_tap_step = sv_tap_step


        super(TapChanger, self).__init__(**kw_args)
    # >>> tap_changer

    # <<< sv_tap_step
    # @generated
    def get_sv_tap_step(self):
        """ The tap step state associated with the tap changer.The tap step state associated with the tap changer.
        """
        return self._sv_tap_step

    def set_sv_tap_step(self, value):
        if self._sv_tap_step is not None:
            self._sv_tap_step._tap_changer = None

        self._sv_tap_step = value
        if self._sv_tap_step is not None:
            self._sv_tap_step._tap_changer = self

    sv_tap_step = property(get_sv_tap_step, set_sv_tap_step)
    # >>> sv_tap_step


    def __str__(self):
        """ Returns a string representation of the TapChanger.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< tap_changer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TapChanger.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TapChanger", self.uri)
        if format:
            indent += ' ' * depth

        if self.sv_tap_step is not None:
            s += '%s<%s:TapChanger.sv_tap_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_tap_step.uri)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.subsequent_delay>%s</%s:TapChanger.subsequent_delay>' % \
            (indent, ns_prefix, self.subsequent_delay, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.normal_step>%s</%s:TapChanger.normal_step>' % \
            (indent, ns_prefix, self.normal_step, ns_prefix)
        s += '%s<%s:TapChanger.ltc_flag>%s</%s:TapChanger.ltc_flag>' % \
            (indent, ns_prefix, self.ltc_flag, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.initial_delay>%s</%s:TapChanger.initial_delay>' % \
            (indent, ns_prefix, self.initial_delay, ns_prefix)
        s += '%s<%s:TapChanger.regulation_status>%s</%s:TapChanger.regulation_status>' % \
            (indent, ns_prefix, self.regulation_status, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tap_changer.serialize


class Junction(ConductingEquipment):
    """ A point where one or more conducting equipments are connected with zero resistance.A point where one or more conducting equipments are connected with zero resistance.
    """
    pass
    # <<< junction
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Junction' instance.
        """


        super(Junction, self).__init__(**kw_args)
    # >>> junction


    def __str__(self):
        """ Returns a string representation of the Junction.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< junction.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Junction.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Junction", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Junction")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> junction.serialize


class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """
    # <<< energy_source
    # @generated
    def __init__(self, x=0.0, voltage_magnitude=0.0, voltage_angle=0.0, nominal_voltage=0.0, **kw_args):
        """ Initialises a new 'EnergySource' instance.
        """
        # Positive sequence Thevenin reactance.Positive sequence Thevenin reactance. 
        self.x = x

        # Phase-to-phase open circuit voltage magnitude.Phase-to-phase open circuit voltage magnitude. 
        self.voltage_magnitude = voltage_magnitude

        # Phase angle of a-phase open circuit.Phase angle of a-phase open circuit. 
        self.voltage_angle = voltage_angle

        # Phase-to-phase nominal voltage.Phase-to-phase nominal voltage. 
        self.nominal_voltage = nominal_voltage



        super(EnergySource, self).__init__(**kw_args)
    # >>> energy_source


    def __str__(self):
        """ Returns a string representation of the EnergySource.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_source.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergySource.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergySource", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:EnergySource.x>%s</%s:EnergySource.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:EnergySource.voltage_magnitude>%s</%s:EnergySource.voltage_magnitude>' % \
            (indent, ns_prefix, self.voltage_magnitude, ns_prefix)
        s += '%s<%s:EnergySource.voltage_angle>%s</%s:EnergySource.voltage_angle>' % \
            (indent, ns_prefix, self.voltage_angle, ns_prefix)
        s += '%s<%s:EnergySource.nominal_voltage>%s</%s:EnergySource.nominal_voltage>' % \
            (indent, ns_prefix, self.nominal_voltage, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergySource")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_source.serialize


class SynchronousMachine(ConductingEquipment):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """
    # <<< synchronous_machine
    # @generated
    def __init__(self, base_q=0.0, operating_mode='condenser', type='condenser', max_q=0.0, min_q=0.0, generating_unit=None, **kw_args):
        """ Initialises a new 'SynchronousMachine' instance.
        """
        # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        self.base_q = base_q

        # Current mode of operation.Current mode of operation. Values are: "condenser", "generator"
        self.operating_mode = 'condenser'

        # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = 'condenser'

        # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        self.max_q = max_q

        # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit. 
        self.min_q = min_q


        self._generating_unit = None
        self.generating_unit = generating_unit


        super(SynchronousMachine, self).__init__(**kw_args)
    # >>> synchronous_machine

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.synchronous_machines if x != self]
            self._generating_unit._synchronous_machines = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._synchronous_machines.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit


    def __str__(self):
        """ Returns a string representation of the SynchronousMachine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< synchronous_machine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SynchronousMachine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SynchronousMachine", self.uri)
        if format:
            indent += ' ' * depth

        if self.generating_unit is not None:
            s += '%s<%s:SynchronousMachine.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generating_unit.uri)
        s += '%s<%s:SynchronousMachine.base_q>%s</%s:SynchronousMachine.base_q>' % \
            (indent, ns_prefix, self.base_q, ns_prefix)
        s += '%s<%s:SynchronousMachine.operating_mode>%s</%s:SynchronousMachine.operating_mode>' % \
            (indent, ns_prefix, self.operating_mode, ns_prefix)
        s += '%s<%s:SynchronousMachine.type>%s</%s:SynchronousMachine.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:SynchronousMachine.max_q>%s</%s:SynchronousMachine.max_q>' % \
            (indent, ns_prefix, self.max_q, ns_prefix)
        s += '%s<%s:SynchronousMachine.min_q>%s</%s:SynchronousMachine.min_q>' % \
            (indent, ns_prefix, self.min_q, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SynchronousMachine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> synchronous_machine.serialize


class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """
    # <<< energy_consumer
    # @generated
    def __init__(self, pfixed=0.0, pfixed_pct=0.0, qfixed_pct=0.0, qfixed=0.0, customer_count=0, load_response=None, **kw_args):
        """ Initialises a new 'EnergyConsumer' instance.
        """
        # Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity. 
        self.pfixed = pfixed

        # Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power 
        self.pfixed_pct = pfixed_pct

        # Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power. 
        self.qfixed_pct = qfixed_pct

        # Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity. 
        self.qfixed = qfixed

        # Number of individual customers represented by this DemandNumber of individual customers represented by this Demand 
        self.customer_count = customer_count


        self._load_response = None
        self.load_response = load_response


        super(EnergyConsumer, self).__init__(**kw_args)
    # >>> energy_consumer

    # <<< load_response
    # @generated
    def get_load_response(self):
        """ The load response characteristic of this load.The load response characteristic of this load.
        """
        return self._load_response

    def set_load_response(self, value):
        if self._load_response is not None:
            filtered = [x for x in self.load_response.energy_consumer if x != self]
            self._load_response._energy_consumer = filtered

        self._load_response = value
        if self._load_response is not None:
            self._load_response._energy_consumer.append(self)

    load_response = property(get_load_response, set_load_response)
    # >>> load_response


    def __str__(self):
        """ Returns a string representation of the EnergyConsumer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< energy_consumer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the EnergyConsumer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "EnergyConsumer", self.uri)
        if format:
            indent += ' ' * depth

        if self.load_response is not None:
            s += '%s<%s:EnergyConsumer.load_response rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.load_response.uri)
        s += '%s<%s:EnergyConsumer.pfixed>%s</%s:EnergyConsumer.pfixed>' % \
            (indent, ns_prefix, self.pfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.pfixed_pct>%s</%s:EnergyConsumer.pfixed_pct>' % \
            (indent, ns_prefix, self.pfixed_pct, ns_prefix)
        s += '%s<%s:EnergyConsumer.qfixed_pct>%s</%s:EnergyConsumer.qfixed_pct>' % \
            (indent, ns_prefix, self.qfixed_pct, ns_prefix)
        s += '%s<%s:EnergyConsumer.qfixed>%s</%s:EnergyConsumer.qfixed>' % \
            (indent, ns_prefix, self.qfixed, ns_prefix)
        s += '%s<%s:EnergyConsumer.customer_count>%s</%s:EnergyConsumer.customer_count>' % \
            (indent, ns_prefix, self.customer_count, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "EnergyConsumer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> energy_consumer.serialize


class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.
    """
    # <<< switch
    # @generated
    def __init__(self, normal_open=False, **kw_args):
        """ Initialises a new 'Switch' instance.
        """
        # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        self.normal_open = normal_open



        super(Switch, self).__init__(**kw_args)
    # >>> switch


    def __str__(self):
        """ Returns a string representation of the Switch.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< switch.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Switch.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Switch", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Switch")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switch.serialize


class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """
    # <<< line
    # @generated
    def __init__(self, region=None, **kw_args):
        """ Initialises a new 'Line' instance.
        """

        self._region = None
        self.region = region


        super(Line, self).__init__(**kw_args)
    # >>> line

    # <<< region
    # @generated
    def get_region(self):
        """ A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.lines if x != self]
            self._region._lines = filtered

        self._region = value
        if self._region is not None:
            self._region._lines.append(self)

    region = property(get_region, set_region)
    # >>> region


    def __str__(self):
        """ Returns a string representation of the Line.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< line.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Line.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Line", self.uri)
        if format:
            indent += ' ' * depth

        if self.region is not None:
            s += '%s<%s:Line.region rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.region.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.connectivity_nodes:
            s += '%s<%s:ConnectivityNodeContainer.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.equipments:
            s += '%s<%s:EquipmentContainer.equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Line")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> line.serialize


class ShuntCompensator(ConductingEquipment):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """
    # <<< shunt_compensator
    # @generated
    def __init__(self, nom_q=0.0, nom_u=0.0, normal_sections=0, maximum_sections=0, reactive_per_section=0.0, **kw_args):
        """ Initialises a new 'ShuntCompensator' instance.
        """
        # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive. 
        self.nom_q = nom_q

        # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        self.nom_u = nom_u

        # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        self.normal_sections = normal_sections

        # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in. 
        self.maximum_sections = maximum_sections

        # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        self.reactive_per_section = reactive_per_section



        super(ShuntCompensator, self).__init__(**kw_args)
    # >>> shunt_compensator


    def __str__(self):
        """ Returns a string representation of the ShuntCompensator.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< shunt_compensator.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ShuntCompensator.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ShuntCompensator", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ShuntCompensator.nom_q>%s</%s:ShuntCompensator.nom_q>' % \
            (indent, ns_prefix, self.nom_q, ns_prefix)
        s += '%s<%s:ShuntCompensator.nom_u>%s</%s:ShuntCompensator.nom_u>' % \
            (indent, ns_prefix, self.nom_u, ns_prefix)
        s += '%s<%s:ShuntCompensator.normal_sections>%s</%s:ShuntCompensator.normal_sections>' % \
            (indent, ns_prefix, self.normal_sections, ns_prefix)
        s += '%s<%s:ShuntCompensator.maximum_sections>%s</%s:ShuntCompensator.maximum_sections>' % \
            (indent, ns_prefix, self.maximum_sections, ns_prefix)
        s += '%s<%s:ShuntCompensator.reactive_per_section>%s</%s:ShuntCompensator.reactive_per_section>' % \
            (indent, ns_prefix, self.reactive_per_section, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShuntCompensator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> shunt_compensator.serialize


class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """
    # <<< conductor
    # @generated
    def __init__(self, length=0.0, **kw_args):
        """ Initialises a new 'Conductor' instance.
        """
        # Segment length for calculating line section capabilitiesSegment length for calculating line section capabilities 
        self.length = length



        super(Conductor, self).__init__(**kw_args)
    # >>> conductor


    def __str__(self):
        """ Returns a string representation of the Conductor.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< conductor.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Conductor.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Conductor", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Conductor.length>%s</%s:Conductor.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Conductor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conductor.serialize


class LoadBreakSwitch(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """
    # <<< load_break_switch
    # @generated
    def __init__(self, rated_current=0.0, **kw_args):
        """ Initialises a new 'LoadBreakSwitch' instance.
        """
        # Current carrying capacity of a wire or cable under stated thermal conditions.Current carrying capacity of a wire or cable under stated thermal conditions. 
        self.rated_current = rated_current



        super(LoadBreakSwitch, self).__init__(**kw_args)
    # >>> load_break_switch


    def __str__(self):
        """ Returns a string representation of the LoadBreakSwitch.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< load_break_switch.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the LoadBreakSwitch.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "LoadBreakSwitch", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:LoadBreakSwitch.rated_current>%s</%s:LoadBreakSwitch.rated_current>' % \
            (indent, ns_prefix, self.rated_current, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "LoadBreakSwitch")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> load_break_switch.serialize


class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """
    # <<< fuse
    # @generated
    def __init__(self, rating_current=0.0, **kw_args):
        """ Initialises a new 'Fuse' instance.
        """
        # Fault interrupting current rating.Fault interrupting current rating. 
        self.rating_current = rating_current



        super(Fuse, self).__init__(**kw_args)
    # >>> fuse


    def __str__(self):
        """ Returns a string representation of the Fuse.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< fuse.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Fuse.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Fuse", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Fuse.rating_current>%s</%s:Fuse.rating_current>' % \
            (indent, ns_prefix, self.rating_current, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Fuse")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> fuse.serialize


class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.
    """
    # <<< acline_segment
    # @generated
    def __init__(self, r=0.0, x0=0.0, bch=0.0, x=0.0, b0ch=0.0, r0=0.0, **kw_args):
        """ Initialises a new 'ACLineSegment' instance.
        """
        # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section. 
        self.r = r

        # Zero sequence series reactance of the entire line section.Zero sequence series reactance of the entire line section. 
        self.x0 = x0

        # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        self.bch = bch

        # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section. 
        self.x = x

        # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.b0ch = b0ch

        # Zero sequence series resistance of the entire line section.Zero sequence series resistance of the entire line section. 
        self.r0 = r0



        super(ACLineSegment, self).__init__(**kw_args)
    # >>> acline_segment


    def __str__(self):
        """ Returns a string representation of the ACLineSegment.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< acline_segment.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ACLineSegment.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ACLineSegment", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:ACLineSegment.r>%s</%s:ACLineSegment.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:ACLineSegment.x0>%s</%s:ACLineSegment.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:ACLineSegment.bch>%s</%s:ACLineSegment.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)
        s += '%s<%s:ACLineSegment.x>%s</%s:ACLineSegment.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:ACLineSegment.b0ch>%s</%s:ACLineSegment.b0ch>' % \
            (indent, ns_prefix, self.b0ch, ns_prefix)
        s += '%s<%s:ACLineSegment.r0>%s</%s:ACLineSegment.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Conductor.length>%s</%s:Conductor.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ACLineSegment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> acline_segment.serialize


class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """
    pass
    # <<< disconnector
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Disconnector' instance.
        """


        super(Disconnector, self).__init__(**kw_args)
    # >>> disconnector


    def __str__(self):
        """ Returns a string representation of the Disconnector.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< disconnector.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Disconnector.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Disconnector", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Disconnector")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> disconnector.serialize


class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """
    # <<< ratio_tap_changer
    # @generated
    def __init__(self, tcul_control_mode='reactive', winding=None, **kw_args):
        """ Initialises a new 'RatioTapChanger' instance.
        """
        # Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        self.tcul_control_mode = 'reactive'


        self._winding = None
        self.winding = winding


        super(RatioTapChanger, self).__init__(**kw_args)
    # >>> ratio_tap_changer

    # <<< winding
    # @generated
    def get_winding(self):
        """ Winding to which this ratio tap changer belongs.Winding to which this ratio tap changer belongs.
        """
        return self._winding

    def set_winding(self, value):
        if self._winding is not None:
            self._winding._ratio_tap_changer = None

        self._winding = value
        if self._winding is not None:
            self._winding._ratio_tap_changer = self

    winding = property(get_winding, set_winding)
    # >>> winding


    def __str__(self):
        """ Returns a string representation of the RatioTapChanger.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< ratio_tap_changer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RatioTapChanger.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RatioTapChanger", self.uri)
        if format:
            indent += ' ' * depth

        if self.winding is not None:
            s += '%s<%s:RatioTapChanger.winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.winding.uri)
        s += '%s<%s:RatioTapChanger.tcul_control_mode>%s</%s:RatioTapChanger.tcul_control_mode>' % \
            (indent, ns_prefix, self.tcul_control_mode, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.sv_tap_step is not None:
            s += '%s<%s:TapChanger.sv_tap_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_tap_step.uri)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.subsequent_delay>%s</%s:TapChanger.subsequent_delay>' % \
            (indent, ns_prefix, self.subsequent_delay, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.normal_step>%s</%s:TapChanger.normal_step>' % \
            (indent, ns_prefix, self.normal_step, ns_prefix)
        s += '%s<%s:TapChanger.ltc_flag>%s</%s:TapChanger.ltc_flag>' % \
            (indent, ns_prefix, self.ltc_flag, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.initial_delay>%s</%s:TapChanger.initial_delay>' % \
            (indent, ns_prefix, self.initial_delay, ns_prefix)
        s += '%s<%s:TapChanger.regulation_status>%s</%s:TapChanger.regulation_status>' % \
            (indent, ns_prefix, self.regulation_status, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RatioTapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ratio_tap_changer.serialize


class Breaker(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """
    # <<< breaker
    # @generated
    def __init__(self, rated_current=0.0, **kw_args):
        """ Initialises a new 'Breaker' instance.
        """
        # Fault interrupting current rating.Fault interrupting current rating. 
        self.rated_current = rated_current



        super(Breaker, self).__init__(**kw_args)
    # >>> breaker


    def __str__(self):
        """ Returns a string representation of the Breaker.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< breaker.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Breaker.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Breaker", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Breaker.rated_current>%s</%s:Breaker.rated_current>' % \
            (indent, ns_prefix, self.rated_current, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        s += '%s<%s:ConductingEquipment.phases>%s</%s:ConductingEquipment.phases>' % \
            (indent, ns_prefix, self.phases, ns_prefix)
        s += '%s<%s:Switch.normal_open>%s</%s:Switch.normal_open>' % \
            (indent, ns_prefix, self.normal_open, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Breaker")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> breaker.serialize


# <<< wires
# @generated
# >>> wires
