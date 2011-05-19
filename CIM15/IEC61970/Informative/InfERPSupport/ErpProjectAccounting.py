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

class ErpProjectAccounting(Document):
    """Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.Utility Project Accounting information, used by ERP applications to enable all relevant sub-systems that submit single sided transactions to transfer information with a Project Accounting Application. This would include, but not necessarily be limited to: Accounts Payable, Accounts Receivable, Budget, Order Management, Purchasing, Time and Labor, Travel and Expense.
    """

    def __init__(self, Works=None, Projects=None, ErpTimeEntries=None, WorkCostDetails=None, *args, **kw_args):
        """Initialises a new 'ErpProjectAccounting' instance.

        @param Works:
        @param Projects:
        @param ErpTimeEntries:
        @param WorkCostDetails:
        """
        self._Works = []
        self.Works = [] if Works is None else Works

        self._Projects = []
        self.Projects = [] if Projects is None else Projects

        self._ErpTimeEntries = []
        self.ErpTimeEntries = [] if ErpTimeEntries is None else ErpTimeEntries

        self._WorkCostDetails = []
        self.WorkCostDetails = [] if WorkCostDetails is None else WorkCostDetails

        super(ErpProjectAccounting, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Works", "Projects", "ErpTimeEntries", "WorkCostDetails"]
    _many_refs = ["Works", "Projects", "ErpTimeEntries", "WorkCostDetails"]

    def getWorks(self):
        
        return self._Works

    def setWorks(self, value):
        for x in self._Works:
            x.ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            obj.ErpProjectAccounting = self

    def removeWorks(self, *Works):
        for obj in Works:
            obj.ErpProjectAccounting = None

    def getProjects(self):
        
        return self._Projects

    def setProjects(self, value):
        for x in self._Projects:
            x.ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._Projects = value

    Projects = property(getProjects, setProjects)

    def addProjects(self, *Projects):
        for obj in Projects:
            obj.ErpProjectAccounting = self

    def removeProjects(self, *Projects):
        for obj in Projects:
            obj.ErpProjectAccounting = None

    def getErpTimeEntries(self):
        
        return self._ErpTimeEntries

    def setErpTimeEntries(self, value):
        for x in self._ErpTimeEntries:
            x.ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._ErpTimeEntries = value

    ErpTimeEntries = property(getErpTimeEntries, setErpTimeEntries)

    def addErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj.ErpProjectAccounting = self

    def removeErpTimeEntries(self, *ErpTimeEntries):
        for obj in ErpTimeEntries:
            obj.ErpProjectAccounting = None

    def getWorkCostDetails(self):
        
        return self._WorkCostDetails

    def setWorkCostDetails(self, value):
        for x in self._WorkCostDetails:
            x.ErpProjectAccounting = None
        for y in value:
            y._ErpProjectAccounting = self
        self._WorkCostDetails = value

    WorkCostDetails = property(getWorkCostDetails, setWorkCostDetails)

    def addWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.ErpProjectAccounting = self

    def removeWorkCostDetails(self, *WorkCostDetails):
        for obj in WorkCostDetails:
            obj.ErpProjectAccounting = None

