#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "TopologicalNode" class:
#------------------------------------------------------------------------------

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReportingGroup = Instance("CIM13.Core.ReportingGroup",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_ReportingGroups"))

    _ReportingGroups = Property( List(Instance("CIM.Root")) )

    def _get__ReportingGroups(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, ReportingGroup)]
        else:
            return []

    AngleRef_TopologicalIsland = Instance("CIM13.Topology.TopologicalIsland",
        transient=True,
        opposite="AngleRef_TopologicalNode",
        editor=InstanceEditor(name="_TopologicalIslands"))

    _TopologicalIslands = Property( List(Instance("CIM.Root")) )

    def _get__TopologicalIslands(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, AngleRef_TopologicalIsland)]
        else:
            return []

    ConnectivityNodeContainer = Instance("CIM13.Core.ConnectivityNodeContainer",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_ConnectivityNodeContainers"))

    _ConnectivityNodeContainers = Property( List(Instance("CIM.Root")) )

    def _get__ConnectivityNodeContainers(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, ConnectivityNodeContainer)]
        else:
            return []

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("CIM13.Topology.TopologicalIsland",
        desc="A topological node belongs to a topological island",
        transient=True,
        opposite="TopologicalNodes",
        editor=InstanceEditor(name="_TopologicalIslands"))

    _TopologicalIslands = Property( List(Instance("CIM.Root")) )

    def _get__TopologicalIslands(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, TopologicalIsland)]
        else:
            return []

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("CIM13.Topology.ConnectivityNode"),
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.")

    Terminal = List(Instance("CIM13.Core.Terminal"))

    ControlArea = Instance("CIM13.ControlArea.ControlArea",
        transient=True,
        opposite="TopologicalNode",
        editor=InstanceEditor(name="_ControlAreas"))

    _ControlAreas = Property( List(Instance("CIM.Root")) )

    def _get__ControlAreas(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, ControlArea)]
        else:
            return []

    # True if node energized
    energized = Bool(desc="True if node energized")

    # Net injection active power
    netInjectionP = Float(desc="Net injection active power")

    # Net injection reactive power
    netInjectionQ = Float(desc="Net injection reactive power")

    # Phase angle of node
    phaseAngle = Float(desc="Phase angle of node")

    # The observability status of the node.
    observabilityFlag = Bool(desc="The observability status of the node.")

    # Voltage of node
    voltage = Float(desc="Voltage of node")

    # True if node is load carrying
    loadCarrying = Bool(desc="True if node is load carrying")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "energized", "netInjectionP", "netInjectionQ", "phaseAngle", "observabilityFlag", "voltage", "loadCarrying",
                label="Attributes", columns=1),
            VGroup("ContainedBy", "ModelingAuthoritySet", "ReportingGroup", "AngleRef_TopologicalIsland", "ConnectivityNodeContainer", "TopologicalIsland", "ConnectivityNodes", "Terminal", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13.Topology.TopologicalNode",
        title="TopologicalNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalNode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TopologicalIsland" class:
#------------------------------------------------------------------------------

class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    AngleRef_TopologicalNode = Instance("CIM13.Topology.TopologicalNode",
        transient=True,
        opposite="AngleRef_TopologicalIsland",
        editor=InstanceEditor(name="_TopologicalNodes"))

    _TopologicalNodes = Property( List(Instance("CIM.Root")) )

    def _get__TopologicalNodes(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, AngleRef_TopologicalNode)]
        else:
            return []

    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("CIM13.Topology.TopologicalNode"),
        desc="A topological node belongs to a topological island")

    #--------------------------------------------------------------------------
    #  Begin "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "AngleRef_TopologicalNode", "TopologicalNodes",
                label="References"),
            dock="tab"),
        id="CIM13.Topology.TopologicalIsland",
        title="TopologicalIsland",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TopologicalIsland" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConnectivityNode" class:
#------------------------------------------------------------------------------

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    MemberOf_EquipmentContainer = Instance("CIM13.Core.ConnectivityNodeContainer",
        transient=True,
        opposite="ConnectivityNodes",
        editor=InstanceEditor(name="_ConnectivityNodeContainers"))

    _ConnectivityNodeContainers = Property( List(Instance("CIM.Root")) )

    def _get__ConnectivityNodeContainers(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, MemberOf_EquipmentContainer)]
        else:
            return []

    BusNameMarker = Instance("CIM13.Topology.BusNameMarker",
        transient=True,
        opposite="ConnectivityNode",
        editor=InstanceEditor(name="_BusNameMarkers"))

    _BusNameMarkers = Property( List(Instance("CIM.Root")) )

    def _get__BusNameMarkers(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, BusNameMarker)]
        else:
            return []

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CIM13.Core.Terminal"),
        desc="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("CIM13.Topology.TopologicalNode",
        desc="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.",
        transient=True,
        opposite="ConnectivityNodes",
        editor=InstanceEditor(name="_TopologicalNodes"))

    _TopologicalNodes = Property( List(Instance("CIM.Root")) )

    def _get__TopologicalNodes(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, TopologicalNode)]
        else:
            return []

    #--------------------------------------------------------------------------
    #  Begin "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "MemberOf_EquipmentContainer", "BusNameMarker", "Terminals", "TopologicalNode",
                label="References"),
            dock="tab"),
        id="CIM13.Topology.ConnectivityNode",
        title="ConnectivityNode",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConnectivityNode" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusNameMarker" class:
#------------------------------------------------------------------------------

class BusNameMarker(IdentifiedObject):
    """ Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ControlArea = Instance("CIM13.ControlArea.ControlArea",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_ControlAreas"))

    _ControlAreas = Property( List(Instance("CIM.Root")) )

    def _get__ControlAreas(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, ControlArea)]
        else:
            return []

    ConnectivityNode = List(Instance("CIM13.Topology.ConnectivityNode"))

    ReportingGroup = Instance("CIM13.Core.ReportingGroup",
        transient=True,
        opposite="BusNameMarker",
        editor=InstanceEditor(name="_ReportingGroups"))

    _ReportingGroups = Property( List(Instance("CIM.Root")) )

    def _get__ReportingGroups(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, ReportingGroup)]
        else:
            return []

    #--------------------------------------------------------------------------
    #  Begin "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "ControlArea", "ConnectivityNode", "ReportingGroup",
                label="References"),
            dock="tab"),
        id="CIM13.Topology.BusNameMarker",
        title="BusNameMarker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusNameMarker" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
