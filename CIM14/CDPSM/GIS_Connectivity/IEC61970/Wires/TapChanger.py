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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.PowerSystemResource import PowerSystemResource

class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions.
    """

    def __init__(self, stepVoltageIncrement=0.0, subsequentDelay=0.0, neutralStep=0, normalStep=0, ltcFlag=False, neutralU=0.0, lowStep=0, initialDelay=0.0, regulationStatus=False, highStep=0, SvTapStep=None, *args, **kw_args):
        """Initialises a new 'TapChanger' instance.

        @param stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        @param subsequentDelay: For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        @param neutralStep: The neutral tap step position for this winding. 
        @param normalStep: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. 
        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param initialDelay: For an LTC, the delay for initial tap changer operation (first step change) 
        @param regulationStatus: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        @param highStep: Highest possible tap step position, advance from neutral 
        @param SvTapStep: The tap step state associated with the tap changer.
        """
        #: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: For an LTC, the delay for subsequent tap changer operation (second and later step changes)
        self.subsequentDelay = subsequentDelay

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

        #: For an LTC, the delay for initial tap changer operation (first step change)
        self.initialDelay = initialDelay

        #: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
        self.regulationStatus = regulationStatus

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        self._SvTapStep = None
        self.SvTapStep = SvTapStep

        super(TapChanger, self).__init__(*args, **kw_args)

    _attrs = ["stepVoltageIncrement", "subsequentDelay", "neutralStep", "normalStep", "ltcFlag", "neutralU", "lowStep", "initialDelay", "regulationStatus", "highStep"]
    _attr_types = {"stepVoltageIncrement": float, "subsequentDelay": float, "neutralStep": int, "normalStep": int, "ltcFlag": bool, "neutralU": float, "lowStep": int, "initialDelay": float, "regulationStatus": bool, "highStep": int}
    _defaults = {"stepVoltageIncrement": 0.0, "subsequentDelay": 0.0, "neutralStep": 0, "normalStep": 0, "ltcFlag": False, "neutralU": 0.0, "lowStep": 0, "initialDelay": 0.0, "regulationStatus": False, "highStep": 0}
    _enums = {}
    _refs = ["SvTapStep"]
    _many_refs = []

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

