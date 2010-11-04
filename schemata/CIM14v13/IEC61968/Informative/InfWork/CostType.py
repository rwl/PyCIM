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

class CostType(IdentifiedObject):
    """A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.
    """

    def __init__(self, code='', amountAssignmentFlag=False, level='', stage='', WorkCostDetails=None, ErpJournalEntries=None, ChildCostTypes=None, ParentCostType=None, status=None, CompatibleUnits=None, *args, **kw_args):
        """Initializes a new 'CostType' instance.

        @param code: A codified representation of the resource element. 
        @param amountAssignmentFlag: True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components). 
        @param level: The level of the resource element in the hierarchy of resource elements (recursive relationship). 
        @param stage: The stage for which this costType applies: estimated design, estimated actual or actual actual. 
        @param WorkCostDetails:
        @param ErpJournalEntries:
        @param ChildCostTypes:
        @param ParentCostType:
        @param status:
        @param CompatibleUnits:
        """
        #: A codified representation of the resource element.
        self.code = code

        #: True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components).
        self.amountAssignmentFlag = amountAssignmentFlag

        #: The level of the resource element in the hierarchy of resource elements (recursive relationship).
        self.level = level

        #: The stage for which this costType applies: estimated design, estimated actual or actual actual.
        self.stage = stage

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        self._ChildCostTypes = []
        self.ChildCostTypes = [] if ChildCostTypes is None else ChildCostTypes

        self._ParentCostType = None
        self.ParentCostType = ParentCostType

        self.status = status

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        super(CostType, self).__init__(*args, **kw_args)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x._CostType = None
        for y in value:
            y._CostType = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._CostType = self
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._CostType = None
            self._WorkCostDetails.remove(obj)

    def getErpJournalEntries(self):
        
        return self._ErpJournalEntries

    def setErpJournalEntries(self, value):
        for p in self._ErpJournalEntries:
            filtered = [q for q in p.CostTypes if q != self]
            self._ErpJournalEntries._CostTypes = filtered
        for r in value:
            if self not in r._CostTypes:
                r._CostTypes.append(self)
        self._ErpJournalEntries = value

    ErpJournalEntries = property(getErpJournalEntries, setErpJournalEntries)

    def addErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            if self not in obj._CostTypes:
                obj._CostTypes.append(self)
            self._ErpJournalEntries.append(obj)

    def removeErpJournalEntries(self, *ErpJournalEntries):
        for obj in ErpJournalEntries:
            if self in obj._CostTypes:
                obj._CostTypes.remove(self)
            self._ErpJournalEntries.remove(obj)

    def getChildCostTypes(self):
        
        return self._ChildCostTypes

    def setChildCostTypes(self, value):
        for x in self._ChildCostTypes:
            x._ParentCostType = None
        for y in value:
            y._ParentCostType = self
        self._ChildCostTypes = value

    ChildCostTypes = property(getChildCostTypes, setChildCostTypes)

    def addChildCostTypes(self, *ChildCostTypes):
        for obj in ChildCostTypes:
            obj._ParentCostType = self
            self._ChildCostTypes.append(obj)

    def removeChildCostTypes(self, *ChildCostTypes):
        for obj in ChildCostTypes:
            obj._ParentCostType = None
            self._ChildCostTypes.remove(obj)

    def getParentCostType(self):
        
        return self._ParentCostType

    def setParentCostType(self, value):
        if self._ParentCostType is not None:
            filtered = [x for x in self.ParentCostType.ChildCostTypes if x != self]
            self._ParentCostType._ChildCostTypes = filtered

        self._ParentCostType = value
        if self._ParentCostType is not None:
            self._ParentCostType._ChildCostTypes.append(self)

    ParentCostType = property(getParentCostType, setParentCostType)

    status = None

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for x in self._CompatibleUnits:
            x._CostType = None
        for y in value:
            y._CostType = self
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj._CostType = self
            self._CompatibleUnits.append(obj)

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj._CostType = None
            self._CompatibleUnits.remove(obj)

