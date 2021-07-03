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

from CIM15.CDPSM.Connectivity.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Terminal(IdentifiedObject):
    """An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

    def __init__(self, phases="s12N", ConnectivityNode=None, TransformerEnd=None, ConductingEquipment=None, *args, **kw_args):
        """Initialises a new 'Terminal' instance.

        @param phases: Represents the normal network phasing condition. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param ConnectivityNode: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        @param TransformerEnd: All transformer ends connected at this external terminal.
        @param ConductingEquipment: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        #: Represents the normal network phasing condition. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phases = phases

        self._ConnectivityNode = None
        self.ConnectivityNode = ConnectivityNode

        self._TransformerEnd = []
        self.TransformerEnd = [] if TransformerEnd is None else TransformerEnd

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        super(Terminal, self).__init__(*args, **kw_args)

    _attrs = ["phases"]
    _attr_types = {"phases": str}
    _defaults = {"phases": "s12N"}
    _enums = {"phases": "PhaseCode"}
    _refs = ["ConnectivityNode", "TransformerEnd", "ConductingEquipment"]
    _many_refs = ["TransformerEnd"]

    def getConnectivityNode(self):
        """Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._ConnectivityNode

    def setConnectivityNode(self, value):
        if self._ConnectivityNode is not None:
            filtered = [x for x in self.ConnectivityNode.Terminals if x != self]
            self._ConnectivityNode._Terminals = filtered

        self._ConnectivityNode = value
        if self._ConnectivityNode is not None:
            if self not in self._ConnectivityNode._Terminals:
                self._ConnectivityNode._Terminals.append(self)

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

    def getTransformerEnd(self):
        """All transformer ends connected at this external terminal.
        """
        return self._TransformerEnd

    def setTransformerEnd(self, value):
        for x in self._TransformerEnd:
            x.Terminal = None
        for y in value:
            y._Terminal = self
        self._TransformerEnd = value

    TransformerEnd = property(getTransformerEnd, setTransformerEnd)

    def addTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.Terminal = self

    def removeTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.Terminal = None

    def getConductingEquipment(self):
        """ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            filtered = [x for x in self.ConductingEquipment.Terminals if x != self]
            self._ConductingEquipment._Terminals = filtered

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            if self not in self._ConductingEquipment._Terminals:
                self._ConductingEquipment._Terminals.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

