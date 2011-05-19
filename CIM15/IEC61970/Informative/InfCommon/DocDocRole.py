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

class DocDocRole(Role):
    """Roles played between Documents and other Documents.Roles played between Documents and other Documents.
    """

    def __init__(self, ToDocument=None, FromDocument=None, *args, **kw_args):
        """Initialises a new 'DocDocRole' instance.

        @param ToDocument:
        @param FromDocument:
        """
        self._ToDocument = None
        self.ToDocument = ToDocument

        self._FromDocument = None
        self.FromDocument = FromDocument

        super(DocDocRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["ToDocument", "FromDocument"]
    _many_refs = []

    def getToDocument(self):
        
        return self._ToDocument

    def setToDocument(self, value):
        if self._ToDocument is not None:
            filtered = [x for x in self.ToDocument.FromDocumentRoles if x != self]
            self._ToDocument._FromDocumentRoles = filtered

        self._ToDocument = value
        if self._ToDocument is not None:
            if self not in self._ToDocument._FromDocumentRoles:
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
            if self not in self._FromDocument._ToDocumentRoles:
                self._FromDocument._ToDocumentRoles.append(self)

    FromDocument = property(getFromDocument, setFromDocument)

