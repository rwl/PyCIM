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

from CIM14.IEC61968.Common.Document import Document

class CustomerAccount(Document):
    """Assignment of a group of products and services purchased by the Customer through a CustomerAgreement, used as a mechanism for customer billing and payment. It contains common information from the various types of CustomerAgreements to create billings (invoices) for a Customer and receive payment.
    """

    def __init__(self, PaymentTransactions=None, CustomerAgreements=None, *args, **kw_args):
        """Initialises a new 'CustomerAccount' instance.

        @param PaymentTransactions: All payment transactions for this customer account.
        @param CustomerAgreements: All agreements for this customer account.
        """
        self._PaymentTransactions = []
        self.PaymentTransactions = [] if PaymentTransactions is None else PaymentTransactions

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        super(CustomerAccount, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PaymentTransactions", "CustomerAgreements"]
    _many_refs = ["PaymentTransactions", "CustomerAgreements"]

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

