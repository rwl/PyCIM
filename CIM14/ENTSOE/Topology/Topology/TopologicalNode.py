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

from CIM14.ENTSOE.Topology.Core.IdentifiedObject import IdentifiedObject

class TopologicalNode(IdentifiedObject):
    """For a detailed substation model a TopologicalNode is a set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes changes as the current network state changes (i.e., switches, breakers, etc. change state). For a planning model switch statuses are not used to form TopologicalNodes. Instead they are manually created or deleted in a model builder tool. TopologialNodes maintained this way are also called 'busses'.
    """

    def __init__(self, ConnectivityNodeContainer=None, BaseVoltage=None, Terminal=None, *args, **kw_args):
        """Initialises a new 'TopologicalNode' instance.

        @param ConnectivityNodeContainer: The connectivity node container to which the toplogical node belongs.
        @param BaseVoltage: The base voltage of the topologocial node.
        @param Terminal: The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        self._ConnectivityNodeContainer = None
        self.ConnectivityNodeContainer = ConnectivityNodeContainer

        self._BaseVoltage = None
        self.BaseVoltage = BaseVoltage

        self._Terminal = []
        self.Terminal = [] if Terminal is None else Terminal

        super(TopologicalNode, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ConnectivityNodeContainer", "BaseVoltage", "Terminal"]
    _many_refs = ["Terminal"]

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

