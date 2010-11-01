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

from entsoe.core import Equipment
from entsoe.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Production"

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
    """
    # <<< generating_unit
    # @generated
    def __init__(self, max_operating_p=0.0, startup_cost=0.0, nominal_p=0.0, governor_scd=0.0, maximum_allowable_spinning_reserve=0.0, variable_cost=0.0, min_operating_p=0.0, normal_pf=0.0, contains_synchronous_machines=None, control_area_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'GeneratingUnit' instance.

        @param max_operating_p: This is the maximum operating active power limit the dispatcher can enter for this unit 
        @param startup_cost: The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only. 
        @param nominal_p: The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        @param governor_scd: Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only. 
        @param maximum_allowable_spinning_reserve: Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        @param variable_cost: The variable cost component of production per unit of ActivePower.This is for Short Circuit only. 
        @param min_operating_p: This is the minimum operating active power limit the dispatcher can enter for this unit. 
        @param normal_pf: Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one.  
        @param contains_synchronous_machines: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        @param control_area_generating_unit: ControlArea specifications for this generating unit.
        """
        # This is the maximum operating active power limit the dispatcher can enter for this unit 
        self.max_operating_p = max_operating_p

        # The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only. 
        self.startup_cost = startup_cost

        # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        self.nominal_p = nominal_p

        # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only. 
        self.governor_scd = governor_scd

        # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        self.maximum_allowable_spinning_reserve = maximum_allowable_spinning_reserve

        # The variable cost component of production per unit of ActivePower.This is for Short Circuit only. 
        self.variable_cost = variable_cost

        # This is the minimum operating active power limit the dispatcher can enter for this unit. 
        self.min_operating_p = min_operating_p

        # Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one.  
        self.normal_pf = normal_pf


        self._contains_synchronous_machines = []
        if contains_synchronous_machines is not None:
            self.contains_synchronous_machines = contains_synchronous_machines
        else:
            self.contains_synchronous_machines = []

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



class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
    """
    # <<< fossil_fuel
    # @generated
    def __init__(self, fossil_fuel_type='oil', thermal_generating_unit=None, *args, **kw_args):
        """ Initialises a new 'FossilFuel' instance.

        @param fossil_fuel_type: The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        @param thermal_generating_unit: A thermal generating unit may have one or more fossil fuels
        """
        # The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        self.fossil_fuel_type = fossil_fuel_type


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(FossilFuel, self).__init__(*args, **kw_args)
    # >>> fossil_fuel

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have one or more fossil fuels
        """
        return self._thermal_generating_unit

    def set_thermal_generating_unit(self, value):
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._fossil_fuels = None

        self._thermal_generating_unit = value
        if self._thermal_generating_unit is not None:
            self._thermal_generating_unit._fossil_fuels = self

    thermal_generating_unit = property(get_thermal_generating_unit, set_thermal_generating_unit)
    # >>> thermal_generating_unit



class HydroPump(IdentifiedObject):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.
    """
    # <<< hydro_pump
    # @generated
    def __init__(self, driven_by_synchronous_machine=None, *args, **kw_args):
        """ Initialises a new 'HydroPump' instance.

        @param driven_by_synchronous_machine: The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """

        self._driven_by_synchronous_machine = None
        self.driven_by_synchronous_machine = driven_by_synchronous_machine


        super(HydroPump, self).__init__(*args, **kw_args)
    # >>> hydro_pump

    # <<< driven_by_synchronous_machine
    # @generated
    def get_driven_by_synchronous_machine(self):
        """ The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
        """
        return self._driven_by_synchronous_machine

    def set_driven_by_synchronous_machine(self, value):
        if self._driven_by_synchronous_machine is not None:
            self._driven_by_synchronous_machine._drives_hydro_pump = None

        self._driven_by_synchronous_machine = value
        if self._driven_by_synchronous_machine is not None:
            self._driven_by_synchronous_machine._drives_hydro_pump = self

    driven_by_synchronous_machine = property(get_driven_by_synchronous_machine, set_driven_by_synchronous_machine)
    # >>> driven_by_synchronous_machine



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
    # <<< thermal_generating_unit
    # @generated
    def __init__(self, fossil_fuels=None, *args, **kw_args):
        """ Initialises a new 'ThermalGeneratingUnit' instance.

        @param fossil_fuels: A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
        """

        self._fossil_fuels = None
        self.fossil_fuels = fossil_fuels


        super(ThermalGeneratingUnit, self).__init__(*args, **kw_args)
    # >>> thermal_generating_unit

    # <<< fossil_fuels
    # @generated
    def get_fossil_fuels(self):
        """ A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
        """
        return self._fossil_fuels

    def set_fossil_fuels(self, value):
        if self._fossil_fuels is not None:
            self._fossil_fuels._thermal_generating_unit = None

        self._fossil_fuels = value
        if self._fossil_fuels is not None:
            self._fossil_fuels._thermal_generating_unit = self

    fossil_fuels = property(get_fossil_fuels, set_fossil_fuels)
    # >>> fossil_fuels



# <<< production
# @generated
# >>> production
