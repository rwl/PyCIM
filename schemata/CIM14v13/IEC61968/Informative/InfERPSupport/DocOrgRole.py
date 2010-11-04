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

class DocOrgRole(Role):
    """Roles played between Organisations and Documents.
    """

    def __init__(self, ErpOrganisation=None, Document=None, **kw_args):
        """Initializes a new 'DocOrgRole' instance.

        @param ErpOrganisation:
        @param Document:
        """
        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        self._Document = None
        self.Document = Document

        super(DocOrgRole, self).__init__(**kw_args)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.DocumentRoles if x != self]
            self._ErpOrganisation._DocumentRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            self._ErpOrganisation._DocumentRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ErpOrganisationRoles if x != self]
            self._Document._ErpOrganisationRoles = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._ErpOrganisationRoles.append(self)

    Document = property(getDocument, setDocument)

