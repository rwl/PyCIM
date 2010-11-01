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

from CIM14v13.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EnergySource(ConductingEquipment):
    """A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    def __init__(self, rn=0.0, r=0.0, r0=0.0, voltageMagnitude=0.0, x=0.0, voltageAngle=0.0, xn=0.0, x0=0.0, activePower=0.0, nominalVoltage=0.0, *args, **kw_args):
        """Initializes a new 'EnergySource' instance.

        @param rn: Negative sequence Thevenin resistance. 
        @param r: Positive sequence Thevenin resistance. 
        @param r0: Zero sequence Thevenin resistance. 
        @param voltageMagnitude: Phase-to-phase open circuit voltage magnitude. 
        @param x: Positive sequence Thevenin reactance. 
        @param voltageAngle: Phase angle of a-phase open circuit. 
        @param xn: Negative sequence Thevenin reactance. 
        @param x0: Zero sequence Thevenin reactance. 
        @param activePower: High voltage source load 
        @param nominalVoltage: Phase-to-phase nominal voltage. 
        """
        #: Negative sequence Thevenin resistance. 
        self.rn = rn

        #: Positive sequence Thevenin resistance. 
        self.r = r

        #: Zero sequence Thevenin resistance. 
        self.r0 = r0

        #: Phase-to-phase open circuit voltage magnitude. 
        self.voltageMagnitude = voltageMagnitude

        #: Positive sequence Thevenin reactance. 
        self.x = x

        #: Phase angle of a-phase open circuit. 
        self.voltageAngle = voltageAngle

        #: Negative sequence Thevenin reactance. 
        self.xn = xn

        #: Zero sequence Thevenin reactance. 
        self.x0 = x0

        #: High voltage source load 
        self.activePower = activePower

        #: Phase-to-phase nominal voltage. 
        self.nominalVoltage = nominalVoltage

        super(EnergySource, self).__init__(*args, **kw_args)

