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

class PersonPropertyRole(Role):
    """The role of a person relative to a given piece of property. Examples of roles include: owner, renter, contractor, etc.
    """

    def __init__(self, LandProperty=None, ErpPerson=None, *args, **kw_args):
        """Initializes a new 'PersonPropertyRole' instance.

        @param LandProperty:
        @param ErpPerson:
        """
        self._LandProperty = None
        self.LandProperty = LandProperty

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        super(PersonPropertyRole, self).__init__(*args, **kw_args)

    def getLandProperty(self):
        
        return self._LandProperty

    def setLandProperty(self, value):
        if self._LandProperty is not None:
            filtered = [x for x in self.LandProperty.ErpPersonRoles if x != self]
            self._LandProperty._ErpPersonRoles = filtered

        self._LandProperty = value
        if self._LandProperty is not None:
            self._LandProperty._ErpPersonRoles.append(self)

    LandProperty = property(getLandProperty, setLandProperty)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.LandPropertyRoles if x != self]
            self._ErpPerson._LandPropertyRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._LandPropertyRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

