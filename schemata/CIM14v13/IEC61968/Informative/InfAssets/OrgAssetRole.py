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

class OrgAssetRole(Role):
    """The roles played between an Organisations and an Asset.
    """

    def __init__(self, percentOwnership=0.0, Asset=None, ErpOrganisation=None, *args, **kw_args):
        """Initializes a new 'OrgAssetRole' instance.

        @param percentOwnership: If the role type is 'owner,' this indicate the percentage of ownership. 
        @param Asset:
        @param ErpOrganisation:
        """
        #: If the role type is 'owner,' this indicate the percentage of ownership.
        self.percentOwnership = percentOwnership

        self._Asset = None
        self.Asset = Asset

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        super(OrgAssetRole, self).__init__(*args, **kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.ErpOrganisationRoles if x != self]
            self._Asset._ErpOrganisationRoles = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._ErpOrganisationRoles.append(self)

    Asset = property(getAsset, setAsset)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.AssetRoles if x != self]
            self._ErpOrganisation._AssetRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            self._ErpOrganisation._AssetRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

