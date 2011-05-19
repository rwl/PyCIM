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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class TapChanger(PowerSystemResource):
    """Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """

    def __init__(self, neutralU=0.0, regulationStatus=False, subsequentDelay=0.0, normalStep=0, ltcFlag=False, lowStep=0, neutralStep=0, initialDelay=0.0, highStep=0, TapChangerInfo=None, TapSchedules=None, TapChangerControl=None, SvTapStep=None, *args, **kw_args):
        """Initialises a new 'TapChanger' instance.

        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param regulationStatus: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        @param subsequentDelay: For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        @param normalStep: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param ltcFlag: Specifies whether or not a TapChanger has load tap changing capabilities. 
        @param lowStep: Lowest possible tap step position, retard from neutral 
        @param neutralStep: The neutral tap step position for this winding. 
        @param initialDelay: For an LTC, the delay for initial tap changer operation (first step change) 
        @param highStep: Highest possible tap step position, advance from neutral 
        @param TapChangerInfo: Data for this tap changer.
        @param TapSchedules: A TapChanger can have TapSchedules.
        @param TapChangerControl:
        @param SvTapStep: The tap step state associated with the tap changer.
        """
        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        #: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
        self.regulationStatus = regulationStatus

        #: For an LTC, the delay for subsequent tap changer operation (second and later step changes)
        self.subsequentDelay = subsequentDelay

        #: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
        self.normalStep = normalStep

        #: Specifies whether or not a TapChanger has load tap changing capabilities.
        self.ltcFlag = ltcFlag

        #: Lowest possible tap step position, retard from neutral
        self.lowStep = lowStep

        #: The neutral tap step position for this winding.
        self.neutralStep = neutralStep

        #: For an LTC, the delay for initial tap changer operation (first step change)
        self.initialDelay = initialDelay

        #: Highest possible tap step position, advance from neutral
        self.highStep = highStep

        self._TapChangerInfo = None
        self.TapChangerInfo = TapChangerInfo

        self._TapSchedules = []
        self.TapSchedules = [] if TapSchedules is None else TapSchedules

        self._TapChangerControl = None
        self.TapChangerControl = TapChangerControl

        self._SvTapStep = None
        self.SvTapStep = SvTapStep

        super(TapChanger, self).__init__(*args, **kw_args)

    _attrs = ["neutralU", "regulationStatus", "subsequentDelay", "normalStep", "ltcFlag", "lowStep", "neutralStep", "initialDelay", "highStep"]
    _attr_types = {"neutralU": float, "regulationStatus": bool, "subsequentDelay": float, "normalStep": int, "ltcFlag": bool, "lowStep": int, "neutralStep": int, "initialDelay": float, "highStep": int}
    _defaults = {"neutralU": 0.0, "regulationStatus": False, "subsequentDelay": 0.0, "normalStep": 0, "ltcFlag": False, "lowStep": 0, "neutralStep": 0, "initialDelay": 0.0, "highStep": 0}
    _enums = {}
    _refs = ["TapChangerInfo", "TapSchedules", "TapChangerControl", "SvTapStep"]
    _many_refs = ["TapSchedules"]

    def getTapChangerInfo(self):
        """Data for this tap changer.
        """
        return self._TapChangerInfo

    def setTapChangerInfo(self, value):
        if self._TapChangerInfo is not None:
            filtered = [x for x in self.TapChangerInfo.TapChangers if x != self]
            self._TapChangerInfo._TapChangers = filtered

        self._TapChangerInfo = value
        if self._TapChangerInfo is not None:
            if self not in self._TapChangerInfo._TapChangers:
                self._TapChangerInfo._TapChangers.append(self)

    TapChangerInfo = property(getTapChangerInfo, setTapChangerInfo)

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

    def getTapChangerControl(self):
        
        return self._TapChangerControl

    def setTapChangerControl(self, value):
        if self._TapChangerControl is not None:
            filtered = [x for x in self.TapChangerControl.TapChanger if x != self]
            self._TapChangerControl._TapChanger = filtered

        self._TapChangerControl = value
        if self._TapChangerControl is not None:
            if self not in self._TapChangerControl._TapChanger:
                self._TapChangerControl._TapChanger.append(self)

    TapChangerControl = property(getTapChangerControl, setTapChangerControl)

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

