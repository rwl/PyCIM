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

class OrgOrgRole(Role):
    """Roles played between Organisations and other Organisations. This includes role ups for ogranisations, cost centers, profit centers, regulatory reporting, etc. Note that the parent and child relationship is indicated by the name on each end of the association.
    """

    def __init__(self, clientID='', ChildOrganisation=None, ParentOrganisation=None, *args, **kw_args):
        """Initializes a new 'OrgOrgRole' instance.

        @param clientID: Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc. 
        @param ChildOrganisation:
        @param ParentOrganisation:
        """
        #: Identifiers of the organisation held by another organisation, such as a government agency (federal, state, province, city, county), financial institution (Dun and Bradstreet), etc. 
        self.clientID = clientID

        self._ChildOrganisation = None
        self.ChildOrganisation = ChildOrganisation

        self._ParentOrganisation = None
        self.ParentOrganisation = ParentOrganisation

        super(OrgOrgRole, self).__init__(*args, **kw_args)

    def getChildOrganisation(self):
        
        return self._ChildOrganisation

    def setChildOrganisation(self, value):
        if self._ChildOrganisation is not None:
            filtered = [x for x in self.ChildOrganisation.ParentOrganisationRoles if x != self]
            self._ChildOrganisation._ParentOrganisationRoles = filtered

        self._ChildOrganisation = value
        if self._ChildOrganisation is not None:
            self._ChildOrganisation._ParentOrganisationRoles.append(self)

    ChildOrganisation = property(getChildOrganisation, setChildOrganisation)

    def getParentOrganisation(self):
        
        return self._ParentOrganisation

    def setParentOrganisation(self, value):
        if self._ParentOrganisation is not None:
            filtered = [x for x in self.ParentOrganisation.ChildOrganisationRoles if x != self]
            self._ParentOrganisation._ChildOrganisationRoles = filtered

        self._ParentOrganisation = value
        if self._ParentOrganisation is not None:
            self._ParentOrganisation._ChildOrganisationRoles.append(self)

    ParentOrganisation = property(getParentOrganisation, setParentOrganisation)

