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

class EquipmentItem(IdentifiedObject):
    """An equipment item, such as a vehicle, used for a work order.
    """

    def __init__(self, cost=0.0, code='', WorkCostDetail=None, WorkTask=None, status=None, **kw_args):
        """Initializes a new 'EquipmentItem' instance.

        @param cost: The cost for vehicle usage. 
        @param code: Code for type of vehicle. 
        @param WorkCostDetail:
        @param WorkTask:
        @param status:
        """
        #: The cost for vehicle usage.
        self.cost = cost

        #: Code for type of vehicle.
        self.code = code

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self._WorkTask = None
        self.WorkTask = WorkTask

        self.status = status

        super(EquipmentItem, self).__init__(**kw_args)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.EquipmentItems if x != self]
            self._WorkCostDetail._EquipmentItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._EquipmentItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.EquipmentItems if x != self]
            self._WorkTask._EquipmentItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._EquipmentItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    status = None

