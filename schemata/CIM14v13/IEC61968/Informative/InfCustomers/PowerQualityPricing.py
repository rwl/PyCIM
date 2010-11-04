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

from CIM14v13.IEC61968.Common.Document import Document

class PowerQualityPricing(Document):
    """Pricing can be based on power quality.
    """

    def __init__(self, emergencyLowVoltLimit=0.0, emergencyHighVoltLimit=0.0, voltLimitViolCost=0.0, valueUninterruptedServiceP=0.0, normalLowVoltLimit=0.0, voltImbalanceViolCost=0.0, normalHighVoltLimit=0.0, powerFactorMin=0.0, valueUninterruptedServiceEnergy=0.0, PricingStructure=None, ServiceDeliveryPoints=None, **kw_args):
        """Initializes a new 'PowerQualityPricing' instance.

        @param emergencyLowVoltLimit: Emergency low voltage limit. 
        @param emergencyHighVoltLimit: Emergency high voltage limit. 
        @param voltLimitViolCost: Voltage limit violation cost (Cost per unit Voltage). 
        @param valueUninterruptedServiceP: Value of uninterrupted service (Cost per active power). 
        @param normalLowVoltLimit: Normal low voltage limit. 
        @param voltImbalanceViolCost: Voltage imbalance violation cost (Cost per unit Voltage). 
        @param normalHighVoltLimit: Normal high voltage limit. 
        @param powerFactorMin: Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here. 
        @param valueUninterruptedServiceEnergy: Value of uninterrupted service (Cost per energy). 
        @param PricingStructure:
        @param ServiceDeliveryPoints:
        """
        #: Emergency low voltage limit.
        self.emergencyLowVoltLimit = emergencyLowVoltLimit

        #: Emergency high voltage limit.
        self.emergencyHighVoltLimit = emergencyHighVoltLimit

        #: Voltage limit violation cost (Cost per unit Voltage).
        self.voltLimitViolCost = voltLimitViolCost

        #: Value of uninterrupted service (Cost per active power).
        self.valueUninterruptedServiceP = valueUninterruptedServiceP

        #: Normal low voltage limit.
        self.normalLowVoltLimit = normalLowVoltLimit

        #: Voltage imbalance violation cost (Cost per unit Voltage).
        self.voltImbalanceViolCost = voltImbalanceViolCost

        #: Normal high voltage limit.
        self.normalHighVoltLimit = normalHighVoltLimit

        #: Threshold minimum power factor for this PricingStructure, specified in instances where a special charge is levied if the actual power factor for a Service falls below the value specified here.
        self.powerFactorMin = powerFactorMin

        #: Value of uninterrupted service (Cost per energy).
        self.valueUninterruptedServiceEnergy = valueUninterruptedServiceEnergy

        self._PricingStructure = None
        self.PricingStructure = PricingStructure

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        super(PowerQualityPricing, self).__init__(**kw_args)

    def getPricingStructure(self):
        
        return self._PricingStructure

    def setPricingStructure(self, value):
        if self._PricingStructure is not None:
            filtered = [x for x in self.PricingStructure.PowerQualityPricings if x != self]
            self._PricingStructure._PowerQualityPricings = filtered

        self._PricingStructure = value
        if self._PricingStructure is not None:
            self._PricingStructure._PowerQualityPricings.append(self)

    PricingStructure = property(getPricingStructure, setPricingStructure)

    def getServiceDeliveryPoints(self):
        
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for p in self._ServiceDeliveryPoints:
            filtered = [q for q in p.PowerQualityPricings if q != self]
            self._ServiceDeliveryPoints._PowerQualityPricings = filtered
        for r in value:
            if self not in r._PowerQualityPricings:
                r._PowerQualityPricings.append(self)
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            if self not in obj._PowerQualityPricings:
                obj._PowerQualityPricings.append(self)
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            if self in obj._PowerQualityPricings:
                obj._PowerQualityPricings.remove(self)
            self._ServiceDeliveryPoints.remove(obj)

