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

class ErpPOLineItem(Document):
    """Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.
    """

    def __init__(self, ErpPurchaseOrder=None, ErpRecDelLineItem=None, AssetModelCatalogueItem=None, MaterialItem=None, ErpReqLineItem=None, *args, **kw_args):
        """Initialises a new 'ErpPOLineItem' instance.

        @param ErpPurchaseOrder:
        @param ErpRecDelLineItem:
        @param AssetModelCatalogueItem:
        @param MaterialItem:
        @param ErpReqLineItem:
        """
        self._ErpPurchaseOrder = None
        self.ErpPurchaseOrder = ErpPurchaseOrder

        self._ErpRecDelLineItem = None
        self.ErpRecDelLineItem = ErpRecDelLineItem

        self._AssetModelCatalogueItem = None
        self.AssetModelCatalogueItem = AssetModelCatalogueItem

        self._MaterialItem = None
        self.MaterialItem = MaterialItem

        self._ErpReqLineItem = None
        self.ErpReqLineItem = ErpReqLineItem

        super(ErpPOLineItem, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpPurchaseOrder", "ErpRecDelLineItem", "AssetModelCatalogueItem", "MaterialItem", "ErpReqLineItem"]
    _many_refs = []

    def getErpPurchaseOrder(self):
        
        return self._ErpPurchaseOrder

    def setErpPurchaseOrder(self, value):
        if self._ErpPurchaseOrder is not None:
            filtered = [x for x in self.ErpPurchaseOrder.ErpPOLineItems if x != self]
            self._ErpPurchaseOrder._ErpPOLineItems = filtered

        self._ErpPurchaseOrder = value
        if self._ErpPurchaseOrder is not None:
            if self not in self._ErpPurchaseOrder._ErpPOLineItems:
                self._ErpPurchaseOrder._ErpPOLineItems.append(self)

    ErpPurchaseOrder = property(getErpPurchaseOrder, setErpPurchaseOrder)

    def getErpRecDelLineItem(self):
        
        return self._ErpRecDelLineItem

    def setErpRecDelLineItem(self, value):
        if self._ErpRecDelLineItem is not None:
            self._ErpRecDelLineItem._ErpPOLineItem = None

        self._ErpRecDelLineItem = value
        if self._ErpRecDelLineItem is not None:
            self._ErpRecDelLineItem.ErpPOLineItem = None
            self._ErpRecDelLineItem._ErpPOLineItem = self

    ErpRecDelLineItem = property(getErpRecDelLineItem, setErpRecDelLineItem)

    def getAssetModelCatalogueItem(self):
        
        return self._AssetModelCatalogueItem

    def setAssetModelCatalogueItem(self, value):
        if self._AssetModelCatalogueItem is not None:
            filtered = [x for x in self.AssetModelCatalogueItem.ErpPOLineItems if x != self]
            self._AssetModelCatalogueItem._ErpPOLineItems = filtered

        self._AssetModelCatalogueItem = value
        if self._AssetModelCatalogueItem is not None:
            if self not in self._AssetModelCatalogueItem._ErpPOLineItems:
                self._AssetModelCatalogueItem._ErpPOLineItems.append(self)

    AssetModelCatalogueItem = property(getAssetModelCatalogueItem, setAssetModelCatalogueItem)

    def getMaterialItem(self):
        
        return self._MaterialItem

    def setMaterialItem(self, value):
        if self._MaterialItem is not None:
            filtered = [x for x in self.MaterialItem.ErpPOLineItems if x != self]
            self._MaterialItem._ErpPOLineItems = filtered

        self._MaterialItem = value
        if self._MaterialItem is not None:
            if self not in self._MaterialItem._ErpPOLineItems:
                self._MaterialItem._ErpPOLineItems.append(self)

    MaterialItem = property(getMaterialItem, setMaterialItem)

    def getErpReqLineItem(self):
        
        return self._ErpReqLineItem

    def setErpReqLineItem(self, value):
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem._ErpPOLineItem = None

        self._ErpReqLineItem = value
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem.ErpPOLineItem = None
            self._ErpReqLineItem._ErpPOLineItem = self

    ErpReqLineItem = property(getErpReqLineItem, setErpReqLineItem)

