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

from CIM16.IEC61970.Core.ConductingEquipment import ConductingEquipment

class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.
    """

    def __init__(self, switchOnDate='', normalOpen=False, ratedCurrent=0.0, retained=False, switchOnCount=0, SwitchingOperations=None, LoadMgmtFunctions=None, ConnectDisconnectFunctions=None, SwitchSchedules=None, SwitchPhases=None, CompositeSwitch=None, *args, **kw_args):
        """Initialises a new 'Switch' instance.

        @param switchOnDate: The date and time when the switch was last switched on. 
        @param normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        @param ratedCurrent: The maximum continuous current carrying capacity in amps governed by the device material and construction. 
        @param retained: Branch is retained in a bus branch model. 
        @param switchOnCount: The switch on count since the switch was last reset or initialized. 
        @param SwitchingOperations: A switch may be operated by many schedules.
        @param LoadMgmtFunctions:
        @param ConnectDisconnectFunctions:
        @param SwitchSchedules: A Switch can be associated with SwitchSchedules.
        @param SwitchPhases:
        @param CompositeSwitch: Composite switch this Switch belongs to
        """
        #: The date and time when the switch was last switched on.
        self.switchOnDate = switchOnDate

        #: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
        self.normalOpen = normalOpen

        #: The maximum continuous current carrying capacity in amps governed by the device material and construction.
        self.ratedCurrent = ratedCurrent

        #: Branch is retained in a bus branch model.
        self.retained = retained

        #: The switch on count since the switch was last reset or initialized.
        self.switchOnCount = switchOnCount

        self._SwitchingOperations = []
        self.SwitchingOperations = [] if SwitchingOperations is None else SwitchingOperations

        self._LoadMgmtFunctions = []
        self.LoadMgmtFunctions = [] if LoadMgmtFunctions is None else LoadMgmtFunctions

        self._ConnectDisconnectFunctions = []
        self.ConnectDisconnectFunctions = [] if ConnectDisconnectFunctions is None else ConnectDisconnectFunctions

        self._SwitchSchedules = []
        self.SwitchSchedules = [] if SwitchSchedules is None else SwitchSchedules

        self._SwitchPhases = []
        self.SwitchPhases = [] if SwitchPhases is None else SwitchPhases

        self._CompositeSwitch = None
        self.CompositeSwitch = CompositeSwitch

        super(Switch, self).__init__(*args, **kw_args)

    _attrs = ["switchOnDate", "normalOpen", "ratedCurrent", "retained", "switchOnCount"]
    _attr_types = {"switchOnDate": str, "normalOpen": bool, "ratedCurrent": float, "retained": bool, "switchOnCount": int}
    _defaults = {"switchOnDate": '', "normalOpen": False, "ratedCurrent": 0.0, "retained": False, "switchOnCount": 0}
    _enums = {}
    _refs = ["SwitchingOperations", "LoadMgmtFunctions", "ConnectDisconnectFunctions", "SwitchSchedules", "SwitchPhases", "CompositeSwitch"]
    _many_refs = ["SwitchingOperations", "LoadMgmtFunctions", "ConnectDisconnectFunctions", "SwitchSchedules", "SwitchPhases"]

    def getSwitchingOperations(self):
        """A switch may be operated by many schedules.
        """
        return self._SwitchingOperations

    def setSwitchingOperations(self, value):
        for p in self._SwitchingOperations:
            filtered = [q for q in p.Switches if q != self]
            self._SwitchingOperations._Switches = filtered
        for r in value:
            if self not in r._Switches:
                r._Switches.append(self)
        self._SwitchingOperations = value

    SwitchingOperations = property(getSwitchingOperations, setSwitchingOperations)

    def addSwitchingOperations(self, *SwitchingOperations):
        for obj in SwitchingOperations:
            if self not in obj._Switches:
                obj._Switches.append(self)
            self._SwitchingOperations.append(obj)

    def removeSwitchingOperations(self, *SwitchingOperations):
        for obj in SwitchingOperations:
            if self in obj._Switches:
                obj._Switches.remove(self)
            self._SwitchingOperations.remove(obj)

    def getLoadMgmtFunctions(self):
        
        return self._LoadMgmtFunctions

    def setLoadMgmtFunctions(self, value):
        for p in self._LoadMgmtFunctions:
            filtered = [q for q in p.Switches if q != self]
            self._LoadMgmtFunctions._Switches = filtered
        for r in value:
            if self not in r._Switches:
                r._Switches.append(self)
        self._LoadMgmtFunctions = value

    LoadMgmtFunctions = property(getLoadMgmtFunctions, setLoadMgmtFunctions)

    def addLoadMgmtFunctions(self, *LoadMgmtFunctions):
        for obj in LoadMgmtFunctions:
            if self not in obj._Switches:
                obj._Switches.append(self)
            self._LoadMgmtFunctions.append(obj)

    def removeLoadMgmtFunctions(self, *LoadMgmtFunctions):
        for obj in LoadMgmtFunctions:
            if self in obj._Switches:
                obj._Switches.remove(self)
            self._LoadMgmtFunctions.remove(obj)

    def getConnectDisconnectFunctions(self):
        
        return self._ConnectDisconnectFunctions

    def setConnectDisconnectFunctions(self, value):
        for p in self._ConnectDisconnectFunctions:
            filtered = [q for q in p.Switches if q != self]
            self._ConnectDisconnectFunctions._Switches = filtered
        for r in value:
            if self not in r._Switches:
                r._Switches.append(self)
        self._ConnectDisconnectFunctions = value

    ConnectDisconnectFunctions = property(getConnectDisconnectFunctions, setConnectDisconnectFunctions)

    def addConnectDisconnectFunctions(self, *ConnectDisconnectFunctions):
        for obj in ConnectDisconnectFunctions:
            if self not in obj._Switches:
                obj._Switches.append(self)
            self._ConnectDisconnectFunctions.append(obj)

    def removeConnectDisconnectFunctions(self, *ConnectDisconnectFunctions):
        for obj in ConnectDisconnectFunctions:
            if self in obj._Switches:
                obj._Switches.remove(self)
            self._ConnectDisconnectFunctions.remove(obj)

    def getSwitchSchedules(self):
        """A Switch can be associated with SwitchSchedules.
        """
        return self._SwitchSchedules

    def setSwitchSchedules(self, value):
        for x in self._SwitchSchedules:
            x.Switch = None
        for y in value:
            y._Switch = self
        self._SwitchSchedules = value

    SwitchSchedules = property(getSwitchSchedules, setSwitchSchedules)

    def addSwitchSchedules(self, *SwitchSchedules):
        for obj in SwitchSchedules:
            obj.Switch = self

    def removeSwitchSchedules(self, *SwitchSchedules):
        for obj in SwitchSchedules:
            obj.Switch = None

    def getSwitchPhases(self):
        
        return self._SwitchPhases

    def setSwitchPhases(self, value):
        for x in self._SwitchPhases:
            x.Switch = None
        for y in value:
            y._Switch = self
        self._SwitchPhases = value

    SwitchPhases = property(getSwitchPhases, setSwitchPhases)

    def addSwitchPhases(self, *SwitchPhases):
        for obj in SwitchPhases:
            obj.Switch = self

    def removeSwitchPhases(self, *SwitchPhases):
        for obj in SwitchPhases:
            obj.Switch = None

    def getCompositeSwitch(self):
        """Composite switch this Switch belongs to
        """
        return self._CompositeSwitch

    def setCompositeSwitch(self, value):
        if self._CompositeSwitch is not None:
            filtered = [x for x in self.CompositeSwitch.Switches if x != self]
            self._CompositeSwitch._Switches = filtered

        self._CompositeSwitch = value
        if self._CompositeSwitch is not None:
            if self not in self._CompositeSwitch._Switches:
                self._CompositeSwitch._Switches.append(self)

    CompositeSwitch = property(getCompositeSwitch, setCompositeSwitch)

