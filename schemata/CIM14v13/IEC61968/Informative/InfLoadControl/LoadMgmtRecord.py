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

from CIM14v13.IEC61968.Common.ActivityRecord import ActivityRecord

class LoadMgmtRecord(ActivityRecord):
    """A log of actual measured load reductions as a result of load shed operations.
    """

    def __init__(self, loadReduction=0.0, LoadMgmtFunction=None, *args, **kw_args):
        """Initializes a new 'LoadMgmtRecord' instance.

        @param loadReduction: The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation. 
        @param LoadMgmtFunction:
        """
        #: The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation. 
        self.loadReduction = loadReduction

        self._LoadMgmtFunction = None
        self.LoadMgmtFunction = LoadMgmtFunction

        super(LoadMgmtRecord, self).__init__(*args, **kw_args)

    def getLoadMgmtFunction(self):
        
        return self._LoadMgmtFunction

    def setLoadMgmtFunction(self, value):
        if self._LoadMgmtFunction is not None:
            filtered = [x for x in self.LoadMgmtFunction.LoadMgmtRecords if x != self]
            self._LoadMgmtFunction._LoadMgmtRecords = filtered

        self._LoadMgmtFunction = value
        if self._LoadMgmtFunction is not None:
            self._LoadMgmtFunction._LoadMgmtRecords.append(self)

    LoadMgmtFunction = property(getLoadMgmtFunction, setLoadMgmtFunction)

