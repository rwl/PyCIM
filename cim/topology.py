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

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""

from cim.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimTopology"

ns_uri = "http://iec.ch/TC57/CIM-generic#Topology"

class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """
    # <<< topological_island
    # @generated
    def __init__(self, topological_nodes=None, angle_ref_topological_node=None, **kw_args):
        """ Initialises a new 'TopologicalIsland' instance.
        """

        self._topological_nodes = []
        if topological_nodes is not None:
            self.topological_nodes = topological_nodes
        else:
            self.topological_nodes = []

        self._angle_ref_topological_node = None
        self.angle_ref_topological_node = angle_ref_topological_node


        super(TopologicalIsland, self).__init__(**kw_args)
    # >>> topological_island

    # <<< topological_nodes
    # @generated
    def get_topological_nodes(self):
        """ A topological node belongs to a topological island
        """
        return self._topological_nodes

    def set_topological_nodes(self, value):
        for x in self._topological_nodes:
            x._topological_island = None
        for y in value:
            y._topological_island = self
        self._topological_nodes = value

    topological_nodes = property(get_topological_nodes, set_topological_nodes)

    def add_topological_nodes(self, *topological_nodes):
        for obj in topological_nodes:
            obj._topological_island = self
            self._topological_nodes.append(obj)

    def remove_topological_nodes(self, *topological_nodes):
        for obj in topological_nodes:
            obj._topological_island = None
            self._topological_nodes.remove(obj)
    # >>> topological_nodes

    # <<< angle_ref_topological_node
    # @generated
    def get_angle_ref_topological_node(self):
        """ The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        """
        return self._angle_ref_topological_node

    def set_angle_ref_topological_node(self, value):
        if self._angle_ref_topological_node is not None:
            self._angle_ref_topological_node._angle_ref_topological_island = None

        self._angle_ref_topological_node = value
        if self._angle_ref_topological_node is not None:
            self._angle_ref_topological_node._angle_ref_topological_island = self

    angle_ref_topological_node = property(get_angle_ref_topological_node, set_angle_ref_topological_node)
    # >>> angle_ref_topological_node


    def __str__(self):
        """ Returns a string representation of the TopologicalIsland.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< topological_island.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TopologicalIsland.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TopologicalIsland", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.topological_nodes:
            s += '%s<%s:TopologicalIsland.topological_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.angle_ref_topological_node is not None:
            s += '%s<%s:TopologicalIsland.angle_ref_topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.angle_ref_topological_node.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TopologicalIsland")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> topological_island.serialize


class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """
    # <<< connectivity_node
    # @generated
    def __init__(self, topological_node=None, member_of_equipment_container=None, bus_name_marker=None, terminals=None, **kw_args):
        """ Initialises a new 'ConnectivityNode' instance.
        """

        self._topological_node = None
        self.topological_node = topological_node

        self._member_of_equipment_container = None
        self.member_of_equipment_container = member_of_equipment_container

        self._bus_name_marker = None
        self.bus_name_marker = bus_name_marker

        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []


        super(ConnectivityNode, self).__init__(**kw_args)
    # >>> connectivity_node

    # <<< topological_node
    # @generated
    def get_topological_node(self):
        """ Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        """
        return self._topological_node

    def set_topological_node(self, value):
        if self._topological_node is not None:
            filtered = [x for x in self.topological_node.connectivity_nodes if x != self]
            self._topological_node._connectivity_nodes = filtered

        self._topological_node = value
        if self._topological_node is not None:
            self._topological_node._connectivity_nodes.append(self)

    topological_node = property(get_topological_node, set_topological_node)
    # >>> topological_node

    # <<< member_of_equipment_container
    # @generated
    def get_member_of_equipment_container(self):
        """ Container of this connectivity node.
        """
        return self._member_of_equipment_container

    def set_member_of_equipment_container(self, value):
        if self._member_of_equipment_container is not None:
            filtered = [x for x in self.member_of_equipment_container.connectivity_nodes if x != self]
            self._member_of_equipment_container._connectivity_nodes = filtered

        self._member_of_equipment_container = value
        if self._member_of_equipment_container is not None:
            self._member_of_equipment_container._connectivity_nodes.append(self)

    member_of_equipment_container = property(get_member_of_equipment_container, set_member_of_equipment_container)
    # >>> member_of_equipment_container

    # <<< bus_name_marker
    # @generated
    def get_bus_name_marker(self):
        """ The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.
        """
        return self._bus_name_marker

    def set_bus_name_marker(self, value):
        if self._bus_name_marker is not None:
            filtered = [x for x in self.bus_name_marker.connectivity_node if x != self]
            self._bus_name_marker._connectivity_node = filtered

        self._bus_name_marker = value
        if self._bus_name_marker is not None:
            self._bus_name_marker._connectivity_node.append(self)

    bus_name_marker = property(get_bus_name_marker, set_bus_name_marker)
    # >>> bus_name_marker

    # <<< terminals
    # @generated
    def get_terminals(self):
        """ Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._terminals

    def set_terminals(self, value):
        for x in self._terminals:
            x._connectivity_node = None
        for y in value:
            y._connectivity_node = self
        self._terminals = value

    terminals = property(get_terminals, set_terminals)

    def add_terminals(self, *terminals):
        for obj in terminals:
            obj._connectivity_node = self
            self._terminals.append(obj)

    def remove_terminals(self, *terminals):
        for obj in terminals:
            obj._connectivity_node = None
            self._terminals.remove(obj)
    # >>> terminals


    def __str__(self):
        """ Returns a string representation of the ConnectivityNode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< connectivity_node.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the ConnectivityNode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "ConnectivityNode", self.uri)
        if format:
            indent += ' ' * depth

        if self.topological_node is not None:
            s += '%s<%s:ConnectivityNode.topological_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.topological_node.uri)
        if self.member_of_equipment_container is not None:
            s += '%s<%s:ConnectivityNode.member_of_equipment_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.member_of_equipment_container.uri)
        if self.bus_name_marker is not None:
            s += '%s<%s:ConnectivityNode.bus_name_marker rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.bus_name_marker.uri)
        for obj in self.terminals:
            s += '%s<%s:ConnectivityNode.terminals rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "ConnectivityNode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> connectivity_node.serialize


class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """
    # <<< topological_node
    # @generated
    def __init__(self, equivalent=False, load_carrying=False, net_injection_p=0.0, voltage=0.0, x0_per_x=0.0, net_injection_q=0.0, s_short_circuit=0.0, r0_per_r=0.0, x_per_r=0.0, phase_angle=0.0, energized=False, observability_flag=False, connectivity_nodes=None, connectivity_node_container=None, base_voltage=None, sv_injection=None, reporting_group=None, topological_island=None, terminal=None, angle_ref_topological_island=None, sv_voltage=None, control_area=None, **kw_args):
        """ Initialises a new 'TopologicalNode' instance.
        """
        # The topological node is equivalent and not real equipment. 
        self.equivalent = equivalent

        # True if node is load carrying 
        self.load_carrying = load_carrying

        # Net injection active power 
        self.net_injection_p = net_injection_p

        # Voltage of node 
        self.voltage = voltage

        # The ratio of zero sequence reactance per positive sequence reactance. 
        self.x0_per_x = x0_per_x

        # Net injection reactive power 
        self.net_injection_q = net_injection_q

        # The short circuit apparent power drawn at this node when faulted. 
        self.s_short_circuit = s_short_circuit

        # The ratio of zero sequence resistance to positive sequence resistance. 
        self.r0_per_r = r0_per_r

        # Ratio of positive sequence reactance per postive sequence resistance. 
        self.x_per_r = x_per_r

        # Phase angle of node 
        self.phase_angle = phase_angle

        # True if node energized 
        self.energized = energized

        # The observability status of the node. 
        self.observability_flag = observability_flag


        self._connectivity_nodes = []
        if connectivity_nodes is not None:
            self.connectivity_nodes = connectivity_nodes
        else:
            self.connectivity_nodes = []

        self._connectivity_node_container = None
        self.connectivity_node_container = connectivity_node_container

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._sv_injection = None
        self.sv_injection = sv_injection

        self._reporting_group = None
        self.reporting_group = reporting_group

        self._topological_island = None
        self.topological_island = topological_island

        self._terminal = []
        if terminal is not None:
            self.terminal = terminal
        else:
            self.terminal = []

        self._angle_ref_topological_island = None
        self.angle_ref_topological_island = angle_ref_topological_island

        self._sv_voltage = None
        self.sv_voltage = sv_voltage

        self._control_area = None
        self.control_area = control_area


        super(TopologicalNode, self).__init__(**kw_args)
    # >>> topological_node

    # <<< connectivity_nodes
    # @generated
    def get_connectivity_nodes(self):
        """ Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        """
        return self._connectivity_nodes

    def set_connectivity_nodes(self, value):
        for x in self._connectivity_nodes:
            x._topological_node = None
        for y in value:
            y._topological_node = self
        self._connectivity_nodes = value

    connectivity_nodes = property(get_connectivity_nodes, set_connectivity_nodes)

    def add_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._topological_node = self
            self._connectivity_nodes.append(obj)

    def remove_connectivity_nodes(self, *connectivity_nodes):
        for obj in connectivity_nodes:
            obj._topological_node = None
            self._connectivity_nodes.remove(obj)
    # >>> connectivity_nodes

    # <<< connectivity_node_container
    # @generated
    def get_connectivity_node_container(self):
        """ The connectivity node container to which the toplogical node belongs.
        """
        return self._connectivity_node_container

    def set_connectivity_node_container(self, value):
        if self._connectivity_node_container is not None:
            filtered = [x for x in self.connectivity_node_container.topological_node if x != self]
            self._connectivity_node_container._topological_node = filtered

        self._connectivity_node_container = value
        if self._connectivity_node_container is not None:
            self._connectivity_node_container._topological_node.append(self)

    connectivity_node_container = property(get_connectivity_node_container, set_connectivity_node_container)
    # >>> connectivity_node_container

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ The base voltage of the topologocial node.
        """
        return self._base_voltage

    def set_base_voltage(self, value):
        if self._base_voltage is not None:
            filtered = [x for x in self.base_voltage.topological_node if x != self]
            self._base_voltage._topological_node = filtered

        self._base_voltage = value
        if self._base_voltage is not None:
            self._base_voltage._topological_node.append(self)

    base_voltage = property(get_base_voltage, set_base_voltage)
    # >>> base_voltage

    # <<< sv_injection
    # @generated
    def get_sv_injection(self):
        """ The injection state associated with the topological node.
        """
        return self._sv_injection

    def set_sv_injection(self, value):
        if self._sv_injection is not None:
            self._sv_injection._topological_node = None

        self._sv_injection = value
        if self._sv_injection is not None:
            self._sv_injection._topological_node = self

    sv_injection = property(get_sv_injection, set_sv_injection)
    # >>> sv_injection

    # <<< reporting_group
    # @generated
    def get_reporting_group(self):
        """ The reporting group to which the topological node belongs.
        """
        return self._reporting_group

    def set_reporting_group(self, value):
        if self._reporting_group is not None:
            filtered = [x for x in self.reporting_group.topological_node if x != self]
            self._reporting_group._topological_node = filtered

        self._reporting_group = value
        if self._reporting_group is not None:
            self._reporting_group._topological_node.append(self)

    reporting_group = property(get_reporting_group, set_reporting_group)
    # >>> reporting_group

    # <<< topological_island
    # @generated
    def get_topological_island(self):
        """ A topological node belongs to a topological island
        """
        return self._topological_island

    def set_topological_island(self, value):
        if self._topological_island is not None:
            filtered = [x for x in self.topological_island.topological_nodes if x != self]
            self._topological_island._topological_nodes = filtered

        self._topological_island = value
        if self._topological_island is not None:
            self._topological_island._topological_nodes.append(self)

    topological_island = property(get_topological_island, set_topological_island)
    # >>> topological_island

    # <<< terminal
    # @generated
    def get_terminal(self):
        """ The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._terminal

    def set_terminal(self, value):
        for x in self._terminal:
            x._topological_node = None
        for y in value:
            y._topological_node = self
        self._terminal = value

    terminal = property(get_terminal, set_terminal)

    def add_terminal(self, *terminal):
        for obj in terminal:
            obj._topological_node = self
            self._terminal.append(obj)

    def remove_terminal(self, *terminal):
        for obj in terminal:
            obj._topological_node = None
            self._terminal.remove(obj)
    # >>> terminal

    # <<< angle_ref_topological_island
    # @generated
    def get_angle_ref_topological_island(self):
        """ The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        """
        return self._angle_ref_topological_island

    def set_angle_ref_topological_island(self, value):
        if self._angle_ref_topological_island is not None:
            self._angle_ref_topological_island._angle_ref_topological_node = None

        self._angle_ref_topological_island = value
        if self._angle_ref_topological_island is not None:
            self._angle_ref_topological_island._angle_ref_topological_node = self

    angle_ref_topological_island = property(get_angle_ref_topological_island, set_angle_ref_topological_island)
    # >>> angle_ref_topological_island

    # <<< sv_voltage
    # @generated
    def get_sv_voltage(self):
        """ The state voltage associated with the topological node.
        """
        return self._sv_voltage

    def set_sv_voltage(self, value):
        if self._sv_voltage is not None:
            self._sv_voltage._topological_node = None

        self._sv_voltage = value
        if self._sv_voltage is not None:
            self._sv_voltage._topological_node = self

    sv_voltage = property(get_sv_voltage, set_sv_voltage)
    # >>> sv_voltage

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The control area into which the node is included.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            filtered = [x for x in self.control_area.topological_node if x != self]
            self._control_area._topological_node = filtered

        self._control_area = value
        if self._control_area is not None:
            self._control_area._topological_node.append(self)

    control_area = property(get_control_area, set_control_area)
    # >>> control_area


    def __str__(self):
        """ Returns a string representation of the TopologicalNode.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< topological_node.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the TopologicalNode.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "TopologicalNode", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.connectivity_nodes:
            s += '%s<%s:TopologicalNode.connectivity_nodes rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.connectivity_node_container is not None:
            s += '%s<%s:TopologicalNode.connectivity_node_container rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.connectivity_node_container.uri)
        if self.base_voltage is not None:
            s += '%s<%s:TopologicalNode.base_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.base_voltage.uri)
        if self.sv_injection is not None:
            s += '%s<%s:TopologicalNode.sv_injection rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_injection.uri)
        if self.reporting_group is not None:
            s += '%s<%s:TopologicalNode.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reporting_group.uri)
        if self.topological_island is not None:
            s += '%s<%s:TopologicalNode.topological_island rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.topological_island.uri)
        for obj in self.terminal:
            s += '%s<%s:TopologicalNode.terminal rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.angle_ref_topological_island is not None:
            s += '%s<%s:TopologicalNode.angle_ref_topological_island rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.angle_ref_topological_island.uri)
        if self.sv_voltage is not None:
            s += '%s<%s:TopologicalNode.sv_voltage rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.sv_voltage.uri)
        if self.control_area is not None:
            s += '%s<%s:TopologicalNode.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
        s += '%s<%s:TopologicalNode.equivalent>%s</%s:TopologicalNode.equivalent>' % \
            (indent, ns_prefix, self.equivalent, ns_prefix)
        s += '%s<%s:TopologicalNode.load_carrying>%s</%s:TopologicalNode.load_carrying>' % \
            (indent, ns_prefix, self.load_carrying, ns_prefix)
        s += '%s<%s:TopologicalNode.net_injection_p>%s</%s:TopologicalNode.net_injection_p>' % \
            (indent, ns_prefix, self.net_injection_p, ns_prefix)
        s += '%s<%s:TopologicalNode.voltage>%s</%s:TopologicalNode.voltage>' % \
            (indent, ns_prefix, self.voltage, ns_prefix)
        s += '%s<%s:TopologicalNode.x0_per_x>%s</%s:TopologicalNode.x0_per_x>' % \
            (indent, ns_prefix, self.x0_per_x, ns_prefix)
        s += '%s<%s:TopologicalNode.net_injection_q>%s</%s:TopologicalNode.net_injection_q>' % \
            (indent, ns_prefix, self.net_injection_q, ns_prefix)
        s += '%s<%s:TopologicalNode.s_short_circuit>%s</%s:TopologicalNode.s_short_circuit>' % \
            (indent, ns_prefix, self.s_short_circuit, ns_prefix)
        s += '%s<%s:TopologicalNode.r0_per_r>%s</%s:TopologicalNode.r0_per_r>' % \
            (indent, ns_prefix, self.r0_per_r, ns_prefix)
        s += '%s<%s:TopologicalNode.x_per_r>%s</%s:TopologicalNode.x_per_r>' % \
            (indent, ns_prefix, self.x_per_r, ns_prefix)
        s += '%s<%s:TopologicalNode.phase_angle>%s</%s:TopologicalNode.phase_angle>' % \
            (indent, ns_prefix, self.phase_angle, ns_prefix)
        s += '%s<%s:TopologicalNode.energized>%s</%s:TopologicalNode.energized>' % \
            (indent, ns_prefix, self.energized, ns_prefix)
        s += '%s<%s:TopologicalNode.observability_flag>%s</%s:TopologicalNode.observability_flag>' % \
            (indent, ns_prefix, self.observability_flag, ns_prefix)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "TopologicalNode")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> topological_node.serialize


class BusNameMarker(IdentifiedObject):
    """ Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """
    # <<< bus_name_marker
    # @generated
    def __init__(self, connectivity_node=None, reporting_group=None, control_area=None, **kw_args):
        """ Initialises a new 'BusNameMarker' instance.
        """

        self._connectivity_node = []
        if connectivity_node is not None:
            self.connectivity_node = connectivity_node
        else:
            self.connectivity_node = []

        self._reporting_group = None
        self.reporting_group = reporting_group

        self._control_area = None
        self.control_area = control_area


        super(BusNameMarker, self).__init__(**kw_args)
    # >>> bus_name_marker

    # <<< connectivity_node
    # @generated
    def get_connectivity_node(self):
        """ The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
        """
        return self._connectivity_node

    def set_connectivity_node(self, value):
        for x in self._connectivity_node:
            x._bus_name_marker = None
        for y in value:
            y._bus_name_marker = self
        self._connectivity_node = value

    connectivity_node = property(get_connectivity_node, set_connectivity_node)

    def add_connectivity_node(self, *connectivity_node):
        for obj in connectivity_node:
            obj._bus_name_marker = self
            self._connectivity_node.append(obj)

    def remove_connectivity_node(self, *connectivity_node):
        for obj in connectivity_node:
            obj._bus_name_marker = None
            self._connectivity_node.remove(obj)
    # >>> connectivity_node

    # <<< reporting_group
    # @generated
    def get_reporting_group(self):
        """ The reporting group to which this BusNameMarker belongs.
        """
        return self._reporting_group

    def set_reporting_group(self, value):
        if self._reporting_group is not None:
            filtered = [x for x in self.reporting_group.bus_name_marker if x != self]
            self._reporting_group._bus_name_marker = filtered

        self._reporting_group = value
        if self._reporting_group is not None:
            self._reporting_group._bus_name_marker.append(self)

    reporting_group = property(get_reporting_group, set_reporting_group)
    # >>> reporting_group

    # <<< control_area
    # @generated
    def get_control_area(self):
        """ The control area into which the BusNameMarker is included.
        """
        return self._control_area

    def set_control_area(self, value):
        if self._control_area is not None:
            filtered = [x for x in self.control_area.bus_name_marker if x != self]
            self._control_area._bus_name_marker = filtered

        self._control_area = value
        if self._control_area is not None:
            self._control_area._bus_name_marker.append(self)

    control_area = property(get_control_area, set_control_area)
    # >>> control_area


    def __str__(self):
        """ Returns a string representation of the BusNameMarker.
        """
        return self.serialize(header=True, depth=2, format=True)


    # <<< bus_name_marker.serialize
    # @generated
    def serialize(self, header=False, depth=0, format=False):
        """ Returns an RDF/XML representation of the BusNameMarker.
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

        s += '%s<%s:%s rdf:ID="%s">' % (indent, ns_prefix, "BusNameMarker", self.uri)
        if format:
            indent += ' ' * depth

        for obj in self.connectivity_node:
            s += '%s<%s:BusNameMarker.connectivity_node rdf:resource="#%s"/>' % \
                (indent, ns_prefix, obj.uri)
        if self.reporting_group is not None:
            s += '%s<%s:BusNameMarker.reporting_group rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.reporting_group.uri)
        if self.control_area is not None:
            s += '%s<%s:BusNameMarker.control_area rdf:resource="#%s"/>' % \
                (indent, ns_prefix, self.control_area.uri)
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

        if format:
            indent = indent[:-depth]
        s += '%s</%s:%s>' % (indent, ns_prefix, "BusNameMarker")

        if header:
            s += '%s</rdf:RDF>' % indent[:-depth]

        return s
    # >>> bus_name_marker.serialize


# <<< topology
# @generated
# >>> topology
