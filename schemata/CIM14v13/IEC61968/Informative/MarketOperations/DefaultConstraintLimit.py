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

class DefaultConstraintLimit(Curve):
    """Possibly time-varying max MW or MVA and optionally Min MW limit or MVA limit (Y1 and Y2, respectively) applied as a default value if no specific constraint limits are specified for a contingency analysis. Use CurveSchedule XAxisUnits to specify MW or MVA.
    """

    def __init__(self, SecurityConstraintSum=None, **kw_args):
        """Initializes a new 'DefaultConstraintLimit' instance.

        @param SecurityConstraintSum:
        """
        self._SecurityConstraintSum = None
        self.SecurityConstraintSum = SecurityConstraintSum

        super(DefaultConstraintLimit, self).__init__(**kw_args)

    def getSecurityConstraintSum(self):
        
        return self._SecurityConstraintSum

    def setSecurityConstraintSum(self, value):
        if self._SecurityConstraintSum is not None:
            self._SecurityConstraintSum._DefaultConstraintLimit = None

        self._SecurityConstraintSum = value
        if self._SecurityConstraintSum is not None:
            self._SecurityConstraintSum._DefaultConstraintLimit = self

    SecurityConstraintSum = property(getSecurityConstraintSum, setSecurityConstraintSum)

