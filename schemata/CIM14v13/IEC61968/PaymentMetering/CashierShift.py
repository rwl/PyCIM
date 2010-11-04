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

from CIM14v13.IEC61968.PaymentMetering.Shift import Shift

class CashierShift(Shift):
    """The operating shift for a cashier, during which he may transact against the CashierShift, subject to VendorShift being open.
    """

    def __init__(self, cashFloat=0.0, Cashier=None, Receipts=None, PointOfSale=None, Transactions=None, **kw_args):
        """Initializes a new 'CashierShift' instance.

        @param cashFloat: The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked. 
        @param Cashier: Cashier operating this shift.
        @param Receipts: All Receipts recorded for this Shift.
        @param PointOfSale: Point of sale that is in operation during this shift.
        @param Transactions:
        """
        #: The amount of cash that the cashier brings with him to start his shift and that he will take away at the end of his shift; i.e. the cash float does not get banked.
        self.cashFloat = cashFloat

        self._Cashier = None
        self.Cashier = Cashier

        self._Receipts = []
        self.Receipts = [] if Receipts is None else Receipts

        self._PointOfSale = None
        self.PointOfSale = PointOfSale

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        super(CashierShift, self).__init__(**kw_args)

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
            self._Cashier._CashierShifts.append(self)

    Cashier = property(getCashier, setCashier)

    def getReceipts(self):
        """All Receipts recorded for this Shift.
        """
        return self._Receipts

    def setReceipts(self, value):
        for x in self._Receipts:
            x._CashierShift = None
        for y in value:
            y._CashierShift = self
        self._Receipts = value

    Receipts = property(getReceipts, setReceipts)

    def addReceipts(self, *Receipts):
        for obj in Receipts:
            obj._CashierShift = self
            self._Receipts.append(obj)

    def removeReceipts(self, *Receipts):
        for obj in Receipts:
            obj._CashierShift = None
            self._Receipts.remove(obj)

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
            self._PointOfSale._CashierShifts.append(self)

    PointOfSale = property(getPointOfSale, setPointOfSale)

    def getTransactions(self):
        
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x._CashierShift = None
        for y in value:
            y._CashierShift = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj._CashierShift = self
            self._Transactions.append(obj)

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj._CashierShift = None
            self._Transactions.remove(obj)

