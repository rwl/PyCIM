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

class NonConformLoadGroup(LoadGroup):
    """Loads that do not follow a daily and seasonal load variation pattern.
    """

    def __init__(self, EnergyConsumers=None, NonConformLoadSchedules=None, *args, **kw_args):
        """Initializes a new 'NonConformLoadGroup' instance.

        @param EnergyConsumers: Conform loads assigned to this ConformLoadGroup.
        @param NonConformLoadSchedules: The NonConformLoadSchedules in the NonConformLoadGroup.
        """
        self._EnergyConsumers = []
        self.EnergyConsumers = [] if EnergyConsumers is None else EnergyConsumers

        self._NonConformLoadSchedules = []
        self.NonConformLoadSchedules = [] if NonConformLoadSchedules is None else NonConformLoadSchedules

        super(NonConformLoadGroup, self).__init__(*args, **kw_args)

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

    def getNonConformLoadSchedules(self):
        """The NonConformLoadSchedules in the NonConformLoadGroup.
        """
        return self._NonConformLoadSchedules

    def setNonConformLoadSchedules(self, value):
        for x in self._NonConformLoadSchedules:
            x._NonConformLoadGroup = None
        for y in value:
            y._NonConformLoadGroup = self
        self._NonConformLoadSchedules = value

    NonConformLoadSchedules = property(getNonConformLoadSchedules, setNonConformLoadSchedules)

    def addNonConformLoadSchedules(self, *NonConformLoadSchedules):
        for obj in NonConformLoadSchedules:
            obj._NonConformLoadGroup = self
            self._NonConformLoadSchedules.append(obj)

    def removeNonConformLoadSchedules(self, *NonConformLoadSchedules):
        for obj in NonConformLoadSchedules:
            obj._NonConformLoadGroup = None
            self._NonConformLoadSchedules.remove(obj)

