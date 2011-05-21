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

"""This package contains the core information classes that support asset management applications with specialized classes for asset-level models for objects (as opposed to power system resource models, mainly defined in IEC61970::Wires package).
"""

from CIM14.IEC61968.Assets.AssetFunction import AssetFunction
from CIM14.IEC61968.Assets.Asset import Asset
from CIM14.IEC61968.Assets.AssetContainer import AssetContainer
from CIM14.IEC61968.Assets.AcceptanceTest import AcceptanceTest
from CIM14.IEC61968.Assets.Seal import Seal
from CIM14.IEC61968.Assets.ComMediaAsset import ComMediaAsset

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Assets"
nsPrefix = "cimAssets"


class SealKind(str):
    """Kind of seal.
    Values are: other, lead, steel, lock
    """
    pass

class SealConditionKind(str):
    """Kind of seal condition.
    Values are: open, broken, missing, other, locked
    """
    pass
