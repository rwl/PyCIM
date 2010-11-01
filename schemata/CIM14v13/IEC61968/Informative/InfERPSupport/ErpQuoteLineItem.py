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

class ErpQuoteLineItem(IdentifiedObject):
    """Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.
    """

    def __init__(self, AssetModelCatalogueItem=None, Design=None, Request=None, ErpReqLineItem=None, ErpInvoiceLineItem=None, status=None, ErpQuote=None, *args, **kw_args):
        """Initializes a new 'ErpQuoteLineItem' instance.

        @param AssetModelCatalogueItem:
        @param Design:
        @param Request:
        @param ErpReqLineItem:
        @param ErpInvoiceLineItem: Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.
        @param status:
        @param ErpQuote:
        """
        self._AssetModelCatalogueItem = None
        self.AssetModelCatalogueItem = AssetModelCatalogueItem

        self._Design = None
        self.Design = Design

        self._Request = None
        self.Request = Request

        self._ErpReqLineItem = None
        self.ErpReqLineItem = ErpReqLineItem

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self.status = status

        self._ErpQuote = None
        self.ErpQuote = ErpQuote

        super(ErpQuoteLineItem, self).__init__(*args, **kw_args)

    def getAssetModelCatalogueItem(self):
        
        return self._AssetModelCatalogueItem

    def setAssetModelCatalogueItem(self, value):
        if self._AssetModelCatalogueItem is not None:
            filtered = [x for x in self.AssetModelCatalogueItem.ErpQuoteLineItems if x != self]
            self._AssetModelCatalogueItem._ErpQuoteLineItems = filtered

        self._AssetModelCatalogueItem = value
        if self._AssetModelCatalogueItem is not None:
            self._AssetModelCatalogueItem._ErpQuoteLineItems.append(self)

    AssetModelCatalogueItem = property(getAssetModelCatalogueItem, setAssetModelCatalogueItem)

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            self._Design._ErpQuoteLineItem = None

        self._Design = value
        if self._Design is not None:
            self._Design._ErpQuoteLineItem = self

    Design = property(getDesign, setDesign)

    def getRequest(self):
        
        return self._Request

    def setRequest(self, value):
        if self._Request is not None:
            self._Request._ErpQuoteLineItem = None

        self._Request = value
        if self._Request is not None:
            self._Request._ErpQuoteLineItem = self

    Request = property(getRequest, setRequest)

    def getErpReqLineItem(self):
        
        return self._ErpReqLineItem

    def setErpReqLineItem(self, value):
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem._ErpQuoteLineItem = None

        self._ErpReqLineItem = value
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem._ErpQuoteLineItem = self

    ErpReqLineItem = property(getErpReqLineItem, setErpReqLineItem)

    def getErpInvoiceLineItem(self):
        """Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.
        """
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpQuoteLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpQuoteLineItem = self

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    status = None

    def getErpQuote(self):
        
        return self._ErpQuote

    def setErpQuote(self, value):
        if self._ErpQuote is not None:
            filtered = [x for x in self.ErpQuote.ErpQuoteLineItems if x != self]
            self._ErpQuote._ErpQuoteLineItems = filtered

        self._ErpQuote = value
        if self._ErpQuote is not None:
            self._ErpQuote._ErpQuoteLineItems.append(self)

    ErpQuote = property(getErpQuote, setErpQuote)

