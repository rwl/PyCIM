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

class PotentialTransformerInfo(ElectricalInfo):
    """Used to define either the required additional electrical properties of a type of a Potential Transformer (PT), or a PT Model.
    """

    def __init__(self, primaryRatio=None, tertiaryRatio=None, secondaryRatio=None, PotentialTransformerAssets=None, PotentialTransformerAssetModels=None, PotentialTransformerTypeAsset=None, *args, **kw_args):
        """Initializes a new 'PotentialTransformerInfo' instance.

        @param primaryRatio: Ratio for the primary winding tap changer.
        @param tertiaryRatio: Ratio for the tertiary winding tap changer.
        @param secondaryRatio: Ratio for the secondary winding tap changer.
        @param PotentialTransformerAssets:
        @param PotentialTransformerAssetModels:
        @param PotentialTransformerTypeAsset:
        """
        self.primaryRatio = primaryRatio

        self.tertiaryRatio = tertiaryRatio

        self.secondaryRatio = secondaryRatio

        self._PotentialTransformerAssets = []
        self.PotentialTransformerAssets = [] if PotentialTransformerAssets is None else PotentialTransformerAssets

        self._PotentialTransformerAssetModels = []
        self.PotentialTransformerAssetModels = [] if PotentialTransformerAssetModels is None else PotentialTransformerAssetModels

        self._PotentialTransformerTypeAsset = None
        self.PotentialTransformerTypeAsset = PotentialTransformerTypeAsset

        super(PotentialTransformerInfo, self).__init__(*args, **kw_args)

    # Ratio for the primary winding tap changer.
    primaryRatio = None

    # Ratio for the tertiary winding tap changer.
    tertiaryRatio = None

    # Ratio for the secondary winding tap changer.
    secondaryRatio = None

    def getPotentialTransformerAssets(self):
        
        return self._PotentialTransformerAssets

    def setPotentialTransformerAssets(self, value):
        for x in self._PotentialTransformerAssets:
            x._PotentialTransformerInfo = None
        for y in value:
            y._PotentialTransformerInfo = self
        self._PotentialTransformerAssets = value

    PotentialTransformerAssets = property(getPotentialTransformerAssets, setPotentialTransformerAssets)

    def addPotentialTransformerAssets(self, *PotentialTransformerAssets):
        for obj in PotentialTransformerAssets:
            obj._PotentialTransformerInfo = self
            self._PotentialTransformerAssets.append(obj)

    def removePotentialTransformerAssets(self, *PotentialTransformerAssets):
        for obj in PotentialTransformerAssets:
            obj._PotentialTransformerInfo = None
            self._PotentialTransformerAssets.remove(obj)

    def getPotentialTransformerAssetModels(self):
        
        return self._PotentialTransformerAssetModels

    def setPotentialTransformerAssetModels(self, value):
        for x in self._PotentialTransformerAssetModels:
            x._PotentialTransformerInfo = None
        for y in value:
            y._PotentialTransformerInfo = self
        self._PotentialTransformerAssetModels = value

    PotentialTransformerAssetModels = property(getPotentialTransformerAssetModels, setPotentialTransformerAssetModels)

    def addPotentialTransformerAssetModels(self, *PotentialTransformerAssetModels):
        for obj in PotentialTransformerAssetModels:
            obj._PotentialTransformerInfo = self
            self._PotentialTransformerAssetModels.append(obj)

    def removePotentialTransformerAssetModels(self, *PotentialTransformerAssetModels):
        for obj in PotentialTransformerAssetModels:
            obj._PotentialTransformerInfo = None
            self._PotentialTransformerAssetModels.remove(obj)

    def getPotentialTransformerTypeAsset(self):
        
        return self._PotentialTransformerTypeAsset

    def setPotentialTransformerTypeAsset(self, value):
        if self._PotentialTransformerTypeAsset is not None:
            self._PotentialTransformerTypeAsset._PotentialTransformerInfo = None

        self._PotentialTransformerTypeAsset = value
        if self._PotentialTransformerTypeAsset is not None:
            self._PotentialTransformerTypeAsset._PotentialTransformerInfo = self

    PotentialTransformerTypeAsset = property(getPotentialTransformerTypeAsset, setPotentialTransformerTypeAsset)

