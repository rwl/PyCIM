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

class ErpInvoiceLineItem(Document):
    """An individual line item on an invoice.
    """

    def __init__(self, kind='recalculation', lineNumber='', netAmount=0.0, glAccount='', glDateTime='', lineAmount=0.0, previousAmount=0.0, lineVersion='', WorkBillingInfos=None, ErpRecLineItem=None, MarketFactors=None, ErpJournalEntries=None, billPeriod=None, ErpRecDelvLineItem=None, CustomerBillingInfos=None, UserAttributes=None, ContainerErpInvoiceLineItem=None, ComponentErpInvoiceLineItems=None, ErpPayments=None, Settlements=None, ErpInvoice=None, ErpQuoteLineItem=None, ErpPayableLineItem=None, *args, **kw_args):
        """Initializes a new 'ErpInvoiceLineItem' instance.

        @param kind: Kind of line item. Values are: "recalculation", "initial", "other"
        @param lineNumber: Line item number on invoice statement. 
        @param netAmount: Net line item charge amount. 
        @param glAccount: General Ledger account code, must be a valid combination. 
        @param glDateTime: Date and time line item will be posted to the General Ledger. 
        @param lineAmount: Amount due for this line item. 
        @param previousAmount: Previous line item charge amount. 
        @param lineVersion: Version number of the bill run. 
        @param WorkBillingInfos:
        @param ErpRecLineItem:
        @param MarketFactors:
        @param ErpJournalEntries:
        @param billPeriod: Bill period for the line item.
        @param ErpRecDelvLineItem:
        @param CustomerBillingInfos: Customer billing for services rendered.
        @param UserAttributes:
        @param ContainerErpInvoiceLineItem:
        @param ComponentErpInvoiceLineItems:
        @param ErpPayments:
        @param Settlements:
        @param ErpInvoice:
        @param ErpQuoteLineItem:
        @param ErpPayableLineItem:
        """
        #: Kind of line item.Values are: "recalculation", "initial", "other"
        self.kind = kind

        #: Line item number on invoice statement.
        self.lineNumber = lineNumber

        #: Net line item charge amount.
        self.netAmount = netAmount

        #: General Ledger account code, must be a valid combination.
        self.glAccount = glAccount

        #: Date and time line item will be posted to the General Ledger.
        self.glDateTime = glDateTime

        #: Amount due for this line item.
        self.lineAmount = lineAmount

        #: Previous line item charge amount.
        self.previousAmount = previousAmount

        #: Version number of the bill run.
        self.lineVersion = lineVersion

        self._WorkBillingInfos = []
        self.WorkBillingInfos = [] if WorkBillingInfos is None else WorkBillingInfos

        self._ErpRecLineItem = None
        self.ErpRecLineItem = ErpRecLineItem

        self._MarketFactors = []
        self.MarketFactors = [] if MarketFactors is None else MarketFactors

        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        self.billPeriod = billPeriod

        self._ErpRecDelvLineItem = None
        self.ErpRecDelvLineItem = ErpRecDelvLineItem

        self._CustomerBillingInfos = []
        self.CustomerBillingInfos = [] if CustomerBillingInfos is None else CustomerBillingInfos

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        self._ContainerErpInvoiceLineItem = None
        self.ContainerErpInvoiceLineItem = ContainerErpInvoiceLineItem

        self._ComponentErpInvoiceLineItems = []
        self.ComponentErpInvoiceLineItems = [] if ComponentErpInvoiceLineItems is None else ComponentErpInvoiceLineItems

        self._ErpPayments = []
        self.ErpPayments = [] if ErpPayments is None else ErpPayments

        self._Settlements = []
        self.Settlements = [] if Settlements is None else Settlements

        self._ErpInvoice = None
        self.ErpInvoice = ErpInvoice

        self._ErpQuoteLineItem = None
        self.ErpQuoteLineItem = ErpQuoteLineItem

        self._ErpPayableLineItem = None
        self.ErpPayableLineItem = ErpPayableLineItem

        super(ErpInvoiceLineItem, self).__init__(*args, **kw_args)

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

    def getErpRecLineItem(self):
        
        return self._ErpRecLineItem

    def setErpRecLineItem(self, value):
        if self._ErpRecLineItem is not None:
            self._ErpRecLineItem._ErpInvoiceLineItem = None

        self._ErpRecLineItem = value
        if self._ErpRecLineItem is not None:
            self._ErpRecLineItem._ErpInvoiceLineItem = self

    ErpRecLineItem = property(getErpRecLineItem, setErpRecLineItem)

    def getMarketFactors(self):
        
        return self._MarketFactors

    def setMarketFactors(self, value):
        for p in self._MarketFactors:
            filtered = [q for q in p.ErpInvoices if q != self]
            self._MarketFactors._ErpInvoices = filtered
        for r in value:
            if self not in r._ErpInvoices:
                r._ErpInvoices.append(self)
        self._MarketFactors = value

    MarketFactors = property(getMarketFactors, setMarketFactors)

    def addMarketFactors(self, *MarketFactors):
        for obj in MarketFactors:
            if self not in obj._ErpInvoices:
                obj._ErpInvoices.append(self)
            self._MarketFactors.append(obj)

    def removeMarketFactors(self, *MarketFactors):
        for obj in MarketFactors:
            if self in obj._ErpInvoices:
                obj._ErpInvoices.remove(self)
            self._MarketFactors.remove(obj)

    def getErpJournalEntries(self):
        
        return self._ErpJournalEntries

    def setErpJournalEntries(self, value):
        for x in self._ErpJournalEntries:
            x._ErpInvoiceLineItem = None
        for y in value:
            y._ErpInvoiceLineItem = self
        self._ErpJournalEntries = value

    ErpJournalEntries = property(getErpJournalEntries, setErpJournalEntries)

    def addErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            obj._ErpInvoiceLineItem = self
            self._ErpJournalEntries.append(obj)

    def removeErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            obj._ErpInvoiceLineItem = None
            self._ErpJournalEntries.remove(obj)

    # Bill period for the line item.
    billPeriod = None

    def getErpRecDelvLineItem(self):
        
        return self._ErpRecDelvLineItem

    def setErpRecDelvLineItem(self, value):
        if self._ErpRecDelvLineItem is not None:
            self._ErpRecDelvLineItem._ErpInvoiceLineItem = None

        self._ErpRecDelvLineItem = value
        if self._ErpRecDelvLineItem is not None:
            self._ErpRecDelvLineItem._ErpInvoiceLineItem = self

    ErpRecDelvLineItem = property(getErpRecDelvLineItem, setErpRecDelvLineItem)

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

    def getContainerErpInvoiceLineItem(self):
        
        return self._ContainerErpInvoiceLineItem

    def setContainerErpInvoiceLineItem(self, value):
        if self._ContainerErpInvoiceLineItem is not None:
            filtered = [x for x in self.ContainerErpInvoiceLineItem.ComponentErpInvoiceLineItems if x != self]
            self._ContainerErpInvoiceLineItem._ComponentErpInvoiceLineItems = filtered

        self._ContainerErpInvoiceLineItem = value
        if self._ContainerErpInvoiceLineItem is not None:
            self._ContainerErpInvoiceLineItem._ComponentErpInvoiceLineItems.append(self)

    ContainerErpInvoiceLineItem = property(getContainerErpInvoiceLineItem, setContainerErpInvoiceLineItem)

    def getComponentErpInvoiceLineItems(self):
        
        return self._ComponentErpInvoiceLineItems

    def setComponentErpInvoiceLineItems(self, value):
        for x in self._ComponentErpInvoiceLineItems:
            x._ContainerErpInvoiceLineItem = None
        for y in value:
            y._ContainerErpInvoiceLineItem = self
        self._ComponentErpInvoiceLineItems = value

    ComponentErpInvoiceLineItems = property(getComponentErpInvoiceLineItems, setComponentErpInvoiceLineItems)

    def addComponentErpInvoiceLineItems(self, *ComponentErpInvoiceLineItems):
        for obj in ComponentErpInvoiceLineItems:
            obj._ContainerErpInvoiceLineItem = self
            self._ComponentErpInvoiceLineItems.append(obj)

    def removeComponentErpInvoiceLineItems(self, *ComponentErpInvoiceLineItems):
        for obj in ComponentErpInvoiceLineItems:
            obj._ContainerErpInvoiceLineItem = None
            self._ComponentErpInvoiceLineItems.remove(obj)

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

    def getSettlements(self):
        
        return self._Settlements

    def setSettlements(self, value):
        for p in self._Settlements:
            filtered = [q for q in p.ErpInvoiceLineItems if q != self]
            self._Settlements._ErpInvoiceLineItems = filtered
        for r in value:
            if self not in r._ErpInvoiceLineItems:
                r._ErpInvoiceLineItems.append(self)
        self._Settlements = value

    Settlements = property(getSettlements, setSettlements)

    def addSettlements(self, *Settlements):
        for obj in Settlements:
            if self not in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.append(self)
            self._Settlements.append(obj)

    def removeSettlements(self, *Settlements):
        for obj in Settlements:
            if self in obj._ErpInvoiceLineItems:
                obj._ErpInvoiceLineItems.remove(self)
            self._Settlements.remove(obj)

    def getErpInvoice(self):
        
        return self._ErpInvoice

    def setErpInvoice(self, value):
        if self._ErpInvoice is not None:
            filtered = [x for x in self.ErpInvoice.ErpInvoiceLineItems if x != self]
            self._ErpInvoice._ErpInvoiceLineItems = filtered

        self._ErpInvoice = value
        if self._ErpInvoice is not None:
            self._ErpInvoice._ErpInvoiceLineItems.append(self)

    ErpInvoice = property(getErpInvoice, setErpInvoice)

    def getErpQuoteLineItem(self):
        
        return self._ErpQuoteLineItem

    def setErpQuoteLineItem(self, value):
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._ErpInvoiceLineItem = None

        self._ErpQuoteLineItem = value
        if self._ErpQuoteLineItem is not None:
            self._ErpQuoteLineItem._ErpInvoiceLineItem = self

    ErpQuoteLineItem = property(getErpQuoteLineItem, setErpQuoteLineItem)

    def getErpPayableLineItem(self):
        
        return self._ErpPayableLineItem

    def setErpPayableLineItem(self, value):
        if self._ErpPayableLineItem is not None:
            self._ErpPayableLineItem._ErpInvoiceLineItem = None

        self._ErpPayableLineItem = value
        if self._ErpPayableLineItem is not None:
            self._ErpPayableLineItem._ErpInvoiceLineItem = self

    ErpPayableLineItem = property(getErpPayableLineItem, setErpPayableLineItem)

