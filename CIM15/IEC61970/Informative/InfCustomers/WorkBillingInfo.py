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

class WorkBillingInfo(Document):
    """Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.Billing information for work performed for the customer. The history of Work Billing Info, Invoices, and Payments is to be maintained in associated ActivityRecords.
    """

    def __init__(self, issueDateTime='', deposit=0.0, costEstimate=0.0, discount=0.0, dueDateTime='', receivedDateTime='', workPrice=0.0, Works=None, CustomerAccount=None, ErpLineItems=None, *args, **kw_args):
        """Initialises a new 'WorkBillingInfo' instance.

        @param issueDateTime: Date and time bill was issued to client. 
        @param deposit: Amount of price on deposit. 
        @param costEstimate: Estimated cost for work. 
        @param discount: Discount from standard price. 
        @param dueDateTime: Date and time by which payment for bill is expected from client. 
        @param receivedDateTime: Date payment was received from client. 
        @param workPrice: Amount of bill. 
        @param Works:
        @param CustomerAccount:
        @param ErpLineItems:
        """
        #: Date and time bill was issued to client.
        self.issueDateTime = issueDateTime

        #: Amount of price on deposit.
        self.deposit = deposit

        #: Estimated cost for work.
        self.costEstimate = costEstimate

        #: Discount from standard price.
        self.discount = discount

        #: Date and time by which payment for bill is expected from client.
        self.dueDateTime = dueDateTime

        #: Date payment was received from client.
        self.receivedDateTime = receivedDateTime

        #: Amount of bill.
        self.workPrice = workPrice

        self._Works = []
        self.Works = [] if Works is None else Works

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        self._ErpLineItems = []
        self.ErpLineItems = [] if ErpLineItems is None else ErpLineItems

        super(WorkBillingInfo, self).__init__(*args, **kw_args)

    _attrs = ["issueDateTime", "deposit", "costEstimate", "discount", "dueDateTime", "receivedDateTime", "workPrice"]
    _attr_types = {"issueDateTime": str, "deposit": float, "costEstimate": float, "discount": float, "dueDateTime": str, "receivedDateTime": str, "workPrice": float}
    _defaults = {"issueDateTime": '', "deposit": 0.0, "costEstimate": 0.0, "discount": 0.0, "dueDateTime": '', "receivedDateTime": '', "workPrice": 0.0}
    _enums = {}
    _refs = ["Works", "CustomerAccount", "ErpLineItems"]
    _many_refs = ["Works", "ErpLineItems"]

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x.WorkBillingInfo = None
        for y in value:
            y._WorkBillingInfo = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj.WorkBillingInfo = self

    def removeWorks(self, *Works):
        for obj in Works:
            obj.WorkBillingInfo = None

    def getCustomerAccount(self):
        
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.WorkBillingInfos if x != self]
            self._CustomerAccount._WorkBillingInfos = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            if self not in self._CustomerAccount._WorkBillingInfos:
                self._CustomerAccount._WorkBillingInfos.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

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

