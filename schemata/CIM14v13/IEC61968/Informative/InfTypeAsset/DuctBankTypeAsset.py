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

from CIM14v13.IEC61968.Informative.InfTypeAsset.StructureTypeAsset import StructureTypeAsset

class DuctBankTypeAsset(StructureTypeAsset):
    """A DuctBank contains multiple Ducts. The DuctBank itself should have no connections, since these are defined by the individual ducts within it. However, it will have a ConstructionType and the material it is constructed from.
    """

    def __init__(self, DuctTypeAssets=None, DuctBanks=None, **kw_args):
        """Initializes a new 'DuctBankTypeAsset' instance.

        @param DuctTypeAssets:
        @param DuctBanks:
        """
        self._DuctTypeAssets = []
        self.DuctTypeAssets = [] if DuctTypeAssets is None else DuctTypeAssets

        self._DuctBanks = []
        self.DuctBanks = [] if DuctBanks is None else DuctBanks

        super(DuctBankTypeAsset, self).__init__(**kw_args)

    def getDuctTypeAssets(self):
        
        return self._DuctTypeAssets

    def setDuctTypeAssets(self, value):
        for x in self._DuctTypeAssets:
            x._DuctBankTypeAsset = None
        for y in value:
            y._DuctBankTypeAsset = self
        self._DuctTypeAssets = value

    DuctTypeAssets = property(getDuctTypeAssets, setDuctTypeAssets)

    def addDuctTypeAssets(self, *DuctTypeAssets):
        for obj in DuctTypeAssets:
            obj._DuctBankTypeAsset = self
            self._DuctTypeAssets.append(obj)

    def removeDuctTypeAssets(self, *DuctTypeAssets):
        for obj in DuctTypeAssets:
            obj._DuctBankTypeAsset = None
            self._DuctTypeAssets.remove(obj)

    def getDuctBanks(self):
        
        return self._DuctBanks

    def setDuctBanks(self, value):
        for x in self._DuctBanks:
            x._DuctBankTypeAsset = None
        for y in value:
            y._DuctBankTypeAsset = self
        self._DuctBanks = value

    DuctBanks = property(getDuctBanks, setDuctBanks)

    def addDuctBanks(self, *DuctBanks):
        for obj in DuctBanks:
            obj._DuctBankTypeAsset = self
            self._DuctBanks.append(obj)

    def removeDuctBanks(self, *DuctBanks):
        for obj in DuctBanks:
            obj._DuctBankTypeAsset = None
            self._DuctBanks.remove(obj)

