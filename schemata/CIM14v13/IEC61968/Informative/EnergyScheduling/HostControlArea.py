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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class HostControlArea(IdentifiedObject):
    """A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load, including transmission and distribution losses.
    """

    def __init__(self, areaControlMode='OFF', frequencyBiasFactor=None, freqSetPoint=0.0, InadvertentAccounts=None, AreaReserveSpec=None, SideA_TieLines=None, SubControlAreas=None, SideB_TieLines=None, Receive_DynamicSchedules=None, Send_DynamicSchedules=None, Controls=None, *args, **kw_args):
        """Initializes a new 'HostControlArea' instance.

        @param areaControlMode: The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control) Values are: "OFF", "TLB", "CF", "CTL"
        @param frequencyBiasFactor: The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC) 
        @param freqSetPoint: The present power system frequency set point for automatic generation control 
        @param InadvertentAccounts: A control area can have one or more net inadvertent interchange accounts
        @param AreaReserveSpec: A control area has one or more area reserve specifications
        @param SideA_TieLines: A HostControlArea can have zero or more tie lines.
        @param SubControlAreas: The interchange area  may operate as a control area
        @param SideB_TieLines: A HostControlArea can have zero or more tie lines.
        @param Receive_DynamicSchedules: A control area can receive dynamic schedules from other control areas
        @param Send_DynamicSchedules: A control area can send dynamic schedules to other control areas
        @param Controls: A ControlAreaCompany controls a ControlArea.
        """
        #: The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or (OFF = off control) Values are: "OFF", "TLB", "CF", "CTL"
        self.areaControlMode = areaControlMode

        #: The control area's frequency bias factor, in active power per frequency, for automatic generation control (AGC) 
        self.frequencyBiasFactor = frequencyBiasFactor

        #: The present power system frequency set point for automatic generation control 
        self.freqSetPoint = freqSetPoint

        self._InadvertentAccounts = []
        self.InadvertentAccounts = [] if InadvertentAccounts is None else InadvertentAccounts

        self._AreaReserveSpec = None
        self.AreaReserveSpec = AreaReserveSpec

        self._SideA_TieLines = []
        self.SideA_TieLines = [] if SideA_TieLines is None else SideA_TieLines

        self._SubControlAreas = []
        self.SubControlAreas = [] if SubControlAreas is None else SubControlAreas

        self._SideB_TieLines = []
        self.SideB_TieLines = [] if SideB_TieLines is None else SideB_TieLines

        self._Receive_DynamicSchedules = []
        self.Receive_DynamicSchedules = [] if Receive_DynamicSchedules is None else Receive_DynamicSchedules

        self._Send_DynamicSchedules = []
        self.Send_DynamicSchedules = [] if Send_DynamicSchedules is None else Send_DynamicSchedules

        self._Controls = None
        self.Controls = Controls

        super(HostControlArea, self).__init__(*args, **kw_args)

    def getInadvertentAccounts(self):
        """A control area can have one or more net inadvertent interchange accounts
        """
        return self._InadvertentAccounts

    def setInadvertentAccounts(self, value):
        for x in self._InadvertentAccounts:
            x._HostControlArea = None
        for y in value:
            y._HostControlArea = self
        self._InadvertentAccounts = value

    InadvertentAccounts = property(getInadvertentAccounts, setInadvertentAccounts)

    def addInadvertentAccounts(self, *InadvertentAccounts):
        for obj in InadvertentAccounts:
            obj._HostControlArea = self
            self._InadvertentAccounts.append(obj)

    def removeInadvertentAccounts(self, *InadvertentAccounts):
        for obj in InadvertentAccounts:
            obj._HostControlArea = None
            self._InadvertentAccounts.remove(obj)

    def getAreaReserveSpec(self):
        """A control area has one or more area reserve specifications
        """
        return self._AreaReserveSpec

    def setAreaReserveSpec(self, value):
        if self._AreaReserveSpec is not None:
            filtered = [x for x in self.AreaReserveSpec.HostControlAreas if x != self]
            self._AreaReserveSpec._HostControlAreas = filtered

        self._AreaReserveSpec = value
        if self._AreaReserveSpec is not None:
            self._AreaReserveSpec._HostControlAreas.append(self)

    AreaReserveSpec = property(getAreaReserveSpec, setAreaReserveSpec)

    def getSideA_TieLines(self):
        """A HostControlArea can have zero or more tie lines.
        """
        return self._SideA_TieLines

    def setSideA_TieLines(self, value):
        for x in self._SideA_TieLines:
            x._SideA_HostControlArea = None
        for y in value:
            y._SideA_HostControlArea = self
        self._SideA_TieLines = value

    SideA_TieLines = property(getSideA_TieLines, setSideA_TieLines)

    def addSideA_TieLines(self, *SideA_TieLines):
        for obj in SideA_TieLines:
            obj._SideA_HostControlArea = self
            self._SideA_TieLines.append(obj)

    def removeSideA_TieLines(self, *SideA_TieLines):
        for obj in SideA_TieLines:
            obj._SideA_HostControlArea = None
            self._SideA_TieLines.remove(obj)

    def getSubControlAreas(self):
        """The interchange area  may operate as a control area
        """
        return self._SubControlAreas

    def setSubControlAreas(self, value):
        for x in self._SubControlAreas:
            x._HostControlArea = None
        for y in value:
            y._HostControlArea = self
        self._SubControlAreas = value

    SubControlAreas = property(getSubControlAreas, setSubControlAreas)

    def addSubControlAreas(self, *SubControlAreas):
        for obj in SubControlAreas:
            obj._HostControlArea = self
            self._SubControlAreas.append(obj)

    def removeSubControlAreas(self, *SubControlAreas):
        for obj in SubControlAreas:
            obj._HostControlArea = None
            self._SubControlAreas.remove(obj)

    def getSideB_TieLines(self):
        """A HostControlArea can have zero or more tie lines.
        """
        return self._SideB_TieLines

    def setSideB_TieLines(self, value):
        for x in self._SideB_TieLines:
            x._SideB_HostControlArea = None
        for y in value:
            y._SideB_HostControlArea = self
        self._SideB_TieLines = value

    SideB_TieLines = property(getSideB_TieLines, setSideB_TieLines)

    def addSideB_TieLines(self, *SideB_TieLines):
        for obj in SideB_TieLines:
            obj._SideB_HostControlArea = self
            self._SideB_TieLines.append(obj)

    def removeSideB_TieLines(self, *SideB_TieLines):
        for obj in SideB_TieLines:
            obj._SideB_HostControlArea = None
            self._SideB_TieLines.remove(obj)

    def getReceive_DynamicSchedules(self):
        """A control area can receive dynamic schedules from other control areas
        """
        return self._Receive_DynamicSchedules

    def setReceive_DynamicSchedules(self, value):
        for x in self._Receive_DynamicSchedules:
            x._Receive_HostControlArea = None
        for y in value:
            y._Receive_HostControlArea = self
        self._Receive_DynamicSchedules = value

    Receive_DynamicSchedules = property(getReceive_DynamicSchedules, setReceive_DynamicSchedules)

    def addReceive_DynamicSchedules(self, *Receive_DynamicSchedules):
        for obj in Receive_DynamicSchedules:
            obj._Receive_HostControlArea = self
            self._Receive_DynamicSchedules.append(obj)

    def removeReceive_DynamicSchedules(self, *Receive_DynamicSchedules):
        for obj in Receive_DynamicSchedules:
            obj._Receive_HostControlArea = None
            self._Receive_DynamicSchedules.remove(obj)

    def getSend_DynamicSchedules(self):
        """A control area can send dynamic schedules to other control areas
        """
        return self._Send_DynamicSchedules

    def setSend_DynamicSchedules(self, value):
        for x in self._Send_DynamicSchedules:
            x._Send_HostControlArea = None
        for y in value:
            y._Send_HostControlArea = self
        self._Send_DynamicSchedules = value

    Send_DynamicSchedules = property(getSend_DynamicSchedules, setSend_DynamicSchedules)

    def addSend_DynamicSchedules(self, *Send_DynamicSchedules):
        for obj in Send_DynamicSchedules:
            obj._Send_HostControlArea = self
            self._Send_DynamicSchedules.append(obj)

    def removeSend_DynamicSchedules(self, *Send_DynamicSchedules):
        for obj in Send_DynamicSchedules:
            obj._Send_HostControlArea = None
            self._Send_DynamicSchedules.remove(obj)

    def getControls(self):
        """A ControlAreaCompany controls a ControlArea.
        """
        return self._Controls

    def setControls(self, value):
        if self._Controls is not None:
            self._Controls._ControlledBy = None

        self._Controls = value
        if self._Controls is not None:
            self._Controls._ControlledBy = self

    Controls = property(getControls, setControls)

