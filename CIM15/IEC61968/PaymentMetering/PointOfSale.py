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

class PointOfSale(IdentifiedObject):
    """Logical point where transactions take place with operational interaction between cashier and the payment system; in certain cases point of sale interacts directly with the end customer, in which case cashier might not be a real person: for example a self-service kiosk or over the internet.Logical point where transactions take place with operational interaction between cashier and the payment system; in certain cases point of sale interacts directly with the end customer, in which case cashier might not be a real person: for example a self-service kiosk or over the internet.
    """

    def __init__(self, location='', CashierShifts=None, *args, **kw_args):
        """Initialises a new 'PointOfSale' instance.

        @param location: Local description for where this point of sale is physically located. 
        @param CashierShifts: All shifts this point of sale operated in.
        """
        #: Local description for where this point of sale is physically located.
        self.location = location

        self._CashierShifts = []
        self.CashierShifts = [] if CashierShifts is None else CashierShifts

        super(PointOfSale, self).__init__(*args, **kw_args)

    _attrs = ["location"]
    _attr_types = {"location": str}
    _defaults = {"location": ''}
    _enums = {}
    _refs = ["CashierShifts"]
    _many_refs = ["CashierShifts"]

    def getCashierShifts(self):
        """All shifts this point of sale operated in.
        """
        return self._CashierShifts

    def setCashierShifts(self, value):
        for x in self._CashierShifts:
            x.PointOfSale = None
        for y in value:
            y._PointOfSale = self
        self._CashierShifts = value

    CashierShifts = property(getCashierShifts, setCashierShifts)

    def addCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj.PointOfSale = self

    def removeCashierShifts(self, *CashierShifts):
        for obj in CashierShifts:
            obj.PointOfSale = None

