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

from CIM14.IEC61970.Wires.EnergyConsumer import EnergyConsumer

class ConformLoad(EnergyConsumer):
    """ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.
    """

    def __init__(self, LoadGroup=None, *args, **kw_args):
        """Initialises a new 'ConformLoad' instance.

        @param LoadGroup: Group of this ConformLoad.
        """
        self._LoadGroup = None
        self.LoadGroup = LoadGroup

        super(ConformLoad, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["LoadGroup"]
    _many_refs = []

    def getLoadGroup(self):
        """Group of this ConformLoad.
        """
        return self._LoadGroup

    def setLoadGroup(self, value):
        if self._LoadGroup is not None:
            filtered = [x for x in self.LoadGroup.EnergyConsumers if x != self]
            self._LoadGroup._EnergyConsumers = filtered

        self._LoadGroup = value
        if self._LoadGroup is not None:
            if self not in self._LoadGroup._EnergyConsumers:
                self._LoadGroup._EnergyConsumers.append(self)

    LoadGroup = property(getLoadGroup, setLoadGroup)

