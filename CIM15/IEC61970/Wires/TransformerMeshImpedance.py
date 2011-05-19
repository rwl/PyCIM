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

class TransformerMeshImpedance(IdentifiedObject):
    """Transformer mesh impedance (Delta-model) between transformer ends. The typical case is that TransformerMeshImpedance describe the impedance between two TransformerEnds pare wise, i.e. the cardinalities at both TranformerEnd associations are 1. But in cases where two or more TransformerEnds are operated connected together the cardinality at the ToTransfomerEnd role is larger than 1.Transformer mesh impedance (Delta-model) between transformer ends. The typical case is that TransformerMeshImpedance describe the impedance between two TransformerEnds pare wise, i.e. the cardinalities at both TranformerEnd associations are 1. But in cases where two or more TransformerEnds are operated connected together the cardinality at the ToTransfomerEnd role is larger than 1.
    """

    def __init__(self, r=0.0, x=0.0, x0=0.0, r0=0.0, FromTransformerEndInfo=None, ToTransformerEnd=None, ToTransformerEndInfo=None, FromTransformerEnd=None, *args, **kw_args):
        """Initialises a new 'TransformerMeshImpedance' instance.

        @param r: Resistance between the 'from' and the 'to' end, seen from the 'from' end. 
        @param x: Reactance between the 'from' and the 'to' end, seen from the 'from' end. 
        @param x0: Zero-sequence reactance between the 'from' and the 'to' end, seen from the 'from' end. 
        @param r0: Zero-sequence resistance between the 'from' and the 'to' end, seen from the 'from' end. 
        @param FromTransformerEndInfo: From end info this mesh impedance is connected to. It determines the voltage reference.
        @param ToTransformerEnd: All transformer ends this mesh impedance is connected to.
        @param ToTransformerEndInfo: All transformer end infos this mesh impedance is connected to.
        @param FromTransformerEnd: From end this mesh impedance is connected to. It determines the voltage reference.
        """
        #: Resistance between the 'from' and the 'to' end, seen from the 'from' end.
        self.r = r

        #: Reactance between the 'from' and the 'to' end, seen from the 'from' end.
        self.x = x

        #: Zero-sequence reactance between the 'from' and the 'to' end, seen from the 'from' end.
        self.x0 = x0

        #: Zero-sequence resistance between the 'from' and the 'to' end, seen from the 'from' end.
        self.r0 = r0

        self._FromTransformerEndInfo = None
        self.FromTransformerEndInfo = FromTransformerEndInfo

        self._ToTransformerEnd = []
        self.ToTransformerEnd = [] if ToTransformerEnd is None else ToTransformerEnd

        self._ToTransformerEndInfo = []
        self.ToTransformerEndInfo = [] if ToTransformerEndInfo is None else ToTransformerEndInfo

        self._FromTransformerEnd = None
        self.FromTransformerEnd = FromTransformerEnd

        super(TransformerMeshImpedance, self).__init__(*args, **kw_args)

    _attrs = ["r", "x", "x0", "r0"]
    _attr_types = {"r": float, "x": float, "x0": float, "r0": float}
    _defaults = {"r": 0.0, "x": 0.0, "x0": 0.0, "r0": 0.0}
    _enums = {}
    _refs = ["FromTransformerEndInfo", "ToTransformerEnd", "ToTransformerEndInfo", "FromTransformerEnd"]
    _many_refs = ["ToTransformerEnd", "ToTransformerEndInfo"]

    def getFromTransformerEndInfo(self):
        """From end info this mesh impedance is connected to. It determines the voltage reference.
        """
        return self._FromTransformerEndInfo

    def setFromTransformerEndInfo(self, value):
        if self._FromTransformerEndInfo is not None:
            filtered = [x for x in self.FromTransformerEndInfo.FromMeshImpedance if x != self]
            self._FromTransformerEndInfo._FromMeshImpedance = filtered

        self._FromTransformerEndInfo = value
        if self._FromTransformerEndInfo is not None:
            if self not in self._FromTransformerEndInfo._FromMeshImpedance:
                self._FromTransformerEndInfo._FromMeshImpedance.append(self)

    FromTransformerEndInfo = property(getFromTransformerEndInfo, setFromTransformerEndInfo)

    def getToTransformerEnd(self):
        """All transformer ends this mesh impedance is connected to.
        """
        return self._ToTransformerEnd

    def setToTransformerEnd(self, value):
        for p in self._ToTransformerEnd:
            filtered = [q for q in p.ToMeshImpedance if q != self]
            self._ToTransformerEnd._ToMeshImpedance = filtered
        for r in value:
            if self not in r._ToMeshImpedance:
                r._ToMeshImpedance.append(self)
        self._ToTransformerEnd = value

    ToTransformerEnd = property(getToTransformerEnd, setToTransformerEnd)

    def addToTransformerEnd(self, *ToTransformerEnd):
        for obj in ToTransformerEnd:
            if self not in obj._ToMeshImpedance:
                obj._ToMeshImpedance.append(self)
            self._ToTransformerEnd.append(obj)

    def removeToTransformerEnd(self, *ToTransformerEnd):
        for obj in ToTransformerEnd:
            if self in obj._ToMeshImpedance:
                obj._ToMeshImpedance.remove(self)
            self._ToTransformerEnd.remove(obj)

    def getToTransformerEndInfo(self):
        """All transformer end infos this mesh impedance is connected to.
        """
        return self._ToTransformerEndInfo

    def setToTransformerEndInfo(self, value):
        for p in self._ToTransformerEndInfo:
            filtered = [q for q in p.ToMeshImpedance if q != self]
            self._ToTransformerEndInfo._ToMeshImpedance = filtered
        for r in value:
            if self not in r._ToMeshImpedance:
                r._ToMeshImpedance.append(self)
        self._ToTransformerEndInfo = value

    ToTransformerEndInfo = property(getToTransformerEndInfo, setToTransformerEndInfo)

    def addToTransformerEndInfo(self, *ToTransformerEndInfo):
        for obj in ToTransformerEndInfo:
            if self not in obj._ToMeshImpedance:
                obj._ToMeshImpedance.append(self)
            self._ToTransformerEndInfo.append(obj)

    def removeToTransformerEndInfo(self, *ToTransformerEndInfo):
        for obj in ToTransformerEndInfo:
            if self in obj._ToMeshImpedance:
                obj._ToMeshImpedance.remove(self)
            self._ToTransformerEndInfo.remove(obj)

    def getFromTransformerEnd(self):
        """From end this mesh impedance is connected to. It determines the voltage reference.
        """
        return self._FromTransformerEnd

    def setFromTransformerEnd(self, value):
        if self._FromTransformerEnd is not None:
            filtered = [x for x in self.FromTransformerEnd.FromMeshImpedance if x != self]
            self._FromTransformerEnd._FromMeshImpedance = filtered

        self._FromTransformerEnd = value
        if self._FromTransformerEnd is not None:
            if self not in self._FromTransformerEnd._FromMeshImpedance:
                self._FromTransformerEnd._FromMeshImpedance.append(self)

    FromTransformerEnd = property(getFromTransformerEnd, setFromTransformerEnd)

