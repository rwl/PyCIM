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

class ErpPersonLocRole(Role):
    """Roles played between People and Locations. Some Locations are somewhat static, like the person's home address. Other may be dynamic, for example when the person is part of a crew driving around in truck.
    """

    def __init__(self, Location=None, ErpPerson=None, *args, **kw_args):
        """Initializes a new 'ErpPersonLocRole' instance.

        @param Location:
        @param ErpPerson:
        """
        self._Location = None
        self.Location = Location

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        super(ErpPersonLocRole, self).__init__(*args, **kw_args)

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.ErpPersonRoles if x != self]
            self._Location._ErpPersonRoles = filtered

        self._Location = value
        if self._Location is not None:
            self._Location._ErpPersonRoles.append(self)

    Location = property(getLocation, setLocation)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.LocationRoles if x != self]
            self._ErpPerson._LocationRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._LocationRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

