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

from CIM15.IEC61968.Common.Organisation import Organisation

class ServiceSupplier(Organisation):
    """Organisation that provides services to customers.Organisation that provides services to customers.
    """

    def __init__(self, issuerIdentificationNumber='', kind="other", BankAccounts=None, ServiceDeliveryPoints=None, CustomerAgreements=None, *args, **kw_args):
        """Initialises a new 'ServiceSupplier' instance.

        @param issuerIdentificationNumber: Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2. 
        @param kind: Kind of supplier. Values are: "other", "retailer", "utility"
        @param BankAccounts: All BackAccounts this ServiceSupplier owns.
        @param ServiceDeliveryPoints: All service delivery points this service supplier utilises to deliver a service.
        @param CustomerAgreements: All customer agreements of this service supplier.
        """
        #: Unique transaction reference prefix number issued to an entity by the International Standards Organisation for the purpose of tagging onto electronic financial transactions, as defined in ISO/IEC 7812-1 and ISO/IEC 7812-2.
        self.issuerIdentificationNumber = issuerIdentificationNumber

        #: Kind of supplier. Values are: "other", "retailer", "utility"
        self.kind = kind

        self._BankAccounts = []
        self.BankAccounts = [] if BankAccounts is None else BankAccounts

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        super(ServiceSupplier, self).__init__(*args, **kw_args)

    _attrs = ["issuerIdentificationNumber", "kind"]
    _attr_types = {"issuerIdentificationNumber": str, "kind": str}
    _defaults = {"issuerIdentificationNumber": '', "kind": "other"}
    _enums = {"kind": "SupplierKind"}
    _refs = ["BankAccounts", "ServiceDeliveryPoints", "CustomerAgreements"]
    _many_refs = ["BankAccounts", "ServiceDeliveryPoints", "CustomerAgreements"]

    def getBankAccounts(self):
        """All BackAccounts this ServiceSupplier owns.
        """
        return self._BankAccounts

    def setBankAccounts(self, value):
        for x in self._BankAccounts:
            x.ServiceSupplier = None
        for y in value:
            y._ServiceSupplier = self
        self._BankAccounts = value

    BankAccounts = property(getBankAccounts, setBankAccounts)

    def addBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj.ServiceSupplier = self

    def removeBankAccounts(self, *BankAccounts):
        for obj in BankAccounts:
            obj.ServiceSupplier = None

    def getServiceDeliveryPoints(self):
        """All service delivery points this service supplier utilises to deliver a service.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.ServiceSupplier = None
        for y in value:
            y._ServiceSupplier = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.ServiceSupplier = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.ServiceSupplier = None

    def getCustomerAgreements(self):
        """All customer agreements of this service supplier.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x.ServiceSupplier = None
        for y in value:
            y._ServiceSupplier = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.ServiceSupplier = self

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.ServiceSupplier = None

