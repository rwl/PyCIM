# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" An extension to the Core Package that in association with the Terminal class models Connectivity, that is the physical definition of how equipment is connected together. In addition it models Topology, that is the logical definition of how equipment is connected via closed switches. The Topology definition is independent of the other electrical characteristics.
"""
from iec61970.core import IdentifiedObject
from iec61970.domain import Boolean
from iec61970.domain import ReactivePower
from iec61970.domain import ActivePower
from iec61970.domain import AngleRadians
from iec61970.domain import Voltage
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits, Instance, List, Bool



class ConnectivityNode(IdentifiedObject):
    """ Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """
    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    TopologicalNode = Instance("iec61970.topology.TopologicalNode.TopologicalNode")
    # Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
    Terminals = List(Instance("iec61970.core.Terminal.Terminal"))
    MemberOf_EquipmentContainer = Instance("iec61970.core.ConnectivityNodeContainer.ConnectivityNodeContainer", allow_none=False)

class TopologicalIsland(IdentifiedObject):
    """ An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """
    # A topological node belongs to a topological island
    TopologicalNodes = List(Instance("iec61970.topology.TopologicalNode.TopologicalNode"))

class TopologicalNode(IdentifiedObject):
    """ A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).
    """
    # Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
    ConnectivityNodes = List(Instance("iec61970.topology.ConnectivityNode.ConnectivityNode"))
    # A topological node belongs to a topological island
    TopologicalIsland = Instance("iec61970.topology.TopologicalIsland.TopologicalIsland", allow_none=False)
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

class TopologyVersion(HasTraits):
    version = String
    date = AbsoluteDateTime


