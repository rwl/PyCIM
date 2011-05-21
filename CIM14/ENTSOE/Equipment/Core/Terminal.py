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

from CIM14.ENTSOE.Equipment.Core.IdentifiedObject import IdentifiedObject

class Terminal(IdentifiedObject):
    """An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.
    """

    def __init__(self, sequenceNumber=0, OperationalLimitSet=None, ConductingEquipment=None, HasFirst_MutualCoupling=None, Measurements=None, ConnectivityNode=None, RegulatingControl=None, TieFlow=None, HasSecond_MutualCoupling=None, *args, **kw_args):
        """Initialises a new 'Terminal' instance.

        @param sequenceNumber: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1. 
        @param OperationalLimitSet: The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        @param ConductingEquipment: ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes
        @param HasFirst_MutualCoupling: Mutual couplings associated with the branch as the first branch.
        @param Measurements: One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        @param ConnectivityNode: Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.
        @param RegulatingControl: The terminal is regulated by a control.
        @param TieFlow: The control area tie flows to which this terminal associates.
        @param HasSecond_MutualCoupling: Mutual couplings with the branch associated as the first branch.
        """
        #: The orientation of the terminal connections for a multiple terminal conducting equipment.  The sequence numbering starts with 1 and additional terminals should follow in increasing order.   The first terminal is the 'starting point' for a two terminal branch.   In the case of class TransformerWinding only one terminal is used so its sequenceNumber must be 1.
        self.sequenceNumber = sequenceNumber

        self._OperationalLimitSet = []
        self.OperationalLimitSet = [] if OperationalLimitSet is None else OperationalLimitSet

        self._ConductingEquipment = None
        self.ConductingEquipment = ConductingEquipment

        self._HasFirst_MutualCoupling = []
        self.HasFirst_MutualCoupling = [] if HasFirst_MutualCoupling is None else HasFirst_MutualCoupling

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._ConnectivityNode = None
        self.ConnectivityNode = ConnectivityNode

        self._RegulatingControl = []
        self.RegulatingControl = [] if RegulatingControl is None else RegulatingControl

        self._TieFlow = []
        self.TieFlow = [] if TieFlow is None else TieFlow

        self._HasSecond_MutualCoupling = []
        self.HasSecond_MutualCoupling = [] if HasSecond_MutualCoupling is None else HasSecond_MutualCoupling

        super(Terminal, self).__init__(*args, **kw_args)

    _attrs = ["sequenceNumber"]
    _attr_types = {"sequenceNumber": int}
    _defaults = {"sequenceNumber": 0}
    _enums = {}
    _refs = ["OperationalLimitSet", "ConductingEquipment", "HasFirst_MutualCoupling", "Measurements", "ConnectivityNode", "RegulatingControl", "TieFlow", "HasSecond_MutualCoupling"]
    _many_refs = ["OperationalLimitSet", "HasFirst_MutualCoupling", "Measurements", "RegulatingControl", "TieFlow", "HasSecond_MutualCoupling"]

    def getOperationalLimitSet(self):
        """The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.
        """
        return self._OperationalLimitSet

    def setOperationalLimitSet(self, value):
        for x in self._OperationalLimitSet:
            x.Terminal = None
        for y in value:
            y._Terminal = self
        self._OperationalLimitSet = value

    OperationalLimitSet = property(getOperationalLimitSet, setOperationalLimitSet)

    def addOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj.Terminal = self

    def removeOperationalLimitSet(self, *OperationalLimitSet):
        for obj in OperationalLimitSet:
            obj.Terminal = None

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
            if self not in self._ConductingEquipment._Terminals:
                self._ConductingEquipment._Terminals.append(self)

    ConductingEquipment = property(getConductingEquipment, setConductingEquipment)

    def getHasFirst_MutualCoupling(self):
        """Mutual couplings associated with the branch as the first branch.
        """
        return self._HasFirst_MutualCoupling

    def setHasFirst_MutualCoupling(self, value):
        for x in self._HasFirst_MutualCoupling:
            x.First_Terminal = None
        for y in value:
            y._First_Terminal = self
        self._HasFirst_MutualCoupling = value

    HasFirst_MutualCoupling = property(getHasFirst_MutualCoupling, setHasFirst_MutualCoupling)

    def addHasFirst_MutualCoupling(self, *HasFirst_MutualCoupling):
        for obj in HasFirst_MutualCoupling:
            obj.First_Terminal = self

    def removeHasFirst_MutualCoupling(self, *HasFirst_MutualCoupling):
        for obj in HasFirst_MutualCoupling:
            obj.First_Terminal = None

    def getMeasurements(self):
        """One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x.Terminal = None
        for y in value:
            y._Terminal = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.Terminal = self

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.Terminal = None

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
            if self not in self._ConnectivityNode._Terminals:
                self._ConnectivityNode._Terminals.append(self)

    ConnectivityNode = property(getConnectivityNode, setConnectivityNode)

    def getRegulatingControl(self):
        """The terminal is regulated by a control.
        """
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        for x in self._RegulatingControl:
            x.Terminal = None
        for y in value:
            y._Terminal = self
        self._RegulatingControl = value

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

    def addRegulatingControl(self, *RegulatingControl):
        for obj in RegulatingControl:
            obj.Terminal = self

    def removeRegulatingControl(self, *RegulatingControl):
        for obj in RegulatingControl:
            obj.Terminal = None

    def getTieFlow(self):
        """The control area tie flows to which this terminal associates.
        """
        return self._TieFlow

    def setTieFlow(self, value):
        for x in self._TieFlow:
            x.Terminal = None
        for y in value:
            y._Terminal = self
        self._TieFlow = value

    TieFlow = property(getTieFlow, setTieFlow)

    def addTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj.Terminal = self

    def removeTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj.Terminal = None

    def getHasSecond_MutualCoupling(self):
        """Mutual couplings with the branch associated as the first branch.
        """
        return self._HasSecond_MutualCoupling

    def setHasSecond_MutualCoupling(self, value):
        for x in self._HasSecond_MutualCoupling:
            x.Second_Terminal = None
        for y in value:
            y._Second_Terminal = self
        self._HasSecond_MutualCoupling = value

    HasSecond_MutualCoupling = property(getHasSecond_MutualCoupling, setHasSecond_MutualCoupling)

    def addHasSecond_MutualCoupling(self, *HasSecond_MutualCoupling):
        for obj in HasSecond_MutualCoupling:
            obj.Second_Terminal = self

    def removeHasSecond_MutualCoupling(self, *HasSecond_MutualCoupling):
        for obj in HasSecond_MutualCoupling:
            obj.Second_Terminal = None

