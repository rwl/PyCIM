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

class StartIgnFuelCurve(Curve):
    """The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line
    """

    def __init__(self, ignitionFuelType="lignite", StartupModel=None, *args, **kw_args):
        """Initialises a new 'StartIgnFuelCurve' instance.

        @param ignitionFuelType: Type of ignition fuel Values are: "lignite", "coal", "oil", "gas"
        @param StartupModel: The unit's startup model may have a startup ignition fuel curve
        """
        #: Type of ignition fuel Values are: "lignite", "coal", "oil", "gas"
        self.ignitionFuelType = ignitionFuelType

        self._StartupModel = None
        self.StartupModel = StartupModel

        super(StartIgnFuelCurve, self).__init__(*args, **kw_args)

    _attrs = ["ignitionFuelType"]
    _attr_types = {"ignitionFuelType": str}
    _defaults = {"ignitionFuelType": "lignite"}
    _enums = {"ignitionFuelType": "FuelType"}
    _refs = ["StartupModel"]
    _many_refs = []

    def getStartupModel(self):
        """The unit's startup model may have a startup ignition fuel curve
        """
        return self._StartupModel

    def setStartupModel(self, value):
        if self._StartupModel is not None:
            self._StartupModel._StartIgnFuelCurve = None

        self._StartupModel = value
        if self._StartupModel is not None:
            self._StartupModel.StartIgnFuelCurve = None
            self._StartupModel._StartIgnFuelCurve = self

    StartupModel = property(getStartupModel, setStartupModel)

