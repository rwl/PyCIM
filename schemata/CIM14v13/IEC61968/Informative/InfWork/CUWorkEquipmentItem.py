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

class CUWorkEquipmentItem(IdentifiedObject):
    """Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    """

    def __init__(self, equipCode='', rate=0.0, CompatibleUnits=None, TypeAsset=None, status=None, *args, **kw_args):
        """Initializes a new 'CUWorkEquipmentItem' instance.

        @param equipCode: The equipment type code. 
        @param rate: Standard usage rate for the type of vehicle. 
        @param CompatibleUnits:
        @param TypeAsset:
        @param status:
        """
        #: The equipment type code.
        self.equipCode = equipCode

        #: Standard usage rate for the type of vehicle.
        self.rate = rate

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        self.status = status

        super(CUWorkEquipmentItem, self).__init__(*args, **kw_args)

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.CUWorkEquipmentItems if q != self]
            self._CompatibleUnits._CUWorkEquipmentItems = filtered
        for r in value:
            if self not in r._CUWorkEquipmentItems:
                r._CUWorkEquipmentItems.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._CUWorkEquipmentItems:
                obj._CUWorkEquipmentItems.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._CUWorkEquipmentItems:
                obj._CUWorkEquipmentItems.remove(self)
            self._CompatibleUnits.remove(obj)

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            self._TypeAsset._CUWorkEquipmentAsset = None

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset._CUWorkEquipmentAsset = self

    TypeAsset = property(getTypeAsset, setTypeAsset)

    status = None

