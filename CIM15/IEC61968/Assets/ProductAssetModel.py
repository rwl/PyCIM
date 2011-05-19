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

from CIM15.IEC61968.Assets.AssetModel import AssetModel

class ProductAssetModel(AssetModel):
    """Asset model by a specific manufacturer.Asset model by a specific manufacturer.
    """

    def __init__(self, modelVersion='', usageKind="customerSubstation", corporateStandardKind="standard", modelNumber='', weightTotal=0.0, GenericAssetModelOrMaterial=None, AssetModelCatalogueItems=None, *args, **kw_args):
        """Initialises a new 'ProductAssetModel' instance.

        @param modelVersion: Version number for product model, which indicates vintage of the product. 
        @param usageKind: Intended usage for this asset model. Values are: "customerSubstation", "transmission", "other", "substation", "unknown", "distributionOverhead", "distributionUnderground", "streetlight"
        @param corporateStandardKind: Kind of corporate standard for this asset model. Values are: "standard", "underEvaluation", "other", "experimental"
        @param modelNumber: Manufacturer's model number. 
        @param weightTotal: Total manufactured weight of asset. 
        @param GenericAssetModelOrMaterial: Generic asset model or material satisified by this product asset model.
        @param AssetModelCatalogueItems:
        """
        #: Version number for product model, which indicates vintage of the product.
        self.modelVersion = modelVersion

        #: Intended usage for this asset model. Values are: "customerSubstation", "transmission", "other", "substation", "unknown", "distributionOverhead", "distributionUnderground", "streetlight"
        self.usageKind = usageKind

        #: Kind of corporate standard for this asset model. Values are: "standard", "underEvaluation", "other", "experimental"
        self.corporateStandardKind = corporateStandardKind

        #: Manufacturer's model number.
        self.modelNumber = modelNumber

        #: Total manufactured weight of asset.
        self.weightTotal = weightTotal

        self._GenericAssetModelOrMaterial = None
        self.GenericAssetModelOrMaterial = GenericAssetModelOrMaterial

        self._AssetModelCatalogueItems = []
        self.AssetModelCatalogueItems = [] if AssetModelCatalogueItems is None else AssetModelCatalogueItems

        super(ProductAssetModel, self).__init__(*args, **kw_args)

    _attrs = ["modelVersion", "usageKind", "corporateStandardKind", "modelNumber", "weightTotal"]
    _attr_types = {"modelVersion": str, "usageKind": str, "corporateStandardKind": str, "modelNumber": str, "weightTotal": float}
    _defaults = {"modelVersion": '', "usageKind": "customerSubstation", "corporateStandardKind": "standard", "modelNumber": '', "weightTotal": 0.0}
    _enums = {"usageKind": "AssetModelUsageKind", "corporateStandardKind": "CorporateStandardKind"}
    _refs = ["GenericAssetModelOrMaterial", "AssetModelCatalogueItems"]
    _many_refs = ["AssetModelCatalogueItems"]

    def getGenericAssetModelOrMaterial(self):
        """Generic asset model or material satisified by this product asset model.
        """
        return self._GenericAssetModelOrMaterial

    def setGenericAssetModelOrMaterial(self, value):
        if self._GenericAssetModelOrMaterial is not None:
            filtered = [x for x in self.GenericAssetModelOrMaterial.ProductAssetModels if x != self]
            self._GenericAssetModelOrMaterial._ProductAssetModels = filtered

        self._GenericAssetModelOrMaterial = value
        if self._GenericAssetModelOrMaterial is not None:
            if self not in self._GenericAssetModelOrMaterial._ProductAssetModels:
                self._GenericAssetModelOrMaterial._ProductAssetModels.append(self)

    GenericAssetModelOrMaterial = property(getGenericAssetModelOrMaterial, setGenericAssetModelOrMaterial)

    def getAssetModelCatalogueItems(self):
        
        return self._AssetModelCatalogueItems

    def setAssetModelCatalogueItems(self, value):
        for x in self._AssetModelCatalogueItems:
            x.AssetModel = None
        for y in value:
            y._AssetModel = self
        self._AssetModelCatalogueItems = value

    AssetModelCatalogueItems = property(getAssetModelCatalogueItems, setAssetModelCatalogueItems)

    def addAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj.AssetModel = self

    def removeAssetModelCatalogueItems(self, *AssetModelCatalogueItems):
        for obj in AssetModelCatalogueItems:
            obj.AssetModel = None

