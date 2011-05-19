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

class TapChangerInfo(AssetInfo):
    """Tap changer data.Tap changer data.
    """

    def __init__(self, ctRating=0.0, stepPhaseIncrement=0.0, ratedApparentPower=0.0, frequency=0.0, neutralU=0.0, ctRatio=0.0, stepVoltageIncrement=0.0, isTcul=False, neutralStep=0, ratedCurrent=0.0, lowStep=0, ratedVoltage=0.0, highStep=0, ptRatio=0.0, bil=0.0, TapChangers=None, *args, **kw_args):
        """Initialises a new 'TapChangerInfo' instance.

        @param ctRating: Built-in current transformer primary rating. 
        @param stepPhaseIncrement: Phase shift per step position. 
        @param ratedApparentPower: Rated apparent power. 
        @param frequency: Frequency at which the ratings apply. 
        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param ctRatio: Built-in current transducer ratio. 
        @param stepVoltageIncrement: Tap step increment, in per cent of rated voltage, per step position. 
        @param isTcul: Whether this tap changer has under load tap changing capabilities. 
        @param neutralStep: The neutral tap step position for the winding. 
        @param ratedCurrent: Rated current. 
        @param lowStep: Lowest possible tap step position, retard from neutral. 
        @param ratedVoltage: Rated voltage. 
        @param highStep: Highest possible tap step position, advance from neutral. 
        @param ptRatio: Built-in voltage transducer ratio. 
        @param bil: Basic Insulation Level (BIL) expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        @param TapChangers: All tap changers having this data.
        """
        #: Built-in current transformer primary rating.
        self.ctRating = ctRating

        #: Phase shift per step position.
        self.stepPhaseIncrement = stepPhaseIncrement

        #: Rated apparent power.
        self.ratedApparentPower = ratedApparentPower

        #: Frequency at which the ratings apply.
        self.frequency = frequency

        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        #: Built-in current transducer ratio.
        self.ctRatio = ctRatio

        #: Tap step increment, in per cent of rated voltage, per step position.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: Whether this tap changer has under load tap changing capabilities.
        self.isTcul = isTcul

        #: The neutral tap step position for the winding.
        self.neutralStep = neutralStep

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Lowest possible tap step position, retard from neutral.
        self.lowStep = lowStep

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: Highest possible tap step position, advance from neutral.
        self.highStep = highStep

        #: Built-in voltage transducer ratio.
        self.ptRatio = ptRatio

        #: Basic Insulation Level (BIL) expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges.
        self.bil = bil

        self._TapChangers = []
        self.TapChangers = [] if TapChangers is None else TapChangers

        super(TapChangerInfo, self).__init__(*args, **kw_args)

    _attrs = ["ctRating", "stepPhaseIncrement", "ratedApparentPower", "frequency", "neutralU", "ctRatio", "stepVoltageIncrement", "isTcul", "neutralStep", "ratedCurrent", "lowStep", "ratedVoltage", "highStep", "ptRatio", "bil"]
    _attr_types = {"ctRating": float, "stepPhaseIncrement": float, "ratedApparentPower": float, "frequency": float, "neutralU": float, "ctRatio": float, "stepVoltageIncrement": float, "isTcul": bool, "neutralStep": int, "ratedCurrent": float, "lowStep": int, "ratedVoltage": float, "highStep": int, "ptRatio": float, "bil": float}
    _defaults = {"ctRating": 0.0, "stepPhaseIncrement": 0.0, "ratedApparentPower": 0.0, "frequency": 0.0, "neutralU": 0.0, "ctRatio": 0.0, "stepVoltageIncrement": 0.0, "isTcul": False, "neutralStep": 0, "ratedCurrent": 0.0, "lowStep": 0, "ratedVoltage": 0.0, "highStep": 0, "ptRatio": 0.0, "bil": 0.0}
    _enums = {}
    _refs = ["TapChangers"]
    _many_refs = ["TapChangers"]

    def getTapChangers(self):
        """All tap changers having this data.
        """
        return self._TapChangers

    def setTapChangers(self, value):
        for x in self._TapChangers:
            x.TapChangerInfo = None
        for y in value:
            y._TapChangerInfo = self
        self._TapChangers = value

    TapChangers = property(getTapChangers, setTapChangers)

    def addTapChangers(self, *TapChangers):
        for obj in TapChangers:
            obj.TapChangerInfo = self

    def removeTapChangers(self, *TapChangers):
        for obj in TapChangers:
            obj.TapChangerInfo = None

