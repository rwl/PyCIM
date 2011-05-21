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

from CIM14.IEC61968.Common.Organisation import Organisation

class Customer(Organisation):
    """Organisation receiving services from ServiceSupplier.
    """

    def __init__(self, kind="residentialAndCommercial", pucNumber='', specialNeed='', vip=False, status=None, Works=None, CustomerAgreements=None, EndDeviceAssets=None, *args, **kw_args):
        """Initialises a new 'Customer' instance.

        @param kind: Kind of customer. Values are: "residentialAndCommercial", "residentialStreetlightOthers", "residentialAndStreetlight", "pumpingLoad", "energyServiceSupplier", "windMachine", "residential", "internalUse", "residentialFarmService", "other", "energyServiceScheduler", "commercialIndustrial"
        @param pucNumber: (if applicable) Public Utility Commission identification number. 
        @param specialNeed: True if customer organisation has special service needs such as life support, hospitals, etc. 
        @param vip: True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute. 
        @param status: Status of this customer.
        @param Works: All the works performed for this customer.
        @param CustomerAgreements: All agreements of this customer.
        @param EndDeviceAssets: All end device assets of this customer.
        """
        #: Kind of customer. Values are: "residentialAndCommercial", "residentialStreetlightOthers", "residentialAndStreetlight", "pumpingLoad", "energyServiceSupplier", "windMachine", "residential", "internalUse", "residentialFarmService", "other", "energyServiceScheduler", "commercialIndustrial"
        self.kind = kind

        #: (if applicable) Public Utility Commission identification number.
        self.pucNumber = pucNumber

        #: True if customer organisation has special service needs such as life support, hospitals, etc.
        self.specialNeed = specialNeed

        #: True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute.
        self.vip = vip

        self.status = status

        self._Works = []
        self.Works = [] if Works is None else Works

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        super(Customer, self).__init__(*args, **kw_args)

    _attrs = ["kind", "pucNumber", "specialNeed", "vip"]
    _attr_types = {"kind": str, "pucNumber": str, "specialNeed": str, "vip": bool}
    _defaults = {"kind": "residentialAndCommercial", "pucNumber": '', "specialNeed": '', "vip": False}
    _enums = {"kind": "CustomerKind"}
    _refs = ["status", "Works", "CustomerAgreements", "EndDeviceAssets"]
    _many_refs = ["Works", "CustomerAgreements", "EndDeviceAssets"]

    # Status of this customer.
    status = None

    def getWorks(self):
        """All the works performed for this customer.
        """
        return self._Works

    def setWorks(self, value):
        for p in self._Works:
            filtered = [q for q in p.Customers if q != self]
            self._Works._Customers = filtered
        for r in value:
            if self not in r._Customers:
                r._Customers.append(self)
        self._Works = value

    Works = property(getWorks, setWorks)

    def addWorks(self, *Works):
        for obj in Works:
            if self not in obj._Customers:
                obj._Customers.append(self)
            self._Works.append(obj)

    def removeWorks(self, *Works):
        for obj in Works:
            if self in obj._Customers:
                obj._Customers.remove(self)
            self._Works.remove(obj)

    def getCustomerAgreements(self):
        """All agreements of this customer.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x.Customer = None
        for y in value:
            y._Customer = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.Customer = self

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj.Customer = None

    def getEndDeviceAssets(self):
        """All end device assets of this customer.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for x in self._EndDeviceAssets:
            x.Customer = None
        for y in value:
            y._Customer = self
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj.Customer = self

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj.Customer = None

