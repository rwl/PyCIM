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

from CIM14.CPSM.Equipment.LoadModel.SeasonDayTypeSchedule import SeasonDayTypeSchedule

class RegulationSchedule(SeasonDayTypeSchedule):
    """A pre-established pattern over time for a controlled variable, e.g., busbar voltage.-  By convention, ”value1” represents the target voltage or real power.  “value2” is the deviation. A value1 of 100 and value2 of 1 means regulating to 100KV plus or minus 1KV.  The range would be from 99 KV to 101 KV. Because the regulation values will be specified in either kV for voltage or MW for real power, the value1Multiplier and value2Multiplier attributes do not need to be specified.
    """

    def __init__(self, RegulatingControl=None, *args, **kw_args):
        """Initialises a new 'RegulationSchedule' instance.

        @param RegulatingControl: Regulating controls that have this Schedule.
        """
        self._RegulatingControl = None
        self.RegulatingControl = RegulatingControl

        super(RegulationSchedule, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RegulatingControl"]
    _many_refs = []

    def getRegulatingControl(self):
        """Regulating controls that have this Schedule.
        """
        return self._RegulatingControl

    def setRegulatingControl(self, value):
        if self._RegulatingControl is not None:
            filtered = [x for x in self.RegulatingControl.RegulationSchedule if x != self]
            self._RegulatingControl._RegulationSchedule = filtered

        self._RegulatingControl = value
        if self._RegulatingControl is not None:
            if self not in self._RegulatingControl._RegulationSchedule:
                self._RegulatingControl._RegulationSchedule.append(self)

    RegulatingControl = property(getRegulatingControl, setRegulatingControl)

