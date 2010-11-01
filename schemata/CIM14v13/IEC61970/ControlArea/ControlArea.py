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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class ControlArea(PowerSystemResource):
    """A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    def __init__(self, type='Interchange', pTolerance=0.0, netInterchange=0.0, EnergyArea=None, ControlAreaGeneratingUnit=None, TieFlow=None, *args, **kw_args):
        """Initializes a new 'ControlArea' instance.

        @param type: The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "Interchange", "AGC", "Forecast"
        @param pTolerance: Active power net interchange tolerance 
        @param netInterchange: The specified positive net interchange into the control area. 
        @param EnergyArea: The energy area that is forecast from this control area specification.
        @param ControlAreaGeneratingUnit: The generating unit specificaitons for the control area.
        @param TieFlow: The tie flows associated with the control area.
        """
        #: The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes. Values are: "Interchange", "AGC", "Forecast"
        self.type = type

        #: Active power net interchange tolerance 
        self.pTolerance = pTolerance

        #: The specified positive net interchange into the control area. 
        self.netInterchange = netInterchange

        self._EnergyArea = None
        self.EnergyArea = EnergyArea

        self._ControlAreaGeneratingUnit = []
        self.ControlAreaGeneratingUnit = [] if ControlAreaGeneratingUnit is None else ControlAreaGeneratingUnit

        self._TieFlow = []
        self.TieFlow = [] if TieFlow is None else TieFlow

        super(ControlArea, self).__init__(*args, **kw_args)

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

