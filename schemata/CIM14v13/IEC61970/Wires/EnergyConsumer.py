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

from CIM14v13.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system model
    """

    def __init__(self, qfixedPct=0.0, pfixed=0.0, customerCount=0, qfixed=0.0, pfixedPct=0.0, PowerCutZone=None, ServiceDeliveryPoints=None, LoadResponse=None, *args, **kw_args):
        """Initializes a new 'EnergyConsumer' instance.

        @param qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. 
        @param pfixed: Active power of the load that is a fixed quantity. 
        @param customerCount: Number of individual customers represented by this Demand 
        @param qfixed: Reactive power of the load that is a fixed quantity. 
        @param pfixedPct: Fixed active power as per cent of load group fixed active power 
        @param PowerCutZone: An energy consumer is assigned to a power cut zone
        @param ServiceDeliveryPoints:
        @param LoadResponse: The load response characteristic of this load.
        """
        #: Fixed reactive power as per cent of load group fixed reactive power.
        self.qfixedPct = qfixedPct

        #: Active power of the load that is a fixed quantity.
        self.pfixed = pfixed

        #: Number of individual customers represented by this Demand
        self.customerCount = customerCount

        #: Reactive power of the load that is a fixed quantity.
        self.qfixed = qfixed

        #: Fixed active power as per cent of load group fixed active power
        self.pfixedPct = pfixedPct

        self._PowerCutZone = None
        self.PowerCutZone = PowerCutZone

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._LoadResponse = None
        self.LoadResponse = LoadResponse

        super(EnergyConsumer, self).__init__(*args, **kw_args)

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

