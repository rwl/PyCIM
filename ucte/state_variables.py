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

""" State variables for analysis solutions such as powerflow.State variables for analysis solutions such as powerflow.
"""

from ucte import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_StateVariables"

class StateVariable(Element):
    """ An abstract class for state variables.An abstract class for state variables.
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

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "StateVariable")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> state_variable.serialize


class SvVoltage(StateVariable):
    """ State variable for voltage.State variable for voltage.
    """
    # <<< sv_voltage
    # @generated
    def __init__(self, angle=0.0, v=0.0, topological_node=None, **kw_args):
        """ Initialises a new 'SvVoltage' instance.
        """
        # The voltage angle in radians of the topological node.The voltage angle in radians of the topological node. 
        self.angle = angle

        # The voltage magnitude of the topological node.The voltage magnitude of the topological node. 
        self.v = v


        self._topological_node = None
        self.topological_node = topological_node


        super(SvVoltage, self).__init__(**kw_args)
    # >>> sv_voltage

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ The topological node associated with the voltage state.The topological node associated with the voltage state.
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
        s += '%s<%s:SvVoltage.angle>%s</%s:SvVoltage.angle>' % \
            (indent, ns_prefix, self.angle, ns_prefix)
        s += '%s<%s:SvVoltage.v>%s</%s:SvVoltage.v>' % \
            (indent, ns_prefix, self.v, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvVoltage")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_voltage.serialize


class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.
    """
    # <<< sv_shunt_compensator_sections
    # @generated
    def __init__(self, continuous_sections=0.0, shunt_compensator=None, **kw_args):
        """ Initialises a new 'SvShuntCompensatorSections' instance.
        """
        # The number of sections in service as a continous variable.The number of sections in service as a continous variable. 
        self.continuous_sections = continuous_sections


        self._shunt_compensator = None
        self.shunt_compensator = shunt_compensator


        super(SvShuntCompensatorSections, self).__init__(**kw_args)
    # >>> sv_shunt_compensator_sections

    # <<< shunt_compensator
    # @generated
    def get_shunt_compensator(self):
        """ The shunt compensator for which the state applies.The shunt compensator for which the state applies.
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
        s += '%s<%s:SvShuntCompensatorSections.continuous_sections>%s</%s:SvShuntCompensatorSections.continuous_sections>' % \
            (indent, ns_prefix, self.continuous_sections, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvShuntCompensatorSections")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_shunt_compensator_sections.serialize


class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.
    """
    # <<< sv_tap_step
    # @generated
    def __init__(self, continuous_position=0.0, tap_changer=None, **kw_args):
        """ Initialises a new 'SvTapStep' instance.
        """
        # The floating point tap position.The floating point tap position. 
        self.continuous_position = continuous_position


        self._tap_changer = None
        self.tap_changer = tap_changer


        super(SvTapStep, self).__init__(**kw_args)
    # >>> sv_tap_step

    # <<< tap_changer
    # @generated
    def get_tap_changer(self):
        """ The tap changer associated with the tap step state.The tap changer associated with the tap step state.
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
        s += '%s<%s:SvTapStep.continuous_position>%s</%s:SvTapStep.continuous_position>' % \
            (indent, ns_prefix, self.continuous_position, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvTapStep")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_tap_step.serialize


class SvPowerFlow(StateVariable):
    """ State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.
    """
    # <<< sv_power_flow
    # @generated
    def __init__(self, p=0.0, q=0.0, terminal=None, **kw_args):
        """ Initialises a new 'SvPowerFlow' instance.
        """
        # The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment.The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
        self.p = p

        # The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment.The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
        self.q = q


        self._terminal = None
        self.terminal = terminal


        super(SvPowerFlow, self).__init__(**kw_args)
    # >>> sv_power_flow

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
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
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SvPowerFlow")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> sv_power_flow.serialize


# <<< state_variables
# @generated
# >>> state_variables
