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

class LaborItem(IdentifiedObject):
    """Labor used for work order.Labor used for work order.
    """

    def __init__(self, cost=0.0, laborRate=0.0, laborDuration=0.0, activityCode='', ErpPersons=None, WorkTask=None, status=None, WorkCostDetail=None, *args, **kw_args):
        """Initialises a new 'LaborItem' instance.

        @param cost: Total cost for labor. Note that this may not be able to be derived from labor rate and time charged. 
        @param laborRate: The labor rate applied for work. 
        @param laborDuration: Time required to perform work. 
        @param activityCode: Activity code identifies a specific and distinguishable unit of work. 
        @param ErpPersons:
        @param WorkTask:
        @param status:
        @param WorkCostDetail:
        """
        #: Total cost for labor. Note that this may not be able to be derived from labor rate and time charged.
        self.cost = cost

        #: The labor rate applied for work.
        self.laborRate = laborRate

        #: Time required to perform work.
        self.laborDuration = laborDuration

        #: Activity code identifies a specific and distinguishable unit of work.
        self.activityCode = activityCode

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._WorkTask = None
        self.WorkTask = WorkTask

        self.status = status

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        super(LaborItem, self).__init__(*args, **kw_args)

    _attrs = ["cost", "laborRate", "laborDuration", "activityCode"]
    _attr_types = {"cost": float, "laborRate": float, "laborDuration": float, "activityCode": str}
    _defaults = {"cost": 0.0, "laborRate": 0.0, "laborDuration": 0.0, "activityCode": ''}
    _enums = {}
    _refs = ["ErpPersons", "WorkTask", "status", "WorkCostDetail"]
    _many_refs = ["ErpPersons"]

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

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.LaborItems if x != self]
            self._WorkTask._LaborItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._LaborItems:
                self._WorkTask._LaborItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    status = None

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.LaborItems if x != self]
            self._WorkCostDetail._LaborItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            if self not in self._WorkCostDetail._LaborItems:
                self._WorkCostDetail._LaborItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

