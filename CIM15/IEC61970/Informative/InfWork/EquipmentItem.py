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

class EquipmentItem(IdentifiedObject):
    """An equipment item, such as a vehicle, used for a work order.An equipment item, such as a vehicle, used for a work order.
    """

    def __init__(self, code='', cost=0.0, WorkTask=None, WorkCostDetail=None, status=None, *args, **kw_args):
        """Initialises a new 'EquipmentItem' instance.

        @param code: Code for type of vehicle. 
        @param cost: The cost for vehicle usage. 
        @param WorkTask:
        @param WorkCostDetail:
        @param status:
        """
        #: Code for type of vehicle.
        self.code = code

        #: The cost for vehicle usage.
        self.cost = cost

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self.status = status

        super(EquipmentItem, self).__init__(*args, **kw_args)

    _attrs = ["code", "cost"]
    _attr_types = {"code": str, "cost": float}
    _defaults = {"code": '', "cost": 0.0}
    _enums = {}
    _refs = ["WorkTask", "WorkCostDetail", "status"]
    _many_refs = []

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.EquipmentItems if x != self]
            self._WorkTask._EquipmentItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._EquipmentItems:
                self._WorkTask._EquipmentItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.EquipmentItems if x != self]
            self._WorkCostDetail._EquipmentItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            if self not in self._WorkCostDetail._EquipmentItems:
                self._WorkCostDetail._EquipmentItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

    status = None

