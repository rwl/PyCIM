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

from CIM14v13.IEC61968.Informative.EnergyScheduling.EnergyTransaction import EnergyTransaction

class Reserve(EnergyTransaction):

    def __init__(self, AreaReserveSpec=None, *args, **kw_args):
        """Initializes a new 'Reserve' instance.

        @param AreaReserveSpec: A Reserve type of energy transaction can count towards an area reserve specification.
        """
        self._AreaReserveSpec = []
        self.AreaReserveSpec = [] if AreaReserveSpec is None else AreaReserveSpec

        super(Reserve, self).__init__(*args, **kw_args)

    def getAreaReserveSpec(self):
        """A Reserve type of energy transaction can count towards an area reserve specification.
        """
        return self._AreaReserveSpec

    def setAreaReserveSpec(self, value):
        for x in self._AreaReserveSpec:
            x._ReserveEnergyTransaction = None
        for y in value:
            y._ReserveEnergyTransaction = self
        self._AreaReserveSpec = value

    AreaReserveSpec = property(getAreaReserveSpec, setAreaReserveSpec)

    def addAreaReserveSpec(self, *AreaReserveSpec):
        for obj in AreaReserveSpec:
            obj._ReserveEnergyTransaction = self
            self._AreaReserveSpec.append(obj)

    def removeAreaReserveSpec(self, *AreaReserveSpec):
        for obj in AreaReserveSpec:
            obj._ReserveEnergyTransaction = None
            self._AreaReserveSpec.remove(obj)

