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

from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest

class OpenCircuitTest(DistributionWindingTest):
    """Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """

    def __init__(self, noLoadLossZero=0.0, noLoadLoss=0.0, excitingCurrent=0.0, excitingCurrentZero=0.0, MeasuredWindingSpecs=None, *args, **kw_args):
        """Initialises a new 'OpenCircuitTest' instance.

        @param noLoadLossZero: Losses measured from a zero-sequence open-circuit (excitation) test. 
        @param noLoadLoss: Losses measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        @param excitingCurrent: Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        @param excitingCurrentZero: Exciting current measured from a zero-sequence open-circuit (excitation) test. 
        @param MeasuredWindingSpecs: All other windings measured during this test.
        """
        #: Losses measured from a zero-sequence open-circuit (excitation) test.
        self.noLoadLossZero = noLoadLossZero

        #: Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.
        self.noLoadLoss = noLoadLoss

        #: Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.
        self.excitingCurrent = excitingCurrent

        #: Exciting current measured from a zero-sequence open-circuit (excitation) test.
        self.excitingCurrentZero = excitingCurrentZero

        self._MeasuredWindingSpecs = []
        self.MeasuredWindingSpecs = [] if MeasuredWindingSpecs is None else MeasuredWindingSpecs

        super(OpenCircuitTest, self).__init__(*args, **kw_args)

    _attrs = ["noLoadLossZero", "noLoadLoss", "excitingCurrent", "excitingCurrentZero"]
    _attr_types = {"noLoadLossZero": float, "noLoadLoss": float, "excitingCurrent": float, "excitingCurrentZero": float}
    _defaults = {"noLoadLossZero": 0.0, "noLoadLoss": 0.0, "excitingCurrent": 0.0, "excitingCurrentZero": 0.0}
    _enums = {}
    _refs = ["MeasuredWindingSpecs"]
    _many_refs = ["MeasuredWindingSpecs"]

    def getMeasuredWindingSpecs(self):
        """All other windings measured during this test.
        """
        return self._MeasuredWindingSpecs

    def setMeasuredWindingSpecs(self, value):
        for p in self._MeasuredWindingSpecs:
            filtered = [q for q in p.OpenCircuitTests if q != self]
            self._MeasuredWindingSpecs._OpenCircuitTests = filtered
        for r in value:
            if self not in r._OpenCircuitTests:
                r._OpenCircuitTests.append(self)
        self._MeasuredWindingSpecs = value

    MeasuredWindingSpecs = property(getMeasuredWindingSpecs, setMeasuredWindingSpecs)

    def addMeasuredWindingSpecs(self, *MeasuredWindingSpecs):
        for obj in MeasuredWindingSpecs:
            if self not in obj._OpenCircuitTests:
                obj._OpenCircuitTests.append(self)
            self._MeasuredWindingSpecs.append(obj)

    def removeMeasuredWindingSpecs(self, *MeasuredWindingSpecs):
        for obj in MeasuredWindingSpecs:
            if self in obj._OpenCircuitTests:
                obj._OpenCircuitTests.remove(self)
            self._MeasuredWindingSpecs.remove(obj)

