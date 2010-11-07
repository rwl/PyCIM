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

from CIM14.IEC61970.Generation.GenerationDynamics.FossilSteamSupply import FossilSteamSupply

class HeatRecoveryBoiler(FossilSteamSupply):
    """The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants
    """

    def __init__(self, steamSupplyRating2=0.0, CombustionTurbines=None, **kw_args):
        """Initializes a new 'HeatRecoveryBoiler' instance.

        @param steamSupplyRating2: The steam supply rating in kilopounds per hour, if dual pressure boiler 
        @param CombustionTurbines: A combustion turbine may have a heat recovery boiler for making steam
        """
        #: The steam supply rating in kilopounds per hour, if dual pressure boiler
        self.steamSupplyRating2 = steamSupplyRating2

        self._CombustionTurbines = []
        self.CombustionTurbines = [] if CombustionTurbines is None else CombustionTurbines

        super(HeatRecoveryBoiler, self).__init__(**kw_args)

    def getCombustionTurbines(self):
        """A combustion turbine may have a heat recovery boiler for making steam
        """
        return self._CombustionTurbines

    def setCombustionTurbines(self, value):
        for x in self._CombustionTurbines:
            x._HeatRecoveryBoiler = None
        for y in value:
            y._HeatRecoveryBoiler = self
        self._CombustionTurbines = value

    CombustionTurbines = property(getCombustionTurbines, setCombustionTurbines)

    def addCombustionTurbines(self, *CombustionTurbines):
        for obj in CombustionTurbines:
            obj._HeatRecoveryBoiler = self
            self._CombustionTurbines.append(obj)

    def removeCombustionTurbines(self, *CombustionTurbines):
        for obj in CombustionTurbines:
            obj._HeatRecoveryBoiler = None
            self._CombustionTurbines.remove(obj)

