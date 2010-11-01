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

class ErpProjectAccounting(Document):
    """Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.
    """

    def __init__(self, Projects=None, WorkCostDetails=None, Works=None, ErpTimeEntries=None, *args, **kw_args):
        """Initializes a new 'ErpProjectAccounting' instance.

        @param Projects:
        @param WorkCostDetails:
        @param Works:
        @param ErpTimeEntries:
        """
        self._Projects = []
        self.Projects = [] if Projects is None else Projects

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        self._Works = []
        self.Works = [] if Works is None else Works

        self._ErpTimeEntries = []
        self.ErpTimeEntries = [] if ErpTimeEntries is None else ErpTimeEntries

        super(ErpProjectAccounting, self).__init__(*args, **kw_args)

    def getProjects(self):
        
        return self._Projects

    def setProjects(self, value):
        for x in self._Projects:
            x._ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._Projects = value

    Projects = property(getProjects, setProjects)

    def addProjects(self, *Projects):
        for obj in Projects:
            obj._ErpProjectAccounting = self
            self._Projects.append(obj)

    def removeProjects(self, *Projects):
        for obj in Projects:
            obj._ErpProjectAccounting = None
            self._Projects.remove(obj)

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x._ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._ErpProjectAccounting = self
            self._WorkCostDetails.append(obj)

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj._ErpProjectAccounting = None
            self._WorkCostDetails.remove(obj)

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x._ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj._ErpProjectAccounting = self
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            obj._ErpProjectAccounting = None
            self._Works.remove(obj)

    def getErpTimeEntries(self):
        
        return self._ErpTimeEntries

    def setErpTimeEntries(self, value):
        for x in self._ErpTimeEntries:
            x._ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._ErpTimeEntries = value

    ErpTimeEntries = property(getErpTimeEntries, setErpTimeEntries)

    def addErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj._ErpProjectAccounting = self
            self._ErpTimeEntries.append(obj)

    def removeErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj._ErpProjectAccounting = None
            self._ErpTimeEntries.remove(obj)

