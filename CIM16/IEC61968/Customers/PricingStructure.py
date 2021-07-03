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

from CIM16.IEC61968.Common.Document import Document

class PricingStructure(Document):
    """Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.Grouping of pricing components and prices used in the creation of customer charges and the eligibility criteria under which these terms may be offered to a customer. The reasons for grouping include state, customer classification, site characteristics, classification (i.e. fee price structure, deposit price structure, electric service price structure, etc.) and accounting requirements.
    """

    def __init__(self, dailyFloorUsage=0, dailyCeilingUsage=0, taxExemption=False, code='', dailyEstimatedUsage=0, revenueKind="irrigation", ServiceCategory=None, CustomerAgreements=None, ServiceDeliveryPoints=None, Tariffs=None, Transactions=None, *args, **kw_args):
        """Initialises a new 'PricingStructure' instance.

        @param dailyFloorUsage: Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage. 
        @param dailyCeilingUsage: Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage. 
        @param taxExemption: True if this pricing structure is not taxable. 
        @param code: Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code. 
        @param dailyEstimatedUsage: Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting. 
        @param revenueKind: (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes). Values are: "irrigation", "residential", "nonResidential", "industrial", "other", "commercial", "streetLight"
        @param ServiceCategory: Service category to which this pricing structure applies.
        @param CustomerAgreements: All customer agreements with this pricing structure.
        @param ServiceDeliveryPoints: All service delivery points (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer) to which this pricing structure applies.
        @param Tariffs: All tariffs used by this pricing structure.
        @param Transactions: All transactions applying this pricing structure.
        """
        #: Absolute minimum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
        self.dailyFloorUsage = dailyFloorUsage

        #: Absolute maximum valid non-demand usage quantity used in validating a customer's billed non-demand usage.
        self.dailyCeilingUsage = dailyCeilingUsage

        #: True if this pricing structure is not taxable.
        self.taxExemption = taxExemption

        #: Unique user-allocated key for this pricing structure, used by company representatives to identify the correct price structure for allocating to a customer. For rate schedules it is often prefixed by a state code.
        self.code = code

        #: Used in place of actual computed estimated average when history of usage is not available, and typically manually entered by customer accounting.
        self.dailyEstimatedUsage = dailyEstimatedUsage

        #: (Accounting) Kind of revenue, often used to determine the grace period allowed, before collection actions are taken on a customer (grace periods vary between revenue classes). Values are: "irrigation", "residential", "nonResidential", "industrial", "other", "commercial", "streetLight"
        self.revenueKind = revenueKind

        self._ServiceCategory = None
        self.ServiceCategory = ServiceCategory

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._Tariffs = []
        self.Tariffs = [] if Tariffs is None else Tariffs

        self._Transactions = []
        self.Transactions = [] if Transactions is None else Transactions

        super(PricingStructure, self).__init__(*args, **kw_args)

    _attrs = ["dailyFloorUsage", "dailyCeilingUsage", "taxExemption", "code", "dailyEstimatedUsage", "revenueKind"]
    _attr_types = {"dailyFloorUsage": int, "dailyCeilingUsage": int, "taxExemption": bool, "code": str, "dailyEstimatedUsage": int, "revenueKind": str}
    _defaults = {"dailyFloorUsage": 0, "dailyCeilingUsage": 0, "taxExemption": False, "code": '', "dailyEstimatedUsage": 0, "revenueKind": "irrigation"}
    _enums = {"revenueKind": "RevenueKind"}
    _refs = ["ServiceCategory", "CustomerAgreements", "ServiceDeliveryPoints", "Tariffs", "Transactions"]
    _many_refs = ["CustomerAgreements", "ServiceDeliveryPoints", "Tariffs", "Transactions"]

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
            if self not in self._ServiceCategory._PricingStructures:
                self._ServiceCategory._PricingStructures.append(self)

    ServiceCategory = property(getServiceCategory, setServiceCategory)

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

    def getTransactions(self):
        """All transactions applying this pricing structure.
        """
        return self._Transactions

    def setTransactions(self, value):
        for x in self._Transactions:
            x.PricingStructure = None
        for y in value:
            y._PricingStructure = self
        self._Transactions = value

    Transactions = property(getTransactions, setTransactions)

    def addTransactions(self, *Transactions):
        for obj in Transactions:
            obj.PricingStructure = self

    def removeTransactions(self, *Transactions):
        for obj in Transactions:
            obj.PricingStructure = None

