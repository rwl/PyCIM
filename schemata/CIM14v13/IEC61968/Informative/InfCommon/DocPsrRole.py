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

class DocPsrRole(Role):
    """Potential roles that might played by a document relative to a type of PowerSystemResource.
    """

    def __init__(self, Document=None, PowerSystemResource=None, *args, **kw_args):
        """Initializes a new 'DocPsrRole' instance.

        @param Document:
        @param PowerSystemResource:
        """
        self._Document = None
        self.Document = Document

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        super(DocPsrRole, self).__init__(*args, **kw_args)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.PowerSystemResourceRoles if x != self]
            self._Document._PowerSystemResourceRoles = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._PowerSystemResourceRoles.append(self)

    Document = property(getDocument, setDocument)

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.DocumentRoles if x != self]
            self._PowerSystemResource._DocumentRoles = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._DocumentRoles.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

