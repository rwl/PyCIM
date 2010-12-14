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

class PowerCutZone(PowerSystemResource):
    """An area or zone of the power system which is used for load shedding purposes.
    """

    def __init__(self, cutLevel1=0.0, cutLevel2=0.0, EnergyConsumers=None, *args, **kw_args):
        """Initialises a new 'PowerCutZone' instance.

        @param cutLevel1: First level (amount) of load to cut as a percentage of total zone load 
        @param cutLevel2: Second level (amount) of load to cut as a percentage of total zone load 
        @param EnergyConsumers: An energy consumer is assigned to a power cut zone
        """
        #: First level (amount) of load to cut as a percentage of total zone load
        self.cutLevel1 = cutLevel1

        #: Second level (amount) of load to cut as a percentage of total zone load
        self.cutLevel2 = cutLevel2

        self._EnergyConsumers = []
        self.EnergyConsumers = [] if EnergyConsumers is None else EnergyConsumers

        super(PowerCutZone, self).__init__(*args, **kw_args)

    _attrs = ["cutLevel1", "cutLevel2"]
    _attr_types = {"cutLevel1": float, "cutLevel2": float}
    _defaults = {"cutLevel1": 0.0, "cutLevel2": 0.0}
    _enums = {}
    _refs = ["EnergyConsumers"]
    _many_refs = ["EnergyConsumers"]

    def getEnergyConsumers(self):
        """An energy consumer is assigned to a power cut zone
        """
        return self._EnergyConsumers

    def setEnergyConsumers(self, value):
        for x in self._EnergyConsumers:
            x.PowerCutZone = None
        for y in value:
            y._PowerCutZone = self
        self._EnergyConsumers = value

    EnergyConsumers = property(getEnergyConsumers, setEnergyConsumers)

    def addEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj.PowerCutZone = self

    def removeEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj.PowerCutZone = None

