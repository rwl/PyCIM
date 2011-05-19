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

class ShortCircuitTest(TransformerTest):
    """Short-circuit test results determine mesh impedance parameters. They include load losses and leakage impedances.  For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one grounded winding.Short-circuit test results determine mesh impedance parameters. They include load losses and leakage impedances.  For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one grounded winding.
    """

    def __init__(self, lossZero=0.0, leakageImpedance=0.0, loss=0.0, groundedEndStep=0, leakageImpedanceZero=0.0, energisedEndStep=0, GroundedEnds=None, EnergisedEnd=None, *args, **kw_args):
        """Initialises a new 'ShortCircuitTest' instance.

        @param lossZero: Load losses from a zero-sequence short-circuit test. 
        @param leakageImpedance: Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        @param loss: Load losses from a positive-sequence or single-phase short-circuit test. 
        @param groundedEndStep: Tap step number for the grounded end of the test pair. 
        @param leakageImpedanceZero: Leakage impedance measured from a zero-sequence short-circuit test. 
        @param energisedEndStep: Tap step number for the energised end of the test pair. 
        @param GroundedEnds: All ends short-circuited in this short-circuit test.
        @param EnergisedEnd: Transformer end that voltage is applied to in this short-circuit test. The test voltage is chosen to induce rated current in the energised end.
        """
        #: Load losses from a zero-sequence short-circuit test.
        self.lossZero = lossZero

        #: Leakage impedance measured from a positive-sequence or single-phase short-circuit test.
        self.leakageImpedance = leakageImpedance

        #: Load losses from a positive-sequence or single-phase short-circuit test.
        self.loss = loss

        #: Tap step number for the grounded end of the test pair.
        self.groundedEndStep = groundedEndStep

        #: Leakage impedance measured from a zero-sequence short-circuit test.
        self.leakageImpedanceZero = leakageImpedanceZero

        #: Tap step number for the energised end of the test pair.
        self.energisedEndStep = energisedEndStep

        self._GroundedEnds = []
        self.GroundedEnds = [] if GroundedEnds is None else GroundedEnds

        self._EnergisedEnd = None
        self.EnergisedEnd = EnergisedEnd

        super(ShortCircuitTest, self).__init__(*args, **kw_args)

    _attrs = ["lossZero", "leakageImpedance", "loss", "groundedEndStep", "leakageImpedanceZero", "energisedEndStep"]
    _attr_types = {"lossZero": float, "leakageImpedance": float, "loss": float, "groundedEndStep": int, "leakageImpedanceZero": float, "energisedEndStep": int}
    _defaults = {"lossZero": 0.0, "leakageImpedance": 0.0, "loss": 0.0, "groundedEndStep": 0, "leakageImpedanceZero": 0.0, "energisedEndStep": 0}
    _enums = {}
    _refs = ["GroundedEnds", "EnergisedEnd"]
    _many_refs = ["GroundedEnds"]

    def getGroundedEnds(self):
        """All ends short-circuited in this short-circuit test.
        """
        return self._GroundedEnds

    def setGroundedEnds(self, value):
        for p in self._GroundedEnds:
            filtered = [q for q in p.GroundedEndShortCircuitTests if q != self]
            self._GroundedEnds._GroundedEndShortCircuitTests = filtered
        for r in value:
            if self not in r._GroundedEndShortCircuitTests:
                r._GroundedEndShortCircuitTests.append(self)
        self._GroundedEnds = value

    GroundedEnds = property(getGroundedEnds, setGroundedEnds)

    def addGroundedEnds(self, *GroundedEnds):
        for obj in GroundedEnds:
            if self not in obj._GroundedEndShortCircuitTests:
                obj._GroundedEndShortCircuitTests.append(self)
            self._GroundedEnds.append(obj)

    def removeGroundedEnds(self, *GroundedEnds):
        for obj in GroundedEnds:
            if self in obj._GroundedEndShortCircuitTests:
                obj._GroundedEndShortCircuitTests.remove(self)
            self._GroundedEnds.remove(obj)

    def getEnergisedEnd(self):
        """Transformer end that voltage is applied to in this short-circuit test. The test voltage is chosen to induce rated current in the energised end.
        """
        return self._EnergisedEnd

    def setEnergisedEnd(self, value):
        if self._EnergisedEnd is not None:
            filtered = [x for x in self.EnergisedEnd.EnergisedEndShortCircuitTests if x != self]
            self._EnergisedEnd._EnergisedEndShortCircuitTests = filtered

        self._EnergisedEnd = value
        if self._EnergisedEnd is not None:
            if self not in self._EnergisedEnd._EnergisedEndShortCircuitTests:
                self._EnergisedEnd._EnergisedEndShortCircuitTests.append(self)

    EnergisedEnd = property(getEnergisedEnd, setEnergisedEnd)

