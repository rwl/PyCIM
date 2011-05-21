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

from CIM14.CPSM.Equipment.Core.IdentifiedObject import IdentifiedObject

class OperationalLimitType(IdentifiedObject):
    """A type of limit.  The meaning of a specific limit is described in this class.
    """

    def __init__(self, direction="high", acceptableDuration=0.0, *args, **kw_args):
        """Initialises a new 'OperationalLimitType' instance.

        @param direction: The direction of the limit. Values are: "high", "absoluteValue", "low"
        @param acceptableDuration: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed. 
        """
        #: The direction of the limit. Values are: "high", "absoluteValue", "low"
        self.direction = direction

        #: The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
        self.acceptableDuration = acceptableDuration

        super(OperationalLimitType, self).__init__(*args, **kw_args)

    _attrs = ["direction", "acceptableDuration"]
    _attr_types = {"direction": str, "acceptableDuration": float}
    _defaults = {"direction": "high", "acceptableDuration": 0.0}
    _enums = {"direction": "OperationalLimitDirectionKind"}
    _refs = []
    _many_refs = []

