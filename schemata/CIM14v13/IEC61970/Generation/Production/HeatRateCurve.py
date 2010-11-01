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

class HeatRateCurve(Curve):
    """Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.
    """

    def __init__(self, isNetGrossP=False, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'HeatRateCurve' instance.

        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param ThermalGeneratingUnit: A thermal generating unit may have a heat rate curve
        """
        #: Flag is set to true when output is expressed in net active power 
        self.isNetGrossP = isNetGrossP

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(HeatRateCurve, self).__init__(*args, **kw_args)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have a heat rate curve
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._HeatRateCurve = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._HeatRateCurve = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

