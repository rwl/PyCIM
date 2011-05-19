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

class ReliabilityInfo(IdentifiedObject):
    """Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.
    """

    def __init__(self, momFailureRate=0.0, mTTR=0.0, Specification=None, Assets=None, *args, **kw_args):
        """Initialises a new 'ReliabilityInfo' instance.

        @param momFailureRate: Momentary failure rate (temporary failures/kft-year). 
        @param mTTR: Mean time to repair (MTTR - hours). 
        @param Specification:
        @param Assets:
        """
        #: Momentary failure rate (temporary failures/kft-year).
        self.momFailureRate = momFailureRate

        #: Mean time to repair (MTTR - hours).
        self.mTTR = mTTR

        self._Specification = None
        self.Specification = Specification

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(ReliabilityInfo, self).__init__(*args, **kw_args)

    _attrs = ["momFailureRate", "mTTR"]
    _attr_types = {"momFailureRate": float, "mTTR": float}
    _defaults = {"momFailureRate": 0.0, "mTTR": 0.0}
    _enums = {}
    _refs = ["Specification", "Assets"]
    _many_refs = ["Assets"]

    def getSpecification(self):
        
        return self._Specification

    def setSpecification(self, value):
        if self._Specification is not None:
            filtered = [x for x in self.Specification.ReliabilityInfos if x != self]
            self._Specification._ReliabilityInfos = filtered

        self._Specification = value
        if self._Specification is not None:
            if self not in self._Specification._ReliabilityInfos:
                self._Specification._ReliabilityInfos.append(self)

    Specification = property(getSpecification, setSpecification)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.ReliabilityInfos if q != self]
            self._Assets._ReliabilityInfos = filtered
        for r in value:
            if self not in r._ReliabilityInfos:
                r._ReliabilityInfos.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._ReliabilityInfos:
                obj._ReliabilityInfos.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._ReliabilityInfos:
                obj._ReliabilityInfos.remove(self)
            self._Assets.remove(obj)

