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

class ContractorItem(IdentifiedObject):
    """Contractor information for work task.
    """

    def __init__(self, cost=0.0, bidAmount=0.0, activityCode='', WorkTask=None, WorkCostDetail=None, ErpPayables=None, status=None, **kw_args):
        """Initializes a new 'ContractorItem' instance.

        @param cost: The total amount charged. 
        @param bidAmount: The amount that a given contractor will charge for performing this unit of work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param WorkTask:
        @param WorkCostDetail:
        @param ErpPayables:
        @param status:
        """
        #: The total amount charged.
        self.cost = cost

        #: The amount that a given contractor will charge for performing this unit of work.
        self.bidAmount = bidAmount

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self._ErpPayables = []
        self.ErpPayables = [] if ErpPayables is None else ErpPayables

        self.status = status

        super(ContractorItem, self).__init__(**kw_args)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.ContractorItems if x != self]
            self._WorkTask._ContractorItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._ContractorItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.ContractorItems if x != self]
            self._WorkCostDetail._ContractorItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._ContractorItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

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

