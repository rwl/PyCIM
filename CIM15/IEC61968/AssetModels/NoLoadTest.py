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

from CIM15.IEC61968.AssetModels.TransformerTest import TransformerTest

class NoLoadTest(TransformerTest):
    """No-load test results determine core admittance parameters. They include exciting current and core loss measurements from applying voltage to one winding.  The excitation may be positive sequence or zero  sequence.  The test may be repeated at different voltages to measure saturation.No-load test results determine core admittance parameters. They include exciting current and core loss measurements from applying voltage to one winding.  The excitation may be positive sequence or zero  sequence.  The test may be repeated at different voltages to measure saturation.
    """

    def __init__(self, excitingCurrent=0.0, lossZero=0.0, excitingCurrentZero=0.0, energisedEndVoltage=0.0, loss=0.0, EnergisedEnd=None, *args, **kw_args):
        """Initialises a new 'NoLoadTest' instance.

        @param excitingCurrent: Exciting current measured from a positive-sequence or single-phase excitation test. 
        @param lossZero: Losses measured from a zero-sequence excitation test. 
        @param excitingCurrentZero: Exciting current measured from a zero-sequence open-circuit excitation test. 
        @param energisedEndVoltage: Voltage applied to the winding (end) during test. 
        @param loss: Losses measured from a positive-sequence or single-phase excitation test. 
        @param EnergisedEnd: Transformer end that current is applied to in this no-load test.
        """
        #: Exciting current measured from a positive-sequence or single-phase excitation test.
        self.excitingCurrent = excitingCurrent

        #: Losses measured from a zero-sequence excitation test.
        self.lossZero = lossZero

        #: Exciting current measured from a zero-sequence open-circuit excitation test.
        self.excitingCurrentZero = excitingCurrentZero

        #: Voltage applied to the winding (end) during test.
        self.energisedEndVoltage = energisedEndVoltage

        #: Losses measured from a positive-sequence or single-phase excitation test.
        self.loss = loss

        self._EnergisedEnd = None
        self.EnergisedEnd = EnergisedEnd

        super(NoLoadTest, self).__init__(*args, **kw_args)

    _attrs = ["excitingCurrent", "lossZero", "excitingCurrentZero", "energisedEndVoltage", "loss"]
    _attr_types = {"excitingCurrent": float, "lossZero": float, "excitingCurrentZero": float, "energisedEndVoltage": float, "loss": float}
    _defaults = {"excitingCurrent": 0.0, "lossZero": 0.0, "excitingCurrentZero": 0.0, "energisedEndVoltage": 0.0, "loss": 0.0}
    _enums = {}
    _refs = ["EnergisedEnd"]
    _many_refs = []

    def getEnergisedEnd(self):
        """Transformer end that current is applied to in this no-load test.
        """
        return self._EnergisedEnd

    def setEnergisedEnd(self, value):
        if self._EnergisedEnd is not None:
            filtered = [x for x in self.EnergisedEnd.EnergisedEndNoLoadTest if x != self]
            self._EnergisedEnd._EnergisedEndNoLoadTest = filtered

        self._EnergisedEnd = value
        if self._EnergisedEnd is not None:
            if self not in self._EnergisedEnd._EnergisedEndNoLoadTest:
                self._EnergisedEnd._EnergisedEndNoLoadTest.append(self)

    EnergisedEnd = property(getEnergisedEnd, setEnergisedEnd)

