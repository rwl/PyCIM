# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ConnectivityNode(IdentifiedObject):
    """Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    def __init__(self, Pnode=None, BusNameMarker=None, LossPenaltyFactors=None, TopologicalNode=None, NodeConstraintTerms=None, Terminals=None, ConnectivityNodeContainer=None, **kw_args):
        """Initializes a new 'ConnectivityNode' instance.

        @param Pnode:
        @param BusNameMarker: The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.
        @param LossPenaltyFactors:
        @param TopologicalNode: Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        @param NodeConstraintTerms:
        @param Terminals: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        @param ConnectivityNodeContainer: Container of this connectivity node.
        """
        self._Pnode = None
        self.Pnode = Pnode

        self._BusNameMarker = None
        self.BusNameMarker = BusNameMarker

        self._LossPenaltyFactors = []
        self.LossPenaltyFactors = [] if LossPenaltyFactors is None else LossPenaltyFactors

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        self._NodeConstraintTerms = []
        self.NodeConstraintTerms = [] if NodeConstraintTerms is None else NodeConstraintTerms

        self._Terminals = []
        self.Terminals = [] if Terminals is None else Terminals

        self._ConnectivityNodeContainer = None
        self.ConnectivityNodeContainer = ConnectivityNodeContainer

        super(ConnectivityNode, self).__init__(**kw_args)

    def getPnode(self):
        
        return self._Pnode

    def setPnode(self, value):
        if self._Pnode is not None:
            self._Pnode._ConnectivityNode = None

        self._Pnode = value
        if self._Pnode is not None:
            self._Pnode._ConnectivityNode = self

    Pnode = property(getPnode, setPnode)

    def getBusNameMarker(self):
        """The associated name of the bus (TopologicalNode) containing the ConnectivityNode is derived by an algorithm that uses the bus name marker.
        """
        return self._BusNameMarker

    def setBusNameMarker(self, value):
        if self._BusNameMarker is not None:
            filtered = [x for x in self.BusNameMarker.ConnectivityNode if x != self]
            self._BusNameMarker._ConnectivityNode = filtered

        self._BusNameMarker = value
        if self._BusNameMarker is not None:
            self._BusNameMarker._ConnectivityNode.append(self)

    BusNameMarker = property(getBusNameMarker, setBusNameMarker)

    def getLossPenaltyFactors(self):
        
        return self._LossPenaltyFactors

    def setLossPenaltyFactors(self, value):
        for p in self._LossPenaltyFactors:
            filtered = [q for q in p.ConnectivityNodes if q != self]
            self._LossPenaltyFactors._ConnectivityNodes = filtered
        for r in value:
            if self not in r._ConnectivityNodes:
                r._ConnectivityNodes.append(self)
        self._LossPenaltyFactors = value

    LossPenaltyFactors = property(getLossPenaltyFactors, setLossPenaltyFactors)

    def addLossPenaltyFactors(self, *LossPenaltyFactors):
        for obj in LossPenaltyFactors:
            if self not in obj._ConnectivityNodes:
                obj._ConnectivityNodes.append(self)
            self._LossPenaltyFactors.append(obj)

    def removeLossPenaltyFactors(self, *LossPenaltyFactors):
        for obj in LossPenaltyFactors:
            if self in obj._ConnectivityNodes:
                obj._ConnectivityNodes.remove(self)
            self._LossPenaltyFactors.remove(obj)

    def getTopologicalNode(self):
        """Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            filtered = [x for x in self.TopologicalNode.ConnectivityNodes if x != self]
            self._TopologicalNode._ConnectivityNodes = filtered

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode._ConnectivityNodes.append(self)

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def getNodeConstraintTerms(self):
        
        return self._NodeConstraintTerms

    def setNodeConstraintTerms(self, value):
        for x in self._NodeConstraintTerms:
            x._ConnectivityNode = None
        for y in value:
            y._ConnectivityNode = self
        self._NodeConstraintTerms = value

    NodeConstraintTerms = property(getNodeConstraintTerms, setNodeConstraintTerms)

    def addNodeConstraintTerms(self, *NodeConstraintTerms):
        for obj in NodeConstraintTerms:
            obj._ConnectivityNode = self
            self._NodeConstraintTerms.append(obj)

    def removeNodeConstraintTerms(self, *NodeConstraintTerms):
        for obj in NodeConstraintTerms:
            obj._ConnectivityNode = None
            self._NodeConstraintTerms.remove(obj)

    def getTerminals(self):
        """Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._Terminals

    def setTerminals(self, value):
        for x in self._Terminals:
            x._ConnectivityNode = None
        for y in value:
            y._ConnectivityNode = self
        self._Terminals = value

    Terminals = property(getTerminals, setTerminals)

    def addTerminals(self, *Terminals):
        for obj in Terminals:
            obj._ConnectivityNode = self
            self._Terminals.append(obj)

    def removeTerminals(self, *Terminals):
        for obj in Terminals:
            obj._ConnectivityNode = None
            self._Terminals.remove(obj)

    def getConnectivityNodeContainer(self):
        """Container of this connectivity node.
        """
        return self._ConnectivityNodeContainer

    def setConnectivityNodeContainer(self, value):
        if self._ConnectivityNodeContainer is not None:
            filtered = [x for x in self.ConnectivityNodeContainer.ConnectivityNodes if x != self]
            self._ConnectivityNodeContainer._ConnectivityNodes = filtered

        self._ConnectivityNodeContainer = value
        if self._ConnectivityNodeContainer is not None:
            self._ConnectivityNodeContainer._ConnectivityNodes.append(self)

    ConnectivityNodeContainer = property(getConnectivityNodeContainer, setConnectivityNodeContainer)

