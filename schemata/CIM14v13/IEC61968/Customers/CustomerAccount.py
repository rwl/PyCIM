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

class CustomerAccount(Document):
    """Assignment of a group of products and services purchased by the Customer through a CustomerAgreement, used as a mechanism for customer billing and payment. It contains common information from the various types of CustomerAgreements to create billings (invoices) for a Customer and receive payment.
    """

    def __init__(self, budgetBill='', billingCycle='', WorkBillingInfos=None, PaymentTransactions=None, CustomerAgreements=None, CustomerBillingInfos=None, ErpInvoicees=None, **kw_args):
        """Initializes a new 'CustomerAccount' instance.

        @param budgetBill: Budget bill code. 
        @param billingCycle: Cycle day on which this customer account will normally be billed, used to determine when to produce the CustomerBillingInfo for this customer account. 
        @param WorkBillingInfos:
        @param PaymentTransactions: All payment transactions for this customer account.
        @param CustomerAgreements: All agreements for this customer account.
        @param CustomerBillingInfos:
        @param ErpInvoicees:
        """
        #: Budget bill code.
        self.budgetBill = budgetBill

        #: Cycle day on which this customer account will normally be billed, used to determine when to produce the CustomerBillingInfo for this customer account.
        self.billingCycle = billingCycle

        self._WorkBillingInfos = []
        self.WorkBillingInfos = [] if WorkBillingInfos is None else WorkBillingInfos

        self._PaymentTransactions = []
        self.PaymentTransactions = [] if PaymentTransactions is None else PaymentTransactions

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._CustomerBillingInfos = []
        self.CustomerBillingInfos = [] if CustomerBillingInfos is None else CustomerBillingInfos

        self._ErpInvoicees = []
        self.ErpInvoicees = [] if ErpInvoicees is None else ErpInvoicees

        super(CustomerAccount, self).__init__(**kw_args)

    def getWorkBillingInfos(self):
        
        return self._WorkBillingInfos

    def setWorkBillingInfos(self, value):
        for x in self._WorkBillingInfos:
            x._CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._WorkBillingInfos = value

    WorkBillingInfos = property(getWorkBillingInfos, setWorkBillingInfos)

    def addWorkBillingInfos(self, *WorkBillingInfos):
        for obj in WorkBillingInfos:
            obj._CustomerAccount = self
            self._WorkBillingInfos.append(obj)

    def removeWorkBillingInfos(self, *WorkBillingInfos):
        for obj in WorkBillingInfos:
            obj._CustomerAccount = None
            self._WorkBillingInfos.remove(obj)

    def getPaymentTransactions(self):
        """All payment transactions for this customer account.
        """
        return self._PaymentTransactions

    def setPaymentTransactions(self, value):
        for x in self._PaymentTransactions:
            x._CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._PaymentTransactions = value

    PaymentTransactions = property(getPaymentTransactions, setPaymentTransactions)

    def addPaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj._CustomerAccount = self
            self._PaymentTransactions.append(obj)

    def removePaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj._CustomerAccount = None
            self._PaymentTransactions.remove(obj)

    def getCustomerAgreements(self):
        """All agreements for this customer account.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x._CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._CustomerAccount = self
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._CustomerAccount = None
            self._CustomerAgreements.remove(obj)

    def getCustomerBillingInfos(self):
        
        return self._CustomerBillingInfos

    def setCustomerBillingInfos(self, value):
        for x in self._CustomerBillingInfos:
            x._CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._CustomerBillingInfos = value

    CustomerBillingInfos = property(getCustomerBillingInfos, setCustomerBillingInfos)

    def addCustomerBillingInfos(self, *CustomerBillingInfos):
        for obj in CustomerBillingInfos:
            obj._CustomerAccount = self
            self._CustomerBillingInfos.append(obj)

    def removeCustomerBillingInfos(self, *CustomerBillingInfos):
        for obj in CustomerBillingInfos:
            obj._CustomerAccount = None
            self._CustomerBillingInfos.remove(obj)

    def getErpInvoicees(self):
        
        return self._ErpInvoicees

    def setErpInvoicees(self, value):
        for x in self._ErpInvoicees:
            x._CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._ErpInvoicees = value

    ErpInvoicees = property(getErpInvoicees, setErpInvoicees)

    def addErpInvoicees(self, *ErpInvoicees):
        for obj in ErpInvoicees:
            obj._CustomerAccount = self
            self._ErpInvoicees.append(obj)

    def removeErpInvoicees(self, *ErpInvoicees):
        for obj in ErpInvoicees:
            obj._CustomerAccount = None
            self._ErpInvoicees.remove(obj)

