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

""" The Generation Dynamics package contains prime movers, such as turbines and boilers, which are needed for simulation and educational purposes.
"""

from cim14v13.iec61970.core import PowerSystemResource
from cim14v13.iec61970.core import Curve

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimGenerationDynamics"

ns_uri = "http://iec.ch/TC57/CIM-generic#GenerationDynamics"

class SteamSupply(PowerSystemResource):
    """ Steam supply for steam turbine
    """
    # <<< steam_supply
    # @generated
    def __init__(self, steam_supply_rating=0.0, steam_turbines=None, *args, **kw_args):
        """ Initialises a new 'SteamSupply' instance.

        @param steam_supply_rating: Rating of steam supply 
        @param steam_turbines: Steam turbines may have steam supplied by a steam supply
        """
        # Rating of steam supply 
        self.steam_supply_rating = steam_supply_rating


        self._steam_turbines = []
        if steam_turbines is not None:
            self.steam_turbines = steam_turbines
        else:
            self.steam_turbines = []


        super(SteamSupply, self).__init__(*args, **kw_args)
    # >>> steam_supply

    # <<< steam_turbines
    # @generated
    def get_steam_turbines(self):
        """ Steam turbines may have steam supplied by a steam supply
        """
        return self._steam_turbines

    def set_steam_turbines(self, value):
        for p in self._steam_turbines:
            filtered = [q for q in p.steam_supplys if q != self]
            self._steam_turbines._steam_supplys = filtered
        for r in value:
            if self not in r._steam_supplys:
                r._steam_supplys.append(self)
        self._steam_turbines = value

    steam_turbines = property(get_steam_turbines, set_steam_turbines)

    def add_steam_turbines(self, *steam_turbines):
        for obj in steam_turbines:
            if self not in obj._steam_supplys:
                obj._steam_supplys.append(self)
            self._steam_turbines.append(obj)

    def remove_steam_turbines(self, *steam_turbines):
        for obj in steam_turbines:
            if self in obj._steam_supplys:
                obj._steam_supplys.remove(self)
            self._steam_turbines.remove(obj)
    # >>> steam_turbines



class PrimeMover(PowerSystemResource):
    """ The machine used to develop mechanical energy used to drive a generator.
    """
    # <<< prime_mover
    # @generated
    def __init__(self, prime_mover_rating=0.0, synchronous_machines=None, *args, **kw_args):
        """ Initialises a new 'PrimeMover' instance.

        @param prime_mover_rating: Rating of prime mover 
        @param synchronous_machines: Synchronous machines this Prime mover drives.
        """
        # Rating of prime mover 
        self.prime_mover_rating = prime_mover_rating


        self._synchronous_machines = []
        if synchronous_machines is not None:
            self.synchronous_machines = synchronous_machines
        else:
            self.synchronous_machines = []


        super(PrimeMover, self).__init__(*args, **kw_args)
    # >>> prime_mover

    # <<< synchronous_machines
    # @generated
    def get_synchronous_machines(self):
        """ Synchronous machines this Prime mover drives.
        """
        return self._synchronous_machines

    def set_synchronous_machines(self, value):
        for p in self._synchronous_machines:
            filtered = [q for q in p.prime_movers if q != self]
            self._synchronous_machines._prime_movers = filtered
        for r in value:
            if self not in r._prime_movers:
                r._prime_movers.append(self)
        self._synchronous_machines = value

    synchronous_machines = property(get_synchronous_machines, set_synchronous_machines)

    def add_synchronous_machines(self, *synchronous_machines):
        for obj in synchronous_machines:
            if self not in obj._prime_movers:
                obj._prime_movers.append(self)
            self._synchronous_machines.append(obj)

    def remove_synchronous_machines(self, *synchronous_machines):
        for obj in synchronous_machines:
            if self in obj._prime_movers:
                obj._prime_movers.remove(self)
            self._synchronous_machines.remove(obj)
    # >>> synchronous_machines



class CTTempActivePowerCurve(Curve):
    """ Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """
    # <<< cttemp_active_power_curve
    # @generated
    def __init__(self, combustion_turbine=None, *args, **kw_args):
        """ Initialises a new 'CTTempActivePowerCurve' instance.

        @param combustion_turbine: A combustion turbine may have an active power versus ambient temperature relationship
        """

        self._combustion_turbine = None
        self.combustion_turbine = combustion_turbine


        super(CTTempActivePowerCurve, self).__init__(*args, **kw_args)
    # >>> cttemp_active_power_curve

    # <<< combustion_turbine
    # @generated
    def get_combustion_turbine(self):
        """ A combustion turbine may have an active power versus ambient temperature relationship
        """
        return self._combustion_turbine

    def set_combustion_turbine(self, value):
        if self._combustion_turbine is not None:
            self._combustion_turbine._cttemp_active_power_curve = None

        self._combustion_turbine = value
        if self._combustion_turbine is not None:
            self._combustion_turbine._cttemp_active_power_curve = self

    combustion_turbine = property(get_combustion_turbine, set_combustion_turbine)
    # >>> combustion_turbine



class FossilSteamSupply(SteamSupply):
    """ Fossil fueled boiler (e.g., coal, oil, gas)
    """
    # <<< fossil_steam_supply
    # @generated
    def __init__(self, boiler_control_mode='following', fuel_supply_tc=0.0, pressure_ctrl_dg=0.0, super_heater2_capacity=0.0, control_tc=0.0, control_error_bias_p=0.0, pressure_ctrl_pg=0.0, pressure_ctrl_ig=0.0, feed_water_ig=0.0, super_heater1_capacity=0.0, mech_power_sensor_lag=0.0, control_ic=0.0, control_pc=0.0, pressure_feedback=0, feed_water_pg=0.0, fuel_demand_limit=0.0, control_ped=0.0, aux_power_versus_frequency=0.0, aux_power_versus_voltage=0.0, max_error_rate_p=0.0, fuel_supply_delay=0.0, super_heater_pipe_pd=0.0, control_peb=0.0, feed_water_tc=0.0, throttle_pressure_sp=0.0, min_error_rate_p=0.0, *args, **kw_args):
        """ Initialises a new 'FossilSteamSupply' instance.

        @param boiler_control_mode: The control mode of the boiler Values are: "following", "coordinated"
        @param fuel_supply_tc: Fuel Supply Time Constant 
        @param pressure_ctrl_dg: Pressure Control Derivative Gain ratio 
        @param super_heater2_capacity: Secondary Superheater Capacity 
        @param control_tc: Time Constant 
        @param control_error_bias_p: Active power Error Bias ratio 
        @param pressure_ctrl_pg: Pressure Control Proportional Gain ratio 
        @param pressure_ctrl_ig: Pressure Control Integral Gain ratio 
        @param feed_water_ig: Feedwater Integral Gain ratio 
        @param super_heater1_capacity: Drum/Primary Superheater Capacity 
        @param mech_power_sensor_lag: Mechanical Power Sensor Lag 
        @param control_ic: Integral Constant 
        @param control_pc: Proportional Constant 
        @param pressure_feedback: Pressure Feedback Indicator 
        @param feed_water_pg: Feedwater Proportional Gain ratio 
        @param fuel_demand_limit: Fuel Demand Limit 
        @param control_ped: Pressure Error Deadband 
        @param aux_power_versus_frequency: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        @param aux_power_versus_voltage: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        @param max_error_rate_p: Active power Maximum Error Rate Limit 
        @param fuel_supply_delay: Fuel Delay 
        @param super_heater_pipe_pd: Superheater Pipe Pressure Drop Constant 
        @param control_peb: Pressure Error Bias ratio 
        @param feed_water_tc: Feedwater Time Constant rato 
        @param throttle_pressure_sp: Throttle Pressure Setpoint 
        @param min_error_rate_p: Active power Minimum Error Rate Limit 
        """
        # The control mode of the boiler Values are: "following", "coordinated"
        self.boiler_control_mode = boiler_control_mode

        # Fuel Supply Time Constant 
        self.fuel_supply_tc = fuel_supply_tc

        # Pressure Control Derivative Gain ratio 
        self.pressure_ctrl_dg = pressure_ctrl_dg

        # Secondary Superheater Capacity 
        self.super_heater2_capacity = super_heater2_capacity

        # Time Constant 
        self.control_tc = control_tc

        # Active power Error Bias ratio 
        self.control_error_bias_p = control_error_bias_p

        # Pressure Control Proportional Gain ratio 
        self.pressure_ctrl_pg = pressure_ctrl_pg

        # Pressure Control Integral Gain ratio 
        self.pressure_ctrl_ig = pressure_ctrl_ig

        # Feedwater Integral Gain ratio 
        self.feed_water_ig = feed_water_ig

        # Drum/Primary Superheater Capacity 
        self.super_heater1_capacity = super_heater1_capacity

        # Mechanical Power Sensor Lag 
        self.mech_power_sensor_lag = mech_power_sensor_lag

        # Integral Constant 
        self.control_ic = control_ic

        # Proportional Constant 
        self.control_pc = control_pc

        # Pressure Feedback Indicator 
        self.pressure_feedback = pressure_feedback

        # Feedwater Proportional Gain ratio 
        self.feed_water_pg = feed_water_pg

        # Fuel Demand Limit 
        self.fuel_demand_limit = fuel_demand_limit

        # Pressure Error Deadband 
        self.control_ped = control_ped

        # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        self.aux_power_versus_frequency = aux_power_versus_frequency

        # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        self.aux_power_versus_voltage = aux_power_versus_voltage

        # Active power Maximum Error Rate Limit 
        self.max_error_rate_p = max_error_rate_p

        # Fuel Delay 
        self.fuel_supply_delay = fuel_supply_delay

        # Superheater Pipe Pressure Drop Constant 
        self.super_heater_pipe_pd = super_heater_pipe_pd

        # Pressure Error Bias ratio 
        self.control_peb = control_peb

        # Feedwater Time Constant rato 
        self.feed_water_tc = feed_water_tc

        # Throttle Pressure Setpoint 
        self.throttle_pressure_sp = throttle_pressure_sp

        # Active power Minimum Error Rate Limit 
        self.min_error_rate_p = min_error_rate_p



        super(FossilSteamSupply, self).__init__(*args, **kw_args)
    # >>> fossil_steam_supply



class HeatRecoveryBoiler(FossilSteamSupply):
    """ The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """
    # <<< heat_recovery_boiler
    # @generated
    def __init__(self, steam_supply_rating2=0.0, combustion_turbines=None, *args, **kw_args):
        """ Initialises a new 'HeatRecoveryBoiler' instance.

        @param steam_supply_rating2: The steam supply rating in kilopounds per hour, if dual pressure boiler 
        @param combustion_turbines: A combustion turbine may have a heat recovery boiler for making steam
        """
        # The steam supply rating in kilopounds per hour, if dual pressure boiler 
        self.steam_supply_rating2 = steam_supply_rating2


        self._combustion_turbines = []
        if combustion_turbines is not None:
            self.combustion_turbines = combustion_turbines
        else:
            self.combustion_turbines = []


        super(HeatRecoveryBoiler, self).__init__(*args, **kw_args)
    # >>> heat_recovery_boiler

    # <<< combustion_turbines
    # @generated
    def get_combustion_turbines(self):
        """ A combustion turbine may have a heat recovery boiler for making steam
        """
        return self._combustion_turbines

    def set_combustion_turbines(self, value):
        for x in self._combustion_turbines:
            x._heat_recovery_boiler = None
        for y in value:
            y._heat_recovery_boiler = self
        self._combustion_turbines = value

    combustion_turbines = property(get_combustion_turbines, set_combustion_turbines)

    def add_combustion_turbines(self, *combustion_turbines):
        for obj in combustion_turbines:
            obj._heat_recovery_boiler = self
            self._combustion_turbines.append(obj)

    def remove_combustion_turbines(self, *combustion_turbines):
        for obj in combustion_turbines:
            obj._heat_recovery_boiler = None
            self._combustion_turbines.remove(obj)
    # >>> combustion_turbines



class HydroTurbine(PrimeMover):
    """ A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """
    # <<< hydro_turbine
    # @generated
    def __init__(self, turbine_type='francis', speed_rating=0.0, speed_regulation=0.0, turbine_rating=0.0, transient_droop_time=0.0, min_head_max_p=0.0, transient_regulation=0.0, gate_rate_limit=0.0, max_head_max_p=0.0, water_starting_time=0.0, gate_upper_limit=0.0, *args, **kw_args):
        """ Initialises a new 'HydroTurbine' instance.

        @param turbine_type: Type of turbine. Values are: "francis", "kaplan", "pelton"
        @param speed_rating: Rated speed in number of revolutions. 
        @param speed_regulation: Speed Regulation 
        @param turbine_rating: Rated turbine active power 
        @param transient_droop_time: Transient Droop Time Constant 
        @param min_head_max_p: Maximum efficiency active power at minimum head conditions 
        @param transient_regulation: Transient Regulation 
        @param gate_rate_limit: Gate Rate Limit 
        @param max_head_max_p: Maximum efficiency active power at maximum head conditions 
        @param water_starting_time: Water Starting Time 
        @param gate_upper_limit: Gate Upper Limit 
        """
        # Type of turbine. Values are: "francis", "kaplan", "pelton"
        self.turbine_type = turbine_type

        # Rated speed in number of revolutions. 
        self.speed_rating = speed_rating

        # Speed Regulation 
        self.speed_regulation = speed_regulation

        # Rated turbine active power 
        self.turbine_rating = turbine_rating

        # Transient Droop Time Constant 
        self.transient_droop_time = transient_droop_time

        # Maximum efficiency active power at minimum head conditions 
        self.min_head_max_p = min_head_max_p

        # Transient Regulation 
        self.transient_regulation = transient_regulation

        # Gate Rate Limit 
        self.gate_rate_limit = gate_rate_limit

        # Maximum efficiency active power at maximum head conditions 
        self.max_head_max_p = max_head_max_p

        # Water Starting Time 
        self.water_starting_time = water_starting_time

        # Gate Upper Limit 
        self.gate_upper_limit = gate_upper_limit



        super(HydroTurbine, self).__init__(*args, **kw_args)
    # >>> hydro_turbine



class Subcritical(FossilSteamSupply):
    """ Once-through subcritical boiler
    """
    pass
    # <<< subcritical
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Subcritical' instance.

        """


        super(Subcritical, self).__init__(*args, **kw_args)
    # >>> subcritical



class BWRSteamSupply(SteamSupply):
    """ Boiling water reactor used as a steam supply to a steam turbine
    """
    # <<< bwrsteam_supply
    # @generated
    def __init__(self, proportional_gain=0.0, rf_aux3=0.0, rod_pattern_constant=0.0, rf_aux4=0.0, pressure_setpoint_ga=0.0, in_core_thermal_tc=0.0, rf_aux2=0.0, pressure_limit=0.0, rf_aux1=0.0, rf_aux7=0.0, high_power_limit=0.0, low_power_limit=0.0, lower_limit=0.0, upper_limit=0.0, pressure_setpoint_tc1=0.0, rod_pattern=0.0, rf_aux8=0.0, rf_aux5=0.0, integral_gain=0.0, pressure_setpoint_tc2=0.0, rf_aux6=0.0, *args, **kw_args):
        """ Initialises a new 'BWRSteamSupply' instance.

        @param proportional_gain: Proportional Gain 
        @param rf_aux3: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rod_pattern_constant: Constant Associated With Rod Pattern 
        @param rf_aux4: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressure_setpoint_ga: Pressure Setpoint Gain Adjuster 
        @param in_core_thermal_tc: In-Core Thermal Time Constant 
        @param rf_aux2: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressure_limit: Pressure Limit 
        @param rf_aux1: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rf_aux7: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param high_power_limit: High Power Limit 
        @param low_power_limit: Low Power Limit 
        @param lower_limit: Initial Lower Limit 
        @param upper_limit: Initial Upper Limit 
        @param pressure_setpoint_tc1: Pressure Setpoint Time Constant 
        @param rod_pattern: Rod Pattern 
        @param rf_aux8: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rf_aux5: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param integral_gain: Integral Gain 
        @param pressure_setpoint_tc2: Pressure Setpoint Time Constant 
        @param rf_aux6: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        """
        # Proportional Gain 
        self.proportional_gain = proportional_gain

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux3 = rf_aux3

        # Constant Associated With Rod Pattern 
        self.rod_pattern_constant = rod_pattern_constant

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux4 = rf_aux4

        # Pressure Setpoint Gain Adjuster 
        self.pressure_setpoint_ga = pressure_setpoint_ga

        # In-Core Thermal Time Constant 
        self.in_core_thermal_tc = in_core_thermal_tc

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux2 = rf_aux2

        # Pressure Limit 
        self.pressure_limit = pressure_limit

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux1 = rf_aux1

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux7 = rf_aux7

        # High Power Limit 
        self.high_power_limit = high_power_limit

        # Low Power Limit 
        self.low_power_limit = low_power_limit

        # Initial Lower Limit 
        self.lower_limit = lower_limit

        # Initial Upper Limit 
        self.upper_limit = upper_limit

        # Pressure Setpoint Time Constant 
        self.pressure_setpoint_tc1 = pressure_setpoint_tc1

        # Rod Pattern 
        self.rod_pattern = rod_pattern

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux8 = rf_aux8

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux5 = rf_aux5

        # Integral Gain 
        self.integral_gain = integral_gain

        # Pressure Setpoint Time Constant 
        self.pressure_setpoint_tc2 = pressure_setpoint_tc2

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux6 = rf_aux6



        super(BWRSteamSupply, self).__init__(*args, **kw_args)
    # >>> bwrsteam_supply



class DrumBoiler(FossilSteamSupply):
    """ Drum boiler
    """
    # <<< drum_boiler
    # @generated
    def __init__(self, drum_boiler_rating=0.0, *args, **kw_args):
        """ Initialises a new 'DrumBoiler' instance.

        @param drum_boiler_rating: Rating of drum boiler in steam units 
        """
        # Rating of drum boiler in steam units 
        self.drum_boiler_rating = drum_boiler_rating



        super(DrumBoiler, self).__init__(*args, **kw_args)
    # >>> drum_boiler



class CombustionTurbine(PrimeMover):
    """ A prime mover that is typically fueled by gas or light oil
    """
    # <<< combustion_turbine
    # @generated
    def __init__(self, aux_power_versus_voltage=0.0, ambient_temp=0.0, heat_recovery_flag=False, capability_versus_frequency=0.0, power_variation_by_temp=0.0, reference_temp=0.0, time_constant=0.0, aux_power_versus_frequency=0.0, heat_recovery_boiler=None, cttemp_active_power_curve=None, air_compressor=None, *args, **kw_args):
        """ Initialises a new 'CombustionTurbine' instance.

        @param aux_power_versus_voltage: Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level). 
        @param ambient_temp: Default ambient temperature to be used in modeling applications 
        @param heat_recovery_flag: Flag that is set to true if the combustion turbine is associated with a heat recovery boiler 
        @param capability_versus_frequency: Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency). 
        @param power_variation_by_temp: Per unit change in power per (versus) unit change in ambient temperature 
        @param reference_temp: Reference temperature at which the output of the turbine was defined. 
        @param time_constant: The time constant for the turbine. 
        @param aux_power_versus_frequency: Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency). 
        @param heat_recovery_boiler: A combustion turbine may have a heat recovery boiler for making steam
        @param cttemp_active_power_curve: A combustion turbine may have an active power versus ambient temperature relationship
        @param air_compressor: A CAES air compressor is driven by combustion turbine
        """
        # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level). 
        self.aux_power_versus_voltage = aux_power_versus_voltage

        # Default ambient temperature to be used in modeling applications 
        self.ambient_temp = ambient_temp

        # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler 
        self.heat_recovery_flag = heat_recovery_flag

        # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency). 
        self.capability_versus_frequency = capability_versus_frequency

        # Per unit change in power per (versus) unit change in ambient temperature 
        self.power_variation_by_temp = power_variation_by_temp

        # Reference temperature at which the output of the turbine was defined. 
        self.reference_temp = reference_temp

        # The time constant for the turbine. 
        self.time_constant = time_constant

        # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency). 
        self.aux_power_versus_frequency = aux_power_versus_frequency


        self._heat_recovery_boiler = None
        self.heat_recovery_boiler = heat_recovery_boiler

        self._cttemp_active_power_curve = None
        self.cttemp_active_power_curve = cttemp_active_power_curve

        self._air_compressor = None
        self.air_compressor = air_compressor


        super(CombustionTurbine, self).__init__(*args, **kw_args)
    # >>> combustion_turbine

    # <<< heat_recovery_boiler
    # @generated
    def get_heat_recovery_boiler(self):
        """ A combustion turbine may have a heat recovery boiler for making steam
        """
        return self._heat_recovery_boiler

    def set_heat_recovery_boiler(self, value):
        if self._heat_recovery_boiler is not None:
            filtered = [x for x in self.heat_recovery_boiler.combustion_turbines if x != self]
            self._heat_recovery_boiler._combustion_turbines = filtered

        self._heat_recovery_boiler = value
        if self._heat_recovery_boiler is not None:
            self._heat_recovery_boiler._combustion_turbines.append(self)

    heat_recovery_boiler = property(get_heat_recovery_boiler, set_heat_recovery_boiler)
    # >>> heat_recovery_boiler

    # <<< cttemp_active_power_curve
    # @generated
    def get_cttemp_active_power_curve(self):
        """ A combustion turbine may have an active power versus ambient temperature relationship
        """
        return self._cttemp_active_power_curve

    def set_cttemp_active_power_curve(self, value):
        if self._cttemp_active_power_curve is not None:
            self._cttemp_active_power_curve._combustion_turbine = None

        self._cttemp_active_power_curve = value
        if self._cttemp_active_power_curve is not None:
            self._cttemp_active_power_curve._combustion_turbine = self

    cttemp_active_power_curve = property(get_cttemp_active_power_curve, set_cttemp_active_power_curve)
    # >>> cttemp_active_power_curve

    # <<< air_compressor
    # @generated
    def get_air_compressor(self):
        """ A CAES air compressor is driven by combustion turbine
        """
        return self._air_compressor

    def set_air_compressor(self, value):
        if self._air_compressor is not None:
            self._air_compressor._combustion_turbine = None

        self._air_compressor = value
        if self._air_compressor is not None:
            self._air_compressor._combustion_turbine = self

    air_compressor = property(get_air_compressor, set_air_compressor)
    # >>> air_compressor



class Supercritical(FossilSteamSupply):
    """ Once-through supercritical boiler
    """
    pass
    # <<< supercritical
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Supercritical' instance.

        """


        super(Supercritical, self).__init__(*args, **kw_args)
    # >>> supercritical



class PWRSteamSupply(SteamSupply):
    """ Pressurized water reactor used as a steam supply to a steam turbine
    """
    # <<< pwrsteam_supply
    # @generated
    def __init__(self, core_htlag_tc1=0.0, hot_leg_steam_gain=0.0, cold_leg_lag_tc=0.0, core_neutronics_eff_tc=0.0, steam_flow_fg=0.0, throttle_pressure_factor=0.0, hot_leg_to_cold_leg_gain=0.0, throttle_pressure_sp=0.0, steam_pressure_drop_lag_tc=0.0, core_htlag_tc2=0.0, cold_leg_fg1=0.0, cold_leg_fblag_tc=0.0, hot_leg_lag_tc=0.0, cold_leg_fblead_tc2=0.0, pressure_cg=0.0, cold_leg_fblead_tc1=0.0, cold_leg_fg2=0.0, core_neutronics_ht=0.0, steam_pressure_fg=0.0, feedback_factor=0.0, *args, **kw_args):
        """ Initialises a new 'PWRSteamSupply' instance.

        @param core_htlag_tc1: Core Heat Transfer Lag Time Constant 
        @param hot_leg_steam_gain: Hot Leg Steam Gain 
        @param cold_leg_lag_tc: Cold Leg Lag Time Constant 
        @param core_neutronics_eff_tc: Core Neutronics Effective Time Constant 
        @param steam_flow_fg: Steam Flow Feedback Gain 
        @param throttle_pressure_factor: Throttle Pressure Factor 
        @param hot_leg_to_cold_leg_gain: Hot Leg To Cold Leg Gain 
        @param throttle_pressure_sp: Throttle Pressure Setpoint 
        @param steam_pressure_drop_lag_tc: Steam Pressure Drop Lag Time Constant 
        @param core_htlag_tc2: Core Heat Transfer Lag Time Constant 
        @param cold_leg_fg1: Cold Leg Feedback Gain 1 
        @param cold_leg_fblag_tc: Cold Leg Feedback Lag Time Constant 
        @param hot_leg_lag_tc: Hot Leg Lag Time Constant 
        @param cold_leg_fblead_tc2: Cold Leg Feedback Lead Time Constant 
        @param pressure_cg: Pressure Control Gain 
        @param cold_leg_fblead_tc1: Cold Leg Feedback Lead Time Constant 
        @param cold_leg_fg2: Cold Leg Feedback Gain 2 
        @param core_neutronics_ht: Core Neutronics And Heat Transfer 
        @param steam_pressure_fg: Steam Pressure Feedback Gain 
        @param feedback_factor: Feedback Factor 
        """
        # Core Heat Transfer Lag Time Constant 
        self.core_htlag_tc1 = core_htlag_tc1

        # Hot Leg Steam Gain 
        self.hot_leg_steam_gain = hot_leg_steam_gain

        # Cold Leg Lag Time Constant 
        self.cold_leg_lag_tc = cold_leg_lag_tc

        # Core Neutronics Effective Time Constant 
        self.core_neutronics_eff_tc = core_neutronics_eff_tc

        # Steam Flow Feedback Gain 
        self.steam_flow_fg = steam_flow_fg

        # Throttle Pressure Factor 
        self.throttle_pressure_factor = throttle_pressure_factor

        # Hot Leg To Cold Leg Gain 
        self.hot_leg_to_cold_leg_gain = hot_leg_to_cold_leg_gain

        # Throttle Pressure Setpoint 
        self.throttle_pressure_sp = throttle_pressure_sp

        # Steam Pressure Drop Lag Time Constant 
        self.steam_pressure_drop_lag_tc = steam_pressure_drop_lag_tc

        # Core Heat Transfer Lag Time Constant 
        self.core_htlag_tc2 = core_htlag_tc2

        # Cold Leg Feedback Gain 1 
        self.cold_leg_fg1 = cold_leg_fg1

        # Cold Leg Feedback Lag Time Constant 
        self.cold_leg_fblag_tc = cold_leg_fblag_tc

        # Hot Leg Lag Time Constant 
        self.hot_leg_lag_tc = hot_leg_lag_tc

        # Cold Leg Feedback Lead Time Constant 
        self.cold_leg_fblead_tc2 = cold_leg_fblead_tc2

        # Pressure Control Gain 
        self.pressure_cg = pressure_cg

        # Cold Leg Feedback Lead Time Constant 
        self.cold_leg_fblead_tc1 = cold_leg_fblead_tc1

        # Cold Leg Feedback Gain 2 
        self.cold_leg_fg2 = cold_leg_fg2

        # Core Neutronics And Heat Transfer 
        self.core_neutronics_ht = core_neutronics_ht

        # Steam Pressure Feedback Gain 
        self.steam_pressure_fg = steam_pressure_fg

        # Feedback Factor 
        self.feedback_factor = feedback_factor



        super(PWRSteamSupply, self).__init__(*args, **kw_args)
    # >>> pwrsteam_supply



class SteamTurbine(PrimeMover):
    """ Steam turbine
    """
    # <<< steam_turbine
    # @generated
    def __init__(self, crossover_tc=0.0, shaft2_power_lp1=0.0, shaft1_power_ip=0.0, shaft2_power_ip=0.0, reheater1_tc=0.0, shaft2_power_lp2=0.0, steam_chest_tc=0.0, shaft1_power_hp=0.0, shaft1_power_lp2=0.0, shaft2_power_hp=0.0, reheater2_tc=0.0, shaft1_power_lp1=0.0, steam_supplys=None, *args, **kw_args):
        """ Initialises a new 'SteamTurbine' instance.

        @param crossover_tc: Crossover Time Constant 
        @param shaft2_power_lp1: Fraction Of Power From Shaft 2 First Low Pressure Turbine output 
        @param shaft1_power_ip: Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output 
        @param shaft2_power_ip: Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output 
        @param reheater1_tc: First Reheater Time Constant 
        @param shaft2_power_lp2: Fraction Of Power From Shaft 2 Second Low Pressure Turbine output 
        @param steam_chest_tc: Steam Chest Time Constant 
        @param shaft1_power_hp: Fraction Of Power From Shaft 1 High Pressure Turbine output 
        @param shaft1_power_lp2: Fraction Of Power From Shaft 1 Second Low Pressure Turbine output 
        @param shaft2_power_hp: Fraction Of Power From Shaft 2 High Pressure Turbine output 
        @param reheater2_tc: Second Reheater Time Constant 
        @param shaft1_power_lp1: Fraction Of Power From Shaft 1 First Low Pressure Turbine output 
        @param steam_supplys: Steam turbines may have steam supplied by a steam supply
        """
        # Crossover Time Constant 
        self.crossover_tc = crossover_tc

        # Fraction Of Power From Shaft 2 First Low Pressure Turbine output 
        self.shaft2_power_lp1 = shaft2_power_lp1

        # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output 
        self.shaft1_power_ip = shaft1_power_ip

        # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output 
        self.shaft2_power_ip = shaft2_power_ip

        # First Reheater Time Constant 
        self.reheater1_tc = reheater1_tc

        # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output 
        self.shaft2_power_lp2 = shaft2_power_lp2

        # Steam Chest Time Constant 
        self.steam_chest_tc = steam_chest_tc

        # Fraction Of Power From Shaft 1 High Pressure Turbine output 
        self.shaft1_power_hp = shaft1_power_hp

        # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output 
        self.shaft1_power_lp2 = shaft1_power_lp2

        # Fraction Of Power From Shaft 2 High Pressure Turbine output 
        self.shaft2_power_hp = shaft2_power_hp

        # Second Reheater Time Constant 
        self.reheater2_tc = reheater2_tc

        # Fraction Of Power From Shaft 1 First Low Pressure Turbine output 
        self.shaft1_power_lp1 = shaft1_power_lp1


        self._steam_supplys = []
        if steam_supplys is not None:
            self.steam_supplys = steam_supplys
        else:
            self.steam_supplys = []


        super(SteamTurbine, self).__init__(*args, **kw_args)
    # >>> steam_turbine

    # <<< steam_supplys
    # @generated
    def get_steam_supplys(self):
        """ Steam turbines may have steam supplied by a steam supply
        """
        return self._steam_supplys

    def set_steam_supplys(self, value):
        for p in self._steam_supplys:
            filtered = [q for q in p.steam_turbines if q != self]
            self._steam_supplys._steam_turbines = filtered
        for r in value:
            if self not in r._steam_turbines:
                r._steam_turbines.append(self)
        self._steam_supplys = value

    steam_supplys = property(get_steam_supplys, set_steam_supplys)

    def add_steam_supplys(self, *steam_supplys):
        for obj in steam_supplys:
            if self not in obj._steam_turbines:
                obj._steam_turbines.append(self)
            self._steam_supplys.append(obj)

    def remove_steam_supplys(self, *steam_supplys):
        for obj in steam_supplys:
            if self in obj._steam_turbines:
                obj._steam_turbines.remove(self)
            self._steam_supplys.remove(obj)
    # >>> steam_supplys



# <<< generation_dynamics
# @generated
# >>> generation_dynamics
