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

from CIM14v13.IEC61968.Common.Document import Document

class AssetModel(Document):
    """Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.
    """

    def __init__(self, corporateStandardKind='other', usageKind='distributionUnderground', modelNumber='', weightTotal=0.0, modelVersion='', ErpInventoryCounts=None, TypeAsset=None, AssetModelCatalogueItems=None, **kw_args):
        """Initializes a new 'AssetModel' instance.

        @param corporateStandardKind: Kind of corporate standard for this asset model. Values are: "other", "underEvaluation", "experimental", "standard"
        @param usageKind: Intended usage for this asset model. Values are: "distributionUnderground", "other", "streetlight", "customerSubstation", "unknown", "distributionOverhead", "substation", "transmission"
        @param modelNumber: Manufacturer's model number. 
        @param weightTotal: Total manufactured weight of asset. 
        @param modelVersion: Version number for product model, which indicates vintage of the product. 
        @param ErpInventoryCounts:
        @param TypeAsset: A type of asset may be satisified with many different types of asset models.
        @param AssetModelCatalogueItems:
        """
        #: Kind of corporate standard for this asset model.Values are: "other", "underEvaluation", "experimental", "standard"
        self.corporateStandardKind = corporateStandardKind

        #: Intended usage for this asset model.Values are: "distributionUnderground", "other", "streetlight", "customerSubstation", "unknown", "distributionOverhead", "substation", "transmission"
        self.usageKind = usageKind

        #: Manufacturer's model number.
        self.modelNumber = modelNumber

        #: Total manufactured weight of asset.
        self.weightTotal = weightTotal

        #: Version number for product model, which indicates vintage of the product.
        self.modelVersion = modelVersion

        self._ErpInventoryCounts = []
        self.ErpInventoryCounts = [] if ErpInventoryCounts is None else ErpInventoryCounts

        self._TypeAsset = None
        self.TypeAsset = TypeAsset

        self._AssetModelCatalogueItems = []
        self.AssetModelCatalogueItems = [] if AssetModelCatalogueItems is None else AssetModelCatalogueItems

        super(AssetModel, self).__init__(**kw_args)

    def getErpInventoryCounts(self):
        
        return self._ErpInventoryCounts

    def setErpInventoryCounts(self, value):
        for x in self._ErpInventoryCounts:
            x._AssetModel = None
        for y in value:
            y._AssetModel = self
        self._ErpInventoryCounts = value

    ErpInventoryCounts = property(getErpInventoryCounts, setErpInventoryCounts)

    def addErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj._AssetModel = self
            self._ErpInventoryCounts.append(obj)

    def removeErpInventoryCounts(self, *ErpInventoryCounts):
        for obj in ErpInventoryCounts:
            obj._AssetModel = None
            self._ErpInventoryCounts.remove(obj)

    def getTypeAsset(self):
        """A type of asset may be satisified with many different types of asset models.
        """
        return self._TypeAsset

    def setTypeAsset(self, value):
        if self._TypeAsset is not None:
            filtered = [x for x in self.TypeAsset.AssetModels if x != self]
            self._TypeAsset._AssetModels = filtered

        self._TypeAsset = value
        if self._TypeAsset is not None:
            self._TypeAsset._AssetModels.append(self)

    TypeAsset = property(getTypeAsset, setTypeAsset)

    def getAssetModelCatalogueItems(self):
        
        return self._AssetModelCatalogueItems

    def setAssetModelCatalogueItems(self, value):
        for x in self._AssetModelCatalogueItems:
            x._AssetModel = None
        for y in value:
            y._AssetModel = self
        self._AssetModelCatalogueItems = value

    AssetModelCatalogueItems = property(getAssetModelCatalogueItems, setAssetModelCatalogueItems)

    def addAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj._AssetModel = self
            self._AssetModelCatalogueItems.append(obj)

    def removeAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj._AssetModel = None
            self._AssetModelCatalogueItems.remove(obj)

