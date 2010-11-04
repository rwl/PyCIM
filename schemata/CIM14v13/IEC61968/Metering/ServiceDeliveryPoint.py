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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ServiceDeliveryPoint(IdentifiedObject):
    """Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a ServiceLocation, delivering service in accordance with a CustomerAgreement. Used at the place where a meter may be installed.
    """

    def __init__(self, phaseConfig='other', billingCycle='', loadMgmt='', ratedPower=0.0, nominalServiceVoltage=0, ratedCurrent=0.0, estimatedLoad=0.0, checkBilling=False, serviceDeliveryRemark='', servicePriority='', budgetBill='', grounded=False, consumptionRealEnergy=0.0, ctptReference=0, ServiceSupplier=None, SDPLocations=None, CustomerAgreement=None, MeterReadings=None, EnergyConsumer=None, PricingStructures=None, ServiceCategory=None, PowerQualityPricings=None, ServiceLocation=None, EndDeviceAssets=None, **kw_args):
        """Initializes a new 'ServiceDeliveryPoint' instance.

        @param phaseConfig: Phase configuration kind. Values are: "other", "twoPhaseTwoWire", "threePhaseTwoWire", "threePhaseFourWire", "twoPhaseThreeWire", "threePhaseThreeWire", "onePhaseThreeWire", "onePhaseTwoWire"
        @param billingCycle: Billing cycle. 
        @param loadMgmt: Load management code. 
        @param ratedPower: Power that this service delivery point is configured to deliver. 
        @param nominalServiceVoltage: Nominal service voltage. 
        @param ratedCurrent: Current that this service delivery point is configured to deliver. 
        @param estimatedLoad: Estimated load. 
        @param checkBilling: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved. 
        @param serviceDeliveryRemark: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority. 
        @param servicePriority: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities. 
        @param budgetBill: Budget bill code. 
        @param grounded: True if grounded. 
        @param consumptionRealEnergy: Cumulative totalizing register of consumed service at this service delivery point over its lifetime. 
        @param ctptReference: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point. 
        @param ServiceSupplier: ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
        @param SDPLocations: All locations of this service delivery point.
        @param CustomerAgreement: Customer agreement regulating this service delivery point.
        @param MeterReadings: All meter readings obtained from this service delivery point.
        @param EnergyConsumer:
        @param PricingStructures: All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
        @param ServiceCategory: Service category delivered by this service delivery point.
        @param PowerQualityPricings:
        @param ServiceLocation: Service location where the service delivered by this service delivery point is consumed.
        @param EndDeviceAssets: All end device assets at this service delivery point.
        """
        #: Phase configuration kind.Values are: "other", "twoPhaseTwoWire", "threePhaseTwoWire", "threePhaseFourWire", "twoPhaseThreeWire", "threePhaseThreeWire", "onePhaseThreeWire", "onePhaseTwoWire"
        self.phaseConfig = phaseConfig

        #: Billing cycle.
        self.billingCycle = billingCycle

        #: Load management code.
        self.loadMgmt = loadMgmt

        #: Power that this service delivery point is configured to deliver.
        self.ratedPower = ratedPower

        #: Nominal service voltage.
        self.nominalServiceVoltage = nominalServiceVoltage

        #: Current that this service delivery point is configured to deliver.
        self.ratedCurrent = ratedCurrent

        #: Estimated load.
        self.estimatedLoad = estimatedLoad

        #: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved.
        self.checkBilling = checkBilling

        #: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority.
        self.serviceDeliveryRemark = serviceDeliveryRemark

        #: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities.
        self.servicePriority = servicePriority

        #: Budget bill code.
        self.budgetBill = budgetBill

        #: True if grounded.
        self.grounded = grounded

        #: Cumulative totalizing register of consumed service at this service delivery point over its lifetime.
        self.consumptionRealEnergy = consumptionRealEnergy

        #: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point.
        self.ctptReference = ctptReference

        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._SDPLocations = []
        self.SDPLocations = [] if SDPLocations is None else SDPLocations

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._EnergyConsumer = None
        self.EnergyConsumer = EnergyConsumer

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        self._ServiceCategory = None
        self.ServiceCategory = ServiceCategory

        self._PowerQualityPricings = []
        self.PowerQualityPricings = [] if PowerQualityPricings is None else PowerQualityPricings

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        super(ServiceDeliveryPoint, self).__init__(**kw_args)

    def getServiceSupplier(self):
        """ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
        """
        return self._ServiceSupplier

    def setServiceSupplier(self, value):
        if self._ServiceSupplier is not None:
            filtered = [x for x in self.ServiceSupplier.ServiceDeliveryPoints if x != self]
            self._ServiceSupplier._ServiceDeliveryPoints = filtered

        self._ServiceSupplier = value
        if self._ServiceSupplier is not None:
            self._ServiceSupplier._ServiceDeliveryPoints.append(self)

    ServiceSupplier = property(getServiceSupplier, setServiceSupplier)

    def getSDPLocations(self):
        """All locations of this service delivery point.
        """
        return self._SDPLocations

    def setSDPLocations(self, value):
        for p in self._SDPLocations:
            filtered = [q for q in p.ServiceDeliveryPoints if q != self]
            self._SDPLocations._ServiceDeliveryPoints = filtered
        for r in value:
            if self not in r._ServiceDeliveryPoints:
                r._ServiceDeliveryPoints.append(self)
        self._SDPLocations = value

    SDPLocations = property(getSDPLocations, setSDPLocations)

    def addSDPLocations(self, *SDPLocations):
        for obj in SDPLocations:
            if self not in obj._ServiceDeliveryPoints:
                obj._ServiceDeliveryPoints.append(self)
            self._SDPLocations.append(obj)

    def removeSDPLocations(self, *SDPLocations):
        for obj in SDPLocations:
            if self in obj._ServiceDeliveryPoints:
                obj._ServiceDeliveryPoints.remove(self)
            self._SDPLocations.remove(obj)

    def getCustomerAgreement(self):
        """Customer agreement regulating this service delivery point.
        """
        return self._CustomerAgreement

    def setCustomerAgreement(self, value):
        if self._CustomerAgreement is not None:
            filtered = [x for x in self.CustomerAgreement.ServiceDeliveryPoints if x != self]
            self._CustomerAgreement._ServiceDeliveryPoints = filtered

        self._CustomerAgreement = value
        if self._CustomerAgreement is not None:
            self._CustomerAgreement._ServiceDeliveryPoints.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    def getMeterReadings(self):
        """All meter readings obtained from this service delivery point.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x._ServiceDeliveryPoint = None
        for y in value:
            y._ServiceDeliveryPoint = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj._ServiceDeliveryPoint = self
            self._MeterReadings.append(obj)

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj._ServiceDeliveryPoint = None
            self._MeterReadings.remove(obj)

    def getEnergyConsumer(self):
        
        return self._EnergyConsumer

    def setEnergyConsumer(self, value):
        if self._EnergyConsumer is not None:
            filtered = [x for x in self.EnergyConsumer.ServiceDeliveryPoints if x != self]
            self._EnergyConsumer._ServiceDeliveryPoints = filtered

        self._EnergyConsumer = value
        if self._EnergyConsumer is not None:
            self._EnergyConsumer._ServiceDeliveryPoints.append(self)

    EnergyConsumer = property(getEnergyConsumer, setEnergyConsumer)

    def getPricingStructures(self):
        """All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
        """
        return self._PricingStructures

    def setPricingStructures(self, value):
        for p in self._PricingStructures:
            filtered = [q for q in p.ServiceDeliveryPoints if q != self]
            self._PricingStructures._ServiceDeliveryPoints = filtered
        for r in value:
            if self not in r._ServiceDeliveryPoints:
                r._ServiceDeliveryPoints.append(self)
        self._PricingStructures = value

    PricingStructures = property(getPricingStructures, setPricingStructures)

    def addPricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self not in obj._ServiceDeliveryPoints:
                obj._ServiceDeliveryPoints.append(self)
            self._PricingStructures.append(obj)

    def removePricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self in obj._ServiceDeliveryPoints:
                obj._ServiceDeliveryPoints.remove(self)
            self._PricingStructures.remove(obj)

    def getServiceCategory(self):
        """Service category delivered by this service delivery point.
        """
        return self._ServiceCategory

    def setServiceCategory(self, value):
        if self._ServiceCategory is not None:
            filtered = [x for x in self.ServiceCategory.ServiceDeliveryPoints if x != self]
            self._ServiceCategory._ServiceDeliveryPoints = filtered

        self._ServiceCategory = value
        if self._ServiceCategory is not None:
            self._ServiceCategory._ServiceDeliveryPoints.append(self)

    ServiceCategory = property(getServiceCategory, setServiceCategory)

    def getPowerQualityPricings(self):
        
        return self._PowerQualityPricings

    def setPowerQualityPricings(self, value):
        for p in self._PowerQualityPricings:
            filtered = [q for q in p.ServiceDeliveryPoints if q != self]
            self._PowerQualityPricings._ServiceDeliveryPoints = filtered
        for r in value:
            if self not in r._ServiceDeliveryPoints:
                r._ServiceDeliveryPoints.append(self)
        self._PowerQualityPricings = value

    PowerQualityPricings = property(getPowerQualityPricings, setPowerQualityPricings)

    def addPowerQualityPricings(self, *PowerQualityPricings):
        for obj in PowerQualityPricings:
            if self not in obj._ServiceDeliveryPoints:
                obj._ServiceDeliveryPoints.append(self)
            self._PowerQualityPricings.append(obj)

    def removePowerQualityPricings(self, *PowerQualityPricings):
        for obj in PowerQualityPricings:
            if self in obj._ServiceDeliveryPoints:
                obj._ServiceDeliveryPoints.remove(self)
            self._PowerQualityPricings.remove(obj)

    def getServiceLocation(self):
        """Service location where the service delivered by this service delivery point is consumed.
        """
        return self._ServiceLocation

    def setServiceLocation(self, value):
        if self._ServiceLocation is not None:
            filtered = [x for x in self.ServiceLocation.ServiceDeliveryPoints if x != self]
            self._ServiceLocation._ServiceDeliveryPoints = filtered

        self._ServiceLocation = value
        if self._ServiceLocation is not None:
            self._ServiceLocation._ServiceDeliveryPoints.append(self)

    ServiceLocation = property(getServiceLocation, setServiceLocation)

    def getEndDeviceAssets(self):
        """All end device assets at this service delivery point.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for x in self._EndDeviceAssets:
            x._ServiceDeliveryPoint = None
        for y in value:
            y._ServiceDeliveryPoint = self
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj._ServiceDeliveryPoint = self
            self._EndDeviceAssets.append(obj)

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj._ServiceDeliveryPoint = None
            self._EndDeviceAssets.remove(obj)

