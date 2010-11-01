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

class Customer(Organisation):
    """Organisation receiving services from ServiceSupplier.
    """

    def __init__(self, kind='windMachine', pucNumber='', specialNeed='', vip=False, TroubleTickets=None, Works=None, OutageNotifications=None, ErpPersons=None, EndDeviceAssets=None, CustomerAgreements=None, PlannedOutage=None, status=None, *args, **kw_args):
        """Initializes a new 'Customer' instance.

        @param kind: Kind of customer. Values are: "windMachine", "residentialFarmService", "residential", "energyServiceSupplier", "residentialStreetlightOthers", "other", "pumpingLoad", "commercialIndustrial", "residentialAndStreetlight", "residentialAndCommercial", "energyServiceScheduler", "internalUse"
        @param pucNumber: (if applicable) Public Utility Commission identification number. 
        @param specialNeed: True if customer organisation has special service needs such as life support, hospitals, etc. 
        @param vip: True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute. 
        @param TroubleTickets:
        @param Works: All the works performed for this customer.
        @param OutageNotifications:
        @param ErpPersons:
        @param EndDeviceAssets: All end device assets of this customer.
        @param CustomerAgreements: All agreements of this customer.
        @param PlannedOutage:
        @param status: Status of this customer.
        """
        #: Kind of customer. Values are: "windMachine", "residentialFarmService", "residential", "energyServiceSupplier", "residentialStreetlightOthers", "other", "pumpingLoad", "commercialIndustrial", "residentialAndStreetlight", "residentialAndCommercial", "energyServiceScheduler", "internalUse"
        self.kind = kind

        #: (if applicable) Public Utility Commission identification number. 
        self.pucNumber = pucNumber

        #: True if customer organisation has special service needs such as life support, hospitals, etc. 
        self.specialNeed = specialNeed

        #: True if this is an important customer. Importance is for matters different than those in 'specialNeed' attribute. 
        self.vip = vip

        self._TroubleTickets = []
        self.TroubleTickets = [] if TroubleTickets is None else TroubleTickets

        self._Works = []
        self.Works = [] if Works is None else Works

        self._OutageNotifications = []
        self.OutageNotifications = [] if OutageNotifications is None else OutageNotifications

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._EndDeviceAssets = []
        self.EndDeviceAssets = [] if EndDeviceAssets is None else EndDeviceAssets

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._PlannedOutage = None
        self.PlannedOutage = PlannedOutage

        self.status = status

        super(Customer, self).__init__(*args, **kw_args)

    def getTroubleTickets(self):
        
        return self._TroubleTickets

    def setTroubleTickets(self, value):
        for x in self._TroubleTickets:
            x._CustomerData = None
        for y in value:
            y._CustomerData = self
        self._TroubleTickets = value

    TroubleTickets = property(getTroubleTickets, setTroubleTickets)

    def addTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj._CustomerData = self
            self._TroubleTickets.append(obj)

    def removeTroubleTickets(self, *TroubleTickets):
        for obj in TroubleTickets:
            obj._CustomerData = None
            self._TroubleTickets.remove(obj)

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

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for x in self._ErpPersons:
            x._CustomerData = None
        for y in value:
            y._CustomerData = self
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj._CustomerData = self
            self._ErpPersons.append(obj)

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj._CustomerData = None
            self._ErpPersons.remove(obj)

    def getEndDeviceAssets(self):
        """All end device assets of this customer.
        """
        return self._EndDeviceAssets

    def setEndDeviceAssets(self, value):
        for x in self._EndDeviceAssets:
            x._Customer = None
        for y in value:
            y._Customer = self
        self._EndDeviceAssets = value

    EndDeviceAssets = property(getEndDeviceAssets, setEndDeviceAssets)

    def addEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj._Customer = self
            self._EndDeviceAssets.append(obj)

    def removeEndDeviceAssets(self, *EndDeviceAssets):
        for obj in EndDeviceAssets:
            obj._Customer = None
            self._EndDeviceAssets.remove(obj)

    def getCustomerAgreements(self):
        """All agreements of this customer.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for x in self._CustomerAgreements:
            x._Customer = None
        for y in value:
            y._Customer = self
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._Customer = self
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            obj._Customer = None
            self._CustomerAgreements.remove(obj)

    def getPlannedOutage(self):
        
        return self._PlannedOutage

    def setPlannedOutage(self, value):
        if self._PlannedOutage is not None:
            filtered = [x for x in self.PlannedOutage.CustomerDatas if x != self]
            self._PlannedOutage._CustomerDatas = filtered

        self._PlannedOutage = value
        if self._PlannedOutage is not None:
            self._PlannedOutage._CustomerDatas.append(self)

    PlannedOutage = property(getPlannedOutage, setPlannedOutage)

    # Status of this customer.
    status = None

