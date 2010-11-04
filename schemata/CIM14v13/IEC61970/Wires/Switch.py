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

from CIM14v13.IEC61970.Core.ConductingEquipment import ConductingEquipment

class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more electric circuits.
    """

    def __init__(self, switchOnCount=0, normalOpen=False, retained=False, switchOnDate='', LoadMgmtFunctions=None, CompositeSwitch=None, SwitchSchedules=None, ConnectDisconnectFunctions=None, SwitchingOperations=None, **kw_args):
        """Initializes a new 'Switch' instance.

        @param switchOnCount: The switch on count since the switch was last reset or initialized. 
        @param normalOpen: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        @param retained: Branch is retained in a bus branch model. 
        @param switchOnDate: The date and time when the switch was last switched on. 
        @param LoadMgmtFunctions:
        @param CompositeSwitch: Composite switch this Switch belongs to
        @param SwitchSchedules: A Switch can be associated with SwitchSchedules.
        @param ConnectDisconnectFunctions:
        @param SwitchingOperations: A switch may be operated by many schedules.
        """
        #: The switch on count since the switch was last reset or initialized.
        self.switchOnCount = switchOnCount

        #: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
        self.normalOpen = normalOpen

        #: Branch is retained in a bus branch model.
        self.retained = retained

        #: The date and time when the switch was last switched on.
        self.switchOnDate = switchOnDate

        self._LoadMgmtFunctions = []
        self.LoadMgmtFunctions = [] if LoadMgmtFunctions is None else LoadMgmtFunctions

        self._CompositeSwitch = None
        self.CompositeSwitch = CompositeSwitch

        self._SwitchSchedules = []
        self.SwitchSchedules = [] if SwitchSchedules is None else SwitchSchedules

        self._ConnectDisconnectFunctions = []
        self.ConnectDisconnectFunctions = [] if ConnectDisconnectFunctions is None else ConnectDisconnectFunctions

        self._SwitchingOperations = []
        self.SwitchingOperations = [] if SwitchingOperations is None else SwitchingOperations

        super(Switch, self).__init__(**kw_args)

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
            self._CompositeSwitch._Switches.append(self)

    CompositeSwitch = property(getCompositeSwitch, setCompositeSwitch)

    def getSwitchSchedules(self):
        """A Switch can be associated with SwitchSchedules.
        """
        return self._SwitchSchedules

    def setSwitchSchedules(self, value):
        for x in self._SwitchSchedules:
            x._Switch = None
        for y in value:
            y._Switch = self
        self._SwitchSchedules = value

    SwitchSchedules = property(getSwitchSchedules, setSwitchSchedules)

    def addSwitchSchedules(self, *SwitchSchedules):
        for obj in SwitchSchedules:
            obj._Switch = self
            self._SwitchSchedules.append(obj)

    def removeSwitchSchedules(self, *SwitchSchedules):
        for obj in SwitchSchedules:
            obj._Switch = None
            self._SwitchSchedules.remove(obj)

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

