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

class IncrementalHeatRateCurve(Curve):
    """Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.
    """

    def __init__(self, isNetGrossP=False, ThermalGeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'IncrementalHeatRateCurve' instance.

        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param ThermalGeneratingUnit: A thermal generating unit may have an incremental heat rate curve
        """
        #: Flag is set to true when output is expressed in net active power
        self.isNetGrossP = isNetGrossP

        self._ThermalGeneratingUnit = None
        self.ThermalGeneratingUnit = ThermalGeneratingUnit

        super(IncrementalHeatRateCurve, self).__init__(*args, **kw_args)

    def getThermalGeneratingUnit(self):
        """A thermal generating unit may have an incremental heat rate curve
        """
        return self._ThermalGeneratingUnit

    def setThermalGeneratingUnit(self, value):
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._IncrementalHeatRateCurve = None

        self._ThermalGeneratingUnit = value
        if self._ThermalGeneratingUnit is not None:
            self._ThermalGeneratingUnit._IncrementalHeatRateCurve = self

    ThermalGeneratingUnit = property(getThermalGeneratingUnit, setThermalGeneratingUnit)

