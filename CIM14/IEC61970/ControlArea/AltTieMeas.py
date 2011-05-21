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

from CIM14.Element import Element

class AltTieMeas(Element):
    """A prioritized measurement to be used for the tie flow as part of the control area specification.
    """

    def __init__(self, priority=0, AnalogValue=None, TieFlow=None, *args, **kw_args):
        """Initialises a new 'AltTieMeas' instance.

        @param priority: Priority of a measurement usage.   Lower numbers have first priority. 
        @param AnalogValue: The specific analog value used as a source.
        @param TieFlow: The tie flow of the alternate measurements.
        """
        #: Priority of a measurement usage.   Lower numbers have first priority.
        self.priority = priority

        self._AnalogValue = None
        self.AnalogValue = AnalogValue

        self._TieFlow = None
        self.TieFlow = TieFlow

        super(AltTieMeas, self).__init__(*args, **kw_args)

    _attrs = ["priority"]
    _attr_types = {"priority": int}
    _defaults = {"priority": 0}
    _enums = {}
    _refs = ["AnalogValue", "TieFlow"]
    _many_refs = []

    def getAnalogValue(self):
        """The specific analog value used as a source.
        """
        return self._AnalogValue

    def setAnalogValue(self, value):
        if self._AnalogValue is not None:
            filtered = [x for x in self.AnalogValue.AltTieMeas if x != self]
            self._AnalogValue._AltTieMeas = filtered

        self._AnalogValue = value
        if self._AnalogValue is not None:
            if self not in self._AnalogValue._AltTieMeas:
                self._AnalogValue._AltTieMeas.append(self)

    AnalogValue = property(getAnalogValue, setAnalogValue)

    def getTieFlow(self):
        """The tie flow of the alternate measurements.
        """
        return self._TieFlow

    def setTieFlow(self, value):
        if self._TieFlow is not None:
            filtered = [x for x in self.TieFlow.AltTieMeas if x != self]
            self._TieFlow._AltTieMeas = filtered

        self._TieFlow = value
        if self._TieFlow is not None:
            if self not in self._TieFlow._AltTieMeas:
                self._TieFlow._AltTieMeas.append(self)

    TieFlow = property(getTieFlow, setTieFlow)

