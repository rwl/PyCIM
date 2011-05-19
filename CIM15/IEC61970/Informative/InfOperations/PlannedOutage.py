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

class PlannedOutage(Document):
    """Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.
    """

    def __init__(self, kind="fixed", CustomerDatas=None, OutageSchedules=None, *args, **kw_args):
        """Initialises a new 'PlannedOutage' instance.

        @param kind: Kind of outage. Values are: "fixed", "flexible", "forced"
        @param CustomerDatas: All customers affected by this work. Derived from WorkOrder.connectedCustomers
        @param OutageSchedules:
        """
        #: Kind of outage. Values are: "fixed", "flexible", "forced"
        self.kind = kind

        self._CustomerDatas = []
        self.CustomerDatas = [] if CustomerDatas is None else CustomerDatas

        self._OutageSchedules = []
        self.OutageSchedules = [] if OutageSchedules is None else OutageSchedules

        super(PlannedOutage, self).__init__(*args, **kw_args)

    _attrs = ["kind"]
    _attr_types = {"kind": str}
    _defaults = {"kind": "fixed"}
    _enums = {"kind": "OutageKind"}
    _refs = ["CustomerDatas", "OutageSchedules"]
    _many_refs = ["CustomerDatas", "OutageSchedules"]

    def getCustomerDatas(self):
        """All customers affected by this work. Derived from WorkOrder.connectedCustomers
        """
        return self._CustomerDatas

    def setCustomerDatas(self, value):
        for x in self._CustomerDatas:
            x.PlannedOutage = None
        for y in value:
            y._PlannedOutage = self
        self._CustomerDatas = value

    CustomerDatas = property(getCustomerDatas, setCustomerDatas)

    def addCustomerDatas(self, *CustomerDatas):
        for obj in CustomerDatas:
            obj.PlannedOutage = self

    def removeCustomerDatas(self, *CustomerDatas):
        for obj in CustomerDatas:
            obj.PlannedOutage = None

    def getOutageSchedules(self):
        
        return self._OutageSchedules

    def setOutageSchedules(self, value):
        for x in self._OutageSchedules:
            x.PlannedOutage = None
        for y in value:
            y._PlannedOutage = self
        self._OutageSchedules = value

    OutageSchedules = property(getOutageSchedules, setOutageSchedules)

    def addOutageSchedules(self, *OutageSchedules):
        for obj in OutageSchedules:
            obj.PlannedOutage = self

    def removeOutageSchedules(self, *OutageSchedules):
        for obj in OutageSchedules:
            obj.PlannedOutage = None

