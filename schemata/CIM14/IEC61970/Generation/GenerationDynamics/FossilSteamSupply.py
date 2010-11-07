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

from CIM14.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class FossilSteamSupply(SteamSupply):
    """Fossil fueled boiler (e.g., coal, oil, gas)
    """

    def __init__(self, boilerControlMode='following', superHeater2Capacity=0.0, auxPowerVersusFrequency=0.0, feedWaterIG=0.0, controlPED=0.0, throttlePressureSP=0.0, pressureCtrlIG=0.0, fuelSupplyDelay=0.0, controlPEB=0.0, controlTC=0.0, pressureFeedback=0, feedWaterPG=0.0, controlIC=0.0, controlPC=0.0, minErrorRateP=0.0, fuelSupplyTC=0.0, fuelDemandLimit=0.0, mechPowerSensorLag=0.0, pressureCtrlDG=0.0, maxErrorRateP=0.0, superHeaterPipePD=0.0, controlErrorBiasP=0.0, feedWaterTC=0.0, superHeater1Capacity=0.0, auxPowerVersusVoltage=0.0, pressureCtrlPG=0.0, **kw_args):
        """Initializes a new 'FossilSteamSupply' instance.

        @param boilerControlMode: The control mode of the boiler Values are: "following", "coordinated"
        @param superHeater2Capacity: Secondary Superheater Capacity 
        @param auxPowerVersusFrequency: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        @param feedWaterIG: Feedwater Integral Gain ratio 
        @param controlPED: Pressure Error Deadband 
        @param throttlePressureSP: Throttle Pressure Setpoint 
        @param pressureCtrlIG: Pressure Control Integral Gain ratio 
        @param fuelSupplyDelay: Fuel Delay 
        @param controlPEB: Pressure Error Bias ratio 
        @param controlTC: Time Constant 
        @param pressureFeedback: Pressure Feedback Indicator 
        @param feedWaterPG: Feedwater Proportional Gain ratio 
        @param controlIC: Integral Constant 
        @param controlPC: Proportional Constant 
        @param minErrorRateP: Active power Minimum Error Rate Limit 
        @param fuelSupplyTC: Fuel Supply Time Constant 
        @param fuelDemandLimit: Fuel Demand Limit 
        @param mechPowerSensorLag: Mechanical Power Sensor Lag 
        @param pressureCtrlDG: Pressure Control Derivative Gain ratio 
        @param maxErrorRateP: Active power Maximum Error Rate Limit 
        @param superHeaterPipePD: Superheater Pipe Pressure Drop Constant 
        @param controlErrorBiasP: Active power Error Bias ratio 
        @param feedWaterTC: Feedwater Time Constant rato 
        @param superHeater1Capacity: Drum/Primary Superheater Capacity 
        @param auxPowerVersusVoltage: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        @param pressureCtrlPG: Pressure Control Proportional Gain ratio 
        """
        #: The control mode of the boilerValues are: "following", "coordinated"
        self.boilerControlMode = boilerControlMode

        #: Secondary Superheater Capacity
        self.superHeater2Capacity = superHeater2Capacity

        #: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation.
        self.auxPowerVersusFrequency = auxPowerVersusFrequency

        #: Feedwater Integral Gain ratio
        self.feedWaterIG = feedWaterIG

        #: Pressure Error Deadband
        self.controlPED = controlPED

        #: Throttle Pressure Setpoint
        self.throttlePressureSP = throttlePressureSP

        #: Pressure Control Integral Gain ratio
        self.pressureCtrlIG = pressureCtrlIG

        #: Fuel Delay
        self.fuelSupplyDelay = fuelSupplyDelay

        #: Pressure Error Bias ratio
        self.controlPEB = controlPEB

        #: Time Constant
        self.controlTC = controlTC

        #: Pressure Feedback Indicator
        self.pressureFeedback = pressureFeedback

        #: Feedwater Proportional Gain ratio
        self.feedWaterPG = feedWaterPG

        #: Integral Constant
        self.controlIC = controlIC

        #: Proportional Constant
        self.controlPC = controlPC

        #: Active power Minimum Error Rate Limit
        self.minErrorRateP = minErrorRateP

        #: Fuel Supply Time Constant
        self.fuelSupplyTC = fuelSupplyTC

        #: Fuel Demand Limit
        self.fuelDemandLimit = fuelDemandLimit

        #: Mechanical Power Sensor Lag
        self.mechPowerSensorLag = mechPowerSensorLag

        #: Pressure Control Derivative Gain ratio
        self.pressureCtrlDG = pressureCtrlDG

        #: Active power Maximum Error Rate Limit
        self.maxErrorRateP = maxErrorRateP

        #: Superheater Pipe Pressure Drop Constant
        self.superHeaterPipePD = superHeaterPipePD

        #: Active power Error Bias ratio
        self.controlErrorBiasP = controlErrorBiasP

        #: Feedwater Time Constant rato
        self.feedWaterTC = feedWaterTC

        #: Drum/Primary Superheater Capacity
        self.superHeater1Capacity = superHeater1Capacity

        #: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation.
        self.auxPowerVersusVoltage = auxPowerVersusVoltage

        #: Pressure Control Proportional Gain ratio
        self.pressureCtrlPG = pressureCtrlPG

        super(FossilSteamSupply, self).__init__(**kw_args)

