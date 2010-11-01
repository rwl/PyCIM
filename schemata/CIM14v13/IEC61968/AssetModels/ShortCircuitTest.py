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

from CIM14v13.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest

class ShortCircuitTest(DistributionWindingTest):
    """Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """

    def __init__(self, loadLoss=0.0, loadLossZero=0.0, leakageImpedanceZero=0.0, leakageImpedance=0.0, ShortedWindingSpecs=None, *args, **kw_args):
        """Initializes a new 'ShortCircuitTest' instance.

        @param loadLoss: Load losses from a positive-sequence or single-phase short-circuit test. 
        @param loadLossZero: Load losses from a zero-sequence short-circuit test. 
        @param leakageImpedanceZero: Leakage impedance measured from a zero-sequence short-circuit test. 
        @param leakageImpedance: Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        @param ShortedWindingSpecs: All windings short-circuited during this test.
        """
        #: Load losses from a positive-sequence or single-phase short-circuit test. 
        self.loadLoss = loadLoss

        #: Load losses from a zero-sequence short-circuit test. 
        self.loadLossZero = loadLossZero

        #: Leakage impedance measured from a zero-sequence short-circuit test. 
        self.leakageImpedanceZero = leakageImpedanceZero

        #: Leakage impedance measured from a positive-sequence or single-phase short-circuit test. 
        self.leakageImpedance = leakageImpedance

        self._ShortedWindingSpecs = []
        self.ShortedWindingSpecs = [] if ShortedWindingSpecs is None else ShortedWindingSpecs

        super(ShortCircuitTest, self).__init__(*args, **kw_args)

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

