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

from CIM15.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class FossilSteamSupply(SteamSupply):
    """Fossil fueled boiler (e.g., coal, oil, gas)Fossil fueled boiler (e.g., coal, oil, gas)
    """

    def __init__(self, fuelDemandLimit=0.0, auxPowerVersusFrequency=0.0, mechPowerSensorLag=0.0, pressureCtrlDG=0.0, throttlePressureSP=0.0, feedWaterPG=0.0, feedWaterTC=0.0, controlPC=0.0, fuelSupplyDelay=0.0, controlPED=0.0, controlPEB=0.0, boilerControlMode="following", controlTC=0.0, minErrorRateP=0.0, superHeater1Capacity=0.0, controlErrorBiasP=0.0, pressureCtrlIG=0.0, feedWaterIG=0.0, pressureFeedback=0, auxPowerVersusVoltage=0.0, fuelSupplyTC=0.0, maxErrorRateP=0.0, superHeaterPipePD=0.0, pressureCtrlPG=0.0, superHeater2Capacity=0.0, controlIC=0.0, *args, **kw_args):
        """Initialises a new 'FossilSteamSupply' instance.

        @param fuelDemandLimit: Fuel Demand Limit 
        @param auxPowerVersusFrequency: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        @param mechPowerSensorLag: Mechanical Power Sensor Lag 
        @param pressureCtrlDG: Pressure Control Derivative Gain ratio 
        @param throttlePressureSP: Throttle Pressure Setpoint 
        @param feedWaterPG: Feedwater Proportional Gain ratio 
        @param feedWaterTC: Feedwater Time Constant rato 
        @param controlPC: Proportional Constant 
        @param fuelSupplyDelay: Fuel Delay 
        @param controlPED: Pressure Error Deadband 
        @param controlPEB: Pressure Error Bias ratio 
        @param boilerControlMode: The control mode of the boiler Values are: "following", "coordinated"
        @param controlTC: Time Constant 
        @param minErrorRateP: Active power Minimum Error Rate Limit 
        @param superHeater1Capacity: Drum/Primary Superheater Capacity 
        @param controlErrorBiasP: Active power Error Bias ratio 
        @param pressureCtrlIG: Pressure Control Integral Gain ratio 
        @param feedWaterIG: Feedwater Integral Gain ratio 
        @param pressureFeedback: Pressure Feedback Indicator 
        @param auxPowerVersusVoltage: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        @param fuelSupplyTC: Fuel Supply Time Constant 
        @param maxErrorRateP: Active power Maximum Error Rate Limit 
        @param superHeaterPipePD: Superheater Pipe Pressure Drop Constant 
        @param pressureCtrlPG: Pressure Control Proportional Gain ratio 
        @param superHeater2Capacity: Secondary Superheater Capacity 
        @param controlIC: Integral Constant 
        """
        #: Fuel Demand Limit
        self.fuelDemandLimit = fuelDemandLimit

        #: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
        self.auxPowerVersusFrequency = auxPowerVersusFrequency

        #: Mechanical Power Sensor Lag
        self.mechPowerSensorLag = mechPowerSensorLag

        #: Pressure Control Derivative Gain ratio
        self.pressureCtrlDG = pressureCtrlDG

        #: Throttle Pressure Setpoint
        self.throttlePressureSP = throttlePressureSP

        #: Feedwater Proportional Gain ratio
        self.feedWaterPG = feedWaterPG

        #: Feedwater Time Constant rato
        self.feedWaterTC = feedWaterTC

        #: Proportional Constant
        self.controlPC = controlPC

        #: Fuel Delay
        self.fuelSupplyDelay = fuelSupplyDelay

        #: Pressure Error Deadband
        self.controlPED = controlPED

        #: Pressure Error Bias ratio
        self.controlPEB = controlPEB

        #: The control mode of the boiler Values are: "following", "coordinated"
        self.boilerControlMode = boilerControlMode

        #: Time Constant
        self.controlTC = controlTC

        #: Active power Minimum Error Rate Limit
        self.minErrorRateP = minErrorRateP

        #: Drum/Primary Superheater Capacity
        self.superHeater1Capacity = superHeater1Capacity

        #: Active power Error Bias ratio
        self.controlErrorBiasP = controlErrorBiasP

        #: Pressure Control Integral Gain ratio
        self.pressureCtrlIG = pressureCtrlIG

        #: Feedwater Integral Gain ratio
        self.feedWaterIG = feedWaterIG

        #: Pressure Feedback Indicator
        self.pressureFeedback = pressureFeedback

        #: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
        self.auxPowerVersusVoltage = auxPowerVersusVoltage

        #: Fuel Supply Time Constant
        self.fuelSupplyTC = fuelSupplyTC

        #: Active power Maximum Error Rate Limit
        self.maxErrorRateP = maxErrorRateP

        #: Superheater Pipe Pressure Drop Constant
        self.superHeaterPipePD = superHeaterPipePD

        #: Pressure Control Proportional Gain ratio
        self.pressureCtrlPG = pressureCtrlPG

        #: Secondary Superheater Capacity
        self.superHeater2Capacity = superHeater2Capacity

        #: Integral Constant
        self.controlIC = controlIC

        super(FossilSteamSupply, self).__init__(*args, **kw_args)

    _attrs = ["fuelDemandLimit", "auxPowerVersusFrequency", "mechPowerSensorLag", "pressureCtrlDG", "throttlePressureSP", "feedWaterPG", "feedWaterTC", "controlPC", "fuelSupplyDelay", "controlPED", "controlPEB", "boilerControlMode", "controlTC", "minErrorRateP", "superHeater1Capacity", "controlErrorBiasP", "pressureCtrlIG", "feedWaterIG", "pressureFeedback", "auxPowerVersusVoltage", "fuelSupplyTC", "maxErrorRateP", "superHeaterPipePD", "pressureCtrlPG", "superHeater2Capacity", "controlIC"]
    _attr_types = {"fuelDemandLimit": float, "auxPowerVersusFrequency": float, "mechPowerSensorLag": float, "pressureCtrlDG": float, "throttlePressureSP": float, "feedWaterPG": float, "feedWaterTC": float, "controlPC": float, "fuelSupplyDelay": float, "controlPED": float, "controlPEB": float, "boilerControlMode": str, "controlTC": float, "minErrorRateP": float, "superHeater1Capacity": float, "controlErrorBiasP": float, "pressureCtrlIG": float, "feedWaterIG": float, "pressureFeedback": int, "auxPowerVersusVoltage": float, "fuelSupplyTC": float, "maxErrorRateP": float, "superHeaterPipePD": float, "pressureCtrlPG": float, "superHeater2Capacity": float, "controlIC": float}
    _defaults = {"fuelDemandLimit": 0.0, "auxPowerVersusFrequency": 0.0, "mechPowerSensorLag": 0.0, "pressureCtrlDG": 0.0, "throttlePressureSP": 0.0, "feedWaterPG": 0.0, "feedWaterTC": 0.0, "controlPC": 0.0, "fuelSupplyDelay": 0.0, "controlPED": 0.0, "controlPEB": 0.0, "boilerControlMode": "following", "controlTC": 0.0, "minErrorRateP": 0.0, "superHeater1Capacity": 0.0, "controlErrorBiasP": 0.0, "pressureCtrlIG": 0.0, "feedWaterIG": 0.0, "pressureFeedback": 0, "auxPowerVersusVoltage": 0.0, "fuelSupplyTC": 0.0, "maxErrorRateP": 0.0, "superHeaterPipePD": 0.0, "pressureCtrlPG": 0.0, "superHeater2Capacity": 0.0, "controlIC": 0.0}
    _enums = {"boilerControlMode": "BoilerControlMode"}
    _refs = []
    _many_refs = []

