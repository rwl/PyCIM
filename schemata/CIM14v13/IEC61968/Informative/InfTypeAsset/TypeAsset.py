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

from CIM14v13.IEC61968.Common.Document import Document

class TypeAsset(Document):
    """Whereas an AssetModel is a particular model and version of a vendor's product, a TypeAsset is documentation for a generic asset or material item that may be used for design purposes. Any number of AssetModels may be used to perform this generic function. The primary role of the TypeAsset is typically defined by the PowereSystemResource it is associated with.
    """

    def __init__(self, quantity='', stockItem=False, estimatedUnitCost=0.0, CUWorkEquipmentAsset=None, CUAsset=None, TypeAssetCatalogue=None, AssetModels=None, ErpInventoryIssues=None, ErpReqLineItems=None, ErpBomItemDatas=None, *args, **kw_args):
        """Initializes a new 'TypeAsset' instance.

        @param quantity: The value, unit of measure, and multiplier for the quantity. 
        @param stockItem: True if item is a stock item (default). 
        @param estimatedUnitCost: Estimated unit cost (or cost per unit length) of this type of asset. It does not include labor to install/construct or configure it. 
        @param CUWorkEquipmentAsset:
        @param CUAsset:
        @param TypeAssetCatalogue:
        @param AssetModels: A type of asset may be satisified with many different types of asset models.
        @param ErpInventoryIssues:
        @param ErpReqLineItems:
        @param ErpBomItemDatas:
        """
        #: The value, unit of measure, and multiplier for the quantity. 
        self.quantity = quantity

        #: True if item is a stock item (default). 
        self.stockItem = stockItem

        #: Estimated unit cost (or cost per unit length) of this type of asset. It does not include labor to install/construct or configure it. 
        self.estimatedUnitCost = estimatedUnitCost

        self._CUWorkEquipmentAsset = None
        self.CUWorkEquipmentAsset = CUWorkEquipmentAsset

        self._CUAsset = None
        self.CUAsset = CUAsset

        self._TypeAssetCatalogue = None
        self.TypeAssetCatalogue = TypeAssetCatalogue

        self._AssetModels = []
        self.AssetModels = [] if AssetModels is None else AssetModels

        self._ErpInventoryIssues = []
        self.ErpInventoryIssues = [] if ErpInventoryIssues is None else ErpInventoryIssues

        self._ErpReqLineItems = []
        self.ErpReqLineItems = [] if ErpReqLineItems is None else ErpReqLineItems

        self._ErpBomItemDatas = []
        self.ErpBomItemDatas = [] if ErpBomItemDatas is None else ErpBomItemDatas

        super(TypeAsset, self).__init__(*args, **kw_args)

    def getCUWorkEquipmentAsset(self):
        
        return self._CUWorkEquipmentAsset

    def setCUWorkEquipmentAsset(self, value):
        if self._CUWorkEquipmentAsset is not None:
            self._CUWorkEquipmentAsset._TypeAsset = None

        self._CUWorkEquipmentAsset = value
        if self._CUWorkEquipmentAsset is not None:
            self._CUWorkEquipmentAsset._TypeAsset = self

    CUWorkEquipmentAsset = property(getCUWorkEquipmentAsset, setCUWorkEquipmentAsset)

    def getCUAsset(self):
        
        return self._CUAsset

    def setCUAsset(self, value):
        if self._CUAsset is not None:
            self._CUAsset._TypeAsset = None

        self._CUAsset = value
        if self._CUAsset is not None:
            self._CUAsset._TypeAsset = self

    CUAsset = property(getCUAsset, setCUAsset)

    def getTypeAssetCatalogue(self):
        
        return self._TypeAssetCatalogue

    def setTypeAssetCatalogue(self, value):
        if self._TypeAssetCatalogue is not None:
            filtered = [x for x in self.TypeAssetCatalogue.TypeAssets if x != self]
            self._TypeAssetCatalogue._TypeAssets = filtered

        self._TypeAssetCatalogue = value
        if self._TypeAssetCatalogue is not None:
            self._TypeAssetCatalogue._TypeAssets.append(self)

    TypeAssetCatalogue = property(getTypeAssetCatalogue, setTypeAssetCatalogue)

    def getAssetModels(self):
        """A type of asset may be satisified with many different types of asset models.
        """
        return self._AssetModels

    def setAssetModels(self, value):
        for x in self._AssetModels:
            x._TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._AssetModels = value

    AssetModels = property(getAssetModels, setAssetModels)

    def addAssetModels(self, *AssetModels):
        for obj in AssetModels:
            obj._TypeAsset = self
            self._AssetModels.append(obj)

    def removeAssetModels(self, *AssetModels):
        for obj in AssetModels:
            obj._TypeAsset = None
            self._AssetModels.remove(obj)

    def getErpInventoryIssues(self):
        
        return self._ErpInventoryIssues

    def setErpInventoryIssues(self, value):
        for x in self._ErpInventoryIssues:
            x._TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._ErpInventoryIssues = value

    ErpInventoryIssues = property(getErpInventoryIssues, setErpInventoryIssues)

    def addErpInventoryIssues(self, *ErpInventoryIssues):
        for obj in ErpInventoryIssues:
            obj._TypeAsset = self
            self._ErpInventoryIssues.append(obj)

    def removeErpInventoryIssues(self, *ErpInventoryIssues):
        for obj in ErpInventoryIssues:
            obj._TypeAsset = None
            self._ErpInventoryIssues.remove(obj)

    def getErpReqLineItems(self):
        
        return self._ErpReqLineItems

    def setErpReqLineItems(self, value):
        for x in self._ErpReqLineItems:
            x._TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._ErpReqLineItems = value

    ErpReqLineItems = property(getErpReqLineItems, setErpReqLineItems)

    def addErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj._TypeAsset = self
            self._ErpReqLineItems.append(obj)

    def removeErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj._TypeAsset = None
            self._ErpReqLineItems.remove(obj)

    def getErpBomItemDatas(self):
        
        return self._ErpBomItemDatas

    def setErpBomItemDatas(self, value):
        for x in self._ErpBomItemDatas:
            x._TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._ErpBomItemDatas = value

    ErpBomItemDatas = property(getErpBomItemDatas, setErpBomItemDatas)

    def addErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj._TypeAsset = self
            self._ErpBomItemDatas.append(obj)

    def removeErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj._TypeAsset = None
            self._ErpBomItemDatas.remove(obj)

