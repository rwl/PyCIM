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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.IdentifiedObject import IdentifiedObject

class DistributionWindingTest(IdentifiedObject):
    """Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """

    def __init__(self, fromTapStep=0, FromWinding=None, *args, **kw_args):
        """Initialises a new 'DistributionWindingTest' instance.

        @param fromTapStep: Tap step number for the 'from' winding of the test pair. 
        @param FromWinding: Winding that voltage or current is applied to during the test.
        """
        #: Tap step number for the 'from' winding of the test pair.
        self.fromTapStep = fromTapStep

        self._FromWinding = None
        self.FromWinding = FromWinding

        super(DistributionWindingTest, self).__init__(*args, **kw_args)

    _attrs = ["fromTapStep"]
    _attr_types = {"fromTapStep": int}
    _defaults = {"fromTapStep": 0}
    _enums = {}
    _refs = ["FromWinding"]
    _many_refs = []

    def getFromWinding(self):
        """Winding that voltage or current is applied to during the test.
        """
        return self._FromWinding

    def setFromWinding(self, value):
        if self._FromWinding is not None:
            filtered = [x for x in self.FromWinding.WindingTests if x != self]
            self._FromWinding._WindingTests = filtered

        self._FromWinding = value
        if self._FromWinding is not None:
            if self not in self._FromWinding._WindingTests:
                self._FromWinding._WindingTests.append(self)

    FromWinding = property(getFromWinding, setFromWinding)

