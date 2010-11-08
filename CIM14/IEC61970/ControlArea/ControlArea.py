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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class ControlArea(PowerSystemResource):
    """A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    def __init__(self, type="Interchange", netInterchange=0.0, pTolerance=0.0, TieFlow=None, EnergyArea=None, ControlAreaGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'ControlArea' instance.

        @param type: The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "Interchange", "Forecast", "AGC"
        @param netInterchange: The specified positive net interchange into the control area. 
        @param pTolerance: Active power net interchange tolerance 
        @param TieFlow: The tie flows associated with the control area.
        @param EnergyArea: The energy area that is forecast from this control area specification.
        @param ControlAreaGeneratingUnit: The generating unit specificaitons for the control area.
        """
        #: The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "Interchange", "Forecast", "AGC"
        self.type = type

        #: The specified positive net interchange into the control area.
        self.netInterchange = netInterchange

        #: Active power net interchange tolerance
        self.pTolerance = pTolerance

        self._TieFlow = []
        self.TieFlow = [] if TieFlow is None else TieFlow

        self._EnergyArea = None
        self.EnergyArea = EnergyArea

        self._ControlAreaGeneratingUnit = []
        self.ControlAreaGeneratingUnit = [] if ControlAreaGeneratingUnit is None else ControlAreaGeneratingUnit

        super(ControlArea, self).__init__(*args, **kw_args)

    _attrs = ["type", "netInterchange", "pTolerance"]
    _attr_types = {"type": str, "netInterchange": float, "pTolerance": float}
    _defaults = {"type": "Interchange", "netInterchange": 0.0, "pTolerance": 0.0}
    _enums = {"type": "ControlAreaTypeKind"}
    _refs = ["TieFlow", "EnergyArea", "ControlAreaGeneratingUnit"]
    _many_refs = ["TieFlow", "ControlAreaGeneratingUnit"]

    def getTieFlow(self):
        """The tie flows associated with the control area.
        """
        return self._TieFlow

    def setTieFlow(self, value):
        for x in self._TieFlow:
            x._ControlArea = None
        for y in value:
            y._ControlArea = self
        self._TieFlow = value

    TieFlow = property(getTieFlow, setTieFlow)

    def addTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj._ControlArea = self
            self._TieFlow.append(obj)

    def removeTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj._ControlArea = None
            self._TieFlow.remove(obj)

    def getEnergyArea(self):
        """The energy area that is forecast from this control area specification.
        """
        return self._EnergyArea

    def setEnergyArea(self, value):
        if self._EnergyArea is not None:
            self._EnergyArea._ControlArea = None

        self._EnergyArea = value
        if self._EnergyArea is not None:
            self._EnergyArea._ControlArea = self

    EnergyArea = property(getEnergyArea, setEnergyArea)

    def getControlAreaGeneratingUnit(self):
        """The generating unit specificaitons for the control area.
        """
        return self._ControlAreaGeneratingUnit

    def setControlAreaGeneratingUnit(self, value):
        for x in self._ControlAreaGeneratingUnit:
            x._ControlArea = None
        for y in value:
            y._ControlArea = self
        self._ControlAreaGeneratingUnit = value

    ControlAreaGeneratingUnit = property(getControlAreaGeneratingUnit, setControlAreaGeneratingUnit)

    def addControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj._ControlArea = self
            self._ControlAreaGeneratingUnit.append(obj)

    def removeControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj._ControlArea = None
            self._ControlAreaGeneratingUnit.remove(obj)

