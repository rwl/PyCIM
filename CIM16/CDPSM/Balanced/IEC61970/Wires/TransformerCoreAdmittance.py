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

from CIM16.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerCoreAdmittance(IdentifiedObject):

    def __init__(self, g0=0.0, g=0.0, b=0.0, b0=0.0, TransformerEnd=None, *args, **kw_args):
        """Initialises a new 'TransformerCoreAdmittance' instance.

        @param g0: Zero sequence magnetizing branch conductance. 
        @param g: Magnetizing branch conductance (G mag). 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param TransformerEnd: All transformer ends having this core admittance.
        """
        #: Zero sequence magnetizing branch conductance.
        self.g0 = g0

        #: Magnetizing branch conductance (G mag).
        self.g = g

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative.
        self.b = b

        #: Zero sequence magnetizing branch susceptance.
        self.b0 = b0

        self._TransformerEnd = []
        self.TransformerEnd = [] if TransformerEnd is None else TransformerEnd

        super(TransformerCoreAdmittance, self).__init__(*args, **kw_args)

    _attrs = ["g0", "g", "b", "b0"]
    _attr_types = {"g0": float, "g": float, "b": float, "b0": float}
    _defaults = {"g0": 0.0, "g": 0.0, "b": 0.0, "b0": 0.0}
    _enums = {}
    _refs = ["TransformerEnd"]
    _many_refs = ["TransformerEnd"]

    def getTransformerEnd(self):
        """All transformer ends having this core admittance.
        """
        return self._TransformerEnd

    def setTransformerEnd(self, value):
        for x in self._TransformerEnd:
            x.CoreAdmittance = None
        for y in value:
            y._CoreAdmittance = self
        self._TransformerEnd = value

    TransformerEnd = property(getTransformerEnd, setTransformerEnd)

    def addTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.CoreAdmittance = self

    def removeTransformerEnd(self, *TransformerEnd):
        for obj in TransformerEnd:
            obj.CoreAdmittance = None

