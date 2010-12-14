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

nsPrefix = "cimAssetModels"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#AssetModels"

from CIM14.IEC61968.AssetModels.AssetModel import AssetModel
from CIM14.IEC61968.AssetModels.EndDeviceModel import EndDeviceModel
from CIM14.IEC61968.AssetModels.WireArrangement import WireArrangement
from CIM14.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest
from CIM14.IEC61968.AssetModels.ShortCircuitTest import ShortCircuitTest
from CIM14.IEC61968.AssetModels.TransformerInfo import TransformerInfo
from CIM14.IEC61968.AssetModels.WireType import WireType
from CIM14.IEC61968.AssetModels.OpenCircuitTest import OpenCircuitTest
from CIM14.IEC61968.AssetModels.ConductorInfo import ConductorInfo
from CIM14.IEC61968.AssetModels.OverheadConductorInfo import OverheadConductorInfo
from CIM14.IEC61968.AssetModels.CableInfo import CableInfo
from CIM14.IEC61968.AssetModels.TapeShieldCableInfo import TapeShieldCableInfo
from CIM14.IEC61968.AssetModels.WindingInfo import WindingInfo
from CIM14.IEC61968.AssetModels.ToWindingSpec import ToWindingSpec
from CIM14.IEC61968.AssetModels.ConcentricNeutralCableInfo import ConcentricNeutralCableInfo

class CorporateStandardKind(str):
    """Kind of corporate standard.
    Values are: other, standard, experimental, underEvaluation
    """
    pass

class AssetModelUsageKind(str):
    """Usage for an asset model.
    Values are: streetlight, other, unknown, substation, distributionOverhead, customerSubstation, transmission, distributionUnderground
    """
    pass

class ConductorMaterialKind(str):
    """Kind of conductor material.
    Values are: acsr, steel, aluminum, copper, other
    """
    pass

class CableConstructionKind(str):
    """Kind of cable construction.
    Values are: sector, compressed, segmental, solid, stranded, compacted, other
    """
    pass

class ConductorUsageKind(str):
    """Kind of conductor usage.
    Values are: distribution, secondary, transmission, other
    """
    pass

class ConductorInsulationKind(str):
    """Kind of conductor insulation.
    Values are: crosslinkedPolyethylene, ozoneResistantRubber, highMolecularWeightPolyethylene, unbeltedPilc, treeRetardantCrosslinkedPolyethylene, butyl, rubber, asbestosAndVarnishedCambric, beltedPilc, varnishedDacronGlass, other, treeResistantHighMolecularWeightPolyethylene, lowCapacitanceRubber, varnishedCambricCloth, highPressureFluidFilled, ethylenePropyleneRubber, siliconRubber, oilPaper
    """
    pass

class CableOuterJacketKind(str):
    """Kind of cable outer jacket.
    Values are: polyethylene, pvc, none, linearLowDensityPolyethylene, other, insulating, semiconducting
    """
    pass

class CableShieldMaterialKind(str):
    """Kind of cable shield material.
    Values are: steel, lead, aluminum, other, copper
    """
    pass
