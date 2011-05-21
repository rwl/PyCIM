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

from CIM14.CPSM.Equipment.Core.PowerSystemResource import PowerSystemResource

class RegulatingControl(PowerSystemResource):
    """Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Although targetRange and targetValue is optional, at least one must be used.
    """

    def __init__(self, targetRange=0.0, mode="reactivePower", discrete=False, targetValue=0.0, RegulationSchedule=None, Terminal=None, RegulatingCondEq=None, TapChanger=None, *args, **kw_args):
        """Initialises a new 'RegulatingControl' instance.

        @param targetRange: This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode. 
        @param mode: The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule. Values are: "reactivePower", "timeScheduled", "voltage", "activePower", "currentFlow", "fixed", "temperature", "powerFactor", "admittance"
        @param discrete: The regulation is performed in a discrete mode. 
        @param targetValue: The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute. 
        @param RegulationSchedule: Schedule for this Regulating regulating control.
        @param Terminal: The terminal associated with this regulating control.
        @param RegulatingCondEq: The equipment that participates in this regulating control scheme.
        @param TapChanger: copy from reg conduting eq
        """
        #: This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
        self.targetRange = targetRange

        #: The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule. Values are: "reactivePower", "timeScheduled", "voltage", "activePower", "currentFlow", "fixed", "temperature", "powerFactor", "admittance"
        self.mode = mode

        #: The regulation is performed in a discrete mode.
        self.discrete = discrete

        #: The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
        self.targetValue = targetValue

        self._RegulationSchedule = []
        self.RegulationSchedule = [] if RegulationSchedule is None else RegulationSchedule

        self._Terminal = None
        self.Terminal = Terminal

        self._RegulatingCondEq = []
        self.RegulatingCondEq = [] if RegulatingCondEq is None else RegulatingCondEq

        self._TapChanger = []
        self.TapChanger = [] if TapChanger is None else TapChanger

        super(RegulatingControl, self).__init__(*args, **kw_args)

    _attrs = ["targetRange", "mode", "discrete", "targetValue"]
    _attr_types = {"targetRange": float, "mode": str, "discrete": bool, "targetValue": float}
    _defaults = {"targetRange": 0.0, "mode": "reactivePower", "discrete": False, "targetValue": 0.0}
    _enums = {"mode": "RegulatingControlModeKind"}
    _refs = ["RegulationSchedule", "Terminal", "RegulatingCondEq", "TapChanger"]
    _many_refs = ["RegulationSchedule", "RegulatingCondEq", "TapChanger"]

    def getRegulationSchedule(self):
        """Schedule for this Regulating regulating control.
        """
        return self._RegulationSchedule

    def setRegulationSchedule(self, value):
        for x in self._RegulationSchedule:
            x.RegulatingControl = None
        for y in value:
            y._RegulatingControl = self
        self._RegulationSchedule = value

    RegulationSchedule = property(getRegulationSchedule, setRegulationSchedule)

    def addRegulationSchedule(self, *RegulationSchedule):
        for obj in RegulationSchedule:
            obj.RegulatingControl = self

    def removeRegulationSchedule(self, *RegulationSchedule):
        for obj in RegulationSchedule:
            obj.RegulatingControl = None

    def getTerminal(self):
        """The terminal associated with this regulating control.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.RegulatingControl if x != self]
            self._Terminal._RegulatingControl = filtered

        self._Terminal = value
        if self._Terminal is not None:
            if self not in self._Terminal._RegulatingControl:
                self._Terminal._RegulatingControl.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getRegulatingCondEq(self):
        """The equipment that participates in this regulating control scheme.
        """
        return self._RegulatingCondEq

    def setRegulatingCondEq(self, value):
        for x in self._RegulatingCondEq:
            x.RegulatingControl = None
        for y in value:
            y._RegulatingControl = self
        self._RegulatingCondEq = value

    RegulatingCondEq = property(getRegulatingCondEq, setRegulatingCondEq)

    def addRegulatingCondEq(self, *RegulatingCondEq):
        for obj in RegulatingCondEq:
            obj.RegulatingControl = self

    def removeRegulatingCondEq(self, *RegulatingCondEq):
        for obj in RegulatingCondEq:
            obj.RegulatingControl = None

    def getTapChanger(self):
        """copy from reg conduting eq
        """
        return self._TapChanger

    def setTapChanger(self, value):
        for x in self._TapChanger:
            x.RegulatingControl = None
        for y in value:
            y._RegulatingControl = self
        self._TapChanger = value

    TapChanger = property(getTapChanger, setTapChanger)

    def addTapChanger(self, *TapChanger):
        for obj in TapChanger:
            obj.RegulatingControl = self

    def removeTapChanger(self, *TapChanger):
        for obj in TapChanger:
            obj.RegulatingControl = None

