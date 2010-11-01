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

class MWLimitSchedule(Curve):
    """Maximum MW and optionally Minimum MW (Y1 and Y2, respectively)
    """

    def __init__(self, SecurityConstraintLimit=None, *args, **kw_args):
        """Initializes a new 'MWLimitSchedule' instance.

        @param SecurityConstraintLimit:
        """
        self._SecurityConstraintLimit = None
        self.SecurityConstraintLimit = SecurityConstraintLimit

        super(MWLimitSchedule, self).__init__(*args, **kw_args)

    def getSecurityConstraintLimit(self):
        
        return self._SecurityConstraintLimit

    def setSecurityConstraintLimit(self, value):
        if self._SecurityConstraintLimit is not None:
            self._SecurityConstraintLimit._MWLimitSchedules = None

        self._SecurityConstraintLimit = value
        if self._SecurityConstraintLimit is not None:
            self._SecurityConstraintLimit._MWLimitSchedules = self

    SecurityConstraintLimit = property(getSecurityConstraintLimit, setSecurityConstraintLimit)

