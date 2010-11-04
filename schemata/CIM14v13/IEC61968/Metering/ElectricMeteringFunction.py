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

from CIM14v13.IEC61968.Metering.DeviceFunction import DeviceFunction

class ElectricMeteringFunction(DeviceFunction):
    """Functionality performed by an electric meter.
    """

    def __init__(self, kWMultiplier=0, billingMultiplier=0.0, billingMultiplierApplied=False, transformerCTRatio=0.0, demandMultiplier=0.0, transformerRatiosApplied=False, transformerVTRatio=0.0, demandMultiplierApplied=False, currentRating=0.0, kWhMultiplier=0, voltageRating=0.0, MeteringFunctionConfiguration=None, **kw_args):
        """Initializes a new 'ElectricMeteringFunction' instance.

        @param kWMultiplier: Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        @param billingMultiplier: Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item. 
        @param billingMultiplierApplied: True if the billingMultiplier ratio has already been applied to the associated quantities. 
        @param transformerCTRatio: Current transformer ratio used to convert associated quantities to real measurements. 
        @param demandMultiplier: An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'. 
        @param transformerRatiosApplied: True if transformer ratios have been already applied to the associated quantities. 
        @param transformerVTRatio: Voltage transformer ratio used to convert associated quantities to real measurements. 
        @param demandMultiplierApplied: True if the demandMultiplier ratio has already been applied to the associated quantities. 
        @param currentRating: The current class of the meter. Typical current classes in North America are 10 A, 20 A, 100 A, 200 A, or 320 A. 
        @param kWhMultiplier: Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        @param voltageRating: The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120 V, 240 V, 277 V or 480 V. 
        @param MeteringFunctionConfiguration: Configuration for this electric metering function.
        """
        #: Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
        self.kWMultiplier = kWMultiplier

        #: Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item.
        self.billingMultiplier = billingMultiplier

        #: True if the billingMultiplier ratio has already been applied to the associated quantities.
        self.billingMultiplierApplied = billingMultiplierApplied

        #: Current transformer ratio used to convert associated quantities to real measurements.
        self.transformerCTRatio = transformerCTRatio

        #: An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'.
        self.demandMultiplier = demandMultiplier

        #: True if transformer ratios have been already applied to the associated quantities.
        self.transformerRatiosApplied = transformerRatiosApplied

        #: Voltage transformer ratio used to convert associated quantities to real measurements.
        self.transformerVTRatio = transformerVTRatio

        #: True if the demandMultiplier ratio has already been applied to the associated quantities.
        self.demandMultiplierApplied = demandMultiplierApplied

        #: The current class of the meter. Typical current classes in North America are 10 A, 20 A, 100 A, 200 A, or 320 A.
        self.currentRating = currentRating

        #: Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
        self.kWhMultiplier = kWhMultiplier

        #: The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120 V, 240 V, 277 V or 480 V.
        self.voltageRating = voltageRating

        self._MeteringFunctionConfiguration = None
        self.MeteringFunctionConfiguration = MeteringFunctionConfiguration

        super(ElectricMeteringFunction, self).__init__(**kw_args)

    def getMeteringFunctionConfiguration(self):
        """Configuration for this electric metering function.
        """
        return self._MeteringFunctionConfiguration

    def setMeteringFunctionConfiguration(self, value):
        if self._MeteringFunctionConfiguration is not None:
            filtered = [x for x in self.MeteringFunctionConfiguration.ElectricMeteringFunctions if x != self]
            self._MeteringFunctionConfiguration._ElectricMeteringFunctions = filtered

        self._MeteringFunctionConfiguration = value
        if self._MeteringFunctionConfiguration is not None:
            self._MeteringFunctionConfiguration._ElectricMeteringFunctions.append(self)

    MeteringFunctionConfiguration = property(getMeteringFunctionConfiguration, setMeteringFunctionConfiguration)

