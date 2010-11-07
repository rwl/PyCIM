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

class SteamTurbine(PrimeMover):
    """Steam turbine
    """

    def __init__(self, reheater2TC=0.0, shaft1PowerIP=0.0, shaft1PowerLP2=0.0, reheater1TC=0.0, steamChestTC=0.0, crossoverTC=0.0, shaft2PowerHP=0.0, shaft2PowerLP2=0.0, shaft2PowerIP=0.0, shaft1PowerHP=0.0, shaft1PowerLP1=0.0, shaft2PowerLP1=0.0, SteamSupplys=None, **kw_args):
        """Initializes a new 'SteamTurbine' instance.

        @param reheater2TC: Second Reheater Time Constant 
        @param shaft1PowerIP: Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output 
        @param shaft1PowerLP2: Fraction Of Power From Shaft 1 Second Low Pressure Turbine output 
        @param reheater1TC: First Reheater Time Constant 
        @param steamChestTC: Steam Chest Time Constant 
        @param crossoverTC: Crossover Time Constant 
        @param shaft2PowerHP: Fraction Of Power From Shaft 2 High Pressure Turbine output 
        @param shaft2PowerLP2: Fraction Of Power From Shaft 2 Second Low Pressure Turbine output 
        @param shaft2PowerIP: Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output 
        @param shaft1PowerHP: Fraction Of Power From Shaft 1 High Pressure Turbine output 
        @param shaft1PowerLP1: Fraction Of Power From Shaft 1 First Low Pressure Turbine output 
        @param shaft2PowerLP1: Fraction Of Power From Shaft 2 First Low Pressure Turbine output 
        @param SteamSupplys: Steam turbines may have steam supplied by a steam supply
        """
        #: Second Reheater Time Constant
        self.reheater2TC = reheater2TC

        #: Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
        self.shaft1PowerIP = shaft1PowerIP

        #: Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
        self.shaft1PowerLP2 = shaft1PowerLP2

        #: First Reheater Time Constant
        self.reheater1TC = reheater1TC

        #: Steam Chest Time Constant
        self.steamChestTC = steamChestTC

        #: Crossover Time Constant
        self.crossoverTC = crossoverTC

        #: Fraction Of Power From Shaft 2 High Pressure Turbine output
        self.shaft2PowerHP = shaft2PowerHP

        #: Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
        self.shaft2PowerLP2 = shaft2PowerLP2

        #: Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
        self.shaft2PowerIP = shaft2PowerIP

        #: Fraction Of Power From Shaft 1 High Pressure Turbine output
        self.shaft1PowerHP = shaft1PowerHP

        #: Fraction Of Power From Shaft 1 First Low Pressure Turbine output
        self.shaft1PowerLP1 = shaft1PowerLP1

        #: Fraction Of Power From Shaft 2 First Low Pressure Turbine output
        self.shaft2PowerLP1 = shaft2PowerLP1

        self._SteamSupplys = []
        self.SteamSupplys = [] if SteamSupplys is None else SteamSupplys

        super(SteamTurbine, self).__init__(**kw_args)

    def getSteamSupplys(self):
        """Steam turbines may have steam supplied by a steam supply
        """
        return self._SteamSupplys

    def setSteamSupplys(self, value):
        for p in self._SteamSupplys:
            filtered = [q for q in p.SteamTurbines if q != self]
            self._SteamSupplys._SteamTurbines = filtered
        for r in value:
            if self not in r._SteamTurbines:
                r._SteamTurbines.append(self)
        self._SteamSupplys = value

    SteamSupplys = property(getSteamSupplys, setSteamSupplys)

    def addSteamSupplys(self, *SteamSupplys):
        for obj in SteamSupplys:
            if self not in obj._SteamTurbines:
                obj._SteamTurbines.append(self)
            self._SteamSupplys.append(obj)

    def removeSteamSupplys(self, *SteamSupplys):
        for obj in SteamSupplys:
            if self in obj._SteamTurbines:
                obj._SteamTurbines.remove(self)
            self._SteamSupplys.remove(obj)

