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

from CIM14v13.IEC61968.Informative.InfAssetModels.ElectricalAssetModel import ElectricalAssetModel

class PotentialTransformerAssetModel(ElectricalAssetModel):
    """A particular model supplied by a manufacturer of a Potential Transformer (PT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """

    def __init__(self, PotentialTransformerTypeAsset=None, PotentialTransformerInfo=None, PotentialTransformerAssets=None, *args, **kw_args):
        """Initializes a new 'PotentialTransformerAssetModel' instance.

        @param PotentialTransformerTypeAsset:
        @param PotentialTransformerInfo:
        @param PotentialTransformerAssets:
        """
        self._PotentialTransformerTypeAsset = None
        self.PotentialTransformerTypeAsset = PotentialTransformerTypeAsset

        self._PotentialTransformerInfo = None
        self.PotentialTransformerInfo = PotentialTransformerInfo

        self._PotentialTransformerAssets = []
        self.PotentialTransformerAssets = [] if PotentialTransformerAssets is None else PotentialTransformerAssets

        super(PotentialTransformerAssetModel, self).__init__(*args, **kw_args)

    def getPotentialTransformerTypeAsset(self):
        
        return self._PotentialTransformerTypeAsset

    def setPotentialTransformerTypeAsset(self, value):
        if self._PotentialTransformerTypeAsset is not None:
            filtered = [x for x in self.PotentialTransformerTypeAsset.PotentialTransformerAssetModels if x != self]
            self._PotentialTransformerTypeAsset._PotentialTransformerAssetModels = filtered

        self._PotentialTransformerTypeAsset = value
        if self._PotentialTransformerTypeAsset is not None:
            self._PotentialTransformerTypeAsset._PotentialTransformerAssetModels.append(self)

    PotentialTransformerTypeAsset = property(getPotentialTransformerTypeAsset, setPotentialTransformerTypeAsset)

    def getPotentialTransformerInfo(self):
        
        return self._PotentialTransformerInfo

    def setPotentialTransformerInfo(self, value):
        if self._PotentialTransformerInfo is not None:
            filtered = [x for x in self.PotentialTransformerInfo.PotentialTransformerAssetModels if x != self]
            self._PotentialTransformerInfo._PotentialTransformerAssetModels = filtered

        self._PotentialTransformerInfo = value
        if self._PotentialTransformerInfo is not None:
            self._PotentialTransformerInfo._PotentialTransformerAssetModels.append(self)

    PotentialTransformerInfo = property(getPotentialTransformerInfo, setPotentialTransformerInfo)

    def getPotentialTransformerAssets(self):
        
        return self._PotentialTransformerAssets

    def setPotentialTransformerAssets(self, value):
        for x in self._PotentialTransformerAssets:
            x._PotentialTransformerAssetModel = None
        for y in value:
            y._PotentialTransformerAssetModel = self
        self._PotentialTransformerAssets = value

    PotentialTransformerAssets = property(getPotentialTransformerAssets, setPotentialTransformerAssets)

    def addPotentialTransformerAssets(self, *PotentialTransformerAssets):
        for obj in PotentialTransformerAssets:
            obj._PotentialTransformerAssetModel = self
            self._PotentialTransformerAssets.append(obj)

    def removePotentialTransformerAssets(self, *PotentialTransformerAssets):
        for obj in PotentialTransformerAssets:
            obj._PotentialTransformerAssetModel = None
            self._PotentialTransformerAssets.remove(obj)

