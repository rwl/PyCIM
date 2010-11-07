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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class AssetModel(IdentifiedObject):
    """Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.
    """

    def __init__(self, usageKind='streetlight', corporateStandardKind='other', modelNumber='', weightTotal=0.0, modelVersion='', **kw_args):
        """Initializes a new 'AssetModel' instance.

        @param usageKind: Intended usage for this asset model. Values are: "streetlight", "other", "unknown", "substation", "distributionOverhead", "customerSubstation", "transmission", "distributionUnderground"
        @param corporateStandardKind: Kind of corporate standard for this asset model. Values are: "other", "standard", "experimental", "underEvaluation"
        @param modelNumber: Manufacturer's model number. 
        @param weightTotal: Total manufactured weight of asset. 
        @param modelVersion: Version number for product model, which indicates vintage of the product. 
        """
        #: Intended usage for this asset model.Values are: "streetlight", "other", "unknown", "substation", "distributionOverhead", "customerSubstation", "transmission", "distributionUnderground"
        self.usageKind = usageKind

        #: Kind of corporate standard for this asset model.Values are: "other", "standard", "experimental", "underEvaluation"
        self.corporateStandardKind = corporateStandardKind

        #: Manufacturer's model number.
        self.modelNumber = modelNumber

        #: Total manufactured weight of asset.
        self.weightTotal = weightTotal

        #: Version number for product model, which indicates vintage of the product.
        self.modelVersion = modelVersion

        super(AssetModel, self).__init__(**kw_args)

