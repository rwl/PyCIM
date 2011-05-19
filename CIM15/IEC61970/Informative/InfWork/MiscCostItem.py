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

class MiscCostItem(IdentifiedObject):
    """Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.
    """

    def __init__(self, quantity="", costPerUnit=0.0, externalRefID='', account='', costType='', DesignLocation=None, status=None, WorkTask=None, WorkCostDetail=None, *args, **kw_args):
        """Initialises a new 'MiscCostItem' instance.

        @param quantity: The quantity of the misc. item being assigned to this location. 
        @param costPerUnit: The cost per unit for this misc. item. 
        @param externalRefID: External Reference ID (e.g. PO#, Serial #) 
        @param account: This drives the accounting treatment for this misc. item. 
        @param costType: The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead. 
        @param DesignLocation:
        @param status:
        @param WorkTask:
        @param WorkCostDetail:
        """
        #: The quantity of the misc. item being assigned to this location.
        self.quantity = quantity

        #: The cost per unit for this misc. item.
        self.costPerUnit = costPerUnit

        #: External Reference ID (e.g. PO#, Serial #)
        self.externalRefID = externalRefID

        #: This drives the accounting treatment for this misc. item.
        self.account = account

        #: The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead.
        self.costType = costType

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self.status = status

        self._WorkTask = None
        self.WorkTask = WorkTask

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        super(MiscCostItem, self).__init__(*args, **kw_args)

    _attrs = ["quantity", "costPerUnit", "externalRefID", "account", "costType"]
    _attr_types = {"quantity": str, "costPerUnit": float, "externalRefID": str, "account": str, "costType": str}
    _defaults = {"quantity": "", "costPerUnit": 0.0, "externalRefID": '', "account": '', "costType": ''}
    _enums = {}
    _refs = ["DesignLocation", "status", "WorkTask", "WorkCostDetail"]
    _many_refs = []

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.MiscCostItems if x != self]
            self._DesignLocation._MiscCostItems = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            if self not in self._DesignLocation._MiscCostItems:
                self._DesignLocation._MiscCostItems.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

    status = None

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.MiscCostItems if x != self]
            self._WorkTask._MiscCostItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            if self not in self._WorkTask._MiscCostItems:
                self._WorkTask._MiscCostItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.MiscCostItems if x != self]
            self._WorkCostDetail._MiscCostItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            if self not in self._WorkCostDetail._MiscCostItems:
                self._WorkCostDetail._MiscCostItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

