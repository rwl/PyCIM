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

