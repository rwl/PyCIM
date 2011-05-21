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

from CIM14.CPSM.Topology.Core.IdentifiedObject import IdentifiedObject

class Terminal(IdentifiedObject):
    """An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

    def __init__(self, connected=False, TopologicalNode=None, *args, **kw_args):
        """Initialises a new 'Terminal' instance.

        @param connected: The connected status is related to a bus-branch model and the TopologicalNode-Terminal relation.  True implies the Terminal is connected to the related TopologicalNode and false implies it is not.  In a bus-branch model the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the TopologicalNode-Terminal relation. A valid case is that ConductingEquipment can be connected in one end and open in the other. In particular for an ACLineSegment where the charging can be significant this is a relevant case. 
        @param TopologicalNode: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        #: The connected status is related to a bus-branch model and the TopologicalNode-Terminal relation.  True implies the Terminal is connected to the related TopologicalNode and false implies it is not.  In a bus-branch model the connected status is used to tell if equipment is disconnected without having to change the connectivity described by the TopologicalNode-Terminal relation. A valid case is that ConductingEquipment can be connected in one end and open in the other. In particular for an ACLineSegment where the charging can be significant this is a relevant case.
        self.connected = connected

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        super(Terminal, self).__init__(*args, **kw_args)

    _attrs = ["connected"]
    _attr_types = {"connected": bool}
    _defaults = {"connected": False}
    _enums = {}
    _refs = ["TopologicalNode"]
    _many_refs = []

    def getTopologicalNode(self):
        """The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            filtered = [x for x in self.TopologicalNode.Terminal if x != self]
            self._TopologicalNode._Terminal = filtered

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            if self not in self._TopologicalNode._Terminal:
                self._TopologicalNode._Terminal.append(self)

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

