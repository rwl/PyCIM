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

class OverheadCost(IdentifiedObject):
    """Overhead cost applied to work order.Overhead cost applied to work order.
    """

    def __init__(self, code='', cost=0.0, status=None, WorkCostDetails=None, WorkTasks=None, *args, **kw_args):
        """Initialises a new 'OverheadCost' instance.

        @param code: Overhead code. 
        @param cost: The overhead cost to be applied. 
        @param status:
        @param WorkCostDetails:
        @param WorkTasks:
        """
        #: Overhead code.
        self.code = code

        #: The overhead cost to be applied.
        self.cost = cost

        self.status = status

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        super(OverheadCost, self).__init__(*args, **kw_args)

    _attrs = ["code", "cost"]
    _attr_types = {"code": str, "cost": float}
    _defaults = {"code": '', "cost": 0.0}
    _enums = {}
    _refs = ["status", "WorkCostDetails", "WorkTasks"]
    _many_refs = ["WorkCostDetails", "WorkTasks"]

    status = None

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x.OverheadCost = None
        for y in value:
            y._OverheadCost = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.OverheadCost = self

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.OverheadCost = None

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x.OverheadCost = None
        for y in value:
            y._OverheadCost = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.OverheadCost = self

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.OverheadCost = None

