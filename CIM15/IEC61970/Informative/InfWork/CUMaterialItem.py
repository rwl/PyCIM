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

class CUMaterialItem(IdentifiedObject):
    """Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.
    """

    def __init__(self, quantity="", corporateCode='', status=None, PropertyUnits=None, CompatibleUnits=None, TypeMaterial=None, *args, **kw_args):
        """Initialises a new 'CUMaterialItem' instance.

        @param quantity: Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial. 
        @param corporateCode: Code for material. 
        @param status:
        @param PropertyUnits:
        @param CompatibleUnits:
        @param TypeMaterial:
        """
        #: Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial.
        self.quantity = quantity

        #: Code for material.
        self.corporateCode = corporateCode

        self.status = status

        self._PropertyUnits = []
        self.PropertyUnits = [] if PropertyUnits is None else PropertyUnits

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        super(CUMaterialItem, self).__init__(*args, **kw_args)

    _attrs = ["quantity", "corporateCode"]
    _attr_types = {"quantity": str, "corporateCode": str}
    _defaults = {"quantity": "", "corporateCode": ''}
    _enums = {}
    _refs = ["status", "PropertyUnits", "CompatibleUnits", "TypeMaterial"]
    _many_refs = ["PropertyUnits", "CompatibleUnits"]

    status = None

    def getPropertyUnits(self):
        
        return self._PropertyUnits

    def setPropertyUnits(self, value):
        for p in self._PropertyUnits:
            filtered = [q for q in p.CUMaterialItems if q != self]
            self._PropertyUnits._CUMaterialItems = filtered
        for r in value:
            if self not in r._CUMaterialItems:
                r._CUMaterialItems.append(self)
        self._PropertyUnits = value

    PropertyUnits = property(getPropertyUnits, setPropertyUnits)

    def addPropertyUnits(self, *PropertyUnits):
        for obj in PropertyUnits:
            if self not in obj._CUMaterialItems:
                obj._CUMaterialItems.append(self)
            self._PropertyUnits.append(obj)

    def removePropertyUnits(self, *PropertyUnits):
        for obj in PropertyUnits:
            if self in obj._CUMaterialItems:
                obj._CUMaterialItems.remove(self)
            self._PropertyUnits.remove(obj)

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for p in self._CompatibleUnits:
            filtered = [q for q in p.CUMaterialItems if q != self]
            self._CompatibleUnits._CUMaterialItems = filtered
        for r in value:
            if self not in r._CUMaterialItems:
                r._CUMaterialItems.append(self)
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self not in obj._CUMaterialItems:
                obj._CUMaterialItems.append(self)
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            if self in obj._CUMaterialItems:
                obj._CUMaterialItems.remove(self)
            self._CompatibleUnits.remove(obj)

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.CUMaterialItems if x != self]
            self._TypeMaterial._CUMaterialItems = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            if self not in self._TypeMaterial._CUMaterialItems:
                self._TypeMaterial._CUMaterialItems.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

