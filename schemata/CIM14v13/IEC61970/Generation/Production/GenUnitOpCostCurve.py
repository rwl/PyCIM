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

class GenUnitOpCostCurve(Curve):
    """Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.
    """

    def __init__(self, isNetGrossP=False, GeneratingUnit=None, **kw_args):
        """Initializes a new 'GenUnitOpCostCurve' instance.

        @param isNetGrossP: Flag is set to true when output is expressed in net active power 
        @param GeneratingUnit: A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        #: Flag is set to true when output is expressed in net active power
        self.isNetGrossP = isNetGrossP

        self._GeneratingUnit = None
        self.GeneratingUnit = GeneratingUnit

        super(GenUnitOpCostCurve, self).__init__(**kw_args)

    def getGeneratingUnit(self):
        """A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.
        """
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        if self._GeneratingUnit is not None:
            filtered = [x for x in self.GeneratingUnit.GenUnitOpCostCurves if x != self]
            self._GeneratingUnit._GenUnitOpCostCurves = filtered

        self._GeneratingUnit = value
        if self._GeneratingUnit is not None:
            self._GeneratingUnit._GenUnitOpCostCurves.append(self)

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

