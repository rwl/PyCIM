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

from CIM14v13.IEC61968.Informative.InfTypeAsset.ElectricalTypeAsset import ElectricalTypeAsset

class BusbarTypeAsset(ElectricalTypeAsset):
    """Documentation for a generic busbar that may be used for design purposes. It is typically associated with PoserSystemResource BusbarSection.
    """

    def __init__(self, BusbarTypeAssets=None, *args, **kw_args):
        """Initializes a new 'BusbarTypeAsset' instance.

        @param BusbarTypeAssets:
        """
        self._BusbarTypeAssets = []
        self.BusbarTypeAssets = [] if BusbarTypeAssets is None else BusbarTypeAssets

        super(BusbarTypeAsset, self).__init__(*args, **kw_args)

    def getBusbarTypeAssets(self):
        
        return self._BusbarTypeAssets

    def setBusbarTypeAssets(self, value):
        for x in self._BusbarTypeAssets:
            x._BusbarAssetModel = None
        for y in value:
            y._BusbarAssetModel = self
        self._BusbarTypeAssets = value

    BusbarTypeAssets = property(getBusbarTypeAssets, setBusbarTypeAssets)

    def addBusbarTypeAssets(self, *BusbarTypeAssets):
        for obj in BusbarTypeAssets:
            obj._BusbarAssetModel = self
            self._BusbarTypeAssets.append(obj)

    def removeBusbarTypeAssets(self, *BusbarTypeAssets):
        for obj in BusbarTypeAssets:
            obj._BusbarAssetModel = None
            self._BusbarTypeAssets.remove(obj)

