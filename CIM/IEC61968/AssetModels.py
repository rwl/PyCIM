#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import Document
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Domain import Weight
from CIM.IEC61970.Wires import WindingConnection
from CIM.IEC61970.Domain import ApparentPower
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import Resistance
from CIM.IEC61970.Domain import Length
from CIM.IEC61970.Domain import Temperature
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import KWActivePower
from CIM.IEC61970.Domain import Impedance
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import AngleDegrees



from enthought.traits.api import Instance, List, Property, Enum, Str, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of conductor usage.
ConductorUsageKind = Enum("secondary", "transmission", "other", "distribution", desc="Kind of conductor usage.")
# Kind of conductor material.
ConductorMaterialKind = Enum("aluminum", "steel", "other", "copper", "acsr", desc="Kind of conductor material.")
# Kind of cable outer jacket.
CableOuterJacketKind = Enum("linearLowDensityPolyethylene", "semiconducting", "none", "other", "pvc", "insulating", "polyethylene", desc="Kind of cable outer jacket.")
# Kind of cable construction.
CableConstructionKind = Enum("compacted", "sector", "segmental", "solid", "stranded", "other", "compressed", desc="Kind of cable construction.")
# Kind of cable shield material.
CableShieldMaterialKind = Enum("other", "aluminum", "steel", "lead", "copper", desc="Kind of cable shield material.")
# Usage for an asset model.
AssetModelUsageKind = Enum("distributionUnderground", "other", "streetlight", "customerSubstation", "unknown", "distributionOverhead", "substation", "transmission", desc="Usage for an asset model.")
# Kind of conductor insulation.
ConductorInsulationKind = Enum("highPressureFluidFilled", "lowCapacitanceRubber", "crosslinkedPolyethylene", "ozoneResistantRubber", "highMolecularWeightPolyethylene", "treeRetardantCrosslinkedPolyethylene", "oilPaper", "butyl", "beltedPilc", "rubber", "ethylenePropyleneRubber", "varnishedCambricCloth", "asbestosAndVarnishedCambric", "treeResistantHighMolecularWeightPolyethylene", "other", "siliconRubber", "unbeltedPilc", "varnishedDacronGlass", desc="Kind of conductor insulation.")
# Kind of corporate standard.
CorporateStandardKind = Enum("other", "underEvaluation", "experimental", "standard", desc="Kind of corporate standard.")

#------------------------------------------------------------------------------
#  "AssetModel" class:
#------------------------------------------------------------------------------

class AssetModel(Document):
    """ Documentation for a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ErpInventoryCounts = List(Instance("CIM.IEC61968.Informative.InfERPSupport.ErpInventoryCount"))

    # A type of asset may be satisified with many different types of asset models.
    TypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.TypeAsset",
        desc="A type of asset may be satisified with many different types of asset models.",
        transient=True,
        opposite="AssetModels",
        editor=InstanceEditor(name="_typeassets"))

    def _get_typeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.TypeAsset" ]
        else:
            return []

    _typeassets = Property(fget=_get_typeassets)

    AssetModelCatalogueItems = List(Instance("CIM.IEC61968.Informative.InfAssetModels.AssetModelCatalogueItem"))

    # Kind of corporate standard for this asset model.
    corporateStandardKind = CorporateStandardKind(desc="Kind of corporate standard for this asset model.")

    # Intended usage for this asset model.
    usageKind = AssetModelUsageKind(desc="Intended usage for this asset model.")

    # Manufacturer's model number.
    modelNumber = Str(desc="Manufacturer's model number.")

    # Total manufactured weight of asset.
    weightTotal = Weight(desc="Total manufactured weight of asset.")

    # Version number for product model, which indicates vintage of the product.
    modelVersion = Str(desc="Version number for product model, which indicates vintage of the product.")

    #--------------------------------------------------------------------------
    #  Begin "AssetModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.AssetModel",
        title="AssetModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AssetModel" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DistributionWindingTest" class:
#------------------------------------------------------------------------------

class DistributionWindingTest(IdentifiedObject):
    """ Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Winding that voltage or current is applied to during the test.
    FromWinding = Instance("CIM.IEC61968.AssetModels.WindingInfo",
        desc="Winding that voltage or current is applied to during the test.",
        transient=True,
        opposite="WindingTests",
        editor=InstanceEditor(name="_windinginfos"))

    def _get_windinginfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.WindingInfo" ]
        else:
            return []

    _windinginfos = Property(fget=_get_windinginfos)

    # Tap step number for the 'from' winding of the test pair.
    fromTapStep = Int(desc="Tap step number for the 'from' winding of the test pair.")

    #--------------------------------------------------------------------------
    #  Begin "DistributionWindingTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "fromTapStep",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "FromWinding",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.DistributionWindingTest",
        title="DistributionWindingTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DistributionWindingTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindingInfo" class:
#------------------------------------------------------------------------------

class WindingInfo(IdentifiedObject):
    """ Winding data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Transformer data that this winding description is part of.
    TransformerInfo = Instance("CIM.IEC61968.AssetModels.TransformerInfo",
        desc="Transformer data that this winding description is part of.",
        transient=True,
        opposite="WindingInfos",
        editor=InstanceEditor(name="_transformerinfos"))

    def _get_transformerinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.TransformerInfo" ]
        else:
            return []

    _transformerinfos = Property(fget=_get_transformerinfos)

    # All winding tests during which voltage or current was applied to this winding.
    WindingTests = List(Instance("CIM.IEC61968.AssetModels.DistributionWindingTest"),
        desc="All winding tests during which voltage or current was applied to this winding.")

    # All windings described by this winding data.
    Windings = List(Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding"),
        desc="All windings described by this winding data.")

    # Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
    ToWindingSpecs = List(Instance("CIM.IEC61968.AssetModels.ToWindingSpec"),
        desc="Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.")

    # Kind of connection of this winding.
    connectionKind = WindingConnection(desc="Kind of connection of this winding.")

    # Apparent power that this winding can carry for a short period of time.
    shortTermS = ApparentPower(desc="Apparent power that this winding can carry for a short period of time.")

    # Basic insulation level voltage rating.
    insulationU = Voltage(desc="Basic insulation level voltage rating.")

    # Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.
    sequenceNumber = Int(desc="Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.")

    # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.
    phaseAngle = Int(desc="Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.")

    # Apparent power that the winding can carry under emergency conditions.
    emergencyS = ApparentPower(desc="Apparent power that the winding can carry under emergency conditions.")

    # Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.
    ratedU = Voltage(desc="Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.")

    # DC resistance of this winding.
    r = Resistance(desc="DC resistance of this winding.")

    # Normal apparent power rating of this winding.
    ratedS = ApparentPower(desc="Normal apparent power rating of this winding.")

    #--------------------------------------------------------------------------
    #  Begin "WindingInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "connectionKind", "shortTermS", "insulationU", "sequenceNumber", "phaseAngle", "emergencyS", "ratedU", "r", "ratedS",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TransformerInfo", "WindingTests", "Windings", "ToWindingSpecs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.WindingInfo",
        title="WindingInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductorInfo" class:
#------------------------------------------------------------------------------

class ConductorInfo(IdentifiedObject):
    """ Conductor data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All conductor segments described by this conductor data.
    ConductorSegments = List(Instance("CIM.IEC61968.WiresExt.DistributionLineSegment"),
        desc="All conductor segments described by this conductor data.")

    ConductorAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.ConductorAssetModel",
        transient=True,
        opposite="ConductorInfo",
        editor=InstanceEditor(name="_conductorassetmodels"))

    def _get_conductorassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.ConductorAssetModel" ]
        else:
            return []

    _conductorassetmodels = Property(fget=_get_conductorassetmodels)

    # All wire arrangements (single wires) that make this conductor.
    WireArrangements = List(Instance("CIM.IEC61968.AssetModels.WireArrangement"),
        desc="All wire arrangements (single wires) that make this conductor.")

    # Usage of this conductor.
    usage = ConductorUsageKind(desc="Usage of this conductor.")

    # (if insulated conductor) Material used for insulation.
    insulationMaterial = ConductorInsulationKind(desc="(if insulated conductor) Material used for insulation.")

    # Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.
    phaseCount = Int(desc="Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.")

    # True if conductor is insulated.
    insulated = Bool(desc="True if conductor is insulated.")

    # (if insulated conductor) Thickness of the insulation.
    insulationThickness = Length(desc="(if insulated conductor) Thickness of the insulation.")

    #--------------------------------------------------------------------------
    #  Begin "ConductorInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "usage", "insulationMaterial", "phaseCount", "insulated", "insulationThickness",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorSegments", "ConductorAssetModel", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.ConductorInfo",
        title="ConductorInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductorInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireArrangement" class:
#------------------------------------------------------------------------------

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a Conductor, with reference to their type.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Wire type used for this wire arrangement.
    WireType = Instance("CIM.IEC61968.AssetModels.WireType",
        desc="Wire type used for this wire arrangement.",
        transient=True,
        opposite="WireArrangements",
        editor=InstanceEditor(name="_wiretypes"))

    def _get_wiretypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.WireType" ]
        else:
            return []

    _wiretypes = Property(fget=_get_wiretypes)

    # Conductor data this wire arrangement belongs to.
    ConductorInfo = Instance("CIM.IEC61968.AssetModels.ConductorInfo",
        desc="Conductor data this wire arrangement belongs to.",
        transient=True,
        opposite="WireArrangements",
        editor=InstanceEditor(name="_conductorinfos"))

    def _get_conductorinfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.ConductorInfo" ]
        else:
            return []

    _conductorinfos = Property(fget=_get_conductorinfos)

    # Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.
    position = Int(desc="Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.")

    # Height above ground of the first wire.
    mountingPointY = Length(desc="Height above ground of the first wire.")

    # Signed horizontal distance from the first wire to a common reference point.
    mountingPointX = Length(desc="Signed horizontal distance from the first wire to a common reference point.")

    #--------------------------------------------------------------------------
    #  Begin "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "position", "mountingPointY", "mountingPointX",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WireType", "ConductorInfo",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.WireArrangement",
        title="WireArrangement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireType" class:
#------------------------------------------------------------------------------

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All wire arrangements using this wire type.
    WireArrangements = List(Instance("CIM.IEC61968.AssetModels.WireArrangement"),
        desc="All wire arrangements using this wire type.")

    # All concentric neutral cables using this wire type.
    ConcentricNeutralCableInfos = List(Instance("CIM.IEC61968.AssetModels.ConcentricNeutralCableInfo"),
        desc="All concentric neutral cables using this wire type.")

    # Wire material.
    material = ConductorMaterialKind(desc="Wire material.")

    # Number of strands in the wire.
    strandCount = Int(desc="Number of strands in the wire.")

    # AC resistance per unit length of the conductor at 25 degrees C.
    rAC25 = Resistance(desc="AC resistance per unit length of the conductor at 25 degrees C.")

    # (if used) Number of strands in the steel core.
    coreStrandCount = Int(desc="(if used) Number of strands in the steel core.")

    # Current carrying capacity of the wire under stated thermal conditions.
    ratedCurrent = CurrentFlow(desc="Current carrying capacity of the wire under stated thermal conditions.")

    # Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).
    sizeDescription = Str(desc="Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).")

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gmr = Length(desc="Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.")

    # AC resistance per unit length of the conductor at 75 degrees C.
    rAC75 = Resistance(desc="AC resistance per unit length of the conductor at 75 degrees C.")

    # Outside radius of the wire.
    radius = Length(desc="Outside radius of the wire.")

    # DC resistance per unit length of the conductor at 20 degrees C.
    rDC20 = Resistance(desc="DC resistance per unit length of the conductor at 20 degrees C.")

    # AC resistance per unit length of the conductor at 50 degrees C.
    rAC50 = Resistance(desc="AC resistance per unit length of the conductor at 50 degrees C.")

    # (if there is a different core material) Radius of the central core.
    coreRadius = Length(desc="(if there is a different core material) Radius of the central core.")

    #--------------------------------------------------------------------------
    #  Begin "WireType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "material", "strandCount", "rAC25", "coreStrandCount", "ratedCurrent", "sizeDescription", "gmr", "rAC75", "radius", "rDC20", "rAC50", "coreRadius",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "WireArrangements", "ConcentricNeutralCableInfos",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.WireType",
        title="WireType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerInfo" class:
#------------------------------------------------------------------------------

class TransformerInfo(IdentifiedObject):
    """ Set of transformer data, from an equipment library.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All transformers that can be described with this transformer data.
    Transformers = List(Instance("CIM.IEC61968.WiresExt.DistributionTransformer"),
        desc="All transformers that can be described with this transformer data.")

    TransformerAssets = List(Instance("CIM.IEC61968.Informative.InfAssets.TransformerAsset"))

    # Data for all the windings described by this transformer data.
    WindingInfos = List(Instance("CIM.IEC61968.AssetModels.WindingInfo"),
        desc="Data for all the windings described by this transformer data.")

    TransformerAssetModels = List(Instance("CIM.IEC61968.Informative.InfAssetModels.TransformerAssetModel"))

    #--------------------------------------------------------------------------
    #  Begin "TransformerInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Transformers", "TransformerAssets", "WindingInfos", "TransformerAssetModels",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.TransformerInfo",
        title="TransformerInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ToWindingSpec" class:
#------------------------------------------------------------------------------

class ToWindingSpec(IdentifiedObject):
    """ For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All open-circuit tests in which this winding was measured.
    OpenCircuitTests = List(Instance("CIM.IEC61968.AssetModels.OpenCircuitTest"),
        desc="All open-circuit tests in which this winding was measured.")

    # All short-circuit tests in which this winding was short-circuited.
    ShortCircuitTests = List(Instance("CIM.IEC61968.AssetModels.ShortCircuitTest"),
        desc="All short-circuit tests in which this winding was short-circuited.")

    # Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
    ToWinding = Instance("CIM.IEC61968.AssetModels.WindingInfo",
        desc="Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.",
        transient=True,
        opposite="ToWindingSpecs",
        editor=InstanceEditor(name="_windinginfos"))

    def _get_windinginfos(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.WindingInfo" ]
        else:
            return []

    _windinginfos = Property(fget=_get_windinginfos)

    # (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage(desc="(if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    # Tap step number for the 'to' winding of the test pair.
    toTapStep = Int(desc="Tap step number for the 'to' winding of the test pair.")

    # (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = AngleDegrees(desc="(if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    #--------------------------------------------------------------------------
    #  Begin "ToWindingSpec" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "voltage", "toTapStep", "phaseShift",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OpenCircuitTests", "ShortCircuitTests", "ToWinding",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.ToWindingSpec",
        title="ToWindingSpec",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ToWindingSpec" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CableInfo" class:
#------------------------------------------------------------------------------

class CableInfo(ConductorInfo):
    """ Cable data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Kind of construction of this cable.
    constructionKind = CableConstructionKind(desc="Kind of construction of this cable.")

    # Material of the shield.
    shieldMaterial = CableShieldMaterialKind(desc="Material of the shield.")

    # Kind of outer jacket of this cable.
    outerJacketKind = CableOuterJacketKind(desc="Kind of outer jacket of this cable.")

    # Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.
    diameterOverCore = Length(desc="Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.")

    # True if wire strands are extruded in a way to fill the voids in the cable.
    isStrandFill = Bool(desc="True if wire strands are extruded in a way to fill the voids in the cable.")

    # Diameter over the insulating layer, excluding outer screen.
    diameterOverInsulation = Length(desc="Diameter over the insulating layer, excluding outer screen.")

    # Diameter over the outermost jacketing layer.
    diameterOverJacket = Length(desc="Diameter over the outermost jacketing layer.")

    # Maximum nominal design operating temperature.
    nominalTemperature = Temperature(desc="Maximum nominal design operating temperature.")

    # True if sheath / shield is used as a neutral (i.e., bonded).
    sheathAsNeutral = Bool(desc="True if sheath / shield is used as a neutral (i.e., bonded).")

    # Diameter over the outer screen; should be the shield's inside diameter..
    diameterOverScreen = Length(desc="Diameter over the outer screen; should be the shield's inside diameter..")

    #--------------------------------------------------------------------------
    #  Begin "CableInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "usage", "insulationMaterial", "phaseCount", "insulated", "insulationThickness", "constructionKind", "shieldMaterial", "outerJacketKind", "diameterOverCore", "isStrandFill", "diameterOverInsulation", "diameterOverJacket", "nominalTemperature", "sheathAsNeutral", "diameterOverScreen",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorSegments", "ConductorAssetModel", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.CableInfo",
        title="CableInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CableInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConcentricNeutralCableInfo" class:
#------------------------------------------------------------------------------

class ConcentricNeutralCableInfo(CableInfo):
    """ Concentric neutral cable data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Wire type used for this concentric neutral cable.
    WireType = Instance("CIM.IEC61968.AssetModels.WireType",
        desc="Wire type used for this concentric neutral cable.",
        transient=True,
        opposite="ConcentricNeutralCableInfos",
        editor=InstanceEditor(name="_wiretypes"))

    def _get_wiretypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.WireType" ]
        else:
            return []

    _wiretypes = Property(fget=_get_wiretypes)

    # Number of concentric neutral strands.
    neutralStrandCount = Int(desc="Number of concentric neutral strands.")

    # Diameter over the concentric neutral strands.
    diameterOverNeutral = Length(desc="Diameter over the concentric neutral strands.")

    #--------------------------------------------------------------------------
    #  Begin "ConcentricNeutralCableInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "usage", "insulationMaterial", "phaseCount", "insulated", "insulationThickness", "constructionKind", "shieldMaterial", "outerJacketKind", "diameterOverCore", "isStrandFill", "diameterOverInsulation", "diameterOverJacket", "nominalTemperature", "sheathAsNeutral", "diameterOverScreen", "neutralStrandCount", "diameterOverNeutral",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorSegments", "ConductorAssetModel", "WireArrangements", "WireType",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.ConcentricNeutralCableInfo",
        title="ConcentricNeutralCableInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConcentricNeutralCableInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShortCircuitTest" class:
#------------------------------------------------------------------------------

class ShortCircuitTest(DistributionWindingTest):
    """ Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All windings short-circuited during this test.
    ShortedWindingSpecs = List(Instance("CIM.IEC61968.AssetModels.ToWindingSpec"),
        desc="All windings short-circuited during this test.")

    # Load losses from a positive-sequence or single-phase short-circuit test.
    loadLoss = KWActivePower(desc="Load losses from a positive-sequence or single-phase short-circuit test.")

    # Load losses from a zero-sequence short-circuit test.
    loadLossZero = KWActivePower(desc="Load losses from a zero-sequence short-circuit test.")

    # Leakage impedance measured from a zero-sequence short-circuit test.
    leakageImpedanceZero = Impedance(desc="Leakage impedance measured from a zero-sequence short-circuit test.")

    # Leakage impedance measured from a positive-sequence or single-phase short-circuit test.
    leakageImpedance = Impedance(desc="Leakage impedance measured from a positive-sequence or single-phase short-circuit test.")

    #--------------------------------------------------------------------------
    #  Begin "ShortCircuitTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "fromTapStep", "loadLoss", "loadLossZero", "leakageImpedanceZero", "leakageImpedance",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "FromWinding", "ShortedWindingSpecs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.ShortCircuitTest",
        title="ShortCircuitTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShortCircuitTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OverheadConductorInfo" class:
#------------------------------------------------------------------------------

class OverheadConductorInfo(ConductorInfo):
    """ Overhead conductor data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # (if applicable) Insulation thickness of the neutral conductor.
    neutralInsulationThickness = Length(desc="(if applicable) Insulation thickness of the neutral conductor.")

    # Number of conductor strands in the symmetrical bundle (1-12).
    phaseConductorCount = Int(desc="Number of conductor strands in the symmetrical bundle (1-12).")

    # Distance between conductor strands in a symmetrical bundle.
    phaseConductorSpacing = Length(desc="Distance between conductor strands in a symmetrical bundle.")

    #--------------------------------------------------------------------------
    #  Begin "OverheadConductorInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "usage", "insulationMaterial", "phaseCount", "insulated", "insulationThickness", "neutralInsulationThickness", "phaseConductorCount", "phaseConductorSpacing",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorSegments", "ConductorAssetModel", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.OverheadConductorInfo",
        title="OverheadConductorInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OverheadConductorInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OpenCircuitTest" class:
#------------------------------------------------------------------------------

class OpenCircuitTest(DistributionWindingTest):
    """ Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All other windings measured during this test.
    MeasuredWindingSpecs = List(Instance("CIM.IEC61968.AssetModels.ToWindingSpec"),
        desc="All other windings measured during this test.")

    # Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.
    noLoadLoss = KWActivePower(desc="Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.")

    # Exciting current measured from a zero-sequence open-circuit (excitation) test.
    excitingCurrentZero = PerCent(desc="Exciting current measured from a zero-sequence open-circuit (excitation) test.")

    # Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.
    excitingCurrent = PerCent(desc="Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.")

    # Losses measured from a zero-sequence open-circuit (excitation) test.
    noLoadLossZero = KWActivePower(desc="Losses measured from a zero-sequence open-circuit (excitation) test.")

    #--------------------------------------------------------------------------
    #  Begin "OpenCircuitTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "fromTapStep", "noLoadLoss", "excitingCurrentZero", "excitingCurrent", "noLoadLossZero",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "FromWinding", "MeasuredWindingSpecs",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.OpenCircuitTest",
        title="OpenCircuitTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OpenCircuitTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapeShieldCableInfo" class:
#------------------------------------------------------------------------------

class TapeShieldCableInfo(CableInfo):
    """ Tape shield cable data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Thickness of the tape shield, before wrapping.
    tapeThickness = Length(desc="Thickness of the tape shield, before wrapping.")

    # Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.
    tapeLap = PerCent(desc="Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.")

    #--------------------------------------------------------------------------
    #  Begin "TapeShieldCableInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "usage", "insulationMaterial", "phaseCount", "insulated", "insulationThickness", "constructionKind", "shieldMaterial", "outerJacketKind", "diameterOverCore", "isStrandFill", "diameterOverInsulation", "diameterOverJacket", "nominalTemperature", "sheathAsNeutral", "diameterOverScreen", "tapeThickness", "tapeLap",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorSegments", "ConductorAssetModel", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.TapeShieldCableInfo",
        title="TapeShieldCableInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapeShieldCableInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EndDeviceModel" class:
#------------------------------------------------------------------------------

class EndDeviceModel(AssetModel):
    """ Documentation for particular end device product model made by a manufacturer.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EndDeviceTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.EndDeviceTypeAsset",
        transient=True,
        opposite="EndDeviceModels",
        editor=InstanceEditor(name="_enddevicetypeassets"))

    def _get_enddevicetypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.EndDeviceTypeAsset" ]
        else:
            return []

    _enddevicetypeassets = Property(fget=_get_enddevicetypeassets)

    # All end device assets being of this model.
    EndDeviceAssets = List(Instance("CIM.IEC61968.Metering.EndDeviceAsset"),
        desc="All end device assets being of this model.")

    #--------------------------------------------------------------------------
    #  Begin "EndDeviceModel" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "corporateStandardKind", "usageKind", "modelNumber", "weightTotal", "modelVersion",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "ErpInventoryCounts", "TypeAsset", "AssetModelCatalogueItems", "EndDeviceTypeAsset", "EndDeviceAssets",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.AssetModels.EndDeviceModel",
        title="EndDeviceModel",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EndDeviceModel" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
