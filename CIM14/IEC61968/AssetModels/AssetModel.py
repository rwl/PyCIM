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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetModel(IdentifiedObject):
    """Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.
    """

    def __init__(self, usageKind="streetlight", corporateStandardKind="other", modelNumber='', weightTotal=0.0, modelVersion='', *args, **kw_args):
        """Initialises a new 'AssetModel' instance.

        @param usageKind: Intended usage for this asset model. Values are: "streetlight", "other", "unknown", "substation", "distributionOverhead", "customerSubstation", "transmission", "distributionUnderground"
        @param corporateStandardKind: Kind of corporate standard for this asset model. Values are: "other", "standard", "experimental", "underEvaluation"
        @param modelNumber: Manufacturer's model number. 
        @param weightTotal: Total manufactured weight of asset. 
        @param modelVersion: Version number for product model, which indicates vintage of the product. 
        """
        #: Intended usage for this asset model. Values are: "streetlight", "other", "unknown", "substation", "distributionOverhead", "customerSubstation", "transmission", "distributionUnderground"
        self.usageKind = usageKind

        #: Kind of corporate standard for this asset model. Values are: "other", "standard", "experimental", "underEvaluation"
        self.corporateStandardKind = corporateStandardKind

        #: Manufacturer's model number.
        self.modelNumber = modelNumber

        #: Total manufactured weight of asset.
        self.weightTotal = weightTotal

        #: Version number for product model, which indicates vintage of the product.
        self.modelVersion = modelVersion

        super(AssetModel, self).__init__(*args, **kw_args)

    _attrs = ["usageKind", "corporateStandardKind", "modelNumber", "weightTotal", "modelVersion"]
    _attr_types = {"usageKind": str, "corporateStandardKind": str, "modelNumber": str, "weightTotal": float, "modelVersion": str}
    _defaults = {"usageKind": "streetlight", "corporateStandardKind": "other", "modelNumber": '', "weightTotal": 0.0, "modelVersion": ''}
    _enums = {"usageKind": "AssetModelUsageKind", "corporateStandardKind": "CorporateStandardKind"}
    _refs = []
    _many_refs = []

