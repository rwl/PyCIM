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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class SteamSupply(PowerSystemResource):
    """Steam supply for steam turbineSteam supply for steam turbine
    """

    def __init__(self, steamSupplyRating=0.0, SteamTurbines=None, *args, **kw_args):
        """Initialises a new 'SteamSupply' instance.

        @param steamSupplyRating: Rating of steam supply 
        @param SteamTurbines: Steam turbines may have steam supplied by a steam supply
        """
        #: Rating of steam supply
        self.steamSupplyRating = steamSupplyRating

        self._SteamTurbines = []
        self.SteamTurbines = [] if SteamTurbines is None else SteamTurbines

        super(SteamSupply, self).__init__(*args, **kw_args)

    _attrs = ["steamSupplyRating"]
    _attr_types = {"steamSupplyRating": float}
    _defaults = {"steamSupplyRating": 0.0}
    _enums = {}
    _refs = ["SteamTurbines"]
    _many_refs = ["SteamTurbines"]

    def getSteamTurbines(self):
        """Steam turbines may have steam supplied by a steam supply
        """
        return self._SteamTurbines

    def setSteamTurbines(self, value):
        for p in self._SteamTurbines:
            filtered = [q for q in p.SteamSupplys if q != self]
            self._SteamTurbines._SteamSupplys = filtered
        for r in value:
            if self not in r._SteamSupplys:
                r._SteamSupplys.append(self)
        self._SteamTurbines = value

    SteamTurbines = property(getSteamTurbines, setSteamTurbines)

    def addSteamTurbines(self, *SteamTurbines):
        for obj in SteamTurbines:
            if self not in obj._SteamSupplys:
                obj._SteamSupplys.append(self)
            self._SteamTurbines.append(obj)

    def removeSteamTurbines(self, *SteamTurbines):
        for obj in SteamTurbines:
            if self in obj._SteamSupplys:
                obj._SteamSupplys.remove(self)
            self._SteamTurbines.remove(obj)

