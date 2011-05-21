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

from CIM14.IEC61970.Generation.GenerationDynamics.FossilSteamSupply import FossilSteamSupply

class HeatRecoveryBoiler(FossilSteamSupply):
    """The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """

    def __init__(self, steamSupplyRating2=0.0, CombustionTurbines=None, *args, **kw_args):
        """Initialises a new 'HeatRecoveryBoiler' instance.

        @param steamSupplyRating2: The steam supply rating in kilopounds per hour, if dual pressure boiler 
        @param CombustionTurbines: A combustion turbine may have a heat recovery boiler for making steam
        """
        #: The steam supply rating in kilopounds per hour, if dual pressure boiler
        self.steamSupplyRating2 = steamSupplyRating2

        self._CombustionTurbines = []
        self.CombustionTurbines = [] if CombustionTurbines is None else CombustionTurbines

        super(HeatRecoveryBoiler, self).__init__(*args, **kw_args)

    _attrs = ["steamSupplyRating2"]
    _attr_types = {"steamSupplyRating2": float}
    _defaults = {"steamSupplyRating2": 0.0}
    _enums = {}
    _refs = ["CombustionTurbines"]
    _many_refs = ["CombustionTurbines"]

    def getCombustionTurbines(self):
        """A combustion turbine may have a heat recovery boiler for making steam
        """
        return self._CombustionTurbines

    def setCombustionTurbines(self, value):
        for x in self._CombustionTurbines:
            x.HeatRecoveryBoiler = None
        for y in value:
            y._HeatRecoveryBoiler = self
        self._CombustionTurbines = value

    CombustionTurbines = property(getCombustionTurbines, setCombustionTurbines)

    def addCombustionTurbines(self, *CombustionTurbines):
        for obj in CombustionTurbines:
            obj.HeatRecoveryBoiler = self

    def removeCombustionTurbines(self, *CombustionTurbines):
        for obj in CombustionTurbines:
            obj.HeatRecoveryBoiler = None

