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

