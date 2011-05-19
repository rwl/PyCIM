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

class ErpInvoiceLineItem(Document):
    """An individual line item on an invoice.An individual line item on an invoice.
    """

    def __init__(self, lineNumber='', glDateTime='', lineAmount=0.0, netAmount=0.0, kind="other", lineVersion='', glAccount='', previousAmount=0.0, ErpPayments=None, ContainerErpInvoiceLineItem=None, WorkBillingInfos=None, ErpQuoteLineItem=None, UserAttributes=None, ErpRecDelvLineItem=None, ErpPayableLineItem=None, ComponentErpInvoiceLineItems=None, billPeriod=None, ErpInvoice=None, CustomerBillingInfos=None, ErpRecLineItem=None, ErpJournalEntries=None, *args, **kw_args):
        """Initialises a new 'ErpInvoiceLineItem' instance.

        @param lineNumber: Line item number on invoice statement. 
        @param glDateTime: Date and time line item will be posted to the General Ledger. 
        @param lineAmount: Amount due for this line item. 
        @param netAmount: Net line item charge amount. 
        @param kind: Kind of line item. Values are: "other", "recalculation", "initial"
        @param lineVersion: Version number of the bill run. 
        @param glAccount: General Ledger account code, must be a valid combination. 
        @param previousAmount: Previous line item charge amount. 
        @param ErpPayments:
        @param ContainerErpInvoiceLineItem:
        @param WorkBillingInfos:
        @param ErpQuoteLineItem:
        @param UserAttributes:
        @param ErpRecDelvLineItem:
        @param ErpPayableLineItem:
        @param ComponentErpInvoiceLineItems:
        @param billPeriod: Bill period for the line item.
        @param ErpInvoice:
        @param CustomerBillingInfos: Customer billing for services rendered.
        @param ErpRecLineItem:
        @param ErpJournalEntries:
        """
        #: Line item number on invoice statement.
        self.lineNumber = lineNumber

        #: Date and time line item will be posted to the General Ledger.
        self.glDateTime = glDateTime

        #: Amount due for this line item.
        self.lineAmount = lineAmount

        #: Net line item charge amount.
        self.netAmount = netAmount

        #: Kind of line item. Values are: "other", "recalculation", "initial"
        self.kind = kind

        #: Version number of the bill run.
        self.lineVersion = lineVersion

        #: General Ledger account code, must be a valid combination.
        self.glAccount = glAccount

        #: Previous line item charge amount.
        self.previousAmount = previousAmount

        self._ErpPayments = []
        self.ErpPayments = [] if ErpPayments is None else ErpPayments

        self._ContainerErpInvoiceLineItem = None
        self.ContainerErpInvoiceLineItem = ContainerErpInvoiceLineItem

        self._WorkBillingInfos = []
        self.WorkBillingInfos = [] if WorkBillingInfos is None else WorkBillingInfos

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        self._ErpRecDelvLineItem = None
        self.ErpRecDelvLineItem = ErpRecDelvLineItem

        self._ErpPayableLineItem = None
        self.ErpPayableLineItem = ErpPayableLineItem

        self._ComponentErpInvoiceLineItems = []
        self.ComponentErpInvoiceLineItems = [] if ComponentErpInvoiceLineItems is None else ComponentErpInvoiceLineItems

        self.billPeriod = billPeriod

        self._ErpInvoice = None
        self.ErpInvoice = ErpInvoice

        self._CustomerBillingInfos = []
        self.CustomerBillingInfos = [] if CustomerBillingInfos is None else CustomerBillingInfos

        self._ErpRecLineItem = None
        self.ErpRecLineItem = ErpRecLineItem

        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        super(ErpInvoiceLineItem, self).__init__(*args, **kw_args)

    _attrs = ["lineNumber", "glDateTime", "lineAmount", "netAmount", "kind", "lineVersion", "glAccount", "previousAmount"]
    _attr_types = {"lineNumber": str, "glDateTime": str, "lineAmount": float, "netAmount": float, "kind": str, "lineVersion": str, "glAccount": str, "previousAmount": float}
    _defaults = {"lineNumber": '', "glDateTime": '', "lineAmount": 0.0, "netAmount": 0.0, "kind": "other", "lineVersion": '', "glAccount": '', "previousAmount": 0.0}
    _enums = {"kind": "ErpInvoiceLineItemKind"}
    _refs = ["ErpPayments", "ContainerErpInvoiceLineItem", "WorkBillingInfos", "ErpQuoteLineItem", "UserAttributes", "ErpRecDelvLineItem", "ErpPayableLineItem", "ComponentErpInvoiceLineItems", "billPeriod", "ErpInvoice", "CustomerBillingInfos", "ErpRecLineItem", "ErpJournalEntries"]
    _many_refs = ["ErpPayments", "WorkBillingInfos", "UserAttributes", "ComponentErpInvoiceLineItems", "CustomerBillingInfos", "ErpJournalEntries"]

    def getErpPayments(self):
        
        return self._ErpPayments

    def setErpPayments(self, value):
        for p in self._ErpPayments:
            filtered = [q for q in p.ErpInvoiceLineItems if q != self]
            self._ErpPayments._ErpInvoiceLineItems = filtered
        for r in value:
            if self not in r._ErpInvoiceLineItems:
                r._ErpInvoiceLineItems.append(self)
        self._ErpPayments = value

    ErpPayments = property(getErpPayments, setErpPayments)

    def addErpPayments(self, *ErpPayments):
        for obj in ErpPayments:
            if self not in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.append(self)
            self._ErpPayments.append(obj)

    def removeErpPayments(self, *ErpPayments):
        for obj in ErpPayments:
            if self in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.remove(self)
            self._ErpPayments.remove(obj)

    def getContainerErpInvoiceLineItem(self):
        
        return self._ContainerErpInvoiceLineItem

    def setContainerErpInvoiceLineItem(self, value):
        if self._ContainerErpInvoiceLineItem is not None:
            filtered = [x for x in self.ContainerErpInvoiceLineItem.ComponentErpInvoiceLineItems if x != self]
            self._ContainerErpInvoiceLineItem._ComponentErpInvoiceLineItems = filtered

        self._ContainerErpInvoiceLineItem = value
        if self._ContainerErpInvoiceLineItem is not None:
            if self not in self._ContainerErpInvoiceLineItem._ComponentErpInvoiceLineItems:
                self._ContainerErpInvoiceLineItem._ComponentErpInvoiceLineItems.append(self)

    ContainerErpInvoiceLineItem = property(getContainerErpInvoiceLineItem, setContainerErpInvoiceLineItem)

    def getWorkBillingInfos(self):
        
        return self._WorkBillingInfos

    def setWorkBillingInfos(self, value):
        for p in self._WorkBillingInfos:
            filtered = [q for q in p.ErpLineItems if q != self]
            self._WorkBillingInfos._ErpLineItems = filtered
        for r in value:
            if self not in r._ErpLineItems:
                r._ErpLineItems.append(self)
        self._WorkBillingInfos = value

    WorkBillingInfos = property(getWorkBillingInfos, setWorkBillingInfos)

    def addWorkBillingInfos(self, *WorkBillingInfos):
        for obj in WorkBillingInfos:
            if self not in obj._ErpLineItems:
                obj._ErpLineItems.append(self)
            self._WorkBillingInfos.append(obj)

    def removeWorkBillingInfos(self, *WorkBillingInfos):
        for obj in WorkBillingInfos:
            if self in obj._ErpLineItems:
                obj._ErpLineItems.remove(self)
            self._WorkBillingInfos.remove(obj)

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._ErpInvoiceLineItem = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem.ErpInvoiceLineItem = None
            self._ErpQuoteLineItem._ErpInvoiceLineItem = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

    def getUserAttributes(self):
        
        return self._UserAttributes

    def setUserAttributes(self, value):
        for p in self._UserAttributes:
            filtered = [q for q in p.ErpInvoiceLineItems if q != self]
            self._UserAttributes._ErpInvoiceLineItems = filtered
        for r in value:
            if self not in r._ErpInvoiceLineItems:
                r._ErpInvoiceLineItems.append(self)
        self._UserAttributes = value

    UserAttributes = property(getUserAttributes, setUserAttributes)

    def addUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self not in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.append(self)
            self._UserAttributes.append(obj)

    def removeUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.remove(self)
            self._UserAttributes.remove(obj)

    def getErpRecDelvLineItem(self):
        
        return self._ErpRecDelvLineItem

    def setErpRecDelvLineItem(self, value):
        if self._ErpRecDelvLineItem is not None:
            self._ErpRecDelvLineItem._ErpInvoiceLineItem = None

        self._ErpRecDelvLineItem = value
        if self._ErpRecDelvLineItem is not None:
            self._ErpRecDelvLineItem.ErpInvoiceLineItem = None
            self._ErpRecDelvLineItem._ErpInvoiceLineItem = self

    ErpRecDelvLineItem = property(getErpRecDelvLineItem, setErpRecDelvLineItem)

    def getErpPayableLineItem(self):
        
        return self._ErpPayableLineItem

    def setErpPayableLineItem(self, value):
        if self._ErpPayableLineItem is not None:
            self._ErpPayableLineItem._ErpInvoiceLineItem = None

        self._ErpPayableLineItem = value
        if self._ErpPayableLineItem is not None:
            self._ErpPayableLineItem.ErpInvoiceLineItem = None
            self._ErpPayableLineItem._ErpInvoiceLineItem = self

    ErpPayableLineItem = property(getErpPayableLineItem, setErpPayableLineItem)

    def getComponentErpInvoiceLineItems(self):
        
        return self._ComponentErpInvoiceLineItems

    def setComponentErpInvoiceLineItems(self, value):
        for x in self._ComponentErpInvoiceLineItems:
            x.ContainerErpInvoiceLineItem = None
        for y in value:
            y._ContainerErpInvoiceLineItem = self
        self._ComponentErpInvoiceLineItems = value

    ComponentErpInvoiceLineItems = property(getComponentErpInvoiceLineItems, setComponentErpInvoiceLineItems)

    def addComponentErpInvoiceLineItems(self, *ComponentErpInvoiceLineItems):
        for obj in ComponentErpInvoiceLineItems:
            obj.ContainerErpInvoiceLineItem = self

    def removeComponentErpInvoiceLineItems(self, *ComponentErpInvoiceLineItems):
        for obj in ComponentErpInvoiceLineItems:
            obj.ContainerErpInvoiceLineItem = None

    # Bill period for the line item.
    billPeriod = None

    def getErpInvoice(self):
        
        return self._ErpInvoice

    def setErpInvoice(self, value):
        if self._ErpInvoice is not None:
            filtered = [x for x in self.ErpInvoice.ErpInvoiceLineItems if x != self]
            self._ErpInvoice._ErpInvoiceLineItems = filtered

        self._ErpInvoice = value
        if self._ErpInvoice is not None:
            if self not in self._ErpInvoice._ErpInvoiceLineItems:
                self._ErpInvoice._ErpInvoiceLineItems.append(self)

    ErpInvoice = property(getErpInvoice, setErpInvoice)

    def getCustomerBillingInfos(self):
        """Customer billing for services rendered.
        """
        return self._CustomerBillingInfos

    def setCustomerBillingInfos(self, value):
        for p in self._CustomerBillingInfos:
            filtered = [q for q in p.ErpInvoiceLineItems if q != self]
            self._CustomerBillingInfos._ErpInvoiceLineItems = filtered
        for r in value:
            if self not in r._ErpInvoiceLineItems:
                r._ErpInvoiceLineItems.append(self)
        self._CustomerBillingInfos = value

    CustomerBillingInfos = property(getCustomerBillingInfos, setCustomerBillingInfos)

    def addCustomerBillingInfos(self, *CustomerBillingInfos):
        for obj in CustomerBillingInfos:
            if self not in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.append(self)
            self._CustomerBillingInfos.append(obj)

    def removeCustomerBillingInfos(self, *CustomerBillingInfos):
        for obj in CustomerBillingInfos:
            if self in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.remove(self)
            self._CustomerBillingInfos.remove(obj)

    def getErpRecLineItem(self):
        
        return self._ErpRecLineItem

    def setErpRecLineItem(self, value):
        if self._ErpRecLineItem is not None:
            self._ErpRecLineItem._ErpInvoiceLineItem = None

        self._ErpRecLineItem = value
        if self._ErpRecLineItem is not None:
            self._ErpRecLineItem.ErpInvoiceLineItem = None
            self._ErpRecLineItem._ErpInvoiceLineItem = self

    ErpRecLineItem = property(getErpRecLineItem, setErpRecLineItem)

    def getErpJournalEntries(self):
        
        return self._ErpJournalEntries

    def setErpJournalEntries(self, value):
        for x in self._ErpJournalEntries:
            x.ErpInvoiceLineItem = None
        for y in value:
            y._ErpInvoiceLineItem = self
        self._ErpJournalEntries = value

    ErpJournalEntries = property(getErpJournalEntries, setErpJournalEntries)

    def addErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            obj.ErpInvoiceLineItem = self

    def removeErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            obj.ErpInvoiceLineItem = None

