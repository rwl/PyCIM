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

class OpenCircuitTest(TransformerTest):
    """Open-circuit test results verify winding turn ratios and phase shifts. They include induced voltage and phase shift measurements on open-circuit windings, with voltage applied to the energised end.  For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.Open-circuit test results verify winding turn ratios and phase shifts. They include induced voltage and phase shift measurements on open-circuit windings, with voltage applied to the energised end.  For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """

    def __init__(self, energisedEndStep=0, openEndVoltage=0.0, openEndStep=0, energisedEndVoltage=0.0, phaseShift=0.0, OpenEnd=None, EnergisedEnd=None, *args, **kw_args):
        """Initialises a new 'OpenCircuitTest' instance.

        @param energisedEndStep: Tap step number for the energised end of the test pair. 
        @param openEndVoltage: Voltage measured at the open-circuited end, with the energised end set to rated voltage and all other ends open. 
        @param openEndStep: Tap step number for the open end of the test pair. 
        @param energisedEndVoltage: Voltage applied to the winding (end) during test. 
        @param phaseShift: Phase shift measured at the open end with the energised end set to rated voltage and all other ends open. 
        @param OpenEnd: Transformer end measured for induced voltage and angle in this open-circuit test.
        @param EnergisedEnd: Transformer end that current is applied to in this open-circuit test.
        """
        #: Tap step number for the energised end of the test pair.
        self.energisedEndStep = energisedEndStep

        #: Voltage measured at the open-circuited end, with the energised end set to rated voltage and all other ends open.
        self.openEndVoltage = openEndVoltage

        #: Tap step number for the open end of the test pair.
        self.openEndStep = openEndStep

        #: Voltage applied to the winding (end) during test.
        self.energisedEndVoltage = energisedEndVoltage

        #: Phase shift measured at the open end with the energised end set to rated voltage and all other ends open.
        self.phaseShift = phaseShift

        self._OpenEnd = None
        self.OpenEnd = OpenEnd

        self._EnergisedEnd = None
        self.EnergisedEnd = EnergisedEnd

        super(OpenCircuitTest, self).__init__(*args, **kw_args)

    _attrs = ["energisedEndStep", "openEndVoltage", "openEndStep", "energisedEndVoltage", "phaseShift"]
    _attr_types = {"energisedEndStep": int, "openEndVoltage": float, "openEndStep": int, "energisedEndVoltage": float, "phaseShift": float}
    _defaults = {"energisedEndStep": 0, "openEndVoltage": 0.0, "openEndStep": 0, "energisedEndVoltage": 0.0, "phaseShift": 0.0}
    _enums = {}
    _refs = ["OpenEnd", "EnergisedEnd"]
    _many_refs = []

    def getOpenEnd(self):
        """Transformer end measured for induced voltage and angle in this open-circuit test.
        """
        return self._OpenEnd

    def setOpenEnd(self, value):
        if self._OpenEnd is not None:
            filtered = [x for x in self.OpenEnd.OpenEndOpenCircuitTests if x != self]
            self._OpenEnd._OpenEndOpenCircuitTests = filtered

        self._OpenEnd = value
        if self._OpenEnd is not None:
            if self not in self._OpenEnd._OpenEndOpenCircuitTests:
                self._OpenEnd._OpenEndOpenCircuitTests.append(self)

    OpenEnd = property(getOpenEnd, setOpenEnd)

    def getEnergisedEnd(self):
        """Transformer end that current is applied to in this open-circuit test.
        """
        return self._EnergisedEnd

    def setEnergisedEnd(self, value):
        if self._EnergisedEnd is not None:
            filtered = [x for x in self.EnergisedEnd.EnergisedEndOpenCircuitTests if x != self]
            self._EnergisedEnd._EnergisedEndOpenCircuitTests = filtered

        self._EnergisedEnd = value
        if self._EnergisedEnd is not None:
            if self not in self._EnergisedEnd._EnergisedEndOpenCircuitTests:
                self._EnergisedEnd._EnergisedEndOpenCircuitTests.append(self)

    EnergisedEnd = property(getEnergisedEnd, setEnergisedEnd)

