# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class OperationalLimitSet(IdentifiedObject):
    """A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severities of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severities of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """

    def __init__(self, Terminal=None, OperationalLimitValue=None, *args, **kw_args):
        """Initialises a new 'OperationalLimitSet' instance.

        @param Terminal: The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.
        @param OperationalLimitValue: Values of equipment limits.
        """
        self._Terminal = None
        self.Terminal = Terminal

        self._OperationalLimitValue = []
        self.OperationalLimitValue = [] if OperationalLimitValue is None else OperationalLimitValue

        super(OperationalLimitSet, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Terminal", "OperationalLimitValue"]
    _many_refs = ["OperationalLimitValue"]

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
            if self not in self._Terminal._OperationalLimitSet:
                self._Terminal._OperationalLimitSet.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getOperationalLimitValue(self):
        """Values of equipment limits.
        """
        return self._OperationalLimitValue

    def setOperationalLimitValue(self, value):
        for x in self._OperationalLimitValue:
            x.OperationalLimitSet = None
        for y in value:
            y._OperationalLimitSet = self
        self._OperationalLimitValue = value

    OperationalLimitValue = property(getOperationalLimitValue, setOperationalLimitValue)

    def addOperationalLimitValue(self, *OperationalLimitValue):
        for obj in OperationalLimitValue:
            obj.OperationalLimitSet = self

    def removeOperationalLimitValue(self, *OperationalLimitValue):
        for obj in OperationalLimitValue:
            obj.OperationalLimitSet = None

