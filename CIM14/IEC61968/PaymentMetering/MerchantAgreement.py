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
            x._MerchantAgreement = None
        for y in value:
            y._MerchantAgreement = self
        self._MerchantAccounts = value

    MerchantAccounts = property(getMerchantAccounts, setMerchantAccounts)

    def addMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            obj._MerchantAgreement = self
            self._MerchantAccounts.append(obj)

    def removeMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            obj._MerchantAgreement = None
            self._MerchantAccounts.remove(obj)

