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

class ErpPurchaseOrder(Document):
    """A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.A document that communicates an order to purchase goods from a buyer to a supplier. The PurchaseOrder carries information to and from the buyer and supplier. It is a legally binding document once both Parties agree to the contents and the specified terms and conditions of the order.
    """

    def __init__(self, ErpPOLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpPurchaseOrder' instance.

        @param ErpPOLineItems:
        """
        self._ErpPOLineItems = []
        self.ErpPOLineItems = [] if ErpPOLineItems is None else ErpPOLineItems

        super(ErpPurchaseOrder, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ErpPOLineItems"]
    _many_refs = ["ErpPOLineItems"]

    def getErpPOLineItems(self):
        
        return self._ErpPOLineItems

    def setErpPOLineItems(self, value):
        for x in self._ErpPOLineItems:
            x.ErpPurchaseOrder = None
        for y in value:
            y._ErpPurchaseOrder = self
        self._ErpPOLineItems = value

    ErpPOLineItems = property(getErpPOLineItems, setErpPOLineItems)

    def addErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj.ErpPurchaseOrder = self

    def removeErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj.ErpPurchaseOrder = None

