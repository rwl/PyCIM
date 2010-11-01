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

class BaseCaseConstraintLimit(Curve):
    """Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) assigned to a contingency analysis base case. Use CurveSchedule XAxisUnits to specify MW or MVA. To be used only if the BaseCaseConstraintLimit differs from the DefaultConstraintLimit.
    """

    def __init__(self, SecurityConstraintSum=None, *args, **kw_args):
        """Initializes a new 'BaseCaseConstraintLimit' instance.

        @param SecurityConstraintSum:
        """
        self._SecurityConstraintSum = None
        self.SecurityConstraintSum = SecurityConstraintSum

        super(BaseCaseConstraintLimit, self).__init__(*args, **kw_args)

    def getSecurityConstraintSum(self):
        
        return self._SecurityConstraintSum

    def setSecurityConstraintSum(self, value):
        if self._SecurityConstraintSum is not None:
            self._SecurityConstraintSum._BaseCaseConstraintLimit = None

        self._SecurityConstraintSum = value
        if self._SecurityConstraintSum is not None:
            self._SecurityConstraintSum._BaseCaseConstraintLimit = self

    SecurityConstraintSum = property(getSecurityConstraintSum, setSecurityConstraintSum)

