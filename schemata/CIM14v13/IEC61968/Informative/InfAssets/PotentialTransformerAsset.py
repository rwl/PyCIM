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

from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset

class PotentialTransformerAsset(ElectricalAsset):
    """Physical asset performing Potential Transformer (PT) function.
    """

    def __init__(self, PotentialTransformer=None, PotentialTransformerInfo=None, PotentialTransformerAssetModel=None, *args, **kw_args):
        """Initializes a new 'PotentialTransformerAsset' instance.

        @param PotentialTransformer:
        @param PotentialTransformerInfo:
        @param PotentialTransformerAssetModel:
        """
        self._PotentialTransformer = None
        self.PotentialTransformer = PotentialTransformer

        self._PotentialTransformerInfo = None
        self.PotentialTransformerInfo = PotentialTransformerInfo

        self._PotentialTransformerAssetModel = None
        self.PotentialTransformerAssetModel = PotentialTransformerAssetModel

        super(PotentialTransformerAsset, self).__init__(*args, **kw_args)

    def getPotentialTransformer(self):
        
        return self._PotentialTransformer

    def setPotentialTransformer(self, value):
        if self._PotentialTransformer is not None:
            self._PotentialTransformer._PotentialTransformerAsset = None

        self._PotentialTransformer = value
        if self._PotentialTransformer is not None:
            self._PotentialTransformer._PotentialTransformerAsset = self

    PotentialTransformer = property(getPotentialTransformer, setPotentialTransformer)

    def getPotentialTransformerInfo(self):
        
        return self._PotentialTransformerInfo

    def setPotentialTransformerInfo(self, value):
        if self._PotentialTransformerInfo is not None:
            filtered = [x for x in self.PotentialTransformerInfo.PotentialTransformerAssets if x != self]
            self._PotentialTransformerInfo._PotentialTransformerAssets = filtered

        self._PotentialTransformerInfo = value
        if self._PotentialTransformerInfo is not None:
            self._PotentialTransformerInfo._PotentialTransformerAssets.append(self)

    PotentialTransformerInfo = property(getPotentialTransformerInfo, setPotentialTransformerInfo)

    def getPotentialTransformerAssetModel(self):
        
        return self._PotentialTransformerAssetModel

    def setPotentialTransformerAssetModel(self, value):
        if self._PotentialTransformerAssetModel is not None:
            filtered = [x for x in self.PotentialTransformerAssetModel.PotentialTransformerAssets if x != self]
            self._PotentialTransformerAssetModel._PotentialTransformerAssets = filtered

        self._PotentialTransformerAssetModel = value
        if self._PotentialTransformerAssetModel is not None:
            self._PotentialTransformerAssetModel._PotentialTransformerAssets.append(self)

    PotentialTransformerAssetModel = property(getPotentialTransformerAssetModel, setPotentialTransformerAssetModel)

