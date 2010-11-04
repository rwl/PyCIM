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

class AssetModelCatalogueItem(Document):
    """Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """

    def __init__(self, unitCost=0.0, ErpQuoteLineItems=None, ErpPOLineItems=None, AssetModel=None, AssetModelCatalogue=None, **kw_args):
        """Initializes a new 'AssetModelCatalogueItem' instance.

        @param unitCost: Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        @param ErpQuoteLineItems:
        @param ErpPOLineItems:
        @param AssetModel:
        @param AssetModelCatalogue:
        """
        #: Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
        self.unitCost = unitCost

        self._ErpQuoteLineItems = []
        self.ErpQuoteLineItems = [] if ErpQuoteLineItems is None else ErpQuoteLineItems

        self._ErpPOLineItems = []
        self.ErpPOLineItems = [] if ErpPOLineItems is None else ErpPOLineItems

        self._AssetModel = None
        self.AssetModel = AssetModel

        self._AssetModelCatalogue = None
        self.AssetModelCatalogue = AssetModelCatalogue

        super(AssetModelCatalogueItem, self).__init__(**kw_args)

    def getErpQuoteLineItems(self):
        
        return self._ErpQuoteLineItems

    def setErpQuoteLineItems(self, value):
        for x in self._ErpQuoteLineItems:
            x._AssetModelCatalogueItem = None
        for y in value:
            y._AssetModelCatalogueItem = self
        self._ErpQuoteLineItems = value

    ErpQuoteLineItems = property(getErpQuoteLineItems, setErpQuoteLineItems)

    def addErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj._AssetModelCatalogueItem = self
            self._ErpQuoteLineItems.append(obj)

    def removeErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj._AssetModelCatalogueItem = None
            self._ErpQuoteLineItems.remove(obj)

    def getErpPOLineItems(self):
        
        return self._ErpPOLineItems

    def setErpPOLineItems(self, value):
        for x in self._ErpPOLineItems:
            x._AssetModelCatalogueItem = None
        for y in value:
            y._AssetModelCatalogueItem = self
        self._ErpPOLineItems = value

    ErpPOLineItems = property(getErpPOLineItems, setErpPOLineItems)

    def addErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj._AssetModelCatalogueItem = self
            self._ErpPOLineItems.append(obj)

    def removeErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj._AssetModelCatalogueItem = None
            self._ErpPOLineItems.remove(obj)

    def getAssetModel(self):
        
        return self._AssetModel

    def setAssetModel(self, value):
        if self._AssetModel is not None:
            filtered = [x for x in self.AssetModel.AssetModelCatalogueItems if x != self]
            self._AssetModel._AssetModelCatalogueItems = filtered

        self._AssetModel = value
        if self._AssetModel is not None:
            self._AssetModel._AssetModelCatalogueItems.append(self)

    AssetModel = property(getAssetModel, setAssetModel)

    def getAssetModelCatalogue(self):
        
        return self._AssetModelCatalogue

    def setAssetModelCatalogue(self, value):
        if self._AssetModelCatalogue is not None:
            filtered = [x for x in self.AssetModelCatalogue.AssetModelCatalogueItems if x != self]
            self._AssetModelCatalogue._AssetModelCatalogueItems = filtered

        self._AssetModelCatalogue = value
        if self._AssetModelCatalogue is not None:
            self._AssetModelCatalogue._AssetModelCatalogueItems.append(self)

    AssetModelCatalogue = property(getAssetModelCatalogue, setAssetModelCatalogue)

