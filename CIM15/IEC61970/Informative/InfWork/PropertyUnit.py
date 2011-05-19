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

class PropertyUnit(IdentifiedObject):
    """Unit of property for reporting purposes.Unit of property for reporting purposes.
    """

    def __init__(self, accountingUsage='', propertyAccount='', activityCode="install", status=None, CompatibleUnits=None, CUMaterialItems=None, WorkCostDetails=None, *args, **kw_args):
        """Initialises a new 'PropertyUnit' instance.

        @param accountingUsage: A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications. 
        @param propertyAccount: Used for property record accounting. For example, in the USA, this would be a FERC account. 
        @param activityCode: Activity code identifies a specific and distinguishable work action. Values are: "install", "remove", "transfer", "abandon"
        @param status:
        @param CompatibleUnits:
        @param CUMaterialItems:
        @param WorkCostDetails:
        """
        #: A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications.
        self.accountingUsage = accountingUsage

        #: Used for property record accounting. For example, in the USA, this would be a FERC account.
        self.propertyAccount = propertyAccount

        #: Activity code identifies a specific and distinguishable work action. Values are: "install", "remove", "transfer", "abandon"
        self.activityCode = activityCode

        self.status = status

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self._CUMaterialItems = []
        self.CUMaterialItems = [] if CUMaterialItems is None else CUMaterialItems

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        super(PropertyUnit, self).__init__(*args, **kw_args)

    _attrs = ["accountingUsage", "propertyAccount", "activityCode"]
    _attr_types = {"accountingUsage": str, "propertyAccount": str, "activityCode": str}
    _defaults = {"accountingUsage": '', "propertyAccount": '', "activityCode": "install"}
    _enums = {"activityCode": "WorkActionKind"}
    _refs = ["status", "CompatibleUnits", "CUMaterialItems", "WorkCostDetails"]
    _many_refs = ["CompatibleUnits", "CUMaterialItems", "WorkCostDetails"]

    status = None

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for x in self._CompatibleUnits:
            x.PropertyUnit = None
        for y in value:
            y._PropertyUnit = self
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj.PropertyUnit = self

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj.PropertyUnit = None

    def getCUMaterialItems(self):
        
        return self._CUMaterialItems

    def setCUMaterialItems(self, value):
        for p in self._CUMaterialItems:
            filtered = [q for q in p.PropertyUnits if q != self]
            self._CUMaterialItems._PropertyUnits = filtered
        for r in value:
            if self not in r._PropertyUnits:
                r._PropertyUnits.append(self)
        self._CUMaterialItems = value

    CUMaterialItems = property(getCUMaterialItems, setCUMaterialItems)

    def addCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            if self not in obj._PropertyUnits:
                obj._PropertyUnits.append(self)
            self._CUMaterialItems.append(obj)

    def removeCUMaterialItems(self, *CUMaterialItems):
        for obj in CUMaterialItems:
            if self in obj._PropertyUnits:
                obj._PropertyUnits.remove(self)
            self._CUMaterialItems.remove(obj)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for p in self._WorkCostDetails:
            filtered = [q for q in p.PropertyUnits if q != self]
            self._WorkCostDetails._PropertyUnits = filtered
        for r in value:
            if self not in r._PropertyUnits:
                r._PropertyUnits.append(self)
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            if self not in obj._PropertyUnits:
                obj._PropertyUnits.append(self)
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            if self in obj._PropertyUnits:
                obj._PropertyUnits.remove(self)
            self._WorkCostDetails.remove(obj)

