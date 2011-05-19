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

class TopologicalIsland(IdentifiedObject):
    """An electrically connected subset of the network. Topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of TopologicalNodes in a planning tool.An electrically connected subset of the network. Topological islands can change as the current network state changes: e.g. due to  - disconnect switches or breakers change state in a SCADA/EMS - manual creation, change or deletion of TopologicalNodes in a planning tool.
    """

    def __init__(self, AngleRef_TopologicalNode=None, TopologicalNodes=None, *args, **kw_args):
        """Initialises a new 'TopologicalIsland' instance.

        @param AngleRef_TopologicalNode: The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        @param TopologicalNodes: A topological node belongs to a topological island
        """
        self._AngleRef_TopologicalNode = None
        self.AngleRef_TopologicalNode = AngleRef_TopologicalNode

        self._TopologicalNodes = []
        self.TopologicalNodes = [] if TopologicalNodes is None else TopologicalNodes

        super(TopologicalIsland, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["AngleRef_TopologicalNode", "TopologicalNodes"]
    _many_refs = ["TopologicalNodes"]

    def getAngleRef_TopologicalNode(self):
        """The angle reference for the island.   Normally there is one TopologicalNode that is selected as the angle reference for each island.   Other reference schemes exist, so the association is optional.
        """
        return self._AngleRef_TopologicalNode

    def setAngleRef_TopologicalNode(self, value):
        if self._AngleRef_TopologicalNode is not None:
            self._AngleRef_TopologicalNode._AngleRef_TopologicalIsland = None

        self._AngleRef_TopologicalNode = value
        if self._AngleRef_TopologicalNode is not None:
            self._AngleRef_TopologicalNode.AngleRef_TopologicalIsland = None
            self._AngleRef_TopologicalNode._AngleRef_TopologicalIsland = self

    AngleRef_TopologicalNode = property(getAngleRef_TopologicalNode, setAngleRef_TopologicalNode)

    def getTopologicalNodes(self):
        """A topological node belongs to a topological island
        """
        return self._TopologicalNodes

    def setTopologicalNodes(self, value):
        for x in self._TopologicalNodes:
            x.TopologicalIsland = None
        for y in value:
            y._TopologicalIsland = self
        self._TopologicalNodes = value

    TopologicalNodes = property(getTopologicalNodes, setTopologicalNodes)

    def addTopologicalNodes(self, *TopologicalNodes):
        for obj in TopologicalNodes:
            obj.TopologicalIsland = self

    def removeTopologicalNodes(self, *TopologicalNodes):
        for obj in TopologicalNodes:
            obj.TopologicalIsland = None

