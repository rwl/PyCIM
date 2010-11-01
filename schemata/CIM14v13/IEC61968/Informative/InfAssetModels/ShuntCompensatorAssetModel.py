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

class ShuntCompensatorAssetModel(ElectricalAssetModel):
    """For application as shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer (Organisation). There are typically many instances of an asset associated with a single asset model.
    """

    def __init__(self, ShuntCompensatorAssets=None, ShuntCompensatorTypeAsset=None, ShuntImpedanceInfo=None, *args, **kw_args):
        """Initializes a new 'ShuntCompensatorAssetModel' instance.

        @param ShuntCompensatorAssets:
        @param ShuntCompensatorTypeAsset:
        @param ShuntImpedanceInfo:
        """
        self._ShuntCompensatorAssets = []
        self.ShuntCompensatorAssets = [] if ShuntCompensatorAssets is None else ShuntCompensatorAssets

        self._ShuntCompensatorTypeAsset = None
        self.ShuntCompensatorTypeAsset = ShuntCompensatorTypeAsset

        self._ShuntImpedanceInfo = None
        self.ShuntImpedanceInfo = ShuntImpedanceInfo

        super(ShuntCompensatorAssetModel, self).__init__(*args, **kw_args)

    def getShuntCompensatorAssets(self):
        
        return self._ShuntCompensatorAssets

    def setShuntCompensatorAssets(self, value):
        for x in self._ShuntCompensatorAssets:
            x._ShuntCompensatorAssetModel = None
        for y in value:
            y._ShuntCompensatorAssetModel = self
        self._ShuntCompensatorAssets = value

    ShuntCompensatorAssets = property(getShuntCompensatorAssets, setShuntCompensatorAssets)

    def addShuntCompensatorAssets(self, *ShuntCompensatorAssets):
        for obj in ShuntCompensatorAssets:
            obj._ShuntCompensatorAssetModel = self
            self._ShuntCompensatorAssets.append(obj)

    def removeShuntCompensatorAssets(self, *ShuntCompensatorAssets):
        for obj in ShuntCompensatorAssets:
            obj._ShuntCompensatorAssetModel = None
            self._ShuntCompensatorAssets.remove(obj)

    def getShuntCompensatorTypeAsset(self):
        
        return self._ShuntCompensatorTypeAsset

    def setShuntCompensatorTypeAsset(self, value):
        if self._ShuntCompensatorTypeAsset is not None:
            filtered = [x for x in self.ShuntCompensatorTypeAsset.ShuntCompensatorAssetModels if x != self]
            self._ShuntCompensatorTypeAsset._ShuntCompensatorAssetModels = filtered

        self._ShuntCompensatorTypeAsset = value
        if self._ShuntCompensatorTypeAsset is not None:
            self._ShuntCompensatorTypeAsset._ShuntCompensatorAssetModels.append(self)

    ShuntCompensatorTypeAsset = property(getShuntCompensatorTypeAsset, setShuntCompensatorTypeAsset)

    def getShuntImpedanceInfo(self):
        
        return self._ShuntImpedanceInfo

    def setShuntImpedanceInfo(self, value):
        if self._ShuntImpedanceInfo is not None:
            self._ShuntImpedanceInfo._ShuntCompensatorAssetModel = None

        self._ShuntImpedanceInfo = value
        if self._ShuntImpedanceInfo is not None:
            self._ShuntImpedanceInfo._ShuntCompensatorAssetModel = self

    ShuntImpedanceInfo = property(getShuntImpedanceInfo, setShuntImpedanceInfo)

