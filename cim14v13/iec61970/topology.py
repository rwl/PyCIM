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

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""

from cim14v13.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimTopology"

ns_uri = "http://iec.ch/TC57/CIM-generic#Topology"

class BusNameMarker(IdentifiedObject):
    """ Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """
    # <<< bus_name_marker
    # @generated
    def __init__(self, connectivity_node=None, reporting_group=None, *args, **kw_args):
        """ Initialises a new 'BusNameMarker' instance.

        @param connectivity_node: The list of nodes which have the same bus name in the normal  topology.  Note that this list of ConnectivityNodes should be connected by objects derived from Switch that are normally closed.
        @param reporting_group: The reporting group to which this BusNameMarker belongs.
        """

        self._connectivity_node = []
        if connectivity_node is not None:
            self.connectivity_node = connectivity_node
        else:
            self.connectivity_node = []

        self._reporting_group = None
        self.reporting_group = reporting_group


        super(BusNameMarker, self).__init__(*args, **kw_args)
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



class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """
    # <<< connectivity_node
    # @generated
    def __init__(self, pnode=None, bus_name_marker=None, loss_penalty_factors=None, topological_node=None, node_constraint_terms=None, terminals=None, connectivity_node_container=None, *args, **kw_args):
        """ Initialises a new 'ConnectivityNode' instance.

        @param pnode:
        @param bus_name_marker: The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.
        @param loss_penalty_factors:
        @param topological_node: Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        @param node_constraint_terms:
        @param terminals: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        @param connectivity_node_container: Container of this connectivity node.
        """

        self._pnode = None
        self.pnode = pnode

        self._bus_name_marker = None
        self.bus_name_marker = bus_name_marker

        self._loss_penalty_factors = []
        if loss_penalty_factors is not None:
            self.loss_penalty_factors = loss_penalty_factors
        else:
            self.loss_penalty_factors = []

        self._topological_node = None
        self.topological_node = topological_node

        self._node_constraint_terms = []
        if node_constraint_terms is not None:
            self.node_constraint_terms = node_constraint_terms
        else:
            self.node_constraint_terms = []

        self._terminals = []
        if terminals is not None:
            self.terminals = terminals
        else:
            self.terminals = []

        self._connectivity_node_container = None
        self.connectivity_node_container = connectivity_node_container


        super(ConnectivityNode, self).__init__(*args, **kw_args)
    # >>> connectivity_node

    # <<< pnode
    # @generated
    def get_pnode(self):
        """ 
        """
        return self._pnode

    def set_pnode(self, value):
        if self._pnode is not None:
            self._pnode._connectivity_node = None

        self._pnode = value
        if self._pnode is not None:
            self._pnode._connectivity_node = self

    pnode = property(get_pnode, set_pnode)
    # >>> pnode

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

    # <<< loss_penalty_factors
    # @generated
    def get_loss_penalty_factors(self):
        """ 
        """
        return self._loss_penalty_factors

    def set_loss_penalty_factors(self, value):
        for p in self._loss_penalty_factors:
            filtered = [q for q in p.connectivity_nodes if q != self]
            self._loss_penalty_factors._connectivity_nodes = filtered
        for r in value:
            if self not in r._connectivity_nodes:
                r._connectivity_nodes.append(self)
        self._loss_penalty_factors = value

    loss_penalty_factors = property(get_loss_penalty_factors, set_loss_penalty_factors)

    def add_loss_penalty_factors(self, *loss_penalty_factors):
        for obj in loss_penalty_factors:
            if self not in obj._connectivity_nodes:
                obj._connectivity_nodes.append(self)
            self._loss_penalty_factors.append(obj)

    def remove_loss_penalty_factors(self, *loss_penalty_factors):
        for obj in loss_penalty_factors:
            if self in obj._connectivity_nodes:
                obj._connectivity_nodes.remove(self)
            self._loss_penalty_factors.remove(obj)
    # >>> loss_penalty_factors

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

    # <<< node_constraint_terms
    # @generated
    def get_node_constraint_terms(self):
        """ 
        """
        return self._node_constraint_terms

    def set_node_constraint_terms(self, value):
        for x in self._node_constraint_terms:
            x._connectivity_node = None
        for y in value:
            y._connectivity_node = self
        self._node_constraint_terms = value

    node_constraint_terms = property(get_node_constraint_terms, set_node_constraint_terms)

    def add_node_constraint_terms(self, *node_constraint_terms):
        for obj in node_constraint_terms:
            obj._connectivity_node = self
            self._node_constraint_terms.append(obj)

    def remove_node_constraint_terms(self, *node_constraint_terms):
        for obj in node_constraint_terms:
            obj._connectivity_node = None
            self._node_constraint_terms.remove(obj)
    # >>> node_constraint_terms

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

    # <<< connectivity_node_container
    # @generated
    def get_connectivity_node_container(self):
        """ Container of this connectivity node.
        """
        return self._connectivity_node_container

    def set_connectivity_node_container(self, value):
        if self._connectivity_node_container is not None:
            filtered = [x for x in self.connectivity_node_container.connectivity_nodes if x != self]
            self._connectivity_node_container._connectivity_nodes = filtered

        self._connectivity_node_container = value
        if self._connectivity_node_container is not None:
            self._connectivity_node_container._connectivity_nodes.append(self)

    connectivity_node_container = property(get_connectivity_node_container, set_connectivity_node_container)
    # >>> connectivity_node_container



class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """
    # <<< topological_node
    # @generated
    def __init__(self, sv_voltage=None, reporting_group=None, terminal=None, sv_short_circuit=None, sv_injection=None, angle_ref_topological_island=None, connectivity_nodes=None, connectivity_node_container=None, base_voltage=None, topological_island=None, *args, **kw_args):
        """ Initialises a new 'TopologicalNode' instance.

        @param sv_voltage: The state voltage associated with the topological node.
        @param reporting_group: The reporting group to which the topological node belongs.
        @param terminal: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        @param sv_short_circuit: The short circuit state associated with the topological node.
        @param sv_injection: The injection state associated with the topological node.
        @param angle_ref_topological_island: The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        @param connectivity_nodes: Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        @param connectivity_node_container: The connectivity node container to which the toplogical node belongs.
        @param base_voltage: The base voltage of the topologocial node.
        @param topological_island: A topological node belongs to a topological island
        """

        self._sv_voltage = None
        self.sv_voltage = sv_voltage

        self._reporting_group = None
        self.reporting_group = reporting_group

        self._terminal = []
        if terminal is not None:
            self.terminal = terminal
        else:
            self.terminal = []

        self._sv_short_circuit = None
        self.sv_short_circuit = sv_short_circuit

        self._sv_injection = None
        self.sv_injection = sv_injection

        self._angle_ref_topological_island = None
        self.angle_ref_topological_island = angle_ref_topological_island

        self._connectivity_nodes = []
        if connectivity_nodes is not None:
            self.connectivity_nodes = connectivity_nodes
        else:
            self.connectivity_nodes = []

        self._connectivity_node_container = None
        self.connectivity_node_container = connectivity_node_container

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._topological_island = None
        self.topological_island = topological_island


        super(TopologicalNode, self).__init__(*args, **kw_args)
    # >>> topological_node

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

    # <<< sv_short_circuit
    # @generated
    def get_sv_short_circuit(self):
        """ The short circuit state associated with the topological node.
        """
        return self._sv_short_circuit

    def set_sv_short_circuit(self, value):
        if self._sv_short_circuit is not None:
            self._sv_short_circuit._topological_node = None

        self._sv_short_circuit = value
        if self._sv_short_circuit is not None:
            self._sv_short_circuit._topological_node = self

    sv_short_circuit = property(get_sv_short_circuit, set_sv_short_circuit)
    # >>> sv_short_circuit

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



class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """
    # <<< topological_island
    # @generated
    def __init__(self, angle_ref_topological_node=None, topological_nodes=None, *args, **kw_args):
        """ Initialises a new 'TopologicalIsland' instance.

        @param angle_ref_topological_node: The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        @param topological_nodes: A topological node belongs to a topological island
        """

        self._angle_ref_topological_node = None
        self.angle_ref_topological_node = angle_ref_topological_node

        self._topological_nodes = []
        if topological_nodes is not None:
            self.topological_nodes = topological_nodes
        else:
            self.topological_nodes = []


        super(TopologicalIsland, self).__init__(*args, **kw_args)
    # >>> topological_island

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



# <<< topology
# @generated
# >>> topology
