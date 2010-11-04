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

from CIM14v13.IEC61968.Informative.EnergyScheduling.Profile import Profile

class EnergyProfile(Profile):
    """Specifies the start time, stop time, level for an EnergyTransaction.
    """

    def __init__(self, TransactionBid=None, EnergyTransaction=None, **kw_args):
        """Initializes a new 'EnergyProfile' instance.

        @param TransactionBid:
        @param EnergyTransaction: An EnergyTransaction must have at least one EnergyProfile.
        """
        self._TransactionBid = None
        self.TransactionBid = TransactionBid

        self._EnergyTransaction = None
        self.EnergyTransaction = EnergyTransaction

        super(EnergyProfile, self).__init__(**kw_args)

    def getTransactionBid(self):
        
        return self._TransactionBid

    def setTransactionBid(self, value):
        if self._TransactionBid is not None:
            filtered = [x for x in self.TransactionBid.EnergyProfiles if x != self]
            self._TransactionBid._EnergyProfiles = filtered

        self._TransactionBid = value
        if self._TransactionBid is not None:
            self._TransactionBid._EnergyProfiles.append(self)

    TransactionBid = property(getTransactionBid, setTransactionBid)

    def getEnergyTransaction(self):
        """An EnergyTransaction must have at least one EnergyProfile.
        """
        return self._EnergyTransaction

    def setEnergyTransaction(self, value):
        if self._EnergyTransaction is not None:
            filtered = [x for x in self.EnergyTransaction.EnergyProfiles if x != self]
            self._EnergyTransaction._EnergyProfiles = filtered

        self._EnergyTransaction = value
        if self._EnergyTransaction is not None:
            self._EnergyTransaction._EnergyProfiles.append(self)

    EnergyTransaction = property(getEnergyTransaction, setEnergyTransaction)

