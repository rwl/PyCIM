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

from CIM14v13.IEC61970.Generation.GenerationDynamics.PrimeMover import PrimeMover

class HydroTurbine(PrimeMover):
    """A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """

    def __init__(self, turbineType='francis', speedRating=0.0, speedRegulation=0.0, turbineRating=0.0, transientDroopTime=0.0, minHeadMaxP=0.0, transientRegulation=0.0, gateRateLimit=0.0, maxHeadMaxP=0.0, waterStartingTime=0.0, gateUpperLimit=0.0, **kw_args):
        """Initializes a new 'HydroTurbine' instance.

        @param turbineType: Type of turbine. Values are: "francis", "kaplan", "pelton"
        @param speedRating: Rated speed in number of revolutions. 
        @param speedRegulation: Speed Regulation 
        @param turbineRating: Rated turbine active power 
        @param transientDroopTime: Transient Droop Time Constant 
        @param minHeadMaxP: Maximum efficiency active power at minimum head conditions 
        @param transientRegulation: Transient Regulation 
        @param gateRateLimit: Gate Rate Limit 
        @param maxHeadMaxP: Maximum efficiency active power at maximum head conditions 
        @param waterStartingTime: Water Starting Time 
        @param gateUpperLimit: Gate Upper Limit 
        """
        #: Type of turbine.Values are: "francis", "kaplan", "pelton"
        self.turbineType = turbineType

        #: Rated speed in number of revolutions.
        self.speedRating = speedRating

        #: Speed Regulation
        self.speedRegulation = speedRegulation

        #: Rated turbine active power
        self.turbineRating = turbineRating

        #: Transient Droop Time Constant
        self.transientDroopTime = transientDroopTime

        #: Maximum efficiency active power at minimum head conditions
        self.minHeadMaxP = minHeadMaxP

        #: Transient Regulation
        self.transientRegulation = transientRegulation

        #: Gate Rate Limit
        self.gateRateLimit = gateRateLimit

        #: Maximum efficiency active power at maximum head conditions
        self.maxHeadMaxP = maxHeadMaxP

        #: Water Starting Time
        self.waterStartingTime = waterStartingTime

        #: Gate Upper Limit
        self.gateUpperLimit = gateUpperLimit

        super(HydroTurbine, self).__init__(**kw_args)

