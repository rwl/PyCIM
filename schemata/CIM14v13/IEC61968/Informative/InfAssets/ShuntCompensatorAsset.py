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

class ShuntCompensatorAsset(ElectricalAsset):
    """For a shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is the physical asset performing the ShuntCompensator role (PSR).
    """

    def __init__(self, ShuntCompensatorAssetModel=None, ShuntImpedanceInfo=None, **kw_args):
        """Initializes a new 'ShuntCompensatorAsset' instance.

        @param ShuntCompensatorAssetModel:
        @param ShuntImpedanceInfo:
        """
        self._ShuntCompensatorAssetModel = None
        self.ShuntCompensatorAssetModel = ShuntCompensatorAssetModel

        self._ShuntImpedanceInfo = None
        self.ShuntImpedanceInfo = ShuntImpedanceInfo

        super(ShuntCompensatorAsset, self).__init__(**kw_args)

    def getShuntCompensatorAssetModel(self):
        
        return self._ShuntCompensatorAssetModel

    def setShuntCompensatorAssetModel(self, value):
        if self._ShuntCompensatorAssetModel is not None:
            filtered = [x for x in self.ShuntCompensatorAssetModel.ShuntCompensatorAssets if x != self]
            self._ShuntCompensatorAssetModel._ShuntCompensatorAssets = filtered

        self._ShuntCompensatorAssetModel = value
        if self._ShuntCompensatorAssetModel is not None:
            self._ShuntCompensatorAssetModel._ShuntCompensatorAssets.append(self)

    ShuntCompensatorAssetModel = property(getShuntCompensatorAssetModel, setShuntCompensatorAssetModel)

    def getShuntImpedanceInfo(self):
        
        return self._ShuntImpedanceInfo

    def setShuntImpedanceInfo(self, value):
        if self._ShuntImpedanceInfo is not None:
            filtered = [x for x in self.ShuntImpedanceInfo.ShuntCompensatorAssets if x != self]
            self._ShuntImpedanceInfo._ShuntCompensatorAssets = filtered

        self._ShuntImpedanceInfo = value
        if self._ShuntImpedanceInfo is not None:
            self._ShuntImpedanceInfo._ShuntCompensatorAssets.append(self)

    ShuntImpedanceInfo = property(getShuntImpedanceInfo, setShuntImpedanceInfo)

