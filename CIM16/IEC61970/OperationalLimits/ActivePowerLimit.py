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

from CIM16.IEC61970.OperationalLimits.OperationalLimit import OperationalLimit

class ActivePowerLimit(OperationalLimit):
    """Limit on active power flow.Limit on active power flow.
    """

    def __init__(self, value=0.0, ActivePowerLimitSet=None, *args, **kw_args):
        """Initialises a new 'ActivePowerLimit' instance.

        @param value: Value of active power limit. 
        @param ActivePowerLimitSet:
        """
        #: Value of active power limit.
        self.value = value

        self._ActivePowerLimitSet = None
        self.ActivePowerLimitSet = ActivePowerLimitSet

        super(ActivePowerLimit, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["ActivePowerLimitSet"]
    _many_refs = []

    def getActivePowerLimitSet(self):
        
        return self._ActivePowerLimitSet

    def setActivePowerLimitSet(self, value):
        if self._ActivePowerLimitSet is not None:
            filtered = [x for x in self.ActivePowerLimitSet.ActivePowerLimits if x != self]
            self._ActivePowerLimitSet._ActivePowerLimits = filtered

        self._ActivePowerLimitSet = value
        if self._ActivePowerLimitSet is not None:
            if self not in self._ActivePowerLimitSet._ActivePowerLimits:
                self._ActivePowerLimitSet._ActivePowerLimits.append(self)

    ActivePowerLimitSet = property(getActivePowerLimitSet, setActivePowerLimitSet)

