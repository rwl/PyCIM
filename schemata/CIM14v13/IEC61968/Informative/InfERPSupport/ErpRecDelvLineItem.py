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

class ErpRecDelvLineItem(IdentifiedObject):
    """Of an ErpReceiveDelivery, this is an individually received good or service by the Organisation receiving goods or services. It may be used to indicate receipt of goods in conjunction with a purchase order line item.
    """

    def __init__(self, status=None, ErpPOLineItem=None, ErpReceiveDelivery=None, MaterialItems=None, ErpInvoiceLineItem=None, Assets=None, *args, **kw_args):
        """Initializes a new 'ErpRecDelvLineItem' instance.

        @param status:
        @param ErpPOLineItem:
        @param ErpReceiveDelivery:
        @param MaterialItems:
        @param ErpInvoiceLineItem:
        @param Assets:
        """
        self.status = status

        self._ErpPOLineItem = None
        self.ErpPOLineItem = ErpPOLineItem

        self._ErpReceiveDelivery = None
        self.ErpReceiveDelivery = ErpReceiveDelivery

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._ErpInvoiceLineItem = None
        self.ErpInvoiceLineItem = ErpInvoiceLineItem

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(ErpRecDelvLineItem, self).__init__(*args, **kw_args)

    status = None

    def getErpPOLineItem(self):
        
        return self._ErpPOLineItem

    def setErpPOLineItem(self, value):
        if self._ErpPOLineItem is not None:
            self._ErpPOLineItem._ErpRecDelLineItem = None

        self._ErpPOLineItem = value
        if self._ErpPOLineItem is not None:
            self._ErpPOLineItem._ErpRecDelLineItem = self

    ErpPOLineItem = property(getErpPOLineItem, setErpPOLineItem)

    def getErpReceiveDelivery(self):
        
        return self._ErpReceiveDelivery

    def setErpReceiveDelivery(self, value):
        if self._ErpReceiveDelivery is not None:
            filtered = [x for x in self.ErpReceiveDelivery.ErpRecDelvLineItems if x != self]
            self._ErpReceiveDelivery._ErpRecDelvLineItems = filtered

        self._ErpReceiveDelivery = value
        if self._ErpReceiveDelivery is not None:
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

    def getErpInvoiceLineItem(self):
        
        return self._ErpInvoiceLineItem

    def setErpInvoiceLineItem(self, value):
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpRecDelvLineItem = None

        self._ErpInvoiceLineItem = value
        if self._ErpInvoiceLineItem is not None:
            self._ErpInvoiceLineItem._ErpRecDelvLineItem = self

    ErpInvoiceLineItem = property(getErpInvoiceLineItem, setErpInvoiceLineItem)

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

