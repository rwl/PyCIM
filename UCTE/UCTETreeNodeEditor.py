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

from UCTE import *
from UCTE.StateVariables import *
from UCTE.Core import *
from UCTE.ControlArea import *
from UCTE.Generation import *
from UCTE.LoadModel import *
from UCTE.Topology import *
from UCTE.Equivalents import *
from UCTE.Domain import *
from UCTE.Wires import *
from UCTE.OperationalLimits import *
from UCTE.Generation.Production import *

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


IEC61970CIMVersion_TreeNode = TreeNode(
    node_for=[IEC61970CIMVersion],
        tooltip="This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.This is the IEC 61970 CIM version number assigned to this UML model file.This is the UCTE profile.     We have been using file naming conventions, the profile namespace, and comments here in the profile under IEC61970CIMVersion class.  Profile1_v9 - dated 2009-01-27   - removed SeriesCompensator and ApparentPowerLimit, added TopologicalNode.equivalent  Profile1_v10 - dated 2009-01-29  - documentation added on Terminal.sequenceNumber.  Added notes to GeneratingUnit.normalPF attribute in profile.  Profile1_v11 - dated 2009-02-04  - Made optional SynchronousMachine.InitialReactiveCapabilityCurve, minQ, maxQ.    Rename of SvTapStep.tapRatio to SvTapStep.continuousPosition.   Multiplicity for SvShuntCompensatorSections.continuousSections made manditory.   Removed SvShuntCompensatorSections.sections and SvTapStep.position from profile.  Profile 1_v12 - dated 2009-03-17 - Made all Short Circuit classes and Attributes Optional, made all voltage dependency / coeficient model attributes Optional, added notes from the UCTE Mapping Spreadsheet and added a few clarification notes.  Profile 1_v13 - dated 2009-03-19 - Made the GeneratingUnit.maximumAllowableSpinningReserve Optional and made all of the PhaseTapChanger attributes Optional.  Profile 1_v14 - dated 2009-05-10 - Added some comments to classes based on input from IOP test and added BusBarSection and Line Classes.",
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

SvVoltage_TreeNode = TreeNode(
    node_for=[SvVoltage],
        tooltip="State variable for voltage.State variable for voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvShuntCompensatorSections_TreeNode = TreeNode(
    node_for=[SvShuntCompensatorSections],
        tooltip="State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.State variable for the number of sections in service for a shunt compensator.A SvShuntCompensator is always associated with any instance of ShuntCompensator.   The sections or continuousSections values are specified depending upon the value of the associated RegulatingControl.discrete attribute.  If no RegulatingControl is associated, then the ShuntCompensator is treated as discrete.    In discrete mode, the 'sections' attribute must be present.   In the not 'discrete' mode (continuous mode) the 'continuousSections' attribute must be present.     In the case the Terminal.connected value is 'false' the specificed number of sections is not meaningful to the powerflow solution and powerflow implementations should interpret this as zero injection.   Note that an SvShuntCompensatorSections should be supplied even for ShuntCompensators whose Terminal.connected status is 'false' to keep total number of ShuntCompensator and SvShuntCompensatorSection objects in the model the same.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StateVariable_TreeNode = TreeNode(
    node_for=[StateVariable],
        tooltip="An abstract class for state variables.An abstract class for state variables.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvTapStep_TreeNode = TreeNode(
    node_for=[SvTapStep],
        tooltip="State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.State variable for transformer tap step.     Normally a profile specifies only one of the attributes 'position'or 'continuousPosition'.SvTapStep is only meant to be used for taps that change under load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SvPowerFlow_TreeNode = TreeNode(
    node_for=[SvPowerFlow],
        tooltip="State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.State variable for power flow.Only Terminal instances of EnergyConsumer and SynchronousMachine will have SvPowerFlow instances assigned.   The number of SvPowerFlow instances in the model should match the number EnergyConsumer plus SynchronousMachine objects in the model regardless of the Terminal.connected values.    Any SvPowerFlow with a Terminal.connected value of false must have zero flow explicitly specified on an SvPowerFlow instance. The other types of terminals are not included in exchanges since their values can be readily computed from local voltages and attributes without a global powerflow solution.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Curve_TreeNode = TreeNode(
    node_for=[Curve],
    label="name",
    tooltip="Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Curve_CurveScheduleDatas_TreeNode = TreeNode(
    node_for=[Curve],
    children="CurveScheduleDatas",
    label="=CurveScheduleDatas",
    tooltip="The point data values that define a curveThe point data values that define a curve",
    add=[CurveData],
    move=[CurveData],
    icon_path=IMAGE_PATH)

ConnectivityNodeContainer_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    label="name",
    tooltip="A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.The TopologicalNode will normally belong only to a VoltageLevel instance within a Substation.   All instances of TopologicalNode that are not X-nodes will require an association to a containing VoltageLevel instance.  The BaseVoltage of the VoltageLevel should match that of the TopologicalNode itself. A TopologicalNode object used for an X-node will not be contained, thus this association is specified as optional in the profile. The TopologicalNode will normally belong only to a VoltageLevel within a Substation. In the case of X-nodes, the TopologicalNode is not contained.    ",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNodeContainer_TopologicalNode_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="The topological nodes which belong to this connectivity node container.The topological nodes which belong to this connectivity node container.",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

VoltageLevel_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    label="name",
    tooltip="A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.",
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
    tooltip="Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.The profile requires a BaseVoltage associaton on ConductingEquipment subtypes of classes ACLineSegment and TransformerWinding. The association is not used for any other subtypes. The base voltage of the TopologicalNode should match the BaseVoltage of the containing VoltageLevel if such a containing VoltageLevel is specified.",
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
BaseVoltage_TopologicalNode_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="The topological nodes at the base voltage.The topological nodes at the base voltage.",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

EquipmentContainer_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    label="name",
    tooltip="A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. A modeling construct to provide a root class for all Equipment classesFor a TransformerWinding the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer Association. For a TransformerWinding and ACLineSegment, the association Equipment.MemberOf_EquipmentContainer is not used.  The TransformerWinding instance is instead contained within a PowerTransformer unless the association refers to a different substation than what is used in the PowerTransformer association. ",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EquipmentContainer_Contains_Equipments_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    children="Contains_Equipments",
    label="=Contains_Equipments",
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

Substation_Contains_VoltageLevels_TreeNode = TreeNode(
    node_for=[Substation],
    children="Contains_VoltageLevels",
    label="=Contains_VoltageLevels",
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
    tooltip="An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.The SvPowerFlow is only associated with the Terminal objects of shunt injection classes such as EnergyConsumer and SynchronousMachine.   The flows at any ShuntCompensator can always be computed from connected voltage magnitude, number of sections and local attributes.  Branch flows are not exchanged since they can be readily be computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal. The SvPowerFlow is only associated with the Terminal objects of shunt injection classes EnergyConsumer and  SynchronousMachine.  Branch flows are not exchanged since they can be readily computed from the voltages, impedances, and for transformers additionally the tap parameters including the SvTapStep.  Similarly, Switch flows are not included because they can typically be uniquely computed, except in the case of meshed networks of Switch objects.  Terminals of the ShuntCompensator class are not associated because the injection value can be computed from the solved voltage, number of sections, Termianl.connected state, and the impedance per section attributes on the ShuntCompensator. ",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Terminal_HasFirst_MutualCoupling_TreeNode = TreeNode(
    node_for=[Terminal],
    children="HasFirst_MutualCoupling",
    label="=HasFirst_MutualCoupling",
    tooltip="Mutual couplings associated with the branch as the first branch.Mutual couplings associated with the branch as the first branch.",
    add=[MutualCoupling],
    move=[MutualCoupling],
    icon_path=IMAGE_PATH)
Terminal_OperationalLimitSet_TreeNode = TreeNode(
    node_for=[Terminal],
    children="OperationalLimitSet",
    label="=OperationalLimitSet",
    tooltip="The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.The operatinal limits sets that applie specifically to this terminal.  Other operational limits sets may apply to this terminal through the association to Equipment.",
    add=[OperationalLimitSet],
    move=[OperationalLimitSet],
    icon_path=IMAGE_PATH)
Terminal_RegulatingControl_TreeNode = TreeNode(
    node_for=[Terminal],
    children="RegulatingControl",
    label="=RegulatingControl",
    tooltip="The terminal is regulated by a control.The terminal is regulated by a control.",
    add=[RegulatingControl],
    move=[RegulatingControl],
    icon_path=IMAGE_PATH)
Terminal_TieFlow_TreeNode = TreeNode(
    node_for=[Terminal],
    children="TieFlow",
    label="=TieFlow",
    tooltip="The control area tie flows to which this terminal associates.The control area tie flows to which this terminal associates.",
    add=[TieFlow],
    move=[TieFlow],
    icon_path=IMAGE_PATH)
Terminal_HasSecond_MutualCoupling_TreeNode = TreeNode(
    node_for=[Terminal],
    children="HasSecond_MutualCoupling",
    label="=HasSecond_MutualCoupling",
    tooltip="Mutual couplings with the branch associated as the first branch.Mutual couplings with the branch associated as the first branch.",
    add=[MutualCoupling],
    move=[MutualCoupling],
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

CurveData_TreeNode = TreeNode(
    node_for=[CurveData],
        tooltip="Data point values for defining a curve or scheduleData point values for defining a curve or schedule",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ControlArea_TreeNode = TreeNode(
    node_for=[ControlArea],
    label="name",
    tooltip="A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlArea_TopologicalNode_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="The topological nodes included in the control area.The topological nodes included in the control area.",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)
ControlArea_TieFlow_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="TieFlow",
    label="=TieFlow",
    tooltip="The tie flows associated with the control area.The tie flows associated with the control area.",
    add=[TieFlow],
    move=[TieFlow],
    icon_path=IMAGE_PATH)
ControlArea_ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="ControlAreaGeneratingUnit",
    label="=ControlAreaGeneratingUnit",
    tooltip="The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.",
    add=[ControlAreaGeneratingUnit],
    move=[ControlAreaGeneratingUnit],
    icon_path=IMAGE_PATH)

ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[ControlAreaGeneratingUnit],
        tooltip="A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TieFlow_TreeNode = TreeNode(
    node_for=[TieFlow],
        tooltip="A flow specification in terms of location and direction for a control area.A flow specification in terms of location and direction for a control area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindGeneratingUnit_TreeNode = TreeNode(
    node_for=[WindGeneratingUnit],
    label="name",
    tooltip="A wind driven generating unit.A wind driven generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    label="name",
    tooltip="A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.One GeneratingUnit or its subtype is to be modeled for each SynchronousMachine.     In case the type of generating unit (such as hydro, coal, nuclear, ...) is not well known the GeneratingUnit class may be used as a concrete class in the exchange.  If the type is well known, then an appropriate subtype of GeneratingUnit such as HydroGeneratingUnit should be used in the exchange file. Each SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeneratingUnit_Contains_SynchronousMachines_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="Contains_SynchronousMachines",
    label="=Contains_SynchronousMachines",
    tooltip="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)
GeneratingUnit_ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="ControlAreaGeneratingUnit",
    label="=ControlAreaGeneratingUnit",
    tooltip="ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.",
    add=[ControlAreaGeneratingUnit],
    move=[ControlAreaGeneratingUnit],
    icon_path=IMAGE_PATH)

FossilFuel_TreeNode = TreeNode(
    node_for=[FossilFuel],
    label="name",
    tooltip="The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gasThe UCTE profile allows only one type of fuel per ThermalGeneratingUnit. The UCTE profile allows only one type of fuel per ThermalGeneratingUnit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NuclearGeneratingUnit_TreeNode = TreeNode(
    node_for=[NuclearGeneratingUnit],
    label="name",
    tooltip="A nuclear generating unit.A nuclear generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroGeneratingUnit_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ThermalGeneratingUnit_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroPump_TreeNode = TreeNode(
    node_for=[HydroPump],
    label="name",
    tooltip="A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.A synchronous motor-driven pump, typically associated with a pumped storage plantA HydroPump is included in the profile to indicate the associated SynchronousMachine can run in pump mode.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadResponseCharacteristic_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    label="name",
    tooltip="Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.",
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

TopologicalNode_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    label="name",
    tooltip="A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TopologicalNode_Terminal_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    children="Terminal",
    label="=Terminal",
    tooltip="The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.The terminals associated with the topological node.   This can be used as an alternative to the connectivity node path to terminal, thus making it unneccesary to model connedtivity nodes in some cases.   Note that the if connectivity nodes are in the model, this association would proably not be used.",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)

TopologicalIsland_TreeNode = TreeNode(
    node_for=[TopologicalIsland],
    label="name",
    tooltip="An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TopologicalIsland_TopologicalNodes_TreeNode = TreeNode(
    node_for=[TopologicalIsland],
    children="TopologicalNodes",
    label="=TopologicalNodes",
    tooltip="A topological node belongs to a topological islandA topological node belongs to a topological island",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

EquivalentEquipment_TreeNode = TreeNode(
    node_for=[EquivalentEquipment],
    label="name",
    tooltip="The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BusbarSection_TreeNode = TreeNode(
    node_for=[BusbarSection],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TapChanger_TreeNode = TreeNode(
    node_for=[TapChanger],
    label="name",
    tooltip="Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerWinding_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    label="name",
    tooltip="A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegulatingControl_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    label="name",
    tooltip="Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulatingControl_RegulatingCondEq_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="RegulatingCondEq",
    label="=RegulatingCondEq",
    tooltip="copy from reg cond eqcopy from reg cond eq",
    add=[RegulatingCondEq],
    move=[RegulatingCondEq],
    icon_path=IMAGE_PATH)
RegulatingControl_TapChanger_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="TapChanger",
    label="=TapChanger",
    tooltip="copy from reg conduting eqcopy from reg conduting eq",
    add=[TapChanger],
    move=[TapChanger],
    icon_path=IMAGE_PATH)

ReactiveCapabilityCurve_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    label="name",
    tooltip="Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    children="InitiallyUsedBySynchronousMachine",
    label="=InitiallyUsedBySynchronousMachine",
    tooltip="Synchronous machines using this curve as default.Synchronous machines using this curve as default.",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)

ACLineSegment_TreeNode = TreeNode(
    node_for=[ACLineSegment],
    label="name",
    tooltip="A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PhaseTapChanger_TreeNode = TreeNode(
    node_for=[PhaseTapChanger],
    label="name",
    tooltip="A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MutualCoupling_TreeNode = TreeNode(
    node_for=[MutualCoupling],
    label="name",
    tooltip="This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SynchronousMachine_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    label="name",
    tooltip="An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. ",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RatioTapChanger_TreeNode = TreeNode(
    node_for=[RatioTapChanger],
    label="name",
    tooltip="A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PowerTransformer_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    label="name",
    tooltip="An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerTransformer_Contains_TransformerWindings_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    children="Contains_TransformerWindings",
    label="=Contains_TransformerWindings",
    tooltip="A transformer has windingsA transformer has windings",
    add=[TransformerWinding],
    move=[TransformerWinding],
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


RegulatingCondEq_TreeNode = TreeNode(
    node_for=[RegulatingCondEq],
    label="name",
    tooltip="RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VoltageControlZone_TreeNode = TreeNode(
    node_for=[VoltageControlZone],
    label="name",
    tooltip="An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.",
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
    tooltip="A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Conductor_TreeNode = TreeNode(
    node_for=[Conductor],
    label="name",
    tooltip="Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CurrentLimit_TreeNode = TreeNode(
    node_for=[CurrentLimit],
    label="name",
    tooltip="Operational limit on current.Operational limit on current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VoltageLimit_TreeNode = TreeNode(
    node_for=[VoltageLimit],
    label="name",
    tooltip="Operational limit applied to voltage.Operational limit applied to voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalLimit_TreeNode = TreeNode(
    node_for=[OperationalLimit],
    label="name",
    tooltip="A value associated with a specific kind of limit.A value associated with a specific kind of limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalLimitSet_TreeNode = TreeNode(
    node_for=[OperationalLimitSet],
    label="name",
    tooltip="A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperationalLimitSet_OperationalLimitValue_TreeNode = TreeNode(
    node_for=[OperationalLimitSet],
    children="OperationalLimitValue",
    label="=OperationalLimitValue",
    tooltip="Values of equipment limits.Values of equipment limits.",
    add=[OperationalLimit],
    move=[OperationalLimit],
    icon_path=IMAGE_PATH)

OperationalLimitType_TreeNode = TreeNode(
    node_for=[OperationalLimitType],
    label="name",
    tooltip="A type of limit.  The meaning of a specific limit is described in this class.A type of limit.  The meaning of a specific limit is described in this class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperationalLimitType_OperationalLimit_TreeNode = TreeNode(
    node_for=[OperationalLimitType],
    children="OperationalLimit",
    label="=OperationalLimit",
    tooltip="The operational limits associated with this type of limit.The operational limits associated with this type of limit.",
    add=[OperationalLimit],
    move=[OperationalLimit],
    icon_path=IMAGE_PATH)


#------------------------------------------------------------------------------
#  Tree node list:
#------------------------------------------------------------------------------


tree_nodes = [
    Element_TreeNode,
    Model_TreeNode,
    Model_Elements_TreeNode,
    IEC61970CIMVersion_TreeNode,
    StateVariable_TreeNode,
    SvTapStep_TreeNode,
    SvPowerFlow_TreeNode,
    IdentifiedObject_TreeNode,
    SubGeographicalRegion_TreeNode,
    SubGeographicalRegion_Substations_TreeNode,
    Terminal_TreeNode,
    Terminal_HasFirst_MutualCoupling_TreeNode,
    Terminal_OperationalLimitSet_TreeNode,
    Terminal_RegulatingControl_TreeNode,
    Terminal_TieFlow_TreeNode,
    Terminal_HasSecond_MutualCoupling_TreeNode,
    GeographicalRegion_TreeNode,
    GeographicalRegion_Regions_TreeNode,
    CurveData_TreeNode,
    ControlArea_TreeNode,
    ControlArea_TopologicalNode_TreeNode,
    ControlArea_TieFlow_TreeNode,
    ControlArea_ControlAreaGeneratingUnit_TreeNode,
    ControlAreaGeneratingUnit_TreeNode,
    TieFlow_TreeNode,
    WindGeneratingUnit_TreeNode,
    FossilFuel_TreeNode,
    NuclearGeneratingUnit_TreeNode,
    HydroGeneratingUnit_TreeNode,
    ThermalGeneratingUnit_TreeNode,
    HydroPump_TreeNode,
    LoadResponseCharacteristic_TreeNode,
    LoadResponseCharacteristic_EnergyConsumer_TreeNode,
    TopologicalNode_TreeNode,
    TopologicalNode_Terminal_TreeNode,
    TopologicalIsland_TreeNode,
    TopologicalIsland_TopologicalNodes_TreeNode,
    TapChanger_TreeNode,
    RegulatingControl_TreeNode,
    RegulatingControl_RegulatingCondEq_TreeNode,
    RegulatingControl_TapChanger_TreeNode,
    ReactiveCapabilityCurve_TreeNode,
    ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_TreeNode,
    PhaseTapChanger_TreeNode,
    MutualCoupling_TreeNode,
    RatioTapChanger_TreeNode,
    VoltageControlZone_TreeNode,
    OperationalLimit_TreeNode,
    OperationalLimitSet_TreeNode,
    OperationalLimitSet_OperationalLimitValue_TreeNode,
    OperationalLimitType_TreeNode,
    OperationalLimitType_OperationalLimit_TreeNode,
    SvVoltage_TreeNode,
    SvShuntCompensatorSections_TreeNode,
    Curve_TreeNode,
    Curve_CurveScheduleDatas_TreeNode,
    ConnectivityNodeContainer_TreeNode,
    ConnectivityNodeContainer_TopologicalNode_TreeNode,
    Equipment_TreeNode,
    BaseVoltage_TreeNode,
    BaseVoltage_ConductingEquipment_TreeNode,
    BaseVoltage_VoltageLevel_TreeNode,
    BaseVoltage_TopologicalNode_TreeNode,
    EquipmentContainer_TreeNode,
    EquipmentContainer_Contains_Equipments_TreeNode,
    Substation_TreeNode,
    Substation_Contains_VoltageLevels_TreeNode,
    ConductingEquipment_TreeNode,
    ConductingEquipment_Terminals_TreeNode,
    GeneratingUnit_TreeNode,
    GeneratingUnit_Contains_SynchronousMachines_TreeNode,
    GeneratingUnit_ControlAreaGeneratingUnit_TreeNode,
    EquivalentEquipment_TreeNode,
    BusbarSection_TreeNode,
    TransformerWinding_TreeNode,
    PowerTransformer_TreeNode,
    PowerTransformer_Contains_TransformerWindings_TreeNode,
    EnergyConsumer_TreeNode,
    Switch_TreeNode,
    RegulatingCondEq_TreeNode,
    Line_TreeNode,
    ShuntCompensator_TreeNode,
    Conductor_TreeNode,
    CurrentLimit_TreeNode,
    VoltageLimit_TreeNode,
    VoltageLevel_TreeNode,
    ACLineSegment_TreeNode,
    SynchronousMachine_TreeNode,
]
tree_nodes.reverse()

#------------------------------------------------------------------------------
#  UCTE Tree Editor:
#------------------------------------------------------------------------------

UCTETreeEditor = TreeEditor(nodes=tree_nodes, editable=True)

#------------------------------------------------------------------------------
#  Begin "UCTETreeEditor" user region:
#------------------------------------------------------------------------------
# @generated
class TreeRoot(HasTraits):

    # Root element of the model tree.
    root = Instance(HasTraits)

    # Traits view to display.
    view = View(
        Item('root',
            editor=UCTETreeEditor,
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True,
        buttons   = ["OK", "Cancel"]
    )

#------------------------------------------------------------------------------
#  End "UCTETreeEditor" user region:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    root = TreeRoot()
    root.configure_traits()

# EOF -------------------------------------------------------------------------
