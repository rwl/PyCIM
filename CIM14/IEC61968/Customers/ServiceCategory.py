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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class ServiceCategory(IdentifiedObject):
    """Category of service provided to the customer.
    """

    def __init__(self, kind="water", CustomerAgreements=None, PricingStructures=None, ServiceDeliveryPoints=None, *args, **kw_args):
        """Initialises a new 'ServiceCategory' instance.

        @param kind: Kind of service. Values are: "water", "time", "electricity", "heat", "rates", "gas", "internet", "refuse", "other", "tvLicence", "sewerage"
        @param CustomerAgreements:
        @param PricingStructures: All pricing structures applicable to this service category.
        @param ServiceDeliveryPoints: All service delivery points that deliver this category of service.
        """
        #: Kind of service. Values are: "water", "time", "electricity", "heat", "rates", "gas", "internet", "refuse", "other", "tvLicence", "sewerage"
        self.kind = kind

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        super(ServiceCategory, self).__init__(*args, **kw_args)

    _attrs = ["kind"]
    _attr_types = {"kind": str}
    _defaults = {"kind": "water"}
    _enums = {"kind": "ServiceKind"}
    _refs = ["CustomerAgreements", "PricingStructures", "ServiceDeliveryPoints"]
    _many_refs = ["CustomerAgreements", "PricingStructures", "ServiceDeliveryPoints"]

    def getCustomerAgreements(self):
        
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x.ServiceCategory = None
        for y in value:
            y._ServiceCategory = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.ServiceCategory = self

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.ServiceCategory = None

    def getPricingStructures(self):
        """All pricing structures applicable to this service category.
        """
        return self._PricingStructures

    def setPricingStructures(self, value):
        for x in self._PricingStructures:
            x.ServiceCategory = None
        for y in value:
            y._ServiceCategory = self
        self._PricingStructures = value

    PricingStructures = property(getPricingStructures, setPricingStructures)

    def addPricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            obj.ServiceCategory = self

    def removePricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            obj.ServiceCategory = None

    def getServiceDeliveryPoints(self):
        """All service delivery points that deliver this category of service.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.ServiceCategory = None
        for y in value:
            y._ServiceCategory = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.ServiceCategory = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.ServiceCategory = None

