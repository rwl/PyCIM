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

from CIM15.IEC61968.Common.Document import Document

class Work(Document):
    """Document used to request, initiate, track and record work. This is synonymous with work breakdown structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.Document used to request, initiate, track and record work. This is synonymous with work breakdown structure (WBS), which is traversed through the (currently informative) recursive association of Work. Note that the work name is equal to the WBS name, which is given in the inherited 'name' attribute.
    """

    def __init__(self, kind="disconnect", priority='', requestDateTime='', Designs=None, WorkCostDetails=None, ErpProjectAccounting=None, Project=None, WorkFlowSteps=None, WorkTasks=None, BusinessCase=None, WorkBillingInfo=None, Request=None, Customers=None, *args, **kw_args):
        """Initialises a new 'Work' instance.

        @param kind: Kind of work. Values are: "disconnect", "other", "reconnect", "construction", "service", "meter", "inspection", "maintenance"
        @param priority: Priority of work. 
        @param requestDateTime: Date and time work was requested. 
        @param Designs:
        @param WorkCostDetails:
        @param ErpProjectAccounting:
        @param Project:
        @param WorkFlowSteps:
        @param WorkTasks:
        @param BusinessCase:
        @param WorkBillingInfo:
        @param Request:
        @param Customers: All the customers for which this work is performed.
        """
        #: Kind of work. Values are: "disconnect", "other", "reconnect", "construction", "service", "meter", "inspection", "maintenance"
        self.kind = kind

        #: Priority of work.
        self.priority = priority

        #: Date and time work was requested.
        self.requestDateTime = requestDateTime

        self._Designs = []
        self.Designs = [] if Designs is None else Designs

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._ErpProjectAccounting = None
        self.ErpProjectAccounting = ErpProjectAccounting

        self._Project = None
        self.Project = Project

        self._WorkFlowSteps = []
        self.WorkFlowSteps = [] if WorkFlowSteps is None else WorkFlowSteps

        self._WorkTasks = []
        self.WorkTasks = [] if WorkTasks is None else WorkTasks

        self._BusinessCase = None
        self.BusinessCase = BusinessCase

        self._WorkBillingInfo = None
        self.WorkBillingInfo = WorkBillingInfo

        self._Request = None
        self.Request = Request

        self._Customers = []
        self.Customers = [] if Customers is None else Customers

        super(Work, self).__init__(*args, **kw_args)

    _attrs = ["kind", "priority", "requestDateTime"]
    _attr_types = {"kind": str, "priority": str, "requestDateTime": str}
    _defaults = {"kind": "disconnect", "priority": '', "requestDateTime": ''}
    _enums = {"kind": "WorkKind"}
    _refs = ["Designs", "WorkCostDetails", "ErpProjectAccounting", "Project", "WorkFlowSteps", "WorkTasks", "BusinessCase", "WorkBillingInfo", "Request", "Customers"]
    _many_refs = ["Designs", "WorkCostDetails", "WorkFlowSteps", "WorkTasks", "Customers"]

    def getDesigns(self):
        
        return self._Designs

    def setDesigns(self, value):
        for x in self._Designs:
            x.Work = None
        for y in value:
            y._Work = self
        self._Designs = value

    Designs = property(getDesigns, setDesigns)

    def addDesigns(self, *Designs):
        for obj in Designs:
            obj.Work = self

    def removeDesigns(self, *Designs):
        for obj in Designs:
            obj.Work = None

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

    def getErpProjectAccounting(self):
        
        return self._ErpProjectAccounting

    def setErpProjectAccounting(self, value):
        if self._ErpProjectAccounting is not None:
            filtered = [x for x in self.ErpProjectAccounting.Works if x != self]
            self._ErpProjectAccounting._Works = filtered

        self._ErpProjectAccounting = value
        if self._ErpProjectAccounting is not None:
            if self not in self._ErpProjectAccounting._Works:
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
            if self not in self._Project._Works:
                self._Project._Works.append(self)

    Project = property(getProject, setProject)

    def getWorkFlowSteps(self):
        
        return self._WorkFlowSteps

    def setWorkFlowSteps(self, value):
        for x in self._WorkFlowSteps:
            x.Work = None
        for y in value:
            y._Work = self
        self._WorkFlowSteps = value

    WorkFlowSteps = property(getWorkFlowSteps, setWorkFlowSteps)

    def addWorkFlowSteps(self, *WorkFlowSteps):
        for obj in WorkFlowSteps:
            obj.Work = self

    def removeWorkFlowSteps(self, *WorkFlowSteps):
        for obj in WorkFlowSteps:
            obj.Work = None

    def getWorkTasks(self):
        
        return self._WorkTasks

    def setWorkTasks(self, value):
        for x in self._WorkTasks:
            x.Work = None
        for y in value:
            y._Work = self
        self._WorkTasks = value

    WorkTasks = property(getWorkTasks, setWorkTasks)

    def addWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.Work = self

    def removeWorkTasks(self, *WorkTasks):
        for obj in WorkTasks:
            obj.Work = None

    def getBusinessCase(self):
        
        return self._BusinessCase

    def setBusinessCase(self, value):
        if self._BusinessCase is not None:
            filtered = [x for x in self.BusinessCase.Works if x != self]
            self._BusinessCase._Works = filtered

        self._BusinessCase = value
        if self._BusinessCase is not None:
            if self not in self._BusinessCase._Works:
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
            if self not in self._WorkBillingInfo._Works:
                self._WorkBillingInfo._Works.append(self)

    WorkBillingInfo = property(getWorkBillingInfo, setWorkBillingInfo)

    def getRequest(self):
        
        return self._Request

    def setRequest(self, value):
        if self._Request is not None:
            filtered = [x for x in self.Request.Works if x != self]
            self._Request._Works = filtered

        self._Request = value
        if self._Request is not None:
            if self not in self._Request._Works:
                self._Request._Works.append(self)

    Request = property(getRequest, setRequest)

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

