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

from CIM15.IEC61970.Wires.TapChanger import TapChanger

class RatioTapChanger(TapChanger):
    """A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.A tap changer that changes the voltage ratio impacting the voltage magnitude but not the phase angle across the transformer.
    """

    def __init__(self, stepVoltageIncrement=0.0, tculControlMode="reactive", RatioTapChangerTabular=None, TransformerEnd=None, *args, **kw_args):
        """Initialises a new 'RatioTapChanger' instance.

        @param stepVoltageIncrement: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        @param tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        @param RatioTapChangerTabular:
        @param TransformerEnd: Transformer end to which this ratio tap changer belongs.
        """
        #: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
        self.stepVoltageIncrement = stepVoltageIncrement

        #: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        self.tculControlMode = tculControlMode

        self._RatioTapChangerTabular = None
        self.RatioTapChangerTabular = RatioTapChangerTabular

        self._TransformerEnd = None
        self.TransformerEnd = TransformerEnd

        super(RatioTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["stepVoltageIncrement", "tculControlMode"]
    _attr_types = {"stepVoltageIncrement": float, "tculControlMode": str}
    _defaults = {"stepVoltageIncrement": 0.0, "tculControlMode": "reactive"}
    _enums = {"tculControlMode": "TransformerControlMode"}
    _refs = ["RatioTapChangerTabular", "TransformerEnd"]
    _many_refs = []

    def getRatioTapChangerTabular(self):
        
        return self._RatioTapChangerTabular

    def setRatioTapChangerTabular(self, value):
        if self._RatioTapChangerTabular is not None:
            filtered = [x for x in self.RatioTapChangerTabular.RatioTapChanger if x != self]
            self._RatioTapChangerTabular._RatioTapChanger = filtered

        self._RatioTapChangerTabular = value
        if self._RatioTapChangerTabular is not None:
            if self not in self._RatioTapChangerTabular._RatioTapChanger:
                self._RatioTapChangerTabular._RatioTapChanger.append(self)

    RatioTapChangerTabular = property(getRatioTapChangerTabular, setRatioTapChangerTabular)

    def getTransformerEnd(self):
        """Transformer end to which this ratio tap changer belongs.
        """
        return self._TransformerEnd

    def setTransformerEnd(self, value):
        if self._TransformerEnd is not None:
            self._TransformerEnd._RatioTapChanger = None

        self._TransformerEnd = value
        if self._TransformerEnd is not None:
            self._TransformerEnd.RatioTapChanger = None
            self._TransformerEnd._RatioTapChanger = self

    TransformerEnd = property(getTransformerEnd, setTransformerEnd)

