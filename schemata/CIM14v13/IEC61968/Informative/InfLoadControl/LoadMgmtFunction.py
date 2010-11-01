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

from CIM14v13.IEC61968.Metering.DeviceFunction import DeviceFunction

class LoadMgmtFunction(DeviceFunction):
    """A collective function at an end device that manages the customer load.
    """

    def __init__(self, schedulingBasis='tariffBased', loadStatus='noLoad', manualOverRide=False, overRideTimeOut=0.0, remoteOverRide=False, isAutoOp=False, Switches=None, LoadMgmtRecords=None, *args, **kw_args):
        """Initializes a new 'LoadMgmtFunction' instance.

        @param schedulingBasis: The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "tariffBased", "remoteControl", "manualControl", "timeBased"
        @param loadStatus: The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "noLoad", "fullLoad", "limitedLoad"
        @param manualOverRide: True if the currently active schedule is being manually over-ridden to either shed load or to limit load. 
        @param overRideTimeOut: After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed. 
        @param remoteOverRide: True if the currently active schedule is being remotely over-ridden to either shed load or to limit load. 
        @param isAutoOp: True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control. 
        @param Switches:
        @param LoadMgmtRecords:
        """
        #: The basis of Load Management scheduling used here: Time Based, Tariff Based, Remote Control and Manual Control. Values are: "tariffBased", "remoteControl", "manualControl", "timeBased"
        self.schedulingBasis = schedulingBasis

        #: The present state of the load being either shed (noLoad), limited (limitedLoad) or fully connected (fullLoad). This refers only to the portion of the customer load that is under control of the LoadMgmtFunction. Values are: "noLoad", "fullLoad", "limitedLoad"
        self.loadStatus = loadStatus

        #: True if the currently active schedule is being manually over-ridden to either shed load or to limit load. 
        self.manualOverRide = manualOverRide

        #: After a command had been received to activate the mannualOverRide state or remoteOverRideState, the normal (halted) schedule will resume after this specified time duration had elapsed. 
        self.overRideTimeOut = overRideTimeOut

        #: True if the currently active schedule is being remotely over-ridden to either shed load or to limit load. 
        self.remoteOverRide = remoteOverRide

        #: True if LoadMgmtFunction operates under automatic control, otherwise it operates under manual control. 
        self.isAutoOp = isAutoOp

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        self._LoadMgmtRecords = []
        self.LoadMgmtRecords = [] if LoadMgmtRecords is None else LoadMgmtRecords

        super(LoadMgmtFunction, self).__init__(*args, **kw_args)

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
            x._LoadMgmtFunction = None
        for y in value:
            y._LoadMgmtFunction = self
        self._LoadMgmtRecords = value

    LoadMgmtRecords = property(getLoadMgmtRecords, setLoadMgmtRecords)

    def addLoadMgmtRecords(self, *LoadMgmtRecords):
        for obj in LoadMgmtRecords:
            obj._LoadMgmtFunction = self
            self._LoadMgmtRecords.append(obj)

    def removeLoadMgmtRecords(self, *LoadMgmtRecords):
        for obj in LoadMgmtRecords:
            obj._LoadMgmtFunction = None
            self._LoadMgmtRecords.remove(obj)

