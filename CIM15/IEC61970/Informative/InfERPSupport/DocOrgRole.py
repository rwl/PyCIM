# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Informative.InfCommon.Role import Role

class DocOrgRole(Role):
    """Roles played between Organisations and Documents.Roles played between Organisations and Documents.
    """

    def __init__(self, Document=None, ErpOrganisation=None, *args, **kw_args):
        """Initialises a new 'DocOrgRole' instance.

        @param Document:
        @param ErpOrganisation:
        """
        self._Document = None
        self.Document = Document

        self._ErpOrganisation = None
        self.ErpOrganisation = ErpOrganisation

        super(DocOrgRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Document", "ErpOrganisation"]
    _many_refs = []

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ErpOrganisationRoles if x != self]
            self._Document._ErpOrganisationRoles = filtered

        self._Document = value
        if self._Document is not None:
            if self not in self._Document._ErpOrganisationRoles:
                self._Document._ErpOrganisationRoles.append(self)

    Document = property(getDocument, setDocument)

    def getErpOrganisation(self):
        
        return self._ErpOrganisation

    def setErpOrganisation(self, value):
        if self._ErpOrganisation is not None:
            filtered = [x for x in self.ErpOrganisation.DocumentRoles if x != self]
            self._ErpOrganisation._DocumentRoles = filtered

        self._ErpOrganisation = value
        if self._ErpOrganisation is not None:
            if self not in self._ErpOrganisation._DocumentRoles:
                self._ErpOrganisation._DocumentRoles.append(self)

    ErpOrganisation = property(getErpOrganisation, setErpOrganisation)

