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

class Customer(Organisation):
    """Organisation receiving services from ServiceSupplier.Organisation receiving services from ServiceSupplier.
    """

    def __init__(self, vip=False, pucNumber='', specialNeed='', kind="windMachine", CustomerAgreements=None, ErpPersons=None, EndDevices=None, Works=None, status=None, PlannedOutage=None, OutageNotifications=None, TroubleTickets=None, *args, **kw_args):
        """Initialises a new 'Customer' instance.

        @param vip: True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute. 
        @param pucNumber: (if applicable) Public utility commission (PUC) identification number. 
        @param specialNeed: True if customer organisation has special service needs such as life support, hospitals, etc. 
        @param kind: Kind of customer. Values are: "windMachine", "residentialAndCommercial", "internalUse", "energyServiceScheduler", "residentialAndStreetlight", "residential", "pumpingLoad", "other", "commercialIndustrial", "energyServiceSupplier", "residentialStreetlightOthers", "residentialFarmService"
        @param CustomerAgreements: All agreements of this customer.
        @param ErpPersons:
        @param EndDevices: All end devices of this customer.
        @param Works: All the works performed for this customer.
        @param status: Status of this customer.
        @param PlannedOutage:
        @param OutageNotifications:
        @param TroubleTickets:
        """
        #: True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute.
        self.vip = vip

        #: (if applicable) Public utility commission (PUC) identification number.
        self.pucNumber = pucNumber

        #: True if customer organisation has special service needs such as life support, hospitals, etc.
        self.specialNeed = specialNeed

        #: Kind of customer. Values are: "windMachine", "residentialAndCommercial", "internalUse", "energyServiceScheduler", "residentialAndStreetlight", "residential", "pumpingLoad", "other", "commercialIndustrial", "energyServiceSupplier", "residentialStreetlightOthers", "residentialFarmService"
        self.kind = kind

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._EndDevices = []
        self.EndDevices = [] if EndDevices is None else EndDevices

        self._Works = []
        self.Works = [] if Works is None else Works

        self.status = status

        self._PlannedOutage = None
        self.PlannedOutage = PlannedOutage

        self._OutageNotifications = []
        self.OutageNotifications = [] if OutageNotifications is None else OutageNotifications

        self._TroubleTickets = []
        self.TroubleTickets = [] if TroubleTickets is None else TroubleTickets

        super(Customer, self).__init__(*args, **kw_args)

    _attrs = ["vip", "pucNumber", "specialNeed", "kind"]
    _attr_types = {"vip": bool, "pucNumber": str, "specialNeed": str, "kind": str}
    _defaults = {"vip": False, "pucNumber": '', "specialNeed": '', "kind": "windMachine"}
    _enums = {"kind": "CustomerKind"}
    _refs = ["CustomerAgreements", "ErpPersons", "EndDevices", "Works", "status", "PlannedOutage", "OutageNotifications", "TroubleTickets"]
    _many_refs = ["CustomerAgreements", "ErpPersons", "EndDevices", "Works", "OutageNotifications", "TroubleTickets"]

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

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for x in self._ErpPersons:
            x.CustomerData = None
        for y in value:
            y._CustomerData = self
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj.CustomerData = self

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj.CustomerData = None

    def getEndDevices(self):
        """All end devices of this customer.
        """
        return self._EndDevices

    def setEndDevices(self, value):
        for x in self._EndDevices:
            x.Customer = None
        for y in value:
            y._Customer = self
        self._EndDevices = value

    EndDevices = property(getEndDevices, setEndDevices)

    def addEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.Customer = self

    def removeEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.Customer = None

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

    # Status of this customer.
    status = None

    def getPlannedOutage(self):
        
        return self._PlannedOutage

    def setPlannedOutage(self, value):
        if self._PlannedOutage is not None:
            filtered = [x for x in self.PlannedOutage.CustomerDatas if x != self]
            self._PlannedOutage._CustomerDatas = filtered

        self._PlannedOutage = value
        if self._PlannedOutage is not None:
            if self not in self._PlannedOutage._CustomerDatas:
                self._PlannedOutage._CustomerDatas.append(self)

    PlannedOutage = property(getPlannedOutage, setPlannedOutage)

    def getOutageNotifications(self):
        
        return self._OutageNotifications

    def setOutageNotifications(self, value):
        for p in self._OutageNotifications:
            filtered = [q for q in p.CustomerDatas if q != self]
            self._OutageNotifications._CustomerDatas = filtered
        for r in value:
            if self not in r._CustomerDatas:
                r._CustomerDatas.append(self)
        self._OutageNotifications = value

    OutageNotifications = property(getOutageNotifications, setOutageNotifications)

    def addOutageNotifications(self, *OutageNotifications):
        for obj in OutageNotifications:
            if self not in obj._CustomerDatas:
                obj._CustomerDatas.append(self)
            self._OutageNotifications.append(obj)

    def removeOutageNotifications(self, *OutageNotifications):
        for obj in OutageNotifications:
            if self in obj._CustomerDatas:
                obj._CustomerDatas.remove(self)
            self._OutageNotifications.remove(obj)

    def getTroubleTickets(self):
        
        return self._TroubleTickets

    def setTroubleTickets(self, value):
        for x in self._TroubleTickets:
            x.CustomerData = None
        for y in value:
            y._CustomerData = self
        self._TroubleTickets = value

    TroubleTickets = property(getTroubleTickets, setTroubleTickets)

    def addTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj.CustomerData = self

    def removeTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj.CustomerData = None

