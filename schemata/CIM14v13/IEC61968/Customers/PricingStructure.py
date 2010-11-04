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

from CIM14v13.IEC61968.Common.Document import Document

class PricingStructure(Document):
    """Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.
    """

    def __init__(self, revenueKind='streetLight', code='', dailyFloorUsage=0, taxExemption=False, dailyCeilingUsage=0, dailyEstimatedUsage=0, Tariffs=None, PowerQualityPricings=None, Transactions=None, ServiceDeliveryPoints=None, CustomerAgreements=None, SubscribePowerCurve=None, ServiceCategory=None, **kw_args):
        """Initializes a new 'PricingStructure' instance.

        @param revenueKind: (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes). Values are: "streetLight", "commercial", "other", "irrigation", "nonResidential", "industrial", "residential"
        @param code: Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code. 
        @param dailyFloorUsage: Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage. 
        @param taxExemption: True if this pricing structure is not taxable. 
        @param dailyCeilingUsage: Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage. 
        @param dailyEstimatedUsage: Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting. 
        @param Tariffs: All tariffs used by this pricing structure.
        @param PowerQualityPricings:
        @param Transactions: All transactions applying this pricing structure.
        @param ServiceDeliveryPoints: All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.
        @param CustomerAgreements: All customer agreements with this pricing structure.
        @param SubscribePowerCurve: SubscribePowerCurve specifies the cost according to a prcing structure.
        @param ServiceCategory: Service category to which this pricing structure applies.
        """
        #: (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes).Values are: "streetLight", "commercial", "other", "irrigation", "nonResidential", "industrial", "residential"
        self.revenueKind = revenueKind

        #: Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code.
        self.code = code

        #: Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
        self.dailyFloorUsage = dailyFloorUsage

        #: True if this pricing structure is not taxable.
        self.taxExemption = taxExemption

        #: Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
        self.dailyCeilingUsage = dailyCeilingUsage

        #: Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting.
        self.dailyEstimatedUsage = dailyEstimatedUsage

        self._Tariffs = []
        self.Tariffs = [] if Tariffs is None else Tariffs

        self._PowerQualityPricings = []
        self.PowerQualityPricings = [] if PowerQualityPricings is None else PowerQualityPricings

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._SubscribePowerCurve = None
        self.SubscribePowerCurve = SubscribePowerCurve

        self._ServiceCategory = None
        self.ServiceCategory = ServiceCategory

        super(PricingStructure, self).__init__(**kw_args)

    def getTariffs(self):
        """All tariffs used by this pricing structure.
        """
        return self._Tariffs

    def setTariffs(self, value):
        for p in self._Tariffs:
            filtered = [q for q in p.PricingStructures if q != self]
            self._Tariffs._PricingStructures = filtered
        for r in value:
            if self not in r._PricingStructures:
                r._PricingStructures.append(self)
        self._Tariffs = value

    Tariffs = property(getTariffs, setTariffs)

    def addTariffs(self, *Tariffs):
        for obj in Tariffs:
            if self not in obj._PricingStructures:
                obj._PricingStructures.append(self)
            self._Tariffs.append(obj)

    def removeTariffs(self, *Tariffs):
        for obj in Tariffs:
            if self in obj._PricingStructures:
                obj._PricingStructures.remove(self)
            self._Tariffs.remove(obj)

    def getPowerQualityPricings(self):
        
        return self._PowerQualityPricings

    def setPowerQualityPricings(self, value):
        for x in self._PowerQualityPricings:
            x._PricingStructure = None
        for y in value:
            y._PricingStructure = self
        self._PowerQualityPricings = value

    PowerQualityPricings = property(getPowerQualityPricings, setPowerQualityPricings)

    def addPowerQualityPricings(self, *PowerQualityPricings):
        for obj in PowerQualityPricings:
            obj._PricingStructure = self
            self._PowerQualityPricings.append(obj)

    def removePowerQualityPricings(self, *PowerQualityPricings):
        for obj in PowerQualityPricings:
            obj._PricingStructure = None
            self._PowerQualityPricings.remove(obj)

    def getTransactions(self):
        """All transactions applying this pricing structure.
        """
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x._PricingStructure = None
        for y in value:
            y._PricingStructure = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj._PricingStructure = self
            self._Transactions.append(obj)

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj._PricingStructure = None
            self._Transactions.remove(obj)

    def getServiceDeliveryPoints(self):
        """All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for p in self._ServiceDeliveryPoints:
            filtered = [q for q in p.PricingStructures if q != self]
            self._ServiceDeliveryPoints._PricingStructures = filtered
        for r in value:
            if self not in r._PricingStructures:
                r._PricingStructures.append(self)
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            if self not in obj._PricingStructures:
                obj._PricingStructures.append(self)
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            if self in obj._PricingStructures:
                obj._PricingStructures.remove(self)
            self._ServiceDeliveryPoints.remove(obj)

    def getCustomerAgreements(self):
        """All customer agreements with this pricing structure.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for p in self._CustomerAgreements:
            filtered = [q for q in p.PricingStructures if q != self]
            self._CustomerAgreements._PricingStructures = filtered
        for r in value:
            if self not in r._PricingStructures:
                r._PricingStructures.append(self)
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            if self not in obj._PricingStructures:
                obj._PricingStructures.append(self)
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            if self in obj._PricingStructures:
                obj._PricingStructures.remove(self)
            self._CustomerAgreements.remove(obj)

    def getSubscribePowerCurve(self):
        """SubscribePowerCurve specifies the cost according to a prcing structure.
        """
        return self._SubscribePowerCurve

    def setSubscribePowerCurve(self, value):
        if self._SubscribePowerCurve is not None:
            self._SubscribePowerCurve._PricingStructure = None

        self._SubscribePowerCurve = value
        if self._SubscribePowerCurve is not None:
            self._SubscribePowerCurve._PricingStructure = self

    SubscribePowerCurve = property(getSubscribePowerCurve, setSubscribePowerCurve)

    def getServiceCategory(self):
        """Service category to which this pricing structure applies.
        """
        return self._ServiceCategory

    def setServiceCategory(self, value):
        if self._ServiceCategory is not None:
            filtered = [x for x in self.ServiceCategory.PricingStructures if x != self]
            self._ServiceCategory._PricingStructures = filtered

        self._ServiceCategory = value
        if self._ServiceCategory is not None:
            self._ServiceCategory._PricingStructures.append(self)

    ServiceCategory = property(getServiceCategory, setServiceCategory)

