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

class TailbayLossCurve(Curve):
    """Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level
    """

    def __init__(self, HydroGeneratingUnit=None, *args, **kw_args):
        """Initializes a new 'TailbayLossCurve' instance.

        @param HydroGeneratingUnit: A hydro generating unit has a tailbay loss curve
        """
        self._HydroGeneratingUnit = None
        self.HydroGeneratingUnit = HydroGeneratingUnit

        super(TailbayLossCurve, self).__init__(*args, **kw_args)

    def getHydroGeneratingUnit(self):
        """A hydro generating unit has a tailbay loss curve
        """
        return self._HydroGeneratingUnit

    def setHydroGeneratingUnit(self, value):
        if self._HydroGeneratingUnit is not None:
            filtered = [x for x in self.HydroGeneratingUnit.TailbayLossCurve if x != self]
            self._HydroGeneratingUnit._TailbayLossCurve = filtered

        self._HydroGeneratingUnit = value
        if self._HydroGeneratingUnit is not None:
            self._HydroGeneratingUnit._TailbayLossCurve.append(self)

    HydroGeneratingUnit = property(getHydroGeneratingUnit, setHydroGeneratingUnit)

