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

from CIM15.IEC61968.Common.Document import Document

class PowerQualityPricing(Document):
    """Pricing can be based on power quality.Pricing can be based on power quality.
    """

    def __init__(self, normalLowVoltLimit=0.0, valueUninterruptedServiceEnergy=0.0, voltLimitViolCost=0.0, normalHighVoltLimit=0.0, emergencyHighVoltLimit=0.0, emergencyLowVoltLimit=0.0, powerFactorMin=0.0, voltImbalanceViolCost=0.0, valueUninterruptedServiceP=0.0, *args, **kw_args):
        """Initialises a new 'PowerQualityPricing' instance.

        @param normalLowVoltLimit: Normal low voltage limit. 
        @param valueUninterruptedServiceEnergy: Value of uninterrupted service (Cost per energy). 
        @param voltLimitViolCost: Voltage limit violation cost (Cost per unit Voltage). 
        @param normalHighVoltLimit: Normal high voltage limit. 
        @param emergencyHighVoltLimit: Emergency high voltage limit. 
        @param emergencyLowVoltLimit: Emergency low voltage limit. 
        @param powerFactorMin: Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here. 
        @param voltImbalanceViolCost: Voltage imbalance violation cost (Cost per unit Voltage). 
        @param valueUninterruptedServiceP: Value of uninterrupted service (Cost per active power). 
        """
        #: Normal low voltage limit.
        self.normalLowVoltLimit = normalLowVoltLimit

        #: Value of uninterrupted service (Cost per energy).
        self.valueUninterruptedServiceEnergy = valueUninterruptedServiceEnergy

        #: Voltage limit violation cost (Cost per unit Voltage).
        self.voltLimitViolCost = voltLimitViolCost

        #: Normal high voltage limit.
        self.normalHighVoltLimit = normalHighVoltLimit

        #: Emergency high voltage limit.
        self.emergencyHighVoltLimit = emergencyHighVoltLimit

        #: Emergency low voltage limit.
        self.emergencyLowVoltLimit = emergencyLowVoltLimit

        #: Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here.
        self.powerFactorMin = powerFactorMin

        #: Voltage imbalance violation cost (Cost per unit Voltage).
        self.voltImbalanceViolCost = voltImbalanceViolCost

        #: Value of uninterrupted service (Cost per active power).
        self.valueUninterruptedServiceP = valueUninterruptedServiceP

        super(PowerQualityPricing, self).__init__(*args, **kw_args)

    _attrs = ["normalLowVoltLimit", "valueUninterruptedServiceEnergy", "voltLimitViolCost", "normalHighVoltLimit", "emergencyHighVoltLimit", "emergencyLowVoltLimit", "powerFactorMin", "voltImbalanceViolCost", "valueUninterruptedServiceP"]
    _attr_types = {"normalLowVoltLimit": float, "valueUninterruptedServiceEnergy": float, "voltLimitViolCost": float, "normalHighVoltLimit": float, "emergencyHighVoltLimit": float, "emergencyLowVoltLimit": float, "powerFactorMin": float, "voltImbalanceViolCost": float, "valueUninterruptedServiceP": float}
    _defaults = {"normalLowVoltLimit": 0.0, "valueUninterruptedServiceEnergy": 0.0, "voltLimitViolCost": 0.0, "normalHighVoltLimit": 0.0, "emergencyHighVoltLimit": 0.0, "emergencyLowVoltLimit": 0.0, "powerFactorMin": 0.0, "voltImbalanceViolCost": 0.0, "valueUninterruptedServiceP": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

