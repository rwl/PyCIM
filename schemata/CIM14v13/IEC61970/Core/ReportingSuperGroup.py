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

class ReportingSuperGroup(IdentifiedObject):
    """A reporting super group, groups reporting groups for a higher level report.
    """

    def __init__(self, ReportingGroup=None, *args, **kw_args):
        """Initializes a new 'ReportingSuperGroup' instance.

        @param ReportingGroup: Reporting groups that are grouped under this group group.
        """
        self._ReportingGroup = []
        self.ReportingGroup = [] if ReportingGroup is None else ReportingGroup

        super(ReportingSuperGroup, self).__init__(*args, **kw_args)

    def getReportingGroup(self):
        """Reporting groups that are grouped under this group group.
        """
        return self._ReportingGroup

    def setReportingGroup(self, value):
        for x in self._ReportingGroup:
            x._ReportingSuperGroup = None
        for y in value:
            y._ReportingSuperGroup = self
        self._ReportingGroup = value

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def addReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            obj._ReportingSuperGroup = self
            self._ReportingGroup.append(obj)

    def removeReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            obj._ReportingSuperGroup = None
            self._ReportingGroup.remove(obj)

