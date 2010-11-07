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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a TopologicalNode is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes changes as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model switch statuses are not used to form TopologicalNodes. Instead they are manually created or deleted in a model builder tool. TopologialNodes maintained this way are also called 'busses'.
    """

    def __init__(self, Terminal=None, TopologicalIsland=None, ReportingGroup=None, ConnectivityNodes=None, SvInjection=None, SvVoltage=None, SvShortCircuit=None, BaseVoltage=None, ConnectivityNodeContainer=None, AngleRef_TopologicalIsland=None, **kw_args):
        """Initializes a new 'TopologicalNode' instance.

        @param Terminal: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        @param TopologicalIsland: A topological node belongs to a topological island
        @param ReportingGroup: The reporting group to which the topological node belongs.
        @param ConnectivityNodes: Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        @param SvInjection: The injection state associated with the topological node.
        @param SvVoltage: The state voltage associated with the topological node.
        @param SvShortCircuit: The short circuit state associated with the topological node.
        @param BaseVoltage: The base voltage of the topologocial node.
        @param ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs.
        @param AngleRef_TopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        """
        self._Terminal = []
        self.Terminal = [] if Terminal is None else Terminal

        self._TopologicalIsland = None
        self.TopologicalIsland = TopologicalIsland

        self._ReportingGroup = None
        self.ReportingGroup = ReportingGroup

        self._ConnectivityNodes = []
        self.ConnectivityNodes = [] if ConnectivityNodes is None else ConnectivityNodes

        self._SvInjection = None
        self.SvInjection = SvInjection

        self._SvVoltage = None
        self.SvVoltage = SvVoltage

        self._SvShortCircuit = None
        self.SvShortCircuit = SvShortCircuit

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        self._ConnectivityNodeContainer = None
        self.ConnectivityNodeContainer = ConnectivityNodeContainer

        self._AngleRef_TopologicalIsland = None
        self.AngleRef_TopologicalIsland = AngleRef_TopologicalIsland

        super(TopologicalNode, self).__init__(**kw_args)

    def getTerminal(self):
        """The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._Terminal

    def setTerminal(self, value):
        for x in self._Terminal:
            x._TopologicalNode = None
        for y in value:
            y._TopologicalNode = self
        self._Terminal = value

    Terminal = property(getTerminal, setTerminal)

    def addTerminal(self, *Terminal):
        for obj in Terminal:
            obj._TopologicalNode = self
            self._Terminal.append(obj)

    def removeTerminal(self, *Terminal):
        for obj in Terminal:
            obj._TopologicalNode = None
            self._Terminal.remove(obj)

    def getTopologicalIsland(self):
        """A topological node belongs to a topological island
        """
        return self._TopologicalIsland

    def setTopologicalIsland(self, value):
        if self._TopologicalIsland is not None:
            filtered = [x for x in self.TopologicalIsland.TopologicalNodes if x != self]
            self._TopologicalIsland._TopologicalNodes = filtered

        self._TopologicalIsland = value
        if self._TopologicalIsland is not None:
            self._TopologicalIsland._TopologicalNodes.append(self)

    TopologicalIsland = property(getTopologicalIsland, setTopologicalIsland)

    def getReportingGroup(self):
        """The reporting group to which the topological node belongs.
        """
        return self._ReportingGroup

    def setReportingGroup(self, value):
        if self._ReportingGroup is not None:
            filtered = [x for x in self.ReportingGroup.TopologicalNode if x != self]
            self._ReportingGroup._TopologicalNode = filtered

        self._ReportingGroup = value
        if self._ReportingGroup is not None:
            self._ReportingGroup._TopologicalNode.append(self)

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def getConnectivityNodes(self):
        """Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        """
        return self._ConnectivityNodes

    def setConnectivityNodes(self, value):
        for x in self._ConnectivityNodes:
            x._TopologicalNode = None
        for y in value:
            y._TopologicalNode = self
        self._ConnectivityNodes = value

    ConnectivityNodes = property(getConnectivityNodes, setConnectivityNodes)

    def addConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj._TopologicalNode = self
            self._ConnectivityNodes.append(obj)

    def removeConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj._TopologicalNode = None
            self._ConnectivityNodes.remove(obj)

    def getSvInjection(self):
        """The injection state associated with the topological node.
        """
        return self._SvInjection

    def setSvInjection(self, value):
        if self._SvInjection is not None:
            self._SvInjection._TopologicalNode = None

        self._SvInjection = value
        if self._SvInjection is not None:
            self._SvInjection._TopologicalNode = self

    SvInjection = property(getSvInjection, setSvInjection)

    def getSvVoltage(self):
        """The state voltage associated with the topological node.
        """
        return self._SvVoltage

    def setSvVoltage(self, value):
        if self._SvVoltage is not None:
            self._SvVoltage._TopologicalNode = None

        self._SvVoltage = value
        if self._SvVoltage is not None:
            self._SvVoltage._TopologicalNode = self

    SvVoltage = property(getSvVoltage, setSvVoltage)

    def getSvShortCircuit(self):
        """The short circuit state associated with the topological node.
        """
        return self._SvShortCircuit

    def setSvShortCircuit(self, value):
        if self._SvShortCircuit is not None:
            self._SvShortCircuit._TopologicalNode = None

        self._SvShortCircuit = value
        if self._SvShortCircuit is not None:
            self._SvShortCircuit._TopologicalNode = self

    SvShortCircuit = property(getSvShortCircuit, setSvShortCircuit)

    def getBaseVoltage(self):
        """The base voltage of the topologocial node.
        """
        return self._BaseVoltage

    def setBaseVoltage(self, value):
        if self._BaseVoltage is not None:
            filtered = [x for x in self.BaseVoltage.TopologicalNode if x != self]
            self._BaseVoltage._TopologicalNode = filtered

        self._BaseVoltage = value
        if self._BaseVoltage is not None:
            self._BaseVoltage._TopologicalNode.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)

    def getConnectivityNodeContainer(self):
        """The connectivity node container to which the toplogical node belongs.
        """
        return self._ConnectivityNodeContainer

    def setConnectivityNodeContainer(self, value):
        if self._ConnectivityNodeContainer is not None:
            filtered = [x for x in self.ConnectivityNodeContainer.TopologicalNode if x != self]
            self._ConnectivityNodeContainer._TopologicalNode = filtered

        self._ConnectivityNodeContainer = value
        if self._ConnectivityNodeContainer is not None:
            self._ConnectivityNodeContainer._TopologicalNode.append(self)

    ConnectivityNodeContainer = property(getConnectivityNodeContainer, setConnectivityNodeContainer)

    def getAngleRef_TopologicalIsland(self):
        """The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        """
        return self._AngleRef_TopologicalIsland

    def setAngleRef_TopologicalIsland(self, value):
        if self._AngleRef_TopologicalIsland is not None:
            self._AngleRef_TopologicalIsland._AngleRef_TopologicalNode = None

        self._AngleRef_TopologicalIsland = value
        if self._AngleRef_TopologicalIsland is not None:
            self._AngleRef_TopologicalIsland._AngleRef_TopologicalNode = self

    AngleRef_TopologicalIsland = property(getAngleRef_TopologicalIsland, setAngleRef_TopologicalIsland)

