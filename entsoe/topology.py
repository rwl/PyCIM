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

from entsoe.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Topology"

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """
    # <<< topological_node
    # @generated
    def __init__(self, s_short_circuit=0.0, equivalent=False, x0_per_x=0.0, r0_per_r=0.0, x_per_r=0.0, control_area=None, base_voltage=None, sv_voltage=None, topological_island=None, angle_ref_topological_island=None, connectivity_node_container=None, terminal=None, *args, **kw_args):
        """ Initialises a new 'TopologicalNode' instance.

        @param s_short_circuit: The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only. 
        @param equivalent: The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required. 
        @param x0_per_x: The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only. 
        @param r0_per_r: The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only. 
        @param x_per_r: Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only. 
        @param control_area: The control area into which the node is included.
        @param base_voltage: The base voltage of the topologocial node.The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
        @param sv_voltage: The state voltage associated with the topological node.
        @param topological_island: A topological node belongs to a topological island
        @param angle_ref_topological_island: The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        @param connectivity_node_container: The connectivity node container to which the toplogical node belongs.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.
        @param terminal: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        # The short circuit apparent power drawn at this node when faulted.This is for Short Circuit only. 
        self.s_short_circuit = s_short_circuit

        # The topological node is equivalent and not real equipment.If this is missing, it is assumed to be False.  If it is an X-Node, this equivalent is required. 
        self.equivalent = equivalent

        # The ratio of zero sequence reactance per positive sequence reactance.This is for Short Circuit only. 
        self.x0_per_x = x0_per_x

        # The ratio of zero sequence resistance to positive sequence resistance.This is for Short Circuit only. 
        self.r0_per_r = r0_per_r

        # Ratio of positive sequence reactance per postive sequence resistance.This is for Short Circuit only. 
        self.x_per_r = x_per_r


        self._control_area = None
        self.control_area = control_area

        self._base_voltage = None
        self.base_voltage = base_voltage

        self._sv_voltage = None
        self.sv_voltage = sv_voltage

        self._topological_island = None
        self.topological_island = topological_island

        self._angle_ref_topological_island = None
        self.angle_ref_topological_island = angle_ref_topological_island

        self._connectivity_node_container = None
        self.connectivity_node_container = connectivity_node_container

        self._terminal = []
        if terminal is not None:
            self.terminal = terminal
        else:
            self.terminal = []


        super(TopologicalNode, self).__init__(*args, **kw_args)
    # >>> topological_node

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

    # <<< base_voltage
    # @generated
    def get_base_voltage(self):
        """ The base voltage of the topologocial node.The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.
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

    # <<< connectivity_node_container
    # @generated
    def get_connectivity_node_container(self):
        """ The connectivity node container to which the toplogical node belongs.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile.
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



class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """
    # <<< topological_island
    # @generated
    def __init__(self, topological_nodes=None, angle_ref_topological_node=None, *args, **kw_args):
        """ Initialises a new 'TopologicalIsland' instance.

        @param topological_nodes: A topological node belongs to a topological island
        @param angle_ref_topological_node: The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        """

        self._topological_nodes = []
        if topological_nodes is not None:
            self.topological_nodes = topological_nodes
        else:
            self.topological_nodes = []

        self._angle_ref_topological_node = None
        self.angle_ref_topological_node = angle_ref_topological_node


        super(TopologicalIsland, self).__init__(*args, **kw_args)
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



# <<< topology
# @generated
# >>> topology
