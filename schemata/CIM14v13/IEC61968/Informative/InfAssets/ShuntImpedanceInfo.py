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

from CIM14v13.IEC61968.Assets.ElectricalInfo import ElectricalInfo

class ShuntImpedanceInfo(ElectricalInfo):
    """Properties of a shunt impedance.
    """

    def __init__(self, controlKind='fixed', sensingPhaseCode='BC', regBranchKind='transformer', localControlKind='none', regBranch='', lowVoltageOverride=0.0, switchOperationCycle=0.0, highVoltageOverride=0.0, localOverride=False, regBranchEnd=0, localOffLevel='', branchDirect=0, normalOpen=False, cellSize=0.0, localOnLevel='', maxSwitchOperationCount=0, vRegLineLine=False, ShuntCompensatorTypeAsset=None, ShuntCompensatorAssetModel=None, ShuntCompensatorAssets=None, *args, **kw_args):
        """Initializes a new 'ShuntImpedanceInfo' instance.

        @param controlKind: Kind of control (if any). Values are: "fixed", "remoteWithLocalOverride", "remoteOnly", "localOnly"
        @param sensingPhaseCode: Phases that are measured for controlling the device. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param regBranchKind: (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch. Values are: "transformer", "line", "fuse", "sectionner", "other", "breaker", "switch", "recloser"
        @param localControlKind: Kind of local controller. Values are: "none", "current", "reactivePower", "time", "temperature", "voltage", "powerFactor"
        @param regBranch: For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch. 
        @param lowVoltageOverride: For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings. 
        @param switchOperationCycle: Time interval between consecutive switching operations. 
        @param highVoltageOverride: For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings. 
        @param localOverride: True if the locally controlled capacitor has voltage override capability. 
        @param regBranchEnd: For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer). 
        @param localOffLevel: Upper control setting. 
        @param branchDirect: For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out. 
        @param normalOpen: True if open is normal status for a fixed capacitor bank, otherwise normal status is closed. 
        @param cellSize: The size of the individual units that make up the bank. 
        @param localOnLevel: Lower control setting. 
        @param maxSwitchOperationCount: IdmsShuntImpedanceData.maxNumSwitchOps 
        @param vRegLineLine: True if regulated voltages are measured line to line, otherwise they are measured line to ground. 
        @param ShuntCompensatorTypeAsset:
        @param ShuntCompensatorAssetModel:
        @param ShuntCompensatorAssets:
        """
        #: Kind of control (if any).Values are: "fixed", "remoteWithLocalOverride", "remoteOnly", "localOnly"
        self.controlKind = controlKind

        #: Phases that are measured for controlling the device.Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.sensingPhaseCode = sensingPhaseCode

        #: (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch.Values are: "transformer", "line", "fuse", "sectionner", "other", "breaker", "switch", "recloser"
        self.regBranchKind = regBranchKind

        #: Kind of local controller.Values are: "none", "current", "reactivePower", "time", "temperature", "voltage", "powerFactor"
        self.localControlKind = localControlKind

        #: For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch.
        self.regBranch = regBranch

        #: For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings.
        self.lowVoltageOverride = lowVoltageOverride

        #: Time interval between consecutive switching operations.
        self.switchOperationCycle = switchOperationCycle

        #: For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings.
        self.highVoltageOverride = highVoltageOverride

        #: True if the locally controlled capacitor has voltage override capability.
        self.localOverride = localOverride

        #: For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer).
        self.regBranchEnd = regBranchEnd

        #: Upper control setting.
        self.localOffLevel = localOffLevel

        #: For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out.
        self.branchDirect = branchDirect

        #: True if open is normal status for a fixed capacitor bank, otherwise normal status is closed.
        self.normalOpen = normalOpen

        #: The size of the individual units that make up the bank.
        self.cellSize = cellSize

        #: Lower control setting.
        self.localOnLevel = localOnLevel

        #: IdmsShuntImpedanceData.maxNumSwitchOps
        self.maxSwitchOperationCount = maxSwitchOperationCount

        #: True if regulated voltages are measured line to line, otherwise they are measured line to ground.
        self.vRegLineLine = vRegLineLine

        self._ShuntCompensatorTypeAsset = None
        self.ShuntCompensatorTypeAsset = ShuntCompensatorTypeAsset

        self._ShuntCompensatorAssetModel = None
        self.ShuntCompensatorAssetModel = ShuntCompensatorAssetModel

        self._ShuntCompensatorAssets = []
        self.ShuntCompensatorAssets = [] if ShuntCompensatorAssets is None else ShuntCompensatorAssets

        super(ShuntImpedanceInfo, self).__init__(*args, **kw_args)

    def getShuntCompensatorTypeAsset(self):
        
        return self._ShuntCompensatorTypeAsset

    def setShuntCompensatorTypeAsset(self, value):
        if self._ShuntCompensatorTypeAsset is not None:
            self._ShuntCompensatorTypeAsset._ShuntImpedanceInfo = None

        self._ShuntCompensatorTypeAsset = value
        if self._ShuntCompensatorTypeAsset is not None:
            self._ShuntCompensatorTypeAsset._ShuntImpedanceInfo = self

    ShuntCompensatorTypeAsset = property(getShuntCompensatorTypeAsset, setShuntCompensatorTypeAsset)

    def getShuntCompensatorAssetModel(self):
        
        return self._ShuntCompensatorAssetModel

    def setShuntCompensatorAssetModel(self, value):
        if self._ShuntCompensatorAssetModel is not None:
            self._ShuntCompensatorAssetModel._ShuntImpedanceInfo = None

        self._ShuntCompensatorAssetModel = value
        if self._ShuntCompensatorAssetModel is not None:
            self._ShuntCompensatorAssetModel._ShuntImpedanceInfo = self

    ShuntCompensatorAssetModel = property(getShuntCompensatorAssetModel, setShuntCompensatorAssetModel)

    def getShuntCompensatorAssets(self):
        
        return self._ShuntCompensatorAssets

    def setShuntCompensatorAssets(self, value):
        for x in self._ShuntCompensatorAssets:
            x._ShuntImpedanceInfo = None
        for y in value:
            y._ShuntImpedanceInfo = self
        self._ShuntCompensatorAssets = value

    ShuntCompensatorAssets = property(getShuntCompensatorAssets, setShuntCompensatorAssets)

    def addShuntCompensatorAssets(self, *ShuntCompensatorAssets):
        for obj in ShuntCompensatorAssets:
            obj._ShuntImpedanceInfo = self
            self._ShuntCompensatorAssets.append(obj)

    def removeShuntCompensatorAssets(self, *ShuntCompensatorAssets):
        for obj in ShuntCompensatorAssets:
            obj._ShuntImpedanceInfo = None
            self._ShuntCompensatorAssets.remove(obj)

