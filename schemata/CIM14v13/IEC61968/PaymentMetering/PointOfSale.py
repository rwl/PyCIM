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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class PointOfSale(IdentifiedObject):
    """Logical point where transactions take place with operational interaction between Cashier and the payment system; in certain cases PointOfSale interacts directly with the end customer, in which case Cashier might not be a real person: for example a self-service kiosk or over the internet.
    """

    def __init__(self, location='', Vendor=None, Tokens=None, CashierShifts=None, *args, **kw_args):
        """Initializes a new 'PointOfSale' instance.

        @param location: Local description for where this point of sale is physically located. 
        @param Vendor: Vendor that controls this PointOfSale.
        @param Tokens: All Tokens sold or dispensed at this PointOfSale.
        @param CashierShifts: All shifts this point of sale operated in.
        """
        #: Local description for where this point of sale is physically located.
        self.location = location

        self._Vendor = None
        self.Vendor = Vendor

        self._Tokens = []
        self.Tokens = [] if Tokens is None else Tokens

        self._CashierShifts = []
        self.CashierShifts = [] if CashierShifts is None else CashierShifts

        super(PointOfSale, self).__init__(*args, **kw_args)

    def getVendor(self):
        """Vendor that controls this PointOfSale.
        """
        return self._Vendor

    def setVendor(self, value):
        if self._Vendor is not None:
            filtered = [x for x in self.Vendor.PointOfSales if x != self]
            self._Vendor._PointOfSales = filtered

        self._Vendor = value
        if self._Vendor is not None:
            self._Vendor._PointOfSales.append(self)

    Vendor = property(getVendor, setVendor)

    def getTokens(self):
        """All Tokens sold or dispensed at this PointOfSale.
        """
        return self._Tokens

    def setTokens(self, value):
        for x in self._Tokens:
            x._PointOfSale = None
        for y in value:
            y._PointOfSale = self
        self._Tokens = value

    Tokens = property(getTokens, setTokens)

    def addTokens(self, *Tokens):
        for obj in Tokens:
            obj._PointOfSale = self
            self._Tokens.append(obj)

    def removeTokens(self, *Tokens):
        for obj in Tokens:
            obj._PointOfSale = None
            self._Tokens.remove(obj)

    def getCashierShifts(self):
        """All shifts this point of sale operated in.
        """
        return self._CashierShifts

    def setCashierShifts(self, value):
        for x in self._CashierShifts:
            x._PointOfSale = None
        for y in value:
            y._PointOfSale = self
        self._CashierShifts = value

    CashierShifts = property(getCashierShifts, setCashierShifts)

    def addCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj._PointOfSale = self
            self._CashierShifts.append(obj)

    def removeCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj._PointOfSale = None
            self._CashierShifts.remove(obj)

