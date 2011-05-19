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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ServiceDeliveryPoint(IdentifiedObject):
    """Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a service location, delivering service in accordance with a customer agreement. Used at the place where a meter may be installed.Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a service location, delivering service in accordance with a customer agreement. Used at the place where a meter may be installed.
    """

    def __init__(self, checkBilling=False, estimatedLoad=0.0, ratedPower=0.0, servicePriority='', grounded=False, serviceDeliveryRemark='', phaseCode="s12N", ctptReference=0, ratedCurrent=0.0, ratedVoltage=0.0, SDPLocations=None, ServiceLocation=None, EndDevices=None, MeterReadings=None, ServiceCategory=None, PricingStructures=None, EnergyConsumer=None, ServiceSupplier=None, CustomerAgreement=None, TransformerTanks=None, *args, **kw_args):
        """Initialises a new 'ServiceDeliveryPoint' instance.

        @param checkBilling: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved. 
        @param estimatedLoad: Estimated load. 
        @param ratedPower: Power that this service delivery point is configured to deliver. 
        @param servicePriority: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities. 
        @param grounded: True if grounded. 
        @param serviceDeliveryRemark: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority. 
        @param phaseCode: Phase code. Number of wires and number of phases can be deduced from enumeration literal values. For example, ABCN is three-phase, four-wire. s12n (splitSecondary12N) is single-phase, three-wire. s1n and s2n are single-phase, two-wire. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        @param ctptReference: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point. 
        @param ratedCurrent: Current that this service delivery point is configured to deliver. 
        @param ratedVoltage: Nominal service voltage. 
        @param SDPLocations: All locations of this service delivery point.
        @param ServiceLocation: Service location where the service delivered by this service delivery point is consumed.
        @param EndDevices: All end devices at this service delivery point.
        @param MeterReadings: All meter readings obtained from this service delivery point.
        @param ServiceCategory: Service category delivered by this service delivery point.
        @param PricingStructures: All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
        @param EnergyConsumer:
        @param ServiceSupplier: ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
        @param CustomerAgreement: Customer agreement regulating this service delivery point.
        @param TransformerTanks: Transformer supplying this service delivery point.
        """
        #: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved.
        self.checkBilling = checkBilling

        #: Estimated load.
        self.estimatedLoad = estimatedLoad

        #: Power that this service delivery point is configured to deliver.
        self.ratedPower = ratedPower

        #: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities.
        self.servicePriority = servicePriority

        #: True if grounded.
        self.grounded = grounded

        #: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority.
        self.serviceDeliveryRemark = serviceDeliveryRemark

        #: Phase code. Number of wires and number of phases can be deduced from enumeration literal values. For example, ABCN is three-phase, four-wire. s12n (splitSecondary12N) is single-phase, three-wire. s1n and s2n are single-phase, two-wire. Values are: "s12N", "BN", "BC", "ABN", "s2N", "N", "ACN", "BCN", "ABCN", "AC", "s1N", "AN", "B", "AB", "C", "A", "CN", "ABC"
        self.phaseCode = phaseCode

        #: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point.
        self.ctptReference = ctptReference

        #: Current that this service delivery point is configured to deliver.
        self.ratedCurrent = ratedCurrent

        #: Nominal service voltage.
        self.ratedVoltage = ratedVoltage

        self._SDPLocations = []
        self.SDPLocations = [] if SDPLocations is None else SDPLocations

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._EndDevices = []
        self.EndDevices = [] if EndDevices is None else EndDevices

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._ServiceCategory = None
        self.ServiceCategory = ServiceCategory

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        self._EnergyConsumer = None
        self.EnergyConsumer = EnergyConsumer

        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._CustomerAgreement = None
        self.CustomerAgreement = CustomerAgreement

        self._TransformerTanks = None
        self.TransformerTanks = TransformerTanks

        super(ServiceDeliveryPoint, self).__init__(*args, **kw_args)

    _attrs = ["checkBilling", "estimatedLoad", "ratedPower", "servicePriority", "grounded", "serviceDeliveryRemark", "phaseCode", "ctptReference", "ratedCurrent", "ratedVoltage"]
    _attr_types = {"checkBilling": bool, "estimatedLoad": float, "ratedPower": float, "servicePriority": str, "grounded": bool, "serviceDeliveryRemark": str, "phaseCode": str, "ctptReference": int, "ratedCurrent": float, "ratedVoltage": float}
    _defaults = {"checkBilling": False, "estimatedLoad": 0.0, "ratedPower": 0.0, "servicePriority": '', "grounded": False, "serviceDeliveryRemark": '', "phaseCode": "s12N", "ctptReference": 0, "ratedCurrent": 0.0, "ratedVoltage": 0.0}
    _enums = {"phaseCode": "PhaseCode"}
    _refs = ["SDPLocations", "ServiceLocation", "EndDevices", "MeterReadings", "ServiceCategory", "PricingStructures", "EnergyConsumer", "ServiceSupplier", "CustomerAgreement", "TransformerTanks"]
    _many_refs = ["SDPLocations", "EndDevices", "MeterReadings", "PricingStructures"]

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

    def getEndDevices(self):
        """All end devices at this service delivery point.
        """
        return self._EndDevices

    def setEndDevices(self, value):
        for x in self._EndDevices:
            x.ServiceDeliveryPoint = None
        for y in value:
            y._ServiceDeliveryPoint = self
        self._EndDevices = value

    EndDevices = property(getEndDevices, setEndDevices)

    def addEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.ServiceDeliveryPoint = self

    def removeEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.ServiceDeliveryPoint = None

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

    def getTransformerTanks(self):
        """Transformer supplying this service delivery point.
        """
        return self._TransformerTanks

    def setTransformerTanks(self, value):
        if self._TransformerTanks is not None:
            filtered = [x for x in self.TransformerTanks.ServiceDeliveryPoints if x != self]
            self._TransformerTanks._ServiceDeliveryPoints = filtered

        self._TransformerTanks = value
        if self._TransformerTanks is not None:
            if self not in self._TransformerTanks._ServiceDeliveryPoints:
                self._TransformerTanks._ServiceDeliveryPoints.append(self)

    TransformerTanks = property(getTransformerTanks, setTransformerTanks)

