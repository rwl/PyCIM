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

class OutageHistory(Document):
    """A document collecting OutageReports, that allows utilities to examine the number of outages suffered by a customer. Also provides data to calculate the total supply interruption to any customer over a given period.
    """

    def __init__(self, OutageReports=None, *args, **kw_args):
        """Initializes a new 'OutageHistory' instance.

        @param OutageReports: OutageReports per customer for which this OutageHistory is created.
        """
        self._OutageReports = []
        self.OutageReports = [] if OutageReports is None else OutageReports

        super(OutageHistory, self).__init__(*args, **kw_args)

    def getOutageReports(self):
        """OutageReports per customer for which this OutageHistory is created.
        """
        return self._OutageReports

    def setOutageReports(self, value):
        for x in self._OutageReports:
            x._OutageHistory = None
        for y in value:
            y._OutageHistory = self
        self._OutageReports = value

    OutageReports = property(getOutageReports, setOutageReports)

    def addOutageReports(self, *OutageReports):
        for obj in OutageReports:
            obj._OutageHistory = self
            self._OutageReports.append(obj)

    def removeOutageReports(self, *OutageReports):
        for obj in OutageReports:
            obj._OutageHistory = None
            self._OutageReports.remove(obj)

