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

class OrgErpPersonRole(Role):
    """Roles played between Persons and Organisations.
    """

    def __init__(self, clientID='', ErpOrganisation=None, ErpPerson=None, *args, **kw_args):
        """Initializes a new 'OrgErpPersonRole' instance.

        @param clientID: Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc. 
        @param ErpOrganisation:
        @param ErpPerson:
        """
        #: Identifiers of the person held by an organisation, such as a government agency (federal, state, province, city, county), financial institutions, etc.
        self.clientID = clientID

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        super(OrgErpPersonRole, self).__init__(*args, **kw_args)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.ErpPersonRoles if x != self]
            self._ErpOrganisation._ErpPersonRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            self._ErpOrganisation._ErpPersonRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.ErpOrganisationRoles if x != self]
            self._ErpPerson._ErpOrganisationRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._ErpOrganisationRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

