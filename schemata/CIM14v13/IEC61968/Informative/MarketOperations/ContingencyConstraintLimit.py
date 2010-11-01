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

from CIM14v13.IEC61970.Core.Curve import Curve

class ContingencyConstraintLimit(Curve):
    """Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a constraint for a specific contingency. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """

    def __init__(self, MWLimitSchedules=None, Contingency=None, SecurityConstraintSum=None, *args, **kw_args):
        """Initializes a new 'ContingencyConstraintLimit' instance.

        @param MWLimitSchedules:
        @param Contingency:
        @param SecurityConstraintSum:
        """
        self._MWLimitSchedules = None
        self.MWLimitSchedules = MWLimitSchedules

        self._Contingency = None
        self.Contingency = Contingency

        self._SecurityConstraintSum = None
        self.SecurityConstraintSum = SecurityConstraintSum

        super(ContingencyConstraintLimit, self).__init__(*args, **kw_args)

    def getMWLimitSchedules(self):
        
        return self._MWLimitSchedules

    def setMWLimitSchedules(self, value):
        if self._MWLimitSchedules is not None:
            self._MWLimitSchedules._SecurityConstraintLimit = None

        self._MWLimitSchedules = value
        if self._MWLimitSchedules is not None:
            self._MWLimitSchedules._SecurityConstraintLimit = self

    MWLimitSchedules = property(getMWLimitSchedules, setMWLimitSchedules)

    def getContingency(self):
        
        return self._Contingency

    def setContingency(self, value):
        if self._Contingency is not None:
            filtered = [x for x in self.Contingency.ContingencyConstraintLimit if x != self]
            self._Contingency._ContingencyConstraintLimit = filtered

        self._Contingency = value
        if self._Contingency is not None:
            self._Contingency._ContingencyConstraintLimit.append(self)

    Contingency = property(getContingency, setContingency)

    def getSecurityConstraintSum(self):
        
        return self._SecurityConstraintSum

    def setSecurityConstraintSum(self, value):
        if self._SecurityConstraintSum is not None:
            filtered = [x for x in self.SecurityConstraintSum.ContingencyConstraintLimits if x != self]
            self._SecurityConstraintSum._ContingencyConstraintLimits = filtered

        self._SecurityConstraintSum = value
        if self._SecurityConstraintSum is not None:
            self._SecurityConstraintSum._ContingencyConstraintLimits.append(self)

    SecurityConstraintSum = property(getSecurityConstraintSum, setSecurityConstraintSum)

