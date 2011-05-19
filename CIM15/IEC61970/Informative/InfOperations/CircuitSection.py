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

class CircuitSection(IdentifiedObject):
    """Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.Section of circuit located between two sectionalizing devices. It may contain other circuit sections, for example, a lateral tapped off a primary.
    """

    def __init__(self, connectionKind="electricallyConnected", ConductorAssets=None, Circuits=None, *args, **kw_args):
        """Initialises a new 'CircuitSection' instance.

        @param connectionKind: Kind of this circuit section. Values are: "electricallyConnected", "nominallyConnected", "asBuilt", "other"
        @param ConductorAssets:
        @param Circuits:
        """
        #: Kind of this circuit section. Values are: "electricallyConnected", "nominallyConnected", "asBuilt", "other"
        self.connectionKind = connectionKind

        self._ConductorAssets = []
        self.ConductorAssets = [] if ConductorAssets is None else ConductorAssets

        self._Circuits = []
        self.Circuits = [] if Circuits is None else Circuits

        super(CircuitSection, self).__init__(*args, **kw_args)

    _attrs = ["connectionKind"]
    _attr_types = {"connectionKind": str}
    _defaults = {"connectionKind": "electricallyConnected"}
    _enums = {"connectionKind": "CircuitConnectionKind"}
    _refs = ["ConductorAssets", "Circuits"]
    _many_refs = ["ConductorAssets", "Circuits"]

    def getConductorAssets(self):
        
        return self._ConductorAssets

    def setConductorAssets(self, value):
        for x in self._ConductorAssets:
            x.CircuitSection = None
        for y in value:
            y._CircuitSection = self
        self._ConductorAssets = value

    ConductorAssets = property(getConductorAssets, setConductorAssets)

    def addConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj.CircuitSection = self

    def removeConductorAssets(self, *ConductorAssets):
        for obj in ConductorAssets:
            obj.CircuitSection = None

    def getCircuits(self):
        
        return self._Circuits

    def setCircuits(self, value):
        for p in self._Circuits:
            filtered = [q for q in p.CircuitSections if q != self]
            self._Circuits._CircuitSections = filtered
        for r in value:
            if self not in r._CircuitSections:
                r._CircuitSections.append(self)
        self._Circuits = value

    Circuits = property(getCircuits, setCircuits)

    def addCircuits(self, *Circuits):
        for obj in Circuits:
            if self not in obj._CircuitSections:
                obj._CircuitSections.append(self)
            self._Circuits.append(obj)

    def removeCircuits(self, *Circuits):
        for obj in Circuits:
            if self in obj._CircuitSections:
                obj._CircuitSections.remove(self)
            self._Circuits.remove(obj)

