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

"""This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""

from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.TransformerInfo import TransformerInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.ToWindingSpec import ToWindingSpec
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.WireArrangement import WireArrangement
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.CableInfo import CableInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.OpenCircuitTest import OpenCircuitTest
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.ConcentricNeutralCableInfo import ConcentricNeutralCableInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.ConductorInfo import ConductorInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.DistributionWindingTest import DistributionWindingTest
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.WireType import WireType
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.WindingInfo import WindingInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.OverheadConductorInfo import OverheadConductorInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.TapeShieldCableInfo import TapeShieldCableInfo
from CIM14.CDPSM.Unbalanced.IEC61968.AssetModels.ShortCircuitTest import ShortCircuitTest

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#AssetModels"
nsPrefix = "cimAssetModels"


class CableOuterJacketKind(str):
    """Values are: insulating, other, semiconducting, polyethylene, none, linearLowDensityPolyethylene, pvc
    """
    pass

class CableShieldMaterialKind(str):
    """Values are: other, lead, steel, aluminum, copper
    """
    pass

class ConductorInsulationKind(str):
    """Values are: crosslinkedPolyethylene, butyl, treeRetardantCrosslinkedPolyethylene, asbestosAndVarnishedCambric, highPressureFluidFilled, ethylenePropyleneRubber, ozoneResistantRubber, oilPaper, varnishedDacronGlass, highMolecularWeightPolyethylene, other, varnishedCambricCloth, treeResistantHighMolecularWeightPolyethylene, unbeltedPilc, beltedPilc, rubber, lowCapacitanceRubber, siliconRubber
    """
    pass

class ConductorMaterialKind(str):
    """Values are: steel, other, aluminum, copper, acsr
    """
    pass

class ConductorUsageKind(str):
    """Values are: secondary, other, distribution, transmission
    """
    pass

class CableConstructionKind(str):
    """Values are: solid, stranded, other, segmental, compacted, sector, compressed
    """
    pass
