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

class ConnectivityNodeContainer(IdentifiedObject):
    """A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.
    """

    def __init__(self, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'ConnectivityNodeContainer' instance.

        @param TopologicalNode: The topological nodes which belong to this connectivity node container.
        """
        self._TopologicalNode = []
        self.TopologicalNode = [] if TopologicalNode is None else TopologicalNode

        super(ConnectivityNodeContainer, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TopologicalNode"]
    _many_refs = ["TopologicalNode"]

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

