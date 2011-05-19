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

from CIM15.IEC61968.Assets.AssetInfo import AssetInfo

class ShuntImpedanceInfo(AssetInfo):
    """Properties of a shunt impedance.Properties of a shunt impedance.
    """

    def __init__(self, maxSwitchOperationCount=0, localControlKind="none", switchOperationCycle=0.0, vRegLineLine=False, highVoltageOverride=0.0, lowVoltageOverride=0.0, regBranch='', cellSize=0.0, localOnLevel='', regBranchKind="recloser", normalOpen=False, controlKind="remoteOnly", regBranchEnd=0, branchDirect=0, localOffLevel='', sensingPhaseCode="s12N", localOverride=False, ShuntCompensatorInfos=None, *args, **kw_args):
        """Initialises a new 'ShuntImpedanceInfo' instance.

        @param maxSwitchOperationCount: IdmsShuntImpedanceData.maxNumSwitchOps 
        @param localControlKind: Kind of local controller. Values are: "none", "temperature", "powerFactor", "voltage", "reactivePower", "time", "current"
        @param switchOperationCycle: Time interval between consecutive switching operations. 
        @param vRegLineLine: True if regulated voltages are measured line to line, otherwise they are measured line to ground. 
        @param highVoltageOverride: For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings. 
        @param lowVoltageOverride: For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings. 
        @param regBranch: For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch. 
        @param cellSize: The size of the individual units that make up the bank. 
        @param localOnLevel: Lower control setting. 
        @param regBranchKind: (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch. Values are: "recloser", "transformer", "breaker", "fuse", "switch", "sectionner", "other", "line"
        @param normalOpen: True if open is normal status for a fixed capacitor bank, otherwise normal status is closed. 
        @param controlKind: Kind of control (if any). Values are: "remoteOnly", "remoteWithLocalOverride", "localOnly", "fixed"
        @param regBranchEnd: For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer). 
        @param branchDirect: For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out. 
        @param localOffLevel: Upper control setting. 
        @param sensingPhaseCode: Phases that are measured for controlling the device. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param localOverride: True if the locally controlled capacitor has voltage override capability. 
        @param ShuntCompensatorInfos:
        """
        #: IdmsShuntImpedanceData.maxNumSwitchOps
        self.maxSwitchOperationCount = maxSwitchOperationCount

        #: Kind of local controller. Values are: "none", "temperature", "powerFactor", "voltage", "reactivePower", "time", "current"
        self.localControlKind = localControlKind

        #: Time interval between consecutive switching operations.
        self.switchOperationCycle = switchOperationCycle

        #: True if regulated voltages are measured line to line, otherwise they are measured line to ground.
        self.vRegLineLine = vRegLineLine

        #: For locally controlled shunt impedances which have a voltage override feature, the high voltage override value. If the voltage is above this value, the shunt impedance will be turned off regardless of the other local controller settings.
        self.highVoltageOverride = highVoltageOverride

        #: For locally controlled shunt impedances which have a voltage override feature, the low voltage override value. If the voltage is below this value, the shunt impedance will be turned on regardless of the other local controller settings.
        self.lowVoltageOverride = lowVoltageOverride

        #: For VAR, amp, or power factor locally controlled shunt impedances, the index of the regulation branch.
        self.regBranch = regBranch

        #: The size of the individual units that make up the bank.
        self.cellSize = cellSize

        #: Lower control setting.
        self.localOnLevel = localOnLevel

        #: (For VAR, amp, or power factor locally controlled shunt impedances) Kind of regulation branch. Values are: "recloser", "transformer", "breaker", "fuse", "switch", "sectionner", "other", "line"
        self.regBranchKind = regBranchKind

        #: True if open is normal status for a fixed capacitor bank, otherwise normal status is closed.
        self.normalOpen = normalOpen

        #: Kind of control (if any). Values are: "remoteOnly", "remoteWithLocalOverride", "localOnly", "fixed"
        self.controlKind = controlKind

        #: For VAR, amp, or power factor locally controlled shunt impedances, the end of the branch that is regulated. The field has the following values: from side, to side, and tertiary (only if the branch is a transformer).
        self.regBranchEnd = regBranchEnd

        #: For VAR, amp, or power factor locally controlled shunt impedances, the flow direction: in, out.
        self.branchDirect = branchDirect

        #: Upper control setting.
        self.localOffLevel = localOffLevel

        #: Phases that are measured for controlling the device. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.sensingPhaseCode = sensingPhaseCode

        #: True if the locally controlled capacitor has voltage override capability.
        self.localOverride = localOverride

        self._ShuntCompensatorInfos = []
        self.ShuntCompensatorInfos = [] if ShuntCompensatorInfos is None else ShuntCompensatorInfos

        super(ShuntImpedanceInfo, self).__init__(*args, **kw_args)

    _attrs = ["maxSwitchOperationCount", "localControlKind", "switchOperationCycle", "vRegLineLine", "highVoltageOverride", "lowVoltageOverride", "regBranch", "cellSize", "localOnLevel", "regBranchKind", "normalOpen", "controlKind", "regBranchEnd", "branchDirect", "localOffLevel", "sensingPhaseCode", "localOverride"]
    _attr_types = {"maxSwitchOperationCount": int, "localControlKind": str, "switchOperationCycle": float, "vRegLineLine": bool, "highVoltageOverride": float, "lowVoltageOverride": float, "regBranch": str, "cellSize": float, "localOnLevel": str, "regBranchKind": str, "normalOpen": bool, "controlKind": str, "regBranchEnd": int, "branchDirect": int, "localOffLevel": str, "sensingPhaseCode": str, "localOverride": bool}
    _defaults = {"maxSwitchOperationCount": 0, "localControlKind": "none", "switchOperationCycle": 0.0, "vRegLineLine": False, "highVoltageOverride": 0.0, "lowVoltageOverride": 0.0, "regBranch": '', "cellSize": 0.0, "localOnLevel": '', "regBranchKind": "recloser", "normalOpen": False, "controlKind": "remoteOnly", "regBranchEnd": 0, "branchDirect": 0, "localOffLevel": '', "sensingPhaseCode": "s12N", "localOverride": False}
    _enums = {"localControlKind": "ShuntImpedanceLocalControlKind", "regBranchKind": "RegulationBranchKind", "controlKind": "ShuntImpedanceControlKind", "sensingPhaseCode": "PhaseCode"}
    _refs = ["ShuntCompensatorInfos"]
    _many_refs = ["ShuntCompensatorInfos"]

    def getShuntCompensatorInfos(self):
        
        return self._ShuntCompensatorInfos

    def setShuntCompensatorInfos(self, value):
        for x in self._ShuntCompensatorInfos:
            x.ShuntImpedanceInfo = None
        for y in value:
            y._ShuntImpedanceInfo = self
        self._ShuntCompensatorInfos = value

    ShuntCompensatorInfos = property(getShuntCompensatorInfos, setShuntCompensatorInfos)

    def addShuntCompensatorInfos(self, *ShuntCompensatorInfos):
        for obj in ShuntCompensatorInfos:
            obj.ShuntImpedanceInfo = self

    def removeShuntCompensatorInfos(self, *ShuntCompensatorInfos):
        for obj in ShuntCompensatorInfos:
            obj.ShuntImpedanceInfo = None

