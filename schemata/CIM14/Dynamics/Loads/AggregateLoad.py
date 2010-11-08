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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class AggregateLoad(PowerSystemResource):
    """Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.
    """

    def __init__(self, energyConsumer0=None, *args, **kw_args):
        """Initialises a new 'AggregateLoad' instance.

        @param energyConsumer0:
        """
        self._energyConsumer0 = []
        self.energyConsumer0 = [] if energyConsumer0 is None else energyConsumer0

        super(AggregateLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["energyConsumer0"]
    _many_refs = ["energyConsumer0"]

    def getenergyConsumer0(self):
        
        return self._energyConsumer0

    def setenergyConsumer0(self, value):
        for p in self._energyConsumer0:
            filtered = [q for q in p.aggregateLoad0 if q != self]
            self._energyConsumer0._aggregateLoad0 = filtered
        for r in value:
            if self not in r._aggregateLoad0:
                r._aggregateLoad0.append(self)
        self._energyConsumer0 = value

    energyConsumer0 = property(getenergyConsumer0, setenergyConsumer0)

    def addenergyConsumer0(self, *energyConsumer0):
        for obj in energyConsumer0:
            if self not in obj._aggregateLoad0:
                obj._aggregateLoad0.append(self)
            self._energyConsumer0.append(obj)

    def removeenergyConsumer0(self, *energyConsumer0):
        for obj in energyConsumer0:
            if self in obj._aggregateLoad0:
                obj._aggregateLoad0.remove(self)
            self._energyConsumer0.remove(obj)

