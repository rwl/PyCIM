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

from CIM15.IEC61968.Common.Document import Document

class AssetModelCatalogueItem(Document):
    """Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """

    def __init__(self, unitCost=0.0, ErpPOLineItems=None, AssetModelCatalogue=None, AssetModel=None, ErpQuoteLineItems=None, *args, **kw_args):
        """Initialises a new 'AssetModelCatalogueItem' instance.

        @param unitCost: Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        @param ErpPOLineItems:
        @param AssetModelCatalogue:
        @param AssetModel:
        @param ErpQuoteLineItems:
        """
        #: Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
        self.unitCost = unitCost

        self._ErpPOLineItems = []
        self.ErpPOLineItems = [] if ErpPOLineItems is None else ErpPOLineItems

        self._AssetModelCatalogue = None
        self.AssetModelCatalogue = AssetModelCatalogue

        self._AssetModel = None
        self.AssetModel = AssetModel

        self._ErpQuoteLineItems = []
        self.ErpQuoteLineItems = [] if ErpQuoteLineItems is None else ErpQuoteLineItems

        super(AssetModelCatalogueItem, self).__init__(*args, **kw_args)

    _attrs = ["unitCost"]
    _attr_types = {"unitCost": float}
    _defaults = {"unitCost": 0.0}
    _enums = {}
    _refs = ["ErpPOLineItems", "AssetModelCatalogue", "AssetModel", "ErpQuoteLineItems"]
    _many_refs = ["ErpPOLineItems", "ErpQuoteLineItems"]

    def getErpPOLineItems(self):
        
        return self._ErpPOLineItems

    def setErpPOLineItems(self, value):
        for x in self._ErpPOLineItems:
            x.AssetModelCatalogueItem = None
        for y in value:
            y._AssetModelCatalogueItem = self
        self._ErpPOLineItems = value

    ErpPOLineItems = property(getErpPOLineItems, setErpPOLineItems)

    def addErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj.AssetModelCatalogueItem = self

    def removeErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj.AssetModelCatalogueItem = None

    def getAssetModelCatalogue(self):
        
        return self._AssetModelCatalogue

    def setAssetModelCatalogue(self, value):
        if self._AssetModelCatalogue is not None:
            filtered = [x for x in self.AssetModelCatalogue.AssetModelCatalogueItems if x != self]
            self._AssetModelCatalogue._AssetModelCatalogueItems = filtered

        self._AssetModelCatalogue = value
        if self._AssetModelCatalogue is not None:
            if self not in self._AssetModelCatalogue._AssetModelCatalogueItems:
                self._AssetModelCatalogue._AssetModelCatalogueItems.append(self)

    AssetModelCatalogue = property(getAssetModelCatalogue, setAssetModelCatalogue)

    def getAssetModel(self):
        
        return self._AssetModel

    def setAssetModel(self, value):
        if self._AssetModel is not None:
            filtered = [x for x in self.AssetModel.AssetModelCatalogueItems if x != self]
            self._AssetModel._AssetModelCatalogueItems = filtered

        self._AssetModel = value
        if self._AssetModel is not None:
            if self not in self._AssetModel._AssetModelCatalogueItems:
                self._AssetModel._AssetModelCatalogueItems.append(self)

    AssetModel = property(getAssetModel, setAssetModel)

    def getErpQuoteLineItems(self):
        
        return self._ErpQuoteLineItems

    def setErpQuoteLineItems(self, value):
        for x in self._ErpQuoteLineItems:
            x.AssetModelCatalogueItem = None
        for y in value:
            y._AssetModelCatalogueItem = self
        self._ErpQuoteLineItems = value

    ErpQuoteLineItems = property(getErpQuoteLineItems, setErpQuoteLineItems)

    def addErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj.AssetModelCatalogueItem = self

    def removeErpQuoteLineItems(self, *ErpQuoteLineItems):
        for obj in ErpQuoteLineItems:
            obj.AssetModelCatalogueItem = None

