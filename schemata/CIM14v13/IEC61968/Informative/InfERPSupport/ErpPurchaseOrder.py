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

class ErpPurchaseOrder(Document):
    """A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.
    """

    def __init__(self, ErpPOLineItems=None, *args, **kw_args):
        """Initializes a new 'ErpPurchaseOrder' instance.

        @param ErpPOLineItems:
        """
        self._ErpPOLineItems = []
        self.ErpPOLineItems = [] if ErpPOLineItems is None else ErpPOLineItems

        super(ErpPurchaseOrder, self).__init__(*args, **kw_args)

    def getErpPOLineItems(self):
        
        return self._ErpPOLineItems

    def setErpPOLineItems(self, value):
        for x in self._ErpPOLineItems:
            x._ErpPurchaseOrder = None
        for y in value:
            y._ErpPurchaseOrder = self
        self._ErpPOLineItems = value

    ErpPOLineItems = property(getErpPOLineItems, setErpPOLineItems)

    def addErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj._ErpPurchaseOrder = self
            self._ErpPOLineItems.append(obj)

    def removeErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj._ErpPurchaseOrder = None
            self._ErpPOLineItems.remove(obj)

