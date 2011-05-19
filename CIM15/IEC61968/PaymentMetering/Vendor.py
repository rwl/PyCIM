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

class Vendor(IdentifiedObject):
    """The entity that owns point of sale and contracts with cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by merchant who is a type of organisation. Vendor is accountable to merchant for revenue collected, who is in turn accountable to supplier.The entity that owns point of sale and contracts with cashier to receipt payments and vend tokens using the payment system. Vendor has a private contract with and is managed by merchant who is a type of organisation. Vendor is accountable to merchant for revenue collected, who is in turn accountable to supplier.
    """

    def __init__(self, VendorShifts=None, *args, **kw_args):
        """Initialises a new 'Vendor' instance.

        @param VendorShifts: All vendor shifts opened and owned by this vendor.
        """
        self._VendorShifts = []
        self.VendorShifts = [] if VendorShifts is None else VendorShifts

        super(Vendor, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["VendorShifts"]
    _many_refs = ["VendorShifts"]

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

