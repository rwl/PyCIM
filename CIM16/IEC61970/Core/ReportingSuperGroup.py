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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ReportingSuperGroup(IdentifiedObject):
    """A reporting super group, groups reporting groups for a higher level report.A reporting super group, groups reporting groups for a higher level report.
    """

    def __init__(self, ReportingGroup=None, *args, **kw_args):
        """Initialises a new 'ReportingSuperGroup' instance.

        @param ReportingGroup: Reporting groups that are grouped under this group group.
        """
        self._ReportingGroup = []
        self.ReportingGroup = [] if ReportingGroup is None else ReportingGroup

        super(ReportingSuperGroup, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ReportingGroup"]
    _many_refs = ["ReportingGroup"]

    def getReportingGroup(self):
        """Reporting groups that are grouped under this group group.
        """
        return self._ReportingGroup

    def setReportingGroup(self, value):
        for x in self._ReportingGroup:
            x.ReportingSuperGroup = None
        for y in value:
            y._ReportingSuperGroup = self
        self._ReportingGroup = value

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def addReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            obj.ReportingSuperGroup = self

    def removeReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            obj.ReportingSuperGroup = None

