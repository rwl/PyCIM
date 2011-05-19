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

"""The package is used to define asset-level models for objects. Assets may be comprised of other assets and may have relationships to other assets. Assets also have owners and values. Assets may also have a relationship to a PowerSystemResource in the Wires model.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Assets are the basic units which define a physical infrastructure. PowerSystemResources are logical objects meaningful to operations which are constructed from one or more Assets, although PowerSystemResources are not required to specifiy their component Assets. The Asset package is comprosed of several packages. The key concepts of an Asset are as follows: <ul> 	<li>Assets can have names, through inheritance to the Naming package</li> 	<li>Assets are physical entities which have a lifecycle</li> 	<li>One or more assets can be associated to create a PowerSystemResource</li> 	<li>Assets can be grouped (aggregated) with other Assets</li> 	<li>Assets are typically either 'point' or 'linear' assets, which relate to physical geometry</li> 	<li>Assets have a close relationship to Work as a consequence of their lifecycle</li> </ul> The following sections describe the packages in the Assets package. The AssetBasics package defines the relationship between Asset and other classes, such as Organization, PowerSystemResource and Document. Point assets are those assets whose physical location can be described in terms of a single coordinate, such as a pole or a switch. Linear assets are those assets whose physical location is best described in terms of a line, plyline or polygon. Asset work triggers are used to determine when inspection and/or maintenance are required for assets.'
"""

from CIM15.IEC61970.Informative.InfAssets.FACTSDevice import FACTSDevice
from CIM15.IEC61970.Informative.InfAssets.DocAssetRole import DocAssetRole
from CIM15.IEC61970.Informative.InfAssets.DuctBank import DuctBank
from CIM15.IEC61970.Informative.InfAssets.ConductorAsset import ConductorAsset
from CIM15.IEC61970.Informative.InfAssets.FinancialInfo import FinancialInfo
from CIM15.IEC61970.Informative.InfAssets.ProtectionEquipmentInfo import ProtectionEquipmentInfo
from CIM15.IEC61970.Informative.InfAssets.ProcedureDataSet import ProcedureDataSet
from CIM15.IEC61970.Informative.InfAssets.WindingInsulation import WindingInsulation
from CIM15.IEC61970.Informative.InfAssets.Specification import Specification
from CIM15.IEC61970.Informative.InfAssets.UndergroundStructure import UndergroundStructure
from CIM15.IEC61970.Informative.InfAssets.PotentialTransformerInfo import PotentialTransformerInfo
from CIM15.IEC61970.Informative.InfAssets.Structure import Structure
from CIM15.IEC61970.Informative.InfAssets.CurrentTransformerInfo import CurrentTransformerInfo
from CIM15.IEC61970.Informative.InfAssets.BushingInsulationPF import BushingInsulationPF
from CIM15.IEC61970.Informative.InfAssets.Joint import Joint
from CIM15.IEC61970.Informative.InfAssets.ElectricalInfo import ElectricalInfo
from CIM15.IEC61970.Informative.InfAssets.WorkEquipment import WorkEquipment
from CIM15.IEC61970.Informative.InfAssets.FaultIndicatorInfo import FaultIndicatorInfo
from CIM15.IEC61970.Informative.InfAssets.Duct import Duct
from CIM15.IEC61970.Informative.InfAssets.PowerRating import PowerRating
from CIM15.IEC61970.Informative.InfAssets.AssetAssetRole import AssetAssetRole
from CIM15.IEC61970.Informative.InfAssets.TransformerAsset import TransformerAsset
from CIM15.IEC61970.Informative.InfAssets.Procedure import Procedure
from CIM15.IEC61970.Informative.InfAssets.BreakerInfo import BreakerInfo
from CIM15.IEC61970.Informative.InfAssets.CompositeSwitchInfo import CompositeSwitchInfo
from CIM15.IEC61970.Informative.InfAssets.Cabinet import Cabinet
from CIM15.IEC61970.Informative.InfAssets.Bushing import Bushing
from CIM15.IEC61970.Informative.InfAssets.Vehicle import Vehicle
from CIM15.IEC61970.Informative.InfAssets.SurgeProtectorInfo import SurgeProtectorInfo
from CIM15.IEC61970.Informative.InfAssets.StructureSupport import StructureSupport
from CIM15.IEC61970.Informative.InfAssets.ComEquipment import ComEquipment
from CIM15.IEC61970.Informative.InfAssets.AssetPropertyCurve import AssetPropertyCurve
from CIM15.IEC61970.Informative.InfAssets.FailureEvent import FailureEvent
from CIM15.IEC61970.Informative.InfAssets.DimensionsInfo import DimensionsInfo
from CIM15.IEC61970.Informative.InfAssets.Tower import Tower
from CIM15.IEC61970.Informative.InfAssets.MountingConnection import MountingConnection
from CIM15.IEC61970.Informative.InfAssets.Medium import Medium
from CIM15.IEC61970.Informative.InfAssets.RecloserInfo import RecloserInfo
from CIM15.IEC61970.Informative.InfAssets.Facility import Facility
from CIM15.IEC61970.Informative.InfAssets.ShuntImpedanceInfo import ShuntImpedanceInfo
from CIM15.IEC61970.Informative.InfAssets.ShuntCompensatorInfo import ShuntCompensatorInfo
from CIM15.IEC61970.Informative.InfAssets.MountingPoint import MountingPoint
from CIM15.IEC61970.Informative.InfAssets.SubstationAsset import SubstationAsset
from CIM15.IEC61970.Informative.InfAssets.Streetlight import Streetlight
from CIM15.IEC61970.Informative.InfAssets.Tool import Tool
from CIM15.IEC61970.Informative.InfAssets.SVC import SVC
from CIM15.IEC61970.Informative.InfAssets.OrgAssetRole import OrgAssetRole
from CIM15.IEC61970.Informative.InfAssets.TestDataSet import TestDataSet
from CIM15.IEC61970.Informative.InfAssets.GenericAssetModelOrMaterial import GenericAssetModelOrMaterial
from CIM15.IEC61970.Informative.InfAssets.ReliabilityInfo import ReliabilityInfo
from CIM15.IEC61970.Informative.InfAssets.TransformerObservation import TransformerObservation
from CIM15.IEC61970.Informative.InfAssets.Pole import Pole
from CIM15.IEC61970.Informative.InfAssets.SwitchInfo import SwitchInfo

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#InfAssets"
nsPrefix = "cimInfAssets"


class AnchorKind(str):
    """Values are: concrete, helix, unknown, multiHelix, screw, rod, other
    """
    pass

class TowerConstructionKind(str):
    """Values are: suspension, tension
    """
    pass

class ProcedureKind(str):
    """Values are: test, maintenance, other, inspection, diagnosis
    """
    pass

class FacilityKind(str):
    """Values are: plant, building, storage, switching, generation
    """
    pass

class MediumKind(str):
    """Values are: gas, liquid, solid
    """
    pass

class UndergroundStructureKind(str):
    """Values are: trench, pullbox, vault, burd, subsurfaceEnclosure, handhole, enclosure, tunnel, manhole, pad
    """
    pass

class PolePreservativeKind(str):
    """Values are: penta, unknown, chemonite, other, naphthena, creosote, cellon
    """
    pass

class ShuntImpedanceLocalControlKind(str):
    """Values are: none, temperature, powerFactor, voltage, reactivePower, time, current
    """
    pass

class CoolingKind(str):
    """Values are: forcedAir, selfCooling, forcedOilAndAir, other
    """
    pass

class RegulationBranchKind(str):
    """Values are: recloser, transformer, breaker, fuse, switch, sectionner, other, line
    """
    pass

class VehicleUsageKind(str):
    """Values are: crew, contractor, user, other
    """
    pass

class SubstationFunctionKind(str):
    """Values are: transmission, distribution, other, generation, subTransmission, industrial
    """
    pass

class JointFillKind(str):
    """Values are: epoxy, noFillPrefab, airNoFilling, other, asphaltic, insoluseal, oil, noVoid, petrolatum, bluefill254
    """
    pass

class BushingInsulationPfTestKind(str):
    """Values are: c2, c1
    """
    pass

class PoleTreatmentKind(str):
    """Values are: unknown, natural, grayStain, greenStain, penta, butt, other, full
    """
    pass

class FaultIndicatorResetKind(str):
    """Values are: automatic, other, remote, manual
    """
    pass

class ShuntImpedanceControlKind(str):
    """Values are: remoteOnly, remoteWithLocalOverride, localOnly, fixed
    """
    pass

class JointConfigurationKind(str):
    """Values are: other, wires2to1, wires3to1, wires1to1
    """
    pass

class PoleBaseKind(str):
    """Values are: dirt, asphalt, unknown, cement, other
    """
    pass

class FACTSDeviceKind(str):
    """Values are: tcpar, tssc, tsbr, svc, tcsc, tcvl, statcom, upfc
    """
    pass

class StructureSupportKind(str):
    """Values are: guy, anchor
    """
    pass

class BushingInsulationKind(str):
    """Values are: solidPorcelain, compound, other, paperoil
    """
    pass

class StructureMaterialKind(str):
    """Values are: wood, concrete, steel, other
    """
    pass

class StreetlightLampKind(str):
    """Values are: metalHalide, highPressureSodium, other, mercuryVapor
    """
    pass

class CompositeSwitchKind(str):
    """Values are: throwOver, regulatorBypass, escoThrowOver, ral, other, gral, ugMultiSwitch
    """
    pass

class FailureIsolationMethodKind(str):
    """Values are: fuse, manuallyIsolated, breakerOperation, other, burnedInTheClear
    """
    pass
