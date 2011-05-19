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

from CIM15.IEC61968.PaymentMetering.Shift import Shift

class CashierShift(Shift):
    """The operating shift for a cashier, during which he may transact against the cashier shift, subject to vendor shift being open.The operating shift for a cashier, during which he may transact against the cashier shift, subject to vendor shift being open.
    """

    def __init__(self, cashFloat=0.0, Transactions=None, PointOfSale=None, Receipts=None, Cashier=None, *args, **kw_args):
        """Initialises a new 'CashierShift' instance.

        @param cashFloat: The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked. 
        @param Transactions:
        @param PointOfSale: Point of sale that is in operation during this shift.
        @param Receipts: All Receipts recorded for this Shift.
        @param Cashier: Cashier operating this shift.
        """
        #: The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked.
        self.cashFloat = cashFloat

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        self._PointOfSale = None
        self.PointOfSale = PointOfSale

        self._Receipts = []
        self.Receipts = [] if Receipts is None else Receipts

        self._Cashier = None
        self.Cashier = Cashier

        super(CashierShift, self).__init__(*args, **kw_args)

    _attrs = ["cashFloat"]
    _attr_types = {"cashFloat": float}
    _defaults = {"cashFloat": 0.0}
    _enums = {}
    _refs = ["Transactions", "PointOfSale", "Receipts", "Cashier"]
    _many_refs = ["Transactions", "Receipts"]

    def getTransactions(self):
        
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x.CashierShift = None
        for y in value:
            y._CashierShift = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj.CashierShift = self

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj.CashierShift = None

    def getPointOfSale(self):
        """Point of sale that is in operation during this shift.
        """
        return self._PointOfSale

    def setPointOfSale(self, value):
        if self._PointOfSale is not None:
            filtered = [x for x in self.PointOfSale.CashierShifts if x != self]
            self._PointOfSale._CashierShifts = filtered

        self._PointOfSale = value
        if self._PointOfSale is not None:
            if self not in self._PointOfSale._CashierShifts:
                self._PointOfSale._CashierShifts.append(self)

    PointOfSale = property(getPointOfSale, setPointOfSale)

    def getReceipts(self):
        """All Receipts recorded for this Shift.
        """
        return self._Receipts

    def setReceipts(self, value):
        for x in self._Receipts:
            x.CashierShift = None
        for y in value:
            y._CashierShift = self
        self._Receipts = value

    Receipts = property(getReceipts, setReceipts)

    def addReceipts(self, *Receipts):
        for obj in Receipts:
            obj.CashierShift = self

    def removeReceipts(self, *Receipts):
        for obj in Receipts:
            obj.CashierShift = None

    def getCashier(self):
        """Cashier operating this shift.
        """
        return self._Cashier

    def setCashier(self, value):
        if self._Cashier is not None:
            filtered = [x for x in self.Cashier.CashierShifts if x != self]
            self._Cashier._CashierShifts = filtered

        self._Cashier = value
        if self._Cashier is not None:
            if self not in self._Cashier._CashierShifts:
                self._Cashier._CashierShifts.append(self)

    Cashier = property(getCashier, setCashier)

