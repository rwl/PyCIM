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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class SwitchingOperation(IdentifiedObject):
    """A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.
    """

    def __init__(self, newState="open", operationTime='', Switches=None, OutageSchedule=None, *args, **kw_args):
        """Initialises a new 'SwitchingOperation' instance.

        @param newState: The switch position that shall result from this SwitchingOperation Values are: "open", "close"
        @param operationTime: Time of operation in same units as OutageSchedule.xAxixUnits. 
        @param Switches: A switch may be operated by many schedules.
        @param OutageSchedule: An OutageSchedule may operate many switches.
        """
        #: The switch position that shall result from this SwitchingOperation Values are: "open", "close"
        self.newState = newState

        #: Time of operation in same units as OutageSchedule.xAxixUnits.
        self.operationTime = operationTime

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        self._OutageSchedule = None
        self.OutageSchedule = OutageSchedule

        super(SwitchingOperation, self).__init__(*args, **kw_args)

    _attrs = ["newState", "operationTime"]
    _attr_types = {"newState": str, "operationTime": str}
    _defaults = {"newState": "open", "operationTime": ''}
    _enums = {"newState": "SwitchState"}
    _refs = ["Switches", "OutageSchedule"]
    _many_refs = ["Switches"]

    def getSwitches(self):
        """A switch may be operated by many schedules.
        """
        return self._Switches

    def setSwitches(self, value):
        for p in self._Switches:
            filtered = [q for q in p.SwitchingOperations if q != self]
            self._Switches._SwitchingOperations = filtered
        for r in value:
            if self not in r._SwitchingOperations:
                r._SwitchingOperations.append(self)
        self._Switches = value

    Switches = property(getSwitches, setSwitches)

    def addSwitches(self, *Switches):
        for obj in Switches:
            if self not in obj._SwitchingOperations:
                obj._SwitchingOperations.append(self)
            self._Switches.append(obj)

    def removeSwitches(self, *Switches):
        for obj in Switches:
            if self in obj._SwitchingOperations:
                obj._SwitchingOperations.remove(self)
            self._Switches.remove(obj)

    def getOutageSchedule(self):
        """An OutageSchedule may operate many switches.
        """
        return self._OutageSchedule

    def setOutageSchedule(self, value):
        if self._OutageSchedule is not None:
            filtered = [x for x in self.OutageSchedule.SwitchingOperations if x != self]
            self._OutageSchedule._SwitchingOperations = filtered

        self._OutageSchedule = value
        if self._OutageSchedule is not None:
            if self not in self._OutageSchedule._SwitchingOperations:
                self._OutageSchedule._SwitchingOperations.append(self)

    OutageSchedule = property(getOutageSchedule, setOutageSchedule)

