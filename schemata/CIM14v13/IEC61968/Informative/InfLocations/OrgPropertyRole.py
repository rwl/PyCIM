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

class OrgPropertyRole(Role):
    """Roles played between Organisations and a given piece of property. For example, the Organisation may be the owner, renter, occupier, taxiing authority, etc.
    """

    def __init__(self, ErpOrganisation=None, LandProperty=None, **kw_args):
        """Initializes a new 'OrgPropertyRole' instance.

        @param ErpOrganisation:
        @param LandProperty:
        """
        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        self._LandProperty = []
        self.LandProperty = [] if LandProperty is None else LandProperty

        super(OrgPropertyRole, self).__init__(**kw_args)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.LandPropertyRoles if x != self]
            self._ErpOrganisation._LandPropertyRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            self._ErpOrganisation._LandPropertyRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

    def getLandProperty(self):
        
        return self._LandProperty

    def setLandProperty(self, value):
        for p in self._LandProperty:
            filtered = [q for q in p.ErpOrganisationRoles if q != self]
            self._LandProperty._ErpOrganisationRoles = filtered
        for r in value:
            if self not in r._ErpOrganisationRoles:
                r._ErpOrganisationRoles.append(self)
        self._LandProperty = value

    LandProperty = property(getLandProperty, setLandProperty)

    def addLandProperty(self, *LandProperty):
        for obj in LandProperty:
            if self not in obj._ErpOrganisationRoles:
                obj._ErpOrganisationRoles.append(self)
            self._LandProperty.append(obj)

    def removeLandProperty(self, *LandProperty):
        for obj in LandProperty:
            if self in obj._ErpOrganisationRoles:
                obj._ErpOrganisationRoles.remove(self)
            self._LandProperty.remove(obj)

