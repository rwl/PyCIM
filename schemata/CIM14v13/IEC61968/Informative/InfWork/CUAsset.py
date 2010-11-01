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

class CUAsset(IdentifiedObject):
    """Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..
    """

    def __init__(self, quantity=0, typeAssetCode='', CompatibleUnits=None, TypeAsset=None, status=None, *args, **kw_args):
        """Initializes a new 'CUAsset' instance.

        @param quantity: Quantity of the type asset within the CU. 
        @param typeAssetCode: The code for this type of asset. 
        @param CompatibleUnits:
        @param TypeAsset:
        @param status:
        """
        #: Quantity of the type asset within the CU. 
        self.quantity = quantity

        #: The code for this type of asset. 
        self.typeAssetCode = typeAssetCode

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        self.status = status

        super(CUAsset, self).__init__(*args, **kw_args)

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.CUAssets if q != self]
            self._CompatibleUnits._CUAssets = filtered
        for r in value:
            if self not in r._CUAssets:
                r._CUAssets.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._CUAssets:
                obj._CUAssets.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._CUAssets:
                obj._CUAssets.remove(self)
            self._CompatibleUnits.remove(obj)

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            self._TypeAsset._CUAsset = None

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset._CUAsset = self

    TypeAsset = property(getTypeAsset, setTypeAsset)

    status = None

