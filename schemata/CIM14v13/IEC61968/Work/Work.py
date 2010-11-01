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

from CIM14v13.IEC61968.Common.Document import Document

class Work(Document):
    """Document used to request, initiate, track and record work. This is synonymous with Work Breakdown Structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.
    """

    def __init__(self, kind='service', requestDateTime='', priority='', WorkFlowSteps=None, Customers=None, WorkTasks=None, ErpProjectAccounting=None, Project=None, Designs=None, BusinessCase=None, WorkBillingInfo=None, WorkCostDetails=None, Request=None, *args, **kw_args):
        """Initializes a new 'Work' instance.

        @param kind: Kind of work. Values are: "service", "reconnect", "disconnect", "other", "meter", "construction", "inspection", "maintenance"
        @param requestDateTime: Date and time work was requested. 
        @param priority: Priority of work. 
        @param WorkFlowSteps:
        @param Customers: All the customers for which this work is performed.
        @param WorkTasks:
        @param ErpProjectAccounting:
        @param Project:
        @param Designs:
        @param BusinessCase:
        @param WorkBillingInfo:
        @param WorkCostDetails:
        @param Request:
        """
        #: Kind of work. Values are: "service", "reconnect", "disconnect", "other", "meter", "construction", "inspection", "maintenance"
        self.kind = kind

        #: Date and time work was requested. 
        self.requestDateTime = requestDateTime

        #: Priority of work. 
        self.priority = priority

        self._WorkFlowSteps = []
        self.WorkFlowSteps = [] if WorkFlowSteps is None else WorkFlowSteps

        self._Customers = []
        self.Customers = [] if Customers is None else Customers

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._Project = None
        self.Project = Project

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self._BusinessCase = None
        self.BusinessCase = BusinessCase

        self._WorkBillingInfo = None
        self.WorkBillingInfo = WorkBillingInfo

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._Request = None
        self.Request = Request

        super(Work, self).__init__(*args, **kw_args)

    def getWorkFlowSteps(self):
        
        return self._WorkFlowSteps

    def setWorkFlowSteps(self, value):
        for x in self._WorkFlowSteps:
            x._Work = None
        for y in value:
            y._Work = self
        self._WorkFlowSteps = value

    WorkFlowSteps = property(getWorkFlowSteps, setWorkFlowSteps)

    def addWorkFlowSteps(self, *WorkFlowSteps):
        for obj in WorkFlowSteps:
            obj._Work = self
            self._WorkFlowSteps.append(obj)

    def removeWorkFlowSteps(self, *WorkFlowSteps):
        for obj in WorkFlowSteps:
            obj._Work = None
            self._WorkFlowSteps.remove(obj)

    def getCustomers(self):
        """All the customers for which this work is performed.
        """
        return self._Customers

    def setCustomers(self, value):
        for p in self._Customers:
            filtered = [q for q in p.Works if q != self]
            self._Customers._Works = filtered
        for r in value:
            if self not in r._Works:
                r._Works.append(self)
        self._Customers = value

    Customers = property(getCustomers, setCustomers)

    def addCustomers(self, *Customers):
        for obj in Customers:
            if self not in obj._Works:
                obj._Works.append(self)
            self._Customers.append(obj)

    def removeCustomers(self, *Customers):
        for obj in Customers:
            if self in obj._Works:
                obj._Works.remove(self)
            self._Customers.remove(obj)

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x._Work = None
        for y in value:
            y._Work = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._Work = self
            self._WorkTasks.append(obj)

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj._Work = None
            self._WorkTasks.remove(obj)

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.Works if x != self]
            self._ErpProjectAccounting._Works = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            self._ErpProjectAccounting._Works.append(self)

    ErpProjectAccounting = property(getErpProjectAccounting, setErpProjectAccounting)

    def getProject(self):
        
        return self._Project

    def setProject(self, value):
        if self._Project is not None:
            filtered = [x for x in self.Project.Works if x != self]
            self._Project._Works = filtered

        self._Project = value
        if self._Project is not None:
            self._Project._Works.append(self)

    Project = property(getProject, setProject)

    def getDesigns(self):
        
        return self._Designs

    def setDesigns(self, value):
        for x in self._Designs:
            x._Work = None
        for y in value:
            y._Work = self
        self._Designs = value

    Designs = property(getDesigns, setDesigns)

    def addDesigns(self, *Designs):
        for obj in Designs:
            obj._Work = self
            self._Designs.append(obj)

    def removeDesigns(self, *Designs):
        for obj in Designs:
            obj._Work = None
            self._Designs.remove(obj)

    def getBusinessCase(self):
        
        return self._BusinessCase

    def setBusinessCase(self, value):
        if self._BusinessCase is not None:
            filtered = [x for x in self.BusinessCase.Works if x != self]
            self._BusinessCase._Works = filtered

        self._BusinessCase = value
        if self._BusinessCase is not None:
            self._BusinessCase._Works.append(self)

    BusinessCase = property(getBusinessCase, setBusinessCase)

    def getWorkBillingInfo(self):
        
        return self._WorkBillingInfo

    def setWorkBillingInfo(self, value):
        if self._WorkBillingInfo is not None:
            filtered = [x for x in self.WorkBillingInfo.Works if x != self]
            self._WorkBillingInfo._Works = filtered

        self._WorkBillingInfo = value
        if self._WorkBillingInfo is not None:
            self._WorkBillingInfo._Works.append(self)

    WorkBillingInfo = property(getWorkBillingInfo, setWorkBillingInfo)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for p in self._WorkCostDetails:
            filtered = [q for q in p.Works if q != self]
            self._WorkCostDetails._Works = filtered
        for r in value:
            if self not in r._Works:
                r._Works.append(self)
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            if self not in obj._Works:
                obj._Works.append(self)
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            if self in obj._Works:
                obj._Works.remove(self)
            self._WorkCostDetails.remove(obj)

    def getRequest(self):
        
        return self._Request

    def setRequest(self, value):
        if self._Request is not None:
            filtered = [x for x in self.Request.Works if x != self]
            self._Request._Works = filtered

        self._Request = value
        if self._Request is not None:
            self._Request._Works.append(self)

    Request = property(getRequest, setRequest)

