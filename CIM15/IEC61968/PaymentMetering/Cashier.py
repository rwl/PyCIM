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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Cashier(IdentifiedObject):
    """The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.The operator of the point of sale for the duration of CashierShift. Cashier is under the exclusive management control of Vendor.
    """

    def __init__(self, electronicAddress=None, CashierShifts=None, *args, **kw_args):
        """Initialises a new 'Cashier' instance.

        @param electronicAddress: Electronic address.
        @param CashierShifts: All shifts operated by this cashier.
        """
        self.electronicAddress = electronicAddress

        self._CashierShifts = []
        self.CashierShifts = [] if CashierShifts is None else CashierShifts

        super(Cashier, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["electronicAddress", "CashierShifts"]
    _many_refs = ["CashierShifts"]

    # Electronic address.
    electronicAddress = None

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

