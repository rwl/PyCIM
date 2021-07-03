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

from CIM15.CDPSM.Connectivity.IEC61970.Wires.TransformerEnd import TransformerEnd

class PowerTransformerEnd(TransformerEnd):
    """A PowerTransformerEnd is associated with each Terminal of a PowerTransformer. The impdedance values r, r0, x, and x0 of a PowerTransformerEnd represents a star equivalentas follows 1) for a two Terminal PowerTransformer the high voltage PowerTransformerEnd has non zero values on r, r0, x, and x0 while the low voltage PowerTransformerEnd has zero values for r, r0, x, and x0. 2) for a three Terminal PowerTransformer the three PowerTransformerEnds represents a star equivalent with each leg in the star represented by r, r0, x, and x0 values. 3) for a PowerTransformer with more than three Terminals the PowerTransformerEnd impedance values cannot be used. Instead use the TransformerMeshImpedance or split the transformer into multiple PowerTransformers.
    """

    def __init__(self, PowerTransformer=None, *args, **kw_args):
        """Initialises a new 'PowerTransformerEnd' instance.

        @param PowerTransformer:
        """
        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        super(PowerTransformerEnd, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PowerTransformer"]
    _many_refs = []

    def getPowerTransformer(self):
        
        return self._PowerTransformer

    def setPowerTransformer(self, value):
        if self._PowerTransformer is not None:
            filtered = [x for x in self.PowerTransformer.PowerTransformerEnd if x != self]
            self._PowerTransformer._PowerTransformerEnd = filtered

        self._PowerTransformer = value
        if self._PowerTransformer is not None:
            if self not in self._PowerTransformer._PowerTransformerEnd:
                self._PowerTransformer._PowerTransformerEnd.append(self)

    PowerTransformer = property(getPowerTransformer, setPowerTransformer)

