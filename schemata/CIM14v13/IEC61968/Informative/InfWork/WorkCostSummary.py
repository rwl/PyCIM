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

class WorkCostSummary(Document):
    """A roll up by cost category for the entire cost of a work order. For example, total labor.
    """

    def __init__(self, WorkCostDetail=None, *args, **kw_args):
        """Initializes a new 'WorkCostSummary' instance.

        @param WorkCostDetail:
        """
        self._WorkCostDetail = None
        self.WorkCostDetail = WorkCostDetail

        super(WorkCostSummary, self).__init__(*args, **kw_args)

    def getWorkCostDetail(self):
        
        return self._WorkCostDetail

    def setWorkCostDetail(self, value):
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._WorkCostSummary = None

        self._WorkCostDetail = value
        if self._WorkCostDetail is not None:
            self._WorkCostDetail._WorkCostSummary = self

    WorkCostDetail = property(getWorkCostDetail, setWorkCostDetail)

