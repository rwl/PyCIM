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

class AssetAssetRole(Role):
    """Roles played between Assets and other Assets.
    """

    def __init__(self, ToAsset=None, FromAsset=None, *args, **kw_args):
        """Initializes a new 'AssetAssetRole' instance.

        @param ToAsset:
        @param FromAsset:
        """
        self._ToAsset = None
        self.ToAsset = ToAsset

        self._FromAsset = None
        self.FromAsset = FromAsset

        super(AssetAssetRole, self).__init__(*args, **kw_args)

    def getToAsset(self):
        
        return self._ToAsset

    def setToAsset(self, value):
        if self._ToAsset is not None:
            filtered = [x for x in self.ToAsset.FromAssetRoles if x != self]
            self._ToAsset._FromAssetRoles = filtered

        self._ToAsset = value
        if self._ToAsset is not None:
            self._ToAsset._FromAssetRoles.append(self)

    ToAsset = property(getToAsset, setToAsset)

    def getFromAsset(self):
        
        return self._FromAsset

    def setFromAsset(self, value):
        if self._FromAsset is not None:
            filtered = [x for x in self.FromAsset.ToAssetRoles if x != self]
            self._FromAsset._ToAssetRoles = filtered

        self._FromAsset = value
        if self._FromAsset is not None:
            self._FromAsset._ToAssetRoles.append(self)

    FromAsset = property(getFromAsset, setFromAsset)

