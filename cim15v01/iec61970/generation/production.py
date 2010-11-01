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

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

from cim15v01.iec61970.core import Curve
from cim15v01.iec61970.core import Equipment
from cim15v01.iec61970.core import PowerSystemResource
from cim15v01.iec61970.core import RegularIntervalSchedule
from cim15v01.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimProduction"

ns_uri = "http://iec.ch/TC57/CIM-generic#Production"

class PenstockLossCurve(Curve):
    """ Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.
    """
    # <<< penstock_loss_curve
    # @generated
    def __init__(self, hydro_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'PenstockLossCurve' instance.

        @param hydro_generating_unit: A hydro generating unit has a penstock loss curve
        """

        self._hydro_generating_unit = None
        self.hydro_generating_unit = hydro_generating_unit


        super(PenstockLossCurve, self).__init__(*args, **kw_args)
    # >>> penstock_loss_curve

    # <<< hydro_generating_unit
    # @generated
    def get_hydro_generating_unit(self):
        """ A hydro generating unit has a penstock loss curve
        """
        return self._hydro_generating_unit

    def set_hydro_generating_unit(self, value):
        if self._hydro_generating_unit is not None:
            self._hydro_generating_unit._penstock_loss_curve = None

        self._hydro_generating_unit = value
        if self._hydro_generating_unit is not None:
            self._hydro_generating_unit._penstock_loss_curve = self

    hydro_generating_unit = property(get_hydro_generating_unit, set_hydro_generating_unit)
    # >>> hydro_generating_unit



class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """
    # <<< generating_unit
    # @generated
    def __init__(self, gen_operating_mode='off', gen_control_mode='setpoint', gen_control_source='on_agc', variable_cost=0.0, short_pf=0.0, rated_gross_min_p=0.0, max_operating_p=0.0, maximum_allowable_spinning_reserve=0.0, startup_time=0.0, long_pf=0.0, initial_p=0.0, lower_ramp_rate=0.0, minimum_off_time=0.0, spin_reserve_ramp=0.0, fuel_priority=0, rated_gross_max_p=0.0, model_detail=0, efficiency=0.0, raise_ramp_rate=0.0, tie_line_pf=0.0, penalty_factor=0.0, min_operating_p=0.0, auto_cntrl_margin_p=0.0, min_economic_p=0.0, control_deadband=0.0, disp_reserve_flag=False, normal_pf=0.0, high_control_limit=0.0, alloc_spin_res_p=0.0, low_control_limit=0.0, governor_mpl=0.0, control_pulse_low=0.0, fast_start_flag=False, nominal_p=0.0, base_p=0.0, rated_net_max_p=0.0, max_economic_p=0.0, control_response_rate=0.0, step_change=0.0, energy_min_p=0.0, startup_cost=0.0, governor_scd=0.0, control_pulse_high=0.0, operated_by_generation_provider=None, control_area_generating_unit=None, gen_unit_op_cost_curves=None, sub_control_area=None, registered_generator=None, synchronous_machines=None, gen_unit_op_schedule=None, gross_to_net_active_power_curves=None, *args, **kw_args):
        """ Initialises a new 'GeneratingUnit' instance.

        @param gen_operating_mode: Operating mode for secondary control. Values are: "off", "agc", "manual", "mrn", "lfc", "edc", "fixed", "reg"
        @param gen_control_mode: The unit control mode. Values are: "setpoint", "pulse"
        @param gen_control_source: The source of controls for a generating unit. Values are: "on_agc", "plant_control", "unavailable", "off_agc"
        @param variable_cost: The variable cost component of production per unit of ActivePower. 
        @param short_pf: Generating unit economic participation factor 
        @param rated_gross_min_p: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        @param max_operating_p: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param maximum_allowable_spinning_reserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param startup_time: Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        @param long_pf: Generating unit economic participation factor 
        @param initial_p: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param lower_ramp_rate: 
        @param minimum_off_time: Minimum time interval between unit shutdown and startup 
        @param spin_reserve_ramp: 
        @param fuel_priority: 
        @param rated_gross_max_p: The unit's gross rated maximum capacity (Book Value). 
        @param model_detail: Detail level of the generator model data 
        @param efficiency: The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy. 
        @param raise_ramp_rate: 
        @param tie_line_pf: Generating unit economic participation factor 
        @param penalty_factor: Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1). 
        @param min_operating_p: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param auto_cntrl_margin_p: The planned unused capacity which can be used to support automatic control overruns. 
        @param min_economic_p: Low economic active power limit that must be greater than or equal to the minimum operating active power limit 
        @param control_deadband: Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit. 
        @param disp_reserve_flag: 
        @param normal_pf: Generating unit economic participation factor 
        @param high_control_limit: High limit for secondary (AGC) control 
        @param alloc_spin_res_p: The planned unused capacity (spinning reserve) which can be used to support emergency load 
        @param low_control_limit: Low limit for secondary (AGC) control 
        @param governor_mpl: Governor Motor Position Limit 
        @param control_pulse_low: Pulse low limit which is the smallest control pulse that the unit can respond to 
        @param fast_start_flag: 
        @param nominal_p: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        @param base_p: For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        @param rated_net_max_p: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param max_economic_p: Maximum high economic active power limit, that should not exceed the maximum operating active power limit 
        @param control_response_rate: Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit. 
        @param step_change: 
        @param energy_min_p: 
        @param startup_cost: The initial startup cost incurred for each start of the GeneratingUnit. 
        @param governor_scd: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        @param control_pulse_high: Pulse high limit which is the largest control pulse that the unit can respond to 
        @param operated_by_generation_provider: A GenerationProvider operates one or more GeneratingUnits.
        @param control_area_generating_unit: ControlArea specifications for this generating unit.
        @param gen_unit_op_cost_curves: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        @param sub_control_area: A GeneratingUnit injects energy into a SubControlArea.
        @param registered_generator:
        @param synchronous_machines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param gen_unit_op_schedule: A generating unit may have an operating schedule, indicating the planned operation of the unit
        @param gross_to_net_active_power_curves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        # Operating mode for secondary control. Values are: "off", "agc", "manual", "mrn", "lfc", "edc", "fixed", "reg"
        self.gen_operating_mode = gen_operating_mode

        # The unit control mode. Values are: "setpoint", "pulse"
        self.gen_control_mode = gen_control_mode

        # The source of controls for a generating unit. Values are: "on_agc", "plant_control", "unavailable", "off_agc"
        self.gen_control_source = gen_control_source

        # The variable cost component of production per unit of ActivePower. 
        self.variable_cost = variable_cost

        # Generating unit economic participation factor 
        self.short_pf = short_pf

        # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        self.rated_gross_min_p = rated_gross_min_p

        # This is the maximum operating active power limit the dispatcher can enter for this unit 
        self.max_operating_p = max_operating_p

        # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        self.maximum_allowable_spinning_reserve = maximum_allowable_spinning_reserve

        # Time it takes to get the unit on-line, from the time that the prime mover mechanical power is applied 
        self.startup_time = startup_time

        # Generating unit economic participation factor 
        self.long_pf = long_pf

        # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        self.initial_p = initial_p

 
        self.lower_ramp_rate = lower_ramp_rate

        # Minimum time interval between unit shutdown and startup 
        self.minimum_off_time = minimum_off_time

 
        self.spin_reserve_ramp = spin_reserve_ramp

 
        self.fuel_priority = fuel_priority

        # The unit's gross rated maximum capacity (Book Value). 
        self.rated_gross_max_p = rated_gross_max_p

        # Detail level of the generator model data 
        self.model_detail = model_detail

        # The efficiency of the unit in converting mechanical energy, from the prime mover, into electrical energy. 
        self.efficiency = efficiency

 
        self.raise_ramp_rate = raise_ramp_rate

        # Generating unit economic participation factor 
        self.tie_line_pf = tie_line_pf

        # Defined as: 1 / ( 1 - Incremental Transmission Loss); with the Incremental Transmission Loss expressed as a plus or minus value. The typical range of penalty factors is (0.9 to 1.1). 
        self.penalty_factor = penalty_factor

        # This is the minimum operating active power limit the dispatcher can enter for this unit. 
        self.min_operating_p = min_operating_p

        # The planned unused capacity which can be used to support automatic control overruns. 
        self.auto_cntrl_margin_p = auto_cntrl_margin_p

        # Low economic active power limit that must be greater than or equal to the minimum operating active power limit 
        self.min_economic_p = min_economic_p

        # Unit control error deadband. When a unit's desired active power change is less than this deadband, then no control pulses will be sent to the unit. 
        self.control_deadband = control_deadband

 
        self.disp_reserve_flag = disp_reserve_flag

        # Generating unit economic participation factor 
        self.normal_pf = normal_pf

        # High limit for secondary (AGC) control 
        self.high_control_limit = high_control_limit

        # The planned unused capacity (spinning reserve) which can be used to support emergency load 
        self.alloc_spin_res_p = alloc_spin_res_p

        # Low limit for secondary (AGC) control 
        self.low_control_limit = low_control_limit

        # Governor Motor Position Limit 
        self.governor_mpl = governor_mpl

        # Pulse low limit which is the smallest control pulse that the unit can respond to 
        self.control_pulse_low = control_pulse_low

 
        self.fast_start_flag = fast_start_flag

        # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        self.nominal_p = nominal_p

        # For dispatchable units, this value represents the economic active power basepoint, for units that are not dispatchable, this value represents the fixed generation value. The value must be between the operating low and high limits. 
        self.base_p = base_p

        # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        self.rated_net_max_p = rated_net_max_p

        # Maximum high economic active power limit, that should not exceed the maximum operating active power limit 
        self.max_economic_p = max_economic_p

        # Unit response rate which specifies the active power change for a control pulse of one second in the most responsive loading level of the unit. 
        self.control_response_rate = control_response_rate

 
        self.step_change = step_change

 
        self.energy_min_p = energy_min_p

        # The initial startup cost incurred for each start of the GeneratingUnit. 
        self.startup_cost = startup_cost

        # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency. 
        self.governor_scd = governor_scd

        # Pulse high limit which is the largest control pulse that the unit can respond to 
        self.control_pulse_high = control_pulse_high


        self._operated_by_generation_provider = None
        self.operated_by_generation_provider = operated_by_generation_provider

        self._control_area_generating_unit = []
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
        else:
            self.control_area_generating_unit = []

        self._gen_unit_op_cost_curves = []
        if gen_unit_op_cost_curves is not None:
            self.gen_unit_op_cost_curves = gen_unit_op_cost_curves
        else:
            self.gen_unit_op_cost_curves = []

        self._sub_control_area = None
        self.sub_control_area = sub_control_area

        self._registered_generator = None
        self.registered_generator = registered_generator

        self._synchronous_machines = []
        if synchronous_machines is not None:
            self.synchronous_machines = synchronous_machines
        else:
            self.synchronous_machines = []

        self._gen_unit_op_schedule = None
        self.gen_unit_op_schedule = gen_unit_op_schedule

        self._gross_to_net_active_power_curves = []
        if gross_to_net_active_power_curves is not None:
            self.gross_to_net_active_power_curves = gross_to_net_active_power_curves
        else:
            self.gross_to_net_active_power_curves = []


        super(GeneratingUnit, self).__init__(*args, **kw_args)
    # >>> generating_unit

    # <<< operated_by_generation_provider
    # @generated
    def get_operated_by_generation_provider(self):
        """ A GenerationProvider operates one or more GeneratingUnits.
        """
        return self._operated_by_generation_provider

    def set_operated_by_generation_provider(self, value):
        if self._operated_by_generation_provider is not None:
            filtered = [x for x in self.operated_by_generation_provider.generating_units if x != self]
            self._operated_by_generation_provider._generating_units = filtered

        self._operated_by_generation_provider = value
        if self._operated_by_generation_provider is not None:
            self._operated_by_generation_provider._generating_units.append(self)

    operated_by_generation_provider = property(get_operated_by_generation_provider, set_operated_by_generation_provider)
    # >>> operated_by_generation_provider

    # <<< control_area_generating_unit
    # @generated
    def get_control_area_generating_unit(self):
        """ ControlArea specifications for this generating unit.
        """
        return self._control_area_generating_unit

    def set_control_area_generating_unit(self, value):
        for x in self._control_area_generating_unit:
            x._generating_unit = None
        for y in value:
            y._generating_unit = self
        self._control_area_generating_unit = value

    control_area_generating_unit = property(get_control_area_generating_unit, set_control_area_generating_unit)

    def add_control_area_generating_unit(self, *control_area_generating_unit):
        for obj in control_area_generating_unit:
            obj._generating_unit = self
            self._control_area_generating_unit.append(obj)

    def remove_control_area_generating_unit(self, *control_area_generating_unit):
        for obj in control_area_generating_unit:
            obj._generating_unit = None
            self._control_area_generating_unit.remove(obj)
    # >>> control_area_generating_unit

    # <<< gen_unit_op_cost_curves
    # @generated
    def get_gen_unit_op_cost_curves(self):
        """ A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        return self._gen_unit_op_cost_curves

    def set_gen_unit_op_cost_curves(self, value):
        for x in self._gen_unit_op_cost_curves:
            x._generating_unit = None
        for y in value:
            y._generating_unit = self
        self._gen_unit_op_cost_curves = value

    gen_unit_op_cost_curves = property(get_gen_unit_op_cost_curves, set_gen_unit_op_cost_curves)

    def add_gen_unit_op_cost_curves(self, *gen_unit_op_cost_curves):
        for obj in gen_unit_op_cost_curves:
            obj._generating_unit = self
            self._gen_unit_op_cost_curves.append(obj)

    def remove_gen_unit_op_cost_curves(self, *gen_unit_op_cost_curves):
        for obj in gen_unit_op_cost_curves:
            obj._generating_unit = None
            self._gen_unit_op_cost_curves.remove(obj)
    # >>> gen_unit_op_cost_curves

    # <<< sub_control_area
    # @generated
    def get_sub_control_area(self):
        """ A GeneratingUnit injects energy into a SubControlArea.
        """
        return self._sub_control_area

    def set_sub_control_area(self, value):
        if self._sub_control_area is not None:
            filtered = [x for x in self.sub_control_area.generating_units if x != self]
            self._sub_control_area._generating_units = filtered

        self._sub_control_area = value
        if self._sub_control_area is not None:
            self._sub_control_area._generating_units.append(self)

    sub_control_area = property(get_sub_control_area, set_sub_control_area)
    # >>> sub_control_area

    # <<< registered_generator
    # @generated
    def get_registered_generator(self):
        """ 
        """
        return self._registered_generator

    def set_registered_generator(self, value):
        if self._registered_generator is not None:
            self._registered_generator._generating_unit = None

        self._registered_generator = value
        if self._registered_generator is not None:
            self._registered_generator._generating_unit = self

    registered_generator = property(get_registered_generator, set_registered_generator)
    # >>> registered_generator

    # <<< synchronous_machines
    # @generated
    def get_synchronous_machines(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._synchronous_machines

    def set_synchronous_machines(self, value):
        for x in self._synchronous_machines:
            x._generating_unit = None
        for y in value:
            y._generating_unit = self
        self._synchronous_machines = value

    synchronous_machines = property(get_synchronous_machines, set_synchronous_machines)

    def add_synchronous_machines(self, *synchronous_machines):
        for obj in synchronous_machines:
            obj._generating_unit = self
            self._synchronous_machines.append(obj)

    def remove_synchronous_machines(self, *synchronous_machines):
        for obj in synchronous_machines:
            obj._generating_unit = None
            self._synchronous_machines.remove(obj)
    # >>> synchronous_machines

    # <<< gen_unit_op_schedule
    # @generated
    def get_gen_unit_op_schedule(self):
        """ A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        return self._gen_unit_op_schedule

    def set_gen_unit_op_schedule(self, value):
        if self._gen_unit_op_schedule is not None:
            self._gen_unit_op_schedule._generating_unit = None

        self._gen_unit_op_schedule = value
        if self._gen_unit_op_schedule is not None:
            self._gen_unit_op_schedule._generating_unit = self

    gen_unit_op_schedule = property(get_gen_unit_op_schedule, set_gen_unit_op_schedule)
    # >>> gen_unit_op_schedule

    # <<< gross_to_net_active_power_curves
    # @generated
    def get_gross_to_net_active_power_curves(self):
        """ A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        return self._gross_to_net_active_power_curves

    def set_gross_to_net_active_power_curves(self, value):
        for x in self._gross_to_net_active_power_curves:
            x._generating_unit = None
        for y in value:
            y._generating_unit = self
        self._gross_to_net_active_power_curves = value

    gross_to_net_active_power_curves = property(get_gross_to_net_active_power_curves, set_gross_to_net_active_power_curves)

    def add_gross_to_net_active_power_curves(self, *gross_to_net_active_power_curves):
        for obj in gross_to_net_active_power_curves:
            obj._generating_unit = self
            self._gross_to_net_active_power_curves.append(obj)

    def remove_gross_to_net_active_power_curves(self, *gross_to_net_active_power_curves):
        for obj in gross_to_net_active_power_curves:
            obj._generating_unit = None
            self._gross_to_net_active_power_curves.remove(obj)
    # >>> gross_to_net_active_power_curves



class IncrementalHeatRateCurve(Curve):
    """ Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.
    """
    # <<< incremental_heat_rate_curve
    # @generated
    def __init__(self, is_net_gross_p=False, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'IncrementalHeatRateCurve' instance.

        @param is_net_gross_p: Flag is set to true when output is expressed in net active power 
        @param thermal_generating_unit: A thermal generating unit may have an incremental heat rate curve
        """
        # Flag is set to true when output is expressed in net active power 
        self.is_net_gross_p = is_net_gross_p


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(IncrementalHeatRateCurve, self).__init__(*args, **kw_args)
    # >>> incremental_heat_rate_curve

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have an incremental heat rate curve
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._incremental_heat_rate_curve = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._incremental_heat_rate_curve = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class HeatInputCurve(Curve):
    """ Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.
    """
    # <<< heat_input_curve
    # @generated
    def __init__(self, heat_input_eff=0.0, aux_power_offset=0.0, heat_input_offset=0.0, is_net_gross_p=False, aux_power_mult=0.0, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'HeatInputCurve' instance.

        @param heat_input_eff: Heat input - efficiency multiplier adjustment factor. 
        @param aux_power_offset: Power output - auxiliary power offset adjustment factor 
        @param heat_input_offset: Heat input - offset adjustment factor. 
        @param is_net_gross_p: Flag is set to true when output is expressed in net active power 
        @param aux_power_mult: Power output - auxiliary power multiplier adjustment factor. 
        @param thermal_generating_unit: A thermal generating unit may have a heat input curve
        """
        # Heat input - efficiency multiplier adjustment factor. 
        self.heat_input_eff = heat_input_eff

        # Power output - auxiliary power offset adjustment factor 
        self.aux_power_offset = aux_power_offset

        # Heat input - offset adjustment factor. 
        self.heat_input_offset = heat_input_offset

        # Flag is set to true when output is expressed in net active power 
        self.is_net_gross_p = is_net_gross_p

        # Power output - auxiliary power multiplier adjustment factor. 
        self.aux_power_mult = aux_power_mult


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(HeatInputCurve, self).__init__(*args, **kw_args)
    # >>> heat_input_curve

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have a heat input curve
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._heat_input_curve = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._heat_input_curve = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class Reservoir(PowerSystemResource):
    """ A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.
    """
    # <<< reservoir
    # @generated
    def __init__(self, spill_way_gate_type='', spillway_crest_length=0.0, active_storage_capacity=0.0, gross_capacity=0.0, energy_storage_rating=0.0, full_supply_level=0.0, spillway_capacity=0.0, spill_travel_delay=0.0, river_outlet_works='', normal_min_operate_level=0.0, spillway_crest_level=0.0, inflow_forecasts=None, spills_into_reservoirs=None, spills_from_reservoir=None, upstream_from_hydro_power_plants=None, level_vs_volume_curves=None, target_level_schedule=None, hydro_power_plants=None, *args, **kw_args):
        """ Initialises a new 'Reservoir' instance.

        @param spill_way_gate_type: Type of spillway gate, including parameters 
        @param spillway_crest_length: The length of the spillway crest 
        @param active_storage_capacity: Storage volume between the full supply level and the normal minimum operating level 
        @param gross_capacity: Total capacity of reservoir 
        @param energy_storage_rating: The reservoir's energy storage rating in energy for given head conditions 
        @param full_supply_level: Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates. 
        @param spillway_capacity: The flow capacity of the spillway in cubic meters per second 
        @param spill_travel_delay: The spillway water travel delay to the next downstream reservoir 
        @param river_outlet_works: River outlet works for riparian right releases or other purposes 
        @param normal_min_operate_level: Normal minimum operating level below which the penstocks will draw air 
        @param spillway_crest_level: Spillway crest level above which water will spill 
        @param inflow_forecasts: A reservoir may have a 'natural' inflow forecast.
        @param spills_into_reservoirs: A reservoir may spill into a downstream reservoir
        @param spills_from_reservoir: A reservoir may spill into a downstream reservoir
        @param upstream_from_hydro_power_plants: Generators are supplied water from or pumps discharge water to an upstream reservoir
        @param level_vs_volume_curves: A reservoir may have a level versus volume relationship.
        @param target_level_schedule: A reservoir may have a water level target schedule.
        @param hydro_power_plants: Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        # Type of spillway gate, including parameters 
        self.spill_way_gate_type = spill_way_gate_type

        # The length of the spillway crest 
        self.spillway_crest_length = spillway_crest_length

        # Storage volume between the full supply level and the normal minimum operating level 
        self.active_storage_capacity = active_storage_capacity

        # Total capacity of reservoir 
        self.gross_capacity = gross_capacity

        # The reservoir's energy storage rating in energy for given head conditions 
        self.energy_storage_rating = energy_storage_rating

        # Full supply level, above which water will spill. This can be the spillway crest level or the top of closed gates. 
        self.full_supply_level = full_supply_level

        # The flow capacity of the spillway in cubic meters per second 
        self.spillway_capacity = spillway_capacity

        # The spillway water travel delay to the next downstream reservoir 
        self.spill_travel_delay = spill_travel_delay

        # River outlet works for riparian right releases or other purposes 
        self.river_outlet_works = river_outlet_works

        # Normal minimum operating level below which the penstocks will draw air 
        self.normal_min_operate_level = normal_min_operate_level

        # Spillway crest level above which water will spill 
        self.spillway_crest_level = spillway_crest_level


        self._inflow_forecasts = []
        if inflow_forecasts is not None:
            self.inflow_forecasts = inflow_forecasts
        else:
            self.inflow_forecasts = []

        self._spills_into_reservoirs = []
        if spills_into_reservoirs is not None:
            self.spills_into_reservoirs = spills_into_reservoirs
        else:
            self.spills_into_reservoirs = []

        self._spills_from_reservoir = None
        self.spills_from_reservoir = spills_from_reservoir

        self._upstream_from_hydro_power_plants = []
        if upstream_from_hydro_power_plants is not None:
            self.upstream_from_hydro_power_plants = upstream_from_hydro_power_plants
        else:
            self.upstream_from_hydro_power_plants = []

        self._level_vs_volume_curves = []
        if level_vs_volume_curves is not None:
            self.level_vs_volume_curves = level_vs_volume_curves
        else:
            self.level_vs_volume_curves = []

        self._target_level_schedule = None
        self.target_level_schedule = target_level_schedule

        self._hydro_power_plants = []
        if hydro_power_plants is not None:
            self.hydro_power_plants = hydro_power_plants
        else:
            self.hydro_power_plants = []


        super(Reservoir, self).__init__(*args, **kw_args)
    # >>> reservoir

    # <<< inflow_forecasts
    # @generated
    def get_inflow_forecasts(self):
        """ A reservoir may have a 'natural' inflow forecast.
        """
        return self._inflow_forecasts

    def set_inflow_forecasts(self, value):
        for x in self._inflow_forecasts:
            x._reservoir = None
        for y in value:
            y._reservoir = self
        self._inflow_forecasts = value

    inflow_forecasts = property(get_inflow_forecasts, set_inflow_forecasts)

    def add_inflow_forecasts(self, *inflow_forecasts):
        for obj in inflow_forecasts:
            obj._reservoir = self
            self._inflow_forecasts.append(obj)

    def remove_inflow_forecasts(self, *inflow_forecasts):
        for obj in inflow_forecasts:
            obj._reservoir = None
            self._inflow_forecasts.remove(obj)
    # >>> inflow_forecasts

    # <<< spills_into_reservoirs
    # @generated
    def get_spills_into_reservoirs(self):
        """ A reservoir may spill into a downstream reservoir
        """
        return self._spills_into_reservoirs

    def set_spills_into_reservoirs(self, value):
        for x in self._spills_into_reservoirs:
            x._spills_from_reservoir = None
        for y in value:
            y._spills_from_reservoir = self
        self._spills_into_reservoirs = value

    spills_into_reservoirs = property(get_spills_into_reservoirs, set_spills_into_reservoirs)

    def add_spills_into_reservoirs(self, *spills_into_reservoirs):
        for obj in spills_into_reservoirs:
            obj._spills_from_reservoir = self
            self._spills_into_reservoirs.append(obj)

    def remove_spills_into_reservoirs(self, *spills_into_reservoirs):
        for obj in spills_into_reservoirs:
            obj._spills_from_reservoir = None
            self._spills_into_reservoirs.remove(obj)
    # >>> spills_into_reservoirs

    # <<< spills_from_reservoir
    # @generated
    def get_spills_from_reservoir(self):
        """ A reservoir may spill into a downstream reservoir
        """
        return self._spills_from_reservoir

    def set_spills_from_reservoir(self, value):
        if self._spills_from_reservoir is not None:
            filtered = [x for x in self.spills_from_reservoir.spills_into_reservoirs if x != self]
            self._spills_from_reservoir._spills_into_reservoirs = filtered

        self._spills_from_reservoir = value
        if self._spills_from_reservoir is not None:
            self._spills_from_reservoir._spills_into_reservoirs.append(self)

    spills_from_reservoir = property(get_spills_from_reservoir, set_spills_from_reservoir)
    # >>> spills_from_reservoir

    # <<< upstream_from_hydro_power_plants
    # @generated
    def get_upstream_from_hydro_power_plants(self):
        """ Generators are supplied water from or pumps discharge water to an upstream reservoir
        """
        return self._upstream_from_hydro_power_plants

    def set_upstream_from_hydro_power_plants(self, value):
        for x in self._upstream_from_hydro_power_plants:
            x._gen_source_pump_discharge_reservoir = None
        for y in value:
            y._gen_source_pump_discharge_reservoir = self
        self._upstream_from_hydro_power_plants = value

    upstream_from_hydro_power_plants = property(get_upstream_from_hydro_power_plants, set_upstream_from_hydro_power_plants)

    def add_upstream_from_hydro_power_plants(self, *upstream_from_hydro_power_plants):
        for obj in upstream_from_hydro_power_plants:
            obj._gen_source_pump_discharge_reservoir = self
            self._upstream_from_hydro_power_plants.append(obj)

    def remove_upstream_from_hydro_power_plants(self, *upstream_from_hydro_power_plants):
        for obj in upstream_from_hydro_power_plants:
            obj._gen_source_pump_discharge_reservoir = None
            self._upstream_from_hydro_power_plants.remove(obj)
    # >>> upstream_from_hydro_power_plants

    # <<< level_vs_volume_curves
    # @generated
    def get_level_vs_volume_curves(self):
        """ A reservoir may have a level versus volume relationship.
        """
        return self._level_vs_volume_curves

    def set_level_vs_volume_curves(self, value):
        for x in self._level_vs_volume_curves:
            x._reservoir = None
        for y in value:
            y._reservoir = self
        self._level_vs_volume_curves = value

    level_vs_volume_curves = property(get_level_vs_volume_curves, set_level_vs_volume_curves)

    def add_level_vs_volume_curves(self, *level_vs_volume_curves):
        for obj in level_vs_volume_curves:
            obj._reservoir = self
            self._level_vs_volume_curves.append(obj)

    def remove_level_vs_volume_curves(self, *level_vs_volume_curves):
        for obj in level_vs_volume_curves:
            obj._reservoir = None
            self._level_vs_volume_curves.remove(obj)
    # >>> level_vs_volume_curves

    # <<< target_level_schedule
    # @generated
    def get_target_level_schedule(self):
        """ A reservoir may have a water level target schedule.
        """
        return self._target_level_schedule

    def set_target_level_schedule(self, value):
        if self._target_level_schedule is not None:
            self._target_level_schedule._reservoir = None

        self._target_level_schedule = value
        if self._target_level_schedule is not None:
            self._target_level_schedule._reservoir = self

    target_level_schedule = property(get_target_level_schedule, set_target_level_schedule)
    # >>> target_level_schedule

    # <<< hydro_power_plants
    # @generated
    def get_hydro_power_plants(self):
        """ Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        return self._hydro_power_plants

    def set_hydro_power_plants(self, value):
        for x in self._hydro_power_plants:
            x._reservoir = None
        for y in value:
            y._reservoir = self
        self._hydro_power_plants = value

    hydro_power_plants = property(get_hydro_power_plants, set_hydro_power_plants)

    def add_hydro_power_plants(self, *hydro_power_plants):
        for obj in hydro_power_plants:
            obj._reservoir = self
            self._hydro_power_plants.append(obj)

    def remove_hydro_power_plants(self, *hydro_power_plants):
        for obj in hydro_power_plants:
            obj._reservoir = None
            self._hydro_power_plants.remove(obj)
    # >>> hydro_power_plants



class GenUnitOpCostCurve(Curve):
    """ Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.
    """
    # <<< gen_unit_op_cost_curve
    # @generated
    def __init__(self, is_net_gross_p=False, generating_unit=None, *args, **kw_args):
        """ Initialises a new 'GenUnitOpCostCurve' instance.

        @param is_net_gross_p: Flag is set to true when output is expressed in net active power 
        @param generating_unit: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        # Flag is set to true when output is expressed in net active power 
        self.is_net_gross_p = is_net_gross_p


        self._generating_unit = None
        self.generating_unit = generating_unit


        super(GenUnitOpCostCurve, self).__init__(*args, **kw_args)
    # >>> gen_unit_op_cost_curve

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.gen_unit_op_cost_curves if x != self]
            self._generating_unit._gen_unit_op_cost_curves = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._gen_unit_op_cost_curves.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit



class StartMainFuelCurve(Curve):
    """ The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """
    # <<< start_main_fuel_curve
    # @generated
    def __init__(self, main_fuel_type='gas', startup_model=None, *args, **kw_args):
        """ Initialises a new 'StartMainFuelCurve' instance.

        @param main_fuel_type: Type of main fuel Values are: "gas", "oil", "coal", "lignite"
        @param startup_model: The unit's startup model may have a startup main fuel curve
        """
        # Type of main fuel Values are: "gas", "oil", "coal", "lignite"
        self.main_fuel_type = main_fuel_type


        self._startup_model = None
        self.startup_model = startup_model


        super(StartMainFuelCurve, self).__init__(*args, **kw_args)
    # >>> start_main_fuel_curve

    # <<< startup_model
    # @generated
    def get_startup_model(self):
        """ The unit's startup model may have a startup main fuel curve
        """
        return self._startup_model

    def set_startup_model(self, value):
        if self._startup_model is not None:
            self._startup_model._start_main_fuel_curve = None

        self._startup_model = value
        if self._startup_model is not None:
            self._startup_model._start_main_fuel_curve = self

    startup_model = property(get_startup_model, set_startup_model)
    # >>> startup_model



class CogenerationPlant(PowerSystemResource):
    """ A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.
    """
    # <<< cogeneration_plant
    # @generated
    def __init__(self, cogen_hpsendout_rating=0.0, rated_p=0.0, cogen_lpsendout_rating=0.0, cogen_lpsteam_rating=0.0, cogen_hpsteam_rating=0.0, steam_sendout_schedule=None, thermal_generating_units=None, *args, **kw_args):
        """ Initialises a new 'CogenerationPlant' instance.

        @param cogen_hpsendout_rating: The high pressure steam sendout 
        @param rated_p: The rated output active power of the cogeneration plant 
        @param cogen_lpsendout_rating: The low pressure steam sendout 
        @param cogen_lpsteam_rating: The low pressure steam rating 
        @param cogen_hpsteam_rating: The high pressure steam rating 
        @param steam_sendout_schedule: A cogeneration plant has a steam sendout schedule
        @param thermal_generating_units: A thermal generating unit may be a member of a cogeneration plant
        """
        # The high pressure steam sendout 
        self.cogen_hpsendout_rating = cogen_hpsendout_rating

        # The rated output active power of the cogeneration plant 
        self.rated_p = rated_p

        # The low pressure steam sendout 
        self.cogen_lpsendout_rating = cogen_lpsendout_rating

        # The low pressure steam rating 
        self.cogen_lpsteam_rating = cogen_lpsteam_rating

        # The high pressure steam rating 
        self.cogen_hpsteam_rating = cogen_hpsteam_rating


        self._steam_sendout_schedule = None
        self.steam_sendout_schedule = steam_sendout_schedule

        self._thermal_generating_units = []
        if thermal_generating_units is not None:
            self.thermal_generating_units = thermal_generating_units
        else:
            self.thermal_generating_units = []


        super(CogenerationPlant, self).__init__(*args, **kw_args)
    # >>> cogeneration_plant

    # <<< steam_sendout_schedule
    # @generated
    def get_steam_sendout_schedule(self):
        """ A cogeneration plant has a steam sendout schedule
        """
        return self._steam_sendout_schedule

    def set_steam_sendout_schedule(self, value):
        if self._steam_sendout_schedule is not None:
            self._steam_sendout_schedule._cogeneration_plant = None

        self._steam_sendout_schedule = value
        if self._steam_sendout_schedule is not None:
            self._steam_sendout_schedule._cogeneration_plant = self

    steam_sendout_schedule = property(get_steam_sendout_schedule, set_steam_sendout_schedule)
    # >>> steam_sendout_schedule

    # <<< thermal_generating_units
    # @generated
    def get_thermal_generating_units(self):
        """ A thermal generating unit may be a member of a cogeneration plant
        """
        return self._thermal_generating_units

    def set_thermal_generating_units(self, value):
        for x in self._thermal_generating_units:
            x._cogeneration_plant = None
        for y in value:
            y._cogeneration_plant = self
        self._thermal_generating_units = value

    thermal_generating_units = property(get_thermal_generating_units, set_thermal_generating_units)

    def add_thermal_generating_units(self, *thermal_generating_units):
        for obj in thermal_generating_units:
            obj._cogeneration_plant = self
            self._thermal_generating_units.append(obj)

    def remove_thermal_generating_units(self, *thermal_generating_units):
        for obj in thermal_generating_units:
            obj._cogeneration_plant = None
            self._thermal_generating_units.remove(obj)
    # >>> thermal_generating_units



class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """
    # <<< gross_to_net_active_power_curve
    # @generated
    def __init__(self, generating_unit=None, *args, **kw_args):
        """ Initialises a new 'GrossToNetActivePowerCurve' instance.

        @param generating_unit: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """

        self._generating_unit = None
        self.generating_unit = generating_unit


        super(GrossToNetActivePowerCurve, self).__init__(*args, **kw_args)
    # >>> gross_to_net_active_power_curve

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.gross_to_net_active_power_curves if x != self]
            self._generating_unit._gross_to_net_active_power_curves = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._gross_to_net_active_power_curves.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit



class AirCompressor(PowerSystemResource):
    """ Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant
    """
    # <<< air_compressor
    # @generated
    def __init__(self, air_compressor_rating=0.0, combustion_turbine=None, caesplant=None, *args, **kw_args):
        """ Initialises a new 'AirCompressor' instance.

        @param air_compressor_rating: Rating of the CAES air compressor 
        @param combustion_turbine: A CAES air compressor is driven by combustion turbine
        @param caesplant: An air compressor may be a member of a compressed air energy storage plant
        """
        # Rating of the CAES air compressor 
        self.air_compressor_rating = air_compressor_rating


        self._combustion_turbine = None
        self.combustion_turbine = combustion_turbine

        self._caesplant = None
        self.caesplant = caesplant


        super(AirCompressor, self).__init__(*args, **kw_args)
    # >>> air_compressor

    # <<< combustion_turbine
    # @generated
    def get_combustion_turbine(self):
        """ A CAES air compressor is driven by combustion turbine
        """
        return self._combustion_turbine

    def set_combustion_turbine(self, value):
        if self._combustion_turbine is not None:
            self._combustion_turbine._air_compressor = None

        self._combustion_turbine = value
        if self._combustion_turbine is not None:
            self._combustion_turbine._air_compressor = self

    combustion_turbine = property(get_combustion_turbine, set_combustion_turbine)
    # >>> combustion_turbine

    # <<< caesplant
    # @generated
    def get_caesplant(self):
        """ An air compressor may be a member of a compressed air energy storage plant
        """
        return self._caesplant

    def set_caesplant(self, value):
        if self._caesplant is not None:
            self._caesplant._air_compressor = None

        self._caesplant = value
        if self._caesplant is not None:
            self._caesplant._air_compressor = self

    caesplant = property(get_caesplant, set_caesplant)
    # >>> caesplant



class ShutdownCurve(Curve):
    """ Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)
    """
    # <<< shutdown_curve
    # @generated
    def __init__(self, shutdown_date='', shutdown_cost=0.0, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'ShutdownCurve' instance.

        @param shutdown_date: The date and time of the most recent generating unit shutdown 
        @param shutdown_cost: Fixed shutdown cost 
        @param thermal_generating_unit: A thermal generating unit may have a shutdown curve
        """
        # The date and time of the most recent generating unit shutdown 
        self.shutdown_date = shutdown_date

        # Fixed shutdown cost 
        self.shutdown_cost = shutdown_cost


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(ShutdownCurve, self).__init__(*args, **kw_args)
    # >>> shutdown_curve

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have a shutdown curve
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._shutdown_curve = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._shutdown_curve = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class FuelAllocationSchedule(Curve):
    """ The amount of fuel of a given type which is allocated for consumption over a specified period of time
    """
    # <<< fuel_allocation_schedule
    # @generated
    def __init__(self, fuel_type='gas', min_fuel_allocation=0.0, fuel_allocation_start_date='', max_fuel_allocation=0.0, fuel_allocation_end_date='', thermal_generating_unit=None, fossil_fuel=None, *args, **kw_args):
        """ Initialises a new 'FuelAllocationSchedule' instance.

        @param fuel_type: The type of fuel, which also indicates the corresponding measurement unit Values are: "gas", "oil", "coal", "lignite"
        @param min_fuel_allocation: The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract 
        @param fuel_allocation_start_date: The start time and date of the fuel allocation schedule 
        @param max_fuel_allocation: The maximum amount fuel that is allocated for consumption for the scheduled time period 
        @param fuel_allocation_end_date: The end time and date of the fuel allocation schedule 
        @param thermal_generating_unit: A thermal generating unit may have one or more fuel allocation schedules
        @param fossil_fuel: A fuel allocation schedule must have a fossil fuel
        """
        # The type of fuel, which also indicates the corresponding measurement unit Values are: "gas", "oil", "coal", "lignite"
        self.fuel_type = fuel_type

        # The minimum amount fuel that is allocated for consumption for the scheduled time period, e.g., based on a 'take-or-pay' contract 
        self.min_fuel_allocation = min_fuel_allocation

        # The start time and date of the fuel allocation schedule 
        self.fuel_allocation_start_date = fuel_allocation_start_date

        # The maximum amount fuel that is allocated for consumption for the scheduled time period 
        self.max_fuel_allocation = max_fuel_allocation

        # The end time and date of the fuel allocation schedule 
        self.fuel_allocation_end_date = fuel_allocation_end_date


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit

        self._fossil_fuel = None
        self.fossil_fuel = fossil_fuel


        super(FuelAllocationSchedule, self).__init__(*args, **kw_args)
    # >>> fuel_allocation_schedule

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have one or more fuel allocation schedules
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            filtered = [x for x in self.thermal_generating_unit.fuel_allocation_schedules if x != self]
            self._thermal_generating_unit._fuel_allocation_schedules = filtered

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._fuel_allocation_schedules.append(self)

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit

    # <<< fossil_fuel
    # @generated
    def get_fossil_fuel(self):
        """ A fuel allocation schedule must have a fossil fuel
        """
        return self._fossil_fuel

    def set_fossil_fuel(self, value):
        if self._fossil_fuel is not None:
            filtered = [x for x in self.fossil_fuel.fuel_allocation_schedules if x != self]
            self._fossil_fuel._fuel_allocation_schedules = filtered

        self._fossil_fuel = value
        if self._fossil_fuel is not None:
            self._fossil_fuel._fuel_allocation_schedules.append(self)

    fossil_fuel = property(get_fossil_fuel, set_fossil_fuel)
    # >>> fossil_fuel



class TailbayLossCurve(Curve):
    """ Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level
    """
    # <<< tailbay_loss_curve
    # @generated
    def __init__(self, hydro_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'TailbayLossCurve' instance.

        @param hydro_generating_unit: A hydro generating unit has a tailbay loss curve
        """

        self._hydro_generating_unit = None
        self.hydro_generating_unit = hydro_generating_unit


        super(TailbayLossCurve, self).__init__(*args, **kw_args)
    # >>> tailbay_loss_curve

    # <<< hydro_generating_unit
    # @generated
    def get_hydro_generating_unit(self):
        """ A hydro generating unit has a tailbay loss curve
        """
        return self._hydro_generating_unit

    def set_hydro_generating_unit(self, value):
        if self._hydro_generating_unit is not None:
            filtered = [x for x in self.hydro_generating_unit.tailbay_loss_curve if x != self]
            self._hydro_generating_unit._tailbay_loss_curve = filtered

        self._hydro_generating_unit = value
        if self._hydro_generating_unit is not None:
            self._hydro_generating_unit._tailbay_loss_curve.append(self)

    hydro_generating_unit = property(get_hydro_generating_unit, set_hydro_generating_unit)
    # >>> hydro_generating_unit



class HydroPumpOpSchedule(RegularIntervalSchedule):
    """ The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)
    """
    # <<< hydro_pump_op_schedule
    # @generated
    def __init__(self, hydro_pump=None, *args, **kw_args):
        """ Initialises a new 'HydroPumpOpSchedule' instance.

        @param hydro_pump: The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """

        self._hydro_pump = None
        self.hydro_pump = hydro_pump


        super(HydroPumpOpSchedule, self).__init__(*args, **kw_args)
    # >>> hydro_pump_op_schedule

    # <<< hydro_pump
    # @generated
    def get_hydro_pump(self):
        """ The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        return self._hydro_pump

    def set_hydro_pump(self, value):
        if self._hydro_pump is not None:
            self._hydro_pump._hydro_pump_op_schedule = None

        self._hydro_pump = value
        if self._hydro_pump is not None:
            self._hydro_pump._hydro_pump_op_schedule = self

    hydro_pump = property(get_hydro_pump, set_hydro_pump)
    # >>> hydro_pump



class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas
    """
    # <<< fossil_fuel
    # @generated
    def __init__(self, fossil_fuel_type='gas', fuel_dispatch_cost=0.0, fuel_eff_factor=0.0, fuel_cost=0.0, low_breakpoint_p=0.0, high_breakpoint_p=0.0, fuel_sulfur=0.0, fuel_handling_cost=0.0, fuel_heat_content=0.0, fuel_mixture=0.0, fuel_allocation_schedules=None, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'FossilFuel' instance.

        @param fossil_fuel_type: The type of fossil fuel, such as coal, oil, or gas. Values are: "gas", "oil", "coal", "lignite"
        @param fuel_dispatch_cost: The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost 
        @param fuel_eff_factor: The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed 
        @param fuel_cost: The cost in terms of heat value for the given type of fuel 
        @param low_breakpoint_p: The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels. 
        @param high_breakpoint_p: The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels. 
        @param fuel_sulfur: The fuel's fraction of pollution credit per unit of heat content 
        @param fuel_handling_cost: Handling and processing cost associated with this fuel 
        @param fuel_heat_content: The amount of heat per weight (or volume) of the given type of fuel 
        @param fuel_mixture: Relative amount of the given type of fuel, when multiple fuels are being consumed. 
        @param fuel_allocation_schedules: A fuel allocation schedule must have a fossil fuel
        @param thermal_generating_unit: A thermal generating unit may have one or more fossil fuels
        """
        # The type of fossil fuel, such as coal, oil, or gas. Values are: "gas", "oil", "coal", "lignite"
        self.fossil_fuel_type = fossil_fuel_type

        # The cost of fuel used for economic dispatching which includes: fuel cost, transportation cost,  and incremental maintenance cost 
        self.fuel_dispatch_cost = fuel_dispatch_cost

        # The efficiency factor for the fuel (per unit) in terms of the effective energy absorbed 
        self.fuel_eff_factor = fuel_eff_factor

        # The cost in terms of heat value for the given type of fuel 
        self.fuel_cost = fuel_cost

        # The active power output level of the unit at which the given type of fuel is switched off. This fuel (e.g., oil) is sometimes used to stabilize the base fuel (e.g., coal) at low active power output levels. 
        self.low_breakpoint_p = low_breakpoint_p

        # The active power output level of the unit at which the given type of fuel is switched on. This fuel (e.g., oil) is sometimes used to supplement the base fuel (e.g., coal) at high active power output levels. 
        self.high_breakpoint_p = high_breakpoint_p

        # The fuel's fraction of pollution credit per unit of heat content 
        self.fuel_sulfur = fuel_sulfur

        # Handling and processing cost associated with this fuel 
        self.fuel_handling_cost = fuel_handling_cost

        # The amount of heat per weight (or volume) of the given type of fuel 
        self.fuel_heat_content = fuel_heat_content

        # Relative amount of the given type of fuel, when multiple fuels are being consumed. 
        self.fuel_mixture = fuel_mixture


        self._fuel_allocation_schedules = []
        if fuel_allocation_schedules is not None:
            self.fuel_allocation_schedules = fuel_allocation_schedules
        else:
            self.fuel_allocation_schedules = []

        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(FossilFuel, self).__init__(*args, **kw_args)
    # >>> fossil_fuel

    # <<< fuel_allocation_schedules
    # @generated
    def get_fuel_allocation_schedules(self):
        """ A fuel allocation schedule must have a fossil fuel
        """
        return self._fuel_allocation_schedules

    def set_fuel_allocation_schedules(self, value):
        for x in self._fuel_allocation_schedules:
            x._fossil_fuel = None
        for y in value:
            y._fossil_fuel = self
        self._fuel_allocation_schedules = value

    fuel_allocation_schedules = property(get_fuel_allocation_schedules, set_fuel_allocation_schedules)

    def add_fuel_allocation_schedules(self, *fuel_allocation_schedules):
        for obj in fuel_allocation_schedules:
            obj._fossil_fuel = self
            self._fuel_allocation_schedules.append(obj)

    def remove_fuel_allocation_schedules(self, *fuel_allocation_schedules):
        for obj in fuel_allocation_schedules:
            obj._fossil_fuel = None
            self._fuel_allocation_schedules.remove(obj)
    # >>> fuel_allocation_schedules

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have one or more fossil fuels
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            filtered = [x for x in self.thermal_generating_unit.fossil_fuels if x != self]
            self._thermal_generating_unit._fossil_fuels = filtered

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._fossil_fuels.append(self)

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class TargetLevelSchedule(Curve):
    """ Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days
    """
    # <<< target_level_schedule
    # @generated
    def __init__(self, low_level_limit=0.0, high_level_limit=0.0, reservoir=None, *args, **kw_args):
        """ Initialises a new 'TargetLevelSchedule' instance.

        @param low_level_limit: Low target level limit, below which the reservoir operation will be penalized 
        @param high_level_limit: High target level limit, above which the reservoir operation will be penalized 
        @param reservoir: A reservoir may have a water level target schedule.
        """
        # Low target level limit, below which the reservoir operation will be penalized 
        self.low_level_limit = low_level_limit

        # High target level limit, above which the reservoir operation will be penalized 
        self.high_level_limit = high_level_limit


        self._reservoir = None
        self.reservoir = reservoir


        super(TargetLevelSchedule, self).__init__(*args, **kw_args)
    # >>> target_level_schedule

    # <<< reservoir
    # @generated
    def get_reservoir(self):
        """ A reservoir may have a water level target schedule.
        """
        return self._reservoir

    def set_reservoir(self, value):
        if self._reservoir is not None:
            self._reservoir._target_level_schedule = None

        self._reservoir = value
        if self._reservoir is not None:
            self._reservoir._target_level_schedule = self

    reservoir = property(get_reservoir, set_reservoir)
    # >>> reservoir



class HydroPump(PowerSystemResource):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plant
    """
    # <<< hydro_pump
    # @generated
    def __init__(self, pump_disch_at_min_head=0.0, pump_disch_at_max_head=0.0, pump_power_at_min_head=0.0, pump_power_at_max_head=0.0, hydro_pump_op_schedule=None, synchronous_machine=None, hydro_power_plant=None, *args, **kw_args):
        """ Initialises a new 'HydroPump' instance.

        @param pump_disch_at_min_head: The pumping discharge (m3/sec) under minimum head conditions, usually at full gate 
        @param pump_disch_at_max_head: The pumping discharge (m3/sec) under maximum head conditions, usually at full gate 
        @param pump_power_at_min_head: The pumping power under minimum head conditions, usually at full gate. 
        @param pump_power_at_max_head: The pumping power under maximum head conditions, usually at full gate 
        @param hydro_pump_op_schedule: The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        @param synchronous_machine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        @param hydro_power_plant: The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        # The pumping discharge (m3/sec) under minimum head conditions, usually at full gate 
        self.pump_disch_at_min_head = pump_disch_at_min_head

        # The pumping discharge (m3/sec) under maximum head conditions, usually at full gate 
        self.pump_disch_at_max_head = pump_disch_at_max_head

        # The pumping power under minimum head conditions, usually at full gate. 
        self.pump_power_at_min_head = pump_power_at_min_head

        # The pumping power under maximum head conditions, usually at full gate 
        self.pump_power_at_max_head = pump_power_at_max_head


        self._hydro_pump_op_schedule = None
        self.hydro_pump_op_schedule = hydro_pump_op_schedule

        self._synchronous_machine = None
        self.synchronous_machine = synchronous_machine

        self._hydro_power_plant = None
        self.hydro_power_plant = hydro_power_plant


        super(HydroPump, self).__init__(*args, **kw_args)
    # >>> hydro_pump

    # <<< hydro_pump_op_schedule
    # @generated
    def get_hydro_pump_op_schedule(self):
        """ The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        """
        return self._hydro_pump_op_schedule

    def set_hydro_pump_op_schedule(self, value):
        if self._hydro_pump_op_schedule is not None:
            self._hydro_pump_op_schedule._hydro_pump = None

        self._hydro_pump_op_schedule = value
        if self._hydro_pump_op_schedule is not None:
            self._hydro_pump_op_schedule._hydro_pump = self

    hydro_pump_op_schedule = property(get_hydro_pump_op_schedule, set_hydro_pump_op_schedule)
    # >>> hydro_pump_op_schedule

    # <<< synchronous_machine
    # @generated
    def get_synchronous_machine(self):
        """ The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._synchronous_machine

    def set_synchronous_machine(self, value):
        if self._synchronous_machine is not None:
            self._synchronous_machine._hydro_pump = None

        self._synchronous_machine = value
        if self._synchronous_machine is not None:
            self._synchronous_machine._hydro_pump = self

    synchronous_machine = property(get_synchronous_machine, set_synchronous_machine)
    # >>> synchronous_machine

    # <<< hydro_power_plant
    # @generated
    def get_hydro_power_plant(self):
        """ The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        return self._hydro_power_plant

    def set_hydro_power_plant(self, value):
        if self._hydro_power_plant is not None:
            filtered = [x for x in self.hydro_power_plant.hydro_pumps if x != self]
            self._hydro_power_plant._hydro_pumps = filtered

        self._hydro_power_plant = value
        if self._hydro_power_plant is not None:
            self._hydro_power_plant._hydro_pumps.append(self)

    hydro_power_plant = property(get_hydro_power_plant, set_hydro_power_plant)
    # >>> hydro_power_plant



class HydroPowerPlant(PowerSystemResource):
    """ A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.
    """
    # <<< hydro_power_plant
    # @generated
    def __init__(self, hydro_plant_type='major_storage', surge_tank_code='', penstock_type='', pump_rated_p=0.0, gen_rated_p=0.0, plant_discharge_capacity=0.0, discharge_travel_delay=0.0, plant_rated_head=0.0, surge_tank_crest_level=0.0, gen_source_pump_discharge_reservoir=None, hydro_pumps=None, hydro_generating_units=None, reservoir=None, *args, **kw_args):
        """ Initialises a new 'HydroPowerPlant' instance.

        @param hydro_plant_type: The type of hydro power plant. Values are: "major_storage", "run_of_river", "minor_storage", "pumped_storage"
        @param surge_tank_code: A code describing the type (or absence) of surge tank that is associated with the hydro power plant 
        @param penstock_type: Type and configuration of hydro plant penstock(s) 
        @param pump_rated_p: The hydro plant's pumping rating active power for rated head conditions 
        @param gen_rated_p: The hydro plant's generating rating active power for rated head conditions 
        @param plant_discharge_capacity: Total plant discharge capacity in cubic meters per second 
        @param discharge_travel_delay: Water travel delay from tailbay to next downstream hydro power station 
        @param plant_rated_head: The plant's rated gross head 
        @param surge_tank_crest_level: The level at which the surge tank spills 
        @param gen_source_pump_discharge_reservoir: Generators are supplied water from or pumps discharge water to an upstream reservoir
        @param hydro_pumps: The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        @param hydro_generating_units: The hydro generating unit belongs to a hydro power plant
        @param reservoir: Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        # The type of hydro power plant. Values are: "major_storage", "run_of_river", "minor_storage", "pumped_storage"
        self.hydro_plant_type = hydro_plant_type

        # A code describing the type (or absence) of surge tank that is associated with the hydro power plant 
        self.surge_tank_code = surge_tank_code

        # Type and configuration of hydro plant penstock(s) 
        self.penstock_type = penstock_type

        # The hydro plant's pumping rating active power for rated head conditions 
        self.pump_rated_p = pump_rated_p

        # The hydro plant's generating rating active power for rated head conditions 
        self.gen_rated_p = gen_rated_p

        # Total plant discharge capacity in cubic meters per second 
        self.plant_discharge_capacity = plant_discharge_capacity

        # Water travel delay from tailbay to next downstream hydro power station 
        self.discharge_travel_delay = discharge_travel_delay

        # The plant's rated gross head 
        self.plant_rated_head = plant_rated_head

        # The level at which the surge tank spills 
        self.surge_tank_crest_level = surge_tank_crest_level


        self._gen_source_pump_discharge_reservoir = None
        self.gen_source_pump_discharge_reservoir = gen_source_pump_discharge_reservoir

        self._hydro_pumps = []
        if hydro_pumps is not None:
            self.hydro_pumps = hydro_pumps
        else:
            self.hydro_pumps = []

        self._hydro_generating_units = []
        if hydro_generating_units is not None:
            self.hydro_generating_units = hydro_generating_units
        else:
            self.hydro_generating_units = []

        self._reservoir = None
        self.reservoir = reservoir


        super(HydroPowerPlant, self).__init__(*args, **kw_args)
    # >>> hydro_power_plant

    # <<< gen_source_pump_discharge_reservoir
    # @generated
    def get_gen_source_pump_discharge_reservoir(self):
        """ Generators are supplied water from or pumps discharge water to an upstream reservoir
        """
        return self._gen_source_pump_discharge_reservoir

    def set_gen_source_pump_discharge_reservoir(self, value):
        if self._gen_source_pump_discharge_reservoir is not None:
            filtered = [x for x in self.gen_source_pump_discharge_reservoir.upstream_from_hydro_power_plants if x != self]
            self._gen_source_pump_discharge_reservoir._upstream_from_hydro_power_plants = filtered

        self._gen_source_pump_discharge_reservoir = value
        if self._gen_source_pump_discharge_reservoir is not None:
            self._gen_source_pump_discharge_reservoir._upstream_from_hydro_power_plants.append(self)

    gen_source_pump_discharge_reservoir = property(get_gen_source_pump_discharge_reservoir, set_gen_source_pump_discharge_reservoir)
    # >>> gen_source_pump_discharge_reservoir

    # <<< hydro_pumps
    # @generated
    def get_hydro_pumps(self):
        """ The hydro pump may be a member of a pumped storage plant or a pump for distributing water
        """
        return self._hydro_pumps

    def set_hydro_pumps(self, value):
        for x in self._hydro_pumps:
            x._hydro_power_plant = None
        for y in value:
            y._hydro_power_plant = self
        self._hydro_pumps = value

    hydro_pumps = property(get_hydro_pumps, set_hydro_pumps)

    def add_hydro_pumps(self, *hydro_pumps):
        for obj in hydro_pumps:
            obj._hydro_power_plant = self
            self._hydro_pumps.append(obj)

    def remove_hydro_pumps(self, *hydro_pumps):
        for obj in hydro_pumps:
            obj._hydro_power_plant = None
            self._hydro_pumps.remove(obj)
    # >>> hydro_pumps

    # <<< hydro_generating_units
    # @generated
    def get_hydro_generating_units(self):
        """ The hydro generating unit belongs to a hydro power plant
        """
        return self._hydro_generating_units

    def set_hydro_generating_units(self, value):
        for x in self._hydro_generating_units:
            x._hydro_power_plant = None
        for y in value:
            y._hydro_power_plant = self
        self._hydro_generating_units = value

    hydro_generating_units = property(get_hydro_generating_units, set_hydro_generating_units)

    def add_hydro_generating_units(self, *hydro_generating_units):
        for obj in hydro_generating_units:
            obj._hydro_power_plant = self
            self._hydro_generating_units.append(obj)

    def remove_hydro_generating_units(self, *hydro_generating_units):
        for obj in hydro_generating_units:
            obj._hydro_power_plant = None
            self._hydro_generating_units.remove(obj)
    # >>> hydro_generating_units

    # <<< reservoir
    # @generated
    def get_reservoir(self):
        """ Generators discharge water to or pumps are supplied water from a downstream reservoir
        """
        return self._reservoir

    def set_reservoir(self, value):
        if self._reservoir is not None:
            filtered = [x for x in self.reservoir.hydro_power_plants if x != self]
            self._reservoir._hydro_power_plants = filtered

        self._reservoir = value
        if self._reservoir is not None:
            self._reservoir._hydro_power_plants.append(self)

    reservoir = property(get_reservoir, set_reservoir)
    # >>> reservoir



class InflowForecast(RegularIntervalSchedule):
    """ Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.
    """
    # <<< inflow_forecast
    # @generated
    def __init__(self, reservoir=None, *args, **kw_args):
        """ Initialises a new 'InflowForecast' instance.

        @param reservoir: A reservoir may have a 'natural' inflow forecast.
        """

        self._reservoir = None
        self.reservoir = reservoir


        super(InflowForecast, self).__init__(*args, **kw_args)
    # >>> inflow_forecast

    # <<< reservoir
    # @generated
    def get_reservoir(self):
        """ A reservoir may have a 'natural' inflow forecast.
        """
        return self._reservoir

    def set_reservoir(self, value):
        if self._reservoir is not None:
            filtered = [x for x in self.reservoir.inflow_forecasts if x != self]
            self._reservoir._inflow_forecasts = filtered

        self._reservoir = value
        if self._reservoir is not None:
            self._reservoir._inflow_forecasts.append(self)

    reservoir = property(get_reservoir, set_reservoir)
    # >>> reservoir



class CombinedCyclePlant(PowerSystemResource):
    """ A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency
    """
    # <<< combined_cycle_plant
    # @generated
    def __init__(self, comb_cycle_plant_rating=0.0, thermal_generating_units=None, *args, **kw_args):
        """ Initialises a new 'CombinedCyclePlant' instance.

        @param comb_cycle_plant_rating: The combined cycle plant's active power output rating 
        @param thermal_generating_units: A thermal generating unit may be a member of a combined cycle plant
        """
        # The combined cycle plant's active power output rating 
        self.comb_cycle_plant_rating = comb_cycle_plant_rating


        self._thermal_generating_units = []
        if thermal_generating_units is not None:
            self.thermal_generating_units = thermal_generating_units
        else:
            self.thermal_generating_units = []


        super(CombinedCyclePlant, self).__init__(*args, **kw_args)
    # >>> combined_cycle_plant

    # <<< thermal_generating_units
    # @generated
    def get_thermal_generating_units(self):
        """ A thermal generating unit may be a member of a combined cycle plant
        """
        return self._thermal_generating_units

    def set_thermal_generating_units(self, value):
        for x in self._thermal_generating_units:
            x._combined_cycle_plant = None
        for y in value:
            y._combined_cycle_plant = self
        self._thermal_generating_units = value

    thermal_generating_units = property(get_thermal_generating_units, set_thermal_generating_units)

    def add_thermal_generating_units(self, *thermal_generating_units):
        for obj in thermal_generating_units:
            obj._combined_cycle_plant = self
            self._thermal_generating_units.append(obj)

    def remove_thermal_generating_units(self, *thermal_generating_units):
        for obj in thermal_generating_units:
            obj._combined_cycle_plant = None
            self._thermal_generating_units.remove(obj)
    # >>> thermal_generating_units



class HydroGeneratingEfficiencyCurve(Curve):
    """ Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    """
    # <<< hydro_generating_efficiency_curve
    # @generated
    def __init__(self, hydro_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'HydroGeneratingEfficiencyCurve' instance.

        @param hydro_generating_unit: A hydro generating unit has an efficiency curve
        """

        self._hydro_generating_unit = None
        self.hydro_generating_unit = hydro_generating_unit


        super(HydroGeneratingEfficiencyCurve, self).__init__(*args, **kw_args)
    # >>> hydro_generating_efficiency_curve

    # <<< hydro_generating_unit
    # @generated
    def get_hydro_generating_unit(self):
        """ A hydro generating unit has an efficiency curve
        """
        return self._hydro_generating_unit

    def set_hydro_generating_unit(self, value):
        if self._hydro_generating_unit is not None:
            filtered = [x for x in self.hydro_generating_unit.hydro_generating_efficiency_curves if x != self]
            self._hydro_generating_unit._hydro_generating_efficiency_curves = filtered

        self._hydro_generating_unit = value
        if self._hydro_generating_unit is not None:
            self._hydro_generating_unit._hydro_generating_efficiency_curves.append(self)

    hydro_generating_unit = property(get_hydro_generating_unit, set_hydro_generating_unit)
    # >>> hydro_generating_unit



class StartIgnFuelCurve(Curve):
    """ The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """
    # <<< start_ign_fuel_curve
    # @generated
    def __init__(self, ignition_fuel_type='gas', startup_model=None, *args, **kw_args):
        """ Initialises a new 'StartIgnFuelCurve' instance.

        @param ignition_fuel_type: Type of ignition fuel Values are: "gas", "oil", "coal", "lignite"
        @param startup_model: The unit's startup model may have a startup ignition fuel curve
        """
        # Type of ignition fuel Values are: "gas", "oil", "coal", "lignite"
        self.ignition_fuel_type = ignition_fuel_type


        self._startup_model = None
        self.startup_model = startup_model


        super(StartIgnFuelCurve, self).__init__(*args, **kw_args)
    # >>> start_ign_fuel_curve

    # <<< startup_model
    # @generated
    def get_startup_model(self):
        """ The unit's startup model may have a startup ignition fuel curve
        """
        return self._startup_model

    def set_startup_model(self, value):
        if self._startup_model is not None:
            self._startup_model._start_ign_fuel_curve = None

        self._startup_model = value
        if self._startup_model is not None:
            self._startup_model._start_ign_fuel_curve = self

    startup_model = property(get_startup_model, set_startup_model)
    # >>> startup_model



class CAESPlant(PowerSystemResource):
    """ Compressed air energy storage plant
    """
    # <<< caesplant
    # @generated
    def __init__(self, rated_capacity_p=0.0, energy_storage_capacity=0.0, thermal_generating_unit=None, air_compressor=None, *args, **kw_args):
        """ Initialises a new 'CAESPlant' instance.

        @param rated_capacity_p: The CAES plant's gross rated generating capacity 
        @param energy_storage_capacity: The rated energy storage capacity. 
        @param thermal_generating_unit: A thermal generating unit may be a member of a compressed air energy storage plant
        @param air_compressor: An air compressor may be a member of a compressed air energy storage plant
        """
        # The CAES plant's gross rated generating capacity 
        self.rated_capacity_p = rated_capacity_p

        # The rated energy storage capacity. 
        self.energy_storage_capacity = energy_storage_capacity


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit

        self._air_compressor = None
        self.air_compressor = air_compressor


        super(CAESPlant, self).__init__(*args, **kw_args)
    # >>> caesplant

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may be a member of a compressed air energy storage plant
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._caesplant = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._caesplant = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit

    # <<< air_compressor
    # @generated
    def get_air_compressor(self):
        """ An air compressor may be a member of a compressed air energy storage plant
        """
        return self._air_compressor

    def set_air_compressor(self, value):
        if self._air_compressor is not None:
            self._air_compressor._caesplant = None

        self._air_compressor = value
        if self._air_compressor is not None:
            self._air_compressor._caesplant = self

    air_compressor = property(get_air_compressor, set_air_compressor)
    # >>> air_compressor



class GenUnitOpSchedule(RegularIntervalSchedule):
    """ The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.
    """
    # <<< gen_unit_op_schedule
    # @generated
    def __init__(self, generating_unit=None, *args, **kw_args):
        """ Initialises a new 'GenUnitOpSchedule' instance.

        @param generating_unit: A generating unit may have an operating schedule, indicating the planned operation of the unit
        """

        self._generating_unit = None
        self.generating_unit = generating_unit


        super(GenUnitOpSchedule, self).__init__(*args, **kw_args)
    # >>> gen_unit_op_schedule

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            self._generating_unit._gen_unit_op_schedule = None

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._gen_unit_op_schedule = self

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit



class SteamSendoutSchedule(RegularIntervalSchedule):
    """ The cogeneration plant's steam sendout schedule in volume per time unit.
    """
    # <<< steam_sendout_schedule
    # @generated
    def __init__(self, cogeneration_plant=None, *args, **kw_args):
        """ Initialises a new 'SteamSendoutSchedule' instance.

        @param cogeneration_plant: A cogeneration plant has a steam sendout schedule
        """

        self._cogeneration_plant = None
        self.cogeneration_plant = cogeneration_plant


        super(SteamSendoutSchedule, self).__init__(*args, **kw_args)
    # >>> steam_sendout_schedule

    # <<< cogeneration_plant
    # @generated
    def get_cogeneration_plant(self):
        """ A cogeneration plant has a steam sendout schedule
        """
        return self._cogeneration_plant

    def set_cogeneration_plant(self, value):
        if self._cogeneration_plant is not None:
            self._cogeneration_plant._steam_sendout_schedule = None

        self._cogeneration_plant = value
        if self._cogeneration_plant is not None:
            self._cogeneration_plant._steam_sendout_schedule = self

    cogeneration_plant = property(get_cogeneration_plant, set_cogeneration_plant)
    # >>> cogeneration_plant



class StartRampCurve(Curve):
    """ Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line
    """
    # <<< start_ramp_curve
    # @generated
    def __init__(self, hot_standby_ramp=0.0, startup_model=None, *args, **kw_args):
        """ Initialises a new 'StartRampCurve' instance.

        @param hot_standby_ramp: The startup ramp rate in gross for a unit that is on hot standby 
        @param startup_model: The unit's startup model may have a startup ramp curve
        """
        # The startup ramp rate in gross for a unit that is on hot standby 
        self.hot_standby_ramp = hot_standby_ramp


        self._startup_model = None
        self.startup_model = startup_model


        super(StartRampCurve, self).__init__(*args, **kw_args)
    # >>> start_ramp_curve

    # <<< startup_model
    # @generated
    def get_startup_model(self):
        """ The unit's startup model may have a startup ramp curve
        """
        return self._startup_model

    def set_startup_model(self, value):
        if self._startup_model is not None:
            self._startup_model._start_ramp_curve = None

        self._startup_model = value
        if self._startup_model is not None:
            self._startup_model._start_ramp_curve = self

    startup_model = property(get_startup_model, set_startup_model)
    # >>> startup_model



class HeatRateCurve(Curve):
    """ Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.
    """
    # <<< heat_rate_curve
    # @generated
    def __init__(self, is_net_gross_p=False, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'HeatRateCurve' instance.

        @param is_net_gross_p: Flag is set to true when output is expressed in net active power 
        @param thermal_generating_unit: A thermal generating unit may have a heat rate curve
        """
        # Flag is set to true when output is expressed in net active power 
        self.is_net_gross_p = is_net_gross_p


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(HeatRateCurve, self).__init__(*args, **kw_args)
    # >>> heat_rate_curve

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have a heat rate curve
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._heat_rate_curve = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._heat_rate_curve = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class LevelVsVolumeCurve(Curve):
    """ Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.
    """
    # <<< level_vs_volume_curve
    # @generated
    def __init__(self, reservoir=None, *args, **kw_args):
        """ Initialises a new 'LevelVsVolumeCurve' instance.

        @param reservoir: A reservoir may have a level versus volume relationship.
        """

        self._reservoir = None
        self.reservoir = reservoir


        super(LevelVsVolumeCurve, self).__init__(*args, **kw_args)
    # >>> level_vs_volume_curve

    # <<< reservoir
    # @generated
    def get_reservoir(self):
        """ A reservoir may have a level versus volume relationship.
        """
        return self._reservoir

    def set_reservoir(self, value):
        if self._reservoir is not None:
            filtered = [x for x in self.reservoir.level_vs_volume_curves if x != self]
            self._reservoir._level_vs_volume_curves = filtered

        self._reservoir = value
        if self._reservoir is not None:
            self._reservoir._level_vs_volume_curves.append(self)

    reservoir = property(get_reservoir, set_reservoir)
    # >>> reservoir



class EmissionCurve(Curve):
    """ Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.
    """
    # <<< emission_curve
    # @generated
    def __init__(self, emission_type='nitrogen_oxide', is_net_gross_p=False, emission_content=0.0, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'EmissionCurve' instance.

        @param emission_type: The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "nitrogen_oxide", "carbon_disulfide", "hydrogen_sulfide", "sulfur_dioxide", "chlorine", "carbon_dioxide"
        @param is_net_gross_p: Flag is set to true when output is expressed in net active power 
        @param emission_content: The emission content per quantity of fuel burned 
        @param thermal_generating_unit: A thermal generating unit may have  one or more emission curves
        """
        # The type of emission, which also gives the production rate measurement unit. The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "nitrogen_oxide", "carbon_disulfide", "hydrogen_sulfide", "sulfur_dioxide", "chlorine", "carbon_dioxide"
        self.emission_type = emission_type

        # Flag is set to true when output is expressed in net active power 
        self.is_net_gross_p = is_net_gross_p

        # The emission content per quantity of fuel burned 
        self.emission_content = emission_content


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(EmissionCurve, self).__init__(*args, **kw_args)
    # >>> emission_curve

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have  one or more emission curves
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            filtered = [x for x in self.thermal_generating_unit.emission_curves if x != self]
            self._thermal_generating_unit._emission_curves = filtered

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._emission_curves.append(self)

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class StartupModel(IdentifiedObject):
    """ Unit start up characteristics depending on how long the unit has been off line
    """
    # <<< startup_model
    # @generated
    def __init__(self, incremental_maint_cost=0.0, startup_date='', startup_cost=0.0, stby_aux_p=0.0, startup_priority=0, fixed_maint_cost=0.0, minimum_down_time=0.0, risk_factor_cost=0.0, minimum_run_time=0.0, hot_standby_heat=0.0, start_main_fuel_curve=None, start_ign_fuel_curve=None, start_ramp_curve=None, thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'StartupModel' instance.

        @param incremental_maint_cost: Incremental Maintenance Cost 
        @param startup_date: The date and time of the most recent generating unit startup 
        @param startup_cost: Total miscellaneous start up costs 
        @param stby_aux_p: The unit's auxiliary active power consumption to maintain standby mode 
        @param startup_priority: Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority. 
        @param fixed_maint_cost: Fixed Maintenance Cost 
        @param minimum_down_time: The minimum number of hours the unit must be down before restart 
        @param risk_factor_cost: The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit. 
        @param minimum_run_time: The minimum number of hours the unit must be operating before being allowed to shut down 
        @param hot_standby_heat: The amount of heat input per time uint required for hot standby operation 
        @param start_main_fuel_curve: The unit's startup model may have a startup main fuel curve
        @param start_ign_fuel_curve: The unit's startup model may have a startup ignition fuel curve
        @param start_ramp_curve: The unit's startup model may have a startup ramp curve
        @param thermal_generating_unit: A thermal generating unit may have a startup model
        """
        # Incremental Maintenance Cost 
        self.incremental_maint_cost = incremental_maint_cost

        # The date and time of the most recent generating unit startup 
        self.startup_date = startup_date

        # Total miscellaneous start up costs 
        self.startup_cost = startup_cost

        # The unit's auxiliary active power consumption to maintain standby mode 
        self.stby_aux_p = stby_aux_p

        # Startup priority within control area where lower numbers indicate higher priorities.  More than one unit in an area may be assigned the same priority. 
        self.startup_priority = startup_priority

        # Fixed Maintenance Cost 
        self.fixed_maint_cost = fixed_maint_cost

        # The minimum number of hours the unit must be down before restart 
        self.minimum_down_time = minimum_down_time

        # The opportunity cost associated with the return in monetary unit. This represents the restart's 'share' of the unit depreciation and risk of an event which would damage the unit. 
        self.risk_factor_cost = risk_factor_cost

        # The minimum number of hours the unit must be operating before being allowed to shut down 
        self.minimum_run_time = minimum_run_time

        # The amount of heat input per time uint required for hot standby operation 
        self.hot_standby_heat = hot_standby_heat


        self._start_main_fuel_curve = None
        self.start_main_fuel_curve = start_main_fuel_curve

        self._start_ign_fuel_curve = None
        self.start_ign_fuel_curve = start_ign_fuel_curve

        self._start_ramp_curve = None
        self.start_ramp_curve = start_ramp_curve

        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(StartupModel, self).__init__(*args, **kw_args)
    # >>> startup_model

    # <<< start_main_fuel_curve
    # @generated
    def get_start_main_fuel_curve(self):
        """ The unit's startup model may have a startup main fuel curve
        """
        return self._start_main_fuel_curve

    def set_start_main_fuel_curve(self, value):
        if self._start_main_fuel_curve is not None:
            self._start_main_fuel_curve._startup_model = None

        self._start_main_fuel_curve = value
        if self._start_main_fuel_curve is not None:
            self._start_main_fuel_curve._startup_model = self

    start_main_fuel_curve = property(get_start_main_fuel_curve, set_start_main_fuel_curve)
    # >>> start_main_fuel_curve

    # <<< start_ign_fuel_curve
    # @generated
    def get_start_ign_fuel_curve(self):
        """ The unit's startup model may have a startup ignition fuel curve
        """
        return self._start_ign_fuel_curve

    def set_start_ign_fuel_curve(self, value):
        if self._start_ign_fuel_curve is not None:
            self._start_ign_fuel_curve._startup_model = None

        self._start_ign_fuel_curve = value
        if self._start_ign_fuel_curve is not None:
            self._start_ign_fuel_curve._startup_model = self

    start_ign_fuel_curve = property(get_start_ign_fuel_curve, set_start_ign_fuel_curve)
    # >>> start_ign_fuel_curve

    # <<< start_ramp_curve
    # @generated
    def get_start_ramp_curve(self):
        """ The unit's startup model may have a startup ramp curve
        """
        return self._start_ramp_curve

    def set_start_ramp_curve(self, value):
        if self._start_ramp_curve is not None:
            self._start_ramp_curve._startup_model = None

        self._start_ramp_curve = value
        if self._start_ramp_curve is not None:
            self._start_ramp_curve._startup_model = self

    start_ramp_curve = property(get_start_ramp_curve, set_start_ramp_curve)
    # >>> start_ramp_curve

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have a startup model
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._startup_model = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._startup_model = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class EmissionAccount(Curve):
    """ Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.
    """
    # <<< emission_account
    # @generated
    def __init__(self, emission_type='nitrogen_oxide', emission_value_source='calculated', thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'EmissionAccount' instance.

        @param emission_type: The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "nitrogen_oxide", "carbon_disulfide", "hydrogen_sulfide", "sulfur_dioxide", "chlorine", "carbon_dioxide"
        @param emission_value_source: The source of the emission value. Values are: "calculated", "measured"
        @param thermal_generating_unit: A thermal generating unit may have one or more emission allowance accounts
        """
        # The type of emission, for example sulfur dioxide (SO2). The y1AxisUnits of the curve contains the unit of measure (e.g. kg) and the emissionType is the type of emission (e.g. sulfer dioxide). Values are: "nitrogen_oxide", "carbon_disulfide", "hydrogen_sulfide", "sulfur_dioxide", "chlorine", "carbon_dioxide"
        self.emission_type = emission_type

        # The source of the emission value. Values are: "calculated", "measured"
        self.emission_value_source = emission_value_source


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(EmissionAccount, self).__init__(*args, **kw_args)
    # >>> emission_account

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have one or more emission allowance accounts
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            filtered = [x for x in self.thermal_generating_unit.emmission_accounts if x != self]
            self._thermal_generating_unit._emmission_accounts = filtered

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._emmission_accounts.append(self)

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """
    # <<< thermal_generating_unit
    # @generated
    def __init__(self, o_mcost=0.0, heat_rate_curve=None, emmission_accounts=None, fuel_allocation_schedules=None, heat_input_curve=None, combined_cycle_plant=None, cogeneration_plant=None, emission_curves=None, shutdown_curve=None, caesplant=None, incremental_heat_rate_curve=None, startup_model=None, fossil_fuels=None, *args, **kw_args):
        """ Initialises a new 'ThermalGeneratingUnit' instance.

        @param o_mcost: Operating and maintenance cost for the thermal unit 
        @param heat_rate_curve: A thermal generating unit may have a heat rate curve
        @param emmission_accounts: A thermal generating unit may have one or more emission allowance accounts
        @param fuel_allocation_schedules: A thermal generating unit may have one or more fuel allocation schedules
        @param heat_input_curve: A thermal generating unit may have a heat input curve
        @param combined_cycle_plant: A thermal generating unit may be a member of a combined cycle plant
        @param cogeneration_plant: A thermal generating unit may be a member of a cogeneration plant
        @param emission_curves: A thermal generating unit may have  one or more emission curves
        @param shutdown_curve: A thermal generating unit may have a shutdown curve
        @param caesplant: A thermal generating unit may be a member of a compressed air energy storage plant
        @param incremental_heat_rate_curve: A thermal generating unit may have an incremental heat rate curve
        @param startup_model: A thermal generating unit may have a startup model
        @param fossil_fuels: A thermal generating unit may have one or more fossil fuels
        """
        # Operating and maintenance cost for the thermal unit 
        self.o_mcost = o_mcost


        self._heat_rate_curve = None
        self.heat_rate_curve = heat_rate_curve

        self._emmission_accounts = []
        if emmission_accounts is not None:
            self.emmission_accounts = emmission_accounts
        else:
            self.emmission_accounts = []

        self._fuel_allocation_schedules = []
        if fuel_allocation_schedules is not None:
            self.fuel_allocation_schedules = fuel_allocation_schedules
        else:
            self.fuel_allocation_schedules = []

        self._heat_input_curve = None
        self.heat_input_curve = heat_input_curve

        self._combined_cycle_plant = None
        self.combined_cycle_plant = combined_cycle_plant

        self._cogeneration_plant = None
        self.cogeneration_plant = cogeneration_plant

        self._emission_curves = []
        if emission_curves is not None:
            self.emission_curves = emission_curves
        else:
            self.emission_curves = []

        self._shutdown_curve = None
        self.shutdown_curve = shutdown_curve

        self._caesplant = None
        self.caesplant = caesplant

        self._incremental_heat_rate_curve = None
        self.incremental_heat_rate_curve = incremental_heat_rate_curve

        self._startup_model = None
        self.startup_model = startup_model

        self._fossil_fuels = []
        if fossil_fuels is not None:
            self.fossil_fuels = fossil_fuels
        else:
            self.fossil_fuels = []


        super(ThermalGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> thermal_generating_unit

    # <<< heat_rate_curve
    # @generated
    def get_heat_rate_curve(self):
        """ A thermal generating unit may have a heat rate curve
        """
        return self._heat_rate_curve

    def set_heat_rate_curve(self, value):
        if self._heat_rate_curve is not None:
            self._heat_rate_curve._thermal_generating_unit = None

        self._heat_rate_curve = value
        if self._heat_rate_curve is not None:
            self._heat_rate_curve._thermal_generating_unit = self

    heat_rate_curve = property(get_heat_rate_curve, set_heat_rate_curve)
    # >>> heat_rate_curve

    # <<< emmission_accounts
    # @generated
    def get_emmission_accounts(self):
        """ A thermal generating unit may have one or more emission allowance accounts
        """
        return self._emmission_accounts

    def set_emmission_accounts(self, value):
        for x in self._emmission_accounts:
            x._thermal_generating_unit = None
        for y in value:
            y._thermal_generating_unit = self
        self._emmission_accounts = value

    emmission_accounts = property(get_emmission_accounts, set_emmission_accounts)

    def add_emmission_accounts(self, *emmission_accounts):
        for obj in emmission_accounts:
            obj._thermal_generating_unit = self
            self._emmission_accounts.append(obj)

    def remove_emmission_accounts(self, *emmission_accounts):
        for obj in emmission_accounts:
            obj._thermal_generating_unit = None
            self._emmission_accounts.remove(obj)
    # >>> emmission_accounts

    # <<< fuel_allocation_schedules
    # @generated
    def get_fuel_allocation_schedules(self):
        """ A thermal generating unit may have one or more fuel allocation schedules
        """
        return self._fuel_allocation_schedules

    def set_fuel_allocation_schedules(self, value):
        for x in self._fuel_allocation_schedules:
            x._thermal_generating_unit = None
        for y in value:
            y._thermal_generating_unit = self
        self._fuel_allocation_schedules = value

    fuel_allocation_schedules = property(get_fuel_allocation_schedules, set_fuel_allocation_schedules)

    def add_fuel_allocation_schedules(self, *fuel_allocation_schedules):
        for obj in fuel_allocation_schedules:
            obj._thermal_generating_unit = self
            self._fuel_allocation_schedules.append(obj)

    def remove_fuel_allocation_schedules(self, *fuel_allocation_schedules):
        for obj in fuel_allocation_schedules:
            obj._thermal_generating_unit = None
            self._fuel_allocation_schedules.remove(obj)
    # >>> fuel_allocation_schedules

    # <<< heat_input_curve
    # @generated
    def get_heat_input_curve(self):
        """ A thermal generating unit may have a heat input curve
        """
        return self._heat_input_curve

    def set_heat_input_curve(self, value):
        if self._heat_input_curve is not None:
            self._heat_input_curve._thermal_generating_unit = None

        self._heat_input_curve = value
        if self._heat_input_curve is not None:
            self._heat_input_curve._thermal_generating_unit = self

    heat_input_curve = property(get_heat_input_curve, set_heat_input_curve)
    # >>> heat_input_curve

    # <<< combined_cycle_plant
    # @generated
    def get_combined_cycle_plant(self):
        """ A thermal generating unit may be a member of a combined cycle plant
        """
        return self._combined_cycle_plant

    def set_combined_cycle_plant(self, value):
        if self._combined_cycle_plant is not None:
            filtered = [x for x in self.combined_cycle_plant.thermal_generating_units if x != self]
            self._combined_cycle_plant._thermal_generating_units = filtered

        self._combined_cycle_plant = value
        if self._combined_cycle_plant is not None:
            self._combined_cycle_plant._thermal_generating_units.append(self)

    combined_cycle_plant = property(get_combined_cycle_plant, set_combined_cycle_plant)
    # >>> combined_cycle_plant

    # <<< cogeneration_plant
    # @generated
    def get_cogeneration_plant(self):
        """ A thermal generating unit may be a member of a cogeneration plant
        """
        return self._cogeneration_plant

    def set_cogeneration_plant(self, value):
        if self._cogeneration_plant is not None:
            filtered = [x for x in self.cogeneration_plant.thermal_generating_units if x != self]
            self._cogeneration_plant._thermal_generating_units = filtered

        self._cogeneration_plant = value
        if self._cogeneration_plant is not None:
            self._cogeneration_plant._thermal_generating_units.append(self)

    cogeneration_plant = property(get_cogeneration_plant, set_cogeneration_plant)
    # >>> cogeneration_plant

    # <<< emission_curves
    # @generated
    def get_emission_curves(self):
        """ A thermal generating unit may have  one or more emission curves
        """
        return self._emission_curves

    def set_emission_curves(self, value):
        for x in self._emission_curves:
            x._thermal_generating_unit = None
        for y in value:
            y._thermal_generating_unit = self
        self._emission_curves = value

    emission_curves = property(get_emission_curves, set_emission_curves)

    def add_emission_curves(self, *emission_curves):
        for obj in emission_curves:
            obj._thermal_generating_unit = self
            self._emission_curves.append(obj)

    def remove_emission_curves(self, *emission_curves):
        for obj in emission_curves:
            obj._thermal_generating_unit = None
            self._emission_curves.remove(obj)
    # >>> emission_curves

    # <<< shutdown_curve
    # @generated
    def get_shutdown_curve(self):
        """ A thermal generating unit may have a shutdown curve
        """
        return self._shutdown_curve

    def set_shutdown_curve(self, value):
        if self._shutdown_curve is not None:
            self._shutdown_curve._thermal_generating_unit = None

        self._shutdown_curve = value
        if self._shutdown_curve is not None:
            self._shutdown_curve._thermal_generating_unit = self

    shutdown_curve = property(get_shutdown_curve, set_shutdown_curve)
    # >>> shutdown_curve

    # <<< caesplant
    # @generated
    def get_caesplant(self):
        """ A thermal generating unit may be a member of a compressed air energy storage plant
        """
        return self._caesplant

    def set_caesplant(self, value):
        if self._caesplant is not None:
            self._caesplant._thermal_generating_unit = None

        self._caesplant = value
        if self._caesplant is not None:
            self._caesplant._thermal_generating_unit = self

    caesplant = property(get_caesplant, set_caesplant)
    # >>> caesplant

    # <<< incremental_heat_rate_curve
    # @generated
    def get_incremental_heat_rate_curve(self):
        """ A thermal generating unit may have an incremental heat rate curve
        """
        return self._incremental_heat_rate_curve

    def set_incremental_heat_rate_curve(self, value):
        if self._incremental_heat_rate_curve is not None:
            self._incremental_heat_rate_curve._thermal_generating_unit = None

        self._incremental_heat_rate_curve = value
        if self._incremental_heat_rate_curve is not None:
            self._incremental_heat_rate_curve._thermal_generating_unit = self

    incremental_heat_rate_curve = property(get_incremental_heat_rate_curve, set_incremental_heat_rate_curve)
    # >>> incremental_heat_rate_curve

    # <<< startup_model
    # @generated
    def get_startup_model(self):
        """ A thermal generating unit may have a startup model
        """
        return self._startup_model

    def set_startup_model(self, value):
        if self._startup_model is not None:
            self._startup_model._thermal_generating_unit = None

        self._startup_model = value
        if self._startup_model is not None:
            self._startup_model._thermal_generating_unit = self

    startup_model = property(get_startup_model, set_startup_model)
    # >>> startup_model

    # <<< fossil_fuels
    # @generated
    def get_fossil_fuels(self):
        """ A thermal generating unit may have one or more fossil fuels
        """
        return self._fossil_fuels

    def set_fossil_fuels(self, value):
        for x in self._fossil_fuels:
            x._thermal_generating_unit = None
        for y in value:
            y._thermal_generating_unit = self
        self._fossil_fuels = value

    fossil_fuels = property(get_fossil_fuels, set_fossil_fuels)

    def add_fossil_fuels(self, *fossil_fuels):
        for obj in fossil_fuels:
            obj._thermal_generating_unit = self
            self._fossil_fuels.append(obj)

    def remove_fossil_fuels(self, *fossil_fuels):
        for obj in fossil_fuels:
            obj._thermal_generating_unit = None
            self._fossil_fuels.remove(obj)
    # >>> fossil_fuels



class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit.
    """
    pass
    # <<< wind_generating_unit
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'WindGeneratingUnit' instance.

        """


        super(WindGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> wind_generating_unit



class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit.
    """
    pass
    # <<< nuclear_generating_unit
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'NuclearGeneratingUnit' instance.

        """


        super(NuclearGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> nuclear_generating_unit



class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """
    # <<< hydro_generating_unit
    # @generated
    def __init__(self, energy_conversion_capability='generator', hydro_unit_water_cost=0.0, tailbay_loss_curve=None, hydro_power_plant=None, penstock_loss_curve=None, hydro_generating_efficiency_curves=None, *args, **kw_args):
        """ Initialises a new 'HydroGeneratingUnit' instance.

        @param energy_conversion_capability: Energy conversion capability for generating. Values are: "generator", "pump_and_generator"
        @param hydro_unit_water_cost: The equivalent cost of water that drives the hydro turbine, expressed as cost per volume. 
        @param tailbay_loss_curve: A hydro generating unit has a tailbay loss curve
        @param hydro_power_plant: The hydro generating unit belongs to a hydro power plant
        @param penstock_loss_curve: A hydro generating unit has a penstock loss curve
        @param hydro_generating_efficiency_curves: A hydro generating unit has an efficiency curve
        """
        # Energy conversion capability for generating. Values are: "generator", "pump_and_generator"
        self.energy_conversion_capability = energy_conversion_capability

        # The equivalent cost of water that drives the hydro turbine, expressed as cost per volume. 
        self.hydro_unit_water_cost = hydro_unit_water_cost


        self._tailbay_loss_curve = []
        if tailbay_loss_curve is not None:
            self.tailbay_loss_curve = tailbay_loss_curve
        else:
            self.tailbay_loss_curve = []

        self._hydro_power_plant = None
        self.hydro_power_plant = hydro_power_plant

        self._penstock_loss_curve = None
        self.penstock_loss_curve = penstock_loss_curve

        self._hydro_generating_efficiency_curves = []
        if hydro_generating_efficiency_curves is not None:
            self.hydro_generating_efficiency_curves = hydro_generating_efficiency_curves
        else:
            self.hydro_generating_efficiency_curves = []


        super(HydroGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> hydro_generating_unit

    # <<< tailbay_loss_curve
    # @generated
    def get_tailbay_loss_curve(self):
        """ A hydro generating unit has a tailbay loss curve
        """
        return self._tailbay_loss_curve

    def set_tailbay_loss_curve(self, value):
        for x in self._tailbay_loss_curve:
            x._hydro_generating_unit = None
        for y in value:
            y._hydro_generating_unit = self
        self._tailbay_loss_curve = value

    tailbay_loss_curve = property(get_tailbay_loss_curve, set_tailbay_loss_curve)

    def add_tailbay_loss_curve(self, *tailbay_loss_curve):
        for obj in tailbay_loss_curve:
            obj._hydro_generating_unit = self
            self._tailbay_loss_curve.append(obj)

    def remove_tailbay_loss_curve(self, *tailbay_loss_curve):
        for obj in tailbay_loss_curve:
            obj._hydro_generating_unit = None
            self._tailbay_loss_curve.remove(obj)
    # >>> tailbay_loss_curve

    # <<< hydro_power_plant
    # @generated
    def get_hydro_power_plant(self):
        """ The hydro generating unit belongs to a hydro power plant
        """
        return self._hydro_power_plant

    def set_hydro_power_plant(self, value):
        if self._hydro_power_plant is not None:
            filtered = [x for x in self.hydro_power_plant.hydro_generating_units if x != self]
            self._hydro_power_plant._hydro_generating_units = filtered

        self._hydro_power_plant = value
        if self._hydro_power_plant is not None:
            self._hydro_power_plant._hydro_generating_units.append(self)

    hydro_power_plant = property(get_hydro_power_plant, set_hydro_power_plant)
    # >>> hydro_power_plant

    # <<< penstock_loss_curve
    # @generated
    def get_penstock_loss_curve(self):
        """ A hydro generating unit has a penstock loss curve
        """
        return self._penstock_loss_curve

    def set_penstock_loss_curve(self, value):
        if self._penstock_loss_curve is not None:
            self._penstock_loss_curve._hydro_generating_unit = None

        self._penstock_loss_curve = value
        if self._penstock_loss_curve is not None:
            self._penstock_loss_curve._hydro_generating_unit = self

    penstock_loss_curve = property(get_penstock_loss_curve, set_penstock_loss_curve)
    # >>> penstock_loss_curve

    # <<< hydro_generating_efficiency_curves
    # @generated
    def get_hydro_generating_efficiency_curves(self):
        """ A hydro generating unit has an efficiency curve
        """
        return self._hydro_generating_efficiency_curves

    def set_hydro_generating_efficiency_curves(self, value):
        for x in self._hydro_generating_efficiency_curves:
            x._hydro_generating_unit = None
        for y in value:
            y._hydro_generating_unit = self
        self._hydro_generating_efficiency_curves = value

    hydro_generating_efficiency_curves = property(get_hydro_generating_efficiency_curves, set_hydro_generating_efficiency_curves)

    def add_hydro_generating_efficiency_curves(self, *hydro_generating_efficiency_curves):
        for obj in hydro_generating_efficiency_curves:
            obj._hydro_generating_unit = self
            self._hydro_generating_efficiency_curves.append(obj)

    def remove_hydro_generating_efficiency_curves(self, *hydro_generating_efficiency_curves):
        for obj in hydro_generating_efficiency_curves:
            obj._hydro_generating_unit = None
            self._hydro_generating_efficiency_curves.remove(obj)
    # >>> hydro_generating_efficiency_curves



# <<< production
# @generated
# >>> production
