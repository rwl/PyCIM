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

class MaterialItem(IdentifiedObject):
    """The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.
    """

    def __init__(self, actualCost=0.0, materialCode='', quantity=0, costType='', costDescription='', externalRefID='', account='', Usages=None, DesignLocation=None, status=None, WorkTask=None, ErpInventoryCounts=None, ErpRecDelvLineItems=None, ErpPOLineItems=None, WorkCostDetail=None, TypeMaterial=None, *args, **kw_args):
        """Initializes a new 'MaterialItem' instance.

        @param actualCost: The actual cost of this particular material in this particular quantity. 
        @param materialCode: Code for material. 
        @param quantity: The quantity of material used. 
        @param costType: The category of cost to which this Material Item belongs. 
        @param costDescription: Description of the cost. 
        @param externalRefID: External reference identifier for this actual material item such as a purchase order number, a serial number, etc. 
        @param account: The account to which this actual material item is charged. 
        @param Usages:
        @param DesignLocation:
        @param status:
        @param WorkTask:
        @param ErpInventoryCounts:
        @param ErpRecDelvLineItems:
        @param ErpPOLineItems:
        @param WorkCostDetail:
        @param TypeMaterial:
        """
        #: The actual cost of this particular material in this particular quantity. 
        self.actualCost = actualCost

        #: Code for material. 
        self.materialCode = materialCode

        #: The quantity of material used. 
        self.quantity = quantity

        #: The category of cost to which this Material Item belongs. 
        self.costType = costType

        #: Description of the cost. 
        self.costDescription = costDescription

        #: External reference identifier for this actual material item such as a purchase order number, a serial number, etc. 
        self.externalRefID = externalRefID

        #: The account to which this actual material item is charged. 
        self.account = account

        self._Usages = []
        self.Usages = [] if Usages is None else Usages

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self.status = status

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._ErpInventoryCounts = []
        self.ErpInventoryCounts = [] if ErpInventoryCounts is None else ErpInventoryCounts

        self._ErpRecDelvLineItems = []
        self.ErpRecDelvLineItems = [] if ErpRecDelvLineItems is None else ErpRecDelvLineItems

        self._ErpPOLineItems = []
        self.ErpPOLineItems = [] if ErpPOLineItems is None else ErpPOLineItems

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        super(MaterialItem, self).__init__(*args, **kw_args)

    def getUsages(self):
        
        return self._Usages

    def setUsages(self, value):
        for x in self._Usages:
            x._MaterialItem = None
        for y in value:
            y._MaterialItem = self
        self._Usages = value

    Usages = property(getUsages, setUsages)

    def addUsages(self, *Usages):
        for obj in Usages:
            obj._MaterialItem = self
            self._Usages.append(obj)

    def removeUsages(self, *Usages):
        for obj in Usages:
            obj._MaterialItem = None
            self._Usages.remove(obj)

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.MaterialItems if x != self]
            self._DesignLocation._MaterialItems = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            self._DesignLocation._MaterialItems.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

    status = None

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.MaterialItems if x != self]
            self._WorkTask._MaterialItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._MaterialItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getErpInventoryCounts(self):
        
        return self._ErpInventoryCounts

    def setErpInventoryCounts(self, value):
        for x in self._ErpInventoryCounts:
            x._MaterialItem = None
        for y in value:
            y._MaterialItem = self
        self._ErpInventoryCounts = value

    ErpInventoryCounts = property(getErpInventoryCounts, setErpInventoryCounts)

    def addErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj._MaterialItem = self
            self._ErpInventoryCounts.append(obj)

    def removeErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj._MaterialItem = None
            self._ErpInventoryCounts.remove(obj)

    def getErpRecDelvLineItems(self):
        
        return self._ErpRecDelvLineItems

    def setErpRecDelvLineItems(self, value):
        for p in self._ErpRecDelvLineItems:
            filtered = [q for q in p.MaterialItems if q != self]
            self._ErpRecDelvLineItems._MaterialItems = filtered
        for r in value:
            if self not in r._MaterialItems:
                r._MaterialItems.append(self)
        self._ErpRecDelvLineItems = value

    ErpRecDelvLineItems = property(getErpRecDelvLineItems, setErpRecDelvLineItems)

    def addErpRecDelvLineItems(self, *ErpRecDelvLineItems):
        for obj in ErpRecDelvLineItems:
            if self not in obj._MaterialItems:
                obj._MaterialItems.append(self)
            self._ErpRecDelvLineItems.append(obj)

    def removeErpRecDelvLineItems(self, *ErpRecDelvLineItems):
        for obj in ErpRecDelvLineItems:
            if self in obj._MaterialItems:
                obj._MaterialItems.remove(self)
            self._ErpRecDelvLineItems.remove(obj)

    def getErpPOLineItems(self):
        
        return self._ErpPOLineItems

    def setErpPOLineItems(self, value):
        for x in self._ErpPOLineItems:
            x._MaterialItem = None
        for y in value:
            y._MaterialItem = self
        self._ErpPOLineItems = value

    ErpPOLineItems = property(getErpPOLineItems, setErpPOLineItems)

    def addErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj._MaterialItem = self
            self._ErpPOLineItems.append(obj)

    def removeErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj._MaterialItem = None
            self._ErpPOLineItems.remove(obj)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.MaterialItems if x != self]
            self._WorkCostDetail._MaterialItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._MaterialItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.MaterialItems if x != self]
            self._TypeMaterial._MaterialItems = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            self._TypeMaterial._MaterialItems.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

