# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Assets.AssetModel import AssetModel

class GenericAssetModelOrMaterial(AssetModel):
    """Generic asset or material item that may be used for planning, work or design purposes.Generic asset or material item that may be used for planning, work or design purposes.
    """

    def __init__(self, estimatedUnitCost=0.0, stockItem=False, quantity='', ErpReqLineItems=None, ProductAssetModels=None, ErpInventoryIssues=None, CUWorkEquipmentAsset=None, TypeAssetCatalogue=None, CUAsset=None, ErpBomItemDatas=None, *args, **kw_args):
        """Initialises a new 'GenericAssetModelOrMaterial' instance.

        @param estimatedUnitCost: Estimated unit cost (or cost per unit length) of this type of asset. It does not include labor to install/construct or configure it. 
        @param stockItem: True if item is a stock item (default). 
        @param quantity: The value, unit of measure, and multiplier for the quantity. 
        @param ErpReqLineItems:
        @param ProductAssetModels: All product asset models satisfying this generic asset model.
        @param ErpInventoryIssues:
        @param CUWorkEquipmentAsset:
        @param TypeAssetCatalogue:
        @param CUAsset:
        @param ErpBomItemDatas:
        """
        #: Estimated unit cost (or cost per unit length) of this type of asset. It does not include labor to install/construct or configure it.
        self.estimatedUnitCost = estimatedUnitCost

        #: True if item is a stock item (default).
        self.stockItem = stockItem

        #: The value, unit of measure, and multiplier for the quantity.
        self.quantity = quantity

        self._ErpReqLineItems = []
        self.ErpReqLineItems = [] if ErpReqLineItems is None else ErpReqLineItems

        self._ProductAssetModels = []
        self.ProductAssetModels = [] if ProductAssetModels is None else ProductAssetModels

        self._ErpInventoryIssues = []
        self.ErpInventoryIssues = [] if ErpInventoryIssues is None else ErpInventoryIssues

        self._CUWorkEquipmentAsset = None
        self.CUWorkEquipmentAsset = CUWorkEquipmentAsset

        self._TypeAssetCatalogue = None
        self.TypeAssetCatalogue = TypeAssetCatalogue

        self._CUAsset = None
        self.CUAsset = CUAsset

        self._ErpBomItemDatas = []
        self.ErpBomItemDatas = [] if ErpBomItemDatas is None else ErpBomItemDatas

        super(GenericAssetModelOrMaterial, self).__init__(*args, **kw_args)

    _attrs = ["estimatedUnitCost", "stockItem", "quantity"]
    _attr_types = {"estimatedUnitCost": float, "stockItem": bool, "quantity": str}
    _defaults = {"estimatedUnitCost": 0.0, "stockItem": False, "quantity": ''}
    _enums = {}
    _refs = ["ErpReqLineItems", "ProductAssetModels", "ErpInventoryIssues", "CUWorkEquipmentAsset", "TypeAssetCatalogue", "CUAsset", "ErpBomItemDatas"]
    _many_refs = ["ErpReqLineItems", "ProductAssetModels", "ErpInventoryIssues", "ErpBomItemDatas"]

    def getErpReqLineItems(self):
        
        return self._ErpReqLineItems

    def setErpReqLineItems(self, value):
        for x in self._ErpReqLineItems:
            x.TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._ErpReqLineItems = value

    ErpReqLineItems = property(getErpReqLineItems, setErpReqLineItems)

    def addErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj.TypeAsset = self

    def removeErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj.TypeAsset = None

    def getProductAssetModels(self):
        """All product asset models satisfying this generic asset model.
        """
        return self._ProductAssetModels

    def setProductAssetModels(self, value):
        for x in self._ProductAssetModels:
            x.GenericAssetModelOrMaterial = None
        for y in value:
            y._GenericAssetModelOrMaterial = self
        self._ProductAssetModels = value

    ProductAssetModels = property(getProductAssetModels, setProductAssetModels)

    def addProductAssetModels(self, *ProductAssetModels):
        for obj in ProductAssetModels:
            obj.GenericAssetModelOrMaterial = self

    def removeProductAssetModels(self, *ProductAssetModels):
        for obj in ProductAssetModels:
            obj.GenericAssetModelOrMaterial = None

    def getErpInventoryIssues(self):
        
        return self._ErpInventoryIssues

    def setErpInventoryIssues(self, value):
        for x in self._ErpInventoryIssues:
            x.TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._ErpInventoryIssues = value

    ErpInventoryIssues = property(getErpInventoryIssues, setErpInventoryIssues)

    def addErpInventoryIssues(self, *ErpInventoryIssues):
        for obj in ErpInventoryIssues:
            obj.TypeAsset = self

    def removeErpInventoryIssues(self, *ErpInventoryIssues):
        for obj in ErpInventoryIssues:
            obj.TypeAsset = None

    def getCUWorkEquipmentAsset(self):
        
        return self._CUWorkEquipmentAsset

    def setCUWorkEquipmentAsset(self, value):
        if self._CUWorkEquipmentAsset is not None:
            self._CUWorkEquipmentAsset._TypeAsset = None

        self._CUWorkEquipmentAsset = value
        if self._CUWorkEquipmentAsset is not None:
            self._CUWorkEquipmentAsset.TypeAsset = None
            self._CUWorkEquipmentAsset._TypeAsset = self

    CUWorkEquipmentAsset = property(getCUWorkEquipmentAsset, setCUWorkEquipmentAsset)

    def getTypeAssetCatalogue(self):
        
        return self._TypeAssetCatalogue

    def setTypeAssetCatalogue(self, value):
        if self._TypeAssetCatalogue is not None:
            filtered = [x for x in self.TypeAssetCatalogue.TypeAssets if x != self]
            self._TypeAssetCatalogue._TypeAssets = filtered

        self._TypeAssetCatalogue = value
        if self._TypeAssetCatalogue is not None:
            if self not in self._TypeAssetCatalogue._TypeAssets:
                self._TypeAssetCatalogue._TypeAssets.append(self)

    TypeAssetCatalogue = property(getTypeAssetCatalogue, setTypeAssetCatalogue)

    def getCUAsset(self):
        
        return self._CUAsset

    def setCUAsset(self, value):
        if self._CUAsset is not None:
            self._CUAsset._TypeAsset = None

        self._CUAsset = value
        if self._CUAsset is not None:
            self._CUAsset.TypeAsset = None
            self._CUAsset._TypeAsset = self

    CUAsset = property(getCUAsset, setCUAsset)

    def getErpBomItemDatas(self):
        
        return self._ErpBomItemDatas

    def setErpBomItemDatas(self, value):
        for x in self._ErpBomItemDatas:
            x.TypeAsset = None
        for y in value:
            y._TypeAsset = self
        self._ErpBomItemDatas = value

    ErpBomItemDatas = property(getErpBomItemDatas, setErpBomItemDatas)

    def addErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj.TypeAsset = self

    def removeErpBomItemDatas(self, *ErpBomItemDatas):
        for obj in ErpBomItemDatas:
            obj.TypeAsset = None

