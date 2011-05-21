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
            x.ControlArea = None
        for y in value:
            y._ControlArea = self
        self._TieFlow = value

    TieFlow = property(getTieFlow, setTieFlow)

    def addTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj.ControlArea = self

    def removeTieFlow(self, *TieFlow):
        for obj in TieFlow:
            obj.ControlArea = None

    def getEnergyArea(self):
        """The energy area that is forecast from this control area specification.
        """
        return self._EnergyArea

    def setEnergyArea(self, value):
        if self._EnergyArea is not None:
            self._EnergyArea._ControlArea = None

        self._EnergyArea = value
        if self._EnergyArea is not None:
            self._EnergyArea.ControlArea = None
            self._EnergyArea._ControlArea = self

    EnergyArea = property(getEnergyArea, setEnergyArea)

    def getControlAreaGeneratingUnit(self):
        """The generating unit specificaitons for the control area.
        """
        return self._ControlAreaGeneratingUnit

    def setControlAreaGeneratingUnit(self, value):
        for x in self._ControlAreaGeneratingUnit:
            x.ControlArea = None
        for y in value:
            y._ControlArea = self
        self._ControlAreaGeneratingUnit = value

    ControlAreaGeneratingUnit = property(getControlAreaGeneratingUnit, setControlAreaGeneratingUnit)

    def addControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj.ControlArea = self

    def removeControlAreaGeneratingUnit(self, *ControlAreaGeneratingUnit):
        for obj in ControlAreaGeneratingUnit:
            obj.ControlArea = None

