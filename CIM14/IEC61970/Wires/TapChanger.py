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

class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions.
    """

    def __init__(self, stepVoltageIncrement=0.0, normalStep=0, neutralStep=0, subsequentDelay=0.0, regulationStatus=False, ltcFlag=False, highStep=0, initialDelay=0.0, lowStep=0, neutralU=0.0, SvTapStep=None, ImpedanceVariationCurve=None, TapSchedules=None, RegulatingControl=None, *args, **kw_args):
        """Initialises a new 'TapChanger' instance.

        @param stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        @param normalStep: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param neutralStep: The neutral tap step position for this winding. 
        @param subsequentDelay: For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        @param regulationStatus: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        @param ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. 
        @param highStep: Highest possible tap step position, advance from neutral 
        @param initialDelay: For an LTC, the delay for initial tap changer operation (first step change) 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param SvTapStep: The tap step state associated with the tap changer.
        @param ImpedanceVariationCurve: A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.
        @param TapSchedules: A TapChanger can have TapSchedules.
        @param RegulatingControl:
        """
        #: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
        self.normalStep = normalStep

        #: The neutral tap step position for this winding.
        self.neutralStep = neutralStep

        #: For an LTC, the delay for subsequent tap changer operation (second and later step changes)
        self.subsequentDelay = subsequentDelay

        #: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
        self.regulationStatus = regulationStatus

        #: Specifies whether or not a TapChanger has load tap changing capabilities.
        self.ltcFlag = ltcFlag

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        #: For an LTC, the delay for initial tap changer operation (first step change)
        self.initialDelay = initialDelay

        #: Lowest possible tap step position, retard from neutral
        self.lowStep = lowStep

        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        self._SvTapStep = None
        self.SvTapStep = SvTapStep

        self._ImpedanceVariationCurve = None
        self.ImpedanceVariationCurve = ImpedanceVariationCurve

        self._TapSchedules = []
        self.TapSchedules = [] if TapSchedules is None else TapSchedules

        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        super(TapChanger, self).__init__(*args, **kw_args)

    _attrs = ["stepVoltageIncrement", "normalStep", "neutralStep", "subsequentDelay", "regulationStatus", "ltcFlag", "highStep", "initialDelay", "lowStep", "neutralU"]
    _attr_types = {"stepVoltageIncrement": float, "normalStep": int, "neutralStep": int, "subsequentDelay": float, "regulationStatus": bool, "ltcFlag": bool, "highStep": int, "initialDelay": float, "lowStep": int, "neutralU": float}
    _defaults = {"stepVoltageIncrement": 0.0, "normalStep": 0, "neutralStep": 0, "subsequentDelay": 0.0, "regulationStatus": False, "ltcFlag": False, "highStep": 0, "initialDelay": 0.0, "lowStep": 0, "neutralU": 0.0}
    _enums = {}
    _refs = ["SvTapStep", "ImpedanceVariationCurve", "TapSchedules", "RegulatingControl"]
    _many_refs = ["TapSchedules"]

    def getSvTapStep(self):
        """The tap step state associated with the tap changer.
        """
        return self._SvTapStep

    def setSvTapStep(self, value):
        if self._SvTapStep is not None:
            self._SvTapStep._TapChanger = None

        self._SvTapStep = value
        if self._SvTapStep is not None:
            self._SvTapStep.TapChanger = None
            self._SvTapStep._TapChanger = self

    SvTapStep = property(getSvTapStep, setSvTapStep)

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

