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

class OutageReport(Document):
    """Document with statistics of an outage.
    """

    def __init__(self, averageCml=0.0, outageDuration=0.0, customerCount=0, totalCml=0.0, OutageRecord=None, OutageHistory=None, **kw_args):
        """Initializes a new 'OutageReport' instance.

        @param averageCml: Average Customer Minutes Lost (CML) for this outage. 
        @param outageDuration: Total outage duration. 
        @param customerCount: Total number of outaged customers. 
        @param totalCml: Total Customer Minutes Lost (CML). 
        @param OutageRecord: reference to related document
        @param OutageHistory: OutageHistory of a customer, which may include this OutageReport.
        """
        #: Average Customer Minutes Lost (CML) for this outage.
        self.averageCml = averageCml

        #: Total outage duration.
        self.outageDuration = outageDuration

        #: Total number of outaged customers.
        self.customerCount = customerCount

        #: Total Customer Minutes Lost (CML).
        self.totalCml = totalCml

        self._OutageRecord = None
        self.OutageRecord = OutageRecord

        self._OutageHistory = None
        self.OutageHistory = OutageHistory

        super(OutageReport, self).__init__(**kw_args)

    def getOutageRecord(self):
        """reference to related document
        """
        return self._OutageRecord

    def setOutageRecord(self, value):
        if self._OutageRecord is not None:
            self._OutageRecord._OutageReport = None

        self._OutageRecord = value
        if self._OutageRecord is not None:
            self._OutageRecord._OutageReport = self

    OutageRecord = property(getOutageRecord, setOutageRecord)

    def getOutageHistory(self):
        """OutageHistory of a customer, which may include this OutageReport.
        """
        return self._OutageHistory

    def setOutageHistory(self, value):
        if self._OutageHistory is not None:
            filtered = [x for x in self.OutageHistory.OutageReports if x != self]
            self._OutageHistory._OutageReports = filtered

        self._OutageHistory = value
        if self._OutageHistory is not None:
            self._OutageHistory._OutageReports.append(self)

    OutageHistory = property(getOutageHistory, setOutageHistory)

