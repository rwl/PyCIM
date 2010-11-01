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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class ConnectivityNodeContainer(PowerSystemResource):
    """A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """

    def __init__(self, TopologicalNode=None, ConnectivityNodes=None, *args, **kw_args):
        """Initializes a new 'ConnectivityNodeContainer' instance.

        @param TopologicalNode: The topological nodes which belong to this connectivity node container.
        @param ConnectivityNodes: Connectivity nodes contained by this container.
        """
        self._TopologicalNode = []
        self.TopologicalNode = [] if TopologicalNode is None else TopologicalNode

        self._ConnectivityNodes = []
        self.ConnectivityNodes = [] if ConnectivityNodes is None else ConnectivityNodes

        super(ConnectivityNodeContainer, self).__init__(*args, **kw_args)

    def getTopologicalNode(self):
        """The topological nodes which belong to this connectivity node container.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        for x in self._TopologicalNode:
            x._ConnectivityNodeContainer = None
        for y in value:
            y._ConnectivityNodeContainer = self
        self._TopologicalNode = value

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def addTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj._ConnectivityNodeContainer = self
            self._TopologicalNode.append(obj)

    def removeTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj._ConnectivityNodeContainer = None
            self._TopologicalNode.remove(obj)

    def getConnectivityNodes(self):
        """Connectivity nodes contained by this container.
        """
        return self._ConnectivityNodes

    def setConnectivityNodes(self, value):
        for x in self._ConnectivityNodes:
            x._ConnectivityNodeContainer = None
        for y in value:
            y._ConnectivityNodeContainer = self
        self._ConnectivityNodes = value

    ConnectivityNodes = property(getConnectivityNodes, setConnectivityNodes)

    def addConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj._ConnectivityNodeContainer = self
            self._ConnectivityNodes.append(obj)

    def removeConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj._ConnectivityNodeContainer = None
            self._ConnectivityNodes.remove(obj)

