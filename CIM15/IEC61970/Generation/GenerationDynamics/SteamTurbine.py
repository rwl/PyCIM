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

class SteamTurbine(PrimeMover):
    """Steam turbineSteam turbine
    """

    def __init__(self, shaft1PowerIP=0.0, shaft2PowerIP=0.0, crossoverTC=0.0, shaft1PowerLP1=0.0, shaft1PowerLP2=0.0, reheater1TC=0.0, shaft2PowerLP1=0.0, shaft2PowerLP2=0.0, reheater2TC=0.0, steamChestTC=0.0, shaft1PowerHP=0.0, shaft2PowerHP=0.0, SteamSupplys=None, *args, **kw_args):
        """Initialises a new 'SteamTurbine' instance.

        @param shaft1PowerIP: Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output 
        @param shaft2PowerIP: Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output 
        @param crossoverTC: Crossover Time Constant 
        @param shaft1PowerLP1: Fraction Of Power From Shaft 1 First Low Pressure Turbine output 
        @param shaft1PowerLP2: Fraction Of Power From Shaft 1 Second Low Pressure Turbine output 
        @param reheater1TC: First Reheater Time Constant 
        @param shaft2PowerLP1: Fraction Of Power From Shaft 2 First Low Pressure Turbine output 
        @param shaft2PowerLP2: Fraction Of Power From Shaft 2 Second Low Pressure Turbine output 
        @param reheater2TC: Second Reheater Time Constant 
        @param steamChestTC: Steam Chest Time Constant 
        @param shaft1PowerHP: Fraction Of Power From Shaft 1 High Pressure Turbine output 
        @param shaft2PowerHP: Fraction Of Power From Shaft 2 High Pressure Turbine output 
        @param SteamSupplys: Steam turbines may have steam supplied by a steam supply
        """
        #: Fraction Of Power From Shaft 1 Intermediate Pressure Turbine output
        self.shaft1PowerIP = shaft1PowerIP

        #: Fraction Of Power From Shaft 2 Intermediate Pressure Turbine output
        self.shaft2PowerIP = shaft2PowerIP

        #: Crossover Time Constant
        self.crossoverTC = crossoverTC

        #: Fraction Of Power From Shaft 1 First Low Pressure Turbine output
        self.shaft1PowerLP1 = shaft1PowerLP1

        #: Fraction Of Power From Shaft 1 Second Low Pressure Turbine output
        self.shaft1PowerLP2 = shaft1PowerLP2

        #: First Reheater Time Constant
        self.reheater1TC = reheater1TC

        #: Fraction Of Power From Shaft 2 First Low Pressure Turbine output
        self.shaft2PowerLP1 = shaft2PowerLP1

        #: Fraction Of Power From Shaft 2 Second Low Pressure Turbine output
        self.shaft2PowerLP2 = shaft2PowerLP2

        #: Second Reheater Time Constant
        self.reheater2TC = reheater2TC

        #: Steam Chest Time Constant
        self.steamChestTC = steamChestTC

        #: Fraction Of Power From Shaft 1 High Pressure Turbine output
        self.shaft1PowerHP = shaft1PowerHP

        #: Fraction Of Power From Shaft 2 High Pressure Turbine output
        self.shaft2PowerHP = shaft2PowerHP

        self._SteamSupplys = []
        self.SteamSupplys = [] if SteamSupplys is None else SteamSupplys

        super(SteamTurbine, self).__init__(*args, **kw_args)

    _attrs = ["shaft1PowerIP", "shaft2PowerIP", "crossoverTC", "shaft1PowerLP1", "shaft1PowerLP2", "reheater1TC", "shaft2PowerLP1", "shaft2PowerLP2", "reheater2TC", "steamChestTC", "shaft1PowerHP", "shaft2PowerHP"]
    _attr_types = {"shaft1PowerIP": float, "shaft2PowerIP": float, "crossoverTC": float, "shaft1PowerLP1": float, "shaft1PowerLP2": float, "reheater1TC": float, "shaft2PowerLP1": float, "shaft2PowerLP2": float, "reheater2TC": float, "steamChestTC": float, "shaft1PowerHP": float, "shaft2PowerHP": float}
    _defaults = {"shaft1PowerIP": 0.0, "shaft2PowerIP": 0.0, "crossoverTC": 0.0, "shaft1PowerLP1": 0.0, "shaft1PowerLP2": 0.0, "reheater1TC": 0.0, "shaft2PowerLP1": 0.0, "shaft2PowerLP2": 0.0, "reheater2TC": 0.0, "steamChestTC": 0.0, "shaft1PowerHP": 0.0, "shaft2PowerHP": 0.0}
    _enums = {}
    _refs = ["SteamSupplys"]
    _many_refs = ["SteamSupplys"]

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

