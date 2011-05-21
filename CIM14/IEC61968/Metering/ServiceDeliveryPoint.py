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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ServiceDeliveryPoint(IdentifiedObject):
    """Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a ServiceLocation, delivering service in accordance with a CustomerAgreement. Used at the place where a meter may be installed.
    """

    def __init__(self, phaseCode="A", ratedPower=0.0, servicePriority='', checkBilling=False, grounded=False, serviceDeliveryRemark='', ratedCurrent=0.0, estimatedLoad=0.0, nominalServiceVoltage=0, ctptReference=0, PricingStructures=None, Transformer=None, SDPLocations=None, EndDeviceAssets=None, EnergyConsumer=None, ServiceLocation=None, CustomerAgreement=None, MeterReadings=None, ServiceSupplier=None, ServiceCategory=None, *args, **kw_args):
        """Initialises a new 'ServiceDeliveryPoint' instance.

        @param phaseCode: Phase code. Number of wires and number of phases can be deduced from enumeration literal values. For example, ABCN is three-phase, four-wire. s12n (splitSecondary12N) is single-phase, three-wire. s1n and s2n are single-phase, two-wire. Values are: "A", "AC", "AN", "ABCN", "B", "C", "BN", "CN", "splitSecondary12N", "ABC", "splitSecondary2N", "N", "ABN", "BC", "BCN", "AB", "splitSecondary1N", "ACN"
        @param ratedPower: Power that this service delivery point is configured to deliver. 
        @param servicePriority: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities. 
        @param checkBilling: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved. 
        @param grounded: True if grounded. 
        @param serviceDeliveryRemark: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority. 
        @param ratedCurrent: Current that this service delivery point is configured to deliver. 
        @param estimatedLoad: Estimated load. 
        @param nominalServiceVoltage: Nominal service voltage. 
        @param ctptReference: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point. 
        @param PricingStructures: All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
        @param Transformer: Transformer supplying this service delivery point.
        @param SDPLocations: All locations of this service delivery point.
        @param EndDeviceAssets: All end device assets at this service delivery point.
        @param EnergyConsumer:
        @param ServiceLocation: Service location where the service delivered by this service delivery point is consumed.
        @param CustomerAgreement: Customer agreement regulating this service delivery point.
        @param MeterReadings: All meter readings obtained from this service delivery point.
        @param ServiceSupplier: ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
        @param ServiceCategory: Service category delivered by this service delivery point.
        """
        #: Phase code. Number of wires and number of phases can be deduced from enumeration literal values. For example, ABCN is three-phase, four-wire. s12n (splitSecondary12N) is single-phase, three-wire. s1n and s2n are single-phase, two-wire. Values are: "A", "AC", "AN", "ABCN", "B", "C", "BN", "CN", "splitSecondary12N", "ABC", "splitSecondary2N", "N", "ABN", "BC", "BCN", "AB", "splitSecondary1N", "ACN"
        self.phaseCode = phaseCode

        #: Power that this service delivery point is configured to deliver.
        self.ratedPower = ratedPower

        #: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities.
        self.servicePriority = servicePriority

        #: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved.
        self.checkBilling = checkBilling

        #: True if grounded.
        self.grounded = grounded

        #: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority.
        self.serviceDeliveryRemark = serviceDeliveryRemark

        #: Current that this service delivery point is configured to deliver.
        self.ratedCurrent = ratedCurrent

        #: Estimated load.
        self.estimatedLoad = estimatedLoad

        #: Nominal service voltage.
        self.nominalServiceVoltage = nominalServiceVoltage

        #: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point.
        self.ctptReference = ctptReference

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        self._Transformer = None
        self.Transformer = Transformer

        self._SDPLocations = []
        self.SDPLocations = [] if SDPLocations is None else SDPLocations

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        self._EnergyConsumer = None
        self.EnergyConsumer = EnergyConsumer

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._ServiceCategory = None
        self.ServiceCategory = ServiceCategory

        super(ServiceDeliveryPoint, self).__init__(*args, **kw_args)

    _attrs = ["phaseCode", "ratedPower", "servicePriority", "checkBilling", "grounded", "serviceDeliveryRemark", "ratedCurrent", "estimatedLoad", "nominalServiceVoltage", "ctptReference"]
    _attr_types = {"phaseCode": str, "ratedPower": float, "servicePriority": str, "checkBilling": bool, "grounded": bool, "serviceDeliveryRemark": str, "ratedCurrent": float, "estimatedLoad": float, "nominalServiceVoltage": int, "ctptReference": int}
    _defaults = {"phaseCode": "A", "ratedPower": 0.0, "servicePriority": '', "checkBilling": False, "grounded": False, "serviceDeliveryRemark": '', "ratedCurrent": 0.0, "estimatedLoad": 0.0, "nominalServiceVoltage": 0, "ctptReference": 0}
    _enums = {"phaseCode": "PhaseCode"}
    _refs = ["PricingStructures", "Transformer", "SDPLocations", "EndDeviceAssets", "EnergyConsumer", "ServiceLocation", "CustomerAgreement", "MeterReadings", "ServiceSupplier", "ServiceCategory"]
    _many_refs = ["PricingStructures", "SDPLocations", "EndDeviceAssets", "MeterReadings"]

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

    def getTransformer(self):
        """Transformer supplying this service delivery point.
        """
        return self._Transformer

    def setTransformer(self, value):
        if self._Transformer is not None:
            filtered = [x for x in self.Transformer.ServiceDeliveryPoints if x != self]
            self._Transformer._ServiceDeliveryPoints = filtered

        self._Transformer = value
        if self._Transformer is not None:
            if self not in self._Transformer._ServiceDeliveryPoints:
                self._Transformer._ServiceDeliveryPoints.append(self)

    Transformer = property(getTransformer, setTransformer)

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

    def getEndDeviceAssets(self):
        """All end device assets at this service delivery point.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for x in self._EndDeviceAssets:
            x.ServiceDeliveryPoint = None
        for y in value:
            y._ServiceDeliveryPoint = self
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj.ServiceDeliveryPoint = self

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj.ServiceDeliveryPoint = None

    def getEnergyConsumer(self):
        
        return self._EnergyConsumer

    def setEnergyConsumer(self, value):
        if self._EnergyConsumer is not None:
            filtered = [x for x in self.EnergyConsumer.ServiceDeliveryPoints if x != self]
            self._EnergyConsumer._ServiceDeliveryPoints = filtered

        self._EnergyConsumer = value
        if self._EnergyConsumer is not None:
            if self not in self._EnergyConsumer._ServiceDeliveryPoints:
                self._EnergyConsumer._ServiceDeliveryPoints.append(self)

    EnergyConsumer = property(getEnergyConsumer, setEnergyConsumer)

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
            if self not in self._ServiceLocation._ServiceDeliveryPoints:
                self._ServiceLocation._ServiceDeliveryPoints.append(self)

    ServiceLocation = property(getServiceLocation, setServiceLocation)

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
            if self not in self._CustomerAgreement._ServiceDeliveryPoints:
                self._CustomerAgreement._ServiceDeliveryPoints.append(self)

    CustomerAgreement = property(getCustomerAgreement, setCustomerAgreement)

    def getMeterReadings(self):
        """All meter readings obtained from this service delivery point.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x.ServiceDeliveryPoint = None
        for y in value:
            y._ServiceDeliveryPoint = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.ServiceDeliveryPoint = self

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.ServiceDeliveryPoint = None

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
            if self not in self._ServiceSupplier._ServiceDeliveryPoints:
                self._ServiceSupplier._ServiceDeliveryPoints.append(self)

    ServiceSupplier = property(getServiceSupplier, setServiceSupplier)

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
            if self not in self._ServiceCategory._ServiceDeliveryPoints:
                self._ServiceCategory._ServiceDeliveryPoints.append(self)

    ServiceCategory = property(getServiceCategory, setServiceCategory)

