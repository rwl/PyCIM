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

class Terminal(IdentifiedObject):
    """An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.
    """

    def __init__(self, sequenceNumber=0, connected=False, ConductingEquipment=None, BushingAsset=None, HasSecond_MutualCoupling=None, OperationalLimitSet=None, HasFirst_MutualCoupling=None, TieFlow=None, Measurements=None, TopologicalNode=None, RegulatingControl=None, SvPowerFlow=None, TerminalConstraints=None, BranchGroupTerminal=None, ConnectivityNode=None, *args, **kw_args):
        """Initializes a new 'Terminal' instance.

        @param sequenceNumber: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        @param connected: The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm 
        @param ConductingEquipment: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param BushingAsset:
        @param HasSecond_MutualCoupling: Mutual couplings with the branch associated as the first branch.
        @param OperationalLimitSet: The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        @param HasFirst_MutualCoupling: Mutual couplings associated with the branch as the first branch.
        @param TieFlow: The control area tie flows to which this terminal associates.
        @param Measurements: One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        @param TopologicalNode: The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        @param RegulatingControl: The terminal is regulated by a control.
        @param SvPowerFlow: The power flow state associated with the terminal.
        @param TerminalConstraints:
        @param BranchGroupTerminal: The directed branch group terminals for which the terminal is monitored.
        @param ConnectivityNode: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        #: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        self.sequenceNumber = sequenceNumber

        #: The terminal connection status.   True implies the terminal is connected, and false implies the terminal is not connected. This is the result of topoplogical processing of a detailed Connectivity node and Switch model whether present in the model or not.   A terminal that is not connected cannot support a current flow.   A terminal that is connected may have flow.  In general a multi-terminal device may simultaneously have connected and disconnected terminals.  No other aspect of the algorithm 
        self.connected = connected

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        self._BushingAsset = None
        self.BushingAsset = BushingAsset

        self._HasSecond_MutualCoupling = []
        self.HasSecond_MutualCoupling = [] if HasSecond_MutualCoupling is None else HasSecond_MutualCoupling

        self._OperationalLimitSet = []
        self.OperationalLimitSet = [] if OperationalLimitSet is None else OperationalLimitSet

        self._HasFirst_MutualCoupling = []
        self.HasFirst_MutualCoupling = [] if HasFirst_MutualCoupling is None else HasFirst_MutualCoupling

        self._TieFlow = []
        self.TieFlow = [] if TieFlow is None else TieFlow

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._TopologicalNode = None
        self.TopologicalNode = TopologicalNode

        self._RegulatingControl = []
        self.RegulatingControl = [] if RegulatingControl is None else RegulatingControl

        self._SvPowerFlow = None
        self.SvPowerFlow = SvPowerFlow

        self._TerminalConstraints = []
        self.TerminalConstraints = [] if TerminalConstraints is None else TerminalConstraints

        self._BranchGroupTerminal = []
        self.BranchGroupTerminal = [] if BranchGroupTerminal is None else BranchGroupTerminal

        self._ConnectivityNode = None
        self.ConnectivityNode = ConnectivityNode

        super(Terminal, self).__init__(*args, **kw_args)

    def getConductingEquipment(self):
        """ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        """
        return self._ConductingEquipment

    def setConductingEquipment(self, value):
        if self._ConductingEquipment is not None:
            filtered = [x for x in self.ConductingEquipment.Terminals if x != self]
            self._ConductingEquipment._Terminals = filtered

        self._ConductingEquipment = value
        if self._ConductingEquipment is not None:
            self._ConductingEquipment._Terminals.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

    def getBushingAsset(self):
        
        return self._BushingAsset

    def setBushingAsset(self, value):
        if self._BushingAsset is not None:
            self._BushingAsset._Terminal = None

        self._BushingAsset = value
        if self._BushingAsset is not None:
            self._BushingAsset._Terminal = self

    BushingAsset = property(getBushingAsset, setBushingAsset)

    def getHasSecond_MutualCoupling(self):
        """Mutual couplings with the branch associated as the first branch.
        """
        return self._HasSecond_MutualCoupling

    def setHasSecond_MutualCoupling(self, value):
        for x in self._HasSecond_MutualCoupling:
            x._Second_Terminal = None
        for y in value:
            y._Second_Terminal = self
        self._HasSecond_MutualCoupling = value

    HasSecond_MutualCoupling = property(getHasSecond_MutualCoupling, setHasSecond_MutualCoupling)

    def addHasSecond_MutualCoupling(self, *HasSecond_MutualCoupling):
        for obj in HasSecond_MutualCoupling:
            obj._Second_Terminal = self
            self._HasSecond_MutualCoupling.append(obj)

    def removeHasSecond_MutualCoupling(self, *HasSecond_MutualCoupling):
        for obj in HasSecond_MutualCoupling:
            obj._Second_Terminal = None
            self._HasSecond_MutualCoupling.remove(obj)

    def getOperationalLimitSet(self):
        """The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        """
        return self._OperationalLimitSet

    def setOperationalLimitSet(self, value):
        for x in self._OperationalLimitSet:
            x._Terminal = None
        for y in value:
            y._Terminal = self
        self._OperationalLimitSet = value

    OperationalLimitSet = property(getOperationalLimitSet, setOperationalLimitSet)

    def addOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj._Terminal = self
            self._OperationalLimitSet.append(obj)

    def removeOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj._Terminal = None
            self._OperationalLimitSet.remove(obj)

    def getHasFirst_MutualCoupling(self):
        """Mutual couplings associated with the branch as the first branch.
        """
        return self._HasFirst_MutualCoupling

    def setHasFirst_MutualCoupling(self, value):
        for x in self._HasFirst_MutualCoupling:
            x._First_Terminal = None
        for y in value:
            y._First_Terminal = self
        self._HasFirst_MutualCoupling = value

    HasFirst_MutualCoupling = property(getHasFirst_MutualCoupling, setHasFirst_MutualCoupling)

    def addHasFirst_MutualCoupling(self, *HasFirst_MutualCoupling):
        for obj in HasFirst_MutualCoupling:
            obj._First_Terminal = self
            self._HasFirst_MutualCoupling.append(obj)

    def removeHasFirst_MutualCoupling(self, *HasFirst_MutualCoupling):
        for obj in HasFirst_MutualCoupling:
            obj._First_Terminal = None
            self._HasFirst_MutualCoupling.remove(obj)

    def getTieFlow(self):
        """The control area tie flows to which this terminal associates.
        """
        return self._TieFlow

    def setTieFlow(self, value):
        for x in self._TieFlow:
            x._Terminal = None
        for y in value:
            y._Terminal = self
        self._TieFlow = value

    TieFlow = property(getTieFlow, setTieFlow)

    def addTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj._Terminal = self
            self._TieFlow.append(obj)

    def removeTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj._Terminal = None
            self._TieFlow.remove(obj)

    def getMeasurements(self):
        """One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x._Terminal = None
        for y in value:
            y._Terminal = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Terminal = self
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Terminal = None
            self._Measurements.remove(obj)

    def getTopologicalNode(self):
        """The topological node associated with the terminal.   This can be used as an alternative to the connectivity node path to topological node, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.
        """
        return self._TopologicalNode

    def setTopologicalNode(self, value):
        if self._TopologicalNode is not None:
            filtered = [x for x in self.TopologicalNode.Terminal if x != self]
            self._TopologicalNode._Terminal = filtered

        self._TopologicalNode = value
        if self._TopologicalNode is not None:
            self._TopologicalNode._Terminal.append(self)

    TopologicalNode = property(getTopologicalNode, setTopologicalNode)

    def getRegulatingControl(self):
        """The terminal is regulated by a control.
        """
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        for x in self._RegulatingControl:
            x._Terminal = None
        for y in value:
            y._Terminal = self
        self._RegulatingControl = value

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

    def addRegulatingControl(self, *RegulatingControl):
        for obj in RegulatingControl:
            obj._Terminal = self
            self._RegulatingControl.append(obj)

    def removeRegulatingControl(self, *RegulatingControl):
        for obj in RegulatingControl:
            obj._Terminal = None
            self._RegulatingControl.remove(obj)

    def getSvPowerFlow(self):
        """The power flow state associated with the terminal.
        """
        return self._SvPowerFlow

    def setSvPowerFlow(self, value):
        if self._SvPowerFlow is not None:
            self._SvPowerFlow._Terminal = None

        self._SvPowerFlow = value
        if self._SvPowerFlow is not None:
            self._SvPowerFlow._Terminal = self

    SvPowerFlow = property(getSvPowerFlow, setSvPowerFlow)

    def getTerminalConstraints(self):
        
        return self._TerminalConstraints

    def setTerminalConstraints(self, value):
        for x in self._TerminalConstraints:
            x._Terminal = None
        for y in value:
            y._Terminal = self
        self._TerminalConstraints = value

    TerminalConstraints = property(getTerminalConstraints, setTerminalConstraints)

    def addTerminalConstraints(self, *TerminalConstraints):
        for obj in TerminalConstraints:
            obj._Terminal = self
            self._TerminalConstraints.append(obj)

    def removeTerminalConstraints(self, *TerminalConstraints):
        for obj in TerminalConstraints:
            obj._Terminal = None
            self._TerminalConstraints.remove(obj)

    def getBranchGroupTerminal(self):
        """The directed branch group terminals for which the terminal is monitored.
        """
        return self._BranchGroupTerminal

    def setBranchGroupTerminal(self, value):
        for x in self._BranchGroupTerminal:
            x._Terminal = None
        for y in value:
            y._Terminal = self
        self._BranchGroupTerminal = value

    BranchGroupTerminal = property(getBranchGroupTerminal, setBranchGroupTerminal)

    def addBranchGroupTerminal(self, *BranchGroupTerminal):
        for obj in BranchGroupTerminal:
            obj._Terminal = self
            self._BranchGroupTerminal.append(obj)

    def removeBranchGroupTerminal(self, *BranchGroupTerminal):
        for obj in BranchGroupTerminal:
            obj._Terminal = None
            self._BranchGroupTerminal.remove(obj)

    def getConnectivityNode(self):
        """Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        """
        return self._ConnectivityNode

    def setConnectivityNode(self, value):
        if self._ConnectivityNode is not None:
            filtered = [x for x in self.ConnectivityNode.Terminals if x != self]
            self._ConnectivityNode._Terminals = filtered

        self._ConnectivityNode = value
        if self._ConnectivityNode is not None:
            self._ConnectivityNode._Terminals.append(self)

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

