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

class FaultIndicatorAssetModel(ElectricalAssetModel):
    """Documentation for a type of an FaultIndicator asset of a particular product model made by a manufacturer.
    """

    def __init__(self, FaultIndicatorTypeAsset=None, FaultIndicatorAssets=None, *args, **kw_args):
        """Initializes a new 'FaultIndicatorAssetModel' instance.

        @param FaultIndicatorTypeAsset:
        @param FaultIndicatorAssets:
        """
        self._FaultIndicatorTypeAsset = None
        self.FaultIndicatorTypeAsset = FaultIndicatorTypeAsset

        self._FaultIndicatorAssets = []
        self.FaultIndicatorAssets = [] if FaultIndicatorAssets is None else FaultIndicatorAssets

        super(FaultIndicatorAssetModel, self).__init__(*args, **kw_args)

    def getFaultIndicatorTypeAsset(self):
        
        return self._FaultIndicatorTypeAsset

    def setFaultIndicatorTypeAsset(self, value):
        if self._FaultIndicatorTypeAsset is not None:
            filtered = [x for x in self.FaultIndicatorTypeAsset.FaultIndicatorAssetModels if x != self]
            self._FaultIndicatorTypeAsset._FaultIndicatorAssetModels = filtered

        self._FaultIndicatorTypeAsset = value
        if self._FaultIndicatorTypeAsset is not None:
            self._FaultIndicatorTypeAsset._FaultIndicatorAssetModels.append(self)

    FaultIndicatorTypeAsset = property(getFaultIndicatorTypeAsset, setFaultIndicatorTypeAsset)

    def getFaultIndicatorAssets(self):
        
        return self._FaultIndicatorAssets

    def setFaultIndicatorAssets(self, value):
        for x in self._FaultIndicatorAssets:
            x._FaultIndicatorAssetModel = None
        for y in value:
            y._FaultIndicatorAssetModel = self
        self._FaultIndicatorAssets = value

    FaultIndicatorAssets = property(getFaultIndicatorAssets, setFaultIndicatorAssets)

    def addFaultIndicatorAssets(self, *FaultIndicatorAssets):
        for obj in FaultIndicatorAssets:
            obj._FaultIndicatorAssetModel = self
            self._FaultIndicatorAssets.append(obj)

    def removeFaultIndicatorAssets(self, *FaultIndicatorAssets):
        for obj in FaultIndicatorAssets:
            obj._FaultIndicatorAssetModel = None
            self._FaultIndicatorAssets.remove(obj)

