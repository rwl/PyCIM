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

from CIM14.IEC61970.Generation.GenerationDynamics.PrimeMover import PrimeMover

class HydroTurbine(PrimeMover):
    """A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """

    def __init__(self, turbineType="francis", turbineRating=0.0, maxHeadMaxP=0.0, transientDroopTime=0.0, speedRegulation=0.0, waterStartingTime=0.0, speedRating=0.0, transientRegulation=0.0, gateUpperLimit=0.0, minHeadMaxP=0.0, gateRateLimit=0.0, HydroTurbineGovernor=None, *args, **kw_args):
        """Initialises a new 'HydroTurbine' instance.

        @param turbineType: Type of turbine. Values are: "francis", "pelton", "kaplan"
        @param turbineRating: Rated turbine active power 
        @param maxHeadMaxP: Maximum efficiency active power at maximum head conditions 
        @param transientDroopTime: Transient Droop Time Constant 
        @param speedRegulation: Speed Regulation 
        @param waterStartingTime: Water Starting Time 
        @param speedRating: Rated speed in number of revolutions. 
        @param transientRegulation: Transient Regulation 
        @param gateUpperLimit: Gate Upper Limit 
        @param minHeadMaxP: Maximum efficiency active power at minimum head conditions 
        @param gateRateLimit: Gate Rate Limit 
        @param HydroTurbineGovernor:
        """
        #: Type of turbine. Values are: "francis", "pelton", "kaplan"
        self.turbineType = turbineType

        #: Rated turbine active power
        self.turbineRating = turbineRating

        #: Maximum efficiency active power at maximum head conditions
        self.maxHeadMaxP = maxHeadMaxP

        #: Transient Droop Time Constant
        self.transientDroopTime = transientDroopTime

        #: Speed Regulation
        self.speedRegulation = speedRegulation

        #: Water Starting Time
        self.waterStartingTime = waterStartingTime

        #: Rated speed in number of revolutions.
        self.speedRating = speedRating

        #: Transient Regulation
        self.transientRegulation = transientRegulation

        #: Gate Upper Limit
        self.gateUpperLimit = gateUpperLimit

        #: Maximum efficiency active power at minimum head conditions
        self.minHeadMaxP = minHeadMaxP

        #: Gate Rate Limit
        self.gateRateLimit = gateRateLimit

        self._HydroTurbineGovernor = None
        self.HydroTurbineGovernor = HydroTurbineGovernor

        super(HydroTurbine, self).__init__(*args, **kw_args)

    _attrs = ["turbineType", "turbineRating", "maxHeadMaxP", "transientDroopTime", "speedRegulation", "waterStartingTime", "speedRating", "transientRegulation", "gateUpperLimit", "minHeadMaxP", "gateRateLimit"]
    _attr_types = {"turbineType": str, "turbineRating": float, "maxHeadMaxP": float, "transientDroopTime": float, "speedRegulation": float, "waterStartingTime": float, "speedRating": float, "transientRegulation": float, "gateUpperLimit": float, "minHeadMaxP": float, "gateRateLimit": float}
    _defaults = {"turbineType": "francis", "turbineRating": 0.0, "maxHeadMaxP": 0.0, "transientDroopTime": 0.0, "speedRegulation": 0.0, "waterStartingTime": 0.0, "speedRating": 0.0, "transientRegulation": 0.0, "gateUpperLimit": 0.0, "minHeadMaxP": 0.0, "gateRateLimit": 0.0}
    _enums = {"turbineType": "TurbineType"}
    _refs = ["HydroTurbineGovernor"]
    _many_refs = []

    def getHydroTurbineGovernor(self):
        
        return self._HydroTurbineGovernor

    def setHydroTurbineGovernor(self, value):
        if self._HydroTurbineGovernor is not None:
            self._HydroTurbineGovernor._HydroTurbine = None

        self._HydroTurbineGovernor = value
        if self._HydroTurbineGovernor is not None:
            self._HydroTurbineGovernor.HydroTurbine = None
            self._HydroTurbineGovernor._HydroTurbine = self

    HydroTurbineGovernor = property(getHydroTurbineGovernor, setHydroTurbineGovernor)

