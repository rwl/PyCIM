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

from CIM15.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerStarImpedance(IdentifiedObject):
    """Transformer star impedance (Pi-model) that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerTank model and related classes. For transmission networks use PowerTransformerEnd impedances (r, r0, x, x0, b, b0, g and g0).
    """

    def __init__(self, x0=0.0, x=0.0, r0=0.0, r=0.0, TransformerEnd=None, *args, **kw_args):
        """Initialises a new 'TransformerStarImpedance' instance.

        @param x0: Zero sequence series reactance of the transformer end. 
        @param x: Positive sequence series reactance of the transformer end. 
        @param r0: Zero sequence series resistance of the transformer end. 
        @param r: Resistance of the transformer end. 
        @param TransformerEnd: All transformer ends having this star impedance.
        """
        #: Zero sequence series reactance of the transformer end.
        self.x0 = x0

        #: Positive sequence series reactance of the transformer end.
        self.x = x

        #: Zero sequence series resistance of the transformer end.
        self.r0 = r0

        #: Resistance of the transformer end.
        self.r = r

        self._TransformerEnd = []
        self.TransformerEnd = [] if TransformerEnd is None else TransformerEnd

        super(TransformerStarImpedance, self).__init__(*args, **kw_args)

    _attrs = ["x0", "x", "r0", "r"]
    _attr_types = {"x0": float, "x": float, "r0": float, "r": float}
    _defaults = {"x0": 0.0, "x": 0.0, "r0": 0.0, "r": 0.0}
    _enums = {}
    _refs = ["TransformerEnd"]
    _many_refs = ["TransformerEnd"]

    def getTransformerEnd(self):
        """All transformer ends having this star impedance.
        """
        return self._TransformerEnd

    def setTransformerEnd(self, value):
        for x in self._TransformerEnd:
            x.StarImpedance = None
        for y in value:
            y._StarImpedance = self
        self._TransformerEnd = value

    TransformerEnd = property(getTransformerEnd, setTransformerEnd)

    def addTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.StarImpedance = self

    def removeTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.StarImpedance = None

