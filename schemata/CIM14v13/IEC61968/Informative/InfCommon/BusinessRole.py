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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BusinessRole(IdentifiedObject):
    """A business role that this organisation plays. A single organisation typically performs many functions, each one described as a role.
    """

    def __init__(self, category='', Organisations=None, status=None, **kw_args):
        """Initializes a new 'BusinessRole' instance.

        @param category: Category by utility's corporate standards and practices. 
        @param Organisations:
        @param status:
        """
        #: Category by utility's corporate standards and practices.
        self.category = category

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        self.status = status

        super(BusinessRole, self).__init__(**kw_args)

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.BusinessRoles if q != self]
            self._Organisations._BusinessRoles = filtered
        for r in value:
            if self not in r._BusinessRoles:
                r._BusinessRoles.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._BusinessRoles:
                obj._BusinessRoles.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._BusinessRoles:
                obj._BusinessRoles.remove(self)
            self._Organisations.remove(obj)

    status = None

