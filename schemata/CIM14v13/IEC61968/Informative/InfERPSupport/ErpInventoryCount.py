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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpInventoryCount(IdentifiedObject):
    """This is related to Inventory physical counts organized by AssetModel. Note that a count of a type of asset can be accomplished by the association inherited by AssetModel (from Document) to Asset. It enables ERP applications to transfer an inventory count between ERP and the actual physical inventory location. This count may be a cycle count or a physical count.
    """

    def __init__(self, AssetModel=None, MaterialItem=None, status=None, **kw_args):
        """Initializes a new 'ErpInventoryCount' instance.

        @param AssetModel:
        @param MaterialItem:
        @param status:
        """
        self._AssetModel = None
        self.AssetModel = AssetModel

        self._MaterialItem = None
        self.MaterialItem = MaterialItem

        self.status = status

        super(ErpInventoryCount, self).__init__(**kw_args)

    def getAssetModel(self):
        
        return self._AssetModel

    def setAssetModel(self, value):
        if self._AssetModel is not None:
            filtered = [x for x in self.AssetModel.ErpInventoryCounts if x != self]
            self._AssetModel._ErpInventoryCounts = filtered

        self._AssetModel = value
        if self._AssetModel is not None:
            self._AssetModel._ErpInventoryCounts.append(self)

    AssetModel = property(getAssetModel, setAssetModel)

    def getMaterialItem(self):
        
        return self._MaterialItem

    def setMaterialItem(self, value):
        if self._MaterialItem is not None:
            filtered = [x for x in self.MaterialItem.ErpInventoryCounts if x != self]
            self._MaterialItem._ErpInventoryCounts = filtered

        self._MaterialItem = value
        if self._MaterialItem is not None:
            self._MaterialItem._ErpInventoryCounts.append(self)

    MaterialItem = property(getMaterialItem, setMaterialItem)

    status = None

