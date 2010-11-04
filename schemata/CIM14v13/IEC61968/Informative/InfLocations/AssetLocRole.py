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

from CIM14v13.IEC61968.Informative.InfCommon.Role import Role

class AssetLocRole(Role):
    """Roles played between Assets and Locations.
    """

    def __init__(self, Asset=None, Location=None, **kw_args):
        """Initializes a new 'AssetLocRole' instance.

        @param Asset:
        @param Location:
        """
        self._Asset = None
        self.Asset = Asset

        self._Location = None
        self.Location = Location

        super(AssetLocRole, self).__init__(**kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.LocationRoles if x != self]
            self._Asset._LocationRoles = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._LocationRoles.append(self)

    Asset = property(getAsset, setAsset)

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.AssetRoles if x != self]
            self._Location._AssetRoles = filtered

        self._Location = value
        if self._Location is not None:
            self._Location._AssetRoles.append(self)

    Location = property(getLocation, setLocation)

