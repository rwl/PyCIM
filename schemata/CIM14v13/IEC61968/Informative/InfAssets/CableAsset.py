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

from CIM14v13.IEC61968.Informative.InfAssets.ConductorAsset import ConductorAsset

class CableAsset(ConductorAsset):
    """Insultated physical cable for performing the Conductor role used in undergrond and other applications..
    """

    def __init__(self, DuctBanks=None, DuctBankTypeAsset=None, **kw_args):
        """Initializes a new 'CableAsset' instance.

        @param DuctBanks:
        @param DuctBankTypeAsset:
        """
        self._DuctBanks = []
        self.DuctBanks = [] if DuctBanks is None else DuctBanks

        self._DuctBankTypeAsset = None
        self.DuctBankTypeAsset = DuctBankTypeAsset

        super(CableAsset, self).__init__(**kw_args)

    def getDuctBanks(self):
        
        return self._DuctBanks

    def setDuctBanks(self, value):
        for p in self._DuctBanks:
            filtered = [q for q in p.CableAssets if q != self]
            self._DuctBanks._CableAssets = filtered
        for r in value:
            if self not in r._CableAssets:
                r._CableAssets.append(self)
        self._DuctBanks = value

    DuctBanks = property(getDuctBanks, setDuctBanks)

    def addDuctBanks(self, *DuctBanks):
        for obj in DuctBanks:
            if self not in obj._CableAssets:
                obj._CableAssets.append(self)
            self._DuctBanks.append(obj)

    def removeDuctBanks(self, *DuctBanks):
        for obj in DuctBanks:
            if self in obj._CableAssets:
                obj._CableAssets.remove(self)
            self._DuctBanks.remove(obj)

    def getDuctBankTypeAsset(self):
        
        return self._DuctBankTypeAsset

    def setDuctBankTypeAsset(self, value):
        if self._DuctBankTypeAsset is not None:
            filtered = [x for x in self.DuctBankTypeAsset.CableAssets if x != self]
            self._DuctBankTypeAsset._CableAssets = filtered

        self._DuctBankTypeAsset = value
        if self._DuctBankTypeAsset is not None:
            self._DuctBankTypeAsset._CableAssets.append(self)

    DuctBankTypeAsset = property(getDuctBankTypeAsset, setDuctBankTypeAsset)

