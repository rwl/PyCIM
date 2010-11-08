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

from CIM14.IEC61970.Core.EquipmentContainer import EquipmentContainer

class Substation(EquipmentContainer):
    """A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.
    """

    def __init__(self, VoltageLevels=None, Bays=None, Region=None, *args, **kw_args):
        """Initialises a new 'Substation' instance.

        @param VoltageLevels: The association is used in the naming hierarchy.
        @param Bays: The association is used in the naming hierarchy.
        @param Region: The association is used in the naming hierarchy.
        """
        self._VoltageLevels = []
        self.VoltageLevels = [] if VoltageLevels is None else VoltageLevels

        self._Bays = []
        self.Bays = [] if Bays is None else Bays

        self._Region = None
        self.Region = Region

        super(Substation, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["VoltageLevels", "Bays", "Region"]
    _many_refs = ["VoltageLevels", "Bays"]

    def getVoltageLevels(self):
        """The association is used in the naming hierarchy.
        """
        return self._VoltageLevels

    def setVoltageLevels(self, value):
        for x in self._VoltageLevels:
            x._Substation = None
        for y in value:
            y._Substation = self
        self._VoltageLevels = value

    VoltageLevels = property(getVoltageLevels, setVoltageLevels)

    def addVoltageLevels(self, *VoltageLevels):
        for obj in VoltageLevels:
            obj._Substation = self
            self._VoltageLevels.append(obj)

    def removeVoltageLevels(self, *VoltageLevels):
        for obj in VoltageLevels:
            obj._Substation = None
            self._VoltageLevels.remove(obj)

    def getBays(self):
        """The association is used in the naming hierarchy.
        """
        return self._Bays

    def setBays(self, value):
        for x in self._Bays:
            x._Substation = None
        for y in value:
            y._Substation = self
        self._Bays = value

    Bays = property(getBays, setBays)

    def addBays(self, *Bays):
        for obj in Bays:
            obj._Substation = self
            self._Bays.append(obj)

    def removeBays(self, *Bays):
        for obj in Bays:
            obj._Substation = None
            self._Bays.remove(obj)

    def getRegion(self):
        """The association is used in the naming hierarchy.
        """
        return self._Region

    def setRegion(self, value):
        if self._Region is not None:
            filtered = [x for x in self.Region.Substations if x != self]
            self._Region._Substations = filtered

        self._Region = value
        if self._Region is not None:
            self._Region._Substations.append(self)

    Region = property(getRegion, setRegion)

