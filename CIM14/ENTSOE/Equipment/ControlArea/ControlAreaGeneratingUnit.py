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

from CIM14.ENTSOE.Equipment.Element import Element

class ControlAreaGeneratingUnit(Element):
    """A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    def __init__(self, ControlArea=None, GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'ControlAreaGeneratingUnit' instance.

        @param ControlArea: The parent control area for the generating unit specifications.
        @param GeneratingUnit: The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """
        self._ControlArea = None
        self.ControlArea = ControlArea

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(ControlAreaGeneratingUnit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ControlArea", "GeneratingUnit"]
    _many_refs = []

    def getControlArea(self):
        """The parent control area for the generating unit specifications.
        """
        return self._ControlArea

    def setControlArea(self, value):
        if self._ControlArea is not None:
            filtered = [x for x in self.ControlArea.ControlAreaGeneratingUnit if x != self]
            self._ControlArea._ControlAreaGeneratingUnit = filtered

        self._ControlArea = value
        if self._ControlArea is not None:
            if self not in self._ControlArea._ControlAreaGeneratingUnit:
                self._ControlArea._ControlAreaGeneratingUnit.append(self)

    ControlArea = property(getControlArea, setControlArea)

    def getGeneratingUnit(self):
        """The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.ControlAreaGeneratingUnit if x != self]
            self._GeneratingUnit._ControlAreaGeneratingUnit = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            if self not in self._GeneratingUnit._ControlAreaGeneratingUnit:
                self._GeneratingUnit._ControlAreaGeneratingUnit.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

