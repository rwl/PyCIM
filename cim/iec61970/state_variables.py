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

""" State variables for analysis solutions such as powerflow.
"""

from cim import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim.statevariables"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#StateVariables"

class StateVariable(Element):
    """ An abstract class for state variables.
    """
    pass
    # <<< state_variable
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'StateVariable' instance.
        """


        super(StateVariable, self).__init__(**kw_args)
    # >>> state_variable


    def __str__(self):
        """ Returns a string representation of the StateVariable.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< state_variable.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the StateVariable.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "StateVariable", self.uri)
        if format:
            indent += ' ' * depth

        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StateVariable")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> state_variable.serialize


class SvInjection(StateVariable):
    """ Injectixon state variable.
    """
    # <<< sv_injection
    # @generated
    def __init__(self, p_net_injection=0.0, q_net_injection=0.0, topological_node=None, **kw_args):
        """ Initialises a new 'SvInjection' instance.
        """
        # The activive power injected into the bus at this location. 
        self.p_net_injection = p_net_injection

        # The activive power injected into the bus at this location. 
        self.q_net_injection = q_net_injection


        self._topological_node = None
        self.topological_node = topological_node


        super(SvInjection, self).__init__(**kw_args)
    # >>> sv_injection

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological node associated with the state injection.
        """
        return self._topological_node

    def set_topological_node(self, value):
        if self._topological_node is not None:
            self._topological_node._sv_injection = None

        self._topological_node = value
        if self._topological_node is not None:
            self._topological_node._sv_injection = self

    topological_node = property(get_topological_node, set_topological_node)
    # >>> topological_node


    def __str__(self):
        """ Returns a string representation of the SvInjection.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_injection.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvInjection.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvInjection", self.uri)
        if format:
            indent += ' ' * depth

        if self.topological_node is not None:
            s += '%s<%s:SvInjection.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.topological_node.uri)
        s += '%s<%s:SvInjection.p_net_injection>%s</%s:SvInjection.p_net_injection>' % \
            (indent, ns_prefix, self.p_net_injection, ns_prefix)
        s += '%s<%s:SvInjection.q_net_injection>%s</%s:SvInjection.q_net_injection>' % \
            (indent, ns_prefix, self.q_net_injection, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvInjection")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_injection.serialize


class SvPowerFlow(StateVariable):
    """ State variable for power flow.
    """
    # <<< sv_power_flow
    # @generated
    def __init__(self, p=0.0, q=0.0, terminal=None, **kw_args):
        """ Initialises a new 'SvPowerFlow' instance.
        """
        # The active power flow into the terminal. 
        self.p = p

        # The reactive power flow into the terminal. 
        self.q = q


        self._terminal = None
        self.terminal = terminal


        super(SvPowerFlow, self).__init__(**kw_args)
    # >>> sv_power_flow

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal associated with the power flow state.
        """
        return self._terminal

    def set_terminal(self, value):
        if self._terminal is not None:
            self._terminal._sv_power_flow = None

        self._terminal = value
        if self._terminal is not None:
            self._terminal._sv_power_flow = self

    terminal = property(get_terminal, set_terminal)
    # >>> terminal


    def __str__(self):
        """ Returns a string representation of the SvPowerFlow.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_power_flow.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvPowerFlow.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvPowerFlow", self.uri)
        if format:
            indent += ' ' * depth

        if self.terminal is not None:
            s += '%s<%s:SvPowerFlow.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.terminal.uri)
        s += '%s<%s:SvPowerFlow.p>%s</%s:SvPowerFlow.p>' % \
            (indent, ns_prefix, self.p, ns_prefix)
        s += '%s<%s:SvPowerFlow.q>%s</%s:SvPowerFlow.q>' % \
            (indent, ns_prefix, self.q, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvPowerFlow")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_power_flow.serialize


class SvStatus(StateVariable):
    """ State variable for status.
    """
    # <<< sv_status
    # @generated
    def __init__(self, in_service=False, conducting_equipment=None, **kw_args):
        """ Initialises a new 'SvStatus' instance.
        """
        # The in service status as a result of topology processing. 
        self.in_service = in_service


        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment


        super(SvStatus, self).__init__(**kw_args)
    # >>> sv_status

    # <<< conducting_equipment
    # @generated
    def get_conducting_equipment(self):
        """ The conducting equipment associated with the status state.
        """
        return self._conducting_equipment

    def set_conducting_equipment(self, value):
        if self._conducting_equipment is not None:
            self._conducting_equipment._sv_status = None

        self._conducting_equipment = value
        if self._conducting_equipment is not None:
            self._conducting_equipment._sv_status = self

    conducting_equipment = property(get_conducting_equipment, set_conducting_equipment)
    # >>> conducting_equipment


    def __str__(self):
        """ Returns a string representation of the SvStatus.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_status.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvStatus.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvStatus", self.uri)
        if format:
            indent += ' ' * depth

        if self.conducting_equipment is not None:
            s += '%s<%s:SvStatus.conducting_equipment rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.conducting_equipment.uri)
        s += '%s<%s:SvStatus.in_service>%s</%s:SvStatus.in_service>' % \
            (indent, ns_prefix, self.in_service, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvStatus")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_status.serialize


class SvVoltage(StateVariable):
    """ State variable for voltage.
    """
    # <<< sv_voltage
    # @generated
    def __init__(self, v=0.0, angle=0.0, topological_node=None, **kw_args):
        """ Initialises a new 'SvVoltage' instance.
        """
        # The voltage magnitude of the topological node. 
        self.v = v

        # The voltage angle in radians of the topological node. 
        self.angle = angle


        self._topological_node = None
        self.topological_node = topological_node


        super(SvVoltage, self).__init__(**kw_args)
    # >>> sv_voltage

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological node associated with the voltage state.
        """
        return self._topological_node

    def set_topological_node(self, value):
        if self._topological_node is not None:
            self._topological_node._sv_voltage = None

        self._topological_node = value
        if self._topological_node is not None:
            self._topological_node._sv_voltage = self

    topological_node = property(get_topological_node, set_topological_node)
    # >>> topological_node


    def __str__(self):
        """ Returns a string representation of the SvVoltage.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_voltage.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvVoltage.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvVoltage", self.uri)
        if format:
            indent += ' ' * depth

        if self.topological_node is not None:
            s += '%s<%s:SvVoltage.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.topological_node.uri)
        s += '%s<%s:SvVoltage.v>%s</%s:SvVoltage.v>' % \
            (indent, ns_prefix, self.v, ns_prefix)
        s += '%s<%s:SvVoltage.angle>%s</%s:SvVoltage.angle>' % \
            (indent, ns_prefix, self.angle, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvVoltage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_voltage.serialize


class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """
    # <<< sv_tap_step
    # @generated
    def __init__(self, position=0, continuous_position=0.0, tap_changer=None, **kw_args):
        """ Initialises a new 'SvTapStep' instance.
        """
        # The integer tap position. 
        self.position = position

        # The floating point tap position. 
        self.continuous_position = continuous_position


        self._tap_changer = None
        self.tap_changer = tap_changer


        super(SvTapStep, self).__init__(**kw_args)
    # >>> sv_tap_step

    # <<< tap_changer
    # @generated
    def get_tap_changer(self):
        """ The tap changer associated with the tap step state.
        """
        return self._tap_changer

    def set_tap_changer(self, value):
        if self._tap_changer is not None:
            self._tap_changer._sv_tap_step = None

        self._tap_changer = value
        if self._tap_changer is not None:
            self._tap_changer._sv_tap_step = self

    tap_changer = property(get_tap_changer, set_tap_changer)
    # >>> tap_changer


    def __str__(self):
        """ Returns a string representation of the SvTapStep.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_tap_step.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvTapStep.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvTapStep", self.uri)
        if format:
            indent += ' ' * depth

        if self.tap_changer is not None:
            s += '%s<%s:SvTapStep.tap_changer rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.tap_changer.uri)
        s += '%s<%s:SvTapStep.position>%s</%s:SvTapStep.position>' % \
            (indent, ns_prefix, self.position, ns_prefix)
        s += '%s<%s:SvTapStep.continuous_position>%s</%s:SvTapStep.continuous_position>' % \
            (indent, ns_prefix, self.continuous_position, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvTapStep")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_tap_step.serialize


class SvShortCircuit(StateVariable):
    """ State variable for short circuit.
    """
    # <<< sv_short_circuit
    # @generated
    def __init__(self, x_per_r=0.0, r0_per_r=0.0, s_short_circuit=0.0, x0_per_x=0.0, topological_node=None, **kw_args):
        """ Initialises a new 'SvShortCircuit' instance.
        """
        # Ratio of positive sequence reactance per postive sequence resistance. 
        self.x_per_r = x_per_r

        # The ratio of zero sequence resistance to positive sequence resistance. 
        self.r0_per_r = r0_per_r

        # The short circuit apparent power drawn at this node when faulted. 
        self.s_short_circuit = s_short_circuit

        # The ratio of zero sequence reactance per positive sequence reactance. 
        self.x0_per_x = x0_per_x


        self._topological_node = None
        self.topological_node = topological_node


        super(SvShortCircuit, self).__init__(**kw_args)
    # >>> sv_short_circuit

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological node associated with the short circuit state.
        """
        return self._topological_node

    def set_topological_node(self, value):
        if self._topological_node is not None:
            self._topological_node._sv_short_circuit = None

        self._topological_node = value
        if self._topological_node is not None:
            self._topological_node._sv_short_circuit = self

    topological_node = property(get_topological_node, set_topological_node)
    # >>> topological_node


    def __str__(self):
        """ Returns a string representation of the SvShortCircuit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_short_circuit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvShortCircuit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvShortCircuit", self.uri)
        if format:
            indent += ' ' * depth

        if self.topological_node is not None:
            s += '%s<%s:SvShortCircuit.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.topological_node.uri)
        s += '%s<%s:SvShortCircuit.x_per_r>%s</%s:SvShortCircuit.x_per_r>' % \
            (indent, ns_prefix, self.x_per_r, ns_prefix)
        s += '%s<%s:SvShortCircuit.r0_per_r>%s</%s:SvShortCircuit.r0_per_r>' % \
            (indent, ns_prefix, self.r0_per_r, ns_prefix)
        s += '%s<%s:SvShortCircuit.s_short_circuit>%s</%s:SvShortCircuit.s_short_circuit>' % \
            (indent, ns_prefix, self.s_short_circuit, ns_prefix)
        s += '%s<%s:SvShortCircuit.x0_per_x>%s</%s:SvShortCircuit.x0_per_x>' % \
            (indent, ns_prefix, self.x0_per_x, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvShortCircuit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_short_circuit.serialize


class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.
    """
    # <<< sv_shunt_compensator_sections
    # @generated
    def __init__(self, sections=0, continuous_sections=0.0, shunt_compensator=None, **kw_args):
        """ Initialises a new 'SvShuntCompensatorSections' instance.
        """
        # The number of sections in service. 
        self.sections = sections

        # The number of sections in service as a continous variable. 
        self.continuous_sections = continuous_sections


        self._shunt_compensator = None
        self.shunt_compensator = shunt_compensator


        super(SvShuntCompensatorSections, self).__init__(**kw_args)
    # >>> sv_shunt_compensator_sections

    # <<< shunt_compensator
    # @generated
    def get_shunt_compensator(self):
        """ The shunt compensator for which the state applies.
        """
        return self._shunt_compensator

    def set_shunt_compensator(self, value):
        if self._shunt_compensator is not None:
            self._shunt_compensator._sv_shunt_compensator_sections = None

        self._shunt_compensator = value
        if self._shunt_compensator is not None:
            self._shunt_compensator._sv_shunt_compensator_sections = self

    shunt_compensator = property(get_shunt_compensator, set_shunt_compensator)
    # >>> shunt_compensator


    def __str__(self):
        """ Returns a string representation of the SvShuntCompensatorSections.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< sv_shunt_compensator_sections.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SvShuntCompensatorSections.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SvShuntCompensatorSections", self.uri)
        if format:
            indent += ' ' * depth

        if self.shunt_compensator is not None:
            s += '%s<%s:SvShuntCompensatorSections.shunt_compensator rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.shunt_compensator.uri)
        s += '%s<%s:SvShuntCompensatorSections.sections>%s</%s:SvShuntCompensatorSections.sections>' % \
            (indent, ns_prefix, self.sections, ns_prefix)
        s += '%s<%s:SvShuntCompensatorSections.continuous_sections>%s</%s:SvShuntCompensatorSections.continuous_sections>' % \
            (indent, ns_prefix, self.continuous_sections, ns_prefix)
        if self.parent is not None:
            s += '%s<%s:Element.parent rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.parent.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvShuntCompensatorSections")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_shunt_compensator_sections.serialize


# <<< state_variables
# @generated
# >>> state_variables
