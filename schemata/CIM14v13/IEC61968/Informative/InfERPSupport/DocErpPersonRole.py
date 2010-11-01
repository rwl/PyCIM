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

class DocErpPersonRole(Role):
    """Roles played between Persons and Documents.
    """

    def __init__(self, ErpPerson=None, Document=None, *args, **kw_args):
        """Initializes a new 'DocErpPersonRole' instance.

        @param ErpPerson:
        @param Document:
        """
        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        self._Document = None
        self.Document = Document

        super(DocErpPersonRole, self).__init__(*args, **kw_args)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.DocumentRoles if x != self]
            self._ErpPerson._DocumentRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            self._ErpPerson._DocumentRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ErpPersonRoles if x != self]
            self._Document._ErpPersonRoles = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._ErpPersonRoles.append(self)

    Document = property(getDocument, setDocument)

