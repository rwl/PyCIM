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

"""This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""

ns_prefix = "cimAssetModels"
ns_uri = "http://iec.ch/TC57/CIM-generic#AssetModels"

from CIM14v13.IEC61968.AssetModels.AssetModel import AssetModel
from CIM14v13.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest
from CIM14v13.IEC61968.AssetModels.WindingInfo import WindingInfo
from CIM14v13.IEC61968.AssetModels.ConductorInfo import ConductorInfo
from CIM14v13.IEC61968.AssetModels.CableInfo import CableInfo
from CIM14v13.IEC61968.AssetModels.ConcentricNeutralCableInfo import ConcentricNeutralCableInfo
from CIM14v13.IEC61968.AssetModels.WireArrangement import WireArrangement
from CIM14v13.IEC61968.AssetModels.WireType import WireType
from CIM14v13.IEC61968.AssetModels.ShortCircuitTest import ShortCircuitTest
from CIM14v13.IEC61968.AssetModels.OverheadConductorInfo import OverheadConductorInfo
from CIM14v13.IEC61968.AssetModels.OpenCircuitTest import OpenCircuitTest
from CIM14v13.IEC61968.AssetModels.TransformerInfo import TransformerInfo
from CIM14v13.IEC61968.AssetModels.ToWindingSpec import ToWindingSpec
from CIM14v13.IEC61968.AssetModels.TapeShieldCableInfo import TapeShieldCableInfo
from CIM14v13.IEC61968.AssetModels.EndDeviceModel import EndDeviceModel
