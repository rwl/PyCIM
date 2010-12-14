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

class PenstockLossCurve(Curve):
    """Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.
    """

    def __init__(self, HydroGeneratingUnit=None, *args, **kw_args):
        """Initialises a new 'PenstockLossCurve' instance.

        @param HydroGeneratingUnit: A hydro generating unit has a penstock loss curve
        """
        self._HydroGeneratingUnit = None
        self.HydroGeneratingUnit = HydroGeneratingUnit

        super(PenstockLossCurve, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["HydroGeneratingUnit"]
    _many_refs = []

    def getHydroGeneratingUnit(self):
        """A hydro generating unit has a penstock loss curve
        """
        return self._HydroGeneratingUnit

    def setHydroGeneratingUnit(self, value):
        if self._HydroGeneratingUnit is not None:
            self._HydroGeneratingUnit._PenstockLossCurve = None

        self._HydroGeneratingUnit = value
        if self._HydroGeneratingUnit is not None:
            self._HydroGeneratingUnit.PenstockLossCurve = None
            self._HydroGeneratingUnit._PenstockLossCurve = self

    HydroGeneratingUnit = property(getHydroGeneratingUnit, setHydroGeneratingUnit)

