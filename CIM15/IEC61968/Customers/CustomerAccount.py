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

class CustomerAccount(Document):
    """Assignment of a group of products and services purchased by the customer through a customer agreement, used as a mechanism for customer billing and payment. It contains common information from the various types of customer agreements to create billings (invoices) for a customer and receive payment.Assignment of a group of products and services purchased by the customer through a customer agreement, used as a mechanism for customer billing and payment. It contains common information from the various types of customer agreements to create billings (invoices) for a customer and receive payment.
    """

    def __init__(self, WorkBillingInfos=None, CustomerAgreements=None, ErpInvoicees=None, PaymentTransactions=None, CustomerBillingInfos=None, *args, **kw_args):
        """Initialises a new 'CustomerAccount' instance.

        @param WorkBillingInfos:
        @param CustomerAgreements: All agreements for this customer account.
        @param ErpInvoicees:
        @param PaymentTransactions: All payment transactions for this customer account.
        @param CustomerBillingInfos:
        """
        self._WorkBillingInfos = []
        self.WorkBillingInfos = [] if WorkBillingInfos is None else WorkBillingInfos

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._ErpInvoicees = []
        self.ErpInvoicees = [] if ErpInvoicees is None else ErpInvoicees

        self._PaymentTransactions = []
        self.PaymentTransactions = [] if PaymentTransactions is None else PaymentTransactions

        self._CustomerBillingInfos = []
        self.CustomerBillingInfos = [] if CustomerBillingInfos is None else CustomerBillingInfos

        super(CustomerAccount, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["WorkBillingInfos", "CustomerAgreements", "ErpInvoicees", "PaymentTransactions", "CustomerBillingInfos"]
    _many_refs = ["WorkBillingInfos", "CustomerAgreements", "ErpInvoicees", "PaymentTransactions", "CustomerBillingInfos"]

    def getWorkBillingInfos(self):
        
        return self._WorkBillingInfos

    def setWorkBillingInfos(self, value):
        for x in self._WorkBillingInfos:
            x.CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._WorkBillingInfos = value

    WorkBillingInfos = property(getWorkBillingInfos, setWorkBillingInfos)

    def addWorkBillingInfos(self, *WorkBillingInfos):
        for obj in WorkBillingInfos:
            obj.CustomerAccount = self

    def removeWorkBillingInfos(self, *WorkBillingInfos):
        for obj in WorkBillingInfos:
            obj.CustomerAccount = None

    def getCustomerAgreements(self):
        """All agreements for this customer account.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x.CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.CustomerAccount = self

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.CustomerAccount = None

    def getErpInvoicees(self):
        
        return self._ErpInvoicees

    def setErpInvoicees(self, value):
        for x in self._ErpInvoicees:
            x.CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._ErpInvoicees = value

    ErpInvoicees = property(getErpInvoicees, setErpInvoicees)

    def addErpInvoicees(self, *ErpInvoicees):
        for obj in ErpInvoicees:
            obj.CustomerAccount = self

    def removeErpInvoicees(self, *ErpInvoicees):
        for obj in ErpInvoicees:
            obj.CustomerAccount = None

    def getPaymentTransactions(self):
        """All payment transactions for this customer account.
        """
        return self._PaymentTransactions

    def setPaymentTransactions(self, value):
        for x in self._PaymentTransactions:
            x.CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._PaymentTransactions = value

    PaymentTransactions = property(getPaymentTransactions, setPaymentTransactions)

    def addPaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj.CustomerAccount = self

    def removePaymentTransactions(self, *PaymentTransactions):
        for obj in PaymentTransactions:
            obj.CustomerAccount = None

    def getCustomerBillingInfos(self):
        
        return self._CustomerBillingInfos

    def setCustomerBillingInfos(self, value):
        for x in self._CustomerBillingInfos:
            x.CustomerAccount = None
        for y in value:
            y._CustomerAccount = self
        self._CustomerBillingInfos = value

    CustomerBillingInfos = property(getCustomerBillingInfos, setCustomerBillingInfos)

    def addCustomerBillingInfos(self, *CustomerBillingInfos):
        for obj in CustomerBillingInfos:
            obj.CustomerAccount = self

    def removeCustomerBillingInfos(self, *CustomerBillingInfos):
        for obj in CustomerBillingInfos:
            obj.CustomerAccount = None

