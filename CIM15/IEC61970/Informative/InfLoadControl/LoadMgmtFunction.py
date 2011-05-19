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

from CIM15.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction

class LoadMgmtFunction(EndDeviceFunction):
    """A collective function at an end device that manages the customer load.A collective function at an end device that manages the customer load.
    """

    def __init__(self, schedulingBasis="remoteControl", remoteOverRide=False, isAutoOp=False, loadStatus="limitedLoad", manualOverRide=False, overRideTimeOut=0.0, Switches=None, LoadMgmtRecords=None, *args, **kw_args):
        """Initialises a new 'LoadMgmtFunction' instance.

        @param schedulingBasis: The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "remoteControl", "timeBased", "tariffBased", "manualControl"
        @param remoteOverRide: True if the currently active schedule is being remotely over-ridden to either shed load or to limit load. 
        @param isAutoOp: True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control. 
        @param loadStatus: The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "limitedLoad", "noLoad", "fullLoad"
        @param manualOverRide: True if the currently active schedule is being manually over-ridden to either shed load or to limit load. 
        @param overRideTimeOut: After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed. 
        @param Switches:
        @param LoadMgmtRecords:
        """
        #: The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "remoteControl", "timeBased", "tariffBased", "manualControl"
        self.schedulingBasis = schedulingBasis

        #: True if the currently active schedule is being remotely over-ridden to either shed load or to limit load.
        self.remoteOverRide = remoteOverRide

        #: True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control.
        self.isAutoOp = isAutoOp

        #: The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "limitedLoad", "noLoad", "fullLoad"
        self.loadStatus = loadStatus

        #: True if the currently active schedule is being manually over-ridden to either shed load or to limit load.
        self.manualOverRide = manualOverRide

        #: After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed.
        self.overRideTimeOut = overRideTimeOut

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        self._LoadMgmtRecords = []
        self.LoadMgmtRecords = [] if LoadMgmtRecords is None else LoadMgmtRecords

        super(LoadMgmtFunction, self).__init__(*args, **kw_args)

    _attrs = ["schedulingBasis", "remoteOverRide", "isAutoOp", "loadStatus", "manualOverRide", "overRideTimeOut"]
    _attr_types = {"schedulingBasis": str, "remoteOverRide": bool, "isAutoOp": bool, "loadStatus": str, "manualOverRide": bool, "overRideTimeOut": float}
    _defaults = {"schedulingBasis": "remoteControl", "remoteOverRide": False, "isAutoOp": False, "loadStatus": "limitedLoad", "manualOverRide": False, "overRideTimeOut": 0.0}
    _enums = {"schedulingBasis": "LoadMgmtKind", "loadStatus": "LoadStateKind"}
    _refs = ["Switches", "LoadMgmtRecords"]
    _many_refs = ["Switches", "LoadMgmtRecords"]

    def getSwitches(self):
        
        return self._Switches

    def setSwitches(self, value):
        for p in self._Switches:
            filtered = [q for q in p.LoadMgmtFunctions if q != self]
            self._Switches._LoadMgmtFunctions = filtered
        for r in value:
            if self not in r._LoadMgmtFunctions:
                r._LoadMgmtFunctions.append(self)
        self._Switches = value

    Switches = property(getSwitches, setSwitches)

    def addSwitches(self, *Switches):
        for obj in Switches:
            if self not in obj._LoadMgmtFunctions:
                obj._LoadMgmtFunctions.append(self)
            self._Switches.append(obj)

    def removeSwitches(self, *Switches):
        for obj in Switches:
            if self in obj._LoadMgmtFunctions:
                obj._LoadMgmtFunctions.remove(self)
            self._Switches.remove(obj)

    def getLoadMgmtRecords(self):
        
        return self._LoadMgmtRecords

    def setLoadMgmtRecords(self, value):
        for x in self._LoadMgmtRecords:
            x.LoadMgmtFunction = None
        for y in value:
            y._LoadMgmtFunction = self
        self._LoadMgmtRecords = value

    LoadMgmtRecords = property(getLoadMgmtRecords, setLoadMgmtRecords)

    def addLoadMgmtRecords(self, *LoadMgmtRecords):
        for obj in LoadMgmtRecords:
            obj.LoadMgmtFunction = self

    def removeLoadMgmtRecords(self, *LoadMgmtRecords):
        for obj in LoadMgmtRecords:
            obj.LoadMgmtFunction = None

