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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class ConnectivityNode(IdentifiedObject):
    """Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.
    """

    def __init__(self, Terminals=None, *args, **kw_args):
        """Initialises a new 'ConnectivityNode' instance.

        @param Terminals: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        self._Terminals = []
        self.Terminals = [] if Terminals is None else Terminals

        super(ConnectivityNode, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Terminals"]
    _many_refs = ["Terminals"]

    def getTerminals(self):
        """Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._Terminals

    def setTerminals(self, value):
        for x in self._Terminals:
            x.ConnectivityNode = None
        for y in value:
            y._ConnectivityNode = self
        self._Terminals = value

    Terminals = property(getTerminals, setTerminals)

    def addTerminals(self, *Terminals):
        for obj in Terminals:
            obj.ConnectivityNode = self

    def removeTerminals(self, *Terminals):
        for obj in Terminals:
            obj.ConnectivityNode = None

