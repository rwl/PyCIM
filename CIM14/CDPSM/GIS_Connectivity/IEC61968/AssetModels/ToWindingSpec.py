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

class ToWindingSpec(IdentifiedObject):
    """For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """

    def __init__(self, toTapStep=0, voltage=0.0, phaseShift=0.0, OpenCircuitTests=None, ShortCircuitTests=None, ToWinding=None, *args, **kw_args):
        """Initialises a new 'ToWindingSpec' instance.

        @param toTapStep: Tap step number for the 'to' winding of the test pair. 
        @param voltage: (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param phaseShift: (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param OpenCircuitTests: All open-circuit tests in which this winding was measured.
        @param ShortCircuitTests: All short-circuit tests in which this winding was short-circuited.
        @param ToWinding: Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
        """
        #: Tap step number for the 'to' winding of the test pair.
        self.toTapStep = toTapStep

        #: (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
        self.voltage = voltage

        #: (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
        self.phaseShift = phaseShift

        self._OpenCircuitTests = []
        self.OpenCircuitTests = [] if OpenCircuitTests is None else OpenCircuitTests

        self._ShortCircuitTests = []
        self.ShortCircuitTests = [] if ShortCircuitTests is None else ShortCircuitTests

        self._ToWinding = None
        self.ToWinding = ToWinding

        super(ToWindingSpec, self).__init__(*args, **kw_args)

    _attrs = ["toTapStep", "voltage", "phaseShift"]
    _attr_types = {"toTapStep": int, "voltage": float, "phaseShift": float}
    _defaults = {"toTapStep": 0, "voltage": 0.0, "phaseShift": 0.0}
    _enums = {}
    _refs = ["OpenCircuitTests", "ShortCircuitTests", "ToWinding"]
    _many_refs = ["OpenCircuitTests", "ShortCircuitTests"]

    def getOpenCircuitTests(self):
        """All open-circuit tests in which this winding was measured.
        """
        return self._OpenCircuitTests

    def setOpenCircuitTests(self, value):
        for p in self._OpenCircuitTests:
            filtered = [q for q in p.MeasuredWindingSpecs if q != self]
            self._OpenCircuitTests._MeasuredWindingSpecs = filtered
        for r in value:
            if self not in r._MeasuredWindingSpecs:
                r._MeasuredWindingSpecs.append(self)
        self._OpenCircuitTests = value

    OpenCircuitTests = property(getOpenCircuitTests, setOpenCircuitTests)

    def addOpenCircuitTests(self, *OpenCircuitTests):
        for obj in OpenCircuitTests:
            if self not in obj._MeasuredWindingSpecs:
                obj._MeasuredWindingSpecs.append(self)
            self._OpenCircuitTests.append(obj)

    def removeOpenCircuitTests(self, *OpenCircuitTests):
        for obj in OpenCircuitTests:
            if self in obj._MeasuredWindingSpecs:
                obj._MeasuredWindingSpecs.remove(self)
            self._OpenCircuitTests.remove(obj)

    def getShortCircuitTests(self):
        """All short-circuit tests in which this winding was short-circuited.
        """
        return self._ShortCircuitTests

    def setShortCircuitTests(self, value):
        for p in self._ShortCircuitTests:
            filtered = [q for q in p.ShortedWindingSpecs if q != self]
            self._ShortCircuitTests._ShortedWindingSpecs = filtered
        for r in value:
            if self not in r._ShortedWindingSpecs:
                r._ShortedWindingSpecs.append(self)
        self._ShortCircuitTests = value

    ShortCircuitTests = property(getShortCircuitTests, setShortCircuitTests)

    def addShortCircuitTests(self, *ShortCircuitTests):
        for obj in ShortCircuitTests:
            if self not in obj._ShortedWindingSpecs:
                obj._ShortedWindingSpecs.append(self)
            self._ShortCircuitTests.append(obj)

    def removeShortCircuitTests(self, *ShortCircuitTests):
        for obj in ShortCircuitTests:
            if self in obj._ShortedWindingSpecs:
                obj._ShortedWindingSpecs.remove(self)
            self._ShortCircuitTests.remove(obj)

    def getToWinding(self):
        """Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
        """
        return self._ToWinding

    def setToWinding(self, value):
        if self._ToWinding is not None:
            filtered = [x for x in self.ToWinding.ToWindingSpecs if x != self]
            self._ToWinding._ToWindingSpecs = filtered

        self._ToWinding = value
        if self._ToWinding is not None:
            if self not in self._ToWinding._ToWindingSpecs:
                self._ToWinding._ToWindingSpecs.append(self)

    ToWinding = property(getToWinding, setToWinding)

