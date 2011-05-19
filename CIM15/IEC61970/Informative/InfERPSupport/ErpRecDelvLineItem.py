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

class ErpRecDelvLineItem(IdentifiedObject):
    """Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.
    """

    def __init__(self, Assets=None, ErpInvoiceLineItem=None, status=None, ErpReceiveDelivery=None, MaterialItems=None, ErpPOLineItem=None, *args, **kw_args):
        """Initialises a new 'ErpRecDelvLineItem' instance.

        @param Assets:
        @param ErpInvoiceLineItem:
        @param status:
        @param ErpReceiveDelivery:
        @param MaterialItems:
        @param ErpPOLineItem:
        """
        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self.status = status

        self._ErpReceiveDelivery = None
        self.ErpReceiveDelivery = ErpReceiveDelivery

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._ErpPOLineItem = None
        self.ErpPOLineItem = ErpPOLineItem

        super(ErpRecDelvLineItem, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Assets", "ErpInvoiceLineItem", "status", "ErpReceiveDelivery", "MaterialItems", "ErpPOLineItem"]
    _many_refs = ["Assets", "MaterialItems"]

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.ErpRecDeliveryItems if q != self]
            self._Assets._ErpRecDeliveryItems = filtered
        for r in value:
            if self not in r._ErpRecDeliveryItems:
                r._ErpRecDeliveryItems.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._ErpRecDeliveryItems:
                obj._ErpRecDeliveryItems.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._ErpRecDeliveryItems:
                obj._ErpRecDeliveryItems.remove(self)
            self._Assets.remove(obj)

    def getErpInvoiceLineItem(self):
        
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpRecDelvLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem.ErpRecDelvLineItem = None
            self._ErpInvoiceLineItem._ErpRecDelvLineItem = self

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

    status = None

    def getErpReceiveDelivery(self):
        
        return self._ErpReceiveDelivery

    def setErpReceiveDelivery(self, value):
        if self._ErpReceiveDelivery is not None:
            filtered = [x for x in self.ErpReceiveDelivery.ErpRecDelvLineItems if x != self]
            self._ErpReceiveDelivery._ErpRecDelvLineItems = filtered

        self._ErpReceiveDelivery = value
        if self._ErpReceiveDelivery is not None:
            if self not in self._ErpReceiveDelivery._ErpRecDelvLineItems:
                self._ErpReceiveDelivery._ErpRecDelvLineItems.append(self)

    ErpReceiveDelivery = property(getErpReceiveDelivery, setErpReceiveDelivery)

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for p in self._MaterialItems:
            filtered = [q for q in p.ErpRecDelvLineItems if q != self]
            self._MaterialItems._ErpRecDelvLineItems = filtered
        for r in value:
            if self not in r._ErpRecDelvLineItems:
                r._ErpRecDelvLineItems.append(self)
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            if self not in obj._ErpRecDelvLineItems:
                obj._ErpRecDelvLineItems.append(self)
            self._MaterialItems.append(obj)

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            if self in obj._ErpRecDelvLineItems:
                obj._ErpRecDelvLineItems.remove(self)
            self._MaterialItems.remove(obj)

    def getErpPOLineItem(self):
        
        return self._ErpPOLineItem

    def setErpPOLineItem(self, value):
        if self._ErpPOLineItem is not None:
            self._ErpPOLineItem._ErpRecDelLineItem = None

        self._ErpPOLineItem = value
        if self._ErpPOLineItem is not None:
            self._ErpPOLineItem.ErpRecDelLineItem = None
            self._ErpPOLineItem._ErpRecDelLineItem = self

    ErpPOLineItem = property(getErpPOLineItem, setErpPOLineItem)

