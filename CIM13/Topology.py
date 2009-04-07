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



from enthought.traits.api import Instance, List, Bool, Float
# <<< imports

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

    ReportingGroup = Instance("CIM13.Core.ReportingGroup")

    AngleRef_TopologicalIsland = Instance("CIM13.Topology.TopologicalIsland")

    ConnectivityNodeContainer = Instance("CIM13.Core.ConnectivityNodeContainer")

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("CIM13.Topology.TopologicalIsland")

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("CIM13.Topology.ConnectivityNode"))

    Terminal = List(Instance("CIM13.Core.Terminal"))

    ControlArea = Instance("CIM13.ControlArea.ControlArea")

    # True if node energized
    energized = Bool

    # Net injection active power
    netInjectionP = Float

    # Net injection reactive power
    netInjectionQ = Float

    # Phase angle of node
    phaseAngle = Float

    # The observability status of the node.
    observabilityFlag = Bool

    # Voltage of node
    voltage = Float

    # True if node is load carrying
    loadCarrying = Bool

    #--------------------------------------------------------------------------
    #  Begin topologicalNode user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End topologicalNode user definitions:
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

    AngleRef_TopologicalNode = Instance("CIM13.Topology.TopologicalNode")

    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("CIM13.Topology.TopologicalNode"))

    #--------------------------------------------------------------------------
    #  Begin topologicalIsland user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End topologicalIsland user definitions:
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

    MemberOf_EquipmentContainer = Instance("CIM13.Core.ConnectivityNodeContainer")

    BusNameMarker = Instance("CIM13.Topology.BusNameMarker")

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("CIM13.Core.Terminal"))

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("CIM13.Topology.TopologicalNode")

    #--------------------------------------------------------------------------
    #  Begin connectivityNode user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End connectivityNode user definitions:
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

    ControlArea = Instance("CIM13.ControlArea.ControlArea")

    ConnectivityNode = List(Instance("CIM13.Topology.ConnectivityNode"))

    ReportingGroup = Instance("CIM13.Core.ReportingGroup")

    #--------------------------------------------------------------------------
    #  Begin busNameMarker user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End busNameMarker user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
