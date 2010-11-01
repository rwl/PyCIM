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

from CIM14v13.IEC61970.Wires.RatioTapChanger import RatioTapChanger

class DistributionTapChanger(RatioTapChanger):
    """Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.
    """

    def __init__(self, monitoredPhase='BC', targetVoltage=0.0, reverseLineDropR=0.0, limitVoltage=0.0, reverseLineDropX=0.0, lineDropR=0.0, lineDropCompensation=False, lineDropX=0.0, bandVoltage=0.0, ctRating=0.0, ptRatio=0.0, ctRatio=0.0, *args, **kw_args):
        """Initializes a new 'DistributionTapChanger' instance.

        @param monitoredPhase: Phase voltage controlling this regulator, measured at regulator location. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        @param targetVoltage: Target voltage on the PT secondary base. 
        @param reverseLineDropR: Line drop compensator resistance setting for reverse power flow. 
        @param limitVoltage: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        @param reverseLineDropX: Line drop compensator reactance setting for reverse power flow. 
        @param lineDropR: Line drop compensator resistance setting for normal (forward) power flow. 
        @param lineDropCompensation: If true, the line drop compensation is to be applied. 
        @param lineDropX: Line drop compensator reactance setting for normal (forward) power flow. 
        @param bandVoltage: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        @param ctRating: Built-in current transformer primary rating. 
        @param ptRatio: Built-in voltage transducer ratio. 
        @param ctRatio: Built-in current transducer ratio. 
        """
        #: Phase voltage controlling this regulator, measured at regulator location. Values are: "BC", "AB", "B", "AC", "ABC", "splitSecondary1N", "ABN", "ABCN", "CN", "AN", "splitSecondary12N", "BCN", "splitSecondary2N", "ACN", "A", "C", "N", "BN"
        self.monitoredPhase = monitoredPhase

        #: Target voltage on the PT secondary base. 
        self.targetVoltage = targetVoltage

        #: Line drop compensator resistance setting for reverse power flow. 
        self.reverseLineDropR = reverseLineDropR

        #: Maximum allowed regulated voltage on the PT secondary base, regardless of line drop compensation. Sometimes referred to as first-house protection. 
        self.limitVoltage = limitVoltage

        #: Line drop compensator reactance setting for reverse power flow. 
        self.reverseLineDropX = reverseLineDropX

        #: Line drop compensator resistance setting for normal (forward) power flow. 
        self.lineDropR = lineDropR

        #: If true, the line drop compensation is to be applied. 
        self.lineDropCompensation = lineDropCompensation

        #: Line drop compensator reactance setting for normal (forward) power flow. 
        self.lineDropX = lineDropX

        #: Voltage range (max - min) on the PT secondary base, centered on 'targetVoltage'. 
        self.bandVoltage = bandVoltage

        #: Built-in current transformer primary rating. 
        self.ctRating = ctRating

        #: Built-in voltage transducer ratio. 
        self.ptRatio = ptRatio

        #: Built-in current transducer ratio. 
        self.ctRatio = ctRatio

        super(DistributionTapChanger, self).__init__(*args, **kw_args)

