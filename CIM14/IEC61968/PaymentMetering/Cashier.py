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

class Cashier(IdentifiedObject):
    """The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.
    """

    def __init__(self, CashierShifts=None, electronicAddress=None, Vendor=None, *args, **kw_args):
        """Initialises a new 'Cashier' instance.

        @param CashierShifts: All shifts operated by this cashier.
        @param electronicAddress: Electronic address.
        @param Vendor: Vendor that manages this Cachier.
        """
        self._CashierShifts = []
        self.CashierShifts = [] if CashierShifts is None else CashierShifts

        self.electronicAddress = electronicAddress

        self._Vendor = None
        self.Vendor = Vendor

        super(Cashier, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["CashierShifts", "electronicAddress", "Vendor"]
    _many_refs = ["CashierShifts"]

    def getCashierShifts(self):
        """All shifts operated by this cashier.
        """
        return self._CashierShifts

    def setCashierShifts(self, value):
        for x in self._CashierShifts:
            x.Cashier = None
        for y in value:
            y._Cashier = self
        self._CashierShifts = value

    CashierShifts = property(getCashierShifts, setCashierShifts)

    def addCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj.Cashier = self

    def removeCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj.Cashier = None

    # Electronic address.
    electronicAddress = None

    def getVendor(self):
        """Vendor that manages this Cachier.
        """
        return self._Vendor

    def setVendor(self, value):
        if self._Vendor is not None:
            filtered = [x for x in self.Vendor.Cashiers if x != self]
            self._Vendor._Cashiers = filtered

        self._Vendor = value
        if self._Vendor is not None:
            if self not in self._Vendor._Cashiers:
                self._Vendor._Cashiers.append(self)

    Vendor = property(getVendor, setVendor)

