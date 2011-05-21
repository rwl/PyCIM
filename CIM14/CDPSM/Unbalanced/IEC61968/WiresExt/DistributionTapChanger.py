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

from CIM14.CDPSM.Unbalanced.IEC61970.Wires.RatioTapChanger import RatioTapChanger

class DistributionTapChanger(RatioTapChanger):
    """Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """

    def __init__(self, lineDropR=0.0, monitoredPhase="ABC", lineDropCompensation=False, ptRatio=0.0, ctRatio=0.0, reverseLineDropR=0.0, limitVoltage=0.0, reverseLineDropX=0.0, bandVoltage=0.0, targetVoltage=0.0, lineDropX=0.0, *args, **kw_args):
        """Initialises a new 'DistributionTapChanger' instance.

        @param lineDropR: Line drop compensator resistance setting for normal (forward) power flow. 
        @param monitoredPhase: Phase voltage controlling this regulator, measured at regulator location. Values are: "ABC", "splitSecondary2N", "ABN", "CN", "ACN", "BC", "AN", "BN", "AB", "splitSecondary1N", "N", "C", "AC", "ABCN", "splitSecondary12N", "A", "B", "BCN"
        @param lineDropCompensation: If true, the line drop compensation is to be applied. 
        @param ptRatio: Built-in voltage transducer ratio. 
        @param ctRatio: Built-in current transducer ratio. 
        @param reverseLineDropR: Line drop compensator resistance setting for reverse power flow. 
        @param limitVoltage: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        @param reverseLineDropX: Line drop compensator reactance setting for reverse power flow. 
        @param bandVoltage: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        @param targetVoltage: Target voltage on the PT secondary base. 
        @param lineDropX: Line drop compensator reactance setting for normal (forward) power flow. 
        """
        #: Line drop compensator resistance setting for normal (forward) power flow.
        self.lineDropR = lineDropR

        #: Phase voltage controlling this regulator, measured at regulator location. Values are: "ABC", "splitSecondary2N", "ABN", "CN", "ACN", "BC", "AN", "BN", "AB", "splitSecondary1N", "N", "C", "AC", "ABCN", "splitSecondary12N", "A", "B", "BCN"
        self.monitoredPhase = monitoredPhase

        #: If true, the line drop compensation is to be applied.
        self.lineDropCompensation = lineDropCompensation

        #: Built-in voltage transducer ratio.
        self.ptRatio = ptRatio

        #: Built-in current transducer ratio.
        self.ctRatio = ctRatio

        #: Line drop compensator resistance setting for reverse power flow.
        self.reverseLineDropR = reverseLineDropR

        #: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.
        self.limitVoltage = limitVoltage

        #: Line drop compensator reactance setting for reverse power flow.
        self.reverseLineDropX = reverseLineDropX

        #: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.
        self.bandVoltage = bandVoltage

        #: Target voltage on the PT secondary base.
        self.targetVoltage = targetVoltage

        #: Line drop compensator reactance setting for normal (forward) power flow.
        self.lineDropX = lineDropX

        super(DistributionTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["lineDropR", "monitoredPhase", "lineDropCompensation", "ptRatio", "ctRatio", "reverseLineDropR", "limitVoltage", "reverseLineDropX", "bandVoltage", "targetVoltage", "lineDropX"]
    _attr_types = {"lineDropR": float, "monitoredPhase": str, "lineDropCompensation": bool, "ptRatio": float, "ctRatio": float, "reverseLineDropR": float, "limitVoltage": float, "reverseLineDropX": float, "bandVoltage": float, "targetVoltage": float, "lineDropX": float}
    _defaults = {"lineDropR": 0.0, "monitoredPhase": "ABC", "lineDropCompensation": False, "ptRatio": 0.0, "ctRatio": 0.0, "reverseLineDropR": 0.0, "limitVoltage": 0.0, "reverseLineDropX": 0.0, "bandVoltage": 0.0, "targetVoltage": 0.0, "lineDropX": 0.0}
    _enums = {"monitoredPhase": "PhaseCode"}
    _refs = []
    _many_refs = []

