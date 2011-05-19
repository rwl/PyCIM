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

from CIM15.IEC61968.Common.ActivityRecord import ActivityRecord

class LoadMgmtRecord(ActivityRecord):
    """A log of actual measured load reductions as a result of load shed operations.A log of actual measured load reductions as a result of load shed operations.
    """

    def __init__(self, loadReduction=0.0, LoadMgmtFunction=None, *args, **kw_args):
        """Initialises a new 'LoadMgmtRecord' instance.

        @param loadReduction: The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation. 
        @param LoadMgmtFunction:
        """
        #: The measured reduction of the total load power as a result of the load shed activation. Thus it is the difference in power before and after the load shed operation.
        self.loadReduction = loadReduction

        self._LoadMgmtFunction = None
        self.LoadMgmtFunction = LoadMgmtFunction

        super(LoadMgmtRecord, self).__init__(*args, **kw_args)

    _attrs = ["loadReduction"]
    _attr_types = {"loadReduction": float}
    _defaults = {"loadReduction": 0.0}
    _enums = {}
    _refs = ["LoadMgmtFunction"]
    _many_refs = []

    def getLoadMgmtFunction(self):
        
        return self._LoadMgmtFunction

    def setLoadMgmtFunction(self, value):
        if self._LoadMgmtFunction is not None:
            filtered = [x for x in self.LoadMgmtFunction.LoadMgmtRecords if x != self]
            self._LoadMgmtFunction._LoadMgmtRecords = filtered

        self._LoadMgmtFunction = value
        if self._LoadMgmtFunction is not None:
            if self not in self._LoadMgmtFunction._LoadMgmtRecords:
                self._LoadMgmtFunction._LoadMgmtRecords.append(self)

    LoadMgmtFunction = property(getLoadMgmtFunction, setLoadMgmtFunction)

