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

from cdpsm.iec61970.core import Equipment

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Production"

class GeneratingUnit(Equipment):
    """ A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.
    """
    # <<< generating_unit
    # @generated
    def __init__(self, rated_net_max_p=0.0, gen_control_source='on_agc', initial_p=0.0, synchronous_machines=None, **kw_args):
        """ Initialises a new 'GeneratingUnit' instance.
        """
        # The net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacityThe net rated maximum capacity determined by subtracting the auxiliary power used to operate the internal plant machinery from the rated gross maximum capacity 
        self.rated_net_max_p = rated_net_max_p

        # The source of controls for a generating unit.The source of controls for a generating unit. Values are: "on_agc", "unavailable", "plant_control", "off_agc"
        self.gen_control_source = 'on_agc'

        # Default Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configurationDefault Initial active power  which is used to store a powerflow result for the initial active power for this unit in this network configuration 
        self.initial_p = initial_p


        self._synchronous_machines = []
        if synchronous_machines is not None:
            self.synchronous_machines = synchronous_machines
        else:
            self.synchronous_machines = []


        super(GeneratingUnit, self).__init__(**kw_args)
    # >>> generating_unit

    # <<< synchronous_machines
    # @generated
    def get_synchronous_machines(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
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

        for obj in self.synchronous_machines:
            s += '%s<%s:GeneratingUnit.synchronous_machines rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        s += '%s<%s:GeneratingUnit.rated_net_max_p>%s</%s:GeneratingUnit.rated_net_max_p>' % \
            (indent, ns_prefix, self.rated_net_max_p, ns_prefix)
        s += '%s<%s:GeneratingUnit.gen_control_source>%s</%s:GeneratingUnit.gen_control_source>' % \
            (indent, ns_prefix, self.gen_control_source, ns_prefix)
        s += '%s<%s:GeneratingUnit.initial_p>%s</%s:GeneratingUnit.initial_p>' % \
            (indent, ns_prefix, self.initial_p, ns_prefix)
        if self.model is not None:
            s += '%s<%s:Element.model rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.model.uri)
        s += '%s<%s:Element.uri>%s</%s:Element.uri>' % \
            (indent, ns_prefix, self.uri, ns_prefix)
        s += '%s<%s:IdentifiedObject.m_rid>%s</%s:IdentifiedObject.m_rid>' % \
            (indent, ns_prefix, self.m_rid, ns_prefix)
        s += '%s<%s:IdentifiedObject.description>%s</%s:IdentifiedObject.description>' % \
            (indent, ns_prefix, self.description, ns_prefix)
        s += '%s<%s:IdentifiedObject.name>%s</%s:IdentifiedObject.name>' % \
            (indent, ns_prefix, self.name, ns_prefix)
        s += '%s<%s:IdentifiedObject.local_name>%s</%s:IdentifiedObject.local_name>' % \
            (indent, ns_prefix, self.local_name, ns_prefix)
        s += '%s<%s:IdentifiedObject.alias_name>%s</%s:IdentifiedObject.alias_name>' % \
            (indent, ns_prefix, self.alias_name, ns_prefix)
        if self.geo_location is not None:
            s += '%s<%s:PowerSystemResource.geo_location rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.geo_location.uri)
        if self.psrtype is not None:
            s += '%s<%s:PowerSystemResource.psrtype rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.psrtype.uri)
        if self.equipment_container is not None:
            s += '%s<%s:Equipment.equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.equipment_container.uri)
        s += '%s<%s:Equipment.norma_ily_in_service>%s</%s:Equipment.norma_ily_in_service>' % \
            (indent, ns_prefix, self.norma_ily_in_service, ns_prefix)

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "GeneratingUnit")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> generating_unit.serialize


# <<< production
# @generated
# >>> production
