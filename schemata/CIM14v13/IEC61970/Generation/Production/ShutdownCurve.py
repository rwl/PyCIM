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

from CIM14v13.IEC61970.Core.Curve import Curve

class ShutdownCurve(Curve):
    """Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)
    """

    def __init__(self, shutdownDate='', shutdownCost=0.0, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'ShutdownCurve' instance.

        @param shutdownDate: The date and time of the most recent generating unit shutdown 
        @param shutdownCost: Fixed shutdown cost 
        @param ThermalGeneratingUnit: A thermal generating unit may have a shutdown curve
        """
        #: The date and time of the most recent generating unit shutdown
        self.shutdownDate = shutdownDate

        #: Fixed shutdown cost
        self.shutdownCost = shutdownCost

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(ShutdownCurve, self).__init__(*args, **kw_args)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a shutdown curve
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._ShutdownCurve = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._ShutdownCurve = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

