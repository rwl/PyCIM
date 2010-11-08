# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.IEC61970.Wires.RatioTapChanger import RatioTapChanger

class DistributionTapChanger(RatioTapChanger):
    """Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """

    def __init__(self, monitoredPhase="A", ptRatio=0.0, reverseLineDropX=0.0, ctRating=0.0, reverseLineDropR=0.0, lineDropCompensation=False, ctRatio=0.0, targetVoltage=0.0, limitVoltage=0.0, lineDropR=0.0, lineDropX=0.0, bandVoltage=0.0, *args, **kw_args):
        """Initialises a new 'DistributionTapChanger' instance.

        @param monitoredPhase: Phase voltage controlling this regulator, measured at regulator location. Values are: "A", "AC", "AN", "ABCN", "B", "C", "BN", "CN", "splitSecondary12N", "ABC", "splitSecondary2N", "N", "ABN", "BC", "BCN", "AB", "splitSecondary1N", "ACN"
        @param ptRatio: Built-in voltage transducer ratio. 
        @param reverseLineDropX: Line drop compensator reactance setting for reverse power flow. 
        @param ctRating: Built-in current transformer primary rating. 
        @param reverseLineDropR: Line drop compensator resistance setting for reverse power flow. 
        @param lineDropCompensation: If true, the line drop compensation is to be applied. 
        @param ctRatio: Built-in current transducer ratio. 
        @param targetVoltage: Target voltage on the PT secondary base. 
        @param limitVoltage: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        @param lineDropR: Line drop compensator resistance setting for normal (forward) power flow. 
        @param lineDropX: Line drop compensator reactance setting for normal (forward) power flow. 
        @param bandVoltage: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        """
        #: Phase voltage controlling this regulator, measured at regulator location. Values are: "A", "AC", "AN", "ABCN", "B", "C", "BN", "CN", "splitSecondary12N", "ABC", "splitSecondary2N", "N", "ABN", "BC", "BCN", "AB", "splitSecondary1N", "ACN"
        self.monitoredPhase = monitoredPhase

        #: Built-in voltage transducer ratio.
        self.ptRatio = ptRatio

        #: Line drop compensator reactance setting for reverse power flow.
        self.reverseLineDropX = reverseLineDropX

        #: Built-in current transformer primary rating.
        self.ctRating = ctRating

        #: Line drop compensator resistance setting for reverse power flow.
        self.reverseLineDropR = reverseLineDropR

        #: If true, the line drop compensation is to be applied.
        self.lineDropCompensation = lineDropCompensation

        #: Built-in current transducer ratio.
        self.ctRatio = ctRatio

        #: Target voltage on the PT secondary base.
        self.targetVoltage = targetVoltage

        #: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection.
        self.limitVoltage = limitVoltage

        #: Line drop compensator resistance setting for normal (forward) power flow.
        self.lineDropR = lineDropR

        #: Line drop compensator reactance setting for normal (forward) power flow.
        self.lineDropX = lineDropX

        #: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'.
        self.bandVoltage = bandVoltage

        super(DistributionTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["monitoredPhase", "ptRatio", "reverseLineDropX", "ctRating", "reverseLineDropR", "lineDropCompensation", "ctRatio", "targetVoltage", "limitVoltage", "lineDropR", "lineDropX", "bandVoltage"]
    _attr_types = {"monitoredPhase": str, "ptRatio": float, "reverseLineDropX": float, "ctRating": float, "reverseLineDropR": float, "lineDropCompensation": bool, "ctRatio": float, "targetVoltage": float, "limitVoltage": float, "lineDropR": float, "lineDropX": float, "bandVoltage": float}
    _defaults = {"monitoredPhase": "A", "ptRatio": 0.0, "reverseLineDropX": 0.0, "ctRating": 0.0, "reverseLineDropR": 0.0, "lineDropCompensation": False, "ctRatio": 0.0, "targetVoltage": 0.0, "limitVoltage": 0.0, "lineDropR": 0.0, "lineDropX": 0.0, "bandVoltage": 0.0}
    _enums = {"monitoredPhase": "PhaseCode"}
    _refs = []
    _many_refs = []

