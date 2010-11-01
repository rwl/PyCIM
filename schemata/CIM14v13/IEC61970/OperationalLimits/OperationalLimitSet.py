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

class OperationalLimitSet(IdentifiedObject):
    """A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severities of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """

    def __init__(self, Terminal=None, Equipment=None, OperationalLimitValue=None, *args, **kw_args):
        """Initializes a new 'OperationalLimitSet' instance.

        @param Terminal: The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.
        @param Equipment: The equpment to which the limit set applies.
        @param OperationalLimitValue: Values of equipment limits.
        """
        self._Terminal = None
        self.Terminal = Terminal

        self._Equipment = None
        self.Equipment = Equipment

        self._OperationalLimitValue = []
        self.OperationalLimitValue = [] if OperationalLimitValue is None else OperationalLimitValue

        super(OperationalLimitSet, self).__init__(*args, **kw_args)

    def getTerminal(self):
        """The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.OperationalLimitSet if x != self]
            self._Terminal._OperationalLimitSet = filtered

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal._OperationalLimitSet.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getEquipment(self):
        """The equpment to which the limit set applies.
        """
        return self._Equipment

    def setEquipment(self, value):
        if self._Equipment is not None:
            filtered = [x for x in self.Equipment.OperationalLimitSet if x != self]
            self._Equipment._OperationalLimitSet = filtered

        self._Equipment = value
        if self._Equipment is not None:
            self._Equipment._OperationalLimitSet.append(self)

    Equipment = property(getEquipment, setEquipment)

    def getOperationalLimitValue(self):
        """Values of equipment limits.
        """
        return self._OperationalLimitValue

    def setOperationalLimitValue(self, value):
        for x in self._OperationalLimitValue:
            x._OperationalLimitSet = None
        for y in value:
            y._OperationalLimitSet = self
        self._OperationalLimitValue = value

    OperationalLimitValue = property(getOperationalLimitValue, setOperationalLimitValue)

    def addOperationalLimitValue(self, *OperationalLimitValue):
        for obj in OperationalLimitValue:
            obj._OperationalLimitSet = self
            self._OperationalLimitValue.append(obj)

    def removeOperationalLimitValue(self, *OperationalLimitValue):
        for obj in OperationalLimitValue:
            obj._OperationalLimitSet = None
            self._OperationalLimitValue.remove(obj)

