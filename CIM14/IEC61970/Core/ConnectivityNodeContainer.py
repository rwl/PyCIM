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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class ConnectivityNodeContainer(PowerSystemResource):
    """A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """

    def __init__(self, ConnectivityNodes=None, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'ConnectivityNodeContainer' instance.

        @param ConnectivityNodes: Connectivity nodes contained by this container.
        @param TopologicalNode: The topological nodes which belong to this connectivity node container.
        """
        self._ConnectivityNodes = []
        self.ConnectivityNodes = [] if ConnectivityNodes is None else ConnectivityNodes

        self._TopologicalNode = []
        self.TopologicalNode = [] if TopologicalNode is None else TopologicalNode

        super(ConnectivityNodeContainer, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ConnectivityNodes", "TopologicalNode"]
    _many_refs = ["ConnectivityNodes", "TopologicalNode"]

    def getConnectivityNodes(self):
        """Connectivity nodes contained by this container.
        """
        return self._ConnectivityNodes

    def setConnectivityNodes(self, value):
        for x in self._ConnectivityNodes:
            x.ConnectivityNodeContainer = None
        for y in value:
            y._ConnectivityNodeContainer = self
        self._ConnectivityNodes = value

    ConnectivityNodes = property(getConnectivityNodes, setConnectivityNodes)

    def addConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj.ConnectivityNodeContainer = self

    def removeConnectivityNodes(self, *ConnectivityNodes):
        for obj in ConnectivityNodes:
            obj.ConnectivityNodeContainer = None

    def getTopologicalNode(self):
        """The topological nodes which belong to this connectivity node container.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        for x in self._TopologicalNode:
            x.ConnectivityNodeContainer = None
        for y in value:
            y._ConnectivityNodeContainer = self
        self._TopologicalNode = value

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def addTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj.ConnectivityNodeContainer = self

    def removeTopologicalNode(self, *TopologicalNode):
        for obj in TopologicalNode:
            obj.ConnectivityNodeContainer = None

