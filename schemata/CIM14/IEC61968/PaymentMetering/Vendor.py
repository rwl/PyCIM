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

class Vendor(IdentifiedObject):
    """The entity that owns PointOfSale and contracts with Cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by Merchant who is a type of Organisation. Vendor is accountable to Merchant for revenue collected, who is in turn accountable to Supplier.
    """

    def __init__(self, PointOfSales=None, MerchantAccount=None, Cashiers=None, VendorShifts=None, **kw_args):
        """Initializes a new 'Vendor' instance.

        @param PointOfSales: All points of sale this Vendor controls.
        @param MerchantAccount: Merchant account against which this vendor sells tokens or recept payments.
        @param Cashiers: All Cachiers managed by this Vendor.
        @param VendorShifts: All vendor shifts opened and owned by this vendor.
        """
        self._PointOfSales = []
        self.PointOfSales = [] if PointOfSales is None else PointOfSales

        self._MerchantAccount = None
        self.MerchantAccount = MerchantAccount

        self._Cashiers = []
        self.Cashiers = [] if Cashiers is None else Cashiers

        self._VendorShifts = []
        self.VendorShifts = [] if VendorShifts is None else VendorShifts

        super(Vendor, self).__init__(**kw_args)

    def getPointOfSales(self):
        """All points of sale this Vendor controls.
        """
        return self._PointOfSales

    def setPointOfSales(self, value):
        for x in self._PointOfSales:
            x._Vendor = None
        for y in value:
            y._Vendor = self
        self._PointOfSales = value

    PointOfSales = property(getPointOfSales, setPointOfSales)

    def addPointOfSales(self, *PointOfSales):
        for obj in PointOfSales:
            obj._Vendor = self
            self._PointOfSales.append(obj)

    def removePointOfSales(self, *PointOfSales):
        for obj in PointOfSales:
            obj._Vendor = None
            self._PointOfSales.remove(obj)

    def getMerchantAccount(self):
        """Merchant account against which this vendor sells tokens or recept payments.
        """
        return self._MerchantAccount

    def setMerchantAccount(self, value):
        if self._MerchantAccount is not None:
            filtered = [x for x in self.MerchantAccount.Vendors if x != self]
            self._MerchantAccount._Vendors = filtered

        self._MerchantAccount = value
        if self._MerchantAccount is not None:
            self._MerchantAccount._Vendors.append(self)

    MerchantAccount = property(getMerchantAccount, setMerchantAccount)

    def getCashiers(self):
        """All Cachiers managed by this Vendor.
        """
        return self._Cashiers

    def setCashiers(self, value):
        for x in self._Cashiers:
            x._Vendor = None
        for y in value:
            y._Vendor = self
        self._Cashiers = value

    Cashiers = property(getCashiers, setCashiers)

    def addCashiers(self, *Cashiers):
        for obj in Cashiers:
            obj._Vendor = self
            self._Cashiers.append(obj)

    def removeCashiers(self, *Cashiers):
        for obj in Cashiers:
            obj._Vendor = None
            self._Cashiers.remove(obj)

    def getVendorShifts(self):
        """All vendor shifts opened and owned by this vendor.
        """
        return self._VendorShifts

    def setVendorShifts(self, value):
        for x in self._VendorShifts:
            x._Vendor = None
        for y in value:
            y._Vendor = self
        self._VendorShifts = value

    VendorShifts = property(getVendorShifts, setVendorShifts)

    def addVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj._Vendor = self
            self._VendorShifts.append(obj)

    def removeVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj._Vendor = None
            self._VendorShifts.remove(obj)

