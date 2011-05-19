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

from CIM15.IEC61970.Generation.GenerationDynamics.PrimeMover import PrimeMover

class HydroTurbine(PrimeMover):
    """A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.
    """

    def __init__(self, maxHeadMaxP=0.0, minHeadMaxP=0.0, turbineRating=0.0, gateRateLimit=0.0, turbineType="pelton", gateUpperLimit=0.0, speedRating=0.0, speedRegulation=0.0, transientDroopTime=0.0, transientRegulation=0.0, waterStartingTime=0.0, *args, **kw_args):
        """Initialises a new 'HydroTurbine' instance.

        @param maxHeadMaxP: Maximum efficiency active power at maximum head conditions 
        @param minHeadMaxP: Maximum efficiency active power at minimum head conditions 
        @param turbineRating: Rated turbine active power 
        @param gateRateLimit: Gate Rate Limit 
        @param turbineType: Type of turbine. Values are: "pelton", "kaplan", "francis"
        @param gateUpperLimit: Gate Upper Limit 
        @param speedRating: Rated speed in number of revolutions. 
        @param speedRegulation: Speed Regulation 
        @param transientDroopTime: Transient Droop Time Constant 
        @param transientRegulation: Transient Regulation 
        @param waterStartingTime: Water Starting Time 
        """
        #: Maximum efficiency active power at maximum head conditions
        self.maxHeadMaxP = maxHeadMaxP

        #: Maximum efficiency active power at minimum head conditions
        self.minHeadMaxP = minHeadMaxP

        #: Rated turbine active power
        self.turbineRating = turbineRating

        #: Gate Rate Limit
        self.gateRateLimit = gateRateLimit

        #: Type of turbine. Values are: "pelton", "kaplan", "francis"
        self.turbineType = turbineType

        #: Gate Upper Limit
        self.gateUpperLimit = gateUpperLimit

        #: Rated speed in number of revolutions.
        self.speedRating = speedRating

        #: Speed Regulation
        self.speedRegulation = speedRegulation

        #: Transient Droop Time Constant
        self.transientDroopTime = transientDroopTime

        #: Transient Regulation
        self.transientRegulation = transientRegulation

        #: Water Starting Time
        self.waterStartingTime = waterStartingTime

        super(HydroTurbine, self).__init__(*args, **kw_args)

    _attrs = ["maxHeadMaxP", "minHeadMaxP", "turbineRating", "gateRateLimit", "turbineType", "gateUpperLimit", "speedRating", "speedRegulation", "transientDroopTime", "transientRegulation", "waterStartingTime"]
    _attr_types = {"maxHeadMaxP": float, "minHeadMaxP": float, "turbineRating": float, "gateRateLimit": float, "turbineType": str, "gateUpperLimit": float, "speedRating": float, "speedRegulation": float, "transientDroopTime": float, "transientRegulation": float, "waterStartingTime": float}
    _defaults = {"maxHeadMaxP": 0.0, "minHeadMaxP": 0.0, "turbineRating": 0.0, "gateRateLimit": 0.0, "turbineType": "pelton", "gateUpperLimit": 0.0, "speedRating": 0.0, "speedRegulation": 0.0, "transientDroopTime": 0.0, "transientRegulation": 0.0, "waterStartingTime": 0.0}
    _enums = {"turbineType": "TurbineType"}
    _refs = []
    _many_refs = []

