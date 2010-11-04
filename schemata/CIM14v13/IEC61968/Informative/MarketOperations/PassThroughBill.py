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

class PassThroughBill(Document):
    """Pass Through Bill is used for: 1)Two sided charge transactions with or without ISO involvement (hence the ?pass thru?) 2) Specific direct charges or payments that are calculated outside or provided directly to settlements 3) Specific charge bill determinants that are externally supplied and used in charge calculations
    """

    def __init__(self, transactionDate='', transactionType='', billRunType='', timeZone='', taxAmount=0.0, effectiveDate='', tradeDate='', billStart='', price=0.0, soldTo='', previousStart='', providedBy='', productCode='', isProfiled=False, quantity=None, previousEnd='', serviceStart='', paidTo='', billEnd='', amount=0.0, serviceEnd='', billedTo='', isDisputed=False, MarketStatementLineItem=None, UserAttributes=None, ChargeProfiles=None, **kw_args):
        """Initializes a new 'PassThroughBill' instance.

        @param transactionDate: The date the transaction occurs. 
        @param transactionType: The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant 
        @param billRunType: The settlement run type, for example: prelim, final, and rerun. 
        @param timeZone: The time zone code 
        @param taxAmount: The tax on services taken. 
        @param effectiveDate: The effective date of the transaction 
        @param tradeDate: The trade date 
        @param billStart: Bill period start date 
        @param price: The price of product/service. 
        @param soldTo: The company to which the PTB transaction is sold. 
        @param previousStart: The previous bill period start date 
        @param providedBy: The company by which the PTB transaction service is provided. 
        @param productCode: The product identifier for determining the charge type of the transaction. 
        @param isProfiled: A flag indicating whether there is a profile data associated with the PTB. 
        @param quantity: The product quantity. 
        @param previousEnd: The previous bill period end date 
        @param serviceStart: The start date of service provided, if periodic. 
        @param paidTo: The company to which the PTB transaction is paid. 
        @param billEnd: Bill period end date 
        @param amount: The charge amount of the product/service. 
        @param serviceEnd: The end date of service provided, if periodic. 
        @param billedTo: The company to which the PTB transaction is billed. 
        @param isDisputed: Disputed transaction indicator 
        @param MarketStatementLineItem:
        @param UserAttributes:
        @param ChargeProfiles:
        """
        #: The date the transaction occurs.
        self.transactionDate = transactionDate

        #: The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant
        self.transactionType = transactionType

        #: The settlement run type, for example: prelim, final, and rerun.
        self.billRunType = billRunType

        #: The time zone code
        self.timeZone = timeZone

        #: The tax on services taken.
        self.taxAmount = taxAmount

        #: The effective date of the transaction
        self.effectiveDate = effectiveDate

        #: The trade date
        self.tradeDate = tradeDate

        #: Bill period start date
        self.billStart = billStart

        #: The price of product/service.
        self.price = price

        #: The company to which the PTB transaction is sold.
        self.soldTo = soldTo

        #: The previous bill period start date
        self.previousStart = previousStart

        #: The company by which the PTB transaction service is provided.
        self.providedBy = providedBy

        #: The product identifier for determining the charge type of the transaction.
        self.productCode = productCode

        #: A flag indicating whether there is a profile data associated with the PTB.
        self.isProfiled = isProfiled

        #: The product quantity.
        self.quantity = quantity

        #: The previous bill period end date
        self.previousEnd = previousEnd

        #: The start date of service provided, if periodic.
        self.serviceStart = serviceStart

        #: The company to which the PTB transaction is paid.
        self.paidTo = paidTo

        #: Bill period end date
        self.billEnd = billEnd

        #: The charge amount of the product/service.
        self.amount = amount

        #: The end date of service provided, if periodic.
        self.serviceEnd = serviceEnd

        #: The company to which the PTB transaction is billed.
        self.billedTo = billedTo

        #: Disputed transaction indicator
        self.isDisputed = isDisputed

        self._MarketStatementLineItem = None
        self.MarketStatementLineItem = MarketStatementLineItem

        self._UserAttributes = []
        self.UserAttributes = [] if UserAttributes is None else UserAttributes

        self._ChargeProfiles = []
        self.ChargeProfiles = [] if ChargeProfiles is None else ChargeProfiles

        super(PassThroughBill, self).__init__(**kw_args)

    def getMarketStatementLineItem(self):
        
        return self._MarketStatementLineItem

    def setMarketStatementLineItem(self, value):
        if self._MarketStatementLineItem is not None:
            self._MarketStatementLineItem._PassThroughBill = None

        self._MarketStatementLineItem = value
        if self._MarketStatementLineItem is not None:
            self._MarketStatementLineItem._PassThroughBill = self

    MarketStatementLineItem = property(getMarketStatementLineItem, setMarketStatementLineItem)

    def getUserAttributes(self):
        
        return self._UserAttributes

    def setUserAttributes(self, value):
        for p in self._UserAttributes:
            filtered = [q for q in p.PassThroughBills if q != self]
            self._UserAttributes._PassThroughBills = filtered
        for r in value:
            if self not in r._PassThroughBills:
                r._PassThroughBills.append(self)
        self._UserAttributes = value

    UserAttributes = property(getUserAttributes, setUserAttributes)

    def addUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self not in obj._PassThroughBills:
                obj._PassThroughBills.append(self)
            self._UserAttributes.append(obj)

    def removeUserAttributes(self, *UserAttributes):
        for obj in UserAttributes:
            if self in obj._PassThroughBills:
                obj._PassThroughBills.remove(self)
            self._UserAttributes.remove(obj)

    def getChargeProfiles(self):
        
        return self._ChargeProfiles

    def setChargeProfiles(self, value):
        for x in self._ChargeProfiles:
            x._PassTroughBill = None
        for y in value:
            y._PassTroughBill = self
        self._ChargeProfiles = value

    ChargeProfiles = property(getChargeProfiles, setChargeProfiles)

    def addChargeProfiles(self, *ChargeProfiles):
        for obj in ChargeProfiles:
            obj._PassTroughBill = self
            self._ChargeProfiles.append(obj)

    def removeChargeProfiles(self, *ChargeProfiles):
        for obj in ChargeProfiles:
            obj._PassTroughBill = None
            self._ChargeProfiles.remove(obj)

