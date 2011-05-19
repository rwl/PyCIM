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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetModelCatalogue(IdentifiedObject):
    """Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.
    """

    def __init__(self, AssetModelCatalogueItems=None, status=None, *args, **kw_args):
        """Initialises a new 'AssetModelCatalogue' instance.

        @param AssetModelCatalogueItems:
        @param status:
        """
        self._AssetModelCatalogueItems = []
        self.AssetModelCatalogueItems = [] if AssetModelCatalogueItems is None else AssetModelCatalogueItems

        self.status = status

        super(AssetModelCatalogue, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["AssetModelCatalogueItems", "status"]
    _many_refs = ["AssetModelCatalogueItems"]

    def getAssetModelCatalogueItems(self):
        
        return self._AssetModelCatalogueItems

    def setAssetModelCatalogueItems(self, value):
        for x in self._AssetModelCatalogueItems:
            x.AssetModelCatalogue = None
        for y in value:
            y._AssetModelCatalogue = self
        self._AssetModelCatalogueItems = value

    AssetModelCatalogueItems = property(getAssetModelCatalogueItems, setAssetModelCatalogueItems)

    def addAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj.AssetModelCatalogue = self

    def removeAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj.AssetModelCatalogue = None

    status = None

