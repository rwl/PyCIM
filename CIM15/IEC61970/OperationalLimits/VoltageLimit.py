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

class VoltageLimit(OperationalLimit):
    """Operational limit applied to voltage.Operational limit applied to voltage.
    """

    def __init__(self, value=0.0, VoltageLimitSet=None, *args, **kw_args):
        """Initialises a new 'VoltageLimit' instance.

        @param value: Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind 
        @param VoltageLimitSet:
        """
        #: Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind
        self.value = value

        self._VoltageLimitSet = None
        self.VoltageLimitSet = VoltageLimitSet

        super(VoltageLimit, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["VoltageLimitSet"]
    _many_refs = []

    def getVoltageLimitSet(self):
        
        return self._VoltageLimitSet

    def setVoltageLimitSet(self, value):
        if self._VoltageLimitSet is not None:
            filtered = [x for x in self.VoltageLimitSet.VoltageLimits if x != self]
            self._VoltageLimitSet._VoltageLimits = filtered

        self._VoltageLimitSet = value
        if self._VoltageLimitSet is not None:
            if self not in self._VoltageLimitSet._VoltageLimits:
                self._VoltageLimitSet._VoltageLimits.append(self)

    VoltageLimitSet = property(getVoltageLimitSet, setVoltageLimitSet)

