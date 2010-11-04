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

class AssetPsrRole(Role):
    """Roles played between Assets and Power System Resources.
    """

    def __init__(self, PowerSystemResource=None, Asset=None, **kw_args):
        """Initializes a new 'AssetPsrRole' instance.

        @param PowerSystemResource:
        @param Asset:
        """
        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._Asset = None
        self.Asset = Asset

        super(AssetPsrRole, self).__init__(**kw_args)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.AssetRoles if x != self]
            self._PowerSystemResource._AssetRoles = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._AssetRoles.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.PowerSystemResourceRoles if x != self]
            self._Asset._PowerSystemResourceRoles = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._PowerSystemResourceRoles.append(self)

    Asset = property(getAsset, setAsset)

