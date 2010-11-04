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

class LaborItem(IdentifiedObject):
    """Labor used for work order.
    """

    def __init__(self, laborRate=0.0, cost=0.0, activityCode='', laborDuration=0.0, WorkCostDetail=None, ErpPersons=None, status=None, WorkTask=None, *args, **kw_args):
        """Initializes a new 'LaborItem' instance.

        @param laborRate: The labor rate applied for work. 
        @param cost: Total cost for labor. Note that this may not be able to be derived from labor rate and time charged. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param laborDuration: Time required to perform work. 
        @param WorkCostDetail:
        @param ErpPersons:
        @param status:
        @param WorkTask:
        """
        #: The labor rate applied for work.
        self.laborRate = laborRate

        #: Total cost for labor. Note that this may not be able to be derived from labor rate and time charged.
        self.cost = cost

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        #: Time required to perform work.
        self.laborDuration = laborDuration

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self.status = status

        self._WorkTask = None
        self.WorkTask = WorkTask

        super(LaborItem, self).__init__(*args, **kw_args)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.LaborItems if x != self]
            self._WorkCostDetail._LaborItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._LaborItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for p in self._ErpPersons:
            filtered = [q for q in p.LaborItems if q != self]
            self._ErpPersons._LaborItems = filtered
        for r in value:
            if self not in r._LaborItems:
                r._LaborItems.append(self)
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self not in obj._LaborItems:
                obj._LaborItems.append(self)
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            if self in obj._LaborItems:
                obj._LaborItems.remove(self)
            self._ErpPersons.remove(obj)

    status = None

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.LaborItems if x != self]
            self._WorkTask._LaborItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._LaborItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

