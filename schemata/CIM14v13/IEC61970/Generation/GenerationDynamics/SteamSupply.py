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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class SteamSupply(PowerSystemResource):
    """Steam supply for steam turbine
    """

    def __init__(self, steamSupplyRating=0.0, SteamTurbines=None, *args, **kw_args):
        """Initializes a new 'SteamSupply' instance.

        @param steamSupplyRating: Rating of steam supply 
        @param SteamTurbines: Steam turbines may have steam supplied by a steam supply
        """
        #: Rating of steam supply
        self.steamSupplyRating = steamSupplyRating

        self._SteamTurbines = []
        self.SteamTurbines = [] if SteamTurbines is None else SteamTurbines

        super(SteamSupply, self).__init__(*args, **kw_args)

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

