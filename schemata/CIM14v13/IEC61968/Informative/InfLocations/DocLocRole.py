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

class DocLocRole(Role):
    """Roles played between Documents and Locations. For example, as ErpAddress is a type of Location and WorkBilling is a type of Document, a role is the address for which to mail the invoice. As a TroubleTicket is a type of Document, one instance of Location may be the address for which the trouble is reported.
    """

    def __init__(self, Location=None, Document=None, **kw_args):
        """Initializes a new 'DocLocRole' instance.

        @param Location:
        @param Document:
        """
        self._Location = None
        self.Location = Location

        self._Document = None
        self.Document = Document

        super(DocLocRole, self).__init__(**kw_args)

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.DocumentRoles if x != self]
            self._Location._DocumentRoles = filtered

        self._Location = value
        if self._Location is not None:
            self._Location._DocumentRoles.append(self)

    Location = property(getLocation, setLocation)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.LocationRoles if x != self]
            self._Document._LocationRoles = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._LocationRoles.append(self)

    Document = property(getDocument, setDocument)

