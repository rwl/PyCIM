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
            self._CashierShift._Receipts.append(self)

    CashierShift = property(getCashierShift, setCashierShift)

    def getTenders(self):
        """All payments received in the form of tenders recorded by this receipt.
        """
        return self._Tenders

    def setTenders(self, value):
        for x in self._Tenders:
            x._Receipt = None
        for y in value:
            y._Receipt = self
        self._Tenders = value

    Tenders = property(getTenders, setTenders)

    def addTenders(self, *Tenders):
        for obj in Tenders:
            obj._Receipt = self
            self._Tenders.append(obj)

    def removeTenders(self, *Tenders):
        for obj in Tenders:
            obj._Receipt = None
            self._Tenders.remove(obj)

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
            self._VendorShift._Receipts.append(self)

    VendorShift = property(getVendorShift, setVendorShift)

    def getTransactions(self):
        """All transactions recorded for this receipted payment.
        """
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x._Receipt = None
        for y in value:
            y._Receipt = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj._Receipt = self
            self._Transactions.append(obj)

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj._Receipt = None
            self._Transactions.remove(obj)

    # Receipted amount with rounding, date and note.
    line = None

