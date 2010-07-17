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

""" The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.The production package is responsible for classes which describe various kinds of generators. These classes also provide production costing information which is used to economically allocate demand among committed units and calculate reserve quantities.
"""

from ucte.core import Equipment
from ucte.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Production"

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
    """
    # <<< generating_unit
    # @generated
    def __init__(self, max_operating_p=0.0, startup_cost=0.0, nominal_p=0.0, governor_scd=0.0, maximum_allowable_spinning_reserve=0.0, variable_cost=0.0, min_operating_p=0.0, normal_pf=0.0, contains_synchronous_machines=None, control_area_generating_unit=None, **kw_args):
        """ Initialises a new 'GeneratingUnit' instance.
        """
        # This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit 
        self.max_operating_p = max_operating_p

        # The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only.The initial startup cost incurred for each start of the GeneratingUnit.This is for Short Circuit only. 
        self.startup_cost = startup_cost

        # The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute).The nominal power of the generating unit.  Used to give precise meaning to percentage based attributes such as the govenor speed change droop (govenorSCD attribute). 
        self.nominal_p = nominal_p

        # Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only.Governor Speed Changer Droop.   This is the change in generator power output divided by the change in frequency normalized by the nominal power of the generator and the nominal frequency and expressed in percent and negated. A positive value of speed change droop provides additional generator output upon a drop in frequency.This is for Short Circuit Only. 
        self.governor_scd = governor_scd

        # Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point.Maximum allowable spinning reserve. Spinning reserve will never be considered greater than this value regardless of the current operating point. 
        self.maximum_allowable_spinning_reserve = maximum_allowable_spinning_reserve

        # The variable cost component of production per unit of ActivePower.This is for Short Circuit only.The variable cost component of production per unit of ActivePower.This is for Short Circuit only. 
        self.variable_cost = variable_cost

        # This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit. 
        self.min_operating_p = min_operating_p

        # Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one. Generating unit economic participation factorFor UCTE only one Generating per control area should be non-zero.  The attribute is optional on a GeneratingUnit and the value can be assumed to be zero if missing.   This minimizes the data that must be exchanged.   By convention the non-zero value is specified as one.  
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


        super(GeneratingUnit, self).__init__(**kw_args)
    # >>> generating_unit

    # <<< contains_synchronous_machines
    # @generated
    def get_contains_synchronous_machines(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
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
        """ ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.
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


    def __str__(self):
        """ Returns a string representation of the GeneratingUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< generating_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GeneratingUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GeneratingUnit", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.startup_cost>%s</%s:GeneratingUnit.startup_cost>' % \
            (indent, ns_prefix, self.startup_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.nominal_p>%s</%s:GeneratingUnit.nominal_p>' % \
            (indent, ns_prefix, self.nominal_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.governor_scd>%s</%s:GeneratingUnit.governor_scd>' % \
            (indent, ns_prefix, self.governor_scd, ns_prefix)
        s += '%s<%s:GeneratingUnit.maximum_allowable_spinning_reserve>%s</%s:GeneratingUnit.maximum_allowable_spinning_reserve>' % \
            (indent, ns_prefix, self.maximum_allowable_spinning_reserve, ns_prefix)
        s += '%s<%s:GeneratingUnit.variable_cost>%s</%s:GeneratingUnit.variable_cost>' % \
            (indent, ns_prefix, self.variable_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> generating_unit.serialize


class FossilFuel(IdentifiedObject):
    """ The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
    """
    # <<< fossil_fuel
    # @generated
    def __init__(self, fossil_fuel_type='oil', thermal_generating_unit=None, **kw_args):
        """ Initialises a new 'FossilFuel' instance.
        """
        # The type of fossil fuel, such as coal, oil, or gas.The type of fossil fuel, such as coal, oil, or gas. Values are: "oil", "coal", "lignite", "gas"
        self.fossil_fuel_type = 'oil'


        self._thermal_generating_unit = None
        self.thermal_generating_unit = thermal_generating_unit


        super(FossilFuel, self).__init__(**kw_args)
    # >>> fossil_fuel

    # <<< thermal_generating_unit
    # @generated
    def get_thermal_generating_unit(self):
        """ A thermal generating unit may have one or more fossil fuelsA thermal generating unit may have one or more fossil fuels
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


    def __str__(self):
        """ Returns a string representation of the FossilFuel.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< fossil_fuel.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the FossilFuel.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "FossilFuel", self.uri)
        if format:
            indent += ' ' * depth

        if self.thermal_generating_unit is not None:
            s += '%s<%s:FossilFuel.thermal_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.thermal_generating_unit.uri)
        s += '%s<%s:FossilFuel.fossil_fuel_type>%s</%s:FossilFuel.fossil_fuel_type>' % \
            (indent, ns_prefix, self.fossil_fuel_type, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "FossilFuel")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> fossil_fuel.serialize


class HydroPump(IdentifiedObject):
    """ A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.
    """
    # <<< hydro_pump
    # @generated
    def __init__(self, driven_by_synchronous_machine=None, **kw_args):
        """ Initialises a new 'HydroPump' instance.
        """

        self._driven_by_synchronous_machine = None
        self.driven_by_synchronous_machine = driven_by_synchronous_machine


        super(HydroPump, self).__init__(**kw_args)
    # >>> hydro_pump

    # <<< driven_by_synchronous_machine
    # @generated
    def get_driven_by_synchronous_machine(self):
        """ The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
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


    def __str__(self):
        """ Returns a string representation of the HydroPump.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< hydro_pump.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the HydroPump.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "HydroPump", self.uri)
        if format:
            indent += ' ' * depth

        if self.driven_by_synchronous_machine is not None:
            s += '%s<%s:HydroPump.driven_by_synchronous_machine rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.driven_by_synchronous_machine.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "HydroPump")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> hydro_pump.serialize


class WindGeneratingUnit(GeneratingUnit):
    """ A wind driven generating unit.A wind driven generating unit.
    """
    pass
    # <<< wind_generating_unit
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'WindGeneratingUnit' instance.
        """


        super(WindGeneratingUnit, self).__init__(**kw_args)
    # >>> wind_generating_unit


    def __str__(self):
        """ Returns a string representation of the WindGeneratingUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< wind_generating_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the WindGeneratingUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "WindGeneratingUnit", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.startup_cost>%s</%s:GeneratingUnit.startup_cost>' % \
            (indent, ns_prefix, self.startup_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.nominal_p>%s</%s:GeneratingUnit.nominal_p>' % \
            (indent, ns_prefix, self.nominal_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.governor_scd>%s</%s:GeneratingUnit.governor_scd>' % \
            (indent, ns_prefix, self.governor_scd, ns_prefix)
        s += '%s<%s:GeneratingUnit.maximum_allowable_spinning_reserve>%s</%s:GeneratingUnit.maximum_allowable_spinning_reserve>' % \
            (indent, ns_prefix, self.maximum_allowable_spinning_reserve, ns_prefix)
        s += '%s<%s:GeneratingUnit.variable_cost>%s</%s:GeneratingUnit.variable_cost>' % \
            (indent, ns_prefix, self.variable_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "WindGeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> wind_generating_unit.serialize


class NuclearGeneratingUnit(GeneratingUnit):
    """ A nuclear generating unit.A nuclear generating unit.
    """
    pass
    # <<< nuclear_generating_unit
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'NuclearGeneratingUnit' instance.
        """


        super(NuclearGeneratingUnit, self).__init__(**kw_args)
    # >>> nuclear_generating_unit


    def __str__(self):
        """ Returns a string representation of the NuclearGeneratingUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< nuclear_generating_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the NuclearGeneratingUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "NuclearGeneratingUnit", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.startup_cost>%s</%s:GeneratingUnit.startup_cost>' % \
            (indent, ns_prefix, self.startup_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.nominal_p>%s</%s:GeneratingUnit.nominal_p>' % \
            (indent, ns_prefix, self.nominal_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.governor_scd>%s</%s:GeneratingUnit.governor_scd>' % \
            (indent, ns_prefix, self.governor_scd, ns_prefix)
        s += '%s<%s:GeneratingUnit.maximum_allowable_spinning_reserve>%s</%s:GeneratingUnit.maximum_allowable_spinning_reserve>' % \
            (indent, ns_prefix, self.maximum_allowable_spinning_reserve, ns_prefix)
        s += '%s<%s:GeneratingUnit.variable_cost>%s</%s:GeneratingUnit.variable_cost>' % \
            (indent, ns_prefix, self.variable_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "NuclearGeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> nuclear_generating_unit.serialize


class HydroGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)
    """
    pass
    # <<< hydro_generating_unit
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'HydroGeneratingUnit' instance.
        """


        super(HydroGeneratingUnit, self).__init__(**kw_args)
    # >>> hydro_generating_unit


    def __str__(self):
        """ Returns a string representation of the HydroGeneratingUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< hydro_generating_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the HydroGeneratingUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "HydroGeneratingUnit", self.uri)
        if format:
            indent += ' ' * depth

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.startup_cost>%s</%s:GeneratingUnit.startup_cost>' % \
            (indent, ns_prefix, self.startup_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.nominal_p>%s</%s:GeneratingUnit.nominal_p>' % \
            (indent, ns_prefix, self.nominal_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.governor_scd>%s</%s:GeneratingUnit.governor_scd>' % \
            (indent, ns_prefix, self.governor_scd, ns_prefix)
        s += '%s<%s:GeneratingUnit.maximum_allowable_spinning_reserve>%s</%s:GeneratingUnit.maximum_allowable_spinning_reserve>' % \
            (indent, ns_prefix, self.maximum_allowable_spinning_reserve, ns_prefix)
        s += '%s<%s:GeneratingUnit.variable_cost>%s</%s:GeneratingUnit.variable_cost>' % \
            (indent, ns_prefix, self.variable_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "HydroGeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> hydro_generating_unit.serialize


class ThermalGeneratingUnit(GeneratingUnit):
    """ A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.
    """
    # <<< thermal_generating_unit
    # @generated
    def __init__(self, fossil_fuels=None, **kw_args):
        """ Initialises a new 'ThermalGeneratingUnit' instance.
        """

        self._fossil_fuels = None
        self.fossil_fuels = fossil_fuels


        super(ThermalGeneratingUnit, self).__init__(**kw_args)
    # >>> thermal_generating_unit

    # <<< fossil_fuels
    # @generated
    def get_fossil_fuels(self):
        """ A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.A thermal generating unit may have one or more fossil fuelsThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit.
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


    def __str__(self):
        """ Returns a string representation of the ThermalGeneratingUnit.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< thermal_generating_unit.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ThermalGeneratingUnit.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ThermalGeneratingUnit", self.uri)
        if format:
            indent += ' ' * depth

        if self.fossil_fuels is not None:
            s += '%s<%s:ThermalGeneratingUnit.fossil_fuels rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.fossil_fuels.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        s += '%s<%s:Equipment.equivalent>%s</%s:Equipment.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.startup_cost>%s</%s:GeneratingUnit.startup_cost>' % \
            (indent, ns_prefix, self.startup_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.nominal_p>%s</%s:GeneratingUnit.nominal_p>' % \
            (indent, ns_prefix, self.nominal_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.governor_scd>%s</%s:GeneratingUnit.governor_scd>' % \
            (indent, ns_prefix, self.governor_scd, ns_prefix)
        s += '%s<%s:GeneratingUnit.maximum_allowable_spinning_reserve>%s</%s:GeneratingUnit.maximum_allowable_spinning_reserve>' % \
            (indent, ns_prefix, self.maximum_allowable_spinning_reserve, ns_prefix)
        s += '%s<%s:GeneratingUnit.variable_cost>%s</%s:GeneratingUnit.variable_cost>' % \
            (indent, ns_prefix, self.variable_cost, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ThermalGeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> thermal_generating_unit.serialize


# <<< production
# @generated
# >>> production
