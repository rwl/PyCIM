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

from CIM15.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """

    def __init__(self, qfixedPct=0.0, customerCount=0, pfixedPct=0.0, pfixed=0.0, qfixed=0.0, ServiceDeliveryPoints=None, LoadResponse=None, PowerCutZone=None, EnergyConsumerPhases=None, *args, **kw_args):
        """Initialises a new 'EnergyConsumer' instance.

        @param qfixedPct: Fixed reactive power as per cent of load group fixed reactive power. Load sign convention is used, i.e. positive sign means flow out from a node. 
        @param customerCount: Number of individual customers represented by this Demand 
        @param pfixedPct: Fixed active power as per cent of load group fixed active power. Load sign convention is used, i.e. positive sign means flow out from a node. 
        @param pfixed: Active power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. 
        @param qfixed: Reactive power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node. 
        @param ServiceDeliveryPoints:
        @param LoadResponse: The load response characteristic of this load.
        @param PowerCutZone: An energy consumer is assigned to a power cut zone
        @param EnergyConsumerPhases:
        """
        #: Fixed reactive power as per cent of load group fixed reactive power. Load sign convention is used, i.e. positive sign means flow out from a node.
        self.qfixedPct = qfixedPct

        #: Number of individual customers represented by this Demand
        self.customerCount = customerCount

        #: Fixed active power as per cent of load group fixed active power. Load sign convention is used, i.e. positive sign means flow out from a node.
        self.pfixedPct = pfixedPct

        #: Active power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node.
        self.pfixed = pfixed

        #: Reactive power of the load that is a fixed quantity. Load sign convention is used, i.e. positive sign means flow out from a node.
        self.qfixed = qfixed

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._LoadResponse = None
        self.LoadResponse = LoadResponse

        self._PowerCutZone = None
        self.PowerCutZone = PowerCutZone

        self._EnergyConsumerPhases = []
        self.EnergyConsumerPhases = [] if EnergyConsumerPhases is None else EnergyConsumerPhases

        super(EnergyConsumer, self).__init__(*args, **kw_args)

    _attrs = ["qfixedPct", "customerCount", "pfixedPct", "pfixed", "qfixed"]
    _attr_types = {"qfixedPct": float, "customerCount": int, "pfixedPct": float, "pfixed": float, "qfixed": float}
    _defaults = {"qfixedPct": 0.0, "customerCount": 0, "pfixedPct": 0.0, "pfixed": 0.0, "qfixed": 0.0}
    _enums = {}
    _refs = ["ServiceDeliveryPoints", "LoadResponse", "PowerCutZone", "EnergyConsumerPhases"]
    _many_refs = ["ServiceDeliveryPoints", "EnergyConsumerPhases"]

    def getServiceDeliveryPoints(self):
        
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.EnergyConsumer = None
        for y in value:
            y._EnergyConsumer = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.EnergyConsumer = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.EnergyConsumer = None

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
            if self not in self._LoadResponse._EnergyConsumer:
                self._LoadResponse._EnergyConsumer.append(self)

    LoadResponse = property(getLoadResponse, setLoadResponse)

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
            if self not in self._PowerCutZone._EnergyConsumers:
                self._PowerCutZone._EnergyConsumers.append(self)

    PowerCutZone = property(getPowerCutZone, setPowerCutZone)

    def getEnergyConsumerPhases(self):
        
        return self._EnergyConsumerPhases

    def setEnergyConsumerPhases(self, value):
        for x in self._EnergyConsumerPhases:
            x.EnergyConsumer = None
        for y in value:
            y._EnergyConsumer = self
        self._EnergyConsumerPhases = value

    EnergyConsumerPhases = property(getEnergyConsumerPhases, setEnergyConsumerPhases)

    def addEnergyConsumerPhases(self, *EnergyConsumerPhases):
        for obj in EnergyConsumerPhases:
            obj.EnergyConsumer = self

    def removeEnergyConsumerPhases(self, *EnergyConsumerPhases):
        for obj in EnergyConsumerPhases:
            obj.EnergyConsumer = None

