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

class BusbarAsset(ElectricalAsset):
    """Physical asset used to perform the BusbarSection's role.
    """

    def __init__(self, BusbarAssetModel=None, **kw_args):
        """Initializes a new 'BusbarAsset' instance.

        @param BusbarAssetModel:
        """
        self._BusbarAssetModel = None
        self.BusbarAssetModel = BusbarAssetModel

        super(BusbarAsset, self).__init__(**kw_args)

    def getBusbarAssetModel(self):
        
        return self._BusbarAssetModel

    def setBusbarAssetModel(self, value):
        if self._BusbarAssetModel is not None:
            filtered = [x for x in self.BusbarAssetModel.BusbarAssets if x != self]
            self._BusbarAssetModel._BusbarAssets = filtered

        self._BusbarAssetModel = value
        if self._BusbarAssetModel is not None:
            self._BusbarAssetModel._BusbarAssets.append(self)

    BusbarAssetModel = property(getBusbarAssetModel, setBusbarAssetModel)

