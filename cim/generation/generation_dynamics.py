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

""" The Generation Dynamics package contains prime movers, such as turbines and boilers, which are needed for simulation and educational purposes.
"""

from cim.core import PowerSystemResource
from cim.core import Curve

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
    def __init__(self, steam_supply_rating=0.0, steam_turbines=None, **kw_args):
        """ Initialises a new 'SteamSupply' instance.
        """
        # Rating of steam supply 
        self.steam_supply_rating = steam_supply_rating


        self._steam_turbines = []
        if steam_turbines is not None:
            self.steam_turbines = steam_turbines
        else:
            self.steam_turbines = []


        super(SteamSupply, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the SteamSupply.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< steam_supply.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SteamSupply.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SteamSupply", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SteamSupply")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> steam_supply.serialize


class PrimeMover(PowerSystemResource):
    """ The machine used to develop mechanical energy used to drive a generator.
    """
    # <<< prime_mover
    # @generated
    def __init__(self, prime_mover_rating=0.0, drives_synchronous_machines=None, **kw_args):
        """ Initialises a new 'PrimeMover' instance.
        """
        # Rating of prime mover 
        self.prime_mover_rating = prime_mover_rating


        self._drives_synchronous_machines = []
        if drives_synchronous_machines is not None:
            self.drives_synchronous_machines = drives_synchronous_machines
        else:
            self.drives_synchronous_machines = []


        super(PrimeMover, self).__init__(**kw_args)
    # >>> prime_mover

    # <<< drives_synchronous_machines
    # @generated
    def get_drives_synchronous_machines(self):
        """ Synchronous machines this Prime mover drives.
        """
        return self._drives_synchronous_machines

    def set_drives_synchronous_machines(self, value):
        for p in self._drives_synchronous_machines:
            filtered = [q for q in p.driven_by_prime_mover if q != self]
            self._drives_synchronous_machines._driven_by_prime_mover = filtered
        for r in value:
            if self not in r._driven_by_prime_mover:
                r._driven_by_prime_mover.append(self)
        self._drives_synchronous_machines = value

    drives_synchronous_machines = property(get_drives_synchronous_machines, set_drives_synchronous_machines)

    def add_drives_synchronous_machines(self, *drives_synchronous_machines):
        for obj in drives_synchronous_machines:
            if self not in obj._driven_by_prime_mover:
                obj._driven_by_prime_mover.append(self)
            self._drives_synchronous_machines.append(obj)

    def remove_drives_synchronous_machines(self, *drives_synchronous_machines):
        for obj in drives_synchronous_machines:
            if self in obj._driven_by_prime_mover:
                obj._driven_by_prime_mover.remove(self)
            self._drives_synchronous_machines.remove(obj)
    # >>> drives_synchronous_machines


    def __str__(self):
        """ Returns a string representation of the PrimeMover.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< prime_mover.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PrimeMover.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PrimeMover", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.drives_synchronous_machines:
            s += '%s<%s:PrimeMover.drives_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PrimeMover.prime_mover_rating>%s</%s:PrimeMover.prime_mover_rating>' % \
            (indent, ns_prefix, self.prime_mover_rating, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PrimeMover")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> prime_mover.serialize


class CTTempActivePowerCurve(Curve):
    """ Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """
    # <<< cttemp_active_power_curve
    # @generated
    def __init__(self, combustion_turbine=None, **kw_args):
        """ Initialises a new 'CTTempActivePowerCurve' instance.
        """

        self._combustion_turbine = None
        self.combustion_turbine = combustion_turbine


        super(CTTempActivePowerCurve, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the CTTempActivePowerCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< cttemp_active_power_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CTTempActivePowerCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CTTempActivePowerCurve", self.uri)
        if format:
            indent += ' ' * depth

        if self.combustion_turbine is not None:
            s += '%s<%s:CTTempActivePowerCurve.combustion_turbine rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.combustion_turbine.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.curve_schedule_datas:
            s += '%s<%s:Curve.curve_schedule_datas rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:Curve.y2_unit>%s</%s:Curve.y2_unit>' % \
            (indent, ns_prefix, self.y2_unit, ns_prefix)
        s += '%s<%s:Curve.y1_multiplier>%s</%s:Curve.y1_multiplier>' % \
            (indent, ns_prefix, self.y1_multiplier, ns_prefix)
        s += '%s<%s:Curve.curve_style>%s</%s:Curve.curve_style>' % \
            (indent, ns_prefix, self.curve_style, ns_prefix)
        s += '%s<%s:Curve.y2_multiplier>%s</%s:Curve.y2_multiplier>' % \
            (indent, ns_prefix, self.y2_multiplier, ns_prefix)
        s += '%s<%s:Curve.x_unit>%s</%s:Curve.x_unit>' % \
            (indent, ns_prefix, self.x_unit, ns_prefix)
        s += '%s<%s:Curve.y1_unit>%s</%s:Curve.y1_unit>' % \
            (indent, ns_prefix, self.y1_unit, ns_prefix)
        s += '%s<%s:Curve.x_multiplier>%s</%s:Curve.x_multiplier>' % \
            (indent, ns_prefix, self.x_multiplier, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CTTempActivePowerCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> cttemp_active_power_curve.serialize


class FossilSteamSupply(SteamSupply):
    """ Fossil fueled boiler (e.g., coal, oil, gas)
    """
    # <<< fossil_steam_supply
    # @generated
    def __init__(self, boiler_control_mode='coordinated', fuel_demand_limit=0.0, fuel_supply_delay=0.0, control_ic=0.0, feed_water_ig=0.0, super_heater1_capacity=0.0, throttle_pressure_sp=0.0, min_error_rate_p=0.0, feed_water_tc=0.0, super_heater2_capacity=0.0, control_peb=0.0, super_heater_pipe_pd=0.0, control_tc=0.0, control_ped=0.0, pressure_feedback=0, pressure_ctrl_pg=0.0, mech_power_sensor_lag=0.0, control_error_bias_p=0.0, aux_powerversus_voltage=0.0, control_pc=0.0, pressure_ctrl_dg=0.0, max_error_rate_p=0.0, pressure_ctrl_ig=0.0, aux_power_versus_frequency=0.0, feed_water_pg=0.0, fuel_supply_tc=0.0, **kw_args):
        """ Initialises a new 'FossilSteamSupply' instance.
        """
        # The control mode of the boiler Values are: "coordinated", "following"
        self.boiler_control_mode = 'coordinated'

        # Fuel Demand Limit 
        self.fuel_demand_limit = fuel_demand_limit

        # Fuel Delay 
        self.fuel_supply_delay = fuel_supply_delay

        # Integral Constant 
        self.control_ic = control_ic

        # Feedwater Integral Gain ratio 
        self.feed_water_ig = feed_water_ig

        # Drum/Primary Superheater Capacity 
        self.super_heater1_capacity = super_heater1_capacity

        # Throttle Pressure Setpoint 
        self.throttle_pressure_sp = throttle_pressure_sp

        # Active power Minimum Error Rate Limit 
        self.min_error_rate_p = min_error_rate_p

        # Feedwater Time Constant rato 
        self.feed_water_tc = feed_water_tc

        # Secondary Superheater Capacity 
        self.super_heater2_capacity = super_heater2_capacity

        # Pressure Error Bias ratio 
        self.control_peb = control_peb

        # Superheater Pipe Pressure Drop Constant 
        self.super_heater_pipe_pd = super_heater_pipe_pd

        # Time Constant 
        self.control_tc = control_tc

        # Pressure Error Deadband 
        self.control_ped = control_ped

        # Pressure Feedback Indicator 
        self.pressure_feedback = pressure_feedback

        # Pressure Control Proportional Gain ratio 
        self.pressure_ctrl_pg = pressure_ctrl_pg

        # Mechanical Power Sensor Lag 
        self.mech_power_sensor_lag = mech_power_sensor_lag

        # Active power Error Bias ratio 
        self.control_error_bias_p = control_error_bias_p

        # Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        self.aux_powerversus_voltage = aux_powerversus_voltage

        # Proportional Constant 
        self.control_pc = control_pc

        # Pressure Control Derivative Gain ratio 
        self.pressure_ctrl_dg = pressure_ctrl_dg

        # Active power Maximum Error Rate Limit 
        self.max_error_rate_p = max_error_rate_p

        # Pressure Control Integral Gain ratio 
        self.pressure_ctrl_ig = pressure_ctrl_ig

        # Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        self.aux_power_versus_frequency = aux_power_versus_frequency

        # Feedwater Proportional Gain ratio 
        self.feed_water_pg = feed_water_pg

        # Fuel Supply Time Constant 
        self.fuel_supply_tc = fuel_supply_tc



        super(FossilSteamSupply, self).__init__(**kw_args)
    # >>> fossil_steam_supply


    def __str__(self):
        """ Returns a string representation of the FossilSteamSupply.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< fossil_steam_supply.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FossilSteamSupply.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FossilSteamSupply", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:FossilSteamSupply.boiler_control_mode>%s</%s:FossilSteamSupply.boiler_control_mode>' % \
            (indent, ns_prefix, self.boiler_control_mode, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_demand_limit>%s</%s:FossilSteamSupply.fuel_demand_limit>' % \
            (indent, ns_prefix, self.fuel_demand_limit, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_delay>%s</%s:FossilSteamSupply.fuel_supply_delay>' % \
            (indent, ns_prefix, self.fuel_supply_delay, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ic>%s</%s:FossilSteamSupply.control_ic>' % \
            (indent, ns_prefix, self.control_ic, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_ig>%s</%s:FossilSteamSupply.feed_water_ig>' % \
            (indent, ns_prefix, self.feed_water_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater1_capacity>%s</%s:FossilSteamSupply.super_heater1_capacity>' % \
            (indent, ns_prefix, self.super_heater1_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.throttle_pressure_sp>%s</%s:FossilSteamSupply.throttle_pressure_sp>' % \
            (indent, ns_prefix, self.throttle_pressure_sp, ns_prefix)
        s += '%s<%s:FossilSteamSupply.min_error_rate_p>%s</%s:FossilSteamSupply.min_error_rate_p>' % \
            (indent, ns_prefix, self.min_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_tc>%s</%s:FossilSteamSupply.feed_water_tc>' % \
            (indent, ns_prefix, self.feed_water_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater2_capacity>%s</%s:FossilSteamSupply.super_heater2_capacity>' % \
            (indent, ns_prefix, self.super_heater2_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_peb>%s</%s:FossilSteamSupply.control_peb>' % \
            (indent, ns_prefix, self.control_peb, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater_pipe_pd>%s</%s:FossilSteamSupply.super_heater_pipe_pd>' % \
            (indent, ns_prefix, self.super_heater_pipe_pd, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_tc>%s</%s:FossilSteamSupply.control_tc>' % \
            (indent, ns_prefix, self.control_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ped>%s</%s:FossilSteamSupply.control_ped>' % \
            (indent, ns_prefix, self.control_ped, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_feedback>%s</%s:FossilSteamSupply.pressure_feedback>' % \
            (indent, ns_prefix, self.pressure_feedback, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_pg>%s</%s:FossilSteamSupply.pressure_ctrl_pg>' % \
            (indent, ns_prefix, self.pressure_ctrl_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.mech_power_sensor_lag>%s</%s:FossilSteamSupply.mech_power_sensor_lag>' % \
            (indent, ns_prefix, self.mech_power_sensor_lag, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_error_bias_p>%s</%s:FossilSteamSupply.control_error_bias_p>' % \
            (indent, ns_prefix, self.control_error_bias_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_powerversus_voltage>%s</%s:FossilSteamSupply.aux_powerversus_voltage>' % \
            (indent, ns_prefix, self.aux_powerversus_voltage, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_pc>%s</%s:FossilSteamSupply.control_pc>' % \
            (indent, ns_prefix, self.control_pc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_dg>%s</%s:FossilSteamSupply.pressure_ctrl_dg>' % \
            (indent, ns_prefix, self.pressure_ctrl_dg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.max_error_rate_p>%s</%s:FossilSteamSupply.max_error_rate_p>' % \
            (indent, ns_prefix, self.max_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_ig>%s</%s:FossilSteamSupply.pressure_ctrl_ig>' % \
            (indent, ns_prefix, self.pressure_ctrl_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_power_versus_frequency>%s</%s:FossilSteamSupply.aux_power_versus_frequency>' % \
            (indent, ns_prefix, self.aux_power_versus_frequency, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_pg>%s</%s:FossilSteamSupply.feed_water_pg>' % \
            (indent, ns_prefix, self.feed_water_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_tc>%s</%s:FossilSteamSupply.fuel_supply_tc>' % \
            (indent, ns_prefix, self.fuel_supply_tc, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FossilSteamSupply")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> fossil_steam_supply.serialize


class HeatRecoveryBoiler(FossilSteamSupply):
    """ The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """
    # <<< heat_recovery_boiler
    # @generated
    def __init__(self, steam_supply_rating2=0.0, combustion_turbines=None, **kw_args):
        """ Initialises a new 'HeatRecoveryBoiler' instance.
        """
        # The steam supply rating in kilopounds per hour, if dual pressure boiler 
        self.steam_supply_rating2 = steam_supply_rating2


        self._combustion_turbines = []
        if combustion_turbines is not None:
            self.combustion_turbines = combustion_turbines
        else:
            self.combustion_turbines = []


        super(HeatRecoveryBoiler, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the HeatRecoveryBoiler.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< heat_recovery_boiler.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the HeatRecoveryBoiler.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "HeatRecoveryBoiler", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.combustion_turbines:
            s += '%s<%s:HeatRecoveryBoiler.combustion_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:HeatRecoveryBoiler.steam_supply_rating2>%s</%s:HeatRecoveryBoiler.steam_supply_rating2>' % \
            (indent, ns_prefix, self.steam_supply_rating2, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)
        s += '%s<%s:FossilSteamSupply.boiler_control_mode>%s</%s:FossilSteamSupply.boiler_control_mode>' % \
            (indent, ns_prefix, self.boiler_control_mode, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_demand_limit>%s</%s:FossilSteamSupply.fuel_demand_limit>' % \
            (indent, ns_prefix, self.fuel_demand_limit, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_delay>%s</%s:FossilSteamSupply.fuel_supply_delay>' % \
            (indent, ns_prefix, self.fuel_supply_delay, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ic>%s</%s:FossilSteamSupply.control_ic>' % \
            (indent, ns_prefix, self.control_ic, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_ig>%s</%s:FossilSteamSupply.feed_water_ig>' % \
            (indent, ns_prefix, self.feed_water_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater1_capacity>%s</%s:FossilSteamSupply.super_heater1_capacity>' % \
            (indent, ns_prefix, self.super_heater1_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.throttle_pressure_sp>%s</%s:FossilSteamSupply.throttle_pressure_sp>' % \
            (indent, ns_prefix, self.throttle_pressure_sp, ns_prefix)
        s += '%s<%s:FossilSteamSupply.min_error_rate_p>%s</%s:FossilSteamSupply.min_error_rate_p>' % \
            (indent, ns_prefix, self.min_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_tc>%s</%s:FossilSteamSupply.feed_water_tc>' % \
            (indent, ns_prefix, self.feed_water_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater2_capacity>%s</%s:FossilSteamSupply.super_heater2_capacity>' % \
            (indent, ns_prefix, self.super_heater2_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_peb>%s</%s:FossilSteamSupply.control_peb>' % \
            (indent, ns_prefix, self.control_peb, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater_pipe_pd>%s</%s:FossilSteamSupply.super_heater_pipe_pd>' % \
            (indent, ns_prefix, self.super_heater_pipe_pd, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_tc>%s</%s:FossilSteamSupply.control_tc>' % \
            (indent, ns_prefix, self.control_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ped>%s</%s:FossilSteamSupply.control_ped>' % \
            (indent, ns_prefix, self.control_ped, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_feedback>%s</%s:FossilSteamSupply.pressure_feedback>' % \
            (indent, ns_prefix, self.pressure_feedback, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_pg>%s</%s:FossilSteamSupply.pressure_ctrl_pg>' % \
            (indent, ns_prefix, self.pressure_ctrl_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.mech_power_sensor_lag>%s</%s:FossilSteamSupply.mech_power_sensor_lag>' % \
            (indent, ns_prefix, self.mech_power_sensor_lag, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_error_bias_p>%s</%s:FossilSteamSupply.control_error_bias_p>' % \
            (indent, ns_prefix, self.control_error_bias_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_powerversus_voltage>%s</%s:FossilSteamSupply.aux_powerversus_voltage>' % \
            (indent, ns_prefix, self.aux_powerversus_voltage, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_pc>%s</%s:FossilSteamSupply.control_pc>' % \
            (indent, ns_prefix, self.control_pc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_dg>%s</%s:FossilSteamSupply.pressure_ctrl_dg>' % \
            (indent, ns_prefix, self.pressure_ctrl_dg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.max_error_rate_p>%s</%s:FossilSteamSupply.max_error_rate_p>' % \
            (indent, ns_prefix, self.max_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_ig>%s</%s:FossilSteamSupply.pressure_ctrl_ig>' % \
            (indent, ns_prefix, self.pressure_ctrl_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_power_versus_frequency>%s</%s:FossilSteamSupply.aux_power_versus_frequency>' % \
            (indent, ns_prefix, self.aux_power_versus_frequency, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_pg>%s</%s:FossilSteamSupply.feed_water_pg>' % \
            (indent, ns_prefix, self.feed_water_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_tc>%s</%s:FossilSteamSupply.fuel_supply_tc>' % \
            (indent, ns_prefix, self.fuel_supply_tc, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "HeatRecoveryBoiler")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> heat_recovery_boiler.serialize


class PWRSteamSupply(SteamSupply):
    """ Pressurized water reactor used as a steam supply to a steam turbine
    """
    # <<< pwrsteam_supply
    # @generated
    def __init__(self, core_neutronics_eff_tc=0.0, steam_flow_fg=0.0, cold_leg_fblead_tc1=0.0, throttle_pressure_sp=0.0, feedback_factor=0.0, cold_leg_fblag_tc=0.0, steam_pressure_fg=0.0, pressure_cg=0.0, core_neutronics_ht=0.0, cold_leg_fblead_tc2=0.0, steam_pressure_drop_lag_tc=0.0, core_htlag_tc2=0.0, hot_leg_lag_tc=0.0, hot_leg_to_cold_leg_gain=0.0, hot_leg_steam_gain=0.0, cold_leg_fg2=0.0, core_htlag_tc1=0.0, cold_leg_lag_tc=0.0, throttle_pressure_factor=0.0, cold_leg_fg1=0.0, **kw_args):
        """ Initialises a new 'PWRSteamSupply' instance.
        """
        # Core Neutronics Effective Time Constant 
        self.core_neutronics_eff_tc = core_neutronics_eff_tc

        # Steam Flow Feedback Gain 
        self.steam_flow_fg = steam_flow_fg

        # Cold Leg Feedback Lead Time Constant 
        self.cold_leg_fblead_tc1 = cold_leg_fblead_tc1

        # Throttle Pressure Setpoint 
        self.throttle_pressure_sp = throttle_pressure_sp

        # Feedback Factor 
        self.feedback_factor = feedback_factor

        # Cold Leg Feedback Lag Time Constant 
        self.cold_leg_fblag_tc = cold_leg_fblag_tc

        # Steam Pressure Feedback Gain 
        self.steam_pressure_fg = steam_pressure_fg

        # Pressure Control Gain 
        self.pressure_cg = pressure_cg

        # Core Neutronics And Heat Transfer 
        self.core_neutronics_ht = core_neutronics_ht

        # Cold Leg Feedback Lead Time Constant 
        self.cold_leg_fblead_tc2 = cold_leg_fblead_tc2

        # Steam Pressure Drop Lag Time Constant 
        self.steam_pressure_drop_lag_tc = steam_pressure_drop_lag_tc

        # Core Heat Transfer Lag Time Constant 
        self.core_htlag_tc2 = core_htlag_tc2

        # Hot Leg Lag Time Constant 
        self.hot_leg_lag_tc = hot_leg_lag_tc

        # Hot Leg To Cold Leg Gain 
        self.hot_leg_to_cold_leg_gain = hot_leg_to_cold_leg_gain

        # Hot Leg Steam Gain 
        self.hot_leg_steam_gain = hot_leg_steam_gain

        # Cold Leg Feedback Gain 2 
        self.cold_leg_fg2 = cold_leg_fg2

        # Core Heat Transfer Lag Time Constant 
        self.core_htlag_tc1 = core_htlag_tc1

        # Cold Leg Lag Time Constant 
        self.cold_leg_lag_tc = cold_leg_lag_tc

        # Throttle Pressure Factor 
        self.throttle_pressure_factor = throttle_pressure_factor

        # Cold Leg Feedback Gain 1 
        self.cold_leg_fg1 = cold_leg_fg1



        super(PWRSteamSupply, self).__init__(**kw_args)
    # >>> pwrsteam_supply


    def __str__(self):
        """ Returns a string representation of the PWRSteamSupply.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< pwrsteam_supply.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the PWRSteamSupply.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "PWRSteamSupply", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:PWRSteamSupply.core_neutronics_eff_tc>%s</%s:PWRSteamSupply.core_neutronics_eff_tc>' % \
            (indent, ns_prefix, self.core_neutronics_eff_tc, ns_prefix)
        s += '%s<%s:PWRSteamSupply.steam_flow_fg>%s</%s:PWRSteamSupply.steam_flow_fg>' % \
            (indent, ns_prefix, self.steam_flow_fg, ns_prefix)
        s += '%s<%s:PWRSteamSupply.cold_leg_fblead_tc1>%s</%s:PWRSteamSupply.cold_leg_fblead_tc1>' % \
            (indent, ns_prefix, self.cold_leg_fblead_tc1, ns_prefix)
        s += '%s<%s:PWRSteamSupply.throttle_pressure_sp>%s</%s:PWRSteamSupply.throttle_pressure_sp>' % \
            (indent, ns_prefix, self.throttle_pressure_sp, ns_prefix)
        s += '%s<%s:PWRSteamSupply.feedback_factor>%s</%s:PWRSteamSupply.feedback_factor>' % \
            (indent, ns_prefix, self.feedback_factor, ns_prefix)
        s += '%s<%s:PWRSteamSupply.cold_leg_fblag_tc>%s</%s:PWRSteamSupply.cold_leg_fblag_tc>' % \
            (indent, ns_prefix, self.cold_leg_fblag_tc, ns_prefix)
        s += '%s<%s:PWRSteamSupply.steam_pressure_fg>%s</%s:PWRSteamSupply.steam_pressure_fg>' % \
            (indent, ns_prefix, self.steam_pressure_fg, ns_prefix)
        s += '%s<%s:PWRSteamSupply.pressure_cg>%s</%s:PWRSteamSupply.pressure_cg>' % \
            (indent, ns_prefix, self.pressure_cg, ns_prefix)
        s += '%s<%s:PWRSteamSupply.core_neutronics_ht>%s</%s:PWRSteamSupply.core_neutronics_ht>' % \
            (indent, ns_prefix, self.core_neutronics_ht, ns_prefix)
        s += '%s<%s:PWRSteamSupply.cold_leg_fblead_tc2>%s</%s:PWRSteamSupply.cold_leg_fblead_tc2>' % \
            (indent, ns_prefix, self.cold_leg_fblead_tc2, ns_prefix)
        s += '%s<%s:PWRSteamSupply.steam_pressure_drop_lag_tc>%s</%s:PWRSteamSupply.steam_pressure_drop_lag_tc>' % \
            (indent, ns_prefix, self.steam_pressure_drop_lag_tc, ns_prefix)
        s += '%s<%s:PWRSteamSupply.core_htlag_tc2>%s</%s:PWRSteamSupply.core_htlag_tc2>' % \
            (indent, ns_prefix, self.core_htlag_tc2, ns_prefix)
        s += '%s<%s:PWRSteamSupply.hot_leg_lag_tc>%s</%s:PWRSteamSupply.hot_leg_lag_tc>' % \
            (indent, ns_prefix, self.hot_leg_lag_tc, ns_prefix)
        s += '%s<%s:PWRSteamSupply.hot_leg_to_cold_leg_gain>%s</%s:PWRSteamSupply.hot_leg_to_cold_leg_gain>' % \
            (indent, ns_prefix, self.hot_leg_to_cold_leg_gain, ns_prefix)
        s += '%s<%s:PWRSteamSupply.hot_leg_steam_gain>%s</%s:PWRSteamSupply.hot_leg_steam_gain>' % \
            (indent, ns_prefix, self.hot_leg_steam_gain, ns_prefix)
        s += '%s<%s:PWRSteamSupply.cold_leg_fg2>%s</%s:PWRSteamSupply.cold_leg_fg2>' % \
            (indent, ns_prefix, self.cold_leg_fg2, ns_prefix)
        s += '%s<%s:PWRSteamSupply.core_htlag_tc1>%s</%s:PWRSteamSupply.core_htlag_tc1>' % \
            (indent, ns_prefix, self.core_htlag_tc1, ns_prefix)
        s += '%s<%s:PWRSteamSupply.cold_leg_lag_tc>%s</%s:PWRSteamSupply.cold_leg_lag_tc>' % \
            (indent, ns_prefix, self.cold_leg_lag_tc, ns_prefix)
        s += '%s<%s:PWRSteamSupply.throttle_pressure_factor>%s</%s:PWRSteamSupply.throttle_pressure_factor>' % \
            (indent, ns_prefix, self.throttle_pressure_factor, ns_prefix)
        s += '%s<%s:PWRSteamSupply.cold_leg_fg1>%s</%s:PWRSteamSupply.cold_leg_fg1>' % \
            (indent, ns_prefix, self.cold_leg_fg1, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "PWRSteamSupply")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> pwrsteam_supply.serialize


class Supercritical(FossilSteamSupply):
    """ Once-through supercritical boiler
    """
    pass
    # <<< supercritical
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Supercritical' instance.
        """


        super(Supercritical, self).__init__(**kw_args)
    # >>> supercritical


    def __str__(self):
        """ Returns a string representation of the Supercritical.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< supercritical.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Supercritical.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Supercritical", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)
        s += '%s<%s:FossilSteamSupply.boiler_control_mode>%s</%s:FossilSteamSupply.boiler_control_mode>' % \
            (indent, ns_prefix, self.boiler_control_mode, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_demand_limit>%s</%s:FossilSteamSupply.fuel_demand_limit>' % \
            (indent, ns_prefix, self.fuel_demand_limit, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_delay>%s</%s:FossilSteamSupply.fuel_supply_delay>' % \
            (indent, ns_prefix, self.fuel_supply_delay, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ic>%s</%s:FossilSteamSupply.control_ic>' % \
            (indent, ns_prefix, self.control_ic, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_ig>%s</%s:FossilSteamSupply.feed_water_ig>' % \
            (indent, ns_prefix, self.feed_water_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater1_capacity>%s</%s:FossilSteamSupply.super_heater1_capacity>' % \
            (indent, ns_prefix, self.super_heater1_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.throttle_pressure_sp>%s</%s:FossilSteamSupply.throttle_pressure_sp>' % \
            (indent, ns_prefix, self.throttle_pressure_sp, ns_prefix)
        s += '%s<%s:FossilSteamSupply.min_error_rate_p>%s</%s:FossilSteamSupply.min_error_rate_p>' % \
            (indent, ns_prefix, self.min_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_tc>%s</%s:FossilSteamSupply.feed_water_tc>' % \
            (indent, ns_prefix, self.feed_water_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater2_capacity>%s</%s:FossilSteamSupply.super_heater2_capacity>' % \
            (indent, ns_prefix, self.super_heater2_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_peb>%s</%s:FossilSteamSupply.control_peb>' % \
            (indent, ns_prefix, self.control_peb, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater_pipe_pd>%s</%s:FossilSteamSupply.super_heater_pipe_pd>' % \
            (indent, ns_prefix, self.super_heater_pipe_pd, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_tc>%s</%s:FossilSteamSupply.control_tc>' % \
            (indent, ns_prefix, self.control_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ped>%s</%s:FossilSteamSupply.control_ped>' % \
            (indent, ns_prefix, self.control_ped, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_feedback>%s</%s:FossilSteamSupply.pressure_feedback>' % \
            (indent, ns_prefix, self.pressure_feedback, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_pg>%s</%s:FossilSteamSupply.pressure_ctrl_pg>' % \
            (indent, ns_prefix, self.pressure_ctrl_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.mech_power_sensor_lag>%s</%s:FossilSteamSupply.mech_power_sensor_lag>' % \
            (indent, ns_prefix, self.mech_power_sensor_lag, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_error_bias_p>%s</%s:FossilSteamSupply.control_error_bias_p>' % \
            (indent, ns_prefix, self.control_error_bias_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_powerversus_voltage>%s</%s:FossilSteamSupply.aux_powerversus_voltage>' % \
            (indent, ns_prefix, self.aux_powerversus_voltage, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_pc>%s</%s:FossilSteamSupply.control_pc>' % \
            (indent, ns_prefix, self.control_pc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_dg>%s</%s:FossilSteamSupply.pressure_ctrl_dg>' % \
            (indent, ns_prefix, self.pressure_ctrl_dg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.max_error_rate_p>%s</%s:FossilSteamSupply.max_error_rate_p>' % \
            (indent, ns_prefix, self.max_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_ig>%s</%s:FossilSteamSupply.pressure_ctrl_ig>' % \
            (indent, ns_prefix, self.pressure_ctrl_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_power_versus_frequency>%s</%s:FossilSteamSupply.aux_power_versus_frequency>' % \
            (indent, ns_prefix, self.aux_power_versus_frequency, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_pg>%s</%s:FossilSteamSupply.feed_water_pg>' % \
            (indent, ns_prefix, self.feed_water_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_tc>%s</%s:FossilSteamSupply.fuel_supply_tc>' % \
            (indent, ns_prefix, self.fuel_supply_tc, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Supercritical")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> supercritical.serialize


class CombustionTurbine(PrimeMover):
    """ A prime mover that is typically fueled by gas or light oil
    """
    # <<< combustion_turbine
    # @generated
    def __init__(self, power_variation_by_temp=0.0, time_constant=0.0, aux_power_versus_frequency=0.0, reference_temp=0.0, ambient_temp=0.0, capability_versus_frequency=0.0, heat_recovery_flag=False, aux_power_versus_voltage=0.0, cttemp_active_power_curve=None, heat_recovery_boiler=None, drives_air_compressor=None, **kw_args):
        """ Initialises a new 'CombustionTurbine' instance.
        """
        # Per unit change in power per (versus) unit change in ambient temperature 
        self.power_variation_by_temp = power_variation_by_temp

        # The time constant for the turbine. 
        self.time_constant = time_constant

        # Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in frequency (from rated frequency). 
        self.aux_power_versus_frequency = aux_power_versus_frequency

        # Reference temperature at which the output of the turbine was defined. 
        self.reference_temp = reference_temp

        # Default ambient temperature to be used in modeling applications 
        self.ambient_temp = ambient_temp

        # Off-nominal frequency effect on turbine capability. Per unit reduction in unit active power capability versus per unit reduction in frequency (from rated frequency). 
        self.capability_versus_frequency = capability_versus_frequency

        # Flag that is set to true if the combustion turbine is associated with a heat recovery boiler 
        self.heat_recovery_flag = heat_recovery_flag

        # Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in auxiliary active power consumption versus per unit reduction in auxiliary bus voltage (from a specified voltage level). 
        self.aux_power_versus_voltage = aux_power_versus_voltage


        self._cttemp_active_power_curve = None
        self.cttemp_active_power_curve = cttemp_active_power_curve

        self._heat_recovery_boiler = None
        self.heat_recovery_boiler = heat_recovery_boiler

        self._drives_air_compressor = None
        self.drives_air_compressor = drives_air_compressor


        super(CombustionTurbine, self).__init__(**kw_args)
    # >>> combustion_turbine

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

    # <<< drives_air_compressor
    # @generated
    def get_drives_air_compressor(self):
        """ A CAES air compressor is driven by combustion turbine
        """
        return self._drives_air_compressor

    def set_drives_air_compressor(self, value):
        if self._drives_air_compressor is not None:
            self._drives_air_compressor._driven_by_combustion_turbine = None

        self._drives_air_compressor = value
        if self._drives_air_compressor is not None:
            self._drives_air_compressor._driven_by_combustion_turbine = self

    drives_air_compressor = property(get_drives_air_compressor, set_drives_air_compressor)
    # >>> drives_air_compressor


    def __str__(self):
        """ Returns a string representation of the CombustionTurbine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< combustion_turbine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the CombustionTurbine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "CombustionTurbine", self.uri)
        if format:
            indent += ' ' * depth

        if self.cttemp_active_power_curve is not None:
            s += '%s<%s:CombustionTurbine.cttemp_active_power_curve rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.cttemp_active_power_curve.uri)
        if self.heat_recovery_boiler is not None:
            s += '%s<%s:CombustionTurbine.heat_recovery_boiler rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.heat_recovery_boiler.uri)
        if self.drives_air_compressor is not None:
            s += '%s<%s:CombustionTurbine.drives_air_compressor rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.drives_air_compressor.uri)
        s += '%s<%s:CombustionTurbine.power_variation_by_temp>%s</%s:CombustionTurbine.power_variation_by_temp>' % \
            (indent, ns_prefix, self.power_variation_by_temp, ns_prefix)
        s += '%s<%s:CombustionTurbine.time_constant>%s</%s:CombustionTurbine.time_constant>' % \
            (indent, ns_prefix, self.time_constant, ns_prefix)
        s += '%s<%s:CombustionTurbine.aux_power_versus_frequency>%s</%s:CombustionTurbine.aux_power_versus_frequency>' % \
            (indent, ns_prefix, self.aux_power_versus_frequency, ns_prefix)
        s += '%s<%s:CombustionTurbine.reference_temp>%s</%s:CombustionTurbine.reference_temp>' % \
            (indent, ns_prefix, self.reference_temp, ns_prefix)
        s += '%s<%s:CombustionTurbine.ambient_temp>%s</%s:CombustionTurbine.ambient_temp>' % \
            (indent, ns_prefix, self.ambient_temp, ns_prefix)
        s += '%s<%s:CombustionTurbine.capability_versus_frequency>%s</%s:CombustionTurbine.capability_versus_frequency>' % \
            (indent, ns_prefix, self.capability_versus_frequency, ns_prefix)
        s += '%s<%s:CombustionTurbine.heat_recovery_flag>%s</%s:CombustionTurbine.heat_recovery_flag>' % \
            (indent, ns_prefix, self.heat_recovery_flag, ns_prefix)
        s += '%s<%s:CombustionTurbine.aux_power_versus_voltage>%s</%s:CombustionTurbine.aux_power_versus_voltage>' % \
            (indent, ns_prefix, self.aux_power_versus_voltage, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.drives_synchronous_machines:
            s += '%s<%s:PrimeMover.drives_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PrimeMover.prime_mover_rating>%s</%s:PrimeMover.prime_mover_rating>' % \
            (indent, ns_prefix, self.prime_mover_rating, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "CombustionTurbine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> combustion_turbine.serialize


class HydroTurbine(PrimeMover):
    """ A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """
    # <<< hydro_turbine
    # @generated
    def __init__(self, turbine_type='francis', speed_regulation=0.0, min_head_max_p=0.0, gate_upper_limit=0.0, gate_rate_limit=0.0, max_head_max_p=0.0, transient_regulation=0.0, speed_rating=0.0, water_starting_time=0.0, turbine_rating=0.0, transient_droop_time=0.0, **kw_args):
        """ Initialises a new 'HydroTurbine' instance.
        """
        # Type of turbine. Values are: "francis", "kaplan", "pelton"
        self.turbine_type = 'francis'

        # Speed Regulation 
        self.speed_regulation = speed_regulation

        # Maximum efficiency active power at minimum head conditions 
        self.min_head_max_p = min_head_max_p

        # Gate Upper Limit 
        self.gate_upper_limit = gate_upper_limit

        # Gate Rate Limit 
        self.gate_rate_limit = gate_rate_limit

        # Maximum efficiency active power at maximum head conditions 
        self.max_head_max_p = max_head_max_p

        # Transient Regulation 
        self.transient_regulation = transient_regulation

        # Rated speed in number of revolutions. 
        self.speed_rating = speed_rating

        # Water Starting Time 
        self.water_starting_time = water_starting_time

        # Rated turbine active power 
        self.turbine_rating = turbine_rating

        # Transient Droop Time Constant 
        self.transient_droop_time = transient_droop_time



        super(HydroTurbine, self).__init__(**kw_args)
    # >>> hydro_turbine


    def __str__(self):
        """ Returns a string representation of the HydroTurbine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< hydro_turbine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the HydroTurbine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "HydroTurbine", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:HydroTurbine.turbine_type>%s</%s:HydroTurbine.turbine_type>' % \
            (indent, ns_prefix, self.turbine_type, ns_prefix)
        s += '%s<%s:HydroTurbine.speed_regulation>%s</%s:HydroTurbine.speed_regulation>' % \
            (indent, ns_prefix, self.speed_regulation, ns_prefix)
        s += '%s<%s:HydroTurbine.min_head_max_p>%s</%s:HydroTurbine.min_head_max_p>' % \
            (indent, ns_prefix, self.min_head_max_p, ns_prefix)
        s += '%s<%s:HydroTurbine.gate_upper_limit>%s</%s:HydroTurbine.gate_upper_limit>' % \
            (indent, ns_prefix, self.gate_upper_limit, ns_prefix)
        s += '%s<%s:HydroTurbine.gate_rate_limit>%s</%s:HydroTurbine.gate_rate_limit>' % \
            (indent, ns_prefix, self.gate_rate_limit, ns_prefix)
        s += '%s<%s:HydroTurbine.max_head_max_p>%s</%s:HydroTurbine.max_head_max_p>' % \
            (indent, ns_prefix, self.max_head_max_p, ns_prefix)
        s += '%s<%s:HydroTurbine.transient_regulation>%s</%s:HydroTurbine.transient_regulation>' % \
            (indent, ns_prefix, self.transient_regulation, ns_prefix)
        s += '%s<%s:HydroTurbine.speed_rating>%s</%s:HydroTurbine.speed_rating>' % \
            (indent, ns_prefix, self.speed_rating, ns_prefix)
        s += '%s<%s:HydroTurbine.water_starting_time>%s</%s:HydroTurbine.water_starting_time>' % \
            (indent, ns_prefix, self.water_starting_time, ns_prefix)
        s += '%s<%s:HydroTurbine.turbine_rating>%s</%s:HydroTurbine.turbine_rating>' % \
            (indent, ns_prefix, self.turbine_rating, ns_prefix)
        s += '%s<%s:HydroTurbine.transient_droop_time>%s</%s:HydroTurbine.transient_droop_time>' % \
            (indent, ns_prefix, self.transient_droop_time, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.drives_synchronous_machines:
            s += '%s<%s:PrimeMover.drives_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PrimeMover.prime_mover_rating>%s</%s:PrimeMover.prime_mover_rating>' % \
            (indent, ns_prefix, self.prime_mover_rating, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "HydroTurbine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> hydro_turbine.serialize


class Subcritical(FossilSteamSupply):
    """ Once-through subcritical boiler
    """
    pass
    # <<< subcritical
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'Subcritical' instance.
        """


        super(Subcritical, self).__init__(**kw_args)
    # >>> subcritical


    def __str__(self):
        """ Returns a string representation of the Subcritical.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< subcritical.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the Subcritical.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "Subcritical", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)
        s += '%s<%s:FossilSteamSupply.boiler_control_mode>%s</%s:FossilSteamSupply.boiler_control_mode>' % \
            (indent, ns_prefix, self.boiler_control_mode, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_demand_limit>%s</%s:FossilSteamSupply.fuel_demand_limit>' % \
            (indent, ns_prefix, self.fuel_demand_limit, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_delay>%s</%s:FossilSteamSupply.fuel_supply_delay>' % \
            (indent, ns_prefix, self.fuel_supply_delay, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ic>%s</%s:FossilSteamSupply.control_ic>' % \
            (indent, ns_prefix, self.control_ic, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_ig>%s</%s:FossilSteamSupply.feed_water_ig>' % \
            (indent, ns_prefix, self.feed_water_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater1_capacity>%s</%s:FossilSteamSupply.super_heater1_capacity>' % \
            (indent, ns_prefix, self.super_heater1_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.throttle_pressure_sp>%s</%s:FossilSteamSupply.throttle_pressure_sp>' % \
            (indent, ns_prefix, self.throttle_pressure_sp, ns_prefix)
        s += '%s<%s:FossilSteamSupply.min_error_rate_p>%s</%s:FossilSteamSupply.min_error_rate_p>' % \
            (indent, ns_prefix, self.min_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_tc>%s</%s:FossilSteamSupply.feed_water_tc>' % \
            (indent, ns_prefix, self.feed_water_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater2_capacity>%s</%s:FossilSteamSupply.super_heater2_capacity>' % \
            (indent, ns_prefix, self.super_heater2_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_peb>%s</%s:FossilSteamSupply.control_peb>' % \
            (indent, ns_prefix, self.control_peb, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater_pipe_pd>%s</%s:FossilSteamSupply.super_heater_pipe_pd>' % \
            (indent, ns_prefix, self.super_heater_pipe_pd, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_tc>%s</%s:FossilSteamSupply.control_tc>' % \
            (indent, ns_prefix, self.control_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ped>%s</%s:FossilSteamSupply.control_ped>' % \
            (indent, ns_prefix, self.control_ped, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_feedback>%s</%s:FossilSteamSupply.pressure_feedback>' % \
            (indent, ns_prefix, self.pressure_feedback, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_pg>%s</%s:FossilSteamSupply.pressure_ctrl_pg>' % \
            (indent, ns_prefix, self.pressure_ctrl_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.mech_power_sensor_lag>%s</%s:FossilSteamSupply.mech_power_sensor_lag>' % \
            (indent, ns_prefix, self.mech_power_sensor_lag, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_error_bias_p>%s</%s:FossilSteamSupply.control_error_bias_p>' % \
            (indent, ns_prefix, self.control_error_bias_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_powerversus_voltage>%s</%s:FossilSteamSupply.aux_powerversus_voltage>' % \
            (indent, ns_prefix, self.aux_powerversus_voltage, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_pc>%s</%s:FossilSteamSupply.control_pc>' % \
            (indent, ns_prefix, self.control_pc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_dg>%s</%s:FossilSteamSupply.pressure_ctrl_dg>' % \
            (indent, ns_prefix, self.pressure_ctrl_dg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.max_error_rate_p>%s</%s:FossilSteamSupply.max_error_rate_p>' % \
            (indent, ns_prefix, self.max_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_ig>%s</%s:FossilSteamSupply.pressure_ctrl_ig>' % \
            (indent, ns_prefix, self.pressure_ctrl_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_power_versus_frequency>%s</%s:FossilSteamSupply.aux_power_versus_frequency>' % \
            (indent, ns_prefix, self.aux_power_versus_frequency, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_pg>%s</%s:FossilSteamSupply.feed_water_pg>' % \
            (indent, ns_prefix, self.feed_water_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_tc>%s</%s:FossilSteamSupply.fuel_supply_tc>' % \
            (indent, ns_prefix, self.fuel_supply_tc, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "Subcritical")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> subcritical.serialize


class SteamTurbine(PrimeMover):
    """ Steam turbine
    """
    # <<< steam_turbine
    # @generated
    def __init__(self, shaft1_power_ip=0.0, shaft2_power_ip=0.0, shaft2_power_lp2=0.0, reheater1_tc=0.0, crossover_tc=0.0, shaft1_power_hp=0.0, shaft1_power_lp2=0.0, shaft2_power_lp1=0.0, steam_chest_tc=0.0, shaft2_power_hp=0.0, reheater2_tc=0.0, shaft1_power_lp1=0.0, steam_supplys=None, **kw_args):
        """ Initialises a new 'SteamTurbine' instance.
        """
        # Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output 
        self.shaft1_power_ip = shaft1_power_ip

        # Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output 
        self.shaft2_power_ip = shaft2_power_ip

        # Fraction Of Power From Shaft 2 Second Low Pressure Turbine output 
        self.shaft2_power_lp2 = shaft2_power_lp2

        # First Reheater Time Constant 
        self.reheater1_tc = reheater1_tc

        # Crossover Time Constant 
        self.crossover_tc = crossover_tc

        # Fraction Of Power From Shaft 1 High Pressure Turbine output 
        self.shaft1_power_hp = shaft1_power_hp

        # Fraction Of Power From Shaft 1 Second Low Pressure Turbine output 
        self.shaft1_power_lp2 = shaft1_power_lp2

        # Fraction Of Power From Shaft 2 First Low Pressure Turbine output 
        self.shaft2_power_lp1 = shaft2_power_lp1

        # Steam Chest Time Constant 
        self.steam_chest_tc = steam_chest_tc

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


        super(SteamTurbine, self).__init__(**kw_args)
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


    def __str__(self):
        """ Returns a string representation of the SteamTurbine.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< steam_turbine.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the SteamTurbine.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "SteamTurbine", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.steam_supplys:
            s += '%s<%s:SteamTurbine.steam_supplys rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamTurbine.shaft1_power_ip>%s</%s:SteamTurbine.shaft1_power_ip>' % \
            (indent, ns_prefix, self.shaft1_power_ip, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft2_power_ip>%s</%s:SteamTurbine.shaft2_power_ip>' % \
            (indent, ns_prefix, self.shaft2_power_ip, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft2_power_lp2>%s</%s:SteamTurbine.shaft2_power_lp2>' % \
            (indent, ns_prefix, self.shaft2_power_lp2, ns_prefix)
        s += '%s<%s:SteamTurbine.reheater1_tc>%s</%s:SteamTurbine.reheater1_tc>' % \
            (indent, ns_prefix, self.reheater1_tc, ns_prefix)
        s += '%s<%s:SteamTurbine.crossover_tc>%s</%s:SteamTurbine.crossover_tc>' % \
            (indent, ns_prefix, self.crossover_tc, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft1_power_hp>%s</%s:SteamTurbine.shaft1_power_hp>' % \
            (indent, ns_prefix, self.shaft1_power_hp, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft1_power_lp2>%s</%s:SteamTurbine.shaft1_power_lp2>' % \
            (indent, ns_prefix, self.shaft1_power_lp2, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft2_power_lp1>%s</%s:SteamTurbine.shaft2_power_lp1>' % \
            (indent, ns_prefix, self.shaft2_power_lp1, ns_prefix)
        s += '%s<%s:SteamTurbine.steam_chest_tc>%s</%s:SteamTurbine.steam_chest_tc>' % \
            (indent, ns_prefix, self.steam_chest_tc, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft2_power_hp>%s</%s:SteamTurbine.shaft2_power_hp>' % \
            (indent, ns_prefix, self.shaft2_power_hp, ns_prefix)
        s += '%s<%s:SteamTurbine.reheater2_tc>%s</%s:SteamTurbine.reheater2_tc>' % \
            (indent, ns_prefix, self.reheater2_tc, ns_prefix)
        s += '%s<%s:SteamTurbine.shaft1_power_lp1>%s</%s:SteamTurbine.shaft1_power_lp1>' % \
            (indent, ns_prefix, self.shaft1_power_lp1, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.drives_synchronous_machines:
            s += '%s<%s:PrimeMover.drives_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:PrimeMover.prime_mover_rating>%s</%s:PrimeMover.prime_mover_rating>' % \
            (indent, ns_prefix, self.prime_mover_rating, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "SteamTurbine")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> steam_turbine.serialize


class DrumBoiler(FossilSteamSupply):
    """ Drum boiler
    """
    # <<< drum_boiler
    # @generated
    def __init__(self, drum_boiler_rating=0.0, **kw_args):
        """ Initialises a new 'DrumBoiler' instance.
        """
        # Rating of drum boiler in steam units 
        self.drum_boiler_rating = drum_boiler_rating



        super(DrumBoiler, self).__init__(**kw_args)
    # >>> drum_boiler


    def __str__(self):
        """ Returns a string representation of the DrumBoiler.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< drum_boiler.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the DrumBoiler.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "DrumBoiler", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:DrumBoiler.drum_boiler_rating>%s</%s:DrumBoiler.drum_boiler_rating>' % \
            (indent, ns_prefix, self.drum_boiler_rating, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)
        s += '%s<%s:FossilSteamSupply.boiler_control_mode>%s</%s:FossilSteamSupply.boiler_control_mode>' % \
            (indent, ns_prefix, self.boiler_control_mode, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_demand_limit>%s</%s:FossilSteamSupply.fuel_demand_limit>' % \
            (indent, ns_prefix, self.fuel_demand_limit, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_delay>%s</%s:FossilSteamSupply.fuel_supply_delay>' % \
            (indent, ns_prefix, self.fuel_supply_delay, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ic>%s</%s:FossilSteamSupply.control_ic>' % \
            (indent, ns_prefix, self.control_ic, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_ig>%s</%s:FossilSteamSupply.feed_water_ig>' % \
            (indent, ns_prefix, self.feed_water_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater1_capacity>%s</%s:FossilSteamSupply.super_heater1_capacity>' % \
            (indent, ns_prefix, self.super_heater1_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.throttle_pressure_sp>%s</%s:FossilSteamSupply.throttle_pressure_sp>' % \
            (indent, ns_prefix, self.throttle_pressure_sp, ns_prefix)
        s += '%s<%s:FossilSteamSupply.min_error_rate_p>%s</%s:FossilSteamSupply.min_error_rate_p>' % \
            (indent, ns_prefix, self.min_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_tc>%s</%s:FossilSteamSupply.feed_water_tc>' % \
            (indent, ns_prefix, self.feed_water_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater2_capacity>%s</%s:FossilSteamSupply.super_heater2_capacity>' % \
            (indent, ns_prefix, self.super_heater2_capacity, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_peb>%s</%s:FossilSteamSupply.control_peb>' % \
            (indent, ns_prefix, self.control_peb, ns_prefix)
        s += '%s<%s:FossilSteamSupply.super_heater_pipe_pd>%s</%s:FossilSteamSupply.super_heater_pipe_pd>' % \
            (indent, ns_prefix, self.super_heater_pipe_pd, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_tc>%s</%s:FossilSteamSupply.control_tc>' % \
            (indent, ns_prefix, self.control_tc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_ped>%s</%s:FossilSteamSupply.control_ped>' % \
            (indent, ns_prefix, self.control_ped, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_feedback>%s</%s:FossilSteamSupply.pressure_feedback>' % \
            (indent, ns_prefix, self.pressure_feedback, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_pg>%s</%s:FossilSteamSupply.pressure_ctrl_pg>' % \
            (indent, ns_prefix, self.pressure_ctrl_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.mech_power_sensor_lag>%s</%s:FossilSteamSupply.mech_power_sensor_lag>' % \
            (indent, ns_prefix, self.mech_power_sensor_lag, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_error_bias_p>%s</%s:FossilSteamSupply.control_error_bias_p>' % \
            (indent, ns_prefix, self.control_error_bias_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_powerversus_voltage>%s</%s:FossilSteamSupply.aux_powerversus_voltage>' % \
            (indent, ns_prefix, self.aux_powerversus_voltage, ns_prefix)
        s += '%s<%s:FossilSteamSupply.control_pc>%s</%s:FossilSteamSupply.control_pc>' % \
            (indent, ns_prefix, self.control_pc, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_dg>%s</%s:FossilSteamSupply.pressure_ctrl_dg>' % \
            (indent, ns_prefix, self.pressure_ctrl_dg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.max_error_rate_p>%s</%s:FossilSteamSupply.max_error_rate_p>' % \
            (indent, ns_prefix, self.max_error_rate_p, ns_prefix)
        s += '%s<%s:FossilSteamSupply.pressure_ctrl_ig>%s</%s:FossilSteamSupply.pressure_ctrl_ig>' % \
            (indent, ns_prefix, self.pressure_ctrl_ig, ns_prefix)
        s += '%s<%s:FossilSteamSupply.aux_power_versus_frequency>%s</%s:FossilSteamSupply.aux_power_versus_frequency>' % \
            (indent, ns_prefix, self.aux_power_versus_frequency, ns_prefix)
        s += '%s<%s:FossilSteamSupply.feed_water_pg>%s</%s:FossilSteamSupply.feed_water_pg>' % \
            (indent, ns_prefix, self.feed_water_pg, ns_prefix)
        s += '%s<%s:FossilSteamSupply.fuel_supply_tc>%s</%s:FossilSteamSupply.fuel_supply_tc>' % \
            (indent, ns_prefix, self.fuel_supply_tc, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "DrumBoiler")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> drum_boiler.serialize


class BWRSteamSupply(SteamSupply):
    """ Boiling water reactor used as a steam supply to a steam turbine
    """
    # <<< bwrsteam_supply
    # @generated
    def __init__(self, rf_aux1=0.0, rf_aux3=0.0, pressure_setpoint_ga=0.0, pressure_setpoint_tc2=0.0, rod_pattern=0.0, rf_aux5=0.0, rf_aux7=0.0, rf_aux2=0.0, pressure_limit=0.0, pressure_setpoint_tc1=0.0, rf_aux4=0.0, rod_pattern_constant=0.0, integral_gain=0.0, lower_limit=0.0, low_power_limit=0.0, rf_aux6=0.0, proportional_gain=0.0, rf_aux8=0.0, upper_limit=0.0, high_power_limit=0.0, in_core_thermal_tc=0.0, **kw_args):
        """ Initialises a new 'BWRSteamSupply' instance.
        """
        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux1 = rf_aux1

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux3 = rf_aux3

        # Pressure Setpoint Gain Adjuster 
        self.pressure_setpoint_ga = pressure_setpoint_ga

        # Pressure Setpoint Time Constant 
        self.pressure_setpoint_tc2 = pressure_setpoint_tc2

        # Rod Pattern 
        self.rod_pattern = rod_pattern

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux5 = rf_aux5

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux7 = rf_aux7

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux2 = rf_aux2

        # Pressure Limit 
        self.pressure_limit = pressure_limit

        # Pressure Setpoint Time Constant 
        self.pressure_setpoint_tc1 = pressure_setpoint_tc1

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux4 = rf_aux4

        # Constant Associated With Rod Pattern 
        self.rod_pattern_constant = rod_pattern_constant

        # Integral Gain 
        self.integral_gain = integral_gain

        # Initial Lower Limit 
        self.lower_limit = lower_limit

        # Low Power Limit 
        self.low_power_limit = low_power_limit

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux6 = rf_aux6

        # Proportional Gain 
        self.proportional_gain = proportional_gain

        # Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        self.rf_aux8 = rf_aux8

        # Initial Upper Limit 
        self.upper_limit = upper_limit

        # High Power Limit 
        self.high_power_limit = high_power_limit

        # In-Core Thermal Time Constant 
        self.in_core_thermal_tc = in_core_thermal_tc



        super(BWRSteamSupply, self).__init__(**kw_args)
    # >>> bwrsteam_supply


    def __str__(self):
        """ Returns a string representation of the BWRSteamSupply.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bwrsteam_supply.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BWRSteamSupply.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BWRSteamSupply", self.uri)
        if format:
            indent += ' ' * depth

        s += '%s<%s:BWRSteamSupply.rf_aux1>%s</%s:BWRSteamSupply.rf_aux1>' % \
            (indent, ns_prefix, self.rf_aux1, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux3>%s</%s:BWRSteamSupply.rf_aux3>' % \
            (indent, ns_prefix, self.rf_aux3, ns_prefix)
        s += '%s<%s:BWRSteamSupply.pressure_setpoint_ga>%s</%s:BWRSteamSupply.pressure_setpoint_ga>' % \
            (indent, ns_prefix, self.pressure_setpoint_ga, ns_prefix)
        s += '%s<%s:BWRSteamSupply.pressure_setpoint_tc2>%s</%s:BWRSteamSupply.pressure_setpoint_tc2>' % \
            (indent, ns_prefix, self.pressure_setpoint_tc2, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rod_pattern>%s</%s:BWRSteamSupply.rod_pattern>' % \
            (indent, ns_prefix, self.rod_pattern, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux5>%s</%s:BWRSteamSupply.rf_aux5>' % \
            (indent, ns_prefix, self.rf_aux5, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux7>%s</%s:BWRSteamSupply.rf_aux7>' % \
            (indent, ns_prefix, self.rf_aux7, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux2>%s</%s:BWRSteamSupply.rf_aux2>' % \
            (indent, ns_prefix, self.rf_aux2, ns_prefix)
        s += '%s<%s:BWRSteamSupply.pressure_limit>%s</%s:BWRSteamSupply.pressure_limit>' % \
            (indent, ns_prefix, self.pressure_limit, ns_prefix)
        s += '%s<%s:BWRSteamSupply.pressure_setpoint_tc1>%s</%s:BWRSteamSupply.pressure_setpoint_tc1>' % \
            (indent, ns_prefix, self.pressure_setpoint_tc1, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux4>%s</%s:BWRSteamSupply.rf_aux4>' % \
            (indent, ns_prefix, self.rf_aux4, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rod_pattern_constant>%s</%s:BWRSteamSupply.rod_pattern_constant>' % \
            (indent, ns_prefix, self.rod_pattern_constant, ns_prefix)
        s += '%s<%s:BWRSteamSupply.integral_gain>%s</%s:BWRSteamSupply.integral_gain>' % \
            (indent, ns_prefix, self.integral_gain, ns_prefix)
        s += '%s<%s:BWRSteamSupply.lower_limit>%s</%s:BWRSteamSupply.lower_limit>' % \
            (indent, ns_prefix, self.lower_limit, ns_prefix)
        s += '%s<%s:BWRSteamSupply.low_power_limit>%s</%s:BWRSteamSupply.low_power_limit>' % \
            (indent, ns_prefix, self.low_power_limit, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux6>%s</%s:BWRSteamSupply.rf_aux6>' % \
            (indent, ns_prefix, self.rf_aux6, ns_prefix)
        s += '%s<%s:BWRSteamSupply.proportional_gain>%s</%s:BWRSteamSupply.proportional_gain>' % \
            (indent, ns_prefix, self.proportional_gain, ns_prefix)
        s += '%s<%s:BWRSteamSupply.rf_aux8>%s</%s:BWRSteamSupply.rf_aux8>' % \
            (indent, ns_prefix, self.rf_aux8, ns_prefix)
        s += '%s<%s:BWRSteamSupply.upper_limit>%s</%s:BWRSteamSupply.upper_limit>' % \
            (indent, ns_prefix, self.upper_limit, ns_prefix)
        s += '%s<%s:BWRSteamSupply.high_power_limit>%s</%s:BWRSteamSupply.high_power_limit>' % \
            (indent, ns_prefix, self.high_power_limit, ns_prefix)
        s += '%s<%s:BWRSteamSupply.in_core_thermal_tc>%s</%s:BWRSteamSupply.in_core_thermal_tc>' % \
            (indent, ns_prefix, self.in_core_thermal_tc, ns_prefix)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        if self.modeling_authority_set is not None:
            s += '%s<%s:IdentifiedObject.modeling_authority_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.modeling_authority_set.uri)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.operated_by_companies:
            s += '%s<%s:PowerSystemResource.operated_by_companies rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.psr_lists:
            s += '%s<%s:PowerSystemResource.psr_lists rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.operating_share:
            s += '%s<%s:PowerSystemResource.operating_share rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.outage_schedule is not None:
            s += '%s<%s:PowerSystemResource.outage_schedule rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.outage_schedule.uri)
        for obj in self.reporting_group:
            s += '%s<%s:PowerSystemResource.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        for obj in self.steam_turbines:
            s += '%s<%s:SteamSupply.steam_turbines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:SteamSupply.steam_supply_rating>%s</%s:SteamSupply.steam_supply_rating>' % \
            (indent, ns_prefix, self.steam_supply_rating, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BWRSteamSupply")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bwrsteam_supply.serialize


# <<< generation_dynamics
# @generated
# >>> generation_dynamics
