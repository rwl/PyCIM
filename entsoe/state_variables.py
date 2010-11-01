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

from entsoe import Element

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_StateVariables"

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



class SvVoltage(StateVariable):
    """ State variable for voltage.
    """
    # <<< sv_voltage
    # @generated
    def __init__(self, angle=0.0, v=0.0, topological_node=None, *args, **kw_args):
        """ Initialises a new 'SvVoltage' instance.

        @param angle: The voltage angle in radians of the topological node. 
        @param v: The voltage magnitude of the topological node. 
        @param topological_node: The topological node associated with the voltage state.
        """
        # The voltage angle in radians of the topological node. 
        self.angle = angle

        # The voltage magnitude of the topological node. 
        self.v = v


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



class SvShuntCompensatorSections(StateVariable):
    """ State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.
    """
    # <<< sv_shunt_compensator_sections
    # @generated
    def __init__(self, continuous_sections=0.0, shunt_compensator=None, *args, **kw_args):
        """ Initialises a new 'SvShuntCompensatorSections' instance.

        @param continuous_sections: The number of sections in service as a continous variable. 
        @param shunt_compensator: The shunt compensator for which the state applies.
        """
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



class SvTapStep(StateVariable):
    """ State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.
    """
    # <<< sv_tap_step
    # @generated
    def __init__(self, continuous_position=0.0, tap_changer=None, *args, **kw_args):
        """ Initialises a new 'SvTapStep' instance.

        @param continuous_position: The floating point tap position. 
        @param tap_changer: The tap changer associated with the tap step state.
        """
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



class SvPowerFlow(StateVariable):
    """ State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.
    """
    # <<< sv_power_flow
    # @generated
    def __init__(self, p=0.0, q=0.0, terminal=None, *args, **kw_args):
        """ Initialises a new 'SvPowerFlow' instance.

        @param p: The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
        @param q: The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
        @param terminal: The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
        """
        # The active power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.p should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
        self.p = p

        # The reactive power flow into the terminal.If the associated Terminal.connected status is 'false', the flow specified in the SvPowerFlow.q should be zero.   The power flow is into the Terminal of the ConductingEquipment. 
        self.q = q


        self._terminal = None
        self.terminal = terminal


        super(SvPowerFlow, self).__init__(*args, **kw_args)
    # >>> sv_power_flow

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal associated with the power flow state.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. 
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



# <<< state_variables
# @generated
# >>> state_variables
