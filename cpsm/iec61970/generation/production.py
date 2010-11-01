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

from cpsm.iec61970.core import Curve
from cpsm.iec61970.core import Equipment

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Production"

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



class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """
    # <<< generating_unit
    # @generated
    def __init__(self, max_operating_p=0.0, normal_pf=0.0, rated_gross_max_p=0.0, rated_gross_min_p=0.0, gen_control_source='off_agc', rated_net_max_p=0.0, long_pf=0.0, initial_p=0.0, short_pf=0.0, min_operating_p=0.0, contains_synchronous_machines=None, gross_to_net_active_power_curves=None, control_area_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'GeneratingUnit' instance.

        @param max_operating_p: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param normal_pf: Generating unit economic participation factor 
        @param rated_gross_max_p: The unit's gross rated maximum capacity (Book Value). 
        @param rated_gross_min_p: The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        @param gen_control_source: The source of controls for a generating unit. Values are: "off_agc", "unavailable", "on_agc", "plant_control"
        @param rated_net_max_p: The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        @param long_pf: Generating unit economic participation factor 
        @param initial_p: Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        @param short_pf: Generating unit economic participation factor 
        @param min_operating_p: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param contains_synchronous_machines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param gross_to_net_active_power_curves: A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
        @param control_area_generating_unit: ControlArea specifications for this generating unit.
        """
        # This is the maximum operating active power limit the dispatcher can enter for this unit 
        self.max_operating_p = max_operating_p

        # Generating unit economic participation factor 
        self.normal_pf = normal_pf

        # The unit's gross rated maximum capacity (Book Value). 
        self.rated_gross_max_p = rated_gross_max_p

        # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        self.rated_gross_min_p = rated_gross_min_p

        # The source of controls for a generating unit. Values are: "off_agc", "unavailable", "on_agc", "plant_control"
        self.gen_control_source = gen_control_source

        # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        self.rated_net_max_p = rated_net_max_p

        # Generating unit economic participation factor 
        self.long_pf = long_pf

        # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        self.initial_p = initial_p

        # Generating unit economic participation factor 
        self.short_pf = short_pf

        # This is the minimum operating active power limit the dispatcher can enter for this unit. 
        self.min_operating_p = min_operating_p


        self._contains_synchronous_machines = []
        if contains_synchronous_machines is not None:
            self.contains_synchronous_machines = contains_synchronous_machines
        else:
            self.contains_synchronous_machines = []

        self._gross_to_net_active_power_curves = []
        if gross_to_net_active_power_curves is not None:
            self.gross_to_net_active_power_curves = gross_to_net_active_power_curves
        else:
            self.gross_to_net_active_power_curves = []

        self._control_area_generating_unit = []
        if control_area_generating_unit is not None:
            self.control_area_generating_unit = control_area_generating_unit
        else:
            self.control_area_generating_unit = []


        super(GeneratingUnit, self).__init__(*args, **kw_args)
    # >>> generating_unit

    # <<< contains_synchronous_machines
    # @generated
    def get_contains_synchronous_machines(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._contains_synchronous_machines

    def set_contains_synchronous_machines(self, value):
        for x in self._contains_synchronous_machines:
            x._member_of_generating_unit = None
        for y in value:
            y._member_of_generating_unit = self
        self._contains_synchronous_machines = value

    contains_synchronous_machines = property(get_contains_synchronous_machines, set_contains_synchronous_machines)

    def add_contains_synchronous_machines(self, *contains_synchronous_machines):
        for obj in contains_synchronous_machines:
            obj._member_of_generating_unit = self
            self._contains_synchronous_machines.append(obj)

    def remove_contains_synchronous_machines(self, *contains_synchronous_machines):
        for obj in contains_synchronous_machines:
            obj._member_of_generating_unit = None
            self._contains_synchronous_machines.remove(obj)
    # >>> contains_synchronous_machines

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



class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """
    pass
    # <<< hydro_generating_unit
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'HydroGeneratingUnit' instance.

        """


        super(HydroGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> hydro_generating_unit



class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """
    pass
    # <<< thermal_generating_unit
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'ThermalGeneratingUnit' instance.

        """


        super(ThermalGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> thermal_generating_unit



# <<< production
# @generated
# >>> production
