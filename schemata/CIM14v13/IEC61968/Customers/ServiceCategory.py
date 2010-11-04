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

class ServiceCategory(IdentifiedObject):
    """Category of service provided to the customer.
    """

    def __init__(self, kind='refuse', CustomerAgreements=None, ServiceDeliveryPoints=None, SPAccountingFunctions=None, PricingStructures=None, **kw_args):
        """Initializes a new 'ServiceCategory' instance.

        @param kind: Kind of service. Values are: "refuse", "other", "tvLicence", "internet", "electricty", "water", "heat", "rates", "gas", "sewerage", "time"
        @param CustomerAgreements:
        @param ServiceDeliveryPoints: All service delivery points that deliver this category of service.
        @param SPAccountingFunctions:
        @param PricingStructures: All pricing structures applicable to this service category.
        """
        #: Kind of service.Values are: "refuse", "other", "tvLicence", "internet", "electricty", "water", "heat", "rates", "gas", "sewerage", "time"
        self.kind = kind

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._SPAccountingFunctions = []
        self.SPAccountingFunctions = [] if SPAccountingFunctions is None else SPAccountingFunctions

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        super(ServiceCategory, self).__init__(**kw_args)

    def getCustomerAgreements(self):
        
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x._ServiceCategory = None
        for y in value:
            y._ServiceCategory = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._ServiceCategory = self
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._ServiceCategory = None
            self._CustomerAgreements.remove(obj)

    def getServiceDeliveryPoints(self):
        """All service delivery points that deliver this category of service.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x._ServiceCategory = None
        for y in value:
            y._ServiceCategory = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._ServiceCategory = self
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._ServiceCategory = None
            self._ServiceDeliveryPoints.remove(obj)

    def getSPAccountingFunctions(self):
        
        return self._SPAccountingFunctions

    def setSPAccountingFunctions(self, value):
        for x in self._SPAccountingFunctions:
            x._ServiceKind = None
        for y in value:
            y._ServiceKind = self
        self._SPAccountingFunctions = value

    SPAccountingFunctions = property(getSPAccountingFunctions, setSPAccountingFunctions)

    def addSPAccountingFunctions(self, *SPAccountingFunctions):
        for obj in SPAccountingFunctions:
            obj._ServiceKind = self
            self._SPAccountingFunctions.append(obj)

    def removeSPAccountingFunctions(self, *SPAccountingFunctions):
        for obj in SPAccountingFunctions:
            obj._ServiceKind = None
            self._SPAccountingFunctions.remove(obj)

    def getPricingStructures(self):
        """All pricing structures applicable to this service category.
        """
        return self._PricingStructures

    def setPricingStructures(self, value):
        for x in self._PricingStructures:
            x._ServiceCategory = None
        for y in value:
            y._ServiceCategory = self
        self._PricingStructures = value

    PricingStructures = property(getPricingStructures, setPricingStructures)

    def addPricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            obj._ServiceCategory = self
            self._PricingStructures.append(obj)

    def removePricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            obj._ServiceCategory = None
            self._PricingStructures.remove(obj)

