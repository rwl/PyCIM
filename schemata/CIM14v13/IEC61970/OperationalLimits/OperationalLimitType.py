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

from CIM14v13.Element import Element

class OperationalLimitType(Element):
    """A type of limit.  The meaning of a specific limit is described in this class.
    """

    def __init__(self, direction='absoluteValue', acceptableDuration=0.0, OperationalLimit=None, **kw_args):
        """Initializes a new 'OperationalLimitType' instance.

        @param direction: The direction of the limit. Values are: "absoluteValue", "high", "low"
        @param acceptableDuration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        @param OperationalLimit: The operational limits associated with this type of limit.
        """
        #: The direction of the limit.Values are: "absoluteValue", "high", "low"
        self.direction = direction

        #: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
        self.acceptableDuration = acceptableDuration

        self._OperationalLimit = []
        self.OperationalLimit = [] if OperationalLimit is None else OperationalLimit

        super(OperationalLimitType, self).__init__(**kw_args)

    def getOperationalLimit(self):
        """The operational limits associated with this type of limit.
        """
        return self._OperationalLimit

    def setOperationalLimit(self, value):
        for x in self._OperationalLimit:
            x._OperationalLimitType = None
        for y in value:
            y._OperationalLimitType = self
        self._OperationalLimit = value

    OperationalLimit = property(getOperationalLimit, setOperationalLimit)

    def addOperationalLimit(self, *OperationalLimit):
        for obj in OperationalLimit:
            obj._OperationalLimitType = self
            self._OperationalLimit.append(obj)

    def removeOperationalLimit(self, *OperationalLimit):
        for obj in OperationalLimit:
            obj._OperationalLimitType = None
            self._OperationalLimit.remove(obj)

