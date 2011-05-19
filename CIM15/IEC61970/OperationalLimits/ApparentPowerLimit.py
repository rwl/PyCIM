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

from CIM15.IEC61970.OperationalLimits.OperationalLimit import OperationalLimit

class ApparentPowerLimit(OperationalLimit):
    """Apparent power limit.Apparent power limit.
    """

    def __init__(self, value=0.0, ApparentPowerLimitSet=None, *args, **kw_args):
        """Initialises a new 'ApparentPowerLimit' instance.

        @param value: The apparent power limit. 
        @param ApparentPowerLimitSet:
        """
        #: The apparent power limit.
        self.value = value

        self._ApparentPowerLimitSet = None
        self.ApparentPowerLimitSet = ApparentPowerLimitSet

        super(ApparentPowerLimit, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["ApparentPowerLimitSet"]
    _many_refs = []

    def getApparentPowerLimitSet(self):
        
        return self._ApparentPowerLimitSet

    def setApparentPowerLimitSet(self, value):
        if self._ApparentPowerLimitSet is not None:
            filtered = [x for x in self.ApparentPowerLimitSet.ApparentPowerLimits if x != self]
            self._ApparentPowerLimitSet._ApparentPowerLimits = filtered

        self._ApparentPowerLimitSet = value
        if self._ApparentPowerLimitSet is not None:
            if self not in self._ApparentPowerLimitSet._ApparentPowerLimits:
                self._ApparentPowerLimitSet._ApparentPowerLimits.append(self)

    ApparentPowerLimitSet = property(getApparentPowerLimitSet, setApparentPowerLimitSet)

