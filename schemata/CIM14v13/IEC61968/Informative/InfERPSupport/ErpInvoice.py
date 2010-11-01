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

class ErpInvoice(Document):
    """A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.
    """

    def __init__(self, billMediaKind='other', kind='sales', amount=0.0, proForma=False, transactionDateTime='', mailedDate='', dueDate='', transferType='', referenceNumber='', CustomerAccount=None, ErpInvoiceLineItems=None, *args, **kw_args):
        """Initializes a new 'ErpInvoice' instance.

        @param billMediaKind: Kind of media by which the CustomerBillingInfo was delivered. Values are: "other", "paper", "electronic"
        @param kind: Kind of invoice (default is 'sales'). Values are: "sales", "purchase"
        @param amount: Total amount due on this invoice based on line items and applicable adjustments. 
        @param proForma: True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote. 
        @param transactionDateTime: Date and time when the invoice is issued. 
        @param mailedDate: Date on which the customer billing statement/invoice was printed/mailed. 
        @param dueDate: Calculated date upon which the Invoice amount is due. 
        @param transferType: Type of invoice transfer. 
        @param referenceNumber: Number of an invoice to be reference by this invoice. 
        @param CustomerAccount:
        @param ErpInvoiceLineItems:
        """
        #: Kind of media by which the CustomerBillingInfo was delivered. Values are: "other", "paper", "electronic"
        self.billMediaKind = billMediaKind

        #: Kind of invoice (default is 'sales'). Values are: "sales", "purchase"
        self.kind = kind

        #: Total amount due on this invoice based on line items and applicable adjustments. 
        self.amount = amount

        #: True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote. 
        self.proForma = proForma

        #: Date and time when the invoice is issued. 
        self.transactionDateTime = transactionDateTime

        #: Date on which the customer billing statement/invoice was printed/mailed. 
        self.mailedDate = mailedDate

        #: Calculated date upon which the Invoice amount is due. 
        self.dueDate = dueDate

        #: Type of invoice transfer. 
        self.transferType = transferType

        #: Number of an invoice to be reference by this invoice. 
        self.referenceNumber = referenceNumber

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        super(ErpInvoice, self).__init__(*args, **kw_args)

    def getCustomerAccount(self):
        
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.ErpInvoicees if x != self]
            self._CustomerAccount._ErpInvoicees = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            self._CustomerAccount._ErpInvoicees.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

    def getErpInvoiceLineItems(self):
        
        return self._ErpInvoiceLineItems

    def setErpInvoiceLineItems(self, value):
        for x in self._ErpInvoiceLineItems:
            x._ErpInvoice = None
        for y in value:
            y._ErpInvoice = self
        self._ErpInvoiceLineItems = value

    ErpInvoiceLineItems = property(getErpInvoiceLineItems, setErpInvoiceLineItems)

    def addErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            obj._ErpInvoice = self
            self._ErpInvoiceLineItems.append(obj)

    def removeErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            obj._ErpInvoice = None
            self._ErpInvoiceLineItems.remove(obj)

