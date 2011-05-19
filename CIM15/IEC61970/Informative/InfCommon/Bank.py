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

from CIM15.IEC61968.Common.Organisation import Organisation

class Bank(Organisation):
    """Organisation that is a commercial bank, agency, or other institution that offers a similar service.Organisation that is a commercial bank, agency, or other institution that offers a similar service.
    """

    def __init__(self, bic='', iban='', branchCode='', BankAccounts=None, *args, **kw_args):
        """Initialises a new 'Bank' instance.

        @param bic: Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation. 
        @param iban: International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362). 
        @param branchCode: Codified reference to the particular branch of the bank where BankAccount is held. 
        @param BankAccounts: All BankAccounts this Bank provides.
        """
        #: Bank identifier code as defined in ISO 9362; for use in countries wher IBAN is not yet in operation.
        self.bic = bic

        #: International bank account number defined in ISO 13616; for countries where IBAN is not in operation, the existing BIC or SWIFT codes may be used instead (see ISO 9362).
        self.iban = iban

        #: Codified reference to the particular branch of the bank where BankAccount is held.
        self.branchCode = branchCode

        self._BankAccounts = []
        self.BankAccounts = [] if BankAccounts is None else BankAccounts

        super(Bank, self).__init__(*args, **kw_args)

    _attrs = ["bic", "iban", "branchCode"]
    _attr_types = {"bic": str, "iban": str, "branchCode": str}
    _defaults = {"bic": '', "iban": '', "branchCode": ''}
    _enums = {}
    _refs = ["BankAccounts"]
    _many_refs = ["BankAccounts"]

    def getBankAccounts(self):
        """All BankAccounts this Bank provides.
        """
        return self._BankAccounts

    def setBankAccounts(self, value):
        for x in self._BankAccounts:
            x.Bank = None
        for y in value:
            y._Bank = self
        self._BankAccounts = value

    BankAccounts = property(getBankAccounts, setBankAccounts)

    def addBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj.Bank = self

    def removeBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj.Bank = None

