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

from CIM15.IEC61968.AssetModels.CableInfo import CableInfo

class ConcentricNeutralCableInfo(CableInfo):
    """Concentric neutral cable data.Concentric neutral cable data.
    """

    def __init__(self, neutralStrandCount=0, diameterOverNeutral=0.0, WireType=None, *args, **kw_args):
        """Initialises a new 'ConcentricNeutralCableInfo' instance.

        @param neutralStrandCount: Number of concentric neutral strands. 
        @param diameterOverNeutral: Diameter over the concentric neutral strands. 
        @param WireType: Wire type used for this concentric neutral cable.
        """
        #: Number of concentric neutral strands.
        self.neutralStrandCount = neutralStrandCount

        #: Diameter over the concentric neutral strands.
        self.diameterOverNeutral = diameterOverNeutral

        self._WireType = None
        self.WireType = WireType

        super(ConcentricNeutralCableInfo, self).__init__(*args, **kw_args)

    _attrs = ["neutralStrandCount", "diameterOverNeutral"]
    _attr_types = {"neutralStrandCount": int, "diameterOverNeutral": float}
    _defaults = {"neutralStrandCount": 0, "diameterOverNeutral": 0.0}
    _enums = {}
    _refs = ["WireType"]
    _many_refs = []

    def getWireType(self):
        """Wire type used for this concentric neutral cable.
        """
        return self._WireType

    def setWireType(self, value):
        if self._WireType is not None:
            filtered = [x for x in self.WireType.ConcentricNeutralCableInfos if x != self]
            self._WireType._ConcentricNeutralCableInfos = filtered

        self._WireType = value
        if self._WireType is not None:
            if self not in self._WireType._ConcentricNeutralCableInfos:
                self._WireType._ConcentricNeutralCableInfos.append(self)

    WireType = property(getWireType, setWireType)

