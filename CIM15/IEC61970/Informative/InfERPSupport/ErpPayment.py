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

class ErpPayment(Document):
    """Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.
    """

    def __init__(self, termsPayment='', ErpRecLineItems=None, ErpPayableLineItems=None, ErpInvoiceLineItems=None, *args, **kw_args):
        """Initialises a new 'ErpPayment' instance.

        @param termsPayment: Payment terms (e.g., net 30). 
        @param ErpRecLineItems:
        @param ErpPayableLineItems:
        @param ErpInvoiceLineItems:
        """
        #: Payment terms (e.g., net 30).
        self.termsPayment = termsPayment

        self._ErpRecLineItems = []
        self.ErpRecLineItems = [] if ErpRecLineItems is None else ErpRecLineItems

        self._ErpPayableLineItems = []
        self.ErpPayableLineItems = [] if ErpPayableLineItems is None else ErpPayableLineItems

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        super(ErpPayment, self).__init__(*args, **kw_args)

    _attrs = ["termsPayment"]
    _attr_types = {"termsPayment": str}
    _defaults = {"termsPayment": ''}
    _enums = {}
    _refs = ["ErpRecLineItems", "ErpPayableLineItems", "ErpInvoiceLineItems"]
    _many_refs = ["ErpRecLineItems", "ErpPayableLineItems", "ErpInvoiceLineItems"]

    def getErpRecLineItems(self):
        
        return self._ErpRecLineItems

    def setErpRecLineItems(self, value):
        for p in self._ErpRecLineItems:
            filtered = [q for q in p.ErpPayments if q != self]
            self._ErpRecLineItems._ErpPayments = filtered
        for r in value:
            if self not in r._ErpPayments:
                r._ErpPayments.append(self)
        self._ErpRecLineItems = value

    ErpRecLineItems = property(getErpRecLineItems, setErpRecLineItems)

    def addErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            if self not in obj._ErpPayments:
                obj._ErpPayments.append(self)
            self._ErpRecLineItems.append(obj)

    def removeErpRecLineItems(self, *ErpRecLineItems):
        for obj in ErpRecLineItems:
            if self in obj._ErpPayments:
                obj._ErpPayments.remove(self)
            self._ErpRecLineItems.remove(obj)

    def getErpPayableLineItems(self):
        
        return self._ErpPayableLineItems

    def setErpPayableLineItems(self, value):
        for p in self._ErpPayableLineItems:
            filtered = [q for q in p.ErpPayments if q != self]
            self._ErpPayableLineItems._ErpPayments = filtered
        for r in value:
            if self not in r._ErpPayments:
                r._ErpPayments.append(self)
        self._ErpPayableLineItems = value

    ErpPayableLineItems = property(getErpPayableLineItems, setErpPayableLineItems)

    def addErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            if self not in obj._ErpPayments:
                obj._ErpPayments.append(self)
            self._ErpPayableLineItems.append(obj)

    def removeErpPayableLineItems(self, *ErpPayableLineItems):
        for obj in ErpPayableLineItems:
            if self in obj._ErpPayments:
                obj._ErpPayments.remove(self)
            self._ErpPayableLineItems.remove(obj)

    def getErpInvoiceLineItems(self):
        
        return self._ErpInvoiceLineItems

    def setErpInvoiceLineItems(self, value):
        for p in self._ErpInvoiceLineItems:
            filtered = [q for q in p.ErpPayments if q != self]
            self._ErpInvoiceLineItems._ErpPayments = filtered
        for r in value:
            if self not in r._ErpPayments:
                r._ErpPayments.append(self)
        self._ErpInvoiceLineItems = value

    ErpInvoiceLineItems = property(getErpInvoiceLineItems, setErpInvoiceLineItems)

    def addErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self not in obj._ErpPayments:
                obj._ErpPayments.append(self)
            self._ErpInvoiceLineItems.append(obj)

    def removeErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            if self in obj._ErpPayments:
                obj._ErpPayments.remove(self)
            self._ErpInvoiceLineItems.remove(obj)

