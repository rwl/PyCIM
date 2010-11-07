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

from CIM14.IEC61970.Core.Curve import Curve

class CTTempActivePowerCurve(Curve):
    """Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)
    """

    def __init__(self, CombustionTurbine=None, **kw_args):
        """Initializes a new 'CTTempActivePowerCurve' instance.

        @param CombustionTurbine: A combustion turbine may have an active power versus ambient temperature relationship
        """
        self._CombustionTurbine = None
        self.CombustionTurbine = CombustionTurbine

        super(CTTempActivePowerCurve, self).__init__(**kw_args)

    def getCombustionTurbine(self):
        """A combustion turbine may have an active power versus ambient temperature relationship
        """
        return self._CombustionTurbine

    def setCombustionTurbine(self, value):
        if self._CombustionTurbine is not None:
            self._CombustionTurbine._CTTempActivePowerCurve = None

        self._CombustionTurbine = value
        if self._CombustionTurbine is not None:
            self._CombustionTurbine._CTTempActivePowerCurve = self

    CombustionTurbine = property(getCombustionTurbine, setCombustionTurbine)

