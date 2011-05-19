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

class ContractorItem(IdentifiedObject):
    """Contractor information for work task.Contractor information for work task.
    """

    def __init__(self, bidAmount=0.0, activityCode='', cost=0.0, WorkTask=None, ErpPayables=None, status=None, WorkCostDetail=None, *args, **kw_args):
        """Initialises a new 'ContractorItem' instance.

        @param bidAmount: The amount that a given contractor will charge for performing this unit of work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param cost: The total amount charged. 
        @param WorkTask:
        @param ErpPayables:
        @param status:
        @param WorkCostDetail:
        """
        #: The amount that a given contractor will charge for performing this unit of work.
        self.bidAmount = bidAmount

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        #: The total amount charged.
        self.cost = cost

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._ErpPayables = []
        self.ErpPayables = [] if ErpPayables is None else ErpPayables

        self.status = status

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        super(ContractorItem, self).__init__(*args, **kw_args)

    _attrs = ["bidAmount", "activityCode", "cost"]
    _attr_types = {"bidAmount": float, "activityCode": str, "cost": float}
    _defaults = {"bidAmount": 0.0, "activityCode": '', "cost": 0.0}
    _enums = {}
    _refs = ["WorkTask", "ErpPayables", "status", "WorkCostDetail"]
    _many_refs = ["ErpPayables"]

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.ContractorItems if x != self]
            self._WorkTask._ContractorItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._ContractorItems:
                self._WorkTask._ContractorItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getErpPayables(self):
        
        return self._ErpPayables

    def setErpPayables(self, value):
        for p in self._ErpPayables:
            filtered = [q for q in p.ContractorItems if q != self]
            self._ErpPayables._ContractorItems = filtered
        for r in value:
            if self not in r._ContractorItems:
                r._ContractorItems.append(self)
        self._ErpPayables = value

    ErpPayables = property(getErpPayables, setErpPayables)

    def addErpPayables(self, *ErpPayables):
        for obj in ErpPayables:
            if self not in obj._ContractorItems:
                obj._ContractorItems.append(self)
            self._ErpPayables.append(obj)

    def removeErpPayables(self, *ErpPayables):
        for obj in ErpPayables:
            if self in obj._ContractorItems:
                obj._ContractorItems.remove(self)
            self._ErpPayables.remove(obj)

    status = None

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.ContractorItems if x != self]
            self._WorkCostDetail._ContractorItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            if self not in self._WorkCostDetail._ContractorItems:
                self._WorkCostDetail._ContractorItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

