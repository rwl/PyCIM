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

class ErpPayment(Document):
    """Payment infromation and status for any individual line item of an ErpInvoice (e.g., when payment is from a customer). ErpPayable is also updated when payment is to a supplier and ErpReceivable is updated when payment is from a customer. Multiple payments can be made against a single line item and an individual payment can apply to more that one line item.
    """

    def __init__(self, termsPayment='', ErpRecLineItems=None, ErpInvoiceLineItems=None, ErpPayableLineItems=None, **kw_args):
        """Initializes a new 'ErpPayment' instance.

        @param termsPayment: Payment terms (e.g., net 30). 
        @param ErpRecLineItems:
        @param ErpInvoiceLineItems:
        @param ErpPayableLineItems:
        """
        #: Payment terms (e.g., net 30).
        self.termsPayment = termsPayment

        self._ErpRecLineItems = []
        self.ErpRecLineItems = [] if ErpRecLineItems is None else ErpRecLineItems

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        self._ErpPayableLineItems = []
        self.ErpPayableLineItems = [] if ErpPayableLineItems is None else ErpPayableLineItems

        super(ErpPayment, self).__init__(**kw_args)

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

