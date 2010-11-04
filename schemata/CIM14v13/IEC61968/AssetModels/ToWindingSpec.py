# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ToWindingSpec(IdentifiedObject):
    """For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """

    def __init__(self, voltage=0.0, toTapStep=0, phaseShift=0.0, OpenCircuitTests=None, ShortCircuitTests=None, ToWinding=None, **kw_args):
        """Initializes a new 'ToWindingSpec' instance.

        @param voltage: (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param toTapStep: Tap step number for the 'to' winding of the test pair. 
        @param phaseShift: (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited. 
        @param OpenCircuitTests: All open-circuit tests in which this winding was measured.
        @param ShortCircuitTests: All short-circuit tests in which this winding was short-circuited.
        @param ToWinding: Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
        """
        #: (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
        self.voltage = voltage

        #: Tap step number for the 'to' winding of the test pair.
        self.toTapStep = toTapStep

        #: (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
        self.phaseShift = phaseShift

        self._OpenCircuitTests = []
        self.OpenCircuitTests = [] if OpenCircuitTests is None else OpenCircuitTests

        self._ShortCircuitTests = []
        self.ShortCircuitTests = [] if ShortCircuitTests is None else ShortCircuitTests

        self._ToWinding = None
        self.ToWinding = ToWinding

        super(ToWindingSpec, self).__init__(**kw_args)

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
            self._ToWinding._ToWindingSpecs.append(self)

    ToWinding = property(getToWinding, setToWinding)

