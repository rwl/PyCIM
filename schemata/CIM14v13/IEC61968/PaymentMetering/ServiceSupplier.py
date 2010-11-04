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

from CIM14v13.IEC61968.Common.Organisation import Organisation

class ServiceSupplier(Organisation):
    """Organisation that provides services to Customers.
    """

    def __init__(self, kind='other', issuerIdentificationNumber='', ServiceDeliveryPoints=None, CustomerAgreements=None, BankAccounts=None, *args, **kw_args):
        """Initializes a new 'ServiceSupplier' instance.

        @param kind: Kind of supplier. Values are: "other", "retailer", "utility"
        @param issuerIdentificationNumber: Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2. 
        @param ServiceDeliveryPoints: All service delivery points this service supplier utilises to deliver a service.
        @param CustomerAgreements: All customer agreements of this service supplier.
        @param BankAccounts: All BackAccounts this ServiceSupplier owns.
        """
        #: Kind of supplier.Values are: "other", "retailer", "utility"
        self.kind = kind

        #: Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2.
        self.issuerIdentificationNumber = issuerIdentificationNumber

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._BankAccounts = []
        self.BankAccounts = [] if BankAccounts is None else BankAccounts

        super(ServiceSupplier, self).__init__(*args, **kw_args)

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

    def getBankAccounts(self):
        """All BackAccounts this ServiceSupplier owns.
        """
        return self._BankAccounts

    def setBankAccounts(self, value):
        for x in self._BankAccounts:
            x._ServiceSupplier = None
        for y in value:
            y._ServiceSupplier = self
        self._BankAccounts = value

    BankAccounts = property(getBankAccounts, setBankAccounts)

    def addBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj._ServiceSupplier = self
            self._BankAccounts.append(obj)

    def removeBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj._ServiceSupplier = None
            self._BankAccounts.remove(obj)

