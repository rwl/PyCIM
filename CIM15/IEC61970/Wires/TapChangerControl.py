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

from CIM15.IEC61970.Wires.RegulatingControl import RegulatingControl

class TapChangerControl(RegulatingControl):
    """TapChangerControl discribe behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.TapChangerControl discribe behaviour specific to tap changers, e.g. how the voltage at the end of a line varies with the load level and compensation of the voltage drop by tap adjustment.
    """

    def __init__(self, lineDropR=0.0, lineDropX=0.0, reverseLineDropX=0.0, reverseLineDropR=0.0, lineDropCompensation=False, limitVoltage=0.0, TapChanger=None, *args, **kw_args):
        """Initialises a new 'TapChangerControl' instance.

        @param lineDropR: Line drop compensator resistance setting for normal (forward) power flow. 
        @param lineDropX: Line drop compensator reactance setting for normal (forward) power flow. 
        @param reverseLineDropX: Line drop compensator reactance setting for reverse power flow. 
        @param reverseLineDropR: Line drop compensator resistance setting for reverse power flow. 
        @param lineDropCompensation: If true, the line drop compensation is to be applied. 
        @param limitVoltage: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        @param TapChanger: copy from reg conduting eq
        """
        #: Line drop compensator resistance setting for normal (forward) power flow.
        self.lineDropR = lineDropR

        #: Line drop compensator reactance setting for normal (forward) power flow.
        self.lineDropX = lineDropX

        #: Line drop compensator reactance setting for reverse power flow.
        self.reverseLineDropX = reverseLineDropX

        #: Line drop compensator resistance setting for reverse power flow.
        self.reverseLineDropR = reverseLineDropR

        #: If true, the line drop compensation is to be applied.
        self.lineDropCompensation = lineDropCompensation

        #: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.
        self.limitVoltage = limitVoltage

        self._TapChanger = []
        self.TapChanger = [] if TapChanger is None else TapChanger

        super(TapChangerControl, self).__init__(*args, **kw_args)

    _attrs = ["lineDropR", "lineDropX", "reverseLineDropX", "reverseLineDropR", "lineDropCompensation", "limitVoltage"]
    _attr_types = {"lineDropR": float, "lineDropX": float, "reverseLineDropX": float, "reverseLineDropR": float, "lineDropCompensation": bool, "limitVoltage": float}
    _defaults = {"lineDropR": 0.0, "lineDropX": 0.0, "reverseLineDropX": 0.0, "reverseLineDropR": 0.0, "lineDropCompensation": False, "limitVoltage": 0.0}
    _enums = {}
    _refs = ["TapChanger"]
    _many_refs = ["TapChanger"]

    def getTapChanger(self):
        """copy from reg conduting eq
        """
        return self._TapChanger

    def setTapChanger(self, value):
        for x in self._TapChanger:
            x.TapChangerControl = None
        for y in value:
            y._TapChangerControl = self
        self._TapChanger = value

    TapChanger = property(getTapChanger, setTapChanger)

    def addTapChanger(self, *TapChanger):
        for obj in TapChanger:
            obj.TapChangerControl = self

    def removeTapChanger(self, *TapChanger):
        for obj in TapChanger:
            obj.TapChangerControl = None

