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

from CIM14v13.IEC61970.LoadModel.LoadGroup import LoadGroup

class ConformLoadGroup(LoadGroup):
    """A group of loads conforming to an allocation pattern.
    """

    def __init__(self, ConformLoadSchedules=None, EnergyConsumers=None, *args, **kw_args):
        """Initializes a new 'ConformLoadGroup' instance.

        @param ConformLoadSchedules: The ConformLoadSchedules in the ConformLoadGroup.
        @param EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
        """
        self._ConformLoadSchedules = []
        self.ConformLoadSchedules = [] if ConformLoadSchedules is None else ConformLoadSchedules

        self._EnergyConsumers = []
        self.EnergyConsumers = [] if EnergyConsumers is None else EnergyConsumers

        super(ConformLoadGroup, self).__init__(*args, **kw_args)

    def getConformLoadSchedules(self):
        """The ConformLoadSchedules in the ConformLoadGroup.
        """
        return self._ConformLoadSchedules

    def setConformLoadSchedules(self, value):
        for x in self._ConformLoadSchedules:
            x._ConformLoadGroup = None
        for y in value:
            y._ConformLoadGroup = self
        self._ConformLoadSchedules = value

    ConformLoadSchedules = property(getConformLoadSchedules, setConformLoadSchedules)

    def addConformLoadSchedules(self, *ConformLoadSchedules):
        for obj in ConformLoadSchedules:
            obj._ConformLoadGroup = self
            self._ConformLoadSchedules.append(obj)

    def removeConformLoadSchedules(self, *ConformLoadSchedules):
        for obj in ConformLoadSchedules:
            obj._ConformLoadGroup = None
            self._ConformLoadSchedules.remove(obj)

    def getEnergyConsumers(self):
        """Conform loads assigned to this ConformLoadGroup.
        """
        return self._EnergyConsumers

    def setEnergyConsumers(self, value):
        for x in self._EnergyConsumers:
            x._LoadGroup = None
        for y in value:
            y._LoadGroup = self
        self._EnergyConsumers = value

    EnergyConsumers = property(getEnergyConsumers, setEnergyConsumers)

    def addEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj._LoadGroup = self
            self._EnergyConsumers.append(obj)

    def removeEnergyConsumers(self, *EnergyConsumers):
        for obj in EnergyConsumers:
            obj._LoadGroup = None
            self._EnergyConsumers.remove(obj)

