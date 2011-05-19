# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a TopologicalNode is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes changes as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model switch statuses are not used to form TopologicalNodes. Instead they are manually created or deleted in a model builder tool. TopologialNodes maintained this way are also called 'busses'.For a detailed substation model a TopologicalNode is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes changes as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model switch statuses are not used to form TopologicalNodes. Instead they are manually created or deleted in a model builder tool. TopologialNodes maintained this way are also called 'busses'.
    """

    def __init__(self, SvShortCircuit=None, ConnectivityNodeContainer=None, SvInjection=None, ConnectivityNodes=None, SvVoltage=None, BaseVoltage=None, TopologicalIsland=None, ReportingGroup=None, Terminal=None, AngleRef_TopologicalIsland=None, *args, **kw_args):
        """Initialises a new 'TopologicalNode' instance.

        @param SvShortCircuit: The short circuit state associated with the topological node.
        @param ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs.
        @param SvInjection: The injection state associated with the topological node.
        @param ConnectivityNodes: Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        @param SvVoltage: The state voltage associated with the topological node.
        @param BaseVoltage: The base voltage of the topologocial node.
        @param TopologicalIsland: A topological node belongs to a topological island
        @param ReportingGroup: The reporting group to which the topological node belongs.
        @param Terminal: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        @param AngleRef_TopologicalIsland: The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        """
        self._SvShortCircuit = None
        self.SvShortCircuit = SvShortCircuit

        self._ConnectivityNodeContainer = None
        self.ConnectivityNodeContainer = ConnectivityNodeContainer

        self._SvInjection = None
        self.SvInjection = SvInjection

        self._ConnectivityNodes = []
        self.ConnectivityNodes = [] if ConnectivityNodes is None else ConnectivityNodes

        self._SvVoltage = None
        self.SvVoltage = SvVoltage

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        self._TopologicalIsland = None
        self.TopologicalIsland = TopologicalIsland

        self._ReportingGroup = None
        self.ReportingGroup = ReportingGroup

        self._Terminal = []
        self.Terminal = [] if Terminal is None else Terminal

        self._AngleRef_TopologicalIsland = None
        self.AngleRef_TopologicalIsland = AngleRef_TopologicalIsland

        super(TopologicalNode, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["SvShortCircuit", "ConnectivityNodeContainer", "SvInjection", "ConnectivityNodes", "SvVoltage", "BaseVoltage", "TopologicalIsland", "ReportingGroup", "Terminal", "AngleRef_TopologicalIsland"]
    _many_refs = ["ConnectivityNodes", "Terminal"]

    def getSvShortCircuit(self):
        """The short circuit state associated with the topological node.
        """
        return self._SvShortCircuit

    def setSvShortCircuit(self, value):
        if self._SvShortCircuit is not None:
            self._SvShortCircuit._TopologicalNode = None

        self._SvShortCircuit = value
        if self._SvShortCircuit is not None:
            self._SvShortCircuit.TopologicalNode = None
            self._SvShortCircuit._TopologicalNode = self

    SvShortCircuit = property(getSvShortCircuit, setSvShortCircuit)

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
            if self not in self._ConnectivityNodeContainer._TopologicalNode:
                self._ConnectivityNodeContainer._TopologicalNode.append(self)

    ConnectivityNodeContainer = property(getConnectivityNodeContainer, setConnectivityNodeContainer)

    def getSvInjection(self):
        """The injection state associated with the topological node.
        """
        return self._SvInjection

    def setSvInjection(self, value):
        if self._SvInjection is not None:
            self._SvInjection._TopologicalNode = None

        self._SvInjection = value
        if self._SvInjection is not None:
            self._SvInjection.TopologicalNode = None
            self._SvInjection._TopologicalNode = self

    SvInjection = property(getSvInjection, setSvInjection)

    def getConnectivityNodes(self):
        """Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.
        """
        return self._ConnectivityNodes

    def setConnectivityNodes(self, value):
        for x in self._ConnectivityNodes:
            x.TopologicalNode = None
        for y in value:
            y._TopologicalNode = self
        self._ConnectivityNodes = value

    ConnectivityNodes = property(getConnectivityNodes, setConnectivityNodes)

    def addConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj.TopologicalNode = self

    def removeConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj.TopologicalNode = None

    def getSvVoltage(self):
        """The state voltage associated with the topological node.
        """
        return self._SvVoltage

    def setSvVoltage(self, value):
        if self._SvVoltage is not None:
            self._SvVoltage._TopologicalNode = None

        self._SvVoltage = value
        if self._SvVoltage is not None:
            self._SvVoltage.TopologicalNode = None
            self._SvVoltage._TopologicalNode = self

    SvVoltage = property(getSvVoltage, setSvVoltage)

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
            if self not in self._BaseVoltage._TopologicalNode:
                self._BaseVoltage._TopologicalNode.append(self)

    BaseVoltage = property(getBaseVoltage, setBaseVoltage)

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
            if self not in self._TopologicalIsland._TopologicalNodes:
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
            if self not in self._ReportingGroup._TopologicalNode:
                self._ReportingGroup._TopologicalNode.append(self)

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def getTerminal(self):
        """The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._Terminal

    def setTerminal(self, value):
        for x in self._Terminal:
            x.TopologicalNode = None
        for y in value:
            y._TopologicalNode = self
        self._Terminal = value

    Terminal = property(getTerminal, setTerminal)

    def addTerminal(self, *Terminal):
        for obj in Terminal:
            obj.TopologicalNode = self

    def removeTerminal(self, *Terminal):
        for obj in Terminal:
            obj.TopologicalNode = None

    def getAngleRef_TopologicalIsland(self):
        """The island for which the node is an angle reference.   Normally there is one angle reference node for each island.
        """
        return self._AngleRef_TopologicalIsland

    def setAngleRef_TopologicalIsland(self, value):
        if self._AngleRef_TopologicalIsland is not None:
            self._AngleRef_TopologicalIsland._AngleRef_TopologicalNode = None

        self._AngleRef_TopologicalIsland = value
        if self._AngleRef_TopologicalIsland is not None:
            self._AngleRef_TopologicalIsland.AngleRef_TopologicalNode = None
            self._AngleRef_TopologicalIsland._AngleRef_TopologicalNode = self

    AngleRef_TopologicalIsland = property(getAngleRef_TopologicalIsland, setAngleRef_TopologicalIsland)

