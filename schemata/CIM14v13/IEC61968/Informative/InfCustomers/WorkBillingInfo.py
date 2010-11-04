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

class WorkBillingInfo(Document):
    """Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.
    """

    def __init__(self, dueDateTime='', receivedDateTime='', deposit=0.0, workPrice=0.0, discount=0.0, costEstimate=0.0, issueDateTime='', ErpLineItems=None, CustomerAccount=None, Works=None, *args, **kw_args):
        """Initializes a new 'WorkBillingInfo' instance.

        @param dueDateTime: Date and time by which payment for bill is expected from client. 
        @param receivedDateTime: Date payment was received from client. 
        @param deposit: Amount of price on deposit. 
        @param workPrice: Amount of bill. 
        @param discount: Discount from standard price. 
        @param costEstimate: Estimated cost for work. 
        @param issueDateTime: Date and time bill was issued to client. 
        @param ErpLineItems:
        @param CustomerAccount:
        @param Works:
        """
        #: Date and time by which payment for bill is expected from client.
        self.dueDateTime = dueDateTime

        #: Date payment was received from client.
        self.receivedDateTime = receivedDateTime

        #: Amount of price on deposit.
        self.deposit = deposit

        #: Amount of bill.
        self.workPrice = workPrice

        #: Discount from standard price.
        self.discount = discount

        #: Estimated cost for work.
        self.costEstimate = costEstimate

        #: Date and time bill was issued to client.
        self.issueDateTime = issueDateTime

        self._ErpLineItems = []
        self.ErpLineItems = [] if ErpLineItems is None else ErpLineItems

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        self._Works = []
        self.Works = [] if Works is None else Works

        super(WorkBillingInfo, self).__init__(*args, **kw_args)

    def getErpLineItems(self):
        
        return self._ErpLineItems

    def setErpLineItems(self, value):
        for p in self._ErpLineItems:
            filtered = [q for q in p.WorkBillingInfos if q != self]
            self._ErpLineItems._WorkBillingInfos = filtered
        for r in value:
            if self not in r._WorkBillingInfos:
                r._WorkBillingInfos.append(self)
        self._ErpLineItems = value

    ErpLineItems = property(getErpLineItems, setErpLineItems)

    def addErpLineItems(self, *ErpLineItems):
        for obj in ErpLineItems:
            if self not in obj._WorkBillingInfos:
                obj._WorkBillingInfos.append(self)
            self._ErpLineItems.append(obj)

    def removeErpLineItems(self, *ErpLineItems):
        for obj in ErpLineItems:
            if self in obj._WorkBillingInfos:
                obj._WorkBillingInfos.remove(self)
            self._ErpLineItems.remove(obj)

    def getCustomerAccount(self):
        
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.WorkBillingInfos if x != self]
            self._CustomerAccount._WorkBillingInfos = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            self._CustomerAccount._WorkBillingInfos.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x._WorkBillingInfo = None
        for y in value:
            y._WorkBillingInfo = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj._WorkBillingInfo = self
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            obj._WorkBillingInfo = None
            self._Works.remove(obj)

