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

class MiscCostItem(IdentifiedObject):
    """Various cost items that are not associated with compatible units. Examples include rental equipment, labor, materials, contractor costs, permits - anything not covered in a CU.
    """

    def __init__(self, costPerUnit=0.0, externalRefID='', costType='', quantity=0, account='', WorkCostDetail=None, DesignLocation=None, WorkTask=None, status=None, **kw_args):
        """Initializes a new 'MiscCostItem' instance.

        @param costPerUnit: The cost per unit for this misc. item. 
        @param externalRefID: External Reference ID (e.g. PO#, Serial #) 
        @param costType: The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead. 
        @param quantity: The quantity of the misc. item being assigned to this location. 
        @param account: This drives the accounting treatment for this misc. item. 
        @param WorkCostDetail:
        @param DesignLocation:
        @param WorkTask:
        @param status:
        """
        #: The cost per unit for this misc. item.
        self.costPerUnit = costPerUnit

        #: External Reference ID (e.g. PO#, Serial #)
        self.externalRefID = externalRefID

        #: The cost category for accounting, such as material, labor, vehicle, contractor, equipment, overhead.
        self.costType = costType

        #: The quantity of the misc. item being assigned to this location.
        self.quantity = quantity

        #: This drives the accounting treatment for this misc. item.
        self.account = account

        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        self._DesignLocation = None
        self.DesignLocation = DesignLocation

        self._WorkTask = None
        self.WorkTask = WorkTask

        self.status = status

        super(MiscCostItem, self).__init__(**kw_args)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            filtered = [x for x in self.WorkCostDetail.MiscCostItems if x != self]
            self._WorkCostDetail._MiscCostItems = filtered

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._MiscCostItems.append(self)

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

    def getDesignLocation(self):
        
        return self._DesignLocation

    def setDesignLocation(self, value):
        if self._DesignLocation is not None:
            filtered = [x for x in self.DesignLocation.MiscCostItems if x != self]
            self._DesignLocation._MiscCostItems = filtered

        self._DesignLocation = value
        if self._DesignLocation is not None:
            self._DesignLocation._MiscCostItems.append(self)

    DesignLocation = property(getDesignLocation, setDesignLocation)

    def getWorkTask(self):
        
        return self._WorkTask

    def setWorkTask(self, value):
        if self._WorkTask is not None:
            filtered = [x for x in self.WorkTask.MiscCostItems if x != self]
            self._WorkTask._MiscCostItems = filtered

        self._WorkTask = value
        if self._WorkTask is not None:
            self._WorkTask._MiscCostItems.append(self)

    WorkTask = property(getWorkTask, setWorkTask)

    status = None

