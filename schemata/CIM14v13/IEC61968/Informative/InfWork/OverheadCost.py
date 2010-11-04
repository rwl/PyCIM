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

class OverheadCost(IdentifiedObject):
    """Overhead cost applied to work order.
    """

    def __init__(self, cost=0.0, code='', WorkCostDetails=None, WorkTasks=None, status=None, **kw_args):
        """Initializes a new 'OverheadCost' instance.

        @param cost: The overhead cost to be applied. 
        @param code: Overhead code. 
        @param WorkCostDetails:
        @param WorkTasks:
        @param status:
        """
        #: The overhead cost to be applied.
        self.cost = cost

        #: Overhead code.
        self.code = code

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self.status = status

        super(OverheadCost, self).__init__(**kw_args)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x._OverheadCost = None
        for y in value:
            y._OverheadCost = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._OverheadCost = self
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._OverheadCost = None
            self._WorkCostDetails.remove(obj)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x._OverheadCost = None
        for y in value:
            y._OverheadCost = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._OverheadCost = self
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._OverheadCost = None
            self._WorkTasks.remove(obj)

    status = None

