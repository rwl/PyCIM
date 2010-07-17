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

from ucte.core import ConductingEquipment
from ucte.core import IdentifiedObject
from ucte.core import Curve
from ucte.core import Equipment
from ucte.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Wires"

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.
    """
    # <<< busbar_section
    # @generated
    def __init__(self, voltage_control_zone=None, **kw_args):
        """ Initialises a new 'BusbarSection' instance.
        """

        self._voltage_control_zone = None
        self.voltage_control_zone = voltage_control_zone


        super(BusbarSection, self).__init__(**kw_args)
    # >>> busbar_section

    # <<< voltage_control_zone
    # @generated
    def get_voltage_control_zone(self):
        """ A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.
        """
        return self._voltage_control_zone

    def set_voltage_control_zone(self, value):
        if self._voltage_control_zone is not None:
            self._voltage_control_zone._busbar_section = None

        self._voltage_control_zone = value
        if self._voltage_control_zone is not None:
            self._voltage_control_zone._busbar_section = self

    voltage_control_zone = property(get_voltage_control_zone, set_voltage_control_zone)
    # >>> voltage_control_zone


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

        if self.voltage_control_zone is not None:
            s += '%s<%s:BusbarSection.voltage_control_zone rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.voltage_control_zone.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusbarSection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> busbar_section.serialize


class TapChanger(IdentifiedObject):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """
    # <<< tap_changer
    # @generated
    def __init__(self, step_voltage_increment=0.0, neutral_u=0.0, low_step=0, neutral_step=0, high_step=0, sv_tap_step=None, regulating_control=None, **kw_args):
        """ Initialises a new 'TapChanger' instance.
        """
        # Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltagesTap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages 
        self.step_voltage_increment = step_voltage_increment

        # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting. 
        self.neutral_u = neutral_u

        # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral 
        self.low_step = low_step

        # The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value.  
        self.neutral_step = neutral_step

        # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral 
        self.high_step = high_step


        self._sv_tap_step = None
        self.sv_tap_step = sv_tap_step

        self._regulating_control = None
        self.regulating_control = regulating_control


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

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ 
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        if self._regulating_control is not None:
            filtered = [x for x in self.regulating_control.tap_changer if x != self]
            self._regulating_control._tap_changer = filtered

        self._regulating_control = value
        if self._regulating_control is not None:
            self._regulating_control._tap_changer.append(self)

    regulating_control = property(get_regulating_control, set_regulating_control)
    # >>> regulating_control


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
        if self.regulating_control is not None:
            s += '%s<%s:TapChanger.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> tap_changer.serialize


class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.
    """
    # <<< transformer_winding
    # @generated
    def __init__(self, x=0.0, b=0.0, connection_type='z', rated_s=0.0, x0=0.0, r=0.0, r0=0.0, b0=0.0, rated_u=0.0, g0=0.0, g=0.0, xground=0.0, winding_type='tertiary', rground=0.0, member_of_power_transformer=None, ratio_tap_changer=None, phase_tap_changer=None, **kw_args):
        """ Initialises a new 'TransformerWinding' instance.
        """
        # Positive sequence series reactance of the winding.Positive sequence series reactance of the winding. 
        self.x = x

        # Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag). 
        self.b = b

        # The type of connection of the winding.The type of connection of the winding. Values are: "z", "y", "d"
        self.connection_type = 'z'

        # The normal apparent power rating for the windingThe normal apparent power rating for the winding 
        self.rated_s = rated_s

        # Zero sequence series reactance of the winding.This is for Short Circuit only.Zero sequence series reactance of the winding.This is for Short Circuit only. 
        self.x0 = x0

        # Positive sequence series resistance of the winding.Positive sequence series resistance of the winding. 
        self.r = r

        # Zero sequence series resistance of the winding.This is for Short Circuit only.Zero sequence series resistance of the winding.This is for Short Circuit only. 
        self.r0 = r0

        # Zero sequence magnetizing branch susceptance.This is for Short Circuit only.Zero sequence magnetizing branch susceptance.This is for Short Circuit only. 
        self.b0 = b0

        # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        self.rated_u = rated_u

        # Zero sequence magnetizing branch conductance.This is for Short Circuit only.Zero sequence magnetizing branch conductance.This is for Short Circuit only. 
        self.g0 = g0

        # Magnetizing branch conductance (G mag).Magnetizing branch conductance (G mag). 
        self.g = g

        # Ground reactance path through connected grounding transformer.This is for Short Circuit only.Ground reactance path through connected grounding transformer.This is for Short Circuit only. 
        self.xground = xground

        # The type of winding.The type of winding. Values are: "tertiary", "primary", "secondary"
        self.winding_type = 'tertiary'

        # Ground resistance path through connected grounding transformer.This is for Short Circuit only.Ground resistance path through connected grounding transformer.This is for Short Circuit only. 
        self.rground = rground


        self._member_of_power_transformer = None
        self.member_of_power_transformer = member_of_power_transformer

        self._ratio_tap_changer = None
        self.ratio_tap_changer = ratio_tap_changer

        self._phase_tap_changer = None
        self.phase_tap_changer = phase_tap_changer


        super(TransformerWinding, self).__init__(**kw_args)
    # >>> transformer_winding

    # <<< member_of_power_transformer
    # @generated
    def get_member_of_power_transformer(self):
        """ A transformer has windingsA transformer has windings
        """
        return self._member_of_power_transformer

    def set_member_of_power_transformer(self, value):
        if self._member_of_power_transformer is not None:
            filtered = [x for x in self.member_of_power_transformer.contains_transformer_windings if x != self]
            self._member_of_power_transformer._contains_transformer_windings = filtered

        self._member_of_power_transformer = value
        if self._member_of_power_transformer is not None:
            self._member_of_power_transformer._contains_transformer_windings.append(self)

    member_of_power_transformer = property(get_member_of_power_transformer, set_member_of_power_transformer)
    # >>> member_of_power_transformer

    # <<< ratio_tap_changer
    # @generated
    def get_ratio_tap_changer(self):
        """ The ratio tap changer associated with the transformer winding.The ratio tap changer associated with the transformer winding.
        """
        return self._ratio_tap_changer

    def set_ratio_tap_changer(self, value):
        if self._ratio_tap_changer is not None:
            self._ratio_tap_changer._transformer_winding = None

        self._ratio_tap_changer = value
        if self._ratio_tap_changer is not None:
            self._ratio_tap_changer._transformer_winding = self

    ratio_tap_changer = property(get_ratio_tap_changer, set_ratio_tap_changer)
    # >>> ratio_tap_changer

    # <<< phase_tap_changer
    # @generated
    def get_phase_tap_changer(self):
        """ The phase tap changer associated with the transformer winding.The phase tap changer associated with the transformer winding.
        """
        return self._phase_tap_changer

    def set_phase_tap_changer(self, value):
        if self._phase_tap_changer is not None:
            self._phase_tap_changer._transformer_winding = None

        self._phase_tap_changer = value
        if self._phase_tap_changer is not None:
            self._phase_tap_changer._transformer_winding = self

    phase_tap_changer = property(get_phase_tap_changer, set_phase_tap_changer)
    # >>> phase_tap_changer


    def __str__(self):
        """ Returns a string representation of the TransformerWinding.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< transformer_winding.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TransformerWinding.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TransformerWinding", self.uri)
        if format:
            indent += ' ' * depth

        if self.member_of_power_transformer is not None:
            s += '%s<%s:TransformerWinding.member_of_power_transformer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_power_transformer.uri)
        if self.ratio_tap_changer is not None:
            s += '%s<%s:TransformerWinding.ratio_tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.ratio_tap_changer.uri)
        if self.phase_tap_changer is not None:
            s += '%s<%s:TransformerWinding.phase_tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.phase_tap_changer.uri)
        s += '%s<%s:TransformerWinding.x>%s</%s:TransformerWinding.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:TransformerWinding.b>%s</%s:TransformerWinding.b>' % \
            (indent, ns_prefix, self.b, ns_prefix)
        s += '%s<%s:TransformerWinding.connection_type>%s</%s:TransformerWinding.connection_type>' % \
            (indent, ns_prefix, self.connection_type, ns_prefix)
        s += '%s<%s:TransformerWinding.rated_s>%s</%s:TransformerWinding.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:TransformerWinding.x0>%s</%s:TransformerWinding.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:TransformerWinding.r>%s</%s:TransformerWinding.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:TransformerWinding.r0>%s</%s:TransformerWinding.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:TransformerWinding.b0>%s</%s:TransformerWinding.b0>' % \
            (indent, ns_prefix, self.b0, ns_prefix)
        s += '%s<%s:TransformerWinding.rated_u>%s</%s:TransformerWinding.rated_u>' % \
            (indent, ns_prefix, self.rated_u, ns_prefix)
        s += '%s<%s:TransformerWinding.g0>%s</%s:TransformerWinding.g0>' % \
            (indent, ns_prefix, self.g0, ns_prefix)
        s += '%s<%s:TransformerWinding.g>%s</%s:TransformerWinding.g>' % \
            (indent, ns_prefix, self.g, ns_prefix)
        s += '%s<%s:TransformerWinding.xground>%s</%s:TransformerWinding.xground>' % \
            (indent, ns_prefix, self.xground, ns_prefix)
        s += '%s<%s:TransformerWinding.winding_type>%s</%s:TransformerWinding.winding_type>' % \
            (indent, ns_prefix, self.winding_type, ns_prefix)
        s += '%s<%s:TransformerWinding.rground>%s</%s:TransformerWinding.rground>' % \
            (indent, ns_prefix, self.rground, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TransformerWinding")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> transformer_winding.serialize


class RegulatingControl(IdentifiedObject):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.
    """
    # <<< regulating_control
    # @generated
    def __init__(self, mode='reactive_power', discrete=False, target_value=0.0, target_range=0.0, terminal=None, regulating_cond_eq=None, tap_changer=None, **kw_args):
        """ Initialises a new 'RegulatingControl' instance.
        """
        # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule. Values are: "reactive_power", "voltage", "active_power", "current_flow", "fixed", "admittance"
        self.mode = 'reactive_power'

        # The regulation is performed in a discrete mode.The regulation is performed in a discrete mode. 
        self.discrete = discrete

        # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute. 
        self.target_value = target_value

        # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode. 
        self.target_range = target_range


        self._terminal = None
        self.terminal = terminal

        self._regulating_cond_eq = []
        if regulating_cond_eq is not None:
            self.regulating_cond_eq = regulating_cond_eq
        else:
            self.regulating_cond_eq = []

        self._tap_changer = []
        if tap_changer is not None:
            self.tap_changer = tap_changer
        else:
            self.tap_changer = []


        super(RegulatingControl, self).__init__(**kw_args)
    # >>> regulating_control

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal associated with this regulating control.The terminal associated with this regulating control.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            filtered = [x for x in self.terminal.regulating_control if x != self]
            self._terminal._regulating_control = filtered

        self._terminal = value
        if self._terminal is not None:
            self._terminal._regulating_control.append(self)

    terminal = property(get_terminal, set_terminal)
    # >>> terminal

    # <<< regulating_cond_eq
    # @generated
    def get_regulating_cond_eq(self):
        """ copy from reg cond eqcopy from reg cond eq
        """
        return self._regulating_cond_eq

    def set_regulating_cond_eq(self, value):
        for x in self._regulating_cond_eq:
            x._regulating_control = None
        for y in value:
            y._regulating_control = self
        self._regulating_cond_eq = value

    regulating_cond_eq = property(get_regulating_cond_eq, set_regulating_cond_eq)

    def add_regulating_cond_eq(self, *regulating_cond_eq):
        for obj in regulating_cond_eq:
            obj._regulating_control = self
            self._regulating_cond_eq.append(obj)

    def remove_regulating_cond_eq(self, *regulating_cond_eq):
        for obj in regulating_cond_eq:
            obj._regulating_control = None
            self._regulating_cond_eq.remove(obj)
    # >>> regulating_cond_eq

    # <<< tap_changer
    # @generated
    def get_tap_changer(self):
        """ copy from reg conduting eqcopy from reg conduting eq
        """
        return self._tap_changer

    def set_tap_changer(self, value):
        for x in self._tap_changer:
            x._regulating_control = None
        for y in value:
            y._regulating_control = self
        self._tap_changer = value

    tap_changer = property(get_tap_changer, set_tap_changer)

    def add_tap_changer(self, *tap_changer):
        for obj in tap_changer:
            obj._regulating_control = self
            self._tap_changer.append(obj)

    def remove_tap_changer(self, *tap_changer):
        for obj in tap_changer:
            obj._regulating_control = None
            self._tap_changer.remove(obj)
    # >>> tap_changer


    def __str__(self):
        """ Returns a string representation of the RegulatingControl.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regulating_control.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegulatingControl.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegulatingControl", self.uri)
        if format:
            indent += ' ' * depth

        if self.terminal is not None:
            s += '%s<%s:RegulatingControl.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        for obj in self.regulating_cond_eq:
            s += '%s<%s:RegulatingControl.regulating_cond_eq rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.tap_changer:
            s += '%s<%s:RegulatingControl.tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:RegulatingControl.mode>%s</%s:RegulatingControl.mode>' % \
            (indent, ns_prefix, self.mode, ns_prefix)
        s += '%s<%s:RegulatingControl.discrete>%s</%s:RegulatingControl.discrete>' % \
            (indent, ns_prefix, self.discrete, ns_prefix)
        s += '%s<%s:RegulatingControl.target_value>%s</%s:RegulatingControl.target_value>' % \
            (indent, ns_prefix, self.target_value, ns_prefix)
        s += '%s<%s:RegulatingControl.target_range>%s</%s:RegulatingControl.target_range>' % \
            (indent, ns_prefix, self.target_range, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegulatingControl")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regulating_control.serialize


class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.
    """
    # <<< reactive_capability_curve
    # @generated
    def __init__(self, initially_used_by_synchronous_machine=None, **kw_args):
        """ Initialises a new 'ReactiveCapabilityCurve' instance.
        """

        self._initially_used_by_synchronous_machine = []
        if initially_used_by_synchronous_machine is not None:
            self.initially_used_by_synchronous_machine = initially_used_by_synchronous_machine
        else:
            self.initially_used_by_synchronous_machine = []


        super(ReactiveCapabilityCurve, self).__init__(**kw_args)
    # >>> reactive_capability_curve

    # <<< initially_used_by_synchronous_machine
    # @generated
    def get_initially_used_by_synchronous_machine(self):
        """ Synchronous machines using this curve as default.Synchronous machines using this curve as default.
        """
        return self._initially_used_by_synchronous_machine

    def set_initially_used_by_synchronous_machine(self, value):
        for x in self._initially_used_by_synchronous_machine:
            x._initial_reactive_capability_curve = None
        for y in value:
            y._initial_reactive_capability_curve = self
        self._initially_used_by_synchronous_machine = value

    initially_used_by_synchronous_machine = property(get_initially_used_by_synchronous_machine, set_initially_used_by_synchronous_machine)

    def add_initially_used_by_synchronous_machine(self, *initially_used_by_synchronous_machine):
        for obj in initially_used_by_synchronous_machine:
            obj._initial_reactive_capability_curve = self
            self._initially_used_by_synchronous_machine.append(obj)

    def remove_initially_used_by_synchronous_machine(self, *initially_used_by_synchronous_machine):
        for obj in initially_used_by_synchronous_machine:
            obj._initial_reactive_capability_curve = None
            self._initially_used_by_synchronous_machine.remove(obj)
    # >>> initially_used_by_synchronous_machine


    def __str__(self):
        """ Returns a string representation of the ReactiveCapabilityCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< reactive_capability_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ReactiveCapabilityCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ReactiveCapabilityCurve", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.initially_used_by_synchronous_machine:
            s += '%s<%s:ReactiveCapabilityCurve.initially_used_by_synchronous_machine rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.curve_schedule_datas:
            s += '%s<%s:Curve.curve_schedule_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ReactiveCapabilityCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> reactive_capability_curve.serialize


class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.
    """
    # <<< mutual_coupling
    # @generated
    def __init__(self, distance22=0.0, g0ch=0.0, distance21=0.0, r0=0.0, b0ch=0.0, x0=0.0, distance11=0.0, distance12=0.0, first_terminal=None, second_terminal=None, **kw_args):
        """ Initialises a new 'MutualCoupling' instance.
        """
        # Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance22 = distance22

        # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
        self.g0ch = g0ch

        # Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance21 = distance21

        # Zero sequence branch-to-branch mutual impedance coupling, resistanceZero sequence branch-to-branch mutual impedance coupling, resistance 
        self.r0 = r0

        # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.b0ch = b0ch

        # Zero sequence branch-to-branch mutual impedance coupling, reactanceZero sequence branch-to-branch mutual impedance coupling, reactance 
        self.x0 = x0

        # Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance11 = distance11

        # Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance12 = distance12


        self._first_terminal = None
        self.first_terminal = first_terminal

        self._second_terminal = None
        self.second_terminal = second_terminal


        super(MutualCoupling, self).__init__(**kw_args)
    # >>> mutual_coupling

    # <<< first_terminal
    # @generated
    def get_first_terminal(self):
        """ The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
        """
        return self._first_terminal

    def set_first_terminal(self, value):
        if self._first_terminal is not None:
            filtered = [x for x in self.first_terminal.has_first_mutual_coupling if x != self]
            self._first_terminal._has_first_mutual_coupling = filtered

        self._first_terminal = value
        if self._first_terminal is not None:
            self._first_terminal._has_first_mutual_coupling.append(self)

    first_terminal = property(get_first_terminal, set_first_terminal)
    # >>> first_terminal

    # <<< second_terminal
    # @generated
    def get_second_terminal(self):
        """ The starting terminal for the calculation of distances along the second branch of the mutual coupling.The starting terminal for the calculation of distances along the second branch of the mutual coupling.
        """
        return self._second_terminal

    def set_second_terminal(self, value):
        if self._second_terminal is not None:
            filtered = [x for x in self.second_terminal.has_second_mutual_coupling if x != self]
            self._second_terminal._has_second_mutual_coupling = filtered

        self._second_terminal = value
        if self._second_terminal is not None:
            self._second_terminal._has_second_mutual_coupling.append(self)

    second_terminal = property(get_second_terminal, set_second_terminal)
    # >>> second_terminal


    def __str__(self):
        """ Returns a string representation of the MutualCoupling.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< mutual_coupling.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the MutualCoupling.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "MutualCoupling", self.uri)
        if format:
            indent += ' ' * depth

        if self.first_terminal is not None:
            s += '%s<%s:MutualCoupling.first_terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.first_terminal.uri)
        if self.second_terminal is not None:
            s += '%s<%s:MutualCoupling.second_terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.second_terminal.uri)
        s += '%s<%s:MutualCoupling.distance22>%s</%s:MutualCoupling.distance22>' % \
            (indent, ns_prefix, self.distance22, ns_prefix)
        s += '%s<%s:MutualCoupling.g0ch>%s</%s:MutualCoupling.g0ch>' % \
            (indent, ns_prefix, self.g0ch, ns_prefix)
        s += '%s<%s:MutualCoupling.distance21>%s</%s:MutualCoupling.distance21>' % \
            (indent, ns_prefix, self.distance21, ns_prefix)
        s += '%s<%s:MutualCoupling.r0>%s</%s:MutualCoupling.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:MutualCoupling.b0ch>%s</%s:MutualCoupling.b0ch>' % \
            (indent, ns_prefix, self.b0ch, ns_prefix)
        s += '%s<%s:MutualCoupling.x0>%s</%s:MutualCoupling.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:MutualCoupling.distance11>%s</%s:MutualCoupling.distance11>' % \
            (indent, ns_prefix, self.distance11, ns_prefix)
        s += '%s<%s:MutualCoupling.distance12>%s</%s:MutualCoupling.distance12>' % \
            (indent, ns_prefix, self.distance12, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "MutualCoupling")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> mutual_coupling.serialize


class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """
    # <<< power_transformer
    # @generated
    def __init__(self, contains_transformer_windings=None, **kw_args):
        """ Initialises a new 'PowerTransformer' instance.
        """

        self._contains_transformer_windings = []
        if contains_transformer_windings is not None:
            self.contains_transformer_windings = contains_transformer_windings
        else:
            self.contains_transformer_windings = []


        super(PowerTransformer, self).__init__(**kw_args)
    # >>> power_transformer

    # <<< contains_transformer_windings
    # @generated
    def get_contains_transformer_windings(self):
        """ A transformer has windingsA transformer has windings
        """
        return self._contains_transformer_windings

    def set_contains_transformer_windings(self, value):
        for x in self._contains_transformer_windings:
            x._member_of_power_transformer = None
        for y in value:
            y._member_of_power_transformer = self
        self._contains_transformer_windings = value

    contains_transformer_windings = property(get_contains_transformer_windings, set_contains_transformer_windings)

    def add_contains_transformer_windings(self, *contains_transformer_windings):
        for obj in contains_transformer_windings:
            obj._member_of_power_transformer = self
            self._contains_transformer_windings.append(obj)

    def remove_contains_transformer_windings(self, *contains_transformer_windings):
        for obj in contains_transformer_windings:
            obj._member_of_power_transformer = None
            self._contains_transformer_windings.remove(obj)
    # >>> contains_transformer_windings


    def __str__(self):
        """ Returns a string representation of the PowerTransformer.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< power_transformer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PowerTransformer.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PowerTransformer", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_transformer_windings:
            s += '%s<%s:PowerTransformer.contains_transformer_windings rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PowerTransformer")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> power_transformer.serialize


class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """
    # <<< energy_consumer
    # @generated
    def __init__(self, load_response=None, **kw_args):
        """ Initialises a new 'EnergyConsumer' instance.
        """

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
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

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
    pass
    # <<< switch
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Switch' instance.
        """


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

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Switch")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> switch.serialize


class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """
    # <<< regulating_cond_eq
    # @generated
    def __init__(self, regulating_control=None, **kw_args):
        """ Initialises a new 'RegulatingCondEq' instance.
        """

        self._regulating_control = None
        self.regulating_control = regulating_control


        super(RegulatingCondEq, self).__init__(**kw_args)
    # >>> regulating_cond_eq

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ copy from ...Regulating control scheme in which this equipment participates.copy from ...Regulating control scheme in which this equipment participates.
        """
        return self._regulating_control

    def set_regulating_control(self, value):
        if self._regulating_control is not None:
            filtered = [x for x in self.regulating_control.regulating_cond_eq if x != self]
            self._regulating_control._regulating_cond_eq = filtered

        self._regulating_control = value
        if self._regulating_control is not None:
            self._regulating_control._regulating_cond_eq.append(self)

    regulating_control = property(get_regulating_control, set_regulating_control)
    # >>> regulating_control


    def __str__(self):
        """ Returns a string representation of the RegulatingCondEq.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< regulating_cond_eq.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the RegulatingCondEq.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "RegulatingCondEq", self.uri)
        if format:
            indent += ' ' * depth

        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RegulatingCondEq")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> regulating_cond_eq.serialize


class VoltageControlZone(IdentifiedObject):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """
    # <<< voltage_control_zone
    # @generated
    def __init__(self, busbar_section=None, **kw_args):
        """ Initialises a new 'VoltageControlZone' instance.
        """

        self._busbar_section = None
        self.busbar_section = busbar_section


        super(VoltageControlZone, self).__init__(**kw_args)
    # >>> voltage_control_zone

    # <<< busbar_section
    # @generated
    def get_busbar_section(self):
        """ A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.
        """
        return self._busbar_section

    def set_busbar_section(self, value):
        if self._busbar_section is not None:
            self._busbar_section._voltage_control_zone = None

        self._busbar_section = value
        if self._busbar_section is not None:
            self._busbar_section._voltage_control_zone = self

    busbar_section = property(get_busbar_section, set_busbar_section)
    # >>> busbar_section


    def __str__(self):
        """ Returns a string representation of the VoltageControlZone.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< voltage_control_zone.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the VoltageControlZone.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "VoltageControlZone", self.uri)
        if format:
            indent += ' ' * depth

        if self.busbar_section is not None:
            s += '%s<%s:VoltageControlZone.busbar_section rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.busbar_section.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "VoltageControlZone")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> voltage_control_zone.serialize


class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """
    pass
    # <<< line
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Line' instance.
        """


        super(Line, self).__init__(**kw_args)
    # >>> line


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

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        for obj in self.topological_node:
            s += '%s<%s:ConnectivityNodeContainer.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_equipments:
            s += '%s<%s:EquipmentContainer.contains_equipments rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Line")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> line.serialize


class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """
    # <<< conductor
    # @generated
    def __init__(self, b0ch=0.0, bch=0.0, r0=0.0, x0=0.0, gch=0.0, x=0.0, length=0.0, r=0.0, g0ch=0.0, **kw_args):
        """ Initialises a new 'Conductor' instance.
        """
        # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        self.b0ch = b0ch

        # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.bch = bch

        # Zero sequence series resistance of the entire line section.This is for Short Circuit only.Zero sequence series resistance of the entire line section.This is for Short Circuit only. 
        self.r0 = r0

        # Zero sequence series reactance of the entire line section.This is for Short Circuit only.Zero sequence series reactance of the entire line section.This is for Short Circuit only. 
        self.x0 = x0

        # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        self.gch = gch

        # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section. 
        self.x = x

        # Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling. 
        self.length = length

        # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section. 
        self.r = r

        # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        self.g0ch = g0ch



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

        s += '%s<%s:Conductor.b0ch>%s</%s:Conductor.b0ch>' % \
            (indent, ns_prefix, self.b0ch, ns_prefix)
        s += '%s<%s:Conductor.bch>%s</%s:Conductor.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)
        s += '%s<%s:Conductor.r0>%s</%s:Conductor.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:Conductor.x0>%s</%s:Conductor.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:Conductor.gch>%s</%s:Conductor.gch>' % \
            (indent, ns_prefix, self.gch, ns_prefix)
        s += '%s<%s:Conductor.x>%s</%s:Conductor.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:Conductor.length>%s</%s:Conductor.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        s += '%s<%s:Conductor.r>%s</%s:Conductor.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:Conductor.g0ch>%s</%s:Conductor.g0ch>' % \
            (indent, ns_prefix, self.g0ch, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Conductor")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> conductor.serialize


class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.
    """
    pass
    # <<< acline_segment
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ACLineSegment' instance.
        """


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

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Conductor.b0ch>%s</%s:Conductor.b0ch>' % \
            (indent, ns_prefix, self.b0ch, ns_prefix)
        s += '%s<%s:Conductor.bch>%s</%s:Conductor.bch>' % \
            (indent, ns_prefix, self.bch, ns_prefix)
        s += '%s<%s:Conductor.r0>%s</%s:Conductor.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:Conductor.x0>%s</%s:Conductor.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:Conductor.gch>%s</%s:Conductor.gch>' % \
            (indent, ns_prefix, self.gch, ns_prefix)
        s += '%s<%s:Conductor.x>%s</%s:Conductor.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:Conductor.length>%s</%s:Conductor.length>' % \
            (indent, ns_prefix, self.length, ns_prefix)
        s += '%s<%s:Conductor.r>%s</%s:Conductor.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:Conductor.g0ch>%s</%s:Conductor.g0ch>' % \
            (indent, ns_prefix, self.g0ch, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ACLineSegment")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> acline_segment.serialize


class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """
    # <<< phase_tap_changer
    # @generated
    def __init__(self, x_step_min=0.0, x_step_max=0.0, step_phase_shift_increment=0.0, winding_connection_angle=0.0, phase_tap_changer_type='asymmetrical', voltage_step_increment_out_of_phase=0.0, transformer_winding=None, **kw_args):
        """ Initialises a new 'PhaseTapChanger' instance.
        """
        # The reactance at the minimum tap step.The reactance at the minimum tap step. 
        self.x_step_min = x_step_min

        # The reactance at the maximum tap step.The reactance at the maximum tap step. 
        self.x_step_max = x_step_max

        # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
        self.step_phase_shift_increment = step_phase_shift_increment

        # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is AsymmetricalThe phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is Asymmetrical 
        self.winding_connection_angle = winding_connection_angle

        # The type of phase shifter construction.The type of phase shifter construction. Values are: "asymmetrical", "symmetrical"
        self.phase_tap_changer_type = 'asymmetrical'

        # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical. 
        self.voltage_step_increment_out_of_phase = voltage_step_increment_out_of_phase


        self._transformer_winding = None
        self.transformer_winding = transformer_winding


        super(PhaseTapChanger, self).__init__(**kw_args)
    # >>> phase_tap_changer

    # <<< transformer_winding
    # @generated
    def get_transformer_winding(self):
        """ The transformer winding to which the phase tap changer belongs.The transformer winding to which the phase tap changer belongs.
        """
        return self._transformer_winding

    def set_transformer_winding(self, value):
        if self._transformer_winding is not None:
            self._transformer_winding._phase_tap_changer = None

        self._transformer_winding = value
        if self._transformer_winding is not None:
            self._transformer_winding._phase_tap_changer = self

    transformer_winding = property(get_transformer_winding, set_transformer_winding)
    # >>> transformer_winding


    def __str__(self):
        """ Returns a string representation of the PhaseTapChanger.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< phase_tap_changer.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PhaseTapChanger.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PhaseTapChanger", self.uri)
        if format:
            indent += ' ' * depth

        if self.transformer_winding is not None:
            s += '%s<%s:PhaseTapChanger.transformer_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_winding.uri)
        s += '%s<%s:PhaseTapChanger.x_step_min>%s</%s:PhaseTapChanger.x_step_min>' % \
            (indent, ns_prefix, self.x_step_min, ns_prefix)
        s += '%s<%s:PhaseTapChanger.x_step_max>%s</%s:PhaseTapChanger.x_step_max>' % \
            (indent, ns_prefix, self.x_step_max, ns_prefix)
        s += '%s<%s:PhaseTapChanger.step_phase_shift_increment>%s</%s:PhaseTapChanger.step_phase_shift_increment>' % \
            (indent, ns_prefix, self.step_phase_shift_increment, ns_prefix)
        s += '%s<%s:PhaseTapChanger.winding_connection_angle>%s</%s:PhaseTapChanger.winding_connection_angle>' % \
            (indent, ns_prefix, self.winding_connection_angle, ns_prefix)
        s += '%s<%s:PhaseTapChanger.phase_tap_changer_type>%s</%s:PhaseTapChanger.phase_tap_changer_type>' % \
            (indent, ns_prefix, self.phase_tap_changer_type, ns_prefix)
        s += '%s<%s:PhaseTapChanger.voltage_step_increment_out_of_phase>%s</%s:PhaseTapChanger.voltage_step_increment_out_of_phase>' % \
            (indent, ns_prefix, self.voltage_step_increment_out_of_phase, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.sv_tap_step is not None:
            s += '%s<%s:TapChanger.sv_tap_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_tap_step.uri)
        if self.regulating_control is not None:
            s += '%s<%s:TapChanger.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PhaseTapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> phase_tap_changer.serialize


class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. 
    """
    # <<< synchronous_machine
    # @generated
    def __init__(self, x0=0.0, operating_mode='condenser', r0=0.0, q_percent=0.0, x2=0.0, type='condenser', r2=0.0, r=0.0, max_q=0.0, x=0.0, rated_s=0.0, min_q=0.0, initial_reactive_capability_curve=None, drives_hydro_pump=None, member_of_generating_unit=None, **kw_args):
        """ Initialises a new 'SynchronousMachine' instance.
        """
        # Zero sequence reactance of the synchronous machine.This is for Short Circuit only.Zero sequence reactance of the synchronous machine.This is for Short Circuit only. 
        self.x0 = x0

        # Current mode of operation.Current mode of operation. Values are: "condenser", "generator"
        self.operating_mode = 'condenser'

        # Zero sequence resistance of the synchronous machine.This is for Short Circuit only.Zero sequence resistance of the synchronous machine.This is for Short Circuit only. 
        self.r0 = r0

        # Percent of the coordinated reactive control that comes from this machine.Percent of the coordinated reactive control that comes from this machine. 
        self.q_percent = q_percent

        # Negative sequence reactance.This is for Short Circuit only.Negative sequence reactance.This is for Short Circuit only. 
        self.x2 = x2

        # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = 'condenser'

        # Negative sequence resistance.This is for Short Circuit only.Negative sequence resistance.This is for Short Circuit only. 
        self.r2 = r2

        # Positive sequence resistance of the synchronous machine.Positive sequence resistance of the synchronous machine. 
        self.r = r

        # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        self.max_q = max_q

        # Positive sequence reactance of the synchronous machine.Positive sequence reactance of the synchronous machine. 
        self.x = x

        # Nameplate apparent power rating for the unitNameplate apparent power rating for the unit 
        self.rated_s = rated_s

        # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit. 
        self.min_q = min_q


        self._initial_reactive_capability_curve = None
        self.initial_reactive_capability_curve = initial_reactive_capability_curve

        self._drives_hydro_pump = None
        self.drives_hydro_pump = drives_hydro_pump

        self._member_of_generating_unit = None
        self.member_of_generating_unit = member_of_generating_unit


        super(SynchronousMachine, self).__init__(**kw_args)
    # >>> synchronous_machine

    # <<< initial_reactive_capability_curve
    # @generated
    def get_initial_reactive_capability_curve(self):
        """ The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine
        """
        return self._initial_reactive_capability_curve

    def set_initial_reactive_capability_curve(self, value):
        if self._initial_reactive_capability_curve is not None:
            filtered = [x for x in self.initial_reactive_capability_curve.initially_used_by_synchronous_machine if x != self]
            self._initial_reactive_capability_curve._initially_used_by_synchronous_machine = filtered

        self._initial_reactive_capability_curve = value
        if self._initial_reactive_capability_curve is not None:
            self._initial_reactive_capability_curve._initially_used_by_synchronous_machine.append(self)

    initial_reactive_capability_curve = property(get_initial_reactive_capability_curve, set_initial_reactive_capability_curve)
    # >>> initial_reactive_capability_curve

    # <<< drives_hydro_pump
    # @generated
    def get_drives_hydro_pump(self):
        """ The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._drives_hydro_pump

    def set_drives_hydro_pump(self, value):
        if self._drives_hydro_pump is not None:
            self._drives_hydro_pump._driven_by_synchronous_machine = None

        self._drives_hydro_pump = value
        if self._drives_hydro_pump is not None:
            self._drives_hydro_pump._driven_by_synchronous_machine = self

    drives_hydro_pump = property(get_drives_hydro_pump, set_drives_hydro_pump)
    # >>> drives_hydro_pump

    # <<< member_of_generating_unit
    # @generated
    def get_member_of_generating_unit(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
        """
        return self._member_of_generating_unit

    def set_member_of_generating_unit(self, value):
        if self._member_of_generating_unit is not None:
            filtered = [x for x in self.member_of_generating_unit.contains_synchronous_machines if x != self]
            self._member_of_generating_unit._contains_synchronous_machines = filtered

        self._member_of_generating_unit = value
        if self._member_of_generating_unit is not None:
            self._member_of_generating_unit._contains_synchronous_machines.append(self)

    member_of_generating_unit = property(get_member_of_generating_unit, set_member_of_generating_unit)
    # >>> member_of_generating_unit


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

        if self.initial_reactive_capability_curve is not None:
            s += '%s<%s:SynchronousMachine.initial_reactive_capability_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.initial_reactive_capability_curve.uri)
        if self.drives_hydro_pump is not None:
            s += '%s<%s:SynchronousMachine.drives_hydro_pump rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.drives_hydro_pump.uri)
        if self.member_of_generating_unit is not None:
            s += '%s<%s:SynchronousMachine.member_of_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_generating_unit.uri)
        s += '%s<%s:SynchronousMachine.x0>%s</%s:SynchronousMachine.x0>' % \
            (indent, ns_prefix, self.x0, ns_prefix)
        s += '%s<%s:SynchronousMachine.operating_mode>%s</%s:SynchronousMachine.operating_mode>' % \
            (indent, ns_prefix, self.operating_mode, ns_prefix)
        s += '%s<%s:SynchronousMachine.r0>%s</%s:SynchronousMachine.r0>' % \
            (indent, ns_prefix, self.r0, ns_prefix)
        s += '%s<%s:SynchronousMachine.q_percent>%s</%s:SynchronousMachine.q_percent>' % \
            (indent, ns_prefix, self.q_percent, ns_prefix)
        s += '%s<%s:SynchronousMachine.x2>%s</%s:SynchronousMachine.x2>' % \
            (indent, ns_prefix, self.x2, ns_prefix)
        s += '%s<%s:SynchronousMachine.type>%s</%s:SynchronousMachine.type>' % \
            (indent, ns_prefix, self.type, ns_prefix)
        s += '%s<%s:SynchronousMachine.r2>%s</%s:SynchronousMachine.r2>' % \
            (indent, ns_prefix, self.r2, ns_prefix)
        s += '%s<%s:SynchronousMachine.r>%s</%s:SynchronousMachine.r>' % \
            (indent, ns_prefix, self.r, ns_prefix)
        s += '%s<%s:SynchronousMachine.max_q>%s</%s:SynchronousMachine.max_q>' % \
            (indent, ns_prefix, self.max_q, ns_prefix)
        s += '%s<%s:SynchronousMachine.x>%s</%s:SynchronousMachine.x>' % \
            (indent, ns_prefix, self.x, ns_prefix)
        s += '%s<%s:SynchronousMachine.rated_s>%s</%s:SynchronousMachine.rated_s>' % \
            (indent, ns_prefix, self.rated_s, ns_prefix)
        s += '%s<%s:SynchronousMachine.min_q>%s</%s:SynchronousMachine.min_q>' % \
            (indent, ns_prefix, self.min_q, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SynchronousMachine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> synchronous_machine.serialize


class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """
    # <<< ratio_tap_changer
    # @generated
    def __init__(self, transformer_winding=None, **kw_args):
        """ Initialises a new 'RatioTapChanger' instance.
        """

        self._transformer_winding = None
        self.transformer_winding = transformer_winding


        super(RatioTapChanger, self).__init__(**kw_args)
    # >>> ratio_tap_changer

    # <<< transformer_winding
    # @generated
    def get_transformer_winding(self):
        """ The transformer winding to which the ratio tap changer belongs.The transformer winding to which the ratio tap changer belongs.
        """
        return self._transformer_winding

    def set_transformer_winding(self, value):
        if self._transformer_winding is not None:
            self._transformer_winding._ratio_tap_changer = None

        self._transformer_winding = value
        if self._transformer_winding is not None:
            self._transformer_winding._ratio_tap_changer = self

    transformer_winding = property(get_transformer_winding, set_transformer_winding)
    # >>> transformer_winding


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

        if self.transformer_winding is not None:
            s += '%s<%s:RatioTapChanger.transformer_winding rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.transformer_winding.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.sv_tap_step is not None:
            s += '%s<%s:TapChanger.sv_tap_step rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_tap_step.uri)
        if self.regulating_control is not None:
            s += '%s<%s:TapChanger.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)
        s += '%s<%s:TapChanger.step_voltage_increment>%s</%s:TapChanger.step_voltage_increment>' % \
            (indent, ns_prefix, self.step_voltage_increment, ns_prefix)
        s += '%s<%s:TapChanger.neutral_u>%s</%s:TapChanger.neutral_u>' % \
            (indent, ns_prefix, self.neutral_u, ns_prefix)
        s += '%s<%s:TapChanger.low_step>%s</%s:TapChanger.low_step>' % \
            (indent, ns_prefix, self.low_step, ns_prefix)
        s += '%s<%s:TapChanger.neutral_step>%s</%s:TapChanger.neutral_step>' % \
            (indent, ns_prefix, self.neutral_step, ns_prefix)
        s += '%s<%s:TapChanger.high_step>%s</%s:TapChanger.high_step>' % \
            (indent, ns_prefix, self.high_step, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "RatioTapChanger")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> ratio_tap_changer.serialize


class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.
    """
    # <<< shunt_compensator
    # @generated
    def __init__(self, b0_per_section=0.0, maximum_sections=0, g0_per_section=0.0, b_per_section=0.0, g_per_section=0.0, sv_shunt_compensator_sections=None, **kw_args):
        """ Initialises a new 'ShuntCompensator' instance.
        """
        # Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only. 
        self.b0_per_section = b0_per_section

        # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in. 
        self.maximum_sections = maximum_sections

        # Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only. 
        self.g0_per_section = g0_per_section

        # Positive sequence shunt (charging) susceptance per sectionPositive sequence shunt (charging) susceptance per section 
        self.b_per_section = b_per_section

        # Positive sequence shunt (charging) conductance per sectionPositive sequence shunt (charging) conductance per section 
        self.g_per_section = g_per_section


        self._sv_shunt_compensator_sections = None
        self.sv_shunt_compensator_sections = sv_shunt_compensator_sections


        super(ShuntCompensator, self).__init__(**kw_args)
    # >>> shunt_compensator

    # <<< sv_shunt_compensator_sections
    # @generated
    def get_sv_shunt_compensator_sections(self):
        """ The state for the number of shunt compensator sections in service.The state for the number of shunt compensator sections in service.
        """
        return self._sv_shunt_compensator_sections

    def set_sv_shunt_compensator_sections(self, value):
        if self._sv_shunt_compensator_sections is not None:
            self._sv_shunt_compensator_sections._shunt_compensator = None

        self._sv_shunt_compensator_sections = value
        if self._sv_shunt_compensator_sections is not None:
            self._sv_shunt_compensator_sections._shunt_compensator = self

    sv_shunt_compensator_sections = property(get_sv_shunt_compensator_sections, set_sv_shunt_compensator_sections)
    # >>> sv_shunt_compensator_sections


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

        if self.sv_shunt_compensator_sections is not None:
            s += '%s<%s:ShuntCompensator.sv_shunt_compensator_sections rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_shunt_compensator_sections.uri)
        s += '%s<%s:ShuntCompensator.b0_per_section>%s</%s:ShuntCompensator.b0_per_section>' % \
            (indent, ns_prefix, self.b0_per_section, ns_prefix)
        s += '%s<%s:ShuntCompensator.maximum_sections>%s</%s:ShuntCompensator.maximum_sections>' % \
            (indent, ns_prefix, self.maximum_sections, ns_prefix)
        s += '%s<%s:ShuntCompensator.g0_per_section>%s</%s:ShuntCompensator.g0_per_section>' % \
            (indent, ns_prefix, self.g0_per_section, ns_prefix)
        s += '%s<%s:ShuntCompensator.b_per_section>%s</%s:ShuntCompensator.b_per_section>' % \
            (indent, ns_prefix, self.b_per_section, ns_prefix)
        s += '%s<%s:ShuntCompensator.g_per_section>%s</%s:ShuntCompensator.g_per_section>' % \
            (indent, ns_prefix, self.g_per_section, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        if self.base_voltage is not None:
            s += '%s<%s:ConductingEquipment.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        for obj in self.terminals:
            s += '%s<%s:ConductingEquipment.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.regulating_control is not None:
            s += '%s<%s:RegulatingCondEq.regulating_control rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.regulating_control.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ShuntCompensator")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> shunt_compensator.serialize


# <<< wires
# @generated
# >>> wires
