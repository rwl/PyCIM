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

from CIM14v13.IEC61968.Assets.ElectricalInfo import ElectricalInfo

class SVCInfo(ElectricalInfo):
    """Properties for an SVC, allowing the capacitive and inductive ratings for each phase to be specified individually if required.
    """

    def __init__(self, capacitiveRating=0.0, inductiveRating=0.0, SVCTypeAssets=None, SVCAsset=None, SVCAssetModel=None, *args, **kw_args):
        """Initializes a new 'SVCInfo' instance.

        @param capacitiveRating: Maximum capacitive reactive power 
        @param inductiveRating: Maximum inductive reactive power 
        @param SVCTypeAssets:
        @param SVCAsset:
        @param SVCAssetModel:
        """
        #: Maximum capacitive reactive power 
        self.capacitiveRating = capacitiveRating

        #: Maximum inductive reactive power 
        self.inductiveRating = inductiveRating

        self._SVCTypeAssets = []
        self.SVCTypeAssets = [] if SVCTypeAssets is None else SVCTypeAssets

        self._SVCAsset = None
        self.SVCAsset = SVCAsset

        self._SVCAssetModel = None
        self.SVCAssetModel = SVCAssetModel

        super(SVCInfo, self).__init__(*args, **kw_args)

    def getSVCTypeAssets(self):
        
        return self._SVCTypeAssets

    def setSVCTypeAssets(self, value):
        for p in self._SVCTypeAssets:
            filtered = [q for q in p.SvcInfos if q != self]
            self._SVCTypeAssets._SvcInfos = filtered
        for r in value:
            if self not in r._SvcInfos:
                r._SvcInfos.append(self)
        self._SVCTypeAssets = value

    SVCTypeAssets = property(getSVCTypeAssets, setSVCTypeAssets)

    def addSVCTypeAssets(self, *SVCTypeAssets):
        for obj in SVCTypeAssets:
            if self not in obj._SvcInfos:
                obj._SvcInfos.append(self)
            self._SVCTypeAssets.append(obj)

    def removeSVCTypeAssets(self, *SVCTypeAssets):
        for obj in SVCTypeAssets:
            if self in obj._SvcInfos:
                obj._SvcInfos.remove(self)
            self._SVCTypeAssets.remove(obj)

    def getSVCAsset(self):
        
        return self._SVCAsset

    def setSVCAsset(self, value):
        if self._SVCAsset is not None:
            self._SVCAsset._SvcInfo = None

        self._SVCAsset = value
        if self._SVCAsset is not None:
            self._SVCAsset._SvcInfo = self

    SVCAsset = property(getSVCAsset, setSVCAsset)

    def getSVCAssetModel(self):
        
        return self._SVCAssetModel

    def setSVCAssetModel(self, value):
        if self._SVCAssetModel is not None:
            self._SVCAssetModel._SvcInfo = None

        self._SVCAssetModel = value
        if self._SVCAssetModel is not None:
            self._SVCAssetModel._SvcInfo = self

    SVCAssetModel = property(getSVCAssetModel, setSVCAssetModel)

