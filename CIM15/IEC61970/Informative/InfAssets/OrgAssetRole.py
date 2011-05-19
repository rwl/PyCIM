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

from CIM15.IEC61970.Informative.InfCommon.Role import Role

class OrgAssetRole(Role):
    """The roles played between an Organisations and an Asset.The roles played between an Organisations and an Asset.
    """

    def __init__(self, percentOwnership=0.0, ErpOrganisation=None, Asset=None, *args, **kw_args):
        """Initialises a new 'OrgAssetRole' instance.

        @param percentOwnership: If the role type is 'owner,' this indicate the percentage of ownership. 
        @param ErpOrganisation:
        @param Asset:
        """
        #: If the role type is 'owner,' this indicate the percentage of ownership.
        self.percentOwnership = percentOwnership

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        self._Asset = None
        self.Asset = Asset

        super(OrgAssetRole, self).__init__(*args, **kw_args)

    _attrs = ["percentOwnership"]
    _attr_types = {"percentOwnership": float}
    _defaults = {"percentOwnership": 0.0}
    _enums = {}
    _refs = ["ErpOrganisation", "Asset"]
    _many_refs = []

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.AssetRoles if x != self]
            self._ErpOrganisation._AssetRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            if self not in self._ErpOrganisation._AssetRoles:
                self._ErpOrganisation._AssetRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.ErpOrganisationRoles if x != self]
            self._Asset._ErpOrganisationRoles = filtered

        self._Asset = value
        if self._Asset is not None:
            if self not in self._Asset._ErpOrganisationRoles:
                self._Asset._ErpOrganisationRoles.append(self)

    Asset = property(getAsset, setAsset)

