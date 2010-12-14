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

class OperationalLimit(IdentifiedObject):
    """A value associated with a specific kind of limit.
    """

    def __init__(self, type='', OperationalLimitType=None, OperationalLimitSet=None, *args, **kw_args):
        """Initialises a new 'OperationalLimit' instance.

        @param type: Used to specify high/low and limit levels. 
        @param OperationalLimitType: The limit type associated with this limit.
        @param OperationalLimitSet: The limit set to which the limit values belong.
        """
        #: Used to specify high/low and limit levels.
        self.type = type

        self._OperationalLimitType = None
        self.OperationalLimitType = OperationalLimitType

        self._OperationalLimitSet = None
        self.OperationalLimitSet = OperationalLimitSet

        super(OperationalLimit, self).__init__(*args, **kw_args)

    _attrs = ["type"]
    _attr_types = {"type": str}
    _defaults = {"type": ''}
    _enums = {}
    _refs = ["OperationalLimitType", "OperationalLimitSet"]
    _many_refs = []

    def getOperationalLimitType(self):
        """The limit type associated with this limit.
        """
        return self._OperationalLimitType

    def setOperationalLimitType(self, value):
        if self._OperationalLimitType is not None:
            filtered = [x for x in self.OperationalLimitType.OperationalLimit if x != self]
            self._OperationalLimitType._OperationalLimit = filtered

        self._OperationalLimitType = value
        if self._OperationalLimitType is not None:
            if self not in self._OperationalLimitType._OperationalLimit:
                self._OperationalLimitType._OperationalLimit.append(self)

    OperationalLimitType = property(getOperationalLimitType, setOperationalLimitType)

    def getOperationalLimitSet(self):
        """The limit set to which the limit values belong.
        """
        return self._OperationalLimitSet

    def setOperationalLimitSet(self, value):
        if self._OperationalLimitSet is not None:
            filtered = [x for x in self.OperationalLimitSet.OperationalLimitValue if x != self]
            self._OperationalLimitSet._OperationalLimitValue = filtered

        self._OperationalLimitSet = value
        if self._OperationalLimitSet is not None:
            if self not in self._OperationalLimitSet._OperationalLimitValue:
                self._OperationalLimitSet._OperationalLimitValue.append(self)

    OperationalLimitSet = property(getOperationalLimitSet, setOperationalLimitSet)

