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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more electric circuits.
    """

    def __init__(self, switchOnCount=0, switchOnDate='', retained=False, normalOpen=False, SwitchingOperations=None, CompositeSwitch=None, ConnectDisconnectFunctions=None, SwitchSchedules=None, *args, **kw_args):
        """Initialises a new 'Switch' instance.

        @param switchOnCount: The switch on count since the switch was last reset or initialized. 
        @param switchOnDate: The date and time when the switch was last switched on. 
        @param retained: Branch is retained in a bus branch model. 
        @param normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        @param SwitchingOperations: A switch may be operated by many schedules.
        @param CompositeSwitch: Composite switch this Switch belongs to
        @param ConnectDisconnectFunctions:
        @param SwitchSchedules: A Switch can be associated with SwitchSchedules.
        """
        #: The switch on count since the switch was last reset or initialized.
        self.switchOnCount = switchOnCount

        #: The date and time when the switch was last switched on.
        self.switchOnDate = switchOnDate

        #: Branch is retained in a bus branch model.
        self.retained = retained

        #: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
        self.normalOpen = normalOpen

        self._SwitchingOperations = []
        self.SwitchingOperations = [] if SwitchingOperations is None else SwitchingOperations

        self._CompositeSwitch = None
        self.CompositeSwitch = CompositeSwitch

        self._ConnectDisconnectFunctions = []
        self.ConnectDisconnectFunctions = [] if ConnectDisconnectFunctions is None else ConnectDisconnectFunctions

        self._SwitchSchedules = []
        self.SwitchSchedules = [] if SwitchSchedules is None else SwitchSchedules

        super(Switch, self).__init__(*args, **kw_args)

    _attrs = ["switchOnCount", "switchOnDate", "retained", "normalOpen"]
    _attr_types = {"switchOnCount": int, "switchOnDate": str, "retained": bool, "normalOpen": bool}
    _defaults = {"switchOnCount": 0, "switchOnDate": '', "retained": False, "normalOpen": False}
    _enums = {}
    _refs = ["SwitchingOperations", "CompositeSwitch", "ConnectDisconnectFunctions", "SwitchSchedules"]
    _many_refs = ["SwitchingOperations", "ConnectDisconnectFunctions", "SwitchSchedules"]

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

