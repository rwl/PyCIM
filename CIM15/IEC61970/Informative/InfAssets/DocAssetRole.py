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

class DocAssetRole(Role):
    """Roles played between Documents and Assets.Roles played between Documents and Assets.
    """

    def __init__(self, Document=None, Asset=None, *args, **kw_args):
        """Initialises a new 'DocAssetRole' instance.

        @param Document:
        @param Asset:
        """
        self._Document = None
        self.Document = Document

        self._Asset = None
        self.Asset = Asset

        super(DocAssetRole, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Document", "Asset"]
    _many_refs = []

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.AssetRoles if x != self]
            self._Document._AssetRoles = filtered

        self._Document = value
        if self._Document is not None:
            if self not in self._Document._AssetRoles:
                self._Document._AssetRoles.append(self)

    Document = property(getDocument, setDocument)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.DocumentRoles if x != self]
            self._Asset._DocumentRoles = filtered

        self._Asset = value
        if self._Asset is not None:
            if self not in self._Asset._DocumentRoles:
                self._Asset._DocumentRoles.append(self)

    Asset = property(getAsset, setAsset)

