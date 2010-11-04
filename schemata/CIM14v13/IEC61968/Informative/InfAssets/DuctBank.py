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

from CIM14v13.IEC61968.Assets.Asset import Asset

class DuctBank(Asset):
    """A duct bank may contain many ducts. Each duct contains individual lines that are expressed as conductor assets (thereby describing each line's physical asset characteristics), which are each associated with ACLineSegments and other classes describing their electrical characteristics.
    """

    def __init__(self, circuitCount=0, ductCount=0, CableAssets=None, DuctBankTypeAsset=None, *args, **kw_args):
        """Initializes a new 'DuctBank' instance.

        @param circuitCount: Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts. 
        @param ductCount: Number of ducts in duct bank. 
        @param CableAssets:
        @param DuctBankTypeAsset:
        """
        #: Number of circuits in duct bank. Refer to associations between a duct (ConductorAsset) and an ACLineSegment to understand which circuits are in which ducts.
        self.circuitCount = circuitCount

        #: Number of ducts in duct bank.
        self.ductCount = ductCount

        self._CableAssets = []
        self.CableAssets = [] if CableAssets is None else CableAssets

        self._DuctBankTypeAsset = None
        self.DuctBankTypeAsset = DuctBankTypeAsset

        super(DuctBank, self).__init__(*args, **kw_args)

    def getCableAssets(self):
        
        return self._CableAssets

    def setCableAssets(self, value):
        for p in self._CableAssets:
            filtered = [q for q in p.DuctBanks if q != self]
            self._CableAssets._DuctBanks = filtered
        for r in value:
            if self not in r._DuctBanks:
                r._DuctBanks.append(self)
        self._CableAssets = value

    CableAssets = property(getCableAssets, setCableAssets)

    def addCableAssets(self, *CableAssets):
        for obj in CableAssets:
            if self not in obj._DuctBanks:
                obj._DuctBanks.append(self)
            self._CableAssets.append(obj)

    def removeCableAssets(self, *CableAssets):
        for obj in CableAssets:
            if self in obj._DuctBanks:
                obj._DuctBanks.remove(self)
            self._CableAssets.remove(obj)

    def getDuctBankTypeAsset(self):
        
        return self._DuctBankTypeAsset

    def setDuctBankTypeAsset(self, value):
        if self._DuctBankTypeAsset is not None:
            filtered = [x for x in self.DuctBankTypeAsset.DuctBanks if x != self]
            self._DuctBankTypeAsset._DuctBanks = filtered

        self._DuctBankTypeAsset = value
        if self._DuctBankTypeAsset is not None:
            self._DuctBankTypeAsset._DuctBanks.append(self)

    DuctBankTypeAsset = property(getDuctBankTypeAsset, setDuctBankTypeAsset)

