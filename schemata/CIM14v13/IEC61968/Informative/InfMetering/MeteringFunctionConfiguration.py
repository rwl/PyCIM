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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MeteringFunctionConfiguration(IdentifiedObject):
    """The configuration of data for a given meter function.
    """

    def __init__(self, ElectricMeteringFunctions=None, **kw_args):
        """Initializes a new 'MeteringFunctionConfiguration' instance.

        @param ElectricMeteringFunctions: All electric metering functions with this configuration.
        """
        self._ElectricMeteringFunctions = []
        self.ElectricMeteringFunctions = [] if ElectricMeteringFunctions is None else ElectricMeteringFunctions

        super(MeteringFunctionConfiguration, self).__init__(**kw_args)

    def getElectricMeteringFunctions(self):
        """All electric metering functions with this configuration.
        """
        return self._ElectricMeteringFunctions

    def setElectricMeteringFunctions(self, value):
        for x in self._ElectricMeteringFunctions:
            x._MeteringFunctionConfiguration = None
        for y in value:
            y._MeteringFunctionConfiguration = self
        self._ElectricMeteringFunctions = value

    ElectricMeteringFunctions = property(getElectricMeteringFunctions, setElectricMeteringFunctions)

    def addElectricMeteringFunctions(self, *ElectricMeteringFunctions):
        for obj in ElectricMeteringFunctions:
            obj._MeteringFunctionConfiguration = self
            self._ElectricMeteringFunctions.append(obj)

    def removeElectricMeteringFunctions(self, *ElectricMeteringFunctions):
        for obj in ElectricMeteringFunctions:
            obj._MeteringFunctionConfiguration = None
            self._ElectricMeteringFunctions.remove(obj)

