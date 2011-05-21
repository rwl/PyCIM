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

class OperationalLimitType(IdentifiedObject):
    """A type of limit.  The meaning of a specific limit is described in this class.
    """

    def __init__(self, direction="low", acceptableDuration=0.0, OperationalLimit=None, *args, **kw_args):
        """Initialises a new 'OperationalLimitType' instance.

        @param direction: The direction of the limit. Values are: "low", "absoluteValue", "high"
        @param acceptableDuration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        @param OperationalLimit: The operational limits associated with this type of limit.
        """
        #: The direction of the limit. Values are: "low", "absoluteValue", "high"
        self.direction = direction

        #: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
        self.acceptableDuration = acceptableDuration

        self._OperationalLimit = []
        self.OperationalLimit = [] if OperationalLimit is None else OperationalLimit

        super(OperationalLimitType, self).__init__(*args, **kw_args)

    _attrs = ["direction", "acceptableDuration"]
    _attr_types = {"direction": str, "acceptableDuration": float}
    _defaults = {"direction": "low", "acceptableDuration": 0.0}
    _enums = {"direction": "OperationalLimitDirectionKind"}
    _refs = ["OperationalLimit"]
    _many_refs = ["OperationalLimit"]

    def getOperationalLimit(self):
        """The operational limits associated with this type of limit.
        """
        return self._OperationalLimit

    def setOperationalLimit(self, value):
        for x in self._OperationalLimit:
            x.OperationalLimitType = None
        for y in value:
            y._OperationalLimitType = self
        self._OperationalLimit = value

    OperationalLimit = property(getOperationalLimit, setOperationalLimit)

    def addOperationalLimit(self, *OperationalLimit):
        for obj in OperationalLimit:
            obj.OperationalLimitType = self

    def removeOperationalLimit(self, *OperationalLimit):
        for obj in OperationalLimit:
            obj.OperationalLimitType = None

