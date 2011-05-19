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

class BankAccount(Document):
    """Bank account.Bank account.
    """

    def __init__(self, accountNumber='', ServiceSupplier=None, Bank=None, *args, **kw_args):
        """Initialises a new 'BankAccount' instance.

        @param accountNumber: Account reference number. 
        @param ServiceSupplier: ServiceSupplier that is owner of this BankAccount.
        @param Bank: Bank that provides this BankAccount.
        """
        #: Account reference number.
        self.accountNumber = accountNumber

        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._Bank = None
        self.Bank = Bank

        super(BankAccount, self).__init__(*args, **kw_args)

    _attrs = ["accountNumber"]
    _attr_types = {"accountNumber": str}
    _defaults = {"accountNumber": ''}
    _enums = {}
    _refs = ["ServiceSupplier", "Bank"]
    _many_refs = []

    def getServiceSupplier(self):
        """ServiceSupplier that is owner of this BankAccount.
        """
        return self._ServiceSupplier

    def setServiceSupplier(self, value):
        if self._ServiceSupplier is not None:
            filtered = [x for x in self.ServiceSupplier.BankAccounts if x != self]
            self._ServiceSupplier._BankAccounts = filtered

        self._ServiceSupplier = value
        if self._ServiceSupplier is not None:
            if self not in self._ServiceSupplier._BankAccounts:
                self._ServiceSupplier._BankAccounts.append(self)

    ServiceSupplier = property(getServiceSupplier, setServiceSupplier)

    def getBank(self):
        """Bank that provides this BankAccount.
        """
        return self._Bank

    def setBank(self, value):
        if self._Bank is not None:
            filtered = [x for x in self.Bank.BankAccounts if x != self]
            self._Bank._BankAccounts = filtered

        self._Bank = value
        if self._Bank is not None:
            if self not in self._Bank._BankAccounts:
                self._Bank._BankAccounts.append(self)

    Bank = property(getBank, setBank)

