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

class Transactor(IdentifiedObject):
    """The entity that ultimately executes the transaction and who is in control of the process; typically this is embodied in secure software running on a server that may employ secure hardware encryption devices for secure transaction processing.
    """

    def __init__(self, MerchantAccounts=None, **kw_args):
        """Initializes a new 'Transactor' instance.

        @param MerchantAccounts: All merchant accounts registered with this transactor.
        """
        self._MerchantAccounts = []
        self.MerchantAccounts = [] if MerchantAccounts is None else MerchantAccounts

        super(Transactor, self).__init__(**kw_args)

    def getMerchantAccounts(self):
        """All merchant accounts registered with this transactor.
        """
        return self._MerchantAccounts

    def setMerchantAccounts(self, value):
        for p in self._MerchantAccounts:
            filtered = [q for q in p.Transactors if q != self]
            self._MerchantAccounts._Transactors = filtered
        for r in value:
            if self not in r._Transactors:
                r._Transactors.append(self)
        self._MerchantAccounts = value

    MerchantAccounts = property(getMerchantAccounts, setMerchantAccounts)

    def addMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            if self not in obj._Transactors:
                obj._Transactors.append(self)
            self._MerchantAccounts.append(obj)

    def removeMerchantAccounts(self, *MerchantAccounts):
        for obj in MerchantAccounts:
            if self in obj._Transactors:
                obj._Transactors.remove(self)
            self._MerchantAccounts.remove(obj)

