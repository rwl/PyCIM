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

class BusbarAssetModel(ElectricalAssetModel):
    """Documentation for a type of a busbar asset of a particular product model made by a manufacturer.
    """

    def __init__(self, BusbarAssets=None, BusbarAssetModel=None, **kw_args):
        """Initializes a new 'BusbarAssetModel' instance.

        @param BusbarAssets:
        @param BusbarAssetModel:
        """
        self._BusbarAssets = []
        self.BusbarAssets = [] if BusbarAssets is None else BusbarAssets

        self._BusbarAssetModel = None
        self.BusbarAssetModel = BusbarAssetModel

        super(BusbarAssetModel, self).__init__(**kw_args)

    def getBusbarAssets(self):
        
        return self._BusbarAssets

    def setBusbarAssets(self, value):
        for x in self._BusbarAssets:
            x._BusbarAssetModel = None
        for y in value:
            y._BusbarAssetModel = self
        self._BusbarAssets = value

    BusbarAssets = property(getBusbarAssets, setBusbarAssets)

    def addBusbarAssets(self, *BusbarAssets):
        for obj in BusbarAssets:
            obj._BusbarAssetModel = self
            self._BusbarAssets.append(obj)

    def removeBusbarAssets(self, *BusbarAssets):
        for obj in BusbarAssets:
            obj._BusbarAssetModel = None
            self._BusbarAssets.remove(obj)

    def getBusbarAssetModel(self):
        
        return self._BusbarAssetModel

    def setBusbarAssetModel(self, value):
        if self._BusbarAssetModel is not None:
            filtered = [x for x in self.BusbarAssetModel.BusbarTypeAssets if x != self]
            self._BusbarAssetModel._BusbarTypeAssets = filtered

        self._BusbarAssetModel = value
        if self._BusbarAssetModel is not None:
            self._BusbarAssetModel._BusbarTypeAssets.append(self)

    BusbarAssetModel = property(getBusbarAssetModel, setBusbarAssetModel)

