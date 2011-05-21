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

from CIM14.IEC61968.PaymentMetering.Shift import Shift

class VendorShift(Shift):
    """The operating shift for a vendor during which he may transact against the merchant's account. It aggregates transactions and receipts during the shift and periodically debits a merchant account. The totals in VendorShift should always = sum of totals aggregated in all cashier shifts that were open under the particular vendor shift.
    """

    def __init__(self, merchantDebitAmount=0.0, posted=False, MerchantAccount=None, Transactions=None, Receipts=None, Vendor=None, *args, **kw_args):
        """Initialises a new 'VendorShift' instance.

        @param merchantDebitAmount: The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount). 
        @param posted: = true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes. 
        @param MerchantAccount: Merchant account this vendor shift periodically debits (based on aggregated transactions).
        @param Transactions:
        @param Receipts:
        @param Vendor: Vendor that opens and owns this vendor shift.
        """
        #: The amount that is to be debited from the merchant account for this vendor shift. This amount reflects the sum(PaymentTransaction.transactionAmount).
        self.merchantDebitAmount = merchantDebitAmount

        #: = true if merchantDebitAmount has been debited from MerchantAccount; typically happens at the end of VendorShift when it closes.
        self.posted = posted

        self._MerchantAccount = None
        self.MerchantAccount = MerchantAccount

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        self._Receipts = []
        self.Receipts = [] if Receipts is None else Receipts

        self._Vendor = None
        self.Vendor = Vendor

        super(VendorShift, self).__init__(*args, **kw_args)

    _attrs = ["merchantDebitAmount", "posted"]
    _attr_types = {"merchantDebitAmount": float, "posted": bool}
    _defaults = {"merchantDebitAmount": 0.0, "posted": False}
    _enums = {}
    _refs = ["MerchantAccount", "Transactions", "Receipts", "Vendor"]
    _many_refs = ["Transactions", "Receipts"]

    def getMerchantAccount(self):
        """Merchant account this vendor shift periodically debits (based on aggregated transactions).
        """
        return self._MerchantAccount

    def setMerchantAccount(self, value):
        if self._MerchantAccount is not None:
            filtered = [x for x in self.MerchantAccount.VendorShifts if x != self]
            self._MerchantAccount._VendorShifts = filtered

        self._MerchantAccount = value
        if self._MerchantAccount is not None:
            if self not in self._MerchantAccount._VendorShifts:
                self._MerchantAccount._VendorShifts.append(self)

    MerchantAccount = property(getMerchantAccount, setMerchantAccount)

    def getTransactions(self):
        
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x.VendorShift = None
        for y in value:
            y._VendorShift = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj.VendorShift = self

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj.VendorShift = None

    def getReceipts(self):
        
        return self._Receipts

    def setReceipts(self, value):
        for x in self._Receipts:
            x.VendorShift = None
        for y in value:
            y._VendorShift = self
        self._Receipts = value

    Receipts = property(getReceipts, setReceipts)

    def addReceipts(self, *Receipts):
        for obj in Receipts:
            obj.VendorShift = self

    def removeReceipts(self, *Receipts):
        for obj in Receipts:
            obj.VendorShift = None

    def getVendor(self):
        """Vendor that opens and owns this vendor shift.
        """
        return self._Vendor

    def setVendor(self, value):
        if self._Vendor is not None:
            filtered = [x for x in self.Vendor.VendorShifts if x != self]
            self._Vendor._VendorShifts = filtered

        self._Vendor = value
        if self._Vendor is not None:
            if self not in self._Vendor._VendorShifts:
                self._Vendor._VendorShifts.append(self)

    Vendor = property(getVendor, setVendor)

