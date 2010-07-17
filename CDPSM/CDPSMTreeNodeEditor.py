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

""" Defines TreeNodes interface for the model.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Str, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group, TreeEditor, TreeNode

from enthought.traits.ui.menu \
    import Action, Menu

from CDPSM import *
from CDPSM.IEC61968 import *
from CDPSM.IEC61970 import *
from CDPSM.IEC61968.WiresExt import *
from CDPSM.IEC61968.AssetModels import *
from CDPSM.IEC61968.Common import *
from CDPSM.IEC61970.Wires import *
from CDPSM.IEC61970.Core import *
from CDPSM.IEC61970.Generation import *
from CDPSM.IEC61970.LoadModel import *
from CDPSM.IEC61970.StateVariables import *
from CDPSM.IEC61970.Topology import *
from CDPSM.IEC61970.Domain import *
from CDPSM.IEC61970.Generation.Production import *

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------
# <<< constants
# @generated
IMAGE_PATH = ""
# >>> constants

#------------------------------------------------------------------------------
#  Tree nodes:
#------------------------------------------------------------------------------

Element_TreeNode = TreeNode(
    node_for=[Element],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Model_TreeNode = TreeNode(
    node_for=[Model],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Model_Elements_TreeNode = TreeNode(
    node_for=[Model],
    children="Elements",
    label="=Elements",
    tooltip="",
    add=[Element],
    move=[Element],
    icon_path=IMAGE_PATH)

DistributionTransformerWinding_TreeNode = TreeNode(
    node_for=[DistributionTransformerWinding],
    label="name",
    tooltip="Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.Conducting connection point of a distribution / unbalanced transformer winding instance. This class differs from Wires::TransformerWinding as follows: - the eight Pi model attributes are moved into separate class, that can be optionally referred to from several winding instances. - the three grounding attributes can differ per winding instance, even for windings that use the same TransformerInfo, so they are kept on DistributionTransformerWinding. 'sequenceNumber' attribute replaces 'windingType' attribute.  All the other attributes come from the WindingInfo (and its relationships). TransformerInfo is associated to the DistributionTransformer as referenceable data, so it can be defined once and referred to from instances, instead of being specified with each instance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DistributionLineSegment_TreeNode = TreeNode(
    node_for=[DistributionLineSegment],
    label="name",
    tooltip="Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.At least one of the Associations must exist.Extends ACLineSegment with references to a library of standard types from which electrical parameters can be calculated, as follows: - calculate electrical parameters from asset data, using associated ConductorInfo, with values then multiplied by Conductor.length to produce a matrix model. - calculate unbalanced electrical parameters from associated PerLengthPhaseImpedance, then multiplied by Conductor.length to produce a matrix model. - calculate transposed electrical parameters from associated PerLengthSequenceImpedance, then multiplied by Conductor.length to produce a sequence model. For symmetrical, transposed 3ph lines, it is sufficient to use inherited ACLineSegment attributes, which describe sequence impedances and admittances for the entire length of the segment.  Known issue: Attributes expressing impedances and admittances in PerLengthSequenceImpedance and PhaseImpedanceData use Resistance, etc., which describe pre-calculated, full length of segment, while we should have a longitudinal unit, per length. Taking 'r' as example, its 'unit'=Ohm, but the value is effectively in Ohm/m, so the value needs to be multiplied by Conductor.length. This is against the whole idea of unit data types and is semantically wrong, but base CIM does not have the required data types at this moment. Until the revision of unit modelling in CIM, applications need to deduce and locally handle appending '/m' for units and ensure they multiply the values by Conductor.length.At least one of the Associations must exist.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindingPiImpedance_TreeNode = TreeNode(
    node_for=[WindingPiImpedance],
    label="name",
    tooltip="Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WindingPiImpedance_Windings_TreeNode = TreeNode(
    node_for=[WindingPiImpedance],
    children="Windings",
    label="=Windings",
    tooltip="All windings having this Pi impedance.All windings having this Pi impedance.",
    add=[DistributionTransformerWinding],
    move=[DistributionTransformerWinding],
    icon_path=IMAGE_PATH)

DistributionTapChanger_TreeNode = TreeNode(
    node_for=[DistributionTapChanger],
    label="name",
    tooltip="Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.Additional ratio tap changer parameters common to distribution line regulators. 'tculControlMode' would always be 'volt'. If 'monitoredPhase' is not specified, then if the controlled DistributionTransformerWinding is single-phase, the PT primary is assumed to be connected across that winding, which is the normal case. If the controlled winding is three-phase, then the 'monitoredPhase' is assumed to be 'AN', unless otherwise specified. Whenever 'ctRatio' and 'ptRatio' are specified, it's customary to specify the R and X in 'volts' referred to the PT secondary circuit, otherwise R and X are in feeder primary ohms. If 'ptRatio' is not specified, then 'targetVoltage', 'limitVoltage', and 'bandVoltage' are on the feeder primary base, phase-neutral or phase-phase depending on the 'monitoredPhase'. Otherwise, these attributes are all on the PT secondary base.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PerLengthSequenceImpedance_TreeNode = TreeNode(
    node_for=[PerLengthSequenceImpedance],
    label="name",
    tooltip="Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.Sequence impedance and admittance parameters per unit length, for transposed lines of 1, 2, or 3 phases. For 1-phase lines, define x=x0=xself. For 2-phase lines, define x=xs-xm and x0=xs+xm.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PerLengthSequenceImpedance_ConductorSegments_TreeNode = TreeNode(
    node_for=[PerLengthSequenceImpedance],
    children="ConductorSegments",
    label="=ConductorSegments",
    tooltip="All conductor segments described by this sequence impedance.All conductor segments described by this sequence impedance.",
    add=[DistributionLineSegment],
    move=[DistributionLineSegment],
    icon_path=IMAGE_PATH)

TransformerBank_TreeNode = TreeNode(
    node_for=[TransformerBank],
    label="name",
    tooltip="An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.An assembly of transformers that are connected together. For three-phase transformers, there would be one transformer per bank. For banks of single-phase transformers, there will be more than one transformer per bank, and they need not be identical.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerBank_Transformers_TreeNode = TreeNode(
    node_for=[TransformerBank],
    children="Transformers",
    label="=Transformers",
    tooltip="All transformers that belong to this bank.All transformers that belong to this bank.",
    add=[DistributionTransformer],
    move=[DistributionTransformer],
    icon_path=IMAGE_PATH)

PerLengthPhaseImpedance_TreeNode = TreeNode(
    node_for=[PerLengthPhaseImpedance],
    label="name",
    tooltip="Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.Impedance and admittance parameters per unit length for n-wire unbalanced lines, in matrix form.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PerLengthPhaseImpedance_PhaseImpedanceData_TreeNode = TreeNode(
    node_for=[PerLengthPhaseImpedance],
    children="PhaseImpedanceData",
    label="=PhaseImpedanceData",
    tooltip="All data that belong to this conductor phase impedance.All data that belong to this conductor phase impedance.",
    add=[PhaseImpedanceData],
    move=[PhaseImpedanceData],
    icon_path=IMAGE_PATH)
PerLengthPhaseImpedance_ConductorSegments_TreeNode = TreeNode(
    node_for=[PerLengthPhaseImpedance],
    children="ConductorSegments",
    label="=ConductorSegments",
    tooltip="All conductor segments described by this phase impedance.All conductor segments described by this phase impedance.",
    add=[DistributionLineSegment],
    move=[DistributionLineSegment],
    icon_path=IMAGE_PATH)

DistributionTransformer_TreeNode = TreeNode(
    node_for=[DistributionTransformer],
    label="name",
    tooltip="An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.An assembly of two or more coupled windings that transform electrical power between voltage levels. Supports both balanced and unbalanced winding connections. This class differs from Wires::PowerTransformer as follows: - it is part of a TransformerBank - it draws parameters exclusively from TransformerInfo and its associated classes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DistributionTransformer_Windings_TreeNode = TreeNode(
    node_for=[DistributionTransformer],
    children="Windings",
    label="=Windings",
    tooltip="All windings of this transformer.All windings of this transformer.",
    add=[DistributionTransformerWinding],
    move=[DistributionTransformerWinding],
    icon_path=IMAGE_PATH)

PhaseImpedanceData_TreeNode = TreeNode(
    node_for=[PhaseImpedanceData],
        tooltip="Triplet of resistance, reactance, and susceptance matrix element values.Triplet of resistance, reactance, and susceptance matrix element values.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerInfo_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    label="name",
    tooltip="Set of transformer data, from an equipment library.Set of transformer data, from an equipment library.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerInfo_Transformers_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    children="Transformers",
    label="=Transformers",
    tooltip="All transformers that can be described with this transformer data.All transformers that can be described with this transformer data.",
    add=[DistributionTransformer],
    move=[DistributionTransformer],
    icon_path=IMAGE_PATH)
TransformerInfo_WindingInfos_TreeNode = TreeNode(
    node_for=[TransformerInfo],
    children="WindingInfos",
    label="=WindingInfos",
    tooltip="Data for all the windings described by this transformer data.Data for all the windings described by this transformer data.",
    add=[WindingInfo],
    move=[WindingInfo],
    icon_path=IMAGE_PATH)

ToWindingSpec_TreeNode = TreeNode(
    node_for=[ToWindingSpec],
    label="name",
    tooltip="For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.For short-circuit tests, specifies the winding and tap for all short-circuited windings.  For open-circuit tests, specifies the winding, tap, induced voltage, and induced angle for any non-excited windings that were measured during the test. This won't apply if only the exciting current and no-load losses were measured.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ToWindingSpec_OpenCircuitTests_TreeNode = TreeNode(
    node_for=[ToWindingSpec],
    children="OpenCircuitTests",
    label="=OpenCircuitTests",
    tooltip="All open-circuit tests in which this winding was measured.All open-circuit tests in which this winding was measured.",
    add=[OpenCircuitTest],
    move=[OpenCircuitTest],
    icon_path=IMAGE_PATH)
ToWindingSpec_ShortCircuitTests_TreeNode = TreeNode(
    node_for=[ToWindingSpec],
    children="ShortCircuitTests",
    label="=ShortCircuitTests",
    tooltip="All short-circuit tests in which this winding was short-circuited.All short-circuit tests in which this winding was short-circuited.",
    add=[ShortCircuitTest],
    move=[ShortCircuitTest],
    icon_path=IMAGE_PATH)

WireArrangement_TreeNode = TreeNode(
    node_for=[WireArrangement],
    label="name",
    tooltip="Identification, spacing and configuration of the wires of a Conductor, with reference to their type.Identification, spacing and configuration of the wires of a Conductor, with reference to their type.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CableInfo_TreeNode = TreeNode(
    node_for=[CableInfo],
    label="name",
    tooltip="Cable data.Cable data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OpenCircuitTest_TreeNode = TreeNode(
    node_for=[OpenCircuitTest],
    label="name",
    tooltip="Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. For induced voltage and phase shifts, use the associated ToWindingSpec class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OpenCircuitTest_MeasuredWindingSpecs_TreeNode = TreeNode(
    node_for=[OpenCircuitTest],
    children="MeasuredWindingSpecs",
    label="=MeasuredWindingSpecs",
    tooltip="All other windings measured during this test.All other windings measured during this test.",
    add=[ToWindingSpec],
    move=[ToWindingSpec],
    icon_path=IMAGE_PATH)

ConcentricNeutralCableInfo_TreeNode = TreeNode(
    node_for=[ConcentricNeutralCableInfo],
    label="name",
    tooltip="Concentric neutral cable data.Concentric neutral cable data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConductorInfo_TreeNode = TreeNode(
    node_for=[ConductorInfo],
    label="name",
    tooltip="Conductor data.Conductor data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductorInfo_WireArrangements_TreeNode = TreeNode(
    node_for=[ConductorInfo],
    children="WireArrangements",
    label="=WireArrangements",
    tooltip="All wire arrangements (single wires) that make this conductor.All wire arrangements (single wires) that make this conductor.",
    add=[WireArrangement],
    move=[WireArrangement],
    icon_path=IMAGE_PATH)
ConductorInfo_ConductorSegments_TreeNode = TreeNode(
    node_for=[ConductorInfo],
    children="ConductorSegments",
    label="=ConductorSegments",
    tooltip="All conductor segments described by this conductor data.All conductor segments described by this conductor data.",
    add=[DistributionLineSegment],
    move=[DistributionLineSegment],
    icon_path=IMAGE_PATH)

DistributionWindingTest_TreeNode = TreeNode(
    node_for=[DistributionWindingTest],
    label="name",
    tooltip="Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.Test results for one or more transformer windings. These may include short-circuit or open-circuit (excitation) tests. Short-circuit test results include load losses and leakage impedances. Open-circuit test results may include no-load losses, exciting current, phase shifts, and induced voltage. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WireType_TreeNode = TreeNode(
    node_for=[WireType],
    label="name",
    tooltip="Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WireType_ConcentricNeutralCableInfos_TreeNode = TreeNode(
    node_for=[WireType],
    children="ConcentricNeutralCableInfos",
    label="=ConcentricNeutralCableInfos",
    tooltip="All concentric neutral cables using this wire type.All concentric neutral cables using this wire type.",
    add=[ConcentricNeutralCableInfo],
    move=[ConcentricNeutralCableInfo],
    icon_path=IMAGE_PATH)
WireType_WireArrangements_TreeNode = TreeNode(
    node_for=[WireType],
    children="WireArrangements",
    label="=WireArrangements",
    tooltip="All wire arrangements using this wire type.All wire arrangements using this wire type.",
    add=[WireArrangement],
    move=[WireArrangement],
    icon_path=IMAGE_PATH)

WindingInfo_TreeNode = TreeNode(
    node_for=[WindingInfo],
    label="name",
    tooltip="Winding data.Winding data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WindingInfo_WindingTests_TreeNode = TreeNode(
    node_for=[WindingInfo],
    children="WindingTests",
    label="=WindingTests",
    tooltip="All winding tests during which voltage or current was applied to this winding.All winding tests during which voltage or current was applied to this winding.",
    add=[DistributionWindingTest],
    move=[DistributionWindingTest],
    icon_path=IMAGE_PATH)
WindingInfo_ToWindingSpecs_TreeNode = TreeNode(
    node_for=[WindingInfo],
    children="ToWindingSpecs",
    label="=ToWindingSpecs",
    tooltip="Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.Tap steps and induced voltage/angle measurements for tests in which this winding was not excited.",
    add=[ToWindingSpec],
    move=[ToWindingSpec],
    icon_path=IMAGE_PATH)
WindingInfo_Windings_TreeNode = TreeNode(
    node_for=[WindingInfo],
    children="Windings",
    label="=Windings",
    tooltip="All windings described by this winding data.All windings described by this winding data.",
    add=[DistributionTransformerWinding],
    move=[DistributionTransformerWinding],
    icon_path=IMAGE_PATH)

OverheadConductorInfo_TreeNode = TreeNode(
    node_for=[OverheadConductorInfo],
    label="name",
    tooltip="Overhead conductor data.Overhead conductor data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TapeShieldCableInfo_TreeNode = TreeNode(
    node_for=[TapeShieldCableInfo],
    label="name",
    tooltip="Tape shield cable data.Tape shield cable data.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ShortCircuitTest_TreeNode = TreeNode(
    node_for=[ShortCircuitTest],
    label="name",
    tooltip="Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.Short-circuit test results include load losses and leakage impedances. For three-phase windings, the excitation can be positive sequence (the default) or zero sequence. There must be at least one short-circuited ('to') winding.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ShortCircuitTest_ShortedWindingSpecs_TreeNode = TreeNode(
    node_for=[ShortCircuitTest],
    children="ShortedWindingSpecs",
    label="=ShortedWindingSpecs",
    tooltip="All windings short-circuited during this test.All windings short-circuited during this test.",
    add=[ToWindingSpec],
    move=[ToWindingSpec],
    icon_path=IMAGE_PATH)

GeoLocation_TreeNode = TreeNode(
    node_for=[GeoLocation],
    label="name",
    tooltip="Geographical location.Geographical location.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeoLocation_PowerSystemResources_TreeNode = TreeNode(
    node_for=[GeoLocation],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="All power system resources at this geographical location.All power system resources at this geographical location.",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

Location_TreeNode = TreeNode(
    node_for=[Location],
    label="name",
    tooltip="The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.The place, scene, or point of something where someone or something has been, is, and/or will be at a given moment in time. It may be: - Spatial location of an actual or planned structure, or a set of point-oriented structures (as a substation, structure, building, town, etc.) or diagram objects, which may be defined as a point or polygon, or, - Path of an underground or overhead conductor, or a linear diagram object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Location_PositionPoints_TreeNode = TreeNode(
    node_for=[Location],
    children="PositionPoints",
    label="=PositionPoints",
    tooltip="Sequence of position points describing this location.Sequence of position points describing this location.",
    add=[PositionPoint],
    move=[PositionPoint],
    icon_path=IMAGE_PATH)

PositionPoint_TreeNode = TreeNode(
    node_for=[PositionPoint],
        tooltip="Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.Set of spatial coordinates that determine a point. A sequence of PositionPoints can be used to describe: - physical location of non-point oriented objects like cables or lines, or - area of an object like a substation, a geographical zone or a diagram object.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IEC61970CIMVersion_TreeNode = TreeNode(
    node_for=[IEC61970CIMVersion],
        tooltip="This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusbarSection_TreeNode = TreeNode(
    node_for=[BusbarSection],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadBreakSwitch_TreeNode = TreeNode(
    node_for=[LoadBreakSwitch],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TapChanger_TreeNode = TreeNode(
    node_for=[TapChanger],
    label="name",
    tooltip="Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Fuse_TreeNode = TreeNode(
    node_for=[Fuse],
    label="name",
    tooltip="An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Junction_TreeNode = TreeNode(
    node_for=[Junction],
    label="name",
    tooltip="A point where one or more conducting equipments are connected with zero resistance.A point where one or more conducting equipments are connected with zero resistance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ACLineSegment_TreeNode = TreeNode(
    node_for=[ACLineSegment],
    label="name",
    tooltip="A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Disconnector_TreeNode = TreeNode(
    node_for=[Disconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnergySource_TreeNode = TreeNode(
    node_for=[EnergySource],
    label="name",
    tooltip="A generic equivalent for an energy supplier on a transmission or distribution voltage level.A generic equivalent for an energy supplier on a transmission or distribution voltage level.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SynchronousMachine_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    label="name",
    tooltip="An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RatioTapChanger_TreeNode = TreeNode(
    node_for=[RatioTapChanger],
    label="name",
    tooltip="A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnergyConsumer_TreeNode = TreeNode(
    node_for=[EnergyConsumer],
    label="name",
    tooltip="Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Switch_TreeNode = TreeNode(
    node_for=[Switch],
    label="name",
    tooltip="A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Line_TreeNode = TreeNode(
    node_for=[Line],
    label="name",
    tooltip="A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ShuntCompensator_TreeNode = TreeNode(
    node_for=[ShuntCompensator],
    label="name",
    tooltip="A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Breaker_TreeNode = TreeNode(
    node_for=[Breaker],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Conductor_TreeNode = TreeNode(
    node_for=[Conductor],
    label="name",
    tooltip="Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConnectivityNodeContainer_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    label="name",
    tooltip="A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNodeContainer_ConnectivityNodes_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    children="ConnectivityNodes",
    label="=ConnectivityNodes",
    tooltip="Connectivity nodes contained by this container.Connectivity nodes contained by this container.",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

VoltageLevel_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    label="name",
    tooltip="A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

VoltageLevel_Bays_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    children="Bays",
    label="=Bays",
    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
    add=[Bay],
    move=[Bay],
    icon_path=IMAGE_PATH)

Bay_TreeNode = TreeNode(
    node_for=[Bay],
    label="name",
    tooltip="A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Equipment_TreeNode = TreeNode(
    node_for=[Equipment],
    label="name",
    tooltip="The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BaseVoltage_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    label="name",
    tooltip="Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BaseVoltage_ConductingEquipment_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="ConductingEquipment",
    label="=ConductingEquipment",
    tooltip="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.",
    add=[ConductingEquipment],
    move=[ConductingEquipment],
    icon_path=IMAGE_PATH)
BaseVoltage_VoltageLevel_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="VoltageLevel",
    label="=VoltageLevel",
    tooltip="The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.",
    add=[VoltageLevel],
    move=[VoltageLevel],
    icon_path=IMAGE_PATH)

PSRType_TreeNode = TreeNode(
    node_for=[PSRType],
    label="name",
    tooltip="Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PSRType_PowerSystemResources_TreeNode = TreeNode(
    node_for=[PSRType],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="Power system resources classified with this PSRType.Power system resources classified with this PSRType.",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

EquipmentContainer_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    label="name",
    tooltip="A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EquipmentContainer_Equipments_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    children="Equipments",
    label="=Equipments",
    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
    add=[Equipment],
    move=[Equipment],
    icon_path=IMAGE_PATH)

IdentifiedObject_TreeNode = TreeNode(
    node_for=[IdentifiedObject],
    label="name",
    tooltip="This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Substation_TreeNode = TreeNode(
    node_for=[Substation],
    label="name",
    tooltip="A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Substation_VoltageLevels_TreeNode = TreeNode(
    node_for=[Substation],
    children="VoltageLevels",
    label="=VoltageLevels",
    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
    add=[VoltageLevel],
    move=[VoltageLevel],
    icon_path=IMAGE_PATH)

ConductingEquipment_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    label="name",
    tooltip="The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductingEquipment_Terminals_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="Terminals",
    label="=Terminals",
    tooltip="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)

SubGeographicalRegion_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    label="name",
    tooltip="A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SubGeographicalRegion_Lines_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    children="Lines",
    label="=Lines",
    tooltip="A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.",
    add=[Line],
    move=[Line],
    icon_path=IMAGE_PATH)
SubGeographicalRegion_Substations_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    children="Substations",
    label="=Substations",
    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
    add=[Substation],
    move=[Substation],
    icon_path=IMAGE_PATH)

Terminal_TreeNode = TreeNode(
    node_for=[Terminal],
    label="name",
    tooltip="An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeographicalRegion_TreeNode = TreeNode(
    node_for=[GeographicalRegion],
    label="name",
    tooltip="A geographical region of a power system network model.A geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeographicalRegion_Regions_TreeNode = TreeNode(
    node_for=[GeographicalRegion],
    children="Regions",
    label="=Regions",
    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.",
    add=[SubGeographicalRegion],
    move=[SubGeographicalRegion],
    icon_path=IMAGE_PATH)

PowerSystemResource_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    label="name",
    tooltip="A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    label="name",
    tooltip="A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeneratingUnit_SynchronousMachines_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="SynchronousMachines",
    label="=SynchronousMachines",
    tooltip="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)

LoadResponseCharacteristic_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    label="name",
    tooltip="Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.  If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used as to calculate:  Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent  Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage)** cim:LoadResponseCharacteristic.qVoltageExponent  Where  * means 'multiply' and ** is 'raised to power of'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadResponseCharacteristic_EnergyConsumer_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    children="EnergyConsumer",
    label="=EnergyConsumer",
    tooltip="The set of loads that have the response characteristics.The set of loads that have the response characteristics.",
    add=[EnergyConsumer],
    move=[EnergyConsumer],
    icon_path=IMAGE_PATH)

SvTapStep_TreeNode = TreeNode(
    node_for=[SvTapStep],
        tooltip="State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.State variable for transformer tap step.     This class is to be used for taps of LTC (load tap changing) transformers, not fixed tap transformers.  Normally a profile specifies only one of the attributes 'position'or 'tapRatio'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConnectivityNode_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    label="name",
    tooltip="Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNode_Terminals_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    children="Terminals",
    label="=Terminals",
    tooltip="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)


#------------------------------------------------------------------------------
#  Tree node list:
#------------------------------------------------------------------------------


tree_nodes = [
    Element_TreeNode,
    Model_TreeNode,
    Model_Elements_TreeNode,
    PhaseImpedanceData_TreeNode,
    PositionPoint_TreeNode,
    IEC61970CIMVersion_TreeNode,
    IdentifiedObject_TreeNode,
    SubGeographicalRegion_TreeNode,
    SubGeographicalRegion_Lines_TreeNode,
    SubGeographicalRegion_Substations_TreeNode,
    Terminal_TreeNode,
    GeographicalRegion_TreeNode,
    GeographicalRegion_Regions_TreeNode,
    PowerSystemResource_TreeNode,
    LoadResponseCharacteristic_TreeNode,
    LoadResponseCharacteristic_EnergyConsumer_TreeNode,
    SvTapStep_TreeNode,
    ConnectivityNode_TreeNode,
    ConnectivityNode_Terminals_TreeNode,
    WindingPiImpedance_TreeNode,
    WindingPiImpedance_Windings_TreeNode,
    PerLengthSequenceImpedance_TreeNode,
    PerLengthSequenceImpedance_ConductorSegments_TreeNode,
    PerLengthPhaseImpedance_TreeNode,
    PerLengthPhaseImpedance_PhaseImpedanceData_TreeNode,
    PerLengthPhaseImpedance_ConductorSegments_TreeNode,
    TransformerInfo_TreeNode,
    TransformerInfo_Transformers_TreeNode,
    TransformerInfo_WindingInfos_TreeNode,
    ToWindingSpec_TreeNode,
    ToWindingSpec_OpenCircuitTests_TreeNode,
    ToWindingSpec_ShortCircuitTests_TreeNode,
    WireArrangement_TreeNode,
    ConductorInfo_TreeNode,
    ConductorInfo_WireArrangements_TreeNode,
    ConductorInfo_ConductorSegments_TreeNode,
    DistributionWindingTest_TreeNode,
    WireType_TreeNode,
    WireType_ConcentricNeutralCableInfos_TreeNode,
    WireType_WireArrangements_TreeNode,
    WindingInfo_TreeNode,
    WindingInfo_WindingTests_TreeNode,
    WindingInfo_ToWindingSpecs_TreeNode,
    WindingInfo_Windings_TreeNode,
    OverheadConductorInfo_TreeNode,
    ShortCircuitTest_TreeNode,
    ShortCircuitTest_ShortedWindingSpecs_TreeNode,
    Location_TreeNode,
    Location_PositionPoints_TreeNode,
    TapChanger_TreeNode,
    ACLineSegment_TreeNode,
    RatioTapChanger_TreeNode,
    ConnectivityNodeContainer_TreeNode,
    ConnectivityNodeContainer_ConnectivityNodes_TreeNode,
    Equipment_TreeNode,
    BaseVoltage_TreeNode,
    BaseVoltage_ConductingEquipment_TreeNode,
    BaseVoltage_VoltageLevel_TreeNode,
    PSRType_TreeNode,
    PSRType_PowerSystemResources_TreeNode,
    EquipmentContainer_TreeNode,
    EquipmentContainer_Equipments_TreeNode,
    Substation_TreeNode,
    Substation_VoltageLevels_TreeNode,
    ConductingEquipment_TreeNode,
    ConductingEquipment_Terminals_TreeNode,
    GeneratingUnit_TreeNode,
    GeneratingUnit_SynchronousMachines_TreeNode,
    DistributionTransformerWinding_TreeNode,
    DistributionLineSegment_TreeNode,
    DistributionTapChanger_TreeNode,
    TransformerBank_TreeNode,
    TransformerBank_Transformers_TreeNode,
    DistributionTransformer_TreeNode,
    DistributionTransformer_Windings_TreeNode,
    CableInfo_TreeNode,
    OpenCircuitTest_TreeNode,
    OpenCircuitTest_MeasuredWindingSpecs_TreeNode,
    ConcentricNeutralCableInfo_TreeNode,
    TapeShieldCableInfo_TreeNode,
    GeoLocation_TreeNode,
    GeoLocation_PowerSystemResources_TreeNode,
    BusbarSection_TreeNode,
    Junction_TreeNode,
    EnergySource_TreeNode,
    SynchronousMachine_TreeNode,
    EnergyConsumer_TreeNode,
    Switch_TreeNode,
    Line_TreeNode,
    ShuntCompensator_TreeNode,
    Breaker_TreeNode,
    Conductor_TreeNode,
    VoltageLevel_TreeNode,
    VoltageLevel_Bays_TreeNode,
    Bay_TreeNode,
    LoadBreakSwitch_TreeNode,
    Fuse_TreeNode,
    Disconnector_TreeNode,
]
tree_nodes.reverse()

#------------------------------------------------------------------------------
#  CDPSM Tree Editor:
#------------------------------------------------------------------------------

CDPSMTreeEditor = TreeEditor(nodes=tree_nodes, editable=True)

#------------------------------------------------------------------------------
#  Begin "CDPSMTreeEditor" user region:
#------------------------------------------------------------------------------
# @generated
class TreeRoot(HasTraits):

    # Root element of the model tree.
    root = Instance(HasTraits)

    # Traits view to display.
    view = View(
        Item('root',
            editor=CDPSMTreeEditor,
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True,
        buttons   = ["OK", "Cancel"]
    )

#------------------------------------------------------------------------------
#  End "CDPSMTreeEditor" user region:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    root = TreeRoot()
    root.configure_traits()

# EOF -------------------------------------------------------------------------
