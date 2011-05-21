# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

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

