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

from CIM14.IEC61968.Common.Organisation import Organisation

class ServiceSupplier(Organisation):
    """Organisation that provides services to Customers.
    """

    def __init__(self, kind="retailer", issuerIdentificationNumber='', CustomerAgreements=None, ServiceDeliveryPoints=None, *args, **kw_args):
        """Initialises a new 'ServiceSupplier' instance.

        @param kind: Kind of supplier. Values are: "retailer", "utility", "other"
        @param issuerIdentificationNumber: Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2. 
        @param CustomerAgreements: All customer agreements of this service supplier.
        @param ServiceDeliveryPoints: All service delivery points this service supplier utilises to deliver a service.
        """
        #: Kind of supplier. Values are: "retailer", "utility", "other"
        self.kind = kind

        #: Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2.
        self.issuerIdentificationNumber = issuerIdentificationNumber

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        super(ServiceSupplier, self).__init__(*args, **kw_args)

    _attrs = ["kind", "issuerIdentificationNumber"]
    _attr_types = {"kind": str, "issuerIdentificationNumber": str}
    _defaults = {"kind": "retailer", "issuerIdentificationNumber": ''}
    _enums = {"kind": "SupplierKind"}
    _refs = ["CustomerAgreements", "ServiceDeliveryPoints"]
    _many_refs = ["CustomerAgreements", "ServiceDeliveryPoints"]

    def getCustomerAgreements(self):
        """All customer agreements of this service supplier.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x._ServiceSupplier = None
        for y in value:
            y._ServiceSupplier = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._ServiceSupplier = self
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._ServiceSupplier = None
            self._CustomerAgreements.remove(obj)

    def getServiceDeliveryPoints(self):
        """All service delivery points this service supplier utilises to deliver a service.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x._ServiceSupplier = None
        for y in value:
            y._ServiceSupplier = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._ServiceSupplier = self
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._ServiceSupplier = None
            self._ServiceDeliveryPoints.remove(obj)

