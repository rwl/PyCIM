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

class TypeMaterial(Document):
    """Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.Documentation for a generic material item that may be used for design, work and other purposes. Any number of MaterialItems manufactured by various vendors may be used to perform this TypeMaterial. Note that class analagous to 'AssetModel' is not used for material items. This is because in some cases, for example, a utility sets up a Master material record for a 3 inch long half inch diameter steel bolt and they do not necessarily care what specific supplier is providing the material item. As different vendors are used to supply the part, the Stock Code of the material item can stay the same. In other cases, each time the vendor changes, a new stock code is set up so they can track material used by vendor. Therefore a Material Item 'Model' is not typically needed.
    """

    def __init__(self, stockItem=False, costType='', quantity='', estUnitCost=0.0, ErpIssueInventories=None, MaterialItems=None, CUMaterialItems=None, ErpReqLineItems=None, *args, **kw_args):
        """Initialises a new 'TypeMaterial' instance.

        @param stockItem: True if item is a stock item (default). 
        @param costType: The category of cost to which this Material Item belongs. 
        @param quantity: The value, unit of measure, and multiplier for the quantity. 
        @param estUnitCost: The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        @param ErpIssueInventories:
        @param MaterialItems:
        @param CUMaterialItems:
        @param ErpReqLineItems:
        """
        #: True if item is a stock item (default).
        self.stockItem = stockItem

        #: The category of cost to which this Material Item belongs.
        self.costType = costType

        #: The value, unit of measure, and multiplier for the quantity.
        self.quantity = quantity

        #: The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
        self.estUnitCost = estUnitCost

        self._ErpIssueInventories = []
        self.ErpIssueInventories = [] if ErpIssueInventories is None else ErpIssueInventories

        self._MaterialItems = []
        self.MaterialItems = [] if MaterialItems is None else MaterialItems

        self._CUMaterialItems = []
        self.CUMaterialItems = [] if CUMaterialItems is None else CUMaterialItems

        self._ErpReqLineItems = []
        self.ErpReqLineItems = [] if ErpReqLineItems is None else ErpReqLineItems

        super(TypeMaterial, self).__init__(*args, **kw_args)

    _attrs = ["stockItem", "costType", "quantity", "estUnitCost"]
    _attr_types = {"stockItem": bool, "costType": str, "quantity": str, "estUnitCost": float}
    _defaults = {"stockItem": False, "costType": '', "quantity": '', "estUnitCost": 0.0}
    _enums = {}
    _refs = ["ErpIssueInventories", "MaterialItems", "CUMaterialItems", "ErpReqLineItems"]
    _many_refs = ["ErpIssueInventories", "MaterialItems", "CUMaterialItems", "ErpReqLineItems"]

    def getErpIssueInventories(self):
        
        return self._ErpIssueInventories

    def setErpIssueInventories(self, value):
        for x in self._ErpIssueInventories:
            x.TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._ErpIssueInventories = value

    ErpIssueInventories = property(getErpIssueInventories, setErpIssueInventories)

    def addErpIssueInventories(self, *ErpIssueInventories):
        for obj in ErpIssueInventories:
            obj.TypeMaterial = self

    def removeErpIssueInventories(self, *ErpIssueInventories):
        for obj in ErpIssueInventories:
            obj.TypeMaterial = None

    def getMaterialItems(self):
        
        return self._MaterialItems

    def setMaterialItems(self, value):
        for x in self._MaterialItems:
            x.TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._MaterialItems = value

    MaterialItems = property(getMaterialItems, setMaterialItems)

    def addMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.TypeMaterial = self

    def removeMaterialItems(self, *MaterialItems):
        for obj in MaterialItems:
            obj.TypeMaterial = None

    def getCUMaterialItems(self):
        
        return self._CUMaterialItems

    def setCUMaterialItems(self, value):
        for x in self._CUMaterialItems:
            x.TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._CUMaterialItems = value

    CUMaterialItems = property(getCUMaterialItems, setCUMaterialItems)

    def addCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            obj.TypeMaterial = self

    def removeCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            obj.TypeMaterial = None

    def getErpReqLineItems(self):
        
        return self._ErpReqLineItems

    def setErpReqLineItems(self, value):
        for x in self._ErpReqLineItems:
            x.TypeMaterial = None
        for y in value:
            y._TypeMaterial = self
        self._ErpReqLineItems = value

    ErpReqLineItems = property(getErpReqLineItems, setErpReqLineItems)

    def addErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj.TypeMaterial = self

    def removeErpReqLineItems(self, *ErpReqLineItems):
        for obj in ErpReqLineItems:
            obj.TypeMaterial = None

