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

class OrgLocRole(Role):
    """Roles played between Organisations and Locations, for example a service territory or school district. Note that roles dealing with use of a specific piece of property should be defined based on the relationship between OccupationsOfProperty and Location.
    """

    def __init__(self, ErpOrganisation=None, Location=None, **kw_args):
        """Initializes a new 'OrgLocRole' instance.

        @param ErpOrganisation:
        @param Location:
        """
        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        self._Location = None
        self.Location = Location

        super(OrgLocRole, self).__init__(**kw_args)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.LocationRoles if x != self]
            self._ErpOrganisation._LocationRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            self._ErpOrganisation._LocationRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.ErpOrganisationRoles if x != self]
            self._Location._ErpOrganisationRoles = filtered

        self._Location = value
        if self._Location is not None:
            self._Location._ErpOrganisationRoles.append(self)

    Location = property(getLocation, setLocation)

