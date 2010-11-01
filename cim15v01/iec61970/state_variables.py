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

""" State variables for analysis solutions such as powerflow.
"""

from cim15v01 import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimStateVariables"

ns_uri = "http://iec.ch/TC57/CIM-generic#StateVariables"

class StateVariable(Element):
    """ An abstract class for state variables.
    """
    pass
    # <<< state_variable
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'StateVariable' instance.

        """


        super(StateVariable, self).__init__(*args, **kw_args)
    # >>> state_variable



class SvInjection(StateVariable):
    """ Injectixon state variable.
    """
    # <<< sv_injection
    # @generated
    def __init__(self, p_net_injection=0.0, q_net_injection=0.0, topological_node=None, *args, **kw_args):
        """ Initialises a new 'SvInjection' instance.

        @param p_net_injection: The activive power injected into the bus at this location. 
        @param q_net_injection: The activive power injected into the bus at this location. 
        @param topological_node: The topological node associated with the state injection.
        """
        # The activive power injected into the bus at this location. 
        self.p_net_injection = p_net_injection

        # The activive power injected into the bus at this location. 
        self.q_net_injection = q_net_injection


        self._topological_node = None
        self.topological_node = topological_node


        super(SvInjection, self).__init__(*args, **kw_args)
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



class SvPowerFlow(StateVariable):
    """ State variable for power flow.
    """
    # <<< sv_power_flow
    # @generated
    def __init__(self, p=0.0, q=0.0, terminal=None, *args, **kw_args):
        """ Initialises a new 'SvPowerFlow' instance.

        @param p: The active power flow into the terminal. 
        @param q: The reactive power flow into the terminal. 
        @param terminal: The terminal associated with the power flow state.
        """
        # The active power flow into the terminal. 
        self.p = p

        # The reactive power flow into the terminal. 
        self.q = q


        self._terminal = None
        self.terminal = terminal


        super(SvPowerFlow, self).__init__(*args, **kw_args)
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



class SvStatus(StateVariable):
    """ State variable for status.
    """
    # <<< sv_status
    # @generated
    def __init__(self, in_service=False, conducting_equipment=None, *args, **kw_args):
        """ Initialises a new 'SvStatus' instance.

        @param in_service: The in service status as a result of topology processing. 
        @param conducting_equipment: The conducting equipment associated with the status state.
        """
        # The in service status as a result of topology processing. 
        self.in_service = in_service


        self._conducting_equipment = None
        self.conducting_equipment = conducting_equipment


        super(SvStatus, self).__init__(*args, **kw_args)
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



class SvVoltage(StateVariable):
    """ State variable for voltage.
    """
    # <<< sv_voltage
    # @generated
    def __init__(self, v=0.0, angle=0.0, topological_node=None, *args, **kw_args):
        """ Initialises a new 'SvVoltage' instance.

        @param v: The voltage magnitude of the topological node. 
        @param angle: The voltage angle in radians of the topological node. 
        @param topological_node: The topological node associated with the voltage state.
        """
        # The voltage magnitude of the topological node. 
        self.v = v

        # The voltage angle in radians of the topological node. 
        self.angle = angle


        self._topological_node = None
        self.topological_node = topological_node


        super(SvVoltage, self).__init__(*args, **kw_args)
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



class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.
    """
    # <<< sv_tap_step
    # @generated
    def __init__(self, position=0, continuous_position=0.0, tap_changer=None, *args, **kw_args):
        """ Initialises a new 'SvTapStep' instance.

        @param position: The integer tap position. 
        @param continuous_position: The floating point tap position. 
        @param tap_changer: The tap changer associated with the tap step state.
        """
        # The integer tap position. 
        self.position = position

        # The floating point tap position. 
        self.continuous_position = continuous_position


        self._tap_changer = None
        self.tap_changer = tap_changer


        super(SvTapStep, self).__init__(*args, **kw_args)
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



class SvShortCircuit(StateVariable):
    """ State variable for short circuit.
    """
    # <<< sv_short_circuit
    # @generated
    def __init__(self, x_per_r=0.0, r0_per_r=0.0, s_short_circuit=0.0, x0_per_x=0.0, topological_node=None, *args, **kw_args):
        """ Initialises a new 'SvShortCircuit' instance.

        @param x_per_r: Ratio of positive sequence reactance per postive sequence resistance. 
        @param r0_per_r: The ratio of zero sequence resistance to positive sequence resistance. 
        @param s_short_circuit: The short circuit apparent power drawn at this node when faulted. 
        @param x0_per_x: The ratio of zero sequence reactance per positive sequence reactance. 
        @param topological_node: The topological node associated with the short circuit state.
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


        super(SvShortCircuit, self).__init__(*args, **kw_args)
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



class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.
    """
    # <<< sv_shunt_compensator_sections
    # @generated
    def __init__(self, sections=0, continuous_sections=0.0, shunt_compensator=None, *args, **kw_args):
        """ Initialises a new 'SvShuntCompensatorSections' instance.

        @param sections: The number of sections in service. 
        @param continuous_sections: The number of sections in service as a continous variable. 
        @param shunt_compensator: The shunt compensator for which the state applies.
        """
        # The number of sections in service. 
        self.sections = sections

        # The number of sections in service as a continous variable. 
        self.continuous_sections = continuous_sections


        self._shunt_compensator = None
        self.shunt_compensator = shunt_compensator


        super(SvShuntCompensatorSections, self).__init__(*args, **kw_args)
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



# <<< state_variables
# @generated
# >>> state_variables
