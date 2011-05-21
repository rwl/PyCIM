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

from CIM14.IEC61968.Common.Agreement import Agreement

class MerchantAgreement(Agreement):
    """A formal controlling contractual agreement between Supplier and Merchant, in terms of which Merchant is authorised to vend tokens and receipt payments on behalf of Supplier. Merchant is accountable to Supplier for revenue collected at PointOfSale.
    """

    def __init__(self, MerchantAccounts=None, *args, **kw_args):
        """Initialises a new 'MerchantAgreement' instance.

        @param MerchantAccounts: All merchant accounts instantiated as a result of this merchant agreement.
        """
        self._MerchantAccounts = []
        self.MerchantAccounts = [] if MerchantAccounts is None else MerchantAccounts

        super(MerchantAgreement, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MerchantAccounts"]
    _many_refs = ["MerchantAccounts"]

    def getMerchantAccounts(self):
        """All merchant accounts instantiated as a result of this merchant agreement.
        """
        return self._MerchantAccounts

    def setMerchantAccounts(self, value):
        for x in self._MerchantAccounts:
            x.MerchantAgreement = None
        for y in value:
            y._MerchantAgreement = self
        self._MerchantAccounts = value

    MerchantAccounts = property(getMerchantAccounts, setMerchantAccounts)

    def addMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            obj.MerchantAgreement = self

    def removeMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            obj.MerchantAgreement = None

