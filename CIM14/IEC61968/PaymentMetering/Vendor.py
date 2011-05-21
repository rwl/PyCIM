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

class Vendor(IdentifiedObject):
    """The entity that owns PointOfSale and contracts with Cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by Merchant who is a type of Organisation. Vendor is accountable to Merchant for revenue collected, who is in turn accountable to Supplier.
    """

    def __init__(self, PointOfSales=None, MerchantAccount=None, Cashiers=None, VendorShifts=None, *args, **kw_args):
        """Initialises a new 'Vendor' instance.

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

        super(Vendor, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PointOfSales", "MerchantAccount", "Cashiers", "VendorShifts"]
    _many_refs = ["PointOfSales", "Cashiers", "VendorShifts"]

    def getPointOfSales(self):
        """All points of sale this Vendor controls.
        """
        return self._PointOfSales

    def setPointOfSales(self, value):
        for x in self._PointOfSales:
            x.Vendor = None
        for y in value:
            y._Vendor = self
        self._PointOfSales = value

    PointOfSales = property(getPointOfSales, setPointOfSales)

    def addPointOfSales(self, *PointOfSales):
        for obj in PointOfSales:
            obj.Vendor = self

    def removePointOfSales(self, *PointOfSales):
        for obj in PointOfSales:
            obj.Vendor = None

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
            if self not in self._MerchantAccount._Vendors:
                self._MerchantAccount._Vendors.append(self)

    MerchantAccount = property(getMerchantAccount, setMerchantAccount)

    def getCashiers(self):
        """All Cachiers managed by this Vendor.
        """
        return self._Cashiers

    def setCashiers(self, value):
        for x in self._Cashiers:
            x.Vendor = None
        for y in value:
            y._Vendor = self
        self._Cashiers = value

    Cashiers = property(getCashiers, setCashiers)

    def addCashiers(self, *Cashiers):
        for obj in Cashiers:
            obj.Vendor = self

    def removeCashiers(self, *Cashiers):
        for obj in Cashiers:
            obj.Vendor = None

    def getVendorShifts(self):
        """All vendor shifts opened and owned by this vendor.
        """
        return self._VendorShifts

    def setVendorShifts(self, value):
        for x in self._VendorShifts:
            x.Vendor = None
        for y in value:
            y._Vendor = self
        self._VendorShifts = value

    VendorShifts = property(getVendorShifts, setVendorShifts)

    def addVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj.Vendor = self

    def removeVendorShifts(self, *VendorShifts):
        for obj in VendorShifts:
            obj.Vendor = None

