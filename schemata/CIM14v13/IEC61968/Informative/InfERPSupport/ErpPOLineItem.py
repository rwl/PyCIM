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

class ErpPOLineItem(Document):
    """Of an ErpPurchaseOrder, this is an individually ordered item or product along with the quantity, price and other descriptive information.
    """

    def __init__(self, ErpReqLineItem=None, ErpRecDelLineItem=None, AssetModelCatalogueItem=None, ErpPurchaseOrder=None, MaterialItem=None, *args, **kw_args):
        """Initializes a new 'ErpPOLineItem' instance.

        @param ErpReqLineItem:
        @param ErpRecDelLineItem:
        @param AssetModelCatalogueItem:
        @param ErpPurchaseOrder:
        @param MaterialItem:
        """
        self._ErpReqLineItem = None
        self.ErpReqLineItem = ErpReqLineItem

        self._ErpRecDelLineItem = None
        self.ErpRecDelLineItem = ErpRecDelLineItem

        self._AssetModelCatalogueItem = None
        self.AssetModelCatalogueItem = AssetModelCatalogueItem

        self._ErpPurchaseOrder = None
        self.ErpPurchaseOrder = ErpPurchaseOrder

        self._MaterialItem = None
        self.MaterialItem = MaterialItem

        super(ErpPOLineItem, self).__init__(*args, **kw_args)

    def getErpReqLineItem(self):
        
        return self._ErpReqLineItem

    def setErpReqLineItem(self, value):
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem._ErpPOLineItem = None

        self._ErpReqLineItem = value
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem._ErpPOLineItem = self

    ErpReqLineItem = property(getErpReqLineItem, setErpReqLineItem)

    def getErpRecDelLineItem(self):
        
        return self._ErpRecDelLineItem

    def setErpRecDelLineItem(self, value):
        if self._ErpRecDelLineItem is not None:
            self._ErpRecDelLineItem._ErpPOLineItem = None

        self._ErpRecDelLineItem = value
        if self._ErpRecDelLineItem is not None:
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
            self._AssetModelCatalogueItem._ErpPOLineItems.append(self)

    AssetModelCatalogueItem = property(getAssetModelCatalogueItem, setAssetModelCatalogueItem)

    def getErpPurchaseOrder(self):
        
        return self._ErpPurchaseOrder

    def setErpPurchaseOrder(self, value):
        if self._ErpPurchaseOrder is not None:
            filtered = [x for x in self.ErpPurchaseOrder.ErpPOLineItems if x != self]
            self._ErpPurchaseOrder._ErpPOLineItems = filtered

        self._ErpPurchaseOrder = value
        if self._ErpPurchaseOrder is not None:
            self._ErpPurchaseOrder._ErpPOLineItems.append(self)

    ErpPurchaseOrder = property(getErpPurchaseOrder, setErpPurchaseOrder)

    def getMaterialItem(self):
        
        return self._MaterialItem

    def setMaterialItem(self, value):
        if self._MaterialItem is not None:
            filtered = [x for x in self.MaterialItem.ErpPOLineItems if x != self]
            self._MaterialItem._ErpPOLineItems = filtered

        self._MaterialItem = value
        if self._MaterialItem is not None:
            self._MaterialItem._ErpPOLineItems.append(self)

    MaterialItem = property(getMaterialItem, setMaterialItem)

