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

class WorkCostDetail(Document):
    """A collection of all of the individual cost items collected from multiple sources.A collection of all of the individual cost items collected from multiple sources.
    """

    def __init__(self, type='', isDebit=False, transactionDateTime='', amount=0.0, WorkTask=None, Works=None, Design=None, MiscCostItems=None, WorkCostSummary=None, PropertyUnits=None, ErpProjectAccounting=None, LaborItems=None, MaterialItems=None, EquipmentItems=None, ContractorItems=None, OverheadCost=None, CostType=None, *args, **kw_args):
        """Initialises a new 'WorkCostDetail' instance.

        @param type: Type of work cost. 
        @param isDebit: True if 'amount' is a debit, false if it is a credit. 
        @param transactionDateTime: Date and time that 'amount' is posted to the work. 
        @param amount: Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other. 
        @param WorkTask:
        @param Works:
        @param Design:
        @param MiscCostItems:
        @param WorkCostSummary:
        @param PropertyUnits:
        @param ErpProjectAccounting:
        @param LaborItems:
        @param MaterialItems:
        @param EquipmentItems:
        @param ContractorItems:
        @param OverheadCost:
        @param CostType:
        """
        #: Type of work cost.
        self.type = type

        #: True if 'amount' is a debit, false if it is a credit.
        self.isDebit = isDebit

        #: Date and time that 'amount' is posted to the work.
        self.transactionDateTime = transactionDateTime

        #: Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other.
        self.amount = amount

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._Works = []
        self.Works = [] if Works is None else Works

        self._Design = None
        self.Design = Design

        self._MiscCostItems = []
        self.MiscCostItems = [] if MiscCostItems is None else MiscCostItems

        self._WorkCostSummary = None
        self.WorkCostSummary = WorkCostSummary

        self._PropertyUnits = []
        self.PropertyUnits = [] if PropertyUnits is None else PropertyUnits

        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._LaborItems = []
        self.LaborItems = [] if LaborItems is None else LaborItems

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._EquipmentItems = []
        self.EquipmentItems = [] if EquipmentItems is None else EquipmentItems

        self._ContractorItems = []
        self.ContractorItems = [] if ContractorItems is None else ContractorItems

        self._OverheadCost = None
        self.OverheadCost = OverheadCost

        self._CostType = None
        self.CostType = CostType

        super(WorkCostDetail, self).__init__(*args, **kw_args)

    _attrs = ["type", "isDebit", "transactionDateTime", "amount"]
    _attr_types = {"type": str, "isDebit": bool, "transactionDateTime": str, "amount": float}
    _defaults = {"type": '', "isDebit": False, "transactionDateTime": '', "amount": 0.0}
    _enums = {}
    _refs = ["WorkTask", "Works", "Design", "MiscCostItems", "WorkCostSummary", "PropertyUnits", "ErpProjectAccounting", "LaborItems", "MaterialItems", "EquipmentItems", "ContractorItems", "OverheadCost", "CostType"]
    _many_refs = ["Works", "MiscCostItems", "PropertyUnits", "LaborItems", "MaterialItems", "EquipmentItems", "ContractorItems"]

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.WorkCostDetails if x != self]
            self._WorkTask._WorkCostDetails = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._WorkCostDetails:
                self._WorkTask._WorkCostDetails.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for p in self._Works:
            filtered = [q for q in p.WorkCostDetails if q != self]
            self._Works._WorkCostDetails = filtered
        for r in value:
            if self not in r._WorkCostDetails:
                r._WorkCostDetails.append(self)
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            if self not in obj._WorkCostDetails:
                obj._WorkCostDetails.append(self)
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            if self in obj._WorkCostDetails:
                obj._WorkCostDetails.remove(self)
            self._Works.remove(obj)

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            filtered = [x for x in self.Design.WorkCostDetails if x != self]
            self._Design._WorkCostDetails = filtered

        self._Design = value
        if self._Design is not None:
            if self not in self._Design._WorkCostDetails:
                self._Design._WorkCostDetails.append(self)

    Design = property(getDesign, setDesign)

    def getMiscCostItems(self):
        
        return self._MiscCostItems

    def setMiscCostItems(self, value):
        for x in self._MiscCostItems:
            x.WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._MiscCostItems = value

    MiscCostItems = property(getMiscCostItems, setMiscCostItems)

    def addMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj.WorkCostDetail = self

    def removeMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj.WorkCostDetail = None

    def getWorkCostSummary(self):
        
        return self._WorkCostSummary

    def setWorkCostSummary(self, value):
        if self._WorkCostSummary is not None:
            self._WorkCostSummary._WorkCostDetail = None

        self._WorkCostSummary = value
        if self._WorkCostSummary is not None:
            self._WorkCostSummary.WorkCostDetail = None
            self._WorkCostSummary._WorkCostDetail = self

    WorkCostSummary = property(getWorkCostSummary, setWorkCostSummary)

    def getPropertyUnits(self):
        
        return self._PropertyUnits

    def setPropertyUnits(self, value):
        for p in self._PropertyUnits:
            filtered = [q for q in p.WorkCostDetails if q != self]
            self._PropertyUnits._WorkCostDetails = filtered
        for r in value:
            if self not in r._WorkCostDetails:
                r._WorkCostDetails.append(self)
        self._PropertyUnits = value

    PropertyUnits = property(getPropertyUnits, setPropertyUnits)

    def addPropertyUnits(self, *PropertyUnits):
        for obj in PropertyUnits:
            if self not in obj._WorkCostDetails:
                obj._WorkCostDetails.append(self)
            self._PropertyUnits.append(obj)

    def removePropertyUnits(self, *PropertyUnits):
        for obj in PropertyUnits:
            if self in obj._WorkCostDetails:
                obj._WorkCostDetails.remove(self)
            self._PropertyUnits.remove(obj)

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.WorkCostDetails if x != self]
            self._ErpProjectAccounting._WorkCostDetails = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            if self not in self._ErpProjectAccounting._WorkCostDetails:
                self._ErpProjectAccounting._WorkCostDetails.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

    def getLaborItems(self):
        
        return self._LaborItems

    def setLaborItems(self, value):
        for x in self._LaborItems:
            x.WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._LaborItems = value

    LaborItems = property(getLaborItems, setLaborItems)

    def addLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj.WorkCostDetail = self

    def removeLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj.WorkCostDetail = None

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x.WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.WorkCostDetail = self

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.WorkCostDetail = None

    def getEquipmentItems(self):
        
        return self._EquipmentItems

    def setEquipmentItems(self, value):
        for x in self._EquipmentItems:
            x.WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._EquipmentItems = value

    EquipmentItems = property(getEquipmentItems, setEquipmentItems)

    def addEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj.WorkCostDetail = self

    def removeEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj.WorkCostDetail = None

    def getContractorItems(self):
        
        return self._ContractorItems

    def setContractorItems(self, value):
        for x in self._ContractorItems:
            x.WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._ContractorItems = value

    ContractorItems = property(getContractorItems, setContractorItems)

    def addContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj.WorkCostDetail = self

    def removeContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj.WorkCostDetail = None

    def getOverheadCost(self):
        
        return self._OverheadCost

    def setOverheadCost(self, value):
        if self._OverheadCost is not None:
            filtered = [x for x in self.OverheadCost.WorkCostDetails if x != self]
            self._OverheadCost._WorkCostDetails = filtered

        self._OverheadCost = value
        if self._OverheadCost is not None:
            if self not in self._OverheadCost._WorkCostDetails:
                self._OverheadCost._WorkCostDetails.append(self)

    OverheadCost = property(getOverheadCost, setOverheadCost)

    def getCostType(self):
        
        return self._CostType

    def setCostType(self, value):
        if self._CostType is not None:
            filtered = [x for x in self.CostType.WorkCostDetails if x != self]
            self._CostType._WorkCostDetails = filtered

        self._CostType = value
        if self._CostType is not None:
            if self not in self._CostType._WorkCostDetails:
                self._CostType._WorkCostDetails.append(self)

    CostType = property(getCostType, setCostType)

