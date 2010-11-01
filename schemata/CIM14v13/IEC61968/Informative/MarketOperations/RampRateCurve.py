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

class RampRateCurve(Curve):
    """Ramp rate as a function of resource MW output
    """

    def __init__(self, rampRateType='', GeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'RampRateCurve' instance.

        @param rampRateType: How ramp rate is applied (e.g., raise or lower, as when applied to a generation resource) 
        @param GeneratingUnit:
        """
        #: How ramp rate is applied (e.g., raise or lower, as when applied to a generation resource) 
        self.rampRateType = rampRateType

        self._GeneratingUnit = []
        self.GeneratingUnit = [] if GeneratingUnit is None else GeneratingUnit

        super(RampRateCurve, self).__init__(*args, **kw_args)

    def getGeneratingUnit(self):
        
        return self._GeneratingUnit

    def setGeneratingUnit(self, value):
        for p in self._GeneratingUnit:
            filtered = [q for q in p.RampRateCurves if q != self]
            self._GeneratingUnit._RampRateCurves = filtered
        for r in value:
            if self not in r._RampRateCurves:
                r._RampRateCurves.append(self)
        self._GeneratingUnit = value

    GeneratingUnit = property(getGeneratingUnit, setGeneratingUnit)

    def addGeneratingUnit(self, *GeneratingUnit):
        for obj in GeneratingUnit:
            if self not in obj._RampRateCurves:
                obj._RampRateCurves.append(self)
            self._GeneratingUnit.append(obj)

    def removeGeneratingUnit(self, *GeneratingUnit):
        for obj in GeneratingUnit:
            if self in obj._RampRateCurves:
                obj._RampRateCurves.remove(self)
            self._GeneratingUnit.remove(obj)

