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

from CIM14.CDPSM.GIS_Connectivity.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest

class ShortCircuitTest(DistributionWindingTest):
    """Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """

    def __init__(self, loadLossZero=0.0, leakageImpedanceZero=0.0, leakageImpedance=0.0, loadLoss=0.0, ShortedWindingSpecs=None, *args, **kw_args):
        """Initialises a new 'ShortCircuitTest' instance.

        @param loadLossZero: Load losses from a zero-sequence short-circuit test. 
        @param leakageImpedanceZero: Leakage impedance measured from a zero-sequence short-circuit test. 
        @param leakageImpedance: Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        @param loadLoss: Load losses from a positive-sequence or single-phase short-circuit test. 
        @param ShortedWindingSpecs: All windings short-circuited during this test.
        """
        #: Load losses from a zero-sequence short-circuit test.
        self.loadLossZero = loadLossZero

        #: Leakage impedance measured from a zero-sequence short-circuit test.
        self.leakageImpedanceZero = leakageImpedanceZero

        #: Leakage impedance measured from a positive-sequence or single-phase short-circuit test.
        self.leakageImpedance = leakageImpedance

        #: Load losses from a positive-sequence or single-phase short-circuit test.
        self.loadLoss = loadLoss

        self._ShortedWindingSpecs = []
        self.ShortedWindingSpecs = [] if ShortedWindingSpecs is None else ShortedWindingSpecs

        super(ShortCircuitTest, self).__init__(*args, **kw_args)

    _attrs = ["loadLossZero", "leakageImpedanceZero", "leakageImpedance", "loadLoss"]
    _attr_types = {"loadLossZero": float, "leakageImpedanceZero": float, "leakageImpedance": float, "loadLoss": float}
    _defaults = {"loadLossZero": 0.0, "leakageImpedanceZero": 0.0, "leakageImpedance": 0.0, "loadLoss": 0.0}
    _enums = {}
    _refs = ["ShortedWindingSpecs"]
    _many_refs = ["ShortedWindingSpecs"]

    def getShortedWindingSpecs(self):
        """All windings short-circuited during this test.
        """
        return self._ShortedWindingSpecs

    def setShortedWindingSpecs(self, value):
        for p in self._ShortedWindingSpecs:
            filtered = [q for q in p.ShortCircuitTests if q != self]
            self._ShortedWindingSpecs._ShortCircuitTests = filtered
        for r in value:
            if self not in r._ShortCircuitTests:
                r._ShortCircuitTests.append(self)
        self._ShortedWindingSpecs = value

    ShortedWindingSpecs = property(getShortedWindingSpecs, setShortedWindingSpecs)

    def addShortedWindingSpecs(self, *ShortedWindingSpecs):
        for obj in ShortedWindingSpecs:
            if self not in obj._ShortCircuitTests:
                obj._ShortCircuitTests.append(self)
            self._ShortedWindingSpecs.append(obj)

    def removeShortedWindingSpecs(self, *ShortedWindingSpecs):
        for obj in ShortedWindingSpecs:
            if self in obj._ShortCircuitTests:
                obj._ShortCircuitTests.remove(self)
            self._ShortedWindingSpecs.remove(obj)

