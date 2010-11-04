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

class DocDocRole(Role):
    """Roles played between Documents and other Documents.
    """

    def __init__(self, ToDocument=None, FromDocument=None, **kw_args):
        """Initializes a new 'DocDocRole' instance.

        @param ToDocument:
        @param FromDocument:
        """
        self._ToDocument = None
        self.ToDocument = ToDocument

        self._FromDocument = None
        self.FromDocument = FromDocument

        super(DocDocRole, self).__init__(**kw_args)

    def getToDocument(self):
        
        return self._ToDocument

    def setToDocument(self, value):
        if self._ToDocument is not None:
            filtered = [x for x in self.ToDocument.FromDocumentRoles if x != self]
            self._ToDocument._FromDocumentRoles = filtered

        self._ToDocument = value
        if self._ToDocument is not None:
            self._ToDocument._FromDocumentRoles.append(self)

    ToDocument = property(getToDocument, setToDocument)

    def getFromDocument(self):
        
        return self._FromDocument

    def setFromDocument(self, value):
        if self._FromDocument is not None:
            filtered = [x for x in self.FromDocument.ToDocumentRoles if x != self]
            self._FromDocument._ToDocumentRoles = filtered

        self._FromDocument = value
        if self._FromDocument is not None:
            self._FromDocument._ToDocumentRoles.append(self)

    FromDocument = property(getFromDocument, setFromDocument)

