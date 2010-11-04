# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ReliabilityInfo(IdentifiedObject):
    """Information regarding the experienced and expected reliability of a specific asset, type of asset, or asset model.
    """

    def __init__(self, momFailureRate=0.0, mTTR=0.0, Specification=None, Assets=None, *args, **kw_args):
        """Initializes a new 'ReliabilityInfo' instance.

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

    def getSpecification(self):
        
        return self._Specification

    def setSpecification(self, value):
        if self._Specification is not None:
            filtered = [x for x in self.Specification.ReliabilityInfos if x != self]
            self._Specification._ReliabilityInfos = filtered

        self._Specification = value
        if self._Specification is not None:
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

