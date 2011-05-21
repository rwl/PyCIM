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

from CIM14.CDPSM.Unbalanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WindingPiImpedance(IdentifiedObject):
    """Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.
    """

    def __init__(self, x=0.0, g=0.0, r0=0.0, r=0.0, b=0.0, g0=0.0, x0=0.0, b0=0.0, Windings=None, *args, **kw_args):
        """Initialises a new 'WindingPiImpedance' instance.

        @param x: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        @param g: Magnetizing branch conductance (G mag). 
        @param r0: Zero sequence series resistance of the winding. 
        @param r: DC resistance of the winding. 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param g0: Zero sequence magnetizing branch conductance. 
        @param x0: Zero sequence series reactance of the winding. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param Windings: All windings having this Pi impedance.
        """
        #: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
        self.x = x

        #: Magnetizing branch conductance (G mag).
        self.g = g

        #: Zero sequence series resistance of the winding.
        self.r0 = r0

        #: DC resistance of the winding.
        self.r = r

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
        self.b = b

        #: Zero sequence magnetizing branch conductance.
        self.g0 = g0

        #: Zero sequence series reactance of the winding.
        self.x0 = x0

        #: Zero sequence magnetizing branch susceptance.
        self.b0 = b0

        self._Windings = []
        self.Windings = [] if Windings is None else Windings

        super(WindingPiImpedance, self).__init__(*args, **kw_args)

    _attrs = ["x", "g", "r0", "r", "b", "g0", "x0", "b0"]
    _attr_types = {"x": float, "g": float, "r0": float, "r": float, "b": float, "g0": float, "x0": float, "b0": float}
    _defaults = {"x": 0.0, "g": 0.0, "r0": 0.0, "r": 0.0, "b": 0.0, "g0": 0.0, "x0": 0.0, "b0": 0.0}
    _enums = {}
    _refs = ["Windings"]
    _many_refs = ["Windings"]

    def getWindings(self):
        """All windings having this Pi impedance.
        """
        return self._Windings

    def setWindings(self, value):
        for x in self._Windings:
            x.PiImpedance = None
        for y in value:
            y._PiImpedance = self
        self._Windings = value

    Windings = property(getWindings, setWindings)

    def addWindings(self, *Windings):
        for obj in Windings:
            obj.PiImpedance = self

    def removeWindings(self, *Windings):
        for obj in Windings:
            obj.PiImpedance = None

