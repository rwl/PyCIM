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

""" This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.This package is an extension of Assets package and contains the core information classes that support asset management and different network and work planning applications with specialized documentation classes describing assets of a particular product model made by a manufacturer. There are typically many instances of an asset associated with a single asset model. It also contains 'lightweight' *Info classes, which hold model attributes that can be referenced by not only Assets but also by ConductingEquipments.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CDPSM.IEC61970.Core import IdentifiedObject
from CDPSM.IEC61970.Domain import Voltage
from CDPSM.IEC61970.Domain import AngleDegrees
from CDPSM.IEC61970.Domain import Length
from CDPSM.IEC61970.Domain import Temperature
from CDPSM.IEC61970.Domain import KWActivePower
from CDPSM.IEC61970.Domain import PerCent
from CDPSM.IEC61970.Domain import Resistance
from CDPSM.IEC61970.Domain import CurrentFlow
from CDPSM.IEC61970.Domain import ApparentPower
from CDPSM.IEC61970.Wires import WindingConnection
from CDPSM.IEC61970.Domain import Impedance



from enthought.traits.api import Instance, List, Property, Enum, Int, Bool, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


CableOuterJacketKind = Enum("insulating", "other", "semiconducting", "polyethylene", "none", "linearLowDensityPolyethylene", "pvc")

CableShieldMaterialKind = Enum("other", "lead", "steel", "aluminum", "copper")

ConductorInsulationKind = Enum("crosslinkedPolyethylene", "butyl", "treeRetardantCrosslinkedPolyethylene", "asbestosAndVarnishedCambric", "highPressureFluidFilled", "ethylenePropyleneRubber", "ozoneResistantRubber", "oilPaper", "varnishedDacronGlass", "highMolecularWeightPolyethylene", "other", "varnishedCambricCloth", "treeResistantHighMolecularWeightPolyethylene", "unbeltedPilc", "beltedPilc", "rubber", "lowCapacitanceRubber", "siliconRubber")

ConductorMaterialKind = Enum("steel", "other", "aluminum", "copper", "acsr")

ConductorUsageKind = Enum("secondary", "other", "distribution", "transmission")

CableConstructionKind = Enum("solid", "stranded", "other", "segmental", "compacted", "sector", "compressed")

#------------------------------------------------------------------------------
#  "TransformerInfo" class:
#------------------------------------------------------------------------------

class TransformerInfo(IdentifiedObject):
    """ Set of transformer data, from an equipment library.Set of transformer data, from an equipment library.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All transformers that can be described with this transformer data.All transformers that can be described with this transformer data.
    Transformers = List(Instance("CDPSM.IEC61968.WiresExt.DistributionTransformer"),
        desc="All transformers that can be described with this transformer data.All transformers that can be described with this transformer data.")

    # Data for all the windings described by this transformer data.Data for all the windings described by this transformer data.
    WindingInfos = List(Instance("CDPSM.IEC61968.AssetModels.WindingInfo"),
        desc="Data for all the windings described by this transformer data.Data for all the windings described by this transformer data.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "Transformers", "WindingInfos",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.TransformerInfo",
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
    """ For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All open-circuit tests in which this winding was measured.All open-circuit tests in which this winding was measured.
    OpenCircuitTests = List(Instance("CDPSM.IEC61968.AssetModels.OpenCircuitTest"),
        desc="All open-circuit tests in which this winding was measured.All open-circuit tests in which this winding was measured.")

    # All short-circuit tests in which this winding was short-circuited.All short-circuit tests in which this winding was short-circuited.
    ShortCircuitTests = List(Instance("CDPSM.IEC61968.AssetModels.ShortCircuitTest"),
        desc="All short-circuit tests in which this winding was short-circuited.All short-circuit tests in which this winding was short-circuited.")

    # Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.
    ToWinding = Instance("CDPSM.IEC61968.AssetModels.WindingInfo", allow_none=False,
        desc="Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.Winding short-circuited in a short-circuit test, or measured for induced voltage and angle in an open-circuit test.",
        transient=True,
        opposite="ToWindingSpecs",
        editor=InstanceEditor(name="_windinginfos"))

    def _get_windinginfos(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.AssetModels.WindingInfo" ]
        else:
            return []

    _windinginfos = Property(fget=_get_windinginfos)

    # Tap step number for the 'to' winding of the test pair.Tap step number for the 'to' winding of the test pair.
    toTapStep = Int(desc="Tap step number for the 'to' winding of the test pair.Tap step number for the 'to' winding of the test pair.")

    # (if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage(desc="(if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    # (if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = AngleDegrees(desc="(if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.(if open-circuit test) Phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    #--------------------------------------------------------------------------
    #  Begin "ToWindingSpec" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "toTapStep", "voltage", "phaseShift",
                label="Attributes"),
            VGroup("Model", "OpenCircuitTests", "ShortCircuitTests", "ToWinding",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.ToWindingSpec",
        title="ToWindingSpec",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ToWindingSpec" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireArrangement" class:
#------------------------------------------------------------------------------

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a Conductor, with reference to their type.Identification, spacing and configuration of the wires of a Conductor, with reference to their type.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Conductor data this wire arrangement belongs to.Conductor data this wire arrangement belongs to.
    ConductorInfo = Instance("CDPSM.IEC61968.AssetModels.ConductorInfo",
        desc="Conductor data this wire arrangement belongs to.Conductor data this wire arrangement belongs to.",
        transient=True,
        opposite="WireArrangements",
        editor=InstanceEditor(name="_conductorinfos"))

    def _get_conductorinfos(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.AssetModels.ConductorInfo" ]
        else:
            return []

    _conductorinfos = Property(fget=_get_conductorinfos)

    # Wire type used for this wire arrangement.Wire type used for this wire arrangement.
    WireType = Instance("CDPSM.IEC61968.AssetModels.WireType", allow_none=False,
        desc="Wire type used for this wire arrangement.Wire type used for this wire arrangement.",
        transient=True,
        opposite="WireArrangements",
        editor=InstanceEditor(name="_wiretypes"))

    def _get_wiretypes(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.AssetModels.WireType" ]
        else:
            return []

    _wiretypes = Property(fget=_get_wiretypes)

    # Signed horizontal distance from the first wire to a common reference point.Signed horizontal distance from the first wire to a common reference point.
    mountingPointX = Length(desc="Signed horizontal distance from the first wire to a common reference point.Signed horizontal distance from the first wire to a common reference point.")

    # Height above ground of the first wire.Height above ground of the first wire.
    mountingPointY = Length(desc="Height above ground of the first wire.Height above ground of the first wire.")

    # Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.
    position = Int(desc="Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.Position number on the structure corresponding to this wire. For example, use 1..3 for phases and 4 for the neutral on a 3-phase structure. The individual phase assignments matter; for example, ABC will produce a different set of unbalanced line parameters, by phase, than BAC.")

    #--------------------------------------------------------------------------
    #  Begin "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "mountingPointX", "mountingPointY", "position",
                label="Attributes"),
            VGroup("Model", "ConductorInfo", "WireType",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.WireArrangement",
        title="WireArrangement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductorInfo" class:
#------------------------------------------------------------------------------

class ConductorInfo(IdentifiedObject):
    """ Conductor data.Conductor data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All wire arrangements (single wires) that make this conductor.All wire arrangements (single wires) that make this conductor.
    WireArrangements = List(Instance("CDPSM.IEC61968.AssetModels.WireArrangement"),
        desc="All wire arrangements (single wires) that make this conductor.All wire arrangements (single wires) that make this conductor.")

    # All conductor segments described by this conductor data.All conductor segments described by this conductor data.
    ConductorSegments = List(Instance("CDPSM.IEC61968.WiresExt.DistributionLineSegment"),
        desc="All conductor segments described by this conductor data.All conductor segments described by this conductor data.")

    # Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.
    phaseCount = Int(desc="Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.Number of phases (including neutral) to be retained. Any wires beyond this number should be reduced into the earth return.")

    # (if insulated conductor) Material used for insulation.(if insulated conductor) Material used for insulation.
    insulationMaterial = ConductorInsulationKind(desc="(if insulated conductor) Material used for insulation.(if insulated conductor) Material used for insulation.")

    # (if insulated conductor) Thickness of the insulation.(if insulated conductor) Thickness of the insulation.
    insulationThickness = Length(desc="(if insulated conductor) Thickness of the insulation.(if insulated conductor) Thickness of the insulation.")

    # True if conductor is insulated.True if conductor is insulated.
    insulated = Bool(desc="True if conductor is insulated.True if conductor is insulated.")

    # Usage of this conductor.Usage of this conductor.
    usage = ConductorUsageKind(desc="Usage of this conductor.Usage of this conductor.")

    #--------------------------------------------------------------------------
    #  Begin "ConductorInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "phaseCount", "insulationMaterial", "insulationThickness", "insulated", "usage",
                label="Attributes"),
            VGroup("Model", "WireArrangements", "ConductorSegments",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.ConductorInfo",
        title="ConductorInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductorInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DistributionWindingTest" class:
#------------------------------------------------------------------------------

class DistributionWindingTest(IdentifiedObject):
    """ Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Winding that voltage or current is applied to during the test.Winding that voltage or current is applied to during the test.
    FromWinding = Instance("CDPSM.IEC61968.AssetModels.WindingInfo", allow_none=False,
        desc="Winding that voltage or current is applied to during the test.Winding that voltage or current is applied to during the test.",
        transient=True,
        opposite="WindingTests",
        editor=InstanceEditor(name="_windinginfos"))

    def _get_windinginfos(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.AssetModels.WindingInfo" ]
        else:
            return []

    _windinginfos = Property(fget=_get_windinginfos)

    # Tap step number for the 'from' winding of the test pair.Tap step number for the 'from' winding of the test pair.
    fromTapStep = Int(desc="Tap step number for the 'from' winding of the test pair.Tap step number for the 'from' winding of the test pair.")

    #--------------------------------------------------------------------------
    #  Begin "DistributionWindingTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "fromTapStep",
                label="Attributes"),
            VGroup("Model", "FromWinding",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.DistributionWindingTest",
        title="DistributionWindingTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DistributionWindingTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireType" class:
#------------------------------------------------------------------------------

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All concentric neutral cables using this wire type.All concentric neutral cables using this wire type.
    ConcentricNeutralCableInfos = List(Instance("CDPSM.IEC61968.AssetModels.ConcentricNeutralCableInfo"),
        desc="All concentric neutral cables using this wire type.All concentric neutral cables using this wire type.")

    # All wire arrangements using this wire type.All wire arrangements using this wire type.
    WireArrangements = List(Instance("CDPSM.IEC61968.AssetModels.WireArrangement"),
        desc="All wire arrangements using this wire type.All wire arrangements using this wire type.")

    # AC resistance per unit length of the conductor at 75 degrees C.AC resistance per unit length of the conductor at 75 degrees C.
    rAC75 = Resistance(desc="AC resistance per unit length of the conductor at 75 degrees C.AC resistance per unit length of the conductor at 75 degrees C.")

    # (if there is a different core material) Radius of the central core.(if there is a different core material) Radius of the central core.
    coreRadius = Length(desc="(if there is a different core material) Radius of the central core.(if there is a different core material) Radius of the central core.")

    # (if used) Number of strands in the steel core.(if used) Number of strands in the steel core.
    coreStrandCount = Int(desc="(if used) Number of strands in the steel core.(if used) Number of strands in the steel core.")

    # AC resistance per unit length of the conductor at 25 degrees C.AC resistance per unit length of the conductor at 25 degrees C.
    rAC25 = Resistance(desc="AC resistance per unit length of the conductor at 25 degrees C.AC resistance per unit length of the conductor at 25 degrees C.")

    # Outside radius of the wire.Outside radius of the wire.
    radius = Length(desc="Outside radius of the wire.Outside radius of the wire.")

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gmr = Length(desc="Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.")

    # DC resistance per unit length of the conductor at 20 degrees C.DC resistance per unit length of the conductor at 20 degrees C.
    rDC20 = Resistance(desc="DC resistance per unit length of the conductor at 20 degrees C.DC resistance per unit length of the conductor at 20 degrees C.")

    # AC resistance per unit length of the conductor at 50 degrees C.AC resistance per unit length of the conductor at 50 degrees C.
    rAC50 = Resistance(desc="AC resistance per unit length of the conductor at 50 degrees C.AC resistance per unit length of the conductor at 50 degrees C.")

    # Wire material.Wire material.
    material = ConductorMaterialKind(desc="Wire material.Wire material.")

    # Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).
    sizeDescription = Str(desc="Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).Describes the wire guage or cross section (e.g., 4/0, #2, 336.5).")

    # Number of strands in the wire.Number of strands in the wire.
    strandCount = Int(desc="Number of strands in the wire.Number of strands in the wire.")

    # Current carrying capacity of the wire under stated thermal conditions.Current carrying capacity of the wire under stated thermal conditions.
    ratedCurrent = CurrentFlow(desc="Current carrying capacity of the wire under stated thermal conditions.Current carrying capacity of the wire under stated thermal conditions.")

    #--------------------------------------------------------------------------
    #  Begin "WireType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "rAC75", "coreRadius", "coreStrandCount", "rAC25", "radius", "gmr", "rDC20", "rAC50", "material", "sizeDescription", "strandCount", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("Model", "ConcentricNeutralCableInfos", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.WireType",
        title="WireType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindingInfo" class:
#------------------------------------------------------------------------------

class WindingInfo(IdentifiedObject):
    """ Winding data.Winding data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All winding tests during which voltage or current was applied to this winding.All winding tests during which voltage or current was applied to this winding.
    WindingTests = List(Instance("CDPSM.IEC61968.AssetModels.DistributionWindingTest"),
        desc="All winding tests during which voltage or current was applied to this winding.All winding tests during which voltage or current was applied to this winding.")

    # Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.
    ToWindingSpecs = List(Instance("CDPSM.IEC61968.AssetModels.ToWindingSpec"),
        desc="Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.")

    # Transformer data that this winding description is part of.Transformer data that this winding description is part of.
    TransformerInfo = Instance("CDPSM.IEC61968.AssetModels.TransformerInfo",
        desc="Transformer data that this winding description is part of.Transformer data that this winding description is part of.",
        transient=True,
        opposite="WindingInfos",
        editor=InstanceEditor(name="_transformerinfos"))

    def _get_transformerinfos(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.AssetModels.TransformerInfo" ]
        else:
            return []

    _transformerinfos = Property(fget=_get_transformerinfos)

    # All windings described by this winding data.All windings described by this winding data.
    Windings = List(Instance("CDPSM.IEC61968.WiresExt.DistributionTransformerWinding"),
        desc="All windings described by this winding data.All windings described by this winding data.")

    # Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.
    sequenceNumber = Int(desc="Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.Sequence number for this winding, corresponding to the winding's order in the TransformerBank.vectorGroup attribute. Highest voltage winding should be '1'.")

    # Normal apparent power rating of this winding.Normal apparent power rating of this winding.
    ratedS = ApparentPower(desc="Normal apparent power rating of this winding.Normal apparent power rating of this winding.")

    # Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.
    ratedU = Voltage(desc="Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.Rated voltage of this winding: phase-phase for three-phase windings, and either phase-phase or phase-neutral for single-phase windings.")

    # Kind of connection of this winding.Kind of connection of this winding.
    connectionKind = WindingConnection(desc="Kind of connection of this winding.Kind of connection of this winding.")

    # Apparent power that the winding can carry under emergency conditions.Apparent power that the winding can carry under emergency conditions.
    emergencyS = ApparentPower(desc="Apparent power that the winding can carry under emergency conditions.Apparent power that the winding can carry under emergency conditions.")

    # DC resistance of this winding.DC resistance of this winding.
    r = Resistance(desc="DC resistance of this winding.DC resistance of this winding.")

    # Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.
    phaseAngle = Int(desc="Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.Winding phase angle where 360 degrees are represented with clock hours, so the valid values are {0, ..., 11}. For example, to express winding code 'Dyn11', set attributes as follows: 'connectionKind' = Yn and 'phaseAngle' = 11.")

    # Basic insulation level voltage rating.Basic insulation level voltage rating.
    insulationU = Voltage(desc="Basic insulation level voltage rating.Basic insulation level voltage rating.")

    # Apparent power that this winding can carry for a short period of time.Apparent power that this winding can carry for a short period of time.
    shortTermS = ApparentPower(desc="Apparent power that this winding can carry for a short period of time.Apparent power that this winding can carry for a short period of time.")

    #--------------------------------------------------------------------------
    #  Begin "WindingInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "sequenceNumber", "ratedS", "ratedU", "connectionKind", "emergencyS", "r", "phaseAngle", "insulationU", "shortTermS",
                label="Attributes", columns=1),
            VGroup("Model", "WindingTests", "ToWindingSpecs", "TransformerInfo", "Windings",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.WindingInfo",
        title="WindingInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CableInfo" class:
#------------------------------------------------------------------------------

class CableInfo(ConductorInfo):
    """ Cable data.Cable data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Maximum nominal design operating temperature.Maximum nominal design operating temperature.
    nominalTemperature = Temperature(desc="Maximum nominal design operating temperature.Maximum nominal design operating temperature.")

    # Diameter over the outer screen; should be the shield's inside diameter..Diameter over the outer screen; should be the shield's inside diameter..
    diameterOverScreen = Length(desc="Diameter over the outer screen; should be the shield's inside diameter..Diameter over the outer screen; should be the shield's inside diameter..")

    # True if sheath / shield is used as a neutral (i.e., bonded).True if sheath / shield is used as a neutral (i.e., bonded).
    sheathAsNeutral = Bool(desc="True if sheath / shield is used as a neutral (i.e., bonded).True if sheath / shield is used as a neutral (i.e., bonded).")

    # Diameter over the outermost jacketing layer.Diameter over the outermost jacketing layer.
    diameterOverJacket = Length(desc="Diameter over the outermost jacketing layer.Diameter over the outermost jacketing layer.")

    # Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.
    diameterOverCore = Length(desc="Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.Diameter over the core, including any semi-con screen; should be the insulating layer's inside diameter.")

    # Kind of construction of this cable.Kind of construction of this cable.
    constructionKind = CableConstructionKind(desc="Kind of construction of this cable.Kind of construction of this cable.")

    # Kind of outer jacket of this cable.Kind of outer jacket of this cable.
    outerJacketKind = CableOuterJacketKind(desc="Kind of outer jacket of this cable.Kind of outer jacket of this cable.")

    # True if wire strands are extruded in a way to fill the voids in the cable.True if wire strands are extruded in a way to fill the voids in the cable.
    isStrandFill = Bool(desc="True if wire strands are extruded in a way to fill the voids in the cable.True if wire strands are extruded in a way to fill the voids in the cable.")

    # Material of the shield.Material of the shield.
    shieldMaterial = CableShieldMaterialKind(desc="Material of the shield.Material of the shield.")

    # Diameter over the insulating layer, excluding outer screen.Diameter over the insulating layer, excluding outer screen.
    diameterOverInsulation = Length(desc="Diameter over the insulating layer, excluding outer screen.Diameter over the insulating layer, excluding outer screen.")

    #--------------------------------------------------------------------------
    #  Begin "CableInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "phaseCount", "insulationMaterial", "insulationThickness", "insulated", "usage", "nominalTemperature", "diameterOverScreen", "sheathAsNeutral", "diameterOverJacket", "diameterOverCore", "constructionKind", "outerJacketKind", "isStrandFill", "shieldMaterial", "diameterOverInsulation",
                label="Attributes", columns=1),
            VGroup("Model", "WireArrangements", "ConductorSegments",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.CableInfo",
        title="CableInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CableInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OpenCircuitTest" class:
#------------------------------------------------------------------------------

class OpenCircuitTest(DistributionWindingTest):
    """ Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All other windings measured during this test.All other windings measured during this test.
    MeasuredWindingSpecs = List(Instance("CDPSM.IEC61968.AssetModels.ToWindingSpec"),
        desc="All other windings measured during this test.All other windings measured during this test.")

    # Losses measured from a zero-sequence open-circuit (excitation) test.Losses measured from a zero-sequence open-circuit (excitation) test.
    noLoadLossZero = KWActivePower(desc="Losses measured from a zero-sequence open-circuit (excitation) test.Losses measured from a zero-sequence open-circuit (excitation) test.")

    # Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.
    noLoadLoss = KWActivePower(desc="Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.Losses measured from a positive-sequence or single-phase open-circuit (excitation) test.")

    # Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.
    excitingCurrent = PerCent(desc="Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.Exciting current measured from a positive-sequence or single-phase open-circuit (excitation) test.")

    # Exciting current measured from a zero-sequence open-circuit (excitation) test.Exciting current measured from a zero-sequence open-circuit (excitation) test.
    excitingCurrentZero = PerCent(desc="Exciting current measured from a zero-sequence open-circuit (excitation) test.Exciting current measured from a zero-sequence open-circuit (excitation) test.")

    #--------------------------------------------------------------------------
    #  Begin "OpenCircuitTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "fromTapStep", "noLoadLossZero", "noLoadLoss", "excitingCurrent", "excitingCurrentZero",
                label="Attributes"),
            VGroup("Model", "FromWinding", "MeasuredWindingSpecs",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.OpenCircuitTest",
        title="OpenCircuitTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OpenCircuitTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConcentricNeutralCableInfo" class:
#------------------------------------------------------------------------------

class ConcentricNeutralCableInfo(CableInfo):
    """ Concentric neutral cable data.Concentric neutral cable data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Wire type used for this concentric neutral cable.Wire type used for this concentric neutral cable.
    WireType = Instance("CDPSM.IEC61968.AssetModels.WireType", allow_none=False,
        desc="Wire type used for this concentric neutral cable.Wire type used for this concentric neutral cable.",
        transient=True,
        opposite="ConcentricNeutralCableInfos",
        editor=InstanceEditor(name="_wiretypes"))

    def _get_wiretypes(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.AssetModels.WireType" ]
        else:
            return []

    _wiretypes = Property(fget=_get_wiretypes)

    # Number of concentric neutral strands.Number of concentric neutral strands.
    neutralStrandCount = Int(desc="Number of concentric neutral strands.Number of concentric neutral strands.")

    # Diameter over the concentric neutral strands.Diameter over the concentric neutral strands.
    diameterOverNeutral = Length(desc="Diameter over the concentric neutral strands.Diameter over the concentric neutral strands.")

    #--------------------------------------------------------------------------
    #  Begin "ConcentricNeutralCableInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "phaseCount", "insulationMaterial", "insulationThickness", "insulated", "usage", "nominalTemperature", "diameterOverScreen", "sheathAsNeutral", "diameterOverJacket", "diameterOverCore", "constructionKind", "outerJacketKind", "isStrandFill", "shieldMaterial", "diameterOverInsulation", "neutralStrandCount", "diameterOverNeutral",
                label="Attributes", columns=1),
            VGroup("Model", "WireArrangements", "ConductorSegments", "WireType",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.ConcentricNeutralCableInfo",
        title="ConcentricNeutralCableInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConcentricNeutralCableInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OverheadConductorInfo" class:
#------------------------------------------------------------------------------

class OverheadConductorInfo(ConductorInfo):
    """ Overhead conductor data.Overhead conductor data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # (if applicable) Insulation thickness of the neutral conductor.(if applicable) Insulation thickness of the neutral conductor.
    neutralInsulationThickness = Length(desc="(if applicable) Insulation thickness of the neutral conductor.(if applicable) Insulation thickness of the neutral conductor.")

    # Number of conductor strands in the symmetrical bundle (1-12).Number of conductor strands in the symmetrical bundle (1-12).
    phaseConductorCount = Int(desc="Number of conductor strands in the symmetrical bundle (1-12).Number of conductor strands in the symmetrical bundle (1-12).")

    # Distance between conductor strands in a symmetrical bundle.Distance between conductor strands in a symmetrical bundle.
    phaseConductorSpacing = Length(desc="Distance between conductor strands in a symmetrical bundle.Distance between conductor strands in a symmetrical bundle.")

    #--------------------------------------------------------------------------
    #  Begin "OverheadConductorInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "phaseCount", "insulationMaterial", "insulationThickness", "insulated", "usage", "neutralInsulationThickness", "phaseConductorCount", "phaseConductorSpacing",
                label="Attributes", columns=1),
            VGroup("Model", "WireArrangements", "ConductorSegments",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.OverheadConductorInfo",
        title="OverheadConductorInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OverheadConductorInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapeShieldCableInfo" class:
#------------------------------------------------------------------------------

class TapeShieldCableInfo(CableInfo):
    """ Tape shield cable data.Tape shield cable data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Thickness of the tape shield, before wrapping.Thickness of the tape shield, before wrapping.
    tapeThickness = Length(desc="Thickness of the tape shield, before wrapping.Thickness of the tape shield, before wrapping.")

    # Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.
    tapeLap = PerCent(desc="Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.Percentage of the tape shield width that overlaps in each wrap, typically 10% to 25%.")

    #--------------------------------------------------------------------------
    #  Begin "TapeShieldCableInfo" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "phaseCount", "insulationMaterial", "insulationThickness", "insulated", "usage", "nominalTemperature", "diameterOverScreen", "sheathAsNeutral", "diameterOverJacket", "diameterOverCore", "constructionKind", "outerJacketKind", "isStrandFill", "shieldMaterial", "diameterOverInsulation", "tapeThickness", "tapeLap",
                label="Attributes", columns=1),
            VGroup("Model", "WireArrangements", "ConductorSegments",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.TapeShieldCableInfo",
        title="TapeShieldCableInfo",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapeShieldCableInfo" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShortCircuitTest" class:
#------------------------------------------------------------------------------

class ShortCircuitTest(DistributionWindingTest):
    """ Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All windings short-circuited during this test.All windings short-circuited during this test.
    ShortedWindingSpecs = List(Instance("CDPSM.IEC61968.AssetModels.ToWindingSpec"),
        desc="All windings short-circuited during this test.All windings short-circuited during this test.")

    # Load losses from a zero-sequence short-circuit test.Load losses from a zero-sequence short-circuit test.
    loadLossZero = KWActivePower(desc="Load losses from a zero-sequence short-circuit test.Load losses from a zero-sequence short-circuit test.")

    # Leakage impedance measured from a zero-sequence short-circuit test.Leakage impedance measured from a zero-sequence short-circuit test.
    leakageImpedanceZero = Impedance(desc="Leakage impedance measured from a zero-sequence short-circuit test.Leakage impedance measured from a zero-sequence short-circuit test.")

    # Leakage impedance measured from a positive-sequence or single-phase short-circuit test.Leakage impedance measured from a positive-sequence or single-phase short-circuit test.
    leakageImpedance = Impedance(desc="Leakage impedance measured from a positive-sequence or single-phase short-circuit test.Leakage impedance measured from a positive-sequence or single-phase short-circuit test.")

    # Load losses from a positive-sequence or single-phase short-circuit test.Load losses from a positive-sequence or single-phase short-circuit test.
    loadLoss = KWActivePower(desc="Load losses from a positive-sequence or single-phase short-circuit test.Load losses from a positive-sequence or single-phase short-circuit test.")

    #--------------------------------------------------------------------------
    #  Begin "ShortCircuitTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "fromTapStep", "loadLossZero", "leakageImpedanceZero", "leakageImpedance", "loadLoss",
                label="Attributes"),
            VGroup("Model", "FromWinding", "ShortedWindingSpecs",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61968.AssetModels.ShortCircuitTest",
        title="ShortCircuitTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShortCircuitTest" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
