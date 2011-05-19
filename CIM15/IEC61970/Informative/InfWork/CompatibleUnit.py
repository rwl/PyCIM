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

from CIM15.IEC61968.Common.Document import Document

class CompatibleUnit(Document):
    """A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.A pre-planned job model containing labor, material, and accounting requirements for standardized job planning.
    """

    def __init__(self, quantity='', estCost=0.0, CUWorkEquipmentItems=None, DesignLocationCUs=None, CUGroup=None, CUAssets=None, PropertyUnit=None, CostType=None, CUAllowableAction=None, Procedures=None, CUContractorItems=None, CUMaterialItems=None, CULaborItems=None, *args, **kw_args):
        """Initialises a new 'CompatibleUnit' instance.

        @param quantity: The quantity, unit of measure, and multiplier at the CU level that applies to the materials. 
        @param estCost: Estimated total cost for perfoming CU. 
        @param CUWorkEquipmentItems:
        @param DesignLocationCUs:
        @param CUGroup:
        @param CUAssets:
        @param PropertyUnit:
        @param CostType:
        @param CUAllowableAction:
        @param Procedures:
        @param CUContractorItems:
        @param CUMaterialItems:
        @param CULaborItems:
        """
        #: The quantity, unit of measure, and multiplier at the CU level that applies to the materials.
        self.quantity = quantity

        #: Estimated total cost for perfoming CU.
        self.estCost = estCost

        self._CUWorkEquipmentItems = []
        self.CUWorkEquipmentItems = [] if CUWorkEquipmentItems is None else CUWorkEquipmentItems

        self._DesignLocationCUs = []
        self.DesignLocationCUs = [] if DesignLocationCUs is None else DesignLocationCUs

        self._CUGroup = None
        self.CUGroup = CUGroup

        self._CUAssets = []
        self.CUAssets = [] if CUAssets is None else CUAssets

        self._PropertyUnit = None
        self.PropertyUnit = PropertyUnit

        self._CostType = None
        self.CostType = CostType

        self._CUAllowableAction = None
        self.CUAllowableAction = CUAllowableAction

        self._Procedures = []
        self.Procedures = [] if Procedures is None else Procedures

        self._CUContractorItems = []
        self.CUContractorItems = [] if CUContractorItems is None else CUContractorItems

        self._CUMaterialItems = []
        self.CUMaterialItems = [] if CUMaterialItems is None else CUMaterialItems

        self._CULaborItems = []
        self.CULaborItems = [] if CULaborItems is None else CULaborItems

        super(CompatibleUnit, self).__init__(*args, **kw_args)

    _attrs = ["quantity", "estCost"]
    _attr_types = {"quantity": str, "estCost": float}
    _defaults = {"quantity": '', "estCost": 0.0}
    _enums = {}
    _refs = ["CUWorkEquipmentItems", "DesignLocationCUs", "CUGroup", "CUAssets", "PropertyUnit", "CostType", "CUAllowableAction", "Procedures", "CUContractorItems", "CUMaterialItems", "CULaborItems"]
    _many_refs = ["CUWorkEquipmentItems", "DesignLocationCUs", "CUAssets", "Procedures", "CUContractorItems", "CUMaterialItems", "CULaborItems"]

    def getCUWorkEquipmentItems(self):
        
        return self._CUWorkEquipmentItems

    def setCUWorkEquipmentItems(self, value):
        for p in self._CUWorkEquipmentItems:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._CUWorkEquipmentItems._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._CUWorkEquipmentItems = value

    CUWorkEquipmentItems = property(getCUWorkEquipmentItems, setCUWorkEquipmentItems)

    def addCUWorkEquipmentItems(self, *CUWorkEquipmentItems):
        for obj in CUWorkEquipmentItems:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._CUWorkEquipmentItems.append(obj)

    def removeCUWorkEquipmentItems(self, *CUWorkEquipmentItems):
        for obj in CUWorkEquipmentItems:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._CUWorkEquipmentItems.remove(obj)

    def getDesignLocationCUs(self):
        
        return self._DesignLocationCUs

    def setDesignLocationCUs(self, value):
        for p in self._DesignLocationCUs:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._DesignLocationCUs._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._DesignLocationCUs = value

    DesignLocationCUs = property(getDesignLocationCUs, setDesignLocationCUs)

    def addDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._DesignLocationCUs.append(obj)

    def removeDesignLocationCUs(self, *DesignLocationCUs):
        for obj in DesignLocationCUs:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._DesignLocationCUs.remove(obj)

    def getCUGroup(self):
        
        return self._CUGroup

    def setCUGroup(self, value):
        if self._CUGroup is not None:
            filtered = [x for x in self.CUGroup.CompatibleUnits if x != self]
            self._CUGroup._CompatibleUnits = filtered

        self._CUGroup = value
        if self._CUGroup is not None:
            if self not in self._CUGroup._CompatibleUnits:
                self._CUGroup._CompatibleUnits.append(self)

    CUGroup = property(getCUGroup, setCUGroup)

    def getCUAssets(self):
        
        return self._CUAssets

    def setCUAssets(self, value):
        for p in self._CUAssets:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._CUAssets._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._CUAssets = value

    CUAssets = property(getCUAssets, setCUAssets)

    def addCUAssets(self, *CUAssets):
        for obj in CUAssets:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._CUAssets.append(obj)

    def removeCUAssets(self, *CUAssets):
        for obj in CUAssets:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._CUAssets.remove(obj)

    def getPropertyUnit(self):
        
        return self._PropertyUnit

    def setPropertyUnit(self, value):
        if self._PropertyUnit is not None:
            filtered = [x for x in self.PropertyUnit.CompatibleUnits if x != self]
            self._PropertyUnit._CompatibleUnits = filtered

        self._PropertyUnit = value
        if self._PropertyUnit is not None:
            if self not in self._PropertyUnit._CompatibleUnits:
                self._PropertyUnit._CompatibleUnits.append(self)

    PropertyUnit = property(getPropertyUnit, setPropertyUnit)

    def getCostType(self):
        
        return self._CostType

    def setCostType(self, value):
        if self._CostType is not None:
            filtered = [x for x in self.CostType.CompatibleUnits if x != self]
            self._CostType._CompatibleUnits = filtered

        self._CostType = value
        if self._CostType is not None:
            if self not in self._CostType._CompatibleUnits:
                self._CostType._CompatibleUnits.append(self)

    CostType = property(getCostType, setCostType)

    def getCUAllowableAction(self):
        
        return self._CUAllowableAction

    def setCUAllowableAction(self, value):
        if self._CUAllowableAction is not None:
            filtered = [x for x in self.CUAllowableAction.CompatibleUnits if x != self]
            self._CUAllowableAction._CompatibleUnits = filtered

        self._CUAllowableAction = value
        if self._CUAllowableAction is not None:
            if self not in self._CUAllowableAction._CompatibleUnits:
                self._CUAllowableAction._CompatibleUnits.append(self)

    CUAllowableAction = property(getCUAllowableAction, setCUAllowableAction)

    def getProcedures(self):
        
        return self._Procedures

    def setProcedures(self, value):
        for p in self._Procedures:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._Procedures._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._Procedures = value

    Procedures = property(getProcedures, setProcedures)

    def addProcedures(self, *Procedures):
        for obj in Procedures:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._Procedures.append(obj)

    def removeProcedures(self, *Procedures):
        for obj in Procedures:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._Procedures.remove(obj)

    def getCUContractorItems(self):
        
        return self._CUContractorItems

    def setCUContractorItems(self, value):
        for p in self._CUContractorItems:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._CUContractorItems._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._CUContractorItems = value

    CUContractorItems = property(getCUContractorItems, setCUContractorItems)

    def addCUContractorItems(self, *CUContractorItems):
        for obj in CUContractorItems:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._CUContractorItems.append(obj)

    def removeCUContractorItems(self, *CUContractorItems):
        for obj in CUContractorItems:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._CUContractorItems.remove(obj)

    def getCUMaterialItems(self):
        
        return self._CUMaterialItems

    def setCUMaterialItems(self, value):
        for p in self._CUMaterialItems:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._CUMaterialItems._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._CUMaterialItems = value

    CUMaterialItems = property(getCUMaterialItems, setCUMaterialItems)

    def addCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._CUMaterialItems.append(obj)

    def removeCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._CUMaterialItems.remove(obj)

    def getCULaborItems(self):
        
        return self._CULaborItems

    def setCULaborItems(self, value):
        for p in self._CULaborItems:
            filtered = [q for q in p.CompatibleUnits if q != self]
            self._CULaborItems._CompatibleUnits = filtered
        for r in value:
            if self not in r._CompatibleUnits:
                r._CompatibleUnits.append(self)
        self._CULaborItems = value

    CULaborItems = property(getCULaborItems, setCULaborItems)

    def addCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            if self not in obj._CompatibleUnits:
                obj._CompatibleUnits.append(self)
            self._CULaborItems.append(obj)

    def removeCULaborItems(self, *CULaborItems):
        for obj in CULaborItems:
            if self in obj._CompatibleUnits:
                obj._CompatibleUnits.remove(self)
            self._CULaborItems.remove(obj)

