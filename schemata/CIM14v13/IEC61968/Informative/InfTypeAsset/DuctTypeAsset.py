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

class DuctTypeAsset(StructureTypeAsset):
    """A Duct contains underground cables and is contained within a duct bank. The xCoord and yCoord attributes define its positioning within the DuctBank.
    """

    def __init__(self, xCoord=0, yCoord=0, CableAssets=None, DuctBankTypeAsset=None, *args, **kw_args):
        """Initializes a new 'DuctTypeAsset' instance.

        @param xCoord: X position of the duct within the duct bank. 
        @param yCoord: Y position of the duct within the duct bank. 
        @param CableAssets:
        @param DuctBankTypeAsset:
        """
        #: X position of the duct within the duct bank.
        self.xCoord = xCoord

        #: Y position of the duct within the duct bank.
        self.yCoord = yCoord

        self._CableAssets = []
        self.CableAssets = [] if CableAssets is None else CableAssets

        self._DuctBankTypeAsset = None
        self.DuctBankTypeAsset = DuctBankTypeAsset

        super(DuctTypeAsset, self).__init__(*args, **kw_args)

    def getCableAssets(self):
        
        return self._CableAssets

    def setCableAssets(self, value):
        for x in self._CableAssets:
            x._DuctBankTypeAsset = None
        for y in value:
            y._DuctBankTypeAsset = self
        self._CableAssets = value

    CableAssets = property(getCableAssets, setCableAssets)

    def addCableAssets(self, *CableAssets):
        for obj in CableAssets:
            obj._DuctBankTypeAsset = self
            self._CableAssets.append(obj)

    def removeCableAssets(self, *CableAssets):
        for obj in CableAssets:
            obj._DuctBankTypeAsset = None
            self._CableAssets.remove(obj)

    def getDuctBankTypeAsset(self):
        
        return self._DuctBankTypeAsset

    def setDuctBankTypeAsset(self, value):
        if self._DuctBankTypeAsset is not None:
            filtered = [x for x in self.DuctBankTypeAsset.DuctTypeAssets if x != self]
            self._DuctBankTypeAsset._DuctTypeAssets = filtered

        self._DuctBankTypeAsset = value
        if self._DuctBankTypeAsset is not None:
            self._DuctBankTypeAsset._DuctTypeAssets.append(self)

    DuctBankTypeAsset = property(getDuctBankTypeAsset, setDuctBankTypeAsset)

