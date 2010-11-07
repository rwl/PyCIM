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

from CIM14.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest

class OpenCircuitTest(DistributionWindingTest):
    """Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """

    def __init__(self, excitingCurrentZero=0.0, noLoadLossZero=0.0, noLoadLoss=0.0, excitingCurrent=0.0, MeasuredWindingSpecs=None, **kw_args):
        """Initializes a new 'OpenCircuitTest' instance.

        @param excitingCurrentZero: Exciting current measured from a zero-sequence open-circuit (excitation) test. 
        @param noLoadLossZero: Losses measured from a zero-sequence open-circuit (excitation) test. 
        @param noLoadLoss: Losses measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        @param excitingCurrent: Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test. 
        @param MeasuredWindingSpecs: All other windings measured during this test.
        """
        #: Exciting current measured from a zero-sequence open-circuit (excitation) test.
        self.excitingCurrentZero = excitingCurrentZero

        #: Losses measured from a zero-sequence open-circuit (excitation) test.
        self.noLoadLossZero = noLoadLossZero

        #: Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.
        self.noLoadLoss = noLoadLoss

        #: Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.
        self.excitingCurrent = excitingCurrent

        self._MeasuredWindingSpecs = []
        self.MeasuredWindingSpecs = [] if MeasuredWindingSpecs is None else MeasuredWindingSpecs

        super(OpenCircuitTest, self).__init__(**kw_args)

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

