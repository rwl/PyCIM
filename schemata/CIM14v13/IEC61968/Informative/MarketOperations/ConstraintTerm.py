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

class ConstraintTerm(IdentifiedObject):
    """A constraint term is one element of a linear constraint.
    """

    def __init__(self, factor='', function='', SecurityConstraintSum=None, *args, **kw_args):
        """Initializes a new 'ConstraintTerm' instance.

        @param factor: 
        @param function: The function is an enumerated value that can be 'active', 'reactive', or 'VA' to indicate the type of flow. 
        @param SecurityConstraintSum:
        """
 
        self.factor = factor

        #: The function is an enumerated value that can be 'active', 'reactive', or 'VA' to indicate the type of flow. 
        self.function = function

        self._SecurityConstraintSum = None
        self.SecurityConstraintSum = SecurityConstraintSum

        super(ConstraintTerm, self).__init__(*args, **kw_args)

    def getSecurityConstraintSum(self):
        
        return self._SecurityConstraintSum

    def setSecurityConstraintSum(self, value):
        if self._SecurityConstraintSum is not None:
            filtered = [x for x in self.SecurityConstraintSum.ConstraintTerms if x != self]
            self._SecurityConstraintSum._ConstraintTerms = filtered

        self._SecurityConstraintSum = value
        if self._SecurityConstraintSum is not None:
            self._SecurityConstraintSum._ConstraintTerms.append(self)

    SecurityConstraintSum = property(getSecurityConstraintSum, setSecurityConstraintSum)

