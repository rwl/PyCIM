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

class HydroGeneratingEfficiencyCurve(Curve):
    """Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.
    """

    def __init__(self, HydroGeneratingUnit=None, **kw_args):
        """Initializes a new 'HydroGeneratingEfficiencyCurve' instance.

        @param HydroGeneratingUnit: A hydro generating unit has an efficiency curve
        """
        self._HydroGeneratingUnit = None
        self.HydroGeneratingUnit = HydroGeneratingUnit

        super(HydroGeneratingEfficiencyCurve, self).__init__(**kw_args)

    def getHydroGeneratingUnit(self):
        """A hydro generating unit has an efficiency curve
        """
        return self._HydroGeneratingUnit

    def setHydroGeneratingUnit(self, value):
        if self._HydroGeneratingUnit is not None:
            filtered = [x for x in self.HydroGeneratingUnit.HydroGeneratingEfficiencyCurves if x != self]
            self._HydroGeneratingUnit._HydroGeneratingEfficiencyCurves = filtered

        self._HydroGeneratingUnit = value
        if self._HydroGeneratingUnit is not None:
            self._HydroGeneratingUnit._HydroGeneratingEfficiencyCurves.append(self)

    HydroGeneratingUnit = property(getHydroGeneratingUnit, setHydroGeneratingUnit)

