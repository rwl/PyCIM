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

class Ground(ConductingEquipment):
    """A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.
    """

    def __init__(self, WindingInsulations=None, *args, **kw_args):
        """Initializes a new 'Ground' instance.

        @param WindingInsulations:
        """
        self._WindingInsulations = []
        self.WindingInsulations = [] if WindingInsulations is None else WindingInsulations

        super(Ground, self).__init__(*args, **kw_args)

    def getWindingInsulations(self):
        
        return self._WindingInsulations

    def setWindingInsulations(self, value):
        for x in self._WindingInsulations:
            x._Ground = None
        for y in value:
            y._Ground = self
        self._WindingInsulations = value

    WindingInsulations = property(getWindingInsulations, setWindingInsulations)

    def addWindingInsulations(self, *WindingInsulations):
        for obj in WindingInsulations:
            obj._Ground = self
            self._WindingInsulations.append(obj)

    def removeWindingInsulations(self, *WindingInsulations):
        for obj in WindingInsulations:
            obj._Ground = None
            self._WindingInsulations.remove(obj)

