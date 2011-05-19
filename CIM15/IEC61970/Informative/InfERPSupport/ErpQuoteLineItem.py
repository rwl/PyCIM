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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ErpQuoteLineItem(IdentifiedObject):
    """Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.Of an ErpQuote, the item or product quoted along with quantity, price and other descriptive information.
    """

    def __init__(self, ErpQuote=None, AssetModelCatalogueItem=None, status=None, Design=None, ErpInvoiceLineItem=None, ErpReqLineItem=None, Request=None, *args, **kw_args):
        """Initialises a new 'ErpQuoteLineItem' instance.

        @param ErpQuote:
        @param AssetModelCatalogueItem:
        @param status:
        @param Design:
        @param ErpInvoiceLineItem: Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.
        @param ErpReqLineItem:
        @param Request:
        """
        self._ErpQuote = None
        self.ErpQuote = ErpQuote

        self._AssetModelCatalogueItem = None
        self.AssetModelCatalogueItem = AssetModelCatalogueItem

        self.status = status

        self._Design = None
        self.Design = Design

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self._ErpReqLineItem = None
        self.ErpReqLineItem = ErpReqLineItem

        self._Request = None
        self.Request = Request

        super(ErpQuoteLineItem, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpQuote", "AssetModelCatalogueItem", "status", "Design", "ErpInvoiceLineItem", "ErpReqLineItem", "Request"]
    _many_refs = []

    def getErpQuote(self):
        
        return self._ErpQuote

    def setErpQuote(self, value):
        if self._ErpQuote is not None:
            filtered = [x for x in self.ErpQuote.ErpQuoteLineItems if x != self]
            self._ErpQuote._ErpQuoteLineItems = filtered

        self._ErpQuote = value
        if self._ErpQuote is not None:
            if self not in self._ErpQuote._ErpQuoteLineItems:
                self._ErpQuote._ErpQuoteLineItems.append(self)

    ErpQuote = property(getErpQuote, setErpQuote)

    def getAssetModelCatalogueItem(self):
        
        return self._AssetModelCatalogueItem

    def setAssetModelCatalogueItem(self, value):
        if self._AssetModelCatalogueItem is not None:
            filtered = [x for x in self.AssetModelCatalogueItem.ErpQuoteLineItems if x != self]
            self._AssetModelCatalogueItem._ErpQuoteLineItems = filtered

        self._AssetModelCatalogueItem = value
        if self._AssetModelCatalogueItem is not None:
            if self not in self._AssetModelCatalogueItem._ErpQuoteLineItems:
                self._AssetModelCatalogueItem._ErpQuoteLineItems.append(self)

    AssetModelCatalogueItem = property(getAssetModelCatalogueItem, setAssetModelCatalogueItem)

    status = None

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            self._Design._ErpQuoteLineItem = None

        self._Design = value
        if self._Design is not None:
            self._Design.ErpQuoteLineItem = None
            self._Design._ErpQuoteLineItem = self

    Design = property(getDesign, setDesign)

    def getErpInvoiceLineItem(self):
        """Some utilities provide quotes to customer for services, where the customer accepts the quote by making a payment. An invoice is required for this to occur.
        """
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpQuoteLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem.ErpQuoteLineItem = None
            self._ErpInvoiceLineItem._ErpQuoteLineItem = self

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    def getErpReqLineItem(self):
        
        return self._ErpReqLineItem

    def setErpReqLineItem(self, value):
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem._ErpQuoteLineItem = None

        self._ErpReqLineItem = value
        if self._ErpReqLineItem is not None:
            self._ErpReqLineItem.ErpQuoteLineItem = None
            self._ErpReqLineItem._ErpQuoteLineItem = self

    ErpReqLineItem = property(getErpReqLineItem, setErpReqLineItem)

    def getRequest(self):
        
        return self._Request

    def setRequest(self, value):
        if self._Request is not None:
            self._Request._ErpQuoteLineItem = None

        self._Request = value
        if self._Request is not None:
            self._Request.ErpQuoteLineItem = None
            self._Request._ErpQuoteLineItem = self

    Request = property(getRequest, setRequest)

