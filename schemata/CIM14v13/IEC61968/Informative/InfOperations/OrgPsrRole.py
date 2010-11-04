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

class OrgPsrRole(Role):
    """Roles played between Organisations and Power System Resources.
    """

    def __init__(self, PowerSystemResource=None, ErpOrganisation=None, **kw_args):
        """Initializes a new 'OrgPsrRole' instance.

        @param PowerSystemResource:
        @param ErpOrganisation:
        """
        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        super(OrgPsrRole, self).__init__(**kw_args)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.ErpOrganisationRoles if x != self]
            self._PowerSystemResource._ErpOrganisationRoles = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._ErpOrganisationRoles.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.PowerSystemResourceRoles if x != self]
            self._ErpOrganisation._PowerSystemResourceRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            self._ErpOrganisation._PowerSystemResourceRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

