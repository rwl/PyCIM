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

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from iec61970.core import IdentifiedObject
from iec61970.domain import Boolean
from iec61970.domain import ReactivePower
from iec61970.domain import ActivePower
from iec61970.domain import AngleRadians
from iec61970.domain import Voltage
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits, Instance, List, Bool
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ConnectivityNode" class:
#------------------------------------------------------------------------------

class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("iec61970.topology.TopologicalNode")

    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("iec61970.core.Terminal"))

    MemberOf_EquipmentContainer = Instance("iec61970.core.ConnectivityNodeContainer", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin connectivityNode user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End connectivityNode user definitions:
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

    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("iec61970.topology.TopologicalNode"))

    #--------------------------------------------------------------------------
    #  Begin topologicalIsland user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End topologicalIsland user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TopologicalNode" class:
#------------------------------------------------------------------------------

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("iec61970.topology.ConnectivityNode"))

    # A topological node belongs to a topological island
    TopologicalIsland = Instance("iec61970.topology.TopologicalIsland", allow_none=False)

    # True if node energized
    energized = Boolean

    # True if node is load carrying
    loadCarrying = Boolean

    # Net injection reactive power
    netInjectionQ = ReactivePower

    # Net injection active power
    netInjectionP = ActivePower

    # The observability status of the node.
    observabilityFlag = Boolean

    # Phase angle of node
    phaseAngle = AngleRadians

    # Voltage of node
    voltage = Voltage

    #--------------------------------------------------------------------------
    #  Begin topologicalNode user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End topologicalNode user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TopologyVersion" class:
#------------------------------------------------------------------------------

class TopologyVersion(HasTraits):
    version = String

    date = AbsoluteDateTime

    #--------------------------------------------------------------------------
    #  Begin topologyVersion user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End topologyVersion user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
