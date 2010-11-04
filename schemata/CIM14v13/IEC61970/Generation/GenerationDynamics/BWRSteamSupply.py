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

from CIM14v13.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class BWRSteamSupply(SteamSupply):
    """Boiling water reactor used as a steam supply to a steam turbine
    """

    def __init__(self, proportionalGain=0.0, rfAux3=0.0, rodPatternConstant=0.0, rfAux4=0.0, pressureSetpointGA=0.0, inCoreThermalTC=0.0, rfAux2=0.0, pressureLimit=0.0, rfAux1=0.0, rfAux7=0.0, highPowerLimit=0.0, lowPowerLimit=0.0, lowerLimit=0.0, upperLimit=0.0, pressureSetpointTC1=0.0, rodPattern=0.0, rfAux8=0.0, rfAux5=0.0, integralGain=0.0, pressureSetpointTC2=0.0, rfAux6=0.0, *args, **kw_args):
        """Initializes a new 'BWRSteamSupply' instance.

        @param proportionalGain: Proportional Gain 
        @param rfAux3: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rodPatternConstant: Constant Associated With Rod Pattern 
        @param rfAux4: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressureSetpointGA: Pressure Setpoint Gain Adjuster 
        @param inCoreThermalTC: In-Core Thermal Time Constant 
        @param rfAux2: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressureLimit: Pressure Limit 
        @param rfAux1: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rfAux7: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param highPowerLimit: High Power Limit 
        @param lowPowerLimit: Low Power Limit 
        @param lowerLimit: Initial Lower Limit 
        @param upperLimit: Initial Upper Limit 
        @param pressureSetpointTC1: Pressure Setpoint Time Constant 
        @param rodPattern: Rod Pattern 
        @param rfAux8: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rfAux5: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param integralGain: Integral Gain 
        @param pressureSetpointTC2: Pressure Setpoint Time Constant 
        @param rfAux6: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        """
        #: Proportional Gain
        self.proportionalGain = proportionalGain

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux3 = rfAux3

        #: Constant Associated With Rod Pattern
        self.rodPatternConstant = rodPatternConstant

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux4 = rfAux4

        #: Pressure Setpoint Gain Adjuster
        self.pressureSetpointGA = pressureSetpointGA

        #: In-Core Thermal Time Constant
        self.inCoreThermalTC = inCoreThermalTC

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux2 = rfAux2

        #: Pressure Limit
        self.pressureLimit = pressureLimit

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux1 = rfAux1

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux7 = rfAux7

        #: High Power Limit
        self.highPowerLimit = highPowerLimit

        #: Low Power Limit
        self.lowPowerLimit = lowPowerLimit

        #: Initial Lower Limit
        self.lowerLimit = lowerLimit

        #: Initial Upper Limit
        self.upperLimit = upperLimit

        #: Pressure Setpoint Time Constant
        self.pressureSetpointTC1 = pressureSetpointTC1

        #: Rod Pattern
        self.rodPattern = rodPattern

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux8 = rfAux8

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux5 = rfAux5

        #: Integral Gain
        self.integralGain = integralGain

        #: Pressure Setpoint Time Constant
        self.pressureSetpointTC2 = pressureSetpointTC2

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux6 = rfAux6

        super(BWRSteamSupply, self).__init__(*args, **kw_args)

