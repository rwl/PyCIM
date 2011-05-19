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

class ErpInvoice(Document):
    """A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.A roll up of invoice line items. The whole invoice has a due date and amount to be paid, with information such as customer, banks etc. being obtained through associations. The invoice roll up is based on individual line items that each contain amounts and descriptions for specific services or products.
    """

    def __init__(self, mailedDate='', transactionDateTime='', amount=0.0, dueDate='', billMediaKind="other", referenceNumber='', kind="sales", transferType='', proForma=False, ErpInvoiceLineItems=None, CustomerAccount=None, *args, **kw_args):
        """Initialises a new 'ErpInvoice' instance.

        @param mailedDate: Date on which the customer billing statement/invoice was printed/mailed. 
        @param transactionDateTime: Date and time when the invoice is issued. 
        @param amount: Total amount due on this invoice based on line items and applicable adjustments. 
        @param dueDate: Calculated date upon which the Invoice amount is due. 
        @param billMediaKind: Kind of media by which the CustomerBillingInfo was delivered. Values are: "other", "paper", "electronic"
        @param referenceNumber: Number of an invoice to be reference by this invoice. 
        @param kind: Kind of invoice (default is 'sales'). Values are: "sales", "purchase"
        @param transferType: Type of invoice transfer. 
        @param proForma: True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote. 
        @param ErpInvoiceLineItems:
        @param CustomerAccount:
        """
        #: Date on which the customer billing statement/invoice was printed/mailed.
        self.mailedDate = mailedDate

        #: Date and time when the invoice is issued.
        self.transactionDateTime = transactionDateTime

        #: Total amount due on this invoice based on line items and applicable adjustments.
        self.amount = amount

        #: Calculated date upon which the Invoice amount is due.
        self.dueDate = dueDate

        #: Kind of media by which the CustomerBillingInfo was delivered. Values are: "other", "paper", "electronic"
        self.billMediaKind = billMediaKind

        #: Number of an invoice to be reference by this invoice.
        self.referenceNumber = referenceNumber

        #: Kind of invoice (default is 'sales'). Values are: "sales", "purchase"
        self.kind = kind

        #: Type of invoice transfer.
        self.transferType = transferType

        #: True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote.
        self.proForma = proForma

        self._ErpInvoiceLineItems = []
        self.ErpInvoiceLineItems = [] if ErpInvoiceLineItems is None else ErpInvoiceLineItems

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        super(ErpInvoice, self).__init__(*args, **kw_args)

    _attrs = ["mailedDate", "transactionDateTime", "amount", "dueDate", "billMediaKind", "referenceNumber", "kind", "transferType", "proForma"]
    _attr_types = {"mailedDate": str, "transactionDateTime": str, "amount": float, "dueDate": str, "billMediaKind": str, "referenceNumber": str, "kind": str, "transferType": str, "proForma": bool}
    _defaults = {"mailedDate": '', "transactionDateTime": '', "amount": 0.0, "dueDate": '', "billMediaKind": "other", "referenceNumber": '', "kind": "sales", "transferType": '', "proForma": False}
    _enums = {"billMediaKind": "BillMediaKind", "kind": "ErpInvoiceKind"}
    _refs = ["ErpInvoiceLineItems", "CustomerAccount"]
    _many_refs = ["ErpInvoiceLineItems"]

    def getErpInvoiceLineItems(self):
        
        return self._ErpInvoiceLineItems

    def setErpInvoiceLineItems(self, value):
        for x in self._ErpInvoiceLineItems:
            x.ErpInvoice = None
        for y in value:
            y._ErpInvoice = self
        self._ErpInvoiceLineItems = value

    ErpInvoiceLineItems = property(getErpInvoiceLineItems, setErpInvoiceLineItems)

    def addErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            obj.ErpInvoice = self

    def removeErpInvoiceLineItems(self, *ErpInvoiceLineItems):
        for obj in ErpInvoiceLineItems:
            obj.ErpInvoice = None

    def getCustomerAccount(self):
        
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.ErpInvoicees if x != self]
            self._CustomerAccount._ErpInvoicees = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            if self not in self._CustomerAccount._ErpInvoicees:
                self._CustomerAccount._ErpInvoicees.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

