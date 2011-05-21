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

from CIM14.CPSM.Equipment.Core.PowerSystemResource import PowerSystemResource

class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions.
    """

    def __init__(self, stepVoltageIncrement=0.0, neutralStep=0, normalStep=0, ltcFlag=False, neutralU=0.0, lowStep=0, regulationStatus=False, highStep=0, TapSchedules=None, ImpedanceVariationCurve=None, RegulatingControl=None, *args, **kw_args):
        """Initialises a new 'TapChanger' instance.

        @param stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.This is required if the Tap Changer is a RatioTapChanger and there is no step change table. 
        @param neutralStep: The neutral tap step position for this winding. 
        @param normalStep: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. 
        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param regulationStatus: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        @param highStep: Highest possible tap step position, advance from neutral 
        @param TapSchedules: A TapChanger can have TapSchedules.
        @param ImpedanceVariationCurve: A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.
        @param RegulatingControl:
        """
        #: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.This is required if the Tap Changer is a RatioTapChanger and there is no step change table.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: The neutral tap step position for this winding.
        self.neutralStep = neutralStep

        #: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
        self.normalStep = normalStep

        #: Specifies whether or not a TapChanger has load tap changing capabilities.
        self.ltcFlag = ltcFlag

        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        #: Lowest possible tap step position, retard from neutral
        self.lowStep = lowStep

        #: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
        self.regulationStatus = regulationStatus

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        self._TapSchedules = []
        self.TapSchedules = [] if TapSchedules is None else TapSchedules

        self._ImpedanceVariationCurve = None
        self.ImpedanceVariationCurve = ImpedanceVariationCurve

        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        super(TapChanger, self).__init__(*args, **kw_args)

    _attrs = ["stepVoltageIncrement", "neutralStep", "normalStep", "ltcFlag", "neutralU", "lowStep", "regulationStatus", "highStep"]
    _attr_types = {"stepVoltageIncrement": float, "neutralStep": int, "normalStep": int, "ltcFlag": bool, "neutralU": float, "lowStep": int, "regulationStatus": bool, "highStep": int}
    _defaults = {"stepVoltageIncrement": 0.0, "neutralStep": 0, "normalStep": 0, "ltcFlag": False, "neutralU": 0.0, "lowStep": 0, "regulationStatus": False, "highStep": 0}
    _enums = {}
    _refs = ["TapSchedules", "ImpedanceVariationCurve", "RegulatingControl"]
    _many_refs = ["TapSchedules"]

    def getTapSchedules(self):
        """A TapChanger can have TapSchedules.
        """
        return self._TapSchedules

    def setTapSchedules(self, value):
        for x in self._TapSchedules:
            x.TapChanger = None
        for y in value:
            y._TapChanger = self
        self._TapSchedules = value

    TapSchedules = property(getTapSchedules, setTapSchedules)

    def addTapSchedules(self, *TapSchedules):
        for obj in TapSchedules:
            obj.TapChanger = self

    def removeTapSchedules(self, *TapSchedules):
        for obj in TapSchedules:
            obj.TapChanger = None

    def getImpedanceVariationCurve(self):
        """A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.
        """
        return self._ImpedanceVariationCurve

    def setImpedanceVariationCurve(self, value):
        if self._ImpedanceVariationCurve is not None:
            self._ImpedanceVariationCurve._TapChanger = None

        self._ImpedanceVariationCurve = value
        if self._ImpedanceVariationCurve is not None:
            self._ImpedanceVariationCurve.TapChanger = None
            self._ImpedanceVariationCurve._TapChanger = self

    ImpedanceVariationCurve = property(getImpedanceVariationCurve, setImpedanceVariationCurve)

    def getRegulatingControl(self):
        
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        if self._RegulatingControl is not None:
            filtered = [x for x in self.RegulatingControl.TapChanger if x != self]
            self._RegulatingControl._TapChanger = filtered

        self._RegulatingControl = value
        if self._RegulatingControl is not None:
            if self not in self._RegulatingControl._TapChanger:
                self._RegulatingControl._TapChanger.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

