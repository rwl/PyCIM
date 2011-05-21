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

