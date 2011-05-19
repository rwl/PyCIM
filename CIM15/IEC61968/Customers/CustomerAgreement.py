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

from CIM15.IEC61968.Common.Agreement import Agreement

class CustomerAgreement(Agreement):
    """Agreement between the customer and the service supplier to pay for service at a specific service location. It records certain billing information about the type of service provided at the service location and is used during charge creation to determine the type of service.Agreement between the customer and the service supplier to pay for service at a specific service location. It records certain billing information about the type of service provided at the service location and is used during charge creation to determine the type of service.
    """

    def __init__(self, billingCycle='', loadMgmt='', budgetBill='', PricingStructures=None, CustomerAccount=None, StandardIndustryCode=None, AuxiliaryAgreements=None, MeterReadings=None, Equipments=None, ServiceSupplier=None, ServiceLocations=None, DemandResponseProgram=None, ServiceDeliveryPoints=None, Customer=None, EndDeviceControls=None, *args, **kw_args):
        """Initialises a new 'CustomerAgreement' instance.

        @param billingCycle: Cycle day on which the associated customer account will normally be billed, used to determine when to produce the billing. 
        @param loadMgmt: Load management code. 
        @param budgetBill: Budget bill code. 
        @param PricingStructures: All pricing structures applicable to this customer agreement.
        @param CustomerAccount: Customer account owning this agreement.
        @param StandardIndustryCode:
        @param AuxiliaryAgreements: All (non-service related) auxiliary agreements that refer to this customer agreement.
        @param MeterReadings: (could be deprecated in the future) All meter readings for this customer agreement.
        @param Equipments:
        @param ServiceSupplier: Service supplier for this customer agreement.
        @param ServiceLocations: All service locations regulated by this customer agreement.
        @param DemandResponseProgram: Demand response program for this customer agreement.
        @param ServiceDeliveryPoints: All service delivery points regulated by this customer agreement.
        @param Customer: Customer for this agreement.
        @param EndDeviceControls: Could be deprecated in the future.
        """
        #: Cycle day on which the associated customer account will normally be billed, used to determine when to produce the billing.
        self.billingCycle = billingCycle

        #: Load management code.
        self.loadMgmt = loadMgmt

        #: Budget bill code.
        self.budgetBill = budgetBill

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        self._CustomerAccount = None
        self.CustomerAccount = CustomerAccount

        self._StandardIndustryCode = None
        self.StandardIndustryCode = StandardIndustryCode

        self._AuxiliaryAgreements = []
        self.AuxiliaryAgreements = [] if AuxiliaryAgreements is None else AuxiliaryAgreements

        self._MeterReadings = []
        self.MeterReadings = [] if MeterReadings is None else MeterReadings

        self._Equipments = []
        self.Equipments = [] if Equipments is None else Equipments

        self._ServiceSupplier = None
        self.ServiceSupplier = ServiceSupplier

        self._ServiceLocations = []
        self.ServiceLocations = [] if ServiceLocations is None else ServiceLocations

        self._DemandResponseProgram = None
        self.DemandResponseProgram = DemandResponseProgram

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._Customer = None
        self.Customer = Customer

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        super(CustomerAgreement, self).__init__(*args, **kw_args)

    _attrs = ["billingCycle", "loadMgmt", "budgetBill"]
    _attr_types = {"billingCycle": str, "loadMgmt": str, "budgetBill": str}
    _defaults = {"billingCycle": '', "loadMgmt": '', "budgetBill": ''}
    _enums = {}
    _refs = ["PricingStructures", "CustomerAccount", "StandardIndustryCode", "AuxiliaryAgreements", "MeterReadings", "Equipments", "ServiceSupplier", "ServiceLocations", "DemandResponseProgram", "ServiceDeliveryPoints", "Customer", "EndDeviceControls"]
    _many_refs = ["PricingStructures", "AuxiliaryAgreements", "MeterReadings", "Equipments", "ServiceLocations", "ServiceDeliveryPoints", "EndDeviceControls"]

    def getPricingStructures(self):
        """All pricing structures applicable to this customer agreement.
        """
        return self._PricingStructures

    def setPricingStructures(self, value):
        for p in self._PricingStructures:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._PricingStructures._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._PricingStructures = value

    PricingStructures = property(getPricingStructures, setPricingStructures)

    def addPricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._PricingStructures.append(obj)

    def removePricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._PricingStructures.remove(obj)

    def getCustomerAccount(self):
        """Customer account owning this agreement.
        """
        return self._CustomerAccount

    def setCustomerAccount(self, value):
        if self._CustomerAccount is not None:
            filtered = [x for x in self.CustomerAccount.CustomerAgreements if x != self]
            self._CustomerAccount._CustomerAgreements = filtered

        self._CustomerAccount = value
        if self._CustomerAccount is not None:
            if self not in self._CustomerAccount._CustomerAgreements:
                self._CustomerAccount._CustomerAgreements.append(self)

    CustomerAccount = property(getCustomerAccount, setCustomerAccount)

    def getStandardIndustryCode(self):
        
        return self._StandardIndustryCode

    def setStandardIndustryCode(self, value):
        if self._StandardIndustryCode is not None:
            filtered = [x for x in self.StandardIndustryCode.CustomerAgreements if x != self]
            self._StandardIndustryCode._CustomerAgreements = filtered

        self._StandardIndustryCode = value
        if self._StandardIndustryCode is not None:
            if self not in self._StandardIndustryCode._CustomerAgreements:
                self._StandardIndustryCode._CustomerAgreements.append(self)

    StandardIndustryCode = property(getStandardIndustryCode, setStandardIndustryCode)

    def getAuxiliaryAgreements(self):
        """All (non-service related) auxiliary agreements that refer to this customer agreement.
        """
        return self._AuxiliaryAgreements

    def setAuxiliaryAgreements(self, value):
        for x in self._AuxiliaryAgreements:
            x.CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._AuxiliaryAgreements = value

    AuxiliaryAgreements = property(getAuxiliaryAgreements, setAuxiliaryAgreements)

    def addAuxiliaryAgreements(self, *AuxiliaryAgreements):
        for obj in AuxiliaryAgreements:
            obj.CustomerAgreement = self

    def removeAuxiliaryAgreements(self, *AuxiliaryAgreements):
        for obj in AuxiliaryAgreements:
            obj.CustomerAgreement = None

    def getMeterReadings(self):
        """(could be deprecated in the future) All meter readings for this customer agreement.
        """
        return self._MeterReadings

    def setMeterReadings(self, value):
        for x in self._MeterReadings:
            x.CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._MeterReadings = value

    MeterReadings = property(getMeterReadings, setMeterReadings)

    def addMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.CustomerAgreement = self

    def removeMeterReadings(self, *MeterReadings):
        for obj in MeterReadings:
            obj.CustomerAgreement = None

    def getEquipments(self):
        
        return self._Equipments

    def setEquipments(self, value):
        for p in self._Equipments:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._Equipments._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._Equipments = value

    Equipments = property(getEquipments, setEquipments)

    def addEquipments(self, *Equipments):
        for obj in Equipments:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._Equipments.append(obj)

    def removeEquipments(self, *Equipments):
        for obj in Equipments:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._Equipments.remove(obj)

    def getServiceSupplier(self):
        """Service supplier for this customer agreement.
        """
        return self._ServiceSupplier

    def setServiceSupplier(self, value):
        if self._ServiceSupplier is not None:
            filtered = [x for x in self.ServiceSupplier.CustomerAgreements if x != self]
            self._ServiceSupplier._CustomerAgreements = filtered

        self._ServiceSupplier = value
        if self._ServiceSupplier is not None:
            if self not in self._ServiceSupplier._CustomerAgreements:
                self._ServiceSupplier._CustomerAgreements.append(self)

    ServiceSupplier = property(getServiceSupplier, setServiceSupplier)

    def getServiceLocations(self):
        """All service locations regulated by this customer agreement.
        """
        return self._ServiceLocations

    def setServiceLocations(self, value):
        for p in self._ServiceLocations:
            filtered = [q for q in p.CustomerAgreements if q != self]
            self._ServiceLocations._CustomerAgreements = filtered
        for r in value:
            if self not in r._CustomerAgreements:
                r._CustomerAgreements.append(self)
        self._ServiceLocations = value

    ServiceLocations = property(getServiceLocations, setServiceLocations)

    def addServiceLocations(self, *ServiceLocations):
        for obj in ServiceLocations:
            if self not in obj._CustomerAgreements:
                obj._CustomerAgreements.append(self)
            self._ServiceLocations.append(obj)

    def removeServiceLocations(self, *ServiceLocations):
        for obj in ServiceLocations:
            if self in obj._CustomerAgreements:
                obj._CustomerAgreements.remove(self)
            self._ServiceLocations.remove(obj)

    def getDemandResponseProgram(self):
        """Demand response program for this customer agreement.
        """
        return self._DemandResponseProgram

    def setDemandResponseProgram(self, value):
        if self._DemandResponseProgram is not None:
            filtered = [x for x in self.DemandResponseProgram.CustomerAgreements if x != self]
            self._DemandResponseProgram._CustomerAgreements = filtered

        self._DemandResponseProgram = value
        if self._DemandResponseProgram is not None:
            if self not in self._DemandResponseProgram._CustomerAgreements:
                self._DemandResponseProgram._CustomerAgreements.append(self)

    DemandResponseProgram = property(getDemandResponseProgram, setDemandResponseProgram)

    def getServiceDeliveryPoints(self):
        """All service delivery points regulated by this customer agreement.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.CustomerAgreement = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.CustomerAgreement = None

    def getCustomer(self):
        """Customer for this agreement.
        """
        return self._Customer

    def setCustomer(self, value):
        if self._Customer is not None:
            filtered = [x for x in self.Customer.CustomerAgreements if x != self]
            self._Customer._CustomerAgreements = filtered

        self._Customer = value
        if self._Customer is not None:
            if self not in self._Customer._CustomerAgreements:
                self._Customer._CustomerAgreements.append(self)

    Customer = property(getCustomer, setCustomer)

    def getEndDeviceControls(self):
        """Could be deprecated in the future.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x.CustomerAgreement = None
        for y in value:
            y._CustomerAgreement = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.CustomerAgreement = self

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.CustomerAgreement = None

