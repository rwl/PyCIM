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

"""The package is used to define asset-level models for objects. Assets may be comprised of other assets and may have relationships to other assets. Assets also have owners and values. Assets may also have a relationship to a PowerSystemResource in the Wires model.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'Assets are the basic units which define a physical infrastructure. PowerSystemResources are logical objects meaningful to operations which are constructed from one or more Assets, although PowerSystemResources are not required to specifiy their component Assets. The Asset package is comprosed of several packages. The key concepts of an Asset are as follows: <ul> 	<li>Assets can have names, through inheritance to the Naming package</li> 	<li>Assets are physical entities which have a lifecycle</li> 	<li>One or more assets can be associated to create a PowerSystemResource</li> 	<li>Assets can be grouped (aggregated) with other Assets</li> 	<li>Assets are typically either 'point' or 'linear' assets, which relate to physical geometry</li> 	<li>Assets have a close relationship to Work as a consequence of their lifecycle</li> </ul> The following sections describe the packages in the Assets package. The AssetBasics package defines the relationship between Asset and other classes, such as Organization, PowerSystemResource and Document. Point assets are those assets whose physical location can be described in terms of a single coordinate, such as a pole or a switch. Linear assets are those assets whose physical location is best described in terms of a line, plyline or polygon. Asset work triggers are used to determine when inspection and/or maintenance are required for assets.'
"""

ns_prefix = "cimInfAssets"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfAssets"

from CIM14v13.IEC61968.Informative.InfAssets.FailureEvent import FailureEvent
from CIM14v13.IEC61968.Informative.InfAssets.ElectricalAsset import ElectricalAsset
from CIM14v13.IEC61968.Informative.InfAssets.SwitchAsset import SwitchAsset
from CIM14v13.IEC61968.Informative.InfAssets.SwitchInfo import SwitchInfo
from CIM14v13.IEC61968.Informative.InfAssets.RecloserInfo import RecloserInfo
from CIM14v13.IEC61968.Informative.InfAssets.PowerRating import PowerRating
from CIM14v13.IEC61968.Informative.InfAssets.BusbarAsset import BusbarAsset
from CIM14v13.IEC61968.Informative.InfAssets.StructureSupport import StructureSupport
from CIM14v13.IEC61968.Informative.InfAssets.Guy import Guy
from CIM14v13.IEC61968.Informative.InfAssets.CurrentTransformerInfo import CurrentTransformerInfo
from CIM14v13.IEC61968.Informative.InfAssets.ConductorAsset import ConductorAsset
from CIM14v13.IEC61968.Informative.InfAssets.CableAsset import CableAsset
from CIM14v13.IEC61968.Informative.InfAssets.Medium import Medium
from CIM14v13.IEC61968.Informative.InfAssets.ProcedureDataSet import ProcedureDataSet
from CIM14v13.IEC61968.Informative.InfAssets.Vehicle import Vehicle
from CIM14v13.IEC61968.Informative.InfAssets.WorkEquipmentAsset import WorkEquipmentAsset
from CIM14v13.IEC61968.Informative.InfAssets.GeneratorAsset import GeneratorAsset
from CIM14v13.IEC61968.Informative.InfAssets.Tool import Tool
from CIM14v13.IEC61968.Informative.InfAssets.TransformerAsset import TransformerAsset
from CIM14v13.IEC61968.Informative.InfAssets.Facility import Facility
from CIM14v13.IEC61968.Informative.InfAssets.Structure import Structure
from CIM14v13.IEC61968.Informative.InfAssets.UndergroundStructure import UndergroundStructure
from CIM14v13.IEC61968.Informative.InfAssets.AssetAssetRole import AssetAssetRole
from CIM14v13.IEC61968.Informative.InfAssets.WindingInsulation import WindingInsulation
from CIM14v13.IEC61968.Informative.InfAssets.TransformerObservation import TransformerObservation
from CIM14v13.IEC61968.Informative.InfAssets.ShuntCompensatorAsset import ShuntCompensatorAsset
from CIM14v13.IEC61968.Informative.InfAssets.SurgeProtectorAsset import SurgeProtectorAsset
from CIM14v13.IEC61968.Informative.InfAssets.CompositeSwitchInfo import CompositeSwitchInfo
from CIM14v13.IEC61968.Informative.InfAssets.PotentialTransformerAsset import PotentialTransformerAsset
from CIM14v13.IEC61968.Informative.InfAssets.TestDataSet import TestDataSet
from CIM14v13.IEC61968.Informative.InfAssets.FACTSDeviceAsset import FACTSDeviceAsset
from CIM14v13.IEC61968.Informative.InfAssets.OverheadConductorAsset import OverheadConductorAsset
from CIM14v13.IEC61968.Informative.InfAssets.ShuntImpedanceInfo import ShuntImpedanceInfo
from CIM14v13.IEC61968.Informative.InfAssets.DuctBank import DuctBank
from CIM14v13.IEC61968.Informative.InfAssets.SVCAsset import SVCAsset
from CIM14v13.IEC61968.Informative.InfAssets.ProtectionEquipmentAsset import ProtectionEquipmentAsset
from CIM14v13.IEC61968.Informative.InfAssets.Manhole import Manhole
from CIM14v13.IEC61968.Informative.InfAssets.Procedure import Procedure
from CIM14v13.IEC61968.Informative.InfAssets.BreakerAsset import BreakerAsset
from CIM14v13.IEC61968.Informative.InfAssets.TapChangerAsset import TapChangerAsset
from CIM14v13.IEC61968.Informative.InfAssets.PotentialTransformerInfo import PotentialTransformerInfo
from CIM14v13.IEC61968.Informative.InfAssets.AssetPsrRole import AssetPsrRole
from CIM14v13.IEC61968.Informative.InfAssets.DocAssetRole import DocAssetRole
from CIM14v13.IEC61968.Informative.InfAssets.SubstationAsset import SubstationAsset
from CIM14v13.IEC61968.Informative.InfAssets.SeriesCompensatorAsset import SeriesCompensatorAsset
from CIM14v13.IEC61968.Informative.InfAssets.SVCInfo import SVCInfo
from CIM14v13.IEC61968.Informative.InfAssets.CompositeSwitchAsset import CompositeSwitchAsset
from CIM14v13.IEC61968.Informative.InfAssets.AssetPropertyCurve import AssetPropertyCurve
from CIM14v13.IEC61968.Informative.InfAssets.Pole import Pole
from CIM14v13.IEC61968.Informative.InfAssets.Specification import Specification
from CIM14v13.IEC61968.Informative.InfAssets.BushingInsulationPF import BushingInsulationPF
from CIM14v13.IEC61968.Informative.InfAssets.DimensionsInfo import DimensionsInfo
from CIM14v13.IEC61968.Informative.InfAssets.Anchor import Anchor
from CIM14v13.IEC61968.Informative.InfAssets.ComEquipmentAsset import ComEquipmentAsset
from CIM14v13.IEC61968.Informative.InfAssets.CurrentTransformerAsset import CurrentTransformerAsset
from CIM14v13.IEC61968.Informative.InfAssets.ResistorAsset import ResistorAsset
from CIM14v13.IEC61968.Informative.InfAssets.Streetlight import Streetlight
from CIM14v13.IEC61968.Informative.InfAssets.BushingAsset import BushingAsset
from CIM14v13.IEC61968.Informative.InfAssets.JointAsset import JointAsset
from CIM14v13.IEC61968.Informative.InfAssets.RecloserAsset import RecloserAsset
from CIM14v13.IEC61968.Informative.InfAssets.Cabinet import Cabinet
from CIM14v13.IEC61968.Informative.InfAssets.ReliabilityInfo import ReliabilityInfo
from CIM14v13.IEC61968.Informative.InfAssets.Tower import Tower
from CIM14v13.IEC61968.Informative.InfAssets.FaultIndicatorAsset import FaultIndicatorAsset
from CIM14v13.IEC61968.Informative.InfAssets.OrgAssetRole import OrgAssetRole
from CIM14v13.IEC61968.Informative.InfAssets.FinancialInfo import FinancialInfo
from CIM14v13.IEC61968.Informative.InfAssets.BreakerInfo import BreakerInfo
