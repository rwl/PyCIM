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

from CIM15.CDPSM.Asset.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerTank(IdentifiedObject):
    """An assembly of two or more coupled windings that transform electrical power between voltage levels. These windings are bound on a common core and place in the same tank. Transformer tank can be used to model both single-phase and 3-phase transformers.
    """

    def __init__(self, TransformerTankInfo=None, *args, **kw_args):
        """Initialises a new 'TransformerTank' instance.

        @param TransformerTankInfo: Transformer tank data.
        """
        self._TransformerTankInfo = None
        self.TransformerTankInfo = TransformerTankInfo

        super(TransformerTank, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["TransformerTankInfo"]
    _many_refs = []

    def getTransformerTankInfo(self):
        """Transformer tank data.
        """
        return self._TransformerTankInfo

    def setTransformerTankInfo(self, value):
        if self._TransformerTankInfo is not None:
            filtered = [x for x in self.TransformerTankInfo.TransformerTanks if x != self]
            self._TransformerTankInfo._TransformerTanks = filtered

        self._TransformerTankInfo = value
        if self._TransformerTankInfo is not None:
            if self not in self._TransformerTankInfo._TransformerTanks:
                self._TransformerTankInfo._TransformerTanks.append(self)

    TransformerTankInfo = property(getTransformerTankInfo, setTransformerTankInfo)

