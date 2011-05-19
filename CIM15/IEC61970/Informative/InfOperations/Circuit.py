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

from CIM15.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Circuit(EquipmentContainer):
    """EquipmentContainer that will typically include conductors, energy consumers, transformers and transformer windings, switches, shunt compensators, etc., likely at different voltages. Circuit extends from a substation to a set of open points (radial circuit), or to a second substation (looped circuit). It generally starts with a switching device, located in a substation. Membership in a Circuit is based on the nominal or design system configuration, but the electrical connectivity will change during switching operations.EquipmentContainer that will typically include conductors, energy consumers, transformers and transformer windings, switches, shunt compensators, etc., likely at different voltages. Circuit extends from a substation to a set of open points (radial circuit), or to a second substation (looped circuit). It generally starts with a switching device, located in a substation. Membership in a Circuit is based on the nominal or design system configuration, but the electrical connectivity will change during switching operations.
    """

    def __init__(self, CircuitSections=None, *args, **kw_args):
        """Initialises a new 'Circuit' instance.

        @param CircuitSections:
        """
        self._CircuitSections = []
        self.CircuitSections = [] if CircuitSections is None else CircuitSections

        super(Circuit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["CircuitSections"]
    _many_refs = ["CircuitSections"]

    def getCircuitSections(self):
        
        return self._CircuitSections

    def setCircuitSections(self, value):
        for p in self._CircuitSections:
            filtered = [q for q in p.Circuits if q != self]
            self._CircuitSections._Circuits = filtered
        for r in value:
            if self not in r._Circuits:
                r._Circuits.append(self)
        self._CircuitSections = value

    CircuitSections = property(getCircuitSections, setCircuitSections)

    def addCircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            if self not in obj._Circuits:
                obj._Circuits.append(self)
            self._CircuitSections.append(obj)

    def removeCircuitSections(self, *CircuitSections):
        for obj in CircuitSections:
            if self in obj._Circuits:
                obj._Circuits.remove(self)
            self._CircuitSections.remove(obj)

