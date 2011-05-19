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

class MaterialItem(IdentifiedObject):
    """The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.The physical consumable supply used for work and other purposes. It includes items such as nuts, bolts, brackets, glue, etc.
    """

    def __init__(self, costDescription='', quantity="", materialCode='', externalRefID='', costType='', account='', actualCost=0.0, ErpInventoryCounts=None, Usages=None, ErpPOLineItems=None, ErpRecDelvLineItems=None, DesignLocation=None, status=None, TypeMaterial=None, WorkCostDetail=None, WorkTask=None, *args, **kw_args):
        """Initialises a new 'MaterialItem' instance.

        @param costDescription: Description of the cost. 
        @param quantity: The quantity of material used. 
        @param materialCode: Code for material. 
        @param externalRefID: External reference identifier for this actual material item such as a purchase order number, a serial number, etc. 
        @param costType: The category of cost to which this Material Item belongs. 
        @param account: The account to which this actual material item is charged. 
        @param actualCost: The actual cost of this particular material in this particular quantity. 
        @param ErpInventoryCounts:
        @param Usages:
        @param ErpPOLineItems:
        @param ErpRecDelvLineItems:
        @param DesignLocation:
        @param status:
        @param TypeMaterial:
        @param WorkCostDetail:
        @param WorkTask:
        """
        #: Description of the cost.
        self.costDescription = costDescription

        #: The quantity of material used.
        self.quantity = quantity

        #: Code for material.
        self.materialCode = materialCode

        #: External reference identifier for this actual material item such as a purchase order number, a serial number, etc.
        self.externalRefID = externalRefID

        #: The category of cost to which this Material Item belongs.
        self.costType = costType

        #: The account to which this actual material item is charged.
        self.account = account

        #: The actual cost of this particular material in this particular quantity.
        self.actualCost = actualCost

        self._ErpInventoryCounts = []
        self.ErpInventoryCounts = [] if ErpInventoryCounts is None else ErpInventoryCounts

        self._Usages = []
        self.Usages = [] if Usages is None else Usages

        self._ErpPOLineItems = []
        self.ErpPOLineItems = [] if ErpPOLineItems is None else ErpPOLineItems

        self._ErpRecDelvLineItems = []
        self.ErpRecDelvLineItems = [] if ErpRecDelvLineItems is None else ErpRecDelvLineItems

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self.status = status

        self._TypeMaterial = None
        self.TypeMaterial = TypeMaterial

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self._WorkTask = None
        self.WorkTask = WorkTask

        super(MaterialItem, self).__init__(*args, **kw_args)

    _attrs = ["costDescription", "quantity", "materialCode", "externalRefID", "costType", "account", "actualCost"]
    _attr_types = {"costDescription": str, "quantity": str, "materialCode": str, "externalRefID": str, "costType": str, "account": str, "actualCost": float}
    _defaults = {"costDescription": '', "quantity": "", "materialCode": '', "externalRefID": '', "costType": '', "account": '', "actualCost": 0.0}
    _enums = {}
    _refs = ["ErpInventoryCounts", "Usages", "ErpPOLineItems", "ErpRecDelvLineItems", "DesignLocation", "status", "TypeMaterial", "WorkCostDetail", "WorkTask"]
    _many_refs = ["ErpInventoryCounts", "Usages", "ErpPOLineItems", "ErpRecDelvLineItems"]

    def getErpInventoryCounts(self):
        
        return self._ErpInventoryCounts

    def setErpInventoryCounts(self, value):
        for x in self._ErpInventoryCounts:
            x.MaterialItem = None
        for y in value:
            y._MaterialItem = self
        self._ErpInventoryCounts = value

    ErpInventoryCounts = property(getErpInventoryCounts, setErpInventoryCounts)

    def addErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj.MaterialItem = self

    def removeErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj.MaterialItem = None

    def getUsages(self):
        
        return self._Usages

    def setUsages(self, value):
        for x in self._Usages:
            x.MaterialItem = None
        for y in value:
            y._MaterialItem = self
        self._Usages = value

    Usages = property(getUsages, setUsages)

    def addUsages(self, *Usages):
        for obj in Usages:
            obj.MaterialItem = self

    def removeUsages(self, *Usages):
        for obj in Usages:
            obj.MaterialItem = None

    def getErpPOLineItems(self):
        
        return self._ErpPOLineItems

    def setErpPOLineItems(self, value):
        for x in self._ErpPOLineItems:
            x.MaterialItem = None
        for y in value:
            y._MaterialItem = self
        self._ErpPOLineItems = value

    ErpPOLineItems = property(getErpPOLineItems, setErpPOLineItems)

    def addErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj.MaterialItem = self

    def removeErpPOLineItems(self, *ErpPOLineItems):
        for obj in ErpPOLineItems:
            obj.MaterialItem = None

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

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.MaterialItems if x != self]
            self._DesignLocation._MaterialItems = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            if self not in self._DesignLocation._MaterialItems:
                self._DesignLocation._MaterialItems.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

    status = None

    def getTypeMaterial(self):
        
        return self._TypeMaterial

    def setTypeMaterial(self, value):
        if self._TypeMaterial is not None:
            filtered = [x for x in self.TypeMaterial.MaterialItems if x != self]
            self._TypeMaterial._MaterialItems = filtered

        self._TypeMaterial = value
        if self._TypeMaterial is not None:
            if self not in self._TypeMaterial._MaterialItems:
                self._TypeMaterial._MaterialItems.append(self)

    TypeMaterial = property(getTypeMaterial, setTypeMaterial)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.MaterialItems if x != self]
            self._WorkCostDetail._MaterialItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            if self not in self._WorkCostDetail._MaterialItems:
                self._WorkCostDetail._MaterialItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.MaterialItems if x != self]
            self._WorkTask._MaterialItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._MaterialItems:
                self._WorkTask._MaterialItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

