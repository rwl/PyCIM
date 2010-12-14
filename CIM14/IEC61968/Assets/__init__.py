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

"""This package contains the core information classes that support asset management applications with specialized classes for asset-level models for objects (as opposed to power system resource models, mainly defined in IEC61970::Wires package).
"""

nsPrefix = "cimAssets"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Assets"

from CIM14.IEC61968.Assets.AssetFunction import AssetFunction
from CIM14.IEC61968.Assets.Asset import Asset
from CIM14.IEC61968.Assets.AssetContainer import AssetContainer
from CIM14.IEC61968.Assets.AcceptanceTest import AcceptanceTest
from CIM14.IEC61968.Assets.Seal import Seal
from CIM14.IEC61968.Assets.ComMediaAsset import ComMediaAsset

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
