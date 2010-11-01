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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

from entsoe.core import ConductingEquipment
from entsoe.core import IdentifiedObject
from entsoe.core import Curve
from entsoe.core import Equipment
from entsoe.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Wires"

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.
    """
    # <<< busbar_section
    # @generated
    def __init__(self, voltage_control_zone=None, *args, **kw_args):
        """ Initialises a new 'BusbarSection' instance.

        @param voltage_control_zone: A VoltageControlZone is controlled by a designated BusbarSection.
        """

        self._voltage_control_zone = None
        self.voltage_control_zone = voltage_control_zone


        super(BusbarSection, self).__init__(*args, **kw_args)
    # >>> busbar_section

    # <<< voltage_control_zone
    # @generated
    def get_voltage_control_zone(self):
        """ A VoltageControlZone is controlled by a designated BusbarSection.
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



class TapChanger(IdentifiedObject):
    """ Mechanism for changing transformer winding tap positions.
    """
    # <<< tap_changer
    # @generated
    def __init__(self, step_voltage_increment=0.0, neutral_u=0.0, low_step=0, neutral_step=0, high_step=0, sv_tap_step=None, regulating_control=None, *args, **kw_args):
        """ Initialises a new 'TapChanger' instance.

        @param step_voltage_increment: Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages 
        @param neutral_u: Voltage at which the winding operates at the neutral tap setting. 
        @param low_step: Lowest possible tap step position, retard from neutral 
        @param neutral_step: The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value.  
        @param high_step: Highest possible tap step position, advance from neutral 
        @param sv_tap_step: The tap step state associated with the tap changer.
        @param regulating_control:
        """
        # Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages 
        self.step_voltage_increment = step_voltage_increment

        # Voltage at which the winding operates at the neutral tap setting. 
        self.neutral_u = neutral_u

        # Lowest possible tap step position, retard from neutral 
        self.low_step = low_step

        # The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value.  
        self.neutral_step = neutral_step

        # Highest possible tap step position, advance from neutral 
        self.high_step = high_step


        self._sv_tap_step = None
        self.sv_tap_step = sv_tap_step

        self._regulating_control = None
        self.regulating_control = regulating_control


        super(TapChanger, self).__init__(*args, **kw_args)
    # >>> tap_changer

    # <<< sv_tap_step
    # @generated
    def get_sv_tap_step(self):
        """ The tap step state associated with the tap changer.
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



class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.
    """
    # <<< transformer_winding
    # @generated
    def __init__(self, x=0.0, b=0.0, connection_type='z', rated_s=0.0, x0=0.0, r=0.0, r0=0.0, b0=0.0, rated_u=0.0, g0=0.0, g=0.0, xground=0.0, winding_type='tertiary', rground=0.0, member_of_power_transformer=None, ratio_tap_changer=None, phase_tap_changer=None, *args, **kw_args):
        """ Initialises a new 'TransformerWinding' instance.

        @param x: Positive sequence series reactance of the winding. 
        @param b: Magnetizing branch susceptance (B mag). 
        @param connection_type: The type of connection of the winding. Values are: "z", "y", "d"
        @param rated_s: The normal apparent power rating for the winding 
        @param x0: Zero sequence series reactance of the winding.This is for Short Circuit only. 
        @param r: Positive sequence series resistance of the winding. 
        @param r0: Zero sequence series resistance of the winding.This is for Short Circuit only. 
        @param b0: Zero sequence magnetizing branch susceptance.This is for Short Circuit only. 
        @param rated_u: The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        @param g0: Zero sequence magnetizing branch conductance.This is for Short Circuit only. 
        @param g: Magnetizing branch conductance (G mag). 
        @param xground: Ground reactance path through connected grounding transformer.This is for Short Circuit only. 
        @param winding_type: The type of winding. Values are: "tertiary", "primary", "secondary"
        @param rground: Ground resistance path through connected grounding transformer.This is for Short Circuit only. 
        @param member_of_power_transformer: A transformer has windings
        @param ratio_tap_changer: The ratio tap changer associated with the transformer winding.
        @param phase_tap_changer: The phase tap changer associated with the transformer winding.
        """
        # Positive sequence series reactance of the winding. 
        self.x = x

        # Magnetizing branch susceptance (B mag). 
        self.b = b

        # The type of connection of the winding. Values are: "z", "y", "d"
        self.connection_type = connection_type

        # The normal apparent power rating for the winding 
        self.rated_s = rated_s

        # Zero sequence series reactance of the winding.This is for Short Circuit only. 
        self.x0 = x0

        # Positive sequence series resistance of the winding. 
        self.r = r

        # Zero sequence series resistance of the winding.This is for Short Circuit only. 
        self.r0 = r0

        # Zero sequence magnetizing branch susceptance.This is for Short Circuit only. 
        self.b0 = b0

        # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage. 
        self.rated_u = rated_u

        # Zero sequence magnetizing branch conductance.This is for Short Circuit only. 
        self.g0 = g0

        # Magnetizing branch conductance (G mag). 
        self.g = g

        # Ground reactance path through connected grounding transformer.This is for Short Circuit only. 
        self.xground = xground

        # The type of winding. Values are: "tertiary", "primary", "secondary"
        self.winding_type = winding_type

        # Ground resistance path through connected grounding transformer.This is for Short Circuit only. 
        self.rground = rground


        self._member_of_power_transformer = None
        self.member_of_power_transformer = member_of_power_transformer

        self._ratio_tap_changer = None
        self.ratio_tap_changer = ratio_tap_changer

        self._phase_tap_changer = None
        self.phase_tap_changer = phase_tap_changer


        super(TransformerWinding, self).__init__(*args, **kw_args)
    # >>> transformer_winding

    # <<< member_of_power_transformer
    # @generated
    def get_member_of_power_transformer(self):
        """ A transformer has windings
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
        """ The ratio tap changer associated with the transformer winding.
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
        """ The phase tap changer associated with the transformer winding.
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



class RegulatingControl(IdentifiedObject):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.
    """
    # <<< regulating_control
    # @generated
    def __init__(self, mode='reactive_power', discrete=False, target_value=0.0, target_range=0.0, terminal=None, regulating_cond_eq=None, tap_changer=None, *args, **kw_args):
        """ Initialises a new 'RegulatingControl' instance.

        @param mode: The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule. Values are: "reactive_power", "voltage", "active_power", "current_flow", "fixed", "admittance"
        @param discrete: The regulation is performed in a discrete mode. 
        @param target_value: The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute. 
        @param target_range: This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode. 
        @param terminal: The terminal associated with this regulating control.
        @param regulating_cond_eq: copy from reg cond eq
        @param tap_changer: copy from reg conduting eq
        """
        # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule. Values are: "reactive_power", "voltage", "active_power", "current_flow", "fixed", "admittance"
        self.mode = mode

        # The regulation is performed in a discrete mode. 
        self.discrete = discrete

        # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute. 
        self.target_value = target_value

        # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode. 
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


        super(RegulatingControl, self).__init__(*args, **kw_args)
    # >>> regulating_control

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminal associated with this regulating control.
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
        """ copy from reg cond eq
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
        """ copy from reg conduting eq
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



class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.
    """
    # <<< reactive_capability_curve
    # @generated
    def __init__(self, initially_used_by_synchronous_machine=None, *args, **kw_args):
        """ Initialises a new 'ReactiveCapabilityCurve' instance.

        @param initially_used_by_synchronous_machine: Synchronous machines using this curve as default.
        """

        self._initially_used_by_synchronous_machine = []
        if initially_used_by_synchronous_machine is not None:
            self.initially_used_by_synchronous_machine = initially_used_by_synchronous_machine
        else:
            self.initially_used_by_synchronous_machine = []


        super(ReactiveCapabilityCurve, self).__init__(*args, **kw_args)
    # >>> reactive_capability_curve

    # <<< initially_used_by_synchronous_machine
    # @generated
    def get_initially_used_by_synchronous_machine(self):
        """ Synchronous machines using this curve as default.
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



class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.
    """
    # <<< mutual_coupling
    # @generated
    def __init__(self, distance22=0.0, g0ch=0.0, distance21=0.0, r0=0.0, b0ch=0.0, x0=0.0, distance11=0.0, distance12=0.0, first_terminal=None, second_terminal=None, *args, **kw_args):
        """ Initialises a new 'MutualCoupling' instance.

        @param distance22: Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        @param g0ch: Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
        @param distance21: Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        @param r0: Zero sequence branch-to-branch mutual impedance coupling, resistance 
        @param b0ch: Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param x0: Zero sequence branch-to-branch mutual impedance coupling, reactance 
        @param distance11: Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        @param distance12: Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        @param first_terminal: The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
        @param second_terminal: The starting terminal for the calculation of distances along the second branch of the mutual coupling.
        """
        # Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance22 = distance22

        # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section. 
        self.g0ch = g0ch

        # Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance21 = distance21

        # Zero sequence branch-to-branch mutual impedance coupling, resistance 
        self.r0 = r0

        # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.b0ch = b0ch

        # Zero sequence branch-to-branch mutual impedance coupling, reactance 
        self.x0 = x0

        # Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance11 = distance11

        # Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number. 
        self.distance12 = distance12


        self._first_terminal = None
        self.first_terminal = first_terminal

        self._second_terminal = None
        self.second_terminal = second_terminal


        super(MutualCoupling, self).__init__(*args, **kw_args)
    # >>> mutual_coupling

    # <<< first_terminal
    # @generated
    def get_first_terminal(self):
        """ The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
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
        """ The starting terminal for the calculation of distances along the second branch of the mutual coupling.
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



class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """
    # <<< power_transformer
    # @generated
    def __init__(self, contains_transformer_windings=None, *args, **kw_args):
        """ Initialises a new 'PowerTransformer' instance.

        @param contains_transformer_windings: A transformer has windings
        """

        self._contains_transformer_windings = []
        if contains_transformer_windings is not None:
            self.contains_transformer_windings = contains_transformer_windings
        else:
            self.contains_transformer_windings = []


        super(PowerTransformer, self).__init__(*args, **kw_args)
    # >>> power_transformer

    # <<< contains_transformer_windings
    # @generated
    def get_contains_transformer_windings(self):
        """ A transformer has windings
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



class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system model
    """
    # <<< energy_consumer
    # @generated
    def __init__(self, load_response=None, *args, **kw_args):
        """ Initialises a new 'EnergyConsumer' instance.

        @param load_response: The load response characteristic of this load.
        """

        self._load_response = None
        self.load_response = load_response


        super(EnergyConsumer, self).__init__(*args, **kw_args)
    # >>> energy_consumer

    # <<< load_response
    # @generated
    def get_load_response(self):
        """ The load response characteristic of this load.
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



class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.
    """
    pass
    # <<< switch
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Switch' instance.

        """


        super(Switch, self).__init__(*args, **kw_args)
    # >>> switch



class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """
    # <<< regulating_cond_eq
    # @generated
    def __init__(self, regulating_control=None, *args, **kw_args):
        """ Initialises a new 'RegulatingCondEq' instance.

        @param regulating_control: copy from ...Regulating control scheme in which this equipment participates.
        """

        self._regulating_control = None
        self.regulating_control = regulating_control


        super(RegulatingCondEq, self).__init__(*args, **kw_args)
    # >>> regulating_cond_eq

    # <<< regulating_control
    # @generated
    def get_regulating_control(self):
        """ copy from ...Regulating control scheme in which this equipment participates.
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



class VoltageControlZone(IdentifiedObject):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """
    # <<< voltage_control_zone
    # @generated
    def __init__(self, busbar_section=None, *args, **kw_args):
        """ Initialises a new 'VoltageControlZone' instance.

        @param busbar_section: A VoltageControlZone is controlled by a designated BusbarSection.
        """

        self._busbar_section = None
        self.busbar_section = busbar_section


        super(VoltageControlZone, self).__init__(*args, **kw_args)
    # >>> voltage_control_zone

    # <<< busbar_section
    # @generated
    def get_busbar_section(self):
        """ A VoltageControlZone is controlled by a designated BusbarSection.
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



class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """
    pass
    # <<< line
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Line' instance.

        """


        super(Line, self).__init__(*args, **kw_args)
    # >>> line



class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """
    # <<< conductor
    # @generated
    def __init__(self, b0ch=0.0, bch=0.0, r0=0.0, x0=0.0, gch=0.0, x=0.0, length=0.0, r=0.0, g0ch=0.0, *args, **kw_args):
        """ Initialises a new 'Conductor' instance.

        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section.This is for Short Circuit only. 
        @param x0: Zero sequence series reactance of the entire line section.This is for Short Circuit only. 
        @param gch: Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        @param x: Positive sequence series reactance of the entire line section. 
        @param length: Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling. 
        @param r: Positive sequence series resistance of the entire line section. 
        @param g0ch: Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        """
        # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        self.b0ch = b0ch

        # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.bch = bch

        # Zero sequence series resistance of the entire line section.This is for Short Circuit only. 
        self.r0 = r0

        # Zero sequence series reactance of the entire line section.This is for Short Circuit only. 
        self.x0 = x0

        # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        self.gch = gch

        # Positive sequence series reactance of the entire line section. 
        self.x = x

        # Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling. 
        self.length = length

        # Positive sequence series resistance of the entire line section. 
        self.r = r

        # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only. 
        self.g0ch = g0ch



        super(Conductor, self).__init__(*args, **kw_args)
    # >>> conductor



class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.
    """
    pass
    # <<< acline_segment
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ACLineSegment' instance.

        """


        super(ACLineSegment, self).__init__(*args, **kw_args)
    # >>> acline_segment



class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """
    # <<< phase_tap_changer
    # @generated
    def __init__(self, x_step_min=0.0, x_step_max=0.0, step_phase_shift_increment=0.0, winding_connection_angle=0.0, phase_tap_changer_type='asymmetrical', voltage_step_increment_out_of_phase=0.0, transformer_winding=None, *args, **kw_args):
        """ Initialises a new 'PhaseTapChanger' instance.

        @param x_step_min: The reactance at the minimum tap step. 
        @param x_step_max: The reactance at the maximum tap step. 
        @param step_phase_shift_increment: Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
        @param winding_connection_angle: The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is Asymmetrical 
        @param phase_tap_changer_type: The type of phase shifter construction. Values are: "asymmetrical", "symmetrical"
        @param voltage_step_increment_out_of_phase: The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical. 
        @param transformer_winding: The transformer winding to which the phase tap changer belongs.
        """
        # The reactance at the minimum tap step. 
        self.x_step_min = x_step_min

        # The reactance at the maximum tap step. 
        self.x_step_max = x_step_max

        # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available. 
        self.step_phase_shift_increment = step_phase_shift_increment

        # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is Asymmetrical 
        self.winding_connection_angle = winding_connection_angle

        # The type of phase shifter construction. Values are: "asymmetrical", "symmetrical"
        self.phase_tap_changer_type = phase_tap_changer_type

        # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical. 
        self.voltage_step_increment_out_of_phase = voltage_step_increment_out_of_phase


        self._transformer_winding = None
        self.transformer_winding = transformer_winding


        super(PhaseTapChanger, self).__init__(*args, **kw_args)
    # >>> phase_tap_changer

    # <<< transformer_winding
    # @generated
    def get_transformer_winding(self):
        """ The transformer winding to which the phase tap changer belongs.
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



class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. 
    """
    # <<< synchronous_machine
    # @generated
    def __init__(self, x0=0.0, operating_mode='condenser', r0=0.0, q_percent=0.0, x2=0.0, type='condenser', r2=0.0, r=0.0, max_q=0.0, x=0.0, rated_s=0.0, min_q=0.0, initial_reactive_capability_curve=None, drives_hydro_pump=None, member_of_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'SynchronousMachine' instance.

        @param x0: Zero sequence reactance of the synchronous machine.This is for Short Circuit only. 
        @param operating_mode: Current mode of operation. Values are: "condenser", "generator"
        @param r0: Zero sequence resistance of the synchronous machine.This is for Short Circuit only. 
        @param q_percent: Percent of the coordinated reactive control that comes from this machine. 
        @param x2: Negative sequence reactance.This is for Short Circuit only. 
        @param type: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        @param r2: Negative sequence resistance.This is for Short Circuit only. 
        @param r: Positive sequence resistance of the synchronous machine. 
        @param max_q: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param x: Positive sequence reactance of the synchronous machine. 
        @param rated_s: Nameplate apparent power rating for the unit 
        @param min_q: Minimum reactive power limit for the unit. 
        @param initial_reactive_capability_curve: The default ReactiveCapabilityCurve for use by a SynchronousMachine
        @param drives_hydro_pump: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param member_of_generating_unit: A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
        """
        # Zero sequence reactance of the synchronous machine.This is for Short Circuit only. 
        self.x0 = x0

        # Current mode of operation. Values are: "condenser", "generator"
        self.operating_mode = operating_mode

        # Zero sequence resistance of the synchronous machine.This is for Short Circuit only. 
        self.r0 = r0

        # Percent of the coordinated reactive control that comes from this machine. 
        self.q_percent = q_percent

        # Negative sequence reactance.This is for Short Circuit only. 
        self.x2 = x2

        # Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = type

        # Negative sequence resistance.This is for Short Circuit only. 
        self.r2 = r2

        # Positive sequence resistance of the synchronous machine. 
        self.r = r

        # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        self.max_q = max_q

        # Positive sequence reactance of the synchronous machine. 
        self.x = x

        # Nameplate apparent power rating for the unit 
        self.rated_s = rated_s

        # Minimum reactive power limit for the unit. 
        self.min_q = min_q


        self._initial_reactive_capability_curve = None
        self.initial_reactive_capability_curve = initial_reactive_capability_curve

        self._drives_hydro_pump = None
        self.drives_hydro_pump = drives_hydro_pump

        self._member_of_generating_unit = None
        self.member_of_generating_unit = member_of_generating_unit


        super(SynchronousMachine, self).__init__(*args, **kw_args)
    # >>> synchronous_machine

    # <<< initial_reactive_capability_curve
    # @generated
    def get_initial_reactive_capability_curve(self):
        """ The default ReactiveCapabilityCurve for use by a SynchronousMachine
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
        """ The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
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
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
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



class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """
    # <<< ratio_tap_changer
    # @generated
    def __init__(self, transformer_winding=None, *args, **kw_args):
        """ Initialises a new 'RatioTapChanger' instance.

        @param transformer_winding: The transformer winding to which the ratio tap changer belongs.
        """

        self._transformer_winding = None
        self.transformer_winding = transformer_winding


        super(RatioTapChanger, self).__init__(*args, **kw_args)
    # >>> ratio_tap_changer

    # <<< transformer_winding
    # @generated
    def get_transformer_winding(self):
        """ The transformer winding to which the ratio tap changer belongs.
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



class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.
    """
    # <<< shunt_compensator
    # @generated
    def __init__(self, b0_per_section=0.0, maximum_sections=0, g0_per_section=0.0, b_per_section=0.0, g_per_section=0.0, sv_shunt_compensator_sections=None, *args, **kw_args):
        """ Initialises a new 'ShuntCompensator' instance.

        @param b0_per_section: Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only. 
        @param maximum_sections: For a capacitor bank, the maximum number of sections that may be switched in. 
        @param g0_per_section: Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only. 
        @param b_per_section: Positive sequence shunt (charging) susceptance per section 
        @param g_per_section: Positive sequence shunt (charging) conductance per section 
        @param sv_shunt_compensator_sections: The state for the number of shunt compensator sections in service.
        """
        # Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only. 
        self.b0_per_section = b0_per_section

        # For a capacitor bank, the maximum number of sections that may be switched in. 
        self.maximum_sections = maximum_sections

        # Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only. 
        self.g0_per_section = g0_per_section

        # Positive sequence shunt (charging) susceptance per section 
        self.b_per_section = b_per_section

        # Positive sequence shunt (charging) conductance per section 
        self.g_per_section = g_per_section


        self._sv_shunt_compensator_sections = None
        self.sv_shunt_compensator_sections = sv_shunt_compensator_sections


        super(ShuntCompensator, self).__init__(*args, **kw_args)
    # >>> shunt_compensator

    # <<< sv_shunt_compensator_sections
    # @generated
    def get_sv_shunt_compensator_sections(self):
        """ The state for the number of shunt compensator sections in service.
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



# <<< wires
# @generated
# >>> wires
