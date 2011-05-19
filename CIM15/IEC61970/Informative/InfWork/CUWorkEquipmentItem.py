# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class CUWorkEquipmentItem(IdentifiedObject):
    """Compatible unit for various types of WorkEquipmentAssets, including vehicles.Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    """

    def __init__(self, rate=0.0, equipCode='', TypeAsset=None, status=None, CompatibleUnits=None, *args, **kw_args):
        """Initialises a new 'CUWorkEquipmentItem' instance.

        @param rate: Standard usage rate for the type of vehicle. 
        @param equipCode: The equipment type code. 
        @param TypeAsset:
        @param status:
        @param CompatibleUnits:
        """
        #: Standard usage rate for the type of vehicle.
        self.rate = rate

        #: The equipment type code.
        self.equipCode = equipCode

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        self.status = status

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        super(CUWorkEquipmentItem, self).__init__(*args, **kw_args)

    _attrs = ["rate", "equipCode"]
    _attr_types = {"rate": float, "equipCode": str}
    _defaults = {"rate": 0.0, "equipCode": ''}
    _enums = {}
    _refs = ["TypeAsset", "status", "CompatibleUnits"]
    _many_refs = ["CompatibleUnits"]

    def getTypeAsset(self):
        
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            self._TypeAsset._CUWorkEquipmentAsset = None

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset.CUWorkEquipmentAsset = None
            self._TypeAsset._CUWorkEquipmentAsset = self

    TypeAsset = property(getTypeAsset, setTypeAsset)

    status = None

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

