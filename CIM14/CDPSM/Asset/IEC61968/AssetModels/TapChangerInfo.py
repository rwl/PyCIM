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

from CIM15.CDPSM.Asset.IEC61968.Assets.AssetInfo import AssetInfo

class TapChangerInfo(AssetInfo):
    """Tap changer data.
    """

    def __init__(self, lowStep=0, frequency=0.0, ptRatio=0.0, ratedApparentPower=0.0, stepVoltageIncrement=0.0, ctRatio=0.0, ratedVoltage=0.0, neutralStep=0, ratedCurrent=0.0, ctRating=0.0, highStep=0, stepPhaseIncrement=0.0, neutralU=0.0, isTcul=False, *args, **kw_args):
        """Initialises a new 'TapChangerInfo' instance.

        @param lowStep: Lowest possible tap step position, retard from neutral. 
        @param frequency: Frequency at which the ratings apply. 
        @param ptRatio: Built-in voltage transducer ratio. 
        @param ratedApparentPower: Rated apparent power. 
        @param stepVoltageIncrement: Tap step increment, in per cent of rated voltage, per step position. 
        @param ctRatio: Built-in current transducer ratio. 
        @param ratedVoltage: Rated voltage. 
        @param neutralStep: The neutral tap step position for the winding. 
        @param ratedCurrent: Rated current. 
        @param ctRating: Built-in current transformer primary rating. 
        @param highStep: Highest possible tap step position, advance from neutral. 
        @param stepPhaseIncrement: Phase shift per step position. 
        @param neutralU: Voltage at which the winding operates at the neutral tap setting. 
        @param isTcul: Whether this tap changer has under load tap changing capabilities. 
        """
        #: Lowest possible tap step position, retard from neutral.
        self.lowStep = lowStep

        #: Frequency at which the ratings apply.
        self.frequency = frequency

        #: Built-in voltage transducer ratio.
        self.ptRatio = ptRatio

        #: Rated apparent power.
        self.ratedApparentPower = ratedApparentPower

        #: Tap step increment, in per cent of rated voltage, per step position.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: Built-in current transducer ratio.
        self.ctRatio = ctRatio

        #: Rated voltage.
        self.ratedVoltage = ratedVoltage

        #: The neutral tap step position for the winding.
        self.neutralStep = neutralStep

        #: Rated current.
        self.ratedCurrent = ratedCurrent

        #: Built-in current transformer primary rating.
        self.ctRating = ctRating

        #: Highest possible tap step position, advance from neutral.
        self.highStep = highStep

        #: Phase shift per step position.
        self.stepPhaseIncrement = stepPhaseIncrement

        #: Voltage at which the winding operates at the neutral tap setting.
        self.neutralU = neutralU

        #: Whether this tap changer has under load tap changing capabilities.
        self.isTcul = isTcul

        super(TapChangerInfo, self).__init__(*args, **kw_args)

    _attrs = ["lowStep", "frequency", "ptRatio", "ratedApparentPower", "stepVoltageIncrement", "ctRatio", "ratedVoltage", "neutralStep", "ratedCurrent", "ctRating", "highStep", "stepPhaseIncrement", "neutralU", "isTcul"]
    _attr_types = {"lowStep": int, "frequency": float, "ptRatio": float, "ratedApparentPower": float, "stepVoltageIncrement": float, "ctRatio": float, "ratedVoltage": float, "neutralStep": int, "ratedCurrent": float, "ctRating": float, "highStep": int, "stepPhaseIncrement": float, "neutralU": float, "isTcul": bool}
    _defaults = {"lowStep": 0, "frequency": 0.0, "ptRatio": 0.0, "ratedApparentPower": 0.0, "stepVoltageIncrement": 0.0, "ctRatio": 0.0, "ratedVoltage": 0.0, "neutralStep": 0, "ratedCurrent": 0.0, "ctRating": 0.0, "highStep": 0, "stepPhaseIncrement": 0.0, "neutralU": 0.0, "isTcul": False}
    _enums = {}
    _refs = []
    _many_refs = []

