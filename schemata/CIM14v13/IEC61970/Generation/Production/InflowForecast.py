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

from CIM14v13.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class InflowForecast(RegularIntervalSchedule):
    """Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.
    """

    def __init__(self, Reservoir=None, *args, **kw_args):
        """Initializes a new 'InflowForecast' instance.

        @param Reservoir: A reservoir may have a 'natural' inflow forecast.
        """
        self._Reservoir = None
        self.Reservoir = Reservoir

        super(InflowForecast, self).__init__(*args, **kw_args)

    def getReservoir(self):
        """A reservoir may have a 'natural' inflow forecast.
        """
        return self._Reservoir

    def setReservoir(self, value):
        if self._Reservoir is not None:
            filtered = [x for x in self.Reservoir.InflowForecasts if x != self]
            self._Reservoir._InflowForecasts = filtered

        self._Reservoir = value
        if self._Reservoir is not None:
            self._Reservoir._InflowForecasts.append(self)

    Reservoir = property(getReservoir, setReservoir)

