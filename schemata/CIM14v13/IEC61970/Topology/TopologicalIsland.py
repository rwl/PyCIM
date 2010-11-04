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

class TopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).
    """

    def __init__(self, AngleRef_TopologicalNode=None, TopologicalNodes=None, **kw_args):
        """Initializes a new 'TopologicalIsland' instance.

        @param AngleRef_TopologicalNode: The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        @param TopologicalNodes: A topological node belongs to a topological island
        """
        self._AngleRef_TopologicalNode = None
        self.AngleRef_TopologicalNode = AngleRef_TopologicalNode

        self._TopologicalNodes = []
        self.TopologicalNodes = [] if TopologicalNodes is None else TopologicalNodes

        super(TopologicalIsland, self).__init__(**kw_args)

    def getAngleRef_TopologicalNode(self):
        """The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        """
        return self._AngleRef_TopologicalNode

    def setAngleRef_TopologicalNode(self, value):
        if self._AngleRef_TopologicalNode is not None:
            self._AngleRef_TopologicalNode._AngleRef_TopologicalIsland = None

        self._AngleRef_TopologicalNode = value
        if self._AngleRef_TopologicalNode is not None:
            self._AngleRef_TopologicalNode._AngleRef_TopologicalIsland = self

    AngleRef_TopologicalNode = property(getAngleRef_TopologicalNode, setAngleRef_TopologicalNode)

    def getTopologicalNodes(self):
        """A topological node belongs to a topological island
        """
        return self._TopologicalNodes

    def setTopologicalNodes(self, value):
        for x in self._TopologicalNodes:
            x._TopologicalIsland = None
        for y in value:
            y._TopologicalIsland = self
        self._TopologicalNodes = value

    TopologicalNodes = property(getTopologicalNodes, setTopologicalNodes)

    def addTopologicalNodes(self, *TopologicalNodes):
        for obj in TopologicalNodes:
            obj._TopologicalIsland = self
            self._TopologicalNodes.append(obj)

    def removeTopologicalNodes(self, *TopologicalNodes):
        for obj in TopologicalNodes:
            obj._TopologicalIsland = None
            self._TopologicalNodes.remove(obj)

