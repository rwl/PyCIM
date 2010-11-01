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

class FossilSteamSupply(SteamSupply):
    """Fossil fueled boiler (e.g., coal, oil, gas)
    """

    def __init__(self, boilerControlMode='following', fuelSupplyTC=0.0, pressureCtrlDG=0.0, superHeater2Capacity=0.0, controlTC=0.0, controlErrorBiasP=0.0, pressureCtrlPG=0.0, pressureCtrlIG=0.0, feedWaterIG=0.0, superHeater1Capacity=0.0, mechPowerSensorLag=0.0, controlIC=0.0, controlPC=0.0, pressureFeedback=0, feedWaterPG=0.0, fuelDemandLimit=0.0, controlPED=0.0, auxPowerVersusFrequency=0.0, auxPowerVersusVoltage=0.0, maxErrorRateP=0.0, fuelSupplyDelay=0.0, superHeaterPipePD=0.0, controlPEB=0.0, feedWaterTC=0.0, throttlePressureSP=0.0, minErrorRateP=0.0, *args, **kw_args):
        """Initializes a new 'FossilSteamSupply' instance.

        @param boilerControlMode: The control mode of the boiler Values are: "following", "coordinated"
        @param fuelSupplyTC: Fuel Supply Time Constant 
        @param pressureCtrlDG: Pressure Control Derivative Gain ratio 
        @param superHeater2Capacity: Secondary Superheater Capacity 
        @param controlTC: Time Constant 
        @param controlErrorBiasP: Active power Error Bias ratio 
        @param pressureCtrlPG: Pressure Control Proportional Gain ratio 
        @param pressureCtrlIG: Pressure Control Integral Gain ratio 
        @param feedWaterIG: Feedwater Integral Gain ratio 
        @param superHeater1Capacity: Drum/Primary Superheater Capacity 
        @param mechPowerSensorLag: Mechanical Power Sensor Lag 
        @param controlIC: Integral Constant 
        @param controlPC: Proportional Constant 
        @param pressureFeedback: Pressure Feedback Indicator 
        @param feedWaterPG: Feedwater Proportional Gain ratio 
        @param fuelDemandLimit: Fuel Demand Limit 
        @param controlPED: Pressure Error Deadband 
        @param auxPowerVersusFrequency: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        @param auxPowerVersusVoltage: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        @param maxErrorRateP: Active power Maximum Error Rate Limit 
        @param fuelSupplyDelay: Fuel Delay 
        @param superHeaterPipePD: Superheater Pipe Pressure Drop Constant 
        @param controlPEB: Pressure Error Bias ratio 
        @param feedWaterTC: Feedwater Time Constant rato 
        @param throttlePressureSP: Throttle Pressure Setpoint 
        @param minErrorRateP: Active power Minimum Error Rate Limit 
        """
        #: The control mode of the boiler Values are: "following", "coordinated"
        self.boilerControlMode = boilerControlMode

        #: Fuel Supply Time Constant 
        self.fuelSupplyTC = fuelSupplyTC

        #: Pressure Control Derivative Gain ratio 
        self.pressureCtrlDG = pressureCtrlDG

        #: Secondary Superheater Capacity 
        self.superHeater2Capacity = superHeater2Capacity

        #: Time Constant 
        self.controlTC = controlTC

        #: Active power Error Bias ratio 
        self.controlErrorBiasP = controlErrorBiasP

        #: Pressure Control Proportional Gain ratio 
        self.pressureCtrlPG = pressureCtrlPG

        #: Pressure Control Integral Gain ratio 
        self.pressureCtrlIG = pressureCtrlIG

        #: Feedwater Integral Gain ratio 
        self.feedWaterIG = feedWaterIG

        #: Drum/Primary Superheater Capacity 
        self.superHeater1Capacity = superHeater1Capacity

        #: Mechanical Power Sensor Lag 
        self.mechPowerSensorLag = mechPowerSensorLag

        #: Integral Constant 
        self.controlIC = controlIC

        #: Proportional Constant 
        self.controlPC = controlPC

        #: Pressure Feedback Indicator 
        self.pressureFeedback = pressureFeedback

        #: Feedwater Proportional Gain ratio 
        self.feedWaterPG = feedWaterPG

        #: Fuel Demand Limit 
        self.fuelDemandLimit = fuelDemandLimit

        #: Pressure Error Deadband 
        self.controlPED = controlPED

        #: Off nominal frequency effect on auxiliary real power. Per unit active power variation versus per unit frequency variation. 
        self.auxPowerVersusFrequency = auxPowerVersusFrequency

        #: Off nominal voltage effect on auxiliary real power. Per unit active power variation versus per unit voltage variation. 
        self.auxPowerVersusVoltage = auxPowerVersusVoltage

        #: Active power Maximum Error Rate Limit 
        self.maxErrorRateP = maxErrorRateP

        #: Fuel Delay 
        self.fuelSupplyDelay = fuelSupplyDelay

        #: Superheater Pipe Pressure Drop Constant 
        self.superHeaterPipePD = superHeaterPipePD

        #: Pressure Error Bias ratio 
        self.controlPEB = controlPEB

        #: Feedwater Time Constant rato 
        self.feedWaterTC = feedWaterTC

        #: Throttle Pressure Setpoint 
        self.throttlePressureSP = throttlePressureSP

        #: Active power Minimum Error Rate Limit 
        self.minErrorRateP = minErrorRateP

        super(FossilSteamSupply, self).__init__(*args, **kw_args)

