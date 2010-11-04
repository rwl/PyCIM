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

class PlannedOutage(Document):
    """Planned outage involves network operations which will affect the supply of power to customers. Note that the list of Power System Resources for the PlannedOutage may be the same or a superset of the ones per OutageStep.
    """

    def __init__(self, kind='flexible', CustomerDatas=None, OutageSchedules=None, **kw_args):
        """Initializes a new 'PlannedOutage' instance.

        @param kind: Kind of outage. Values are: "flexible", "fixed", "forced"
        @param CustomerDatas: All customers affected by this work. Derived from WorkOrder.connectedCustomers
        @param OutageSchedules:
        """
        #: Kind of outage.Values are: "flexible", "fixed", "forced"
        self.kind = kind

        self._CustomerDatas = []
        self.CustomerDatas = [] if CustomerDatas is None else CustomerDatas

        self._OutageSchedules = []
        self.OutageSchedules = [] if OutageSchedules is None else OutageSchedules

        super(PlannedOutage, self).__init__(**kw_args)

    def getCustomerDatas(self):
        """All customers affected by this work. Derived from WorkOrder.connectedCustomers
        """
        return self._CustomerDatas

    def setCustomerDatas(self, value):
        for x in self._CustomerDatas:
            x._PlannedOutage = None
        for y in value:
            y._PlannedOutage = self
        self._CustomerDatas = value

    CustomerDatas = property(getCustomerDatas, setCustomerDatas)

    def addCustomerDatas(self, *CustomerDatas):
        for obj in CustomerDatas:
            obj._PlannedOutage = self
            self._CustomerDatas.append(obj)

    def removeCustomerDatas(self, *CustomerDatas):
        for obj in CustomerDatas:
            obj._PlannedOutage = None
            self._CustomerDatas.remove(obj)

    def getOutageSchedules(self):
        
        return self._OutageSchedules

    def setOutageSchedules(self, value):
        for x in self._OutageSchedules:
            x._PlannedOutage = None
        for y in value:
            y._PlannedOutage = self
        self._OutageSchedules = value

    OutageSchedules = property(getOutageSchedules, setOutageSchedules)

    def addOutageSchedules(self, *OutageSchedules):
        for obj in OutageSchedules:
            obj._PlannedOutage = self
            self._OutageSchedules.append(obj)

    def removeOutageSchedules(self, *OutageSchedules):
        for obj in OutageSchedules:
            obj._PlannedOutage = None
            self._OutageSchedules.remove(obj)

