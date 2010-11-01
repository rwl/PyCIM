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

class LossProfile(Profile):
    """LossProfile is associated with an EnerrgyTransaction and must be completely contained within the time frame of the EnergyProfile associated with this EnergyTransaction.
    """

    def __init__(self, EnergyTransaction=None, HasLoss_=None, *args, **kw_args):
        """Initializes a new 'LossProfile' instance.

        @param EnergyTransaction: An EnergyTransaction may have a LossProfile.
        @param HasLoss_: Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
        """
        self._EnergyTransaction = None
        self.EnergyTransaction = EnergyTransaction

        self._HasLoss_ = None
        self.HasLoss_ = HasLoss_

        super(LossProfile, self).__init__(*args, **kw_args)

    def getEnergyTransaction(self):
        """An EnergyTransaction may have a LossProfile.
        """
        return self._EnergyTransaction

    def setEnergyTransaction(self, value):
        if self._EnergyTransaction is not None:
            filtered = [x for x in self.EnergyTransaction.LossProfiles if x != self]
            self._EnergyTransaction._LossProfiles = filtered

        self._EnergyTransaction = value
        if self._EnergyTransaction is not None:
            self._EnergyTransaction._LossProfiles.append(self)

    EnergyTransaction = property(getEnergyTransaction, setEnergyTransaction)

    def getHasLoss_(self):
        """Part of the LossProfile for an EnergyTransaction may be a loss for a TransmissionProvider.
        """
        return self._HasLoss_

    def setHasLoss_(self, value):
        if self._HasLoss_ is not None:
            filtered = [x for x in self.HasLoss_.For if x != self]
            self._HasLoss_._For = filtered

        self._HasLoss_ = value
        if self._HasLoss_ is not None:
            self._HasLoss_._For.append(self)

    HasLoss_ = property(getHasLoss_, setHasLoss_)

