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

from CIM14v13.IEC61968.Common.Document import Document

class WorkCostDetail(Document):
    """A collection of all of the individual cost items collected from multiple sources.
    """

    def __init__(self, amount=0.0, isDebit=False, transactionDateTime='', type='', OverheadCost=None, WorkTask=None, LaborItems=None, ErpProjectAccounting=None, EquipmentItems=None, WorkCostSummary=None, Design=None, MiscCostItems=None, CostType=None, Works=None, ContractorItems=None, MaterialItems=None, PropertyUnits=None, **kw_args):
        """Initializes a new 'WorkCostDetail' instance.

        @param amount: Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other. 
        @param isDebit: True if 'amount' is a debit, false if it is a credit. 
        @param transactionDateTime: Date and time that 'amount' is posted to the work. 
        @param type: Type of work cost. 
        @param OverheadCost:
        @param WorkTask:
        @param LaborItems:
        @param ErpProjectAccounting:
        @param EquipmentItems:
        @param WorkCostSummary:
        @param Design:
        @param MiscCostItems:
        @param CostType:
        @param Works:
        @param ContractorItems:
        @param MaterialItems:
        @param PropertyUnits:
        """
        #: Amount in designated currency for work, either a total or an individual element. As defined in the attribute 'type,' multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other.
        self.amount = amount

        #: True if 'amount' is a debit, false if it is a credit.
        self.isDebit = isDebit

        #: Date and time that 'amount' is posted to the work.
        self.transactionDateTime = transactionDateTime

        #: Type of work cost.
        self.type = type

        self._OverheadCost = None
        self.OverheadCost = OverheadCost

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._LaborItems = []
        self.LaborItems = [] if LaborItems is None else LaborItems

        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._EquipmentItems = []
        self.EquipmentItems = [] if EquipmentItems is None else EquipmentItems

        self._WorkCostSummary = None
        self.WorkCostSummary = WorkCostSummary

        self._Design = None
        self.Design = Design

        self._MiscCostItems = []
        self.MiscCostItems = [] if MiscCostItems is None else MiscCostItems

        self._CostType = None
        self.CostType = CostType

        self._Works = []
        self.Works = [] if Works is None else Works

        self._ContractorItems = []
        self.ContractorItems = [] if ContractorItems is None else ContractorItems

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._PropertyUnits = []
        self.PropertyUnits = [] if PropertyUnits is None else PropertyUnits

        super(WorkCostDetail, self).__init__(**kw_args)

    def getOverheadCost(self):
        
        return self._OverheadCost

    def setOverheadCost(self, value):
        if self._OverheadCost is not None:
            filtered = [x for x in self.OverheadCost.WorkCostDetails if x != self]
            self._OverheadCost._WorkCostDetails = filtered

        self._OverheadCost = value
        if self._OverheadCost is not None:
            self._OverheadCost._WorkCostDetails.append(self)

    OverheadCost = property(getOverheadCost, setOverheadCost)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.WorkCostDetails if x != self]
            self._WorkTask._WorkCostDetails = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._WorkCostDetails.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getLaborItems(self):
        
        return self._LaborItems

    def setLaborItems(self, value):
        for x in self._LaborItems:
            x._WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._LaborItems = value

    LaborItems = property(getLaborItems, setLaborItems)

    def addLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj._WorkCostDetail = self
            self._LaborItems.append(obj)

    def removeLaborItems(self, *LaborItems):
        for obj in LaborItems:
            obj._WorkCostDetail = None
            self._LaborItems.remove(obj)

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.WorkCostDetails if x != self]
            self._ErpProjectAccounting._WorkCostDetails = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            self._ErpProjectAccounting._WorkCostDetails.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

    def getEquipmentItems(self):
        
        return self._EquipmentItems

    def setEquipmentItems(self, value):
        for x in self._EquipmentItems:
            x._WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._EquipmentItems = value

    EquipmentItems = property(getEquipmentItems, setEquipmentItems)

    def addEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj._WorkCostDetail = self
            self._EquipmentItems.append(obj)

    def removeEquipmentItems(self, *EquipmentItems):
        for obj in EquipmentItems:
            obj._WorkCostDetail = None
            self._EquipmentItems.remove(obj)

    def getWorkCostSummary(self):
        
        return self._WorkCostSummary

    def setWorkCostSummary(self, value):
        if self._WorkCostSummary is not None:
            self._WorkCostSummary._WorkCostDetail = None

        self._WorkCostSummary = value
        if self._WorkCostSummary is not None:
            self._WorkCostSummary._WorkCostDetail = self

    WorkCostSummary = property(getWorkCostSummary, setWorkCostSummary)

    def getDesign(self):
        
        return self._Design

    def setDesign(self, value):
        if self._Design is not None:
            filtered = [x for x in self.Design.WorkCostDetails if x != self]
            self._Design._WorkCostDetails = filtered

        self._Design = value
        if self._Design is not None:
            self._Design._WorkCostDetails.append(self)

    Design = property(getDesign, setDesign)

    def getMiscCostItems(self):
        
        return self._MiscCostItems

    def setMiscCostItems(self, value):
        for x in self._MiscCostItems:
            x._WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._MiscCostItems = value

    MiscCostItems = property(getMiscCostItems, setMiscCostItems)

    def addMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj._WorkCostDetail = self
            self._MiscCostItems.append(obj)

    def removeMiscCostItems(self, *MiscCostItems):
        for obj in MiscCostItems:
            obj._WorkCostDetail = None
            self._MiscCostItems.remove(obj)

    def getCostType(self):
        
        return self._CostType

    def setCostType(self, value):
        if self._CostType is not None:
            filtered = [x for x in self.CostType.WorkCostDetails if x != self]
            self._CostType._WorkCostDetails = filtered

        self._CostType = value
        if self._CostType is not None:
            self._CostType._WorkCostDetails.append(self)

    CostType = property(getCostType, setCostType)

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

    def getContractorItems(self):
        
        return self._ContractorItems

    def setContractorItems(self, value):
        for x in self._ContractorItems:
            x._WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._ContractorItems = value

    ContractorItems = property(getContractorItems, setContractorItems)

    def addContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj._WorkCostDetail = self
            self._ContractorItems.append(obj)

    def removeContractorItems(self, *ContractorItems):
        for obj in ContractorItems:
            obj._WorkCostDetail = None
            self._ContractorItems.remove(obj)

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x._WorkCostDetail = None
        for y in value:
            y._WorkCostDetail = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._WorkCostDetail = self
            self._MaterialItems.append(obj)

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._WorkCostDetail = None
            self._MaterialItems.remove(obj)

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

