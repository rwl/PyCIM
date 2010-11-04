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

class CUMaterialItem(IdentifiedObject):
    """Compatible unit of a consumable supply item. For example, nuts, bolts, brackets, glue, etc.
    """

    def __init__(self, corporateCode='', quantity=0, status=None, TypeMaterial=None, CompatibleUnits=None, PropertyUnits=None, *args, **kw_args):
        """Initializes a new 'CUMaterialItem' instance.

        @param corporateCode: Code for material. 
        @param quantity: Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial. 
        @param status:
        @param TypeMaterial:
        @param CompatibleUnits:
        @param PropertyUnits:
        """
        #: Code for material.
        self.corporateCode = corporateCode

        #: Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial.
        self.quantity = quantity

        self.status = status

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._PropertyUnits = []
        self.PropertyUnits = [] if PropertyUnits is None else PropertyUnits

        super(CUMaterialItem, self).__init__(*args, **kw_args)

    status = None

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.CUMaterialItems if x != self]
            self._TypeMaterial._CUMaterialItems = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            self._TypeMaterial._CUMaterialItems.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

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

