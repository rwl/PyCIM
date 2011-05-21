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

class AltGeneratingUnitMeas(Element):
    """A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """

    def __init__(self, priority=0, ControlAreaGeneratingUnit=None, AnalogValue=None, *args, **kw_args):
        """Initialises a new 'AltGeneratingUnitMeas' instance.

        @param priority: Priority of a measurement usage.   Lower numbers have first priority. 
        @param ControlAreaGeneratingUnit: The control aread generating unit to which the prioritized measurement assignment is applied.
        @param AnalogValue: The specific analog value used as a source.
        """
        #: Priority of a measurement usage.   Lower numbers have first priority.
        self.priority = priority

        self._ControlAreaGeneratingUnit = None
        self.ControlAreaGeneratingUnit = ControlAreaGeneratingUnit

        self._AnalogValue = None
        self.AnalogValue = AnalogValue

        super(AltGeneratingUnitMeas, self).__init__(*args, **kw_args)

    _attrs = ["priority"]
    _attr_types = {"priority": int}
    _defaults = {"priority": 0}
    _enums = {}
    _refs = ["ControlAreaGeneratingUnit", "AnalogValue"]
    _many_refs = []

    def getControlAreaGeneratingUnit(self):
        """The control aread generating unit to which the prioritized measurement assignment is applied.
        """
        return self._ControlAreaGeneratingUnit

    def setControlAreaGeneratingUnit(self, value):
        if self._ControlAreaGeneratingUnit is not None:
            filtered = [x for x in self.ControlAreaGeneratingUnit.AltGeneratingUnitMeas if x != self]
            self._ControlAreaGeneratingUnit._AltGeneratingUnitMeas = filtered

        self._ControlAreaGeneratingUnit = value
        if self._ControlAreaGeneratingUnit is not None:
            if self not in self._ControlAreaGeneratingUnit._AltGeneratingUnitMeas:
                self._ControlAreaGeneratingUnit._AltGeneratingUnitMeas.append(self)

    ControlAreaGeneratingUnit = property(getControlAreaGeneratingUnit, setControlAreaGeneratingUnit)

    def getAnalogValue(self):
        """The specific analog value used as a source.
        """
        return self._AnalogValue

    def setAnalogValue(self, value):
        if self._AnalogValue is not None:
            filtered = [x for x in self.AnalogValue.AltGeneratingUnit if x != self]
            self._AnalogValue._AltGeneratingUnit = filtered

        self._AnalogValue = value
        if self._AnalogValue is not None:
            if self not in self._AnalogValue._AltGeneratingUnit:
                self._AnalogValue._AltGeneratingUnit.append(self)

    AnalogValue = property(getAnalogValue, setAnalogValue)

