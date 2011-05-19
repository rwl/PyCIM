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

class DocErpPersonRole(Role):
    """Roles played between Persons and Documents.Roles played between Persons and Documents.
    """

    def __init__(self, Document=None, ErpPerson=None, *args, **kw_args):
        """Initialises a new 'DocErpPersonRole' instance.

        @param Document:
        @param ErpPerson:
        """
        self._Document = None
        self.Document = Document

        self._ErpPerson = None
        self.ErpPerson = ErpPerson

        super(DocErpPersonRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Document", "ErpPerson"]
    _many_refs = []

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.ErpPersonRoles if x != self]
            self._Document._ErpPersonRoles = filtered

        self._Document = value
        if self._Document is not None:
            if self not in self._Document._ErpPersonRoles:
                self._Document._ErpPersonRoles.append(self)

    Document = property(getDocument, setDocument)

    def getErpPerson(self):
        
        return self._ErpPerson

    def setErpPerson(self, value):
        if self._ErpPerson is not None:
            filtered = [x for x in self.ErpPerson.DocumentRoles if x != self]
            self._ErpPerson._DocumentRoles = filtered

        self._ErpPerson = value
        if self._ErpPerson is not None:
            if self not in self._ErpPerson._DocumentRoles:
                self._ErpPerson._DocumentRoles.append(self)

    ErpPerson = property(getErpPerson, setErpPerson)

