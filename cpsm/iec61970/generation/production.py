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

from cpsm.iec61970.core import Curve
from cpsm.iec61970.core import Equipment

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2008/CIM-schema-cim13#Package_Production"

class GrossToNetActivePowerCurve(Curve):
    """ Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.
    """
    # <<< gross_to_net_active_power_curve
    # @generated
    def __init__(self, generating_unit=None, **kw_args):
        """ Initialises a new 'GrossToNetActivePowerCurve' instance.
        """

        self._generating_unit = None
        self.generating_unit = generating_unit


        super(GrossToNetActivePowerCurve, self).__init__(**kw_args)
    # >>> gross_to_net_active_power_curve

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
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


    def __str__(self):
        """ Returns a string representation of the GrossToNetActivePowerCurve.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< gross_to_net_active_power_curve.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the GrossToNetActivePowerCurve.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "GrossToNetActivePowerCurve", self.uri)
        if format:
            indent += ' ' * depth

        if self.generating_unit is not None:
            s += '%s<%s:GrossToNetActivePowerCurve.generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.generating_unit.uri)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
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
        s += '%s<%s:Curve.x_unit>%s</%s:Curve.x_unit>' % \
            (indent, ns_prefix, self.x_unit, ns_prefix)
        s += '%s<%s:Curve.curve_style>%s</%s:Curve.curve_style>' % \
            (indent, ns_prefix, self.curve_style, ns_prefix)
        s += '%s<%s:Curve.y1_unit>%s</%s:Curve.y1_unit>' % \
            (indent, ns_prefix, self.y1_unit, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GrossToNetActivePowerCurve")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> gross_to_net_active_power_curve.serialize


class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """
    # <<< generating_unit
    # @generated
    def __init__(self, max_operating_p=0.0, normal_pf=0.0, rated_gross_max_p=0.0, rated_gross_min_p=0.0, gen_control_source='off_agc', rated_net_max_p=0.0, long_pf=0.0, initial_p=0.0, short_pf=0.0, min_operating_p=0.0, contains_synchronous_machines=None, gross_to_net_active_power_curves=None, control_area_generating_unit=None, **kw_args):
        """ Initialises a new 'GeneratingUnit' instance.
        """
        # This is the maximum operating active power limit the dispatcher can enter for this unitThis is the maximum operating active power limit the dispatcher can enter for this unit 
        self.max_operating_p = max_operating_p

        # Generating unit economic participation factorGenerating unit economic participation factor 
        self.normal_pf = normal_pf

        # The unit's gross rated maximum capacity (Book Value).The unit's gross rated maximum capacity (Book Value). 
        self.rated_gross_max_p = rated_gross_max_p

        # The gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission gridThe gross rated minimum generation level which the unit can safely operate at while delivering power to the transmission grid 
        self.rated_gross_min_p = rated_gross_min_p

        # The source of controls for a generating unit.The source of controls for a generating unit. Values are: "off_agc", "unavailable", "on_agc", "plant_control"
        self.gen_control_source = 'off_agc'

        # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacityThe net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        self.rated_net_max_p = rated_net_max_p

        # Generating unit economic participation factorGenerating unit economic participation factor 
        self.long_pf = long_pf

        # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configurationDefault Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        self.initial_p = initial_p

        # Generating unit economic participation factorGenerating unit economic participation factor 
        self.short_pf = short_pf

        # This is the minimum operating active power limit the dispatcher can enter for this unit.This is the minimum operating active power limit the dispatcher can enter for this unit. 
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

    # <<< gross_to_net_active_power_curves
    # @generated
    def get_gross_to_net_active_power_curves(self):
        """ A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit
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
        for obj in self.gross_to_net_active_power_curves:
            s += '%s<%s:GeneratingUnit.gross_to_net_active_power_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_gross_max_p>%s</%s:GeneratingUnit.rated_gross_max_p>' % \
            (indent, ns_prefix, self.rated_gross_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_gross_min_p>%s</%s:GeneratingUnit.rated_gross_min_p>' % \
            (indent, ns_prefix, self.rated_gross_min_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.gen_control_source>%s</%s:GeneratingUnit.gen_control_source>' % \
            (indent, ns_prefix, self.gen_control_source, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_net_max_p>%s</%s:GeneratingUnit.rated_net_max_p>' % \
            (indent, ns_prefix, self.rated_net_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.long_pf>%s</%s:GeneratingUnit.long_pf>' % \
            (indent, ns_prefix, self.long_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.initial_p>%s</%s:GeneratingUnit.initial_p>' % \
            (indent, ns_prefix, self.initial_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.short_pf>%s</%s:GeneratingUnit.short_pf>' % \
            (indent, ns_prefix, self.short_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> generating_unit.serialize


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
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gross_to_net_active_power_curves:
            s += '%s<%s:GeneratingUnit.gross_to_net_active_power_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_gross_max_p>%s</%s:GeneratingUnit.rated_gross_max_p>' % \
            (indent, ns_prefix, self.rated_gross_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_gross_min_p>%s</%s:GeneratingUnit.rated_gross_min_p>' % \
            (indent, ns_prefix, self.rated_gross_min_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.gen_control_source>%s</%s:GeneratingUnit.gen_control_source>' % \
            (indent, ns_prefix, self.gen_control_source, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_net_max_p>%s</%s:GeneratingUnit.rated_net_max_p>' % \
            (indent, ns_prefix, self.rated_net_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.long_pf>%s</%s:GeneratingUnit.long_pf>' % \
            (indent, ns_prefix, self.long_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.initial_p>%s</%s:GeneratingUnit.initial_p>' % \
            (indent, ns_prefix, self.initial_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.short_pf>%s</%s:GeneratingUnit.short_pf>' % \
            (indent, ns_prefix, self.short_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)

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
    pass
    # <<< thermal_generating_unit
    # @generated
    def __init__(self, **kw_args):
        """ Initialises a new 'ThermalGeneratingUnit' instance.
        """


        super(ThermalGeneratingUnit, self).__init__(**kw_args)
    # >>> thermal_generating_unit


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

        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uuid>%s</%s:Element.uuid>' % \
            (indent, ns_prefix, self.uuid, ns_prefix)
        s += '%s<%s:IdentifiedObject.path_name>%s</%s:IdentifiedObject.path_name>' % \
            (indent, ns_prefix, self.path_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        for obj in self.contains_measurements:
            s += '%s<%s:PowerSystemResource.contains_measurements rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:Equipment.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        for obj in self.operational_limit_set:
            s += '%s<%s:Equipment.operational_limit_set rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.contains_synchronous_machines:
            s += '%s<%s:GeneratingUnit.contains_synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.gross_to_net_active_power_curves:
            s += '%s<%s:GeneratingUnit.gross_to_net_active_power_curves rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        for obj in self.control_area_generating_unit:
            s += '%s<%s:GeneratingUnit.control_area_generating_unit rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.max_operating_p>%s</%s:GeneratingUnit.max_operating_p>' % \
            (indent, ns_prefix, self.max_operating_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.normal_pf>%s</%s:GeneratingUnit.normal_pf>' % \
            (indent, ns_prefix, self.normal_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_gross_max_p>%s</%s:GeneratingUnit.rated_gross_max_p>' % \
            (indent, ns_prefix, self.rated_gross_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_gross_min_p>%s</%s:GeneratingUnit.rated_gross_min_p>' % \
            (indent, ns_prefix, self.rated_gross_min_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.gen_control_source>%s</%s:GeneratingUnit.gen_control_source>' % \
            (indent, ns_prefix, self.gen_control_source, ns_prefix)
        s += '%s<%s:GeneratingUnit.rated_net_max_p>%s</%s:GeneratingUnit.rated_net_max_p>' % \
            (indent, ns_prefix, self.rated_net_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.long_pf>%s</%s:GeneratingUnit.long_pf>' % \
            (indent, ns_prefix, self.long_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.initial_p>%s</%s:GeneratingUnit.initial_p>' % \
            (indent, ns_prefix, self.initial_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.short_pf>%s</%s:GeneratingUnit.short_pf>' % \
            (indent, ns_prefix, self.short_pf, ns_prefix)
        s += '%s<%s:GeneratingUnit.min_operating_p>%s</%s:GeneratingUnit.min_operating_p>' % \
            (indent, ns_prefix, self.min_operating_p, ns_prefix)

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
