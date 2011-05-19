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

from CIM15.IEC61970.Wires.TransformerEnd import TransformerEnd

class TransformerTankEnd(TransformerEnd):
    """Transformer tank end represents an individual winding for unbalanced models or for transformer tanks connected into a bank (and bank is modelled with the PowerTransformer).Transformer tank end represents an individual winding for unbalanced models or for transformer tanks connected into a bank (and bank is modelled with the PowerTransformer).
    """

    def __init__(self, phases="s12N", TransformerTank=None, *args, **kw_args):
        """Initialises a new 'TransformerTankEnd' instance.

        @param phases: Describes the phases carried by a conducting equipment. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param TransformerTank: Transformer this winding belongs to.
        """
        #: Describes the phases carried by a conducting equipment. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phases = phases

        self._TransformerTank = None
        self.TransformerTank = TransformerTank

        super(TransformerTankEnd, self).__init__(*args, **kw_args)

    _attrs = ["phases"]
    _attr_types = {"phases": str}
    _defaults = {"phases": "s12N"}
    _enums = {"phases": "PhaseCode"}
    _refs = ["TransformerTank"]
    _many_refs = []

    def getTransformerTank(self):
        """Transformer this winding belongs to.
        """
        return self._TransformerTank

    def setTransformerTank(self, value):
        if self._TransformerTank is not None:
            filtered = [x for x in self.TransformerTank.TransformerTankEnds if x != self]
            self._TransformerTank._TransformerTankEnds = filtered

        self._TransformerTank = value
        if self._TransformerTank is not None:
            if self not in self._TransformerTank._TransformerTankEnds:
                self._TransformerTank._TransformerTankEnds.append(self)

    TransformerTank = property(getTransformerTank, setTransformerTank)

