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

ns_prefix = "cimAssets"
ns_uri = "http://iec.ch/TC57/CIM-generic#Assets"

from CIM14v13.IEC61968.Assets.Seal import Seal
from CIM14v13.IEC61968.Assets.Asset import Asset
from CIM14v13.IEC61968.Assets.AssetFunction import AssetFunction
from CIM14v13.IEC61968.Assets.ElectricalInfo import ElectricalInfo
from CIM14v13.IEC61968.Assets.ComMediaAsset import ComMediaAsset
from CIM14v13.IEC61968.Assets.AssetContainer import AssetContainer
from CIM14v13.IEC61968.Assets.AcceptanceTest import AcceptanceTest
