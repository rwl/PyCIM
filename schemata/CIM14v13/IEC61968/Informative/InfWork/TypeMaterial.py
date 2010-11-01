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

class TypeMaterial(Document):
    """Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.
    """

    def __init__(self, stockItem=False, quantity='', costType='', estUnitCost=0.0, ErpReqLineItems=None, ErpIssueInventories=None, CUMaterialItems=None, MaterialItems=None, *args, **kw_args):
        """Initializes a new 'TypeMaterial' instance.

        @param stockItem: True if item is a stock item (default). 
        @param quantity: The value, unit of measure, and multiplier for the quantity. 
        @param costType: The category of cost to which this Material Item belongs. 
        @param estUnitCost: The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        @param ErpReqLineItems:
        @param ErpIssueInventories:
        @param CUMaterialItems:
        @param MaterialItems:
        """
        #: True if item is a stock item (default). 
        self.stockItem = stockItem

        #: The value, unit of measure, and multiplier for the quantity. 
        self.quantity = quantity

        #: The category of cost to which this Material Item belongs. 
        self.costType = costType

        #: The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        self.estUnitCost = estUnitCost

        self._ErpReqLineItems = []
        self.ErpReqLineItems = [] if ErpReqLineItems is None else ErpReqLineItems

        self._ErpIssueInventories = []
        self.ErpIssueInventories = [] if ErpIssueInventories is None else ErpIssueInventories

        self._CUMaterialItems = []
        self.CUMaterialItems = [] if CUMaterialItems is None else CUMaterialItems

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        super(TypeMaterial, self).__init__(*args, **kw_args)

    def getErpReqLineItems(self):
        
        return self._ErpReqLineItems

    def setErpReqLineItems(self, value):
        for x in self._ErpReqLineItems:
            x._TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._ErpReqLineItems = value

    ErpReqLineItems = property(getErpReqLineItems, setErpReqLineItems)

    def addErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj._TypeMaterial = self
            self._ErpReqLineItems.append(obj)

    def removeErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj._TypeMaterial = None
            self._ErpReqLineItems.remove(obj)

    def getErpIssueInventories(self):
        
        return self._ErpIssueInventories

    def setErpIssueInventories(self, value):
        for x in self._ErpIssueInventories:
            x._TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._ErpIssueInventories = value

    ErpIssueInventories = property(getErpIssueInventories, setErpIssueInventories)

    def addErpIssueInventories(self, *ErpIssueInventories):
        for obj in ErpIssueInventories:
            obj._TypeMaterial = self
            self._ErpIssueInventories.append(obj)

    def removeErpIssueInventories(self, *ErpIssueInventories):
        for obj in ErpIssueInventories:
            obj._TypeMaterial = None
            self._ErpIssueInventories.remove(obj)

    def getCUMaterialItems(self):
        
        return self._CUMaterialItems

    def setCUMaterialItems(self, value):
        for x in self._CUMaterialItems:
            x._TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._CUMaterialItems = value

    CUMaterialItems = property(getCUMaterialItems, setCUMaterialItems)

    def addCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            obj._TypeMaterial = self
            self._CUMaterialItems.append(obj)

    def removeCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            obj._TypeMaterial = None
            self._CUMaterialItems.remove(obj)

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x._TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._TypeMaterial = self
            self._MaterialItems.append(obj)

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj._TypeMaterial = None
            self._MaterialItems.remove(obj)

