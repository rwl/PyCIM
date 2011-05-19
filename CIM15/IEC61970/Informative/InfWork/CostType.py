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

class CostType(IdentifiedObject):
    """A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.A categorization for resources, often costs, in accounting transactions. Examples include: material components, building in service, coal sales, overhead, etc.
    """

    def __init__(self, stage='', code='', level='', amountAssignable=False, ErpJournalEntries=None, ParentCostType=None, ChildCostTypes=None, WorkCostDetails=None, CompatibleUnits=None, status=None, *args, **kw_args):
        """Initialises a new 'CostType' instance.

        @param stage: The stage for which this costType applies: estimated design, estimated actual or actual actual. 
        @param code: A codified representation of the resource element. 
        @param level: The level of the resource element in the hierarchy of resource elements (recursive relationship). 
        @param amountAssignable: True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components). 
        @param ErpJournalEntries:
        @param ParentCostType:
        @param ChildCostTypes:
        @param WorkCostDetails:
        @param CompatibleUnits:
        @param status:
        """
        #: The stage for which this costType applies: estimated design, estimated actual or actual actual.
        self.stage = stage

        #: A codified representation of the resource element.
        self.code = code

        #: The level of the resource element in the hierarchy of resource elements (recursive relationship).
        self.level = level

        #: True if an amount can be assigned to the resource element (e.g., building in service, transmission plant, software development capital); false otherwise (e.g., internal labor, material components).
        self.amountAssignable = amountAssignable

        self._ErpJournalEntries = []
        self.ErpJournalEntries = [] if ErpJournalEntries is None else ErpJournalEntries

        self._ParentCostType = None
        self.ParentCostType = ParentCostType

        self._ChildCostTypes = []
        self.ChildCostTypes = [] if ChildCostTypes is None else ChildCostTypes

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._CompatibleUnits = []
        self.CompatibleUnits = [] if CompatibleUnits is None else CompatibleUnits

        self.status = status

        super(CostType, self).__init__(*args, **kw_args)

    _attrs = ["stage", "code", "level", "amountAssignable"]
    _attr_types = {"stage": str, "code": str, "level": str, "amountAssignable": bool}
    _defaults = {"stage": '', "code": '', "level": '', "amountAssignable": False}
    _enums = {}
    _refs = ["ErpJournalEntries", "ParentCostType", "ChildCostTypes", "WorkCostDetails", "CompatibleUnits", "status"]
    _many_refs = ["ErpJournalEntries", "ChildCostTypes", "WorkCostDetails", "CompatibleUnits"]

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

    def getParentCostType(self):
        
        return self._ParentCostType

    def setParentCostType(self, value):
        if self._ParentCostType is not None:
            filtered = [x for x in self.ParentCostType.ChildCostTypes if x != self]
            self._ParentCostType._ChildCostTypes = filtered

        self._ParentCostType = value
        if self._ParentCostType is not None:
            if self not in self._ParentCostType._ChildCostTypes:
                self._ParentCostType._ChildCostTypes.append(self)

    ParentCostType = property(getParentCostType, setParentCostType)

    def getChildCostTypes(self):
        
        return self._ChildCostTypes

    def setChildCostTypes(self, value):
        for x in self._ChildCostTypes:
            x.ParentCostType = None
        for y in value:
            y._ParentCostType = self
        self._ChildCostTypes = value

    ChildCostTypes = property(getChildCostTypes, setChildCostTypes)

    def addChildCostTypes(self, *ChildCostTypes):
        for obj in ChildCostTypes:
            obj.ParentCostType = self

    def removeChildCostTypes(self, *ChildCostTypes):
        for obj in ChildCostTypes:
            obj.ParentCostType = None

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x.CostType = None
        for y in value:
            y._CostType = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.CostType = self

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.CostType = None

    def getCompatibleUnits(self):
        
        return self._CompatibleUnits

    def setCompatibleUnits(self, value):
        for x in self._CompatibleUnits:
            x.CostType = None
        for y in value:
            y._CostType = self
        self._CompatibleUnits = value

    CompatibleUnits = property(getCompatibleUnits, setCompatibleUnits)

    def addCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj.CostType = self

    def removeCompatibleUnits(self, *CompatibleUnits):
        for obj in CompatibleUnits:
            obj.CostType = None

    status = None

