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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Receipt(IdentifiedObject):
    """Record of total receipted payment from customer.
    """

    def __init__(self, isBankable=False, CashierShift=None, Tenders=None, VendorShift=None, Transactions=None, line=None, *args, **kw_args):
        """Initialises a new 'Receipt' instance.

        @param isBankable: True if this receipted payment is manually bankable, otherwise it is an electronic funds transfer. 
        @param CashierShift: Cashier shift during which this receipt was recorded.
        @param Tenders: All payments received in the form of tenders recorded by this receipt.
        @param VendorShift: Vendor shift during which this receipt was recorded.
        @param Transactions: All transactions recorded for this receipted payment.
        @param line: Receipted amount with rounding, date and note.
        """
        #: True if this receipted payment is manually bankable, otherwise it is an electronic funds transfer.
        self.isBankable = isBankable

        self._CashierShift = None
        self.CashierShift = CashierShift

        self._Tenders = []
        self.Tenders = [] if Tenders is None else Tenders

        self._VendorShift = None
        self.VendorShift = VendorShift

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        self.line = line

        super(Receipt, self).__init__(*args, **kw_args)

    _attrs = ["isBankable"]
    _attr_types = {"isBankable": bool}
    _defaults = {"isBankable": False}
    _enums = {}
    _refs = ["CashierShift", "Tenders", "VendorShift", "Transactions", "line"]
    _many_refs = ["Tenders", "Transactions"]

    def getCashierShift(self):
        """Cashier shift during which this receipt was recorded.
        """
        return self._CashierShift

    def setCashierShift(self, value):
        if self._CashierShift is not None:
            filtered = [x for x in self.CashierShift.Receipts if x != self]
            self._CashierShift._Receipts = filtered

        self._CashierShift = value
        if self._CashierShift is not None:
            if self not in self._CashierShift._Receipts:
                self._CashierShift._Receipts.append(self)

    CashierShift = property(getCashierShift, setCashierShift)

    def getTenders(self):
        """All payments received in the form of tenders recorded by this receipt.
        """
        return self._Tenders

    def setTenders(self, value):
        for x in self._Tenders:
            x.Receipt = None
        for y in value:
            y._Receipt = self
        self._Tenders = value

    Tenders = property(getTenders, setTenders)

    def addTenders(self, *Tenders):
        for obj in Tenders:
            obj.Receipt = self

    def removeTenders(self, *Tenders):
        for obj in Tenders:
            obj.Receipt = None

    def getVendorShift(self):
        """Vendor shift during which this receipt was recorded.
        """
        return self._VendorShift

    def setVendorShift(self, value):
        if self._VendorShift is not None:
            filtered = [x for x in self.VendorShift.Receipts if x != self]
            self._VendorShift._Receipts = filtered

        self._VendorShift = value
        if self._VendorShift is not None:
            if self not in self._VendorShift._Receipts:
                self._VendorShift._Receipts.append(self)

    VendorShift = property(getVendorShift, setVendorShift)

    def getTransactions(self):
        """All transactions recorded for this receipted payment.
        """
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x.Receipt = None
        for y in value:
            y._Receipt = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj.Receipt = self

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj.Receipt = None

    # Receipted amount with rounding, date and note.
    line = None

