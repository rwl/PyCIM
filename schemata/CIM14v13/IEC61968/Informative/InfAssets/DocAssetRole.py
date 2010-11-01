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

class DocAssetRole(Role):
    """Roles played between Documents and Assets.
    """

    def __init__(self, Asset=None, Document=None, *args, **kw_args):
        """Initializes a new 'DocAssetRole' instance.

        @param Asset:
        @param Document:
        """
        self._Asset = None
        self.Asset = Asset

        self._Document = None
        self.Document = Document

        super(DocAssetRole, self).__init__(*args, **kw_args)

    def getAsset(self):
        
        return self._Asset

    def setAsset(self, value):
        if self._Asset is not None:
            filtered = [x for x in self.Asset.DocumentRoles if x != self]
            self._Asset._DocumentRoles = filtered

        self._Asset = value
        if self._Asset is not None:
            self._Asset._DocumentRoles.append(self)

    Asset = property(getAsset, setAsset)

    def getDocument(self):
        
        return self._Document

    def setDocument(self, value):
        if self._Document is not None:
            filtered = [x for x in self.Document.AssetRoles if x != self]
            self._Document._AssetRoles = filtered

        self._Document = value
        if self._Document is not None:
            self._Document._AssetRoles.append(self)

    Document = property(getDocument, setDocument)

