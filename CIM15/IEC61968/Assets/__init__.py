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

"""This package contains the core information classes that support asset management applications that deal with the physical and lifecycle aspects of various network resources (as opposed to power system resource models defined in IEC61970::Wires package, which support network applications).
"""

from CIM15.IEC61968.Assets.ProductAssetModel import ProductAssetModel
from CIM15.IEC61968.Assets.AssetModel import AssetModel
from CIM15.IEC61968.Assets.Asset import Asset
from CIM15.IEC61968.Assets.ComMedia import ComMedia
from CIM15.IEC61968.Assets.AssetContainer import AssetContainer
from CIM15.IEC61968.Assets.AssetFunction import AssetFunction
from CIM15.IEC61968.Assets.Seal import Seal
from CIM15.IEC61968.Assets.AssetInfo import AssetInfo
from CIM15.IEC61968.Assets.AcceptanceTest import AcceptanceTest

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Assets"
nsPrefix = "cimAssets"


class CorporateStandardKind(str):
    """Values are: standard, underEvaluation, other, experimental
    """
    pass

class SealConditionKind(str):
    """Values are: open, broken, other, missing, locked
    """
    pass

class SealKind(str):
    """Values are: lead, other, steel, lock
    """
    pass

class AssetModelUsageKind(str):
    """Values are: customerSubstation, transmission, other, substation, unknown, distributionOverhead, distributionUnderground, streetlight
    """
    pass
