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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class DistributionWindingTest(IdentifiedObject):
    """Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """

    def __init__(self, fromTapStep=0, FromWinding=None, **kw_args):
        """Initializes a new 'DistributionWindingTest' instance.

        @param fromTapStep: Tap step number for the 'from' winding of the test pair. 
        @param FromWinding: Winding that voltage or current is applied to during the test.
        """
        #: Tap step number for the 'from' winding of the test pair.
        self.fromTapStep = fromTapStep

        self._FromWinding = None
        self.FromWinding = FromWinding

        super(DistributionWindingTest, self).__init__(**kw_args)

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
            self._FromWinding._WindingTests.append(self)

    FromWinding = property(getFromWinding, setFromWinding)

