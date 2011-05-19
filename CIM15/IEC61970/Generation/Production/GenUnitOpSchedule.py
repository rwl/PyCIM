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

from CIM15.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class GenUnitOpSchedule(RegularIntervalSchedule):
    """The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.
    """

    def __init__(self, GeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'GenUnitOpSchedule' instance.

        @param GeneratingUnit: A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(GenUnitOpSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GeneratingUnit"]
    _many_refs = []

    def getGeneratingUnit(self):
        """A generating unit may have an operating schedule, indicating the planned operation of the unit
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._GenUnitOpSchedule = None

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            self._GeneratingUnit.GenUnitOpSchedule = None
            self._GeneratingUnit._GenUnitOpSchedule = self

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

