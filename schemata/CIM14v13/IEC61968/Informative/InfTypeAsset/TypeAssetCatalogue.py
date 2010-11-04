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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TypeAssetCatalogue(IdentifiedObject):
    """Catalogue of generic types of assets (TypeAsset) that may be used for design purposes. It is not associated with a particular manufacturer.
    """

    def __init__(self, TypeAssets=None, status=None, **kw_args):
        """Initializes a new 'TypeAssetCatalogue' instance.

        @param TypeAssets:
        @param status:
        """
        self._TypeAssets = []
        self.TypeAssets = [] if TypeAssets is None else TypeAssets

        self.status = status

        super(TypeAssetCatalogue, self).__init__(**kw_args)

    def getTypeAssets(self):
        
        return self._TypeAssets

    def setTypeAssets(self, value):
        for x in self._TypeAssets:
            x._TypeAssetCatalogue = None
        for y in value:
            y._TypeAssetCatalogue = self
        self._TypeAssets = value

    TypeAssets = property(getTypeAssets, setTypeAssets)

    def addTypeAssets(self, *TypeAssets):
        for obj in TypeAssets:
            obj._TypeAssetCatalogue = self
            self._TypeAssets.append(obj)

    def removeTypeAssets(self, *TypeAssets):
        for obj in TypeAssets:
            obj._TypeAssetCatalogue = None
            self._TypeAssets.remove(obj)

    status = None

