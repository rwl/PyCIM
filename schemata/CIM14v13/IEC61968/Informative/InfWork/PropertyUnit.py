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

class PropertyUnit(IdentifiedObject):
    """Unit of property for reporting purposes.
    """

    def __init__(self, activityCode='install', accountingUsage='', propertyAccount='', CUMaterialItems=None, CompatibleUnits=None, status=None, WorkCostDetails=None, *args, **kw_args):
        """Initializes a new 'PropertyUnit' instance.

        @param activityCode: Activity code identifies a specific and distinguishable work action. Values are: "install", "remove", "transfer", "abandon"
        @param accountingUsage: A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications. 
        @param propertyAccount: Used for property record accounting. For example, in the USA, this would be a FERC account. 
        @param CUMaterialItems:
        @param CompatibleUnits:
        @param status:
        @param WorkCostDetails:
        """
        #: Activity code identifies a specific and distinguishable work action.Values are: "install", "remove", "transfer", "abandon"
        self.activityCode = activityCode

        #: A code that identifies appropriate type of property accounts such as distribution, streetlgihts, communications.
        self.accountingUsage = accountingUsage

        #: Used for property record accounting. For example, in the USA, this would be a FERC account.
        self.propertyAccount = propertyAccount

        self._CUMaterialItems = []
        self.CUMaterialItems = [] if CUMaterialItems is None else CUMaterialItems

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self.status = status

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        super(PropertyUnit, self).__init__(*args, **kw_args)

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

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for x in self._CompatibleUnits:
            x._PropertyUnit = None
        for y in value:
            y._PropertyUnit = self
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj._PropertyUnit = self
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj._PropertyUnit = None
            self._CompatibleUnits.remove(obj)

    status = None

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

