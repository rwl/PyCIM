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

from CIM14.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class BWRSteamSupply(SteamSupply):
    """Boiling water reactor used as a steam supply to a steam turbine
    """

    def __init__(self, lowerLimit=0.0, pressureSetpointGA=0.0, rfAux8=0.0, rfAux3=0.0, rfAux2=0.0, highPowerLimit=0.0, rodPattern=0.0, rodPatternConstant=0.0, integralGain=0.0, rfAux7=0.0, proportionalGain=0.0, rfAux6=0.0, pressureSetpointTC2=0.0, rfAux1=0.0, pressureSetpointTC1=0.0, inCoreThermalTC=0.0, upperLimit=0.0, rfAux4=0.0, pressureLimit=0.0, rfAux5=0.0, lowPowerLimit=0.0, *args, **kw_args):
        """Initialises a new 'BWRSteamSupply' instance.

        @param lowerLimit: Initial Lower Limit 
        @param pressureSetpointGA: Pressure Setpoint Gain Adjuster 
        @param rfAux8: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rfAux3: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param rfAux2: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param highPowerLimit: High Power Limit 
        @param rodPattern: Rod Pattern 
        @param rodPatternConstant: Constant Associated With Rod Pattern 
        @param integralGain: Integral Gain 
        @param rfAux7: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param proportionalGain: Proportional Gain 
        @param rfAux6: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressureSetpointTC2: Pressure Setpoint Time Constant 
        @param rfAux1: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressureSetpointTC1: Pressure Setpoint Time Constant 
        @param inCoreThermalTC: In-Core Thermal Time Constant 
        @param upperLimit: Initial Upper Limit 
        @param rfAux4: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param pressureLimit: Pressure Limit 
        @param rfAux5: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output. 
        @param lowPowerLimit: Low Power Limit 
        """
        #: Initial Lower Limit
        self.lowerLimit = lowerLimit

        #: Pressure Setpoint Gain Adjuster
        self.pressureSetpointGA = pressureSetpointGA

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux8 = rfAux8

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux3 = rfAux3

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux2 = rfAux2

        #: High Power Limit
        self.highPowerLimit = highPowerLimit

        #: Rod Pattern
        self.rodPattern = rodPattern

        #: Constant Associated With Rod Pattern
        self.rodPatternConstant = rodPatternConstant

        #: Integral Gain
        self.integralGain = integralGain

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux7 = rfAux7

        #: Proportional Gain
        self.proportionalGain = proportionalGain

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux6 = rfAux6

        #: Pressure Setpoint Time Constant
        self.pressureSetpointTC2 = pressureSetpointTC2

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux1 = rfAux1

        #: Pressure Setpoint Time Constant
        self.pressureSetpointTC1 = pressureSetpointTC1

        #: In-Core Thermal Time Constant
        self.inCoreThermalTC = inCoreThermalTC

        #: Initial Upper Limit
        self.upperLimit = upperLimit

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux4 = rfAux4

        #: Pressure Limit
        self.pressureLimit = pressureLimit

        #: Coefficient for modeling the effect of off-nominal frequency and voltage on recirculation and core flow, which affects the BWR power output.
        self.rfAux5 = rfAux5

        #: Low Power Limit
        self.lowPowerLimit = lowPowerLimit

        super(BWRSteamSupply, self).__init__(*args, **kw_args)

    _attrs = ["lowerLimit", "pressureSetpointGA", "rfAux8", "rfAux3", "rfAux2", "highPowerLimit", "rodPattern", "rodPatternConstant", "integralGain", "rfAux7", "proportionalGain", "rfAux6", "pressureSetpointTC2", "rfAux1", "pressureSetpointTC1", "inCoreThermalTC", "upperLimit", "rfAux4", "pressureLimit", "rfAux5", "lowPowerLimit"]
    _attr_types = {"lowerLimit": float, "pressureSetpointGA": float, "rfAux8": float, "rfAux3": float, "rfAux2": float, "highPowerLimit": float, "rodPattern": float, "rodPatternConstant": float, "integralGain": float, "rfAux7": float, "proportionalGain": float, "rfAux6": float, "pressureSetpointTC2": float, "rfAux1": float, "pressureSetpointTC1": float, "inCoreThermalTC": float, "upperLimit": float, "rfAux4": float, "pressureLimit": float, "rfAux5": float, "lowPowerLimit": float}
    _defaults = {"lowerLimit": 0.0, "pressureSetpointGA": 0.0, "rfAux8": 0.0, "rfAux3": 0.0, "rfAux2": 0.0, "highPowerLimit": 0.0, "rodPattern": 0.0, "rodPatternConstant": 0.0, "integralGain": 0.0, "rfAux7": 0.0, "proportionalGain": 0.0, "rfAux6": 0.0, "pressureSetpointTC2": 0.0, "rfAux1": 0.0, "pressureSetpointTC1": 0.0, "inCoreThermalTC": 0.0, "upperLimit": 0.0, "rfAux4": 0.0, "pressureLimit": 0.0, "rfAux5": 0.0, "lowPowerLimit": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

