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

class AssetModelCatalogue(IdentifiedObject):
    """Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.
    """

    def __init__(self, status=None, AssetModelCatalogueItems=None, **kw_args):
        """Initializes a new 'AssetModelCatalogue' instance.

        @param status:
        @param AssetModelCatalogueItems:
        """
        self.status = status

        self._AssetModelCatalogueItems = []
        self.AssetModelCatalogueItems = [] if AssetModelCatalogueItems is None else AssetModelCatalogueItems

        super(AssetModelCatalogue, self).__init__(**kw_args)

    status = None

    def getAssetModelCatalogueItems(self):
        
        return self._AssetModelCatalogueItems

    def setAssetModelCatalogueItems(self, value):
        for x in self._AssetModelCatalogueItems:
            x._AssetModelCatalogue = None
        for y in value:
            y._AssetModelCatalogue = self
        self._AssetModelCatalogueItems = value

    AssetModelCatalogueItems = property(getAssetModelCatalogueItems, setAssetModelCatalogueItems)

    def addAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj._AssetModelCatalogue = self
            self._AssetModelCatalogueItems.append(obj)

    def removeAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj._AssetModelCatalogue = None
            self._AssetModelCatalogueItems.remove(obj)

