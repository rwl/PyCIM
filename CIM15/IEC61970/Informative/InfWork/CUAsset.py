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

class CUAsset(IdentifiedObject):
    """Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..Compatible unit for various types of assets such as transformers switches, substation fences, poles, etc..
    """

    def __init__(self, quantity="", typeAssetCode='', CompatibleUnits=None, TypeAsset=None, status=None, *args, **kw_args):
        """Initialises a new 'CUAsset' instance.

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

    _attrs = ["quantity", "typeAssetCode"]
    _attr_types = {"quantity": str, "typeAssetCode": str}
    _defaults = {"quantity": "", "typeAssetCode": ''}
    _enums = {}
    _refs = ["CompatibleUnits", "TypeAsset", "status"]
    _many_refs = ["CompatibleUnits"]

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
            self._TypeAsset.CUAsset = None
            self._TypeAsset._CUAsset = self

    TypeAsset = property(getTypeAsset, setTypeAsset)

    status = None

