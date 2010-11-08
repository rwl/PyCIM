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

from CIM14.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system model
    """

    def __init__(self, customerCount=0, qfixedPct=0.0, pfixed=0.0, pfixedPct=0.0, qfixed=0.0, aggregateLoad0=None, PowerCutZone=None, ServiceDeliveryPoints=None, LoadResponse=None, *args, **kw_args):
        """Initialises a new 'EnergyConsumer' instance.

        @param customerCount: Number of individual customers represented by this Demand 
        @param qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. 
        @param pfixed: Active power of the load that is a fixed quantity. 
        @param pfixedPct: Fixed active power as per cent of load group fixed active power 
        @param qfixed: Reactive power of the load that is a fixed quantity. 
        @param aggregateLoad0:
        @param PowerCutZone: An energy consumer is assigned to a power cut zone
        @param ServiceDeliveryPoints:
        @param LoadResponse: The load response characteristic of this load.
        """
        #: Number of individual customers represented by this Demand
        self.customerCount = customerCount

        #: Fixed reactive power as per cent of load group fixed reactive power.
        self.qfixedPct = qfixedPct

        #: Active power of the load that is a fixed quantity.
        self.pfixed = pfixed

        #: Fixed active power as per cent of load group fixed active power
        self.pfixedPct = pfixedPct

        #: Reactive power of the load that is a fixed quantity.
        self.qfixed = qfixed

        self._aggregateLoad0 = []
        self.aggregateLoad0 = [] if aggregateLoad0 is None else aggregateLoad0

        self._PowerCutZone = None
        self.PowerCutZone = PowerCutZone

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._LoadResponse = None
        self.LoadResponse = LoadResponse

        super(EnergyConsumer, self).__init__(*args, **kw_args)

    _attrs = ["customerCount", "qfixedPct", "pfixed", "pfixedPct", "qfixed"]
    _attr_types = {"customerCount": int, "qfixedPct": float, "pfixed": float, "pfixedPct": float, "qfixed": float}
    _defaults = {"customerCount": 0, "qfixedPct": 0.0, "pfixed": 0.0, "pfixedPct": 0.0, "qfixed": 0.0}
    _enums = {}
    _refs = ["aggregateLoad0", "PowerCutZone", "ServiceDeliveryPoints", "LoadResponse"]
    _many_refs = ["aggregateLoad0", "ServiceDeliveryPoints"]

    def getaggregateLoad0(self):
        
        return self._aggregateLoad0

    def setaggregateLoad0(self, value):
        for p in self._aggregateLoad0:
            filtered = [q for q in p.energyConsumer0 if q != self]
            self._aggregateLoad0._energyConsumer0 = filtered
        for r in value:
            if self not in r._energyConsumer0:
                r._energyConsumer0.append(self)
        self._aggregateLoad0 = value

    aggregateLoad0 = property(getaggregateLoad0, setaggregateLoad0)

    def addaggregateLoad0(self, *aggregateLoad0):
        for obj in aggregateLoad0:
            if self not in obj._energyConsumer0:
                obj._energyConsumer0.append(self)
            self._aggregateLoad0.append(obj)

    def removeaggregateLoad0(self, *aggregateLoad0):
        for obj in aggregateLoad0:
            if self in obj._energyConsumer0:
                obj._energyConsumer0.remove(self)
            self._aggregateLoad0.remove(obj)

    def getPowerCutZone(self):
        """An energy consumer is assigned to a power cut zone
        """
        return self._PowerCutZone

    def setPowerCutZone(self, value):
        if self._PowerCutZone is not None:
            filtered = [x for x in self.PowerCutZone.EnergyConsumers if x != self]
            self._PowerCutZone._EnergyConsumers = filtered

        self._PowerCutZone = value
        if self._PowerCutZone is not None:
            self._PowerCutZone._EnergyConsumers.append(self)

    PowerCutZone = property(getPowerCutZone, setPowerCutZone)

    def getServiceDeliveryPoints(self):
        
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x._EnergyConsumer = None
        for y in value:
            y._EnergyConsumer = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._EnergyConsumer = self
            self._ServiceDeliveryPoints.append(obj)

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj._EnergyConsumer = None
            self._ServiceDeliveryPoints.remove(obj)

    def getLoadResponse(self):
        """The load response characteristic of this load.
        """
        return self._LoadResponse

    def setLoadResponse(self, value):
        if self._LoadResponse is not None:
            filtered = [x for x in self.LoadResponse.EnergyConsumer if x != self]
            self._LoadResponse._EnergyConsumer = filtered

        self._LoadResponse = value
        if self._LoadResponse is not None:
            self._LoadResponse._EnergyConsumer.append(self)

    LoadResponse = property(getLoadResponse, setLoadResponse)

