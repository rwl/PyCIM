#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Defines TreeNodes interface for the model.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Str, Dict, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group, TreeEditor, TreeNode

from enthought.traits.ui.menu \
    import Action, Menu

from CIM13 import *
from CIM13.Wires import *
from CIM13.Generation import *
from CIM13.Meas import *
from CIM13.LoadModel import *
from CIM13.Core import *
from CIM13.Contingency import *
from CIM13.Outage import *
from CIM13.SCADA import *
from CIM13.Domain import *
from CIM13.OperationalLimits import *
from CIM13.ControlArea import *
from CIM13.Equivalents import *
from CIM13.Topology import *
from CIM13.Protection import *
from CIM13.Generation.Production import *
from CIM13.Generation.GenerationDynamics import *

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

Root_TreeNode = TreeNode(
    node_for=[Root],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Model_TreeNode = TreeNode(
    node_for=[Model],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Model_Contains_TreeNode = TreeNode(
    node_for=[Model],
    children="Contains",
    label="=Contains",
    tooltip="",
    add=[Root],
    move=[Root],
    icon_path=IMAGE_PATH)

IEC61970CIMVersion_TreeNode = TreeNode(
    node_for=[IEC61970CIMVersion],
        tooltip="This is the IEC 61970 CIM version number assigned to this UML model file.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegulationSchedule_TreeNode = TreeNode(
    node_for=[RegulationSchedule],
    label="name",
    tooltip="A pre-established pattern over time for a controlled variable, e.g., busbar voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulationSchedule_RegulatingControl_TreeNode = TreeNode(
    node_for=[RegulationSchedule],
    children="RegulatingControl",
    label="=RegulatingControl",
    tooltip="",
    add=[RegulatingControl],
    move=[RegulatingControl],
    icon_path=IMAGE_PATH)
RegulationSchedule_VoltageControlZones_TreeNode = TreeNode(
    node_for=[RegulationSchedule],
    children="VoltageControlZones",
    label="=VoltageControlZones",
    tooltip="A VoltageControlZone may have a  voltage regulation schedule.",
    add=[VoltageControlZone],
    move=[VoltageControlZone],
    icon_path=IMAGE_PATH)

GroundDisconnector_TreeNode = TreeNode(
    node_for=[GroundDisconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TransformerWinding_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    label="name",
    tooltip="A winding is associated with each defined terminal of a transformer (or phase shifter).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TransformerWinding_To_WindingTest_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    children="To_WindingTest",
    label="=To_WindingTest",
    tooltip="The winding to which the test was conducted",
    add=[WindingTest],
    move=[WindingTest],
    icon_path=IMAGE_PATH)
TransformerWinding_From_WindingTest_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    children="From_WindingTest",
    label="=From_WindingTest",
    tooltip="The winding from which the test was conducted",
    add=[WindingTest],
    move=[WindingTest],
    icon_path=IMAGE_PATH)
TransformerWinding_TapChangers_TreeNode = TreeNode(
    node_for=[TransformerWinding],
    children="TapChangers",
    label="=TapChangers",
    tooltip="A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.",
    add=[TapChanger],
    move=[TapChanger],
    icon_path=IMAGE_PATH)

EnergySource_TreeNode = TreeNode(
    node_for=[EnergySource],
    label="name",
    tooltip="A generic equivalent for an energy supplier on a transmission or distribution voltage level.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SeriesCompensator_TreeNode = TreeNode(
    node_for=[SeriesCompensator],
    label="name",
    tooltip="A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WireType_TreeNode = TreeNode(
    node_for=[WireType],
    label="name",
    tooltip="Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

WireType_WireArrangements_TreeNode = TreeNode(
    node_for=[WireType],
    children="WireArrangements",
    label="=WireArrangements",
    tooltip="A WireType is mounted at a specified place in a WireArrangement.",
    add=[WireArrangement],
    move=[WireArrangement],
    icon_path=IMAGE_PATH)

Breaker_TreeNode = TreeNode(
    node_for=[Breaker],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


VoltageControlZone_TreeNode = TreeNode(
    node_for=[VoltageControlZone],
    label="name",
    tooltip="An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FrequencyConverter_TreeNode = TreeNode(
    node_for=[FrequencyConverter],
    label="name",
    tooltip="A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegulatingCondEq_TreeNode = TreeNode(
    node_for=[RegulatingCondEq],
    label="name",
    tooltip="RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulatingCondEq_Controls_TreeNode = TreeNode(
    node_for=[RegulatingCondEq],
    children="Controls",
    label="=Controls",
    tooltip="The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.",
    add=[Control],
    move=[Control],
    icon_path=IMAGE_PATH)

Conductor_TreeNode = TreeNode(
    node_for=[Conductor],
    label="name",
    tooltip="Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadBreakSwitch_TreeNode = TreeNode(
    node_for=[LoadBreakSwitch],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProtectedSwitch_TreeNode = TreeNode(
    node_for=[ProtectedSwitch],
    label="name",
    tooltip="A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProtectedSwitch_OperatedBy_ProtectionEquipments_TreeNode = TreeNode(
    node_for=[ProtectedSwitch],
    children="OperatedBy_ProtectionEquipments",
    label="=OperatedBy_ProtectionEquipments",
    tooltip="Circuit breakers may be operated by protection relays.",
    add=[ProtectionEquipment],
    move=[ProtectionEquipment],
    icon_path=IMAGE_PATH)
ProtectedSwitch_RecloseSequences_TreeNode = TreeNode(
    node_for=[ProtectedSwitch],
    children="RecloseSequences",
    label="=RecloseSequences",
    tooltip="A breaker may have zero or more automatic reclosures after a trip occurs.",
    add=[RecloseSequence],
    move=[RecloseSequence],
    icon_path=IMAGE_PATH)

Line_TreeNode = TreeNode(
    node_for=[Line],
    label="name",
    tooltip="A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Ground_TreeNode = TreeNode(
    node_for=[Ground],
    label="name",
    tooltip="A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Jumper_TreeNode = TreeNode(
    node_for=[Jumper],
    label="name",
    tooltip="A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DCLineSegment_TreeNode = TreeNode(
    node_for=[DCLineSegment],
    label="name",
    tooltip="A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TapChanger_TreeNode = TreeNode(
    node_for=[TapChanger],
    label="name",
    tooltip="Mechanism for changing transformer winding tap positions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CompositeSwitch_TreeNode = TreeNode(
    node_for=[CompositeSwitch],
    label="name",
    tooltip="A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CompositeSwitch_Switches_TreeNode = TreeNode(
    node_for=[CompositeSwitch],
    children="Switches",
    label="=Switches",
    tooltip="",
    add=[Switch],
    move=[Switch],
    icon_path=IMAGE_PATH)

WireArrangement_TreeNode = TreeNode(
    node_for=[WireArrangement],
    label="name",
    tooltip="Identification, spacing and configuration of the wires of a ConductorType, with reference to their type.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PowerTransformer_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    label="name",
    tooltip="An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerTransformer_Contains_TransformerWindings_TreeNode = TreeNode(
    node_for=[PowerTransformer],
    children="Contains_TransformerWindings",
    label="=Contains_TransformerWindings",
    tooltip="A transformer has windings",
    add=[TransformerWinding],
    move=[TransformerWinding],
    icon_path=IMAGE_PATH)

BusbarSection_TreeNode = TreeNode(
    node_for=[BusbarSection],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ACLineSegment_TreeNode = TreeNode(
    node_for=[ACLineSegment],
    label="name",
    tooltip="A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ACLineSegment_HasFirst_MutualCoupling_TreeNode = TreeNode(
    node_for=[ACLineSegment],
    children="HasFirst_MutualCoupling",
    label="=HasFirst_MutualCoupling",
    tooltip="",
    add=[MutualCoupling],
    move=[MutualCoupling],
    icon_path=IMAGE_PATH)
ACLineSegment_HasSecond_MutualCoupling_TreeNode = TreeNode(
    node_for=[ACLineSegment],
    children="HasSecond_MutualCoupling",
    label="=HasSecond_MutualCoupling",
    tooltip="",
    add=[MutualCoupling],
    move=[MutualCoupling],
    icon_path=IMAGE_PATH)

MutualCoupling_TreeNode = TreeNode(
    node_for=[MutualCoupling],
        tooltip="This class represents the zero sequence line mutual coupling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ShuntCompensator_TreeNode = TreeNode(
    node_for=[ShuntCompensator],
    label="name",
    tooltip="A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Fuse_TreeNode = TreeNode(
    node_for=[Fuse],
    label="name",
    tooltip="An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RectifierInverter_TreeNode = TreeNode(
    node_for=[RectifierInverter],
    label="name",
    tooltip="Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatExchanger_TreeNode = TreeNode(
    node_for=[HeatExchanger],
    label="name",
    tooltip="Equipment for the cooling of electrical equipment and the extraction of heat",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EnergyConsumer_TreeNode = TreeNode(
    node_for=[EnergyConsumer],
    label="name",
    tooltip="Generic user of energy - a  point of consumption on the power system model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Switch_TreeNode = TreeNode(
    node_for=[Switch],
    label="name",
    tooltip="A generic device designed to close, or open, or both, one or more electric circuits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Switch_SwitchingOperations_TreeNode = TreeNode(
    node_for=[Switch],
    children="SwitchingOperations",
    label="=SwitchingOperations",
    tooltip="A switch may be operated by many schedules.",
    add=[SwitchingOperation],
    move=[SwitchingOperation],
    icon_path=IMAGE_PATH)

SynchronousMachine_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    label="name",
    tooltip="An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SynchronousMachine_ReactiveCapabilityCurves_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    children="ReactiveCapabilityCurves",
    label="=ReactiveCapabilityCurves",
    tooltip="",
    add=[ReactiveCapabilityCurve],
    move=[ReactiveCapabilityCurve],
    icon_path=IMAGE_PATH)
SynchronousMachine_DrivenBy_PrimeMover_TreeNode = TreeNode(
    node_for=[SynchronousMachine],
    children="DrivenBy_PrimeMover",
    label="=DrivenBy_PrimeMover",
    tooltip="",
    add=[PrimeMover],
    move=[PrimeMover],
    icon_path=IMAGE_PATH)

RegulatingControl_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    label="name",
    tooltip="Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegulatingControl_RegulatingCondEq_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="RegulatingCondEq",
    label="=RegulatingCondEq",
    tooltip="",
    add=[RegulatingCondEq],
    move=[RegulatingCondEq],
    icon_path=IMAGE_PATH)
RegulatingControl_TapChanger_TreeNode = TreeNode(
    node_for=[RegulatingControl],
    children="TapChanger",
    label="=TapChanger",
    tooltip="",
    add=[TapChanger],
    move=[TapChanger],
    icon_path=IMAGE_PATH)

Connector_TreeNode = TreeNode(
    node_for=[Connector],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StaticVarCompensator_TreeNode = TreeNode(
    node_for=[StaticVarCompensator],
    label="name",
    tooltip="A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Junction_TreeNode = TreeNode(
    node_for=[Junction],
    label="name",
    tooltip="A point where one or more conducting equipments are connected with zero resistance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


WindingTest_TreeNode = TreeNode(
    node_for=[WindingTest],
    label="name",
    tooltip="Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Disconnector_TreeNode = TreeNode(
    node_for=[Disconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConductorType_TreeNode = TreeNode(
    node_for=[ConductorType],
    label="name",
    tooltip="Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductorType_Conductors_TreeNode = TreeNode(
    node_for=[ConductorType],
    children="Conductors",
    label="=Conductors",
    tooltip="Sections of conductor are physically described by a conductor type",
    add=[Conductor],
    move=[Conductor],
    icon_path=IMAGE_PATH)
ConductorType_WireArrangements_TreeNode = TreeNode(
    node_for=[ConductorType],
    children="WireArrangements",
    label="=WireArrangements",
    tooltip="A ConductorType is made up of wires that can be configured in several ways.",
    add=[WireArrangement],
    move=[WireArrangement],
    icon_path=IMAGE_PATH)

Plant_TreeNode = TreeNode(
    node_for=[Plant],
    label="name",
    tooltip="A Plant is a collection of equipment for purposes of generation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ReactiveCapabilityCurve_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    label="name",
    tooltip="Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReactiveCapabilityCurve_SynchronousMachines_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    children="SynchronousMachines",
    label="=SynchronousMachines",
    tooltip="",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)
ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_TreeNode = TreeNode(
    node_for=[ReactiveCapabilityCurve],
    children="InitiallyUsedBySynchronousMachine",
    label="=InitiallyUsedBySynchronousMachine",
    tooltip="Defines the default MVArCapabilityCurve for use by a SynchronousMachine.",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)

NuclearGeneratingUnit_TreeNode = TreeNode(
    node_for=[NuclearGeneratingUnit],
    label="name",
    tooltip="A nuclear generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    label="name",
    tooltip="A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeneratingUnit_ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="ControlAreaGeneratingUnit",
    label="=ControlAreaGeneratingUnit",
    tooltip="",
    add=[ControlAreaGeneratingUnit],
    move=[ControlAreaGeneratingUnit],
    icon_path=IMAGE_PATH)
GeneratingUnit_GrossToNetActivePowerCurves_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="GrossToNetActivePowerCurves",
    label="=GrossToNetActivePowerCurves",
    tooltip="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit",
    add=[GrossToNetActivePowerCurve],
    move=[GrossToNetActivePowerCurve],
    icon_path=IMAGE_PATH)
GeneratingUnit_Contains_SynchronousMachines_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="Contains_SynchronousMachines",
    label="=Contains_SynchronousMachines",
    tooltip="A synchronous machine may operate as a generator and as such becomes a member of a generating unit",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)
GeneratingUnit_GenUnitOpCostCurves_TreeNode = TreeNode(
    node_for=[GeneratingUnit],
    children="GenUnitOpCostCurves",
    label="=GenUnitOpCostCurves",
    tooltip="A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.",
    add=[GenUnitOpCostCurve],
    move=[GenUnitOpCostCurve],
    icon_path=IMAGE_PATH)

StartIgnFuelCurve_TreeNode = TreeNode(
    node_for=[StartIgnFuelCurve],
    label="name",
    tooltip="The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroGeneratingEfficiencyCurve_TreeNode = TreeNode(
    node_for=[HydroGeneratingEfficiencyCurve],
    label="name",
    tooltip="Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TargetLevelSchedule_TreeNode = TreeNode(
    node_for=[TargetLevelSchedule],
    label="name",
    tooltip="Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GrossToNetActivePowerCurve_TreeNode = TreeNode(
    node_for=[GrossToNetActivePowerCurve],
    label="name",
    tooltip="Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


IncrementalHeatRateCurve_TreeNode = TreeNode(
    node_for=[IncrementalHeatRateCurve],
    label="name",
    tooltip="Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatInputCurve_TreeNode = TreeNode(
    node_for=[HeatInputCurve],
    label="name",
    tooltip="Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StartRampCurve_TreeNode = TreeNode(
    node_for=[StartRampCurve],
    label="name",
    tooltip="Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AirCompressor_TreeNode = TreeNode(
    node_for=[AirCompressor],
    label="name",
    tooltip="Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ShutdownCurve_TreeNode = TreeNode(
    node_for=[ShutdownCurve],
    label="name",
    tooltip="Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CombinedCyclePlant_TreeNode = TreeNode(
    node_for=[CombinedCyclePlant],
    label="name",
    tooltip="A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CombinedCyclePlant_Contain_ThermalGeneratingUnits_TreeNode = TreeNode(
    node_for=[CombinedCyclePlant],
    children="Contain_ThermalGeneratingUnits",
    label="=Contain_ThermalGeneratingUnits",
    tooltip="A thermal generating unit may be a member of a combined cycle plant",
    add=[ThermalGeneratingUnit],
    move=[ThermalGeneratingUnit],
    icon_path=IMAGE_PATH)

StartupModel_TreeNode = TreeNode(
    node_for=[StartupModel],
    label="name",
    tooltip="Unit start up characteristics depending on how long the unit has been off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroPump_TreeNode = TreeNode(
    node_for=[HydroPump],
    label="name",
    tooltip="A synchronous motor-driven pump, typically associated with a pumped storage plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EmissionCurve_TreeNode = TreeNode(
    node_for=[EmissionCurve],
    label="name",
    tooltip="Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenUnitOpCostCurve_TreeNode = TreeNode(
    node_for=[GenUnitOpCostCurve],
    label="name",
    tooltip="Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroPowerPlant_TreeNode = TreeNode(
    node_for=[HydroPowerPlant],
    label="name",
    tooltip="A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HydroPowerPlant_Contain_HydroGeneratingUnits_TreeNode = TreeNode(
    node_for=[HydroPowerPlant],
    children="Contain_HydroGeneratingUnits",
    label="=Contain_HydroGeneratingUnits",
    tooltip="The hydro generating unit belongs to a hydro power plant",
    add=[HydroGeneratingUnit],
    move=[HydroGeneratingUnit],
    icon_path=IMAGE_PATH)
HydroPowerPlant_Contain_HydroPumps_TreeNode = TreeNode(
    node_for=[HydroPowerPlant],
    children="Contain_HydroPumps",
    label="=Contain_HydroPumps",
    tooltip="The hydro pump may be a member of a pumped storage plant or a pump for distributing water",
    add=[HydroPump],
    move=[HydroPump],
    icon_path=IMAGE_PATH)

HydroGeneratingUnit_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HydroGeneratingUnit_HydroGeneratingEfficiencyCurves_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    children="HydroGeneratingEfficiencyCurves",
    label="=HydroGeneratingEfficiencyCurves",
    tooltip="A hydro generating unit has an efficiency curve",
    add=[HydroGeneratingEfficiencyCurve],
    move=[HydroGeneratingEfficiencyCurve],
    icon_path=IMAGE_PATH)
HydroGeneratingUnit_TailbayLossCurve_TreeNode = TreeNode(
    node_for=[HydroGeneratingUnit],
    children="TailbayLossCurve",
    label="=TailbayLossCurve",
    tooltip="A hydro generating unit has a tailbay loss curve",
    add=[TailbayLossCurve],
    move=[TailbayLossCurve],
    icon_path=IMAGE_PATH)

CAESPlant_TreeNode = TreeNode(
    node_for=[CAESPlant],
    label="name",
    tooltip="Compressed air energy storage plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LevelVsVolumeCurve_TreeNode = TreeNode(
    node_for=[LevelVsVolumeCurve],
    label="name",
    tooltip="Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


InflowForecast_TreeNode = TreeNode(
    node_for=[InflowForecast],
    label="name",
    tooltip="Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SteamSendoutSchedule_TreeNode = TreeNode(
    node_for=[SteamSendoutSchedule],
    label="name",
    tooltip="The cogeneration plant's steam sendout schedule in volume per time unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ThermalGeneratingUnit_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ThermalGeneratingUnit_FuelAllocationSchedules_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="FuelAllocationSchedules",
    label="=FuelAllocationSchedules",
    tooltip="A thermal generating unit may have one or more fuel allocation schedules",
    add=[FuelAllocationSchedule],
    move=[FuelAllocationSchedule],
    icon_path=IMAGE_PATH)
ThermalGeneratingUnit_EmissionCurves_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="EmissionCurves",
    label="=EmissionCurves",
    tooltip="A thermal generating unit may have  one or more emission curves",
    add=[EmissionCurve],
    move=[EmissionCurve],
    icon_path=IMAGE_PATH)
ThermalGeneratingUnit_EmmissionAccounts_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="EmmissionAccounts",
    label="=EmmissionAccounts",
    tooltip="A thermal generating unit may have one or more emission allowance accounts",
    add=[EmissionAccount],
    move=[EmissionAccount],
    icon_path=IMAGE_PATH)
ThermalGeneratingUnit_FossilFuels_TreeNode = TreeNode(
    node_for=[ThermalGeneratingUnit],
    children="FossilFuels",
    label="=FossilFuels",
    tooltip="A thermal generating unit may have one or more fossil fuels",
    add=[FossilFuel],
    move=[FossilFuel],
    icon_path=IMAGE_PATH)

FossilFuel_TreeNode = TreeNode(
    node_for=[FossilFuel],
    label="name",
    tooltip="The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

FossilFuel_FuelAllocationSchedule_TreeNode = TreeNode(
    node_for=[FossilFuel],
    children="FuelAllocationSchedule",
    label="=FuelAllocationSchedule",
    tooltip="A fuel allocation schedule must have a fossil fuel",
    add=[FuelAllocationSchedule],
    move=[FuelAllocationSchedule],
    icon_path=IMAGE_PATH)

FuelAllocationSchedule_TreeNode = TreeNode(
    node_for=[FuelAllocationSchedule],
    label="name",
    tooltip="The amount of fuel of a given type which is allocated for consumption over a specified period of time",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EmissionAccount_TreeNode = TreeNode(
    node_for=[EmissionAccount],
    label="name",
    tooltip="Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TailbayLossCurve_TreeNode = TreeNode(
    node_for=[TailbayLossCurve],
    label="name",
    tooltip="Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PenstockLossCurve_TreeNode = TreeNode(
    node_for=[PenstockLossCurve],
    label="name",
    tooltip="Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StartMainFuelCurve_TreeNode = TreeNode(
    node_for=[StartMainFuelCurve],
    label="name",
    tooltip="The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Reservoir_TreeNode = TreeNode(
    node_for=[Reservoir],
    label="name",
    tooltip="A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Reservoir_LevelVsVolumeCurve_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="LevelVsVolumeCurve",
    label="=LevelVsVolumeCurve",
    tooltip="A reservoir may have a level versus volume relationship.",
    add=[LevelVsVolumeCurve],
    move=[LevelVsVolumeCurve],
    icon_path=IMAGE_PATH)
Reservoir_InflowForecast_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="InflowForecast",
    label="=InflowForecast",
    tooltip="A reservoir may have a 'natural' inflow forecast.",
    add=[InflowForecast],
    move=[InflowForecast],
    icon_path=IMAGE_PATH)
Reservoir_SpillsInto_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="SpillsInto",
    label="=SpillsInto",
    tooltip="A reservoir may spill into a downstream reservoir",
    add=[Reservoir],
    move=[Reservoir],
    icon_path=IMAGE_PATH)
Reservoir_HydroPowerPlants_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="HydroPowerPlants",
    label="=HydroPowerPlants",
    tooltip="Generators discharge water to or pumps are supplied water from a downstream reservoir",
    add=[HydroPowerPlant],
    move=[HydroPowerPlant],
    icon_path=IMAGE_PATH)
Reservoir_UpstreamFrom_TreeNode = TreeNode(
    node_for=[Reservoir],
    children="UpstreamFrom",
    label="=UpstreamFrom",
    tooltip="Generators are supplied water from or pumps discharge water to an upstream reservoir",
    add=[HydroPowerPlant],
    move=[HydroPowerPlant],
    icon_path=IMAGE_PATH)

HydroPumpOpSchedule_TreeNode = TreeNode(
    node_for=[HydroPumpOpSchedule],
    label="name",
    tooltip="The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatRateCurve_TreeNode = TreeNode(
    node_for=[HeatRateCurve],
    label="name",
    tooltip="Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


GenUnitOpSchedule_TreeNode = TreeNode(
    node_for=[GenUnitOpSchedule],
    label="name",
    tooltip="The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CogenerationPlant_TreeNode = TreeNode(
    node_for=[CogenerationPlant],
    label="name",
    tooltip="A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CogenerationPlant_Contain_ThermalGeneratingUnits_TreeNode = TreeNode(
    node_for=[CogenerationPlant],
    children="Contain_ThermalGeneratingUnits",
    label="=Contain_ThermalGeneratingUnits",
    tooltip="A thermal generating unit may be a member of a cogeneration plant",
    add=[ThermalGeneratingUnit],
    move=[ThermalGeneratingUnit],
    icon_path=IMAGE_PATH)

Supercritical_TreeNode = TreeNode(
    node_for=[Supercritical],
    label="name",
    tooltip="Once-through supercritical boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SteamTurbine_TreeNode = TreeNode(
    node_for=[SteamTurbine],
    label="name",
    tooltip="Steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SteamTurbine_SteamSupplys_TreeNode = TreeNode(
    node_for=[SteamTurbine],
    children="SteamSupplys",
    label="=SteamSupplys",
    tooltip="Steam turbines may have steam supplied by a steam supply",
    add=[SteamSupply],
    move=[SteamSupply],
    icon_path=IMAGE_PATH)

CTTempActivePowerCurve_TreeNode = TreeNode(
    node_for=[CTTempActivePowerCurve],
    label="name",
    tooltip="Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PrimeMover_TreeNode = TreeNode(
    node_for=[PrimeMover],
    label="name",
    tooltip="The machine used to develop mechanical energy used to drive a generator.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PrimeMover_Drives_SynchronousMachines_TreeNode = TreeNode(
    node_for=[PrimeMover],
    children="Drives_SynchronousMachines",
    label="=Drives_SynchronousMachines",
    tooltip="",
    add=[SynchronousMachine],
    move=[SynchronousMachine],
    icon_path=IMAGE_PATH)

PWRSteamSupply_TreeNode = TreeNode(
    node_for=[PWRSteamSupply],
    label="name",
    tooltip="Pressurized water reactor used as a steam supply to a steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CombustionTurbine_TreeNode = TreeNode(
    node_for=[CombustionTurbine],
    label="name",
    tooltip="A prime mover that is typically fueled by gas or light oil",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HeatRecoveryBoiler_TreeNode = TreeNode(
    node_for=[HeatRecoveryBoiler],
    label="name",
    tooltip="The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

HeatRecoveryBoiler_CombustionTurbines_TreeNode = TreeNode(
    node_for=[HeatRecoveryBoiler],
    children="CombustionTurbines",
    label="=CombustionTurbines",
    tooltip="A combustion turbine may have a heat recovery boiler for making steam",
    add=[CombustionTurbine],
    move=[CombustionTurbine],
    icon_path=IMAGE_PATH)

BWRSteamSupply_TreeNode = TreeNode(
    node_for=[BWRSteamSupply],
    label="name",
    tooltip="Boiling water reactor used as a steam supply to a steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


HydroTurbine_TreeNode = TreeNode(
    node_for=[HydroTurbine],
    label="name",
    tooltip="A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DrumBoiler_TreeNode = TreeNode(
    node_for=[DrumBoiler],
    label="name",
    tooltip="Drum boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


FossilSteamSupply_TreeNode = TreeNode(
    node_for=[FossilSteamSupply],
    label="name",
    tooltip="Fossil fueled boiler (e.g., coal, oil, gas)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Subcritical_TreeNode = TreeNode(
    node_for=[Subcritical],
    label="name",
    tooltip="Once-through subcritical boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SteamSupply_TreeNode = TreeNode(
    node_for=[SteamSupply],
    label="name",
    tooltip="Steam supply for steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SteamSupply_SteamTurbines_TreeNode = TreeNode(
    node_for=[SteamSupply],
    children="SteamTurbines",
    label="=SteamTurbines",
    tooltip="Steam turbines may have steam supplied by a steam supply",
    add=[SteamTurbine],
    move=[SteamTurbine],
    icon_path=IMAGE_PATH)

Discrete_TreeNode = TreeNode(
    node_for=[Discrete],
    label="name",
    tooltip="Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Discrete_Contain_MeasurementValues_TreeNode = TreeNode(
    node_for=[Discrete],
    children="Contain_MeasurementValues",
    label="=Contain_MeasurementValues",
    tooltip="",
    add=[DiscreteValue],
    move=[DiscreteValue],
    icon_path=IMAGE_PATH)

Measurement_TreeNode = TreeNode(
    node_for=[Measurement],
    label="name",
    tooltip="A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SetPoint_TreeNode = TreeNode(
    node_for=[SetPoint],
    label="name",
    tooltip="A SetPoint is an analog control used for supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Control_TreeNode = TreeNode(
    node_for=[Control],
    label="name",
    tooltip="Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ControlType_TreeNode = TreeNode(
    node_for=[ControlType],
    label="name",
    tooltip="Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlType_Controls_TreeNode = TreeNode(
    node_for=[ControlType],
    children="Controls",
    label="=Controls",
    tooltip="",
    add=[Control],
    move=[Control],
    icon_path=IMAGE_PATH)

DiscreteValue_TreeNode = TreeNode(
    node_for=[DiscreteValue],
    label="name",
    tooltip="DiscreteValue represents a discrete MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Accumulator_TreeNode = TreeNode(
    node_for=[Accumulator],
    label="name",
    tooltip="Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Accumulator_Contain_MeasurementValues_TreeNode = TreeNode(
    node_for=[Accumulator],
    children="Contain_MeasurementValues",
    label="=Contain_MeasurementValues",
    tooltip="",
    add=[AccumulatorValue],
    move=[AccumulatorValue],
    icon_path=IMAGE_PATH)
Accumulator_LimitSets_TreeNode = TreeNode(
    node_for=[Accumulator],
    children="LimitSets",
    label="=LimitSets",
    tooltip="A measurement may have zero or more limit ranges defined for it.",
    add=[AccumulatorLimitSet],
    move=[AccumulatorLimitSet],
    icon_path=IMAGE_PATH)

LimitSet_TreeNode = TreeNode(
    node_for=[LimitSet],
    label="name",
    tooltip="Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AnalogLimit_TreeNode = TreeNode(
    node_for=[AnalogLimit],
    label="name",
    tooltip="Limit values for Analog measurements",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeasurementValue_TreeNode = TreeNode(
    node_for=[MeasurementValue],
    label="name",
    tooltip="The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ValueAliasSet_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    label="name",
    tooltip="Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ValueAliasSet_Values_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    children="Values",
    label="=Values",
    tooltip="",
    add=[ValueToAlias],
    move=[ValueToAlias],
    icon_path=IMAGE_PATH)
ValueAliasSet_Commands_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    children="Commands",
    label="=Commands",
    tooltip="",
    add=[Command],
    move=[Command],
    icon_path=IMAGE_PATH)
ValueAliasSet_Measurements_TreeNode = TreeNode(
    node_for=[ValueAliasSet],
    children="Measurements",
    label="=Measurements",
    tooltip="",
    add=[Discrete],
    move=[Discrete],
    icon_path=IMAGE_PATH)

StringMeasurementValue_TreeNode = TreeNode(
    node_for=[StringMeasurementValue],
    label="name",
    tooltip="StringMeasurementValue represents a measurement value of type string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Quality61850_TreeNode = TreeNode(
    node_for=[Quality61850],
        tooltip="Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Limit_TreeNode = TreeNode(
    node_for=[Limit],
    label="name",
    tooltip="Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeasurementType_TreeNode = TreeNode(
    node_for=[MeasurementType],
    label="name",
    tooltip="Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeasurementType_Measurements_TreeNode = TreeNode(
    node_for=[MeasurementType],
    children="Measurements",
    label="=Measurements",
    tooltip="A measurement has a measurement type.",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)

AccumulatorLimit_TreeNode = TreeNode(
    node_for=[AccumulatorLimit],
    label="name",
    tooltip="Limit values for Accumulator measurements",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StringMeasurement_TreeNode = TreeNode(
    node_for=[StringMeasurement],
    label="name",
    tooltip="StringMeasurement represents a measurement with values of type string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

StringMeasurement_Contains_MeasurementValues_TreeNode = TreeNode(
    node_for=[StringMeasurement],
    children="Contains_MeasurementValues",
    label="=Contains_MeasurementValues",
    tooltip="",
    add=[StringMeasurementValue],
    move=[StringMeasurementValue],
    icon_path=IMAGE_PATH)

ValueToAlias_TreeNode = TreeNode(
    node_for=[ValueToAlias],
    label="name",
    tooltip="Describes the translation of one particular value into a name, e.g. 1->'Open'",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


AnalogValue_TreeNode = TreeNode(
    node_for=[AnalogValue],
    label="name",
    tooltip="AnalogValue represents an analog MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AnalogValue_AltGeneratingUnit_TreeNode = TreeNode(
    node_for=[AnalogValue],
    children="AltGeneratingUnit",
    label="=AltGeneratingUnit",
    tooltip="",
    add=[AltGeneratingUnitMeas],
    move=[AltGeneratingUnitMeas],
    icon_path=IMAGE_PATH)
AnalogValue_AltTieMeas_TreeNode = TreeNode(
    node_for=[AnalogValue],
    children="AltTieMeas",
    label="=AltTieMeas",
    tooltip="",
    add=[AltTieMeas],
    move=[AltTieMeas],
    icon_path=IMAGE_PATH)

MeasurementValueQuality_TreeNode = TreeNode(
    node_for=[MeasurementValueQuality],
        tooltip="Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


MeasurementValueSource_TreeNode = TreeNode(
    node_for=[MeasurementValueSource],
    label="name",
    tooltip="MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

MeasurementValueSource_MeasurementValues_TreeNode = TreeNode(
    node_for=[MeasurementValueSource],
    children="MeasurementValues",
    label="=MeasurementValues",
    tooltip="",
    add=[MeasurementValue],
    move=[MeasurementValue],
    icon_path=IMAGE_PATH)

AccumulatorLimitSet_TreeNode = TreeNode(
    node_for=[AccumulatorLimitSet],
    label="name",
    tooltip="An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AccumulatorLimitSet_Measurements_TreeNode = TreeNode(
    node_for=[AccumulatorLimitSet],
    children="Measurements",
    label="=Measurements",
    tooltip="A measurement may have zero or more limit ranges defined for it.",
    add=[Accumulator],
    move=[Accumulator],
    icon_path=IMAGE_PATH)
AccumulatorLimitSet_Limits_TreeNode = TreeNode(
    node_for=[AccumulatorLimitSet],
    children="Limits",
    label="=Limits",
    tooltip="",
    add=[AccumulatorLimit],
    move=[AccumulatorLimit],
    icon_path=IMAGE_PATH)

AnalogLimitSet_TreeNode = TreeNode(
    node_for=[AnalogLimitSet],
    label="name",
    tooltip="An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

AnalogLimitSet_Limits_TreeNode = TreeNode(
    node_for=[AnalogLimitSet],
    children="Limits",
    label="=Limits",
    tooltip="",
    add=[AnalogLimit],
    move=[AnalogLimit],
    icon_path=IMAGE_PATH)
AnalogLimitSet_Measurements_TreeNode = TreeNode(
    node_for=[AnalogLimitSet],
    children="Measurements",
    label="=Measurements",
    tooltip="A measurement may have zero or more limit ranges defined for it.",
    add=[Analog],
    move=[Analog],
    icon_path=IMAGE_PATH)

Command_TreeNode = TreeNode(
    node_for=[Command],
    label="name",
    tooltip="A Command is a discrete control used for supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Analog_TreeNode = TreeNode(
    node_for=[Analog],
    label="name",
    tooltip="Analog represents an analog Measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Analog_Contain_MeasurementValues_TreeNode = TreeNode(
    node_for=[Analog],
    children="Contain_MeasurementValues",
    label="=Contain_MeasurementValues",
    tooltip="",
    add=[AnalogValue],
    move=[AnalogValue],
    icon_path=IMAGE_PATH)
Analog_LimitSets_TreeNode = TreeNode(
    node_for=[Analog],
    children="LimitSets",
    label="=LimitSets",
    tooltip="A measurement may have zero or more limit ranges defined for it.",
    add=[AnalogLimitSet],
    move=[AnalogLimitSet],
    icon_path=IMAGE_PATH)

AccumulatorValue_TreeNode = TreeNode(
    node_for=[AccumulatorValue],
    label="name",
    tooltip="AccumulatorValue represents a accumulated (counted) MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SubLoadArea_TreeNode = TreeNode(
    node_for=[SubLoadArea],
    label="name",
    tooltip="The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SubLoadArea_LoadGroups_TreeNode = TreeNode(
    node_for=[SubLoadArea],
    children="LoadGroups",
    label="=LoadGroups",
    tooltip="",
    add=[LoadGroup],
    move=[LoadGroup],
    icon_path=IMAGE_PATH)

Load_TreeNode = TreeNode(
    node_for=[Load],
    label="name",
    tooltip="A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadResponseCharacteristic_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    label="name",
    tooltip="Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadResponseCharacteristic_EnergyConsumer_TreeNode = TreeNode(
    node_for=[LoadResponseCharacteristic],
    children="EnergyConsumer",
    label="=EnergyConsumer",
    tooltip="",
    add=[EnergyConsumer],
    move=[EnergyConsumer],
    icon_path=IMAGE_PATH)

Season_TreeNode = TreeNode(
    node_for=[Season],
    label="name",
    tooltip="A specified time period of the year, e.g., Spring, Summer, Fall, Winter",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Season_SeasonDayTypeSchedules_TreeNode = TreeNode(
    node_for=[Season],
    children="SeasonDayTypeSchedules",
    label="=SeasonDayTypeSchedules",
    tooltip="Load demand models can be based on seasons",
    add=[SeasonDayTypeSchedule],
    move=[SeasonDayTypeSchedule],
    icon_path=IMAGE_PATH)

ConformLoadGroup_TreeNode = TreeNode(
    node_for=[ConformLoadGroup],
    label="name",
    tooltip="Load that follows a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConformLoadGroup_EnergyConsumers_TreeNode = TreeNode(
    node_for=[ConformLoadGroup],
    children="EnergyConsumers",
    label="=EnergyConsumers",
    tooltip="Consumers may be assigned to a load area.",
    add=[ConformLoad],
    move=[ConformLoad],
    icon_path=IMAGE_PATH)
ConformLoadGroup_ConformLoadSchedules_TreeNode = TreeNode(
    node_for=[ConformLoadGroup],
    children="ConformLoadSchedules",
    label="=ConformLoadSchedules",
    tooltip="",
    add=[ConformLoadSchedule],
    move=[ConformLoadSchedule],
    icon_path=IMAGE_PATH)

ConformLoad_TreeNode = TreeNode(
    node_for=[ConformLoad],
    label="name",
    tooltip="ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadArea_TreeNode = TreeNode(
    node_for=[LoadArea],
    label="name",
    tooltip="The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

LoadArea_SubLoadAreas_TreeNode = TreeNode(
    node_for=[LoadArea],
    children="SubLoadAreas",
    label="=SubLoadAreas",
    tooltip="The SubLoadAreas in the LoadArea.",
    add=[SubLoadArea],
    move=[SubLoadArea],
    icon_path=IMAGE_PATH)

PowerCutZone_TreeNode = TreeNode(
    node_for=[PowerCutZone],
    label="name",
    tooltip="An area or zone of the power system which is used for load shedding purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerCutZone_EnergyConsumers_TreeNode = TreeNode(
    node_for=[PowerCutZone],
    children="EnergyConsumers",
    label="=EnergyConsumers",
    tooltip="An energy consumer is assigned to a power cut zone",
    add=[EnergyConsumer],
    move=[EnergyConsumer],
    icon_path=IMAGE_PATH)

ConformLoadSchedule_TreeNode = TreeNode(
    node_for=[ConformLoadSchedule],
    label="name",
    tooltip="A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


StationSupply_TreeNode = TreeNode(
    node_for=[StationSupply],
    label="name",
    tooltip="Station supply with load derived from the station output.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


DayType_TreeNode = TreeNode(
    node_for=[DayType],
    label="name",
    tooltip="Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

DayType_SeasonDayTypeSchedules_TreeNode = TreeNode(
    node_for=[DayType],
    children="SeasonDayTypeSchedules",
    label="=SeasonDayTypeSchedules",
    tooltip="Load demand models can be based on day type",
    add=[SeasonDayTypeSchedule],
    move=[SeasonDayTypeSchedule],
    icon_path=IMAGE_PATH)

NonConformLoadSchedule_TreeNode = TreeNode(
    node_for=[NonConformLoadSchedule],
    label="name",
    tooltip="An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CustomerLoad_TreeNode = TreeNode(
    node_for=[CustomerLoad],
    label="name",
    tooltip="A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


LoadGroup_TreeNode = TreeNode(
    node_for=[LoadGroup],
    label="name",
    tooltip="The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NonConformLoadGroup_TreeNode = TreeNode(
    node_for=[NonConformLoadGroup],
    label="name",
    tooltip="Loads that do not follow a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

NonConformLoadGroup_NonConformLoadSchedules_TreeNode = TreeNode(
    node_for=[NonConformLoadGroup],
    children="NonConformLoadSchedules",
    label="=NonConformLoadSchedules",
    tooltip="",
    add=[NonConformLoadSchedule],
    move=[NonConformLoadSchedule],
    icon_path=IMAGE_PATH)
NonConformLoadGroup_EnergyConsumers_TreeNode = TreeNode(
    node_for=[NonConformLoadGroup],
    children="EnergyConsumers",
    label="=EnergyConsumers",
    tooltip="",
    add=[NonConformLoad],
    move=[NonConformLoad],
    icon_path=IMAGE_PATH)

EnergyArea_TreeNode = TreeNode(
    node_for=[EnergyArea],
    label="name",
    tooltip="The class describes an area having energy production or consumption. The class is the basis for further specialization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


SeasonDayTypeSchedule_TreeNode = TreeNode(
    node_for=[SeasonDayTypeSchedule],
    label="name",
    tooltip="The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


NonConformLoad_TreeNode = TreeNode(
    node_for=[NonConformLoad],
    label="name",
    tooltip="NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


InductionMotorLoad_TreeNode = TreeNode(
    node_for=[InductionMotorLoad],
    label="name",
    tooltip="Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Curve_TreeNode = TreeNode(
    node_for=[Curve],
    label="name",
    tooltip="Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Curve_CurveScheduleDatas_TreeNode = TreeNode(
    node_for=[Curve],
    children="CurveScheduleDatas",
    label="=CurveScheduleDatas",
    tooltip="The point data values that define a curve",
    add=[CurveData],
    move=[CurveData],
    icon_path=IMAGE_PATH)

VoltageLevel_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    label="name",
    tooltip="A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

VoltageLevel_Contains_Bays_TreeNode = TreeNode(
    node_for=[VoltageLevel],
    children="Contains_Bays",
    label="=Contains_Bays",
    tooltip="The association is used in the naming hierarchy.",
    add=[Bay],
    move=[Bay],
    icon_path=IMAGE_PATH)

ReportingGroup_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    label="name",
    tooltip="A reporting group is used for various ad-hoc groupings used for reporting.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReportingGroup_PowerSystemResource_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    children="PowerSystemResource",
    label="=PowerSystemResource",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)
ReportingGroup_BusNameMarker_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    children="BusNameMarker",
    label="=BusNameMarker",
    tooltip="",
    add=[BusNameMarker],
    move=[BusNameMarker],
    icon_path=IMAGE_PATH)
ReportingGroup_TopologicalNode_TreeNode = TreeNode(
    node_for=[ReportingGroup],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

ModelingAuthoritySet_TreeNode = TreeNode(
    node_for=[ModelingAuthoritySet],
    label="name",
    tooltip="A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ModelingAuthoritySet_IdentifiedObjects_TreeNode = TreeNode(
    node_for=[ModelingAuthoritySet],
    children="IdentifiedObjects",
    label="=IdentifiedObjects",
    tooltip="An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.",
    add=[IdentifiedObject],
    move=[IdentifiedObject],
    icon_path=IMAGE_PATH)

OperatingParticipant_TreeNode = TreeNode(
    node_for=[OperatingParticipant],
    label="name",
    tooltip="An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperatingParticipant_OperatingShare_TreeNode = TreeNode(
    node_for=[OperatingParticipant],
    children="OperatingShare",
    label="=OperatingShare",
    tooltip="",
    add=[OperatingShare],
    move=[OperatingShare],
    icon_path=IMAGE_PATH)

ReportingSuperGroup_TreeNode = TreeNode(
    node_for=[ReportingSuperGroup],
    label="name",
    tooltip="A reporting super group, groups reporting groups for a higher level report.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ReportingSuperGroup_ReportingGroup_TreeNode = TreeNode(
    node_for=[ReportingSuperGroup],
    children="ReportingGroup",
    label="=ReportingGroup",
    tooltip="",
    add=[ReportingGroup],
    move=[ReportingGroup],
    icon_path=IMAGE_PATH)

Substation_TreeNode = TreeNode(
    node_for=[Substation],
    label="name",
    tooltip="A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Substation_Contains_VoltageLevels_TreeNode = TreeNode(
    node_for=[Substation],
    children="Contains_VoltageLevels",
    label="=Contains_VoltageLevels",
    tooltip="The association is used in the naming hierarchy.",
    add=[VoltageLevel],
    move=[VoltageLevel],
    icon_path=IMAGE_PATH)
Substation_Contains_Bays_TreeNode = TreeNode(
    node_for=[Substation],
    children="Contains_Bays",
    label="=Contains_Bays",
    tooltip="The association is used in the naming hierarchy.",
    add=[Bay],
    move=[Bay],
    icon_path=IMAGE_PATH)

ConductingEquipment_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    label="name",
    tooltip="The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConductingEquipment_Terminals_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="Terminals",
    label="=Terminals",
    tooltip="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)
ConductingEquipment_ProtectionEquipments_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="ProtectionEquipments",
    label="=ProtectionEquipments",
    tooltip="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.",
    add=[ProtectionEquipment],
    move=[ProtectionEquipment],
    icon_path=IMAGE_PATH)
ConductingEquipment_ClearanceTags_TreeNode = TreeNode(
    node_for=[ConductingEquipment],
    children="ClearanceTags",
    label="=ClearanceTags",
    tooltip="Conducting equipment may have multiple clearance tags for authorized field work",
    add=[ClearanceTag],
    move=[ClearanceTag],
    icon_path=IMAGE_PATH)

IrregularTimePoint_TreeNode = TreeNode(
    node_for=[IrregularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points varies.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ConnectivityNodeContainer_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    label="name",
    tooltip="A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNodeContainer_TopologicalNode_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)
ConnectivityNodeContainer_ConnectivityNodes_TreeNode = TreeNode(
    node_for=[ConnectivityNodeContainer],
    children="ConnectivityNodes",
    label="=ConnectivityNodes",
    tooltip="",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

GeographicalRegion_TreeNode = TreeNode(
    node_for=[GeographicalRegion],
    label="name",
    tooltip="A geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

GeographicalRegion_Regions_TreeNode = TreeNode(
    node_for=[GeographicalRegion],
    children="Regions",
    label="=Regions",
    tooltip="The association is used in the naming hierarchy.",
    add=[SubGeographicalRegion],
    move=[SubGeographicalRegion],
    icon_path=IMAGE_PATH)

Unit_TreeNode = TreeNode(
    node_for=[Unit],
    label="name",
    tooltip="Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Unit_Controls_TreeNode = TreeNode(
    node_for=[Unit],
    children="Controls",
    label="=Controls",
    tooltip="",
    add=[Control],
    move=[Control],
    icon_path=IMAGE_PATH)
Unit_ProtectionEquipments_TreeNode = TreeNode(
    node_for=[Unit],
    children="ProtectionEquipments",
    label="=ProtectionEquipments",
    tooltip="The Protection Equipments having the Unit.",
    add=[ProtectionEquipment],
    move=[ProtectionEquipment],
    icon_path=IMAGE_PATH)
Unit_Measurements_TreeNode = TreeNode(
    node_for=[Unit],
    children="Measurements",
    label="=Measurements",
    tooltip="",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)

EquipmentContainer_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    label="name",
    tooltip="A modeling construct to provide a root class for all Equipment classes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EquipmentContainer_Contains_Equipments_TreeNode = TreeNode(
    node_for=[EquipmentContainer],
    children="Contains_Equipments",
    label="=Contains_Equipments",
    tooltip="The association is used in the naming hierarchy.",
    add=[Equipment],
    move=[Equipment],
    icon_path=IMAGE_PATH)

ModelingAuthority_TreeNode = TreeNode(
    node_for=[ModelingAuthority],
    label="name",
    tooltip="A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ModelingAuthority_ModelingAuthoritySets_TreeNode = TreeNode(
    node_for=[ModelingAuthority],
    children="ModelingAuthoritySets",
    label="=ModelingAuthoritySets",
    tooltip="A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.",
    add=[ModelingAuthoritySet],
    move=[ModelingAuthoritySet],
    icon_path=IMAGE_PATH)

BaseVoltage_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    label="name",
    tooltip="Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BaseVoltage_ConductingEquipment_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="ConductingEquipment",
    label="=ConductingEquipment",
    tooltip="Use association to ConductingEquipment only when there is no VoltageLevel container used.",
    add=[ConductingEquipment],
    move=[ConductingEquipment],
    icon_path=IMAGE_PATH)
BaseVoltage_VoltageLevel_TreeNode = TreeNode(
    node_for=[BaseVoltage],
    children="VoltageLevel",
    label="=VoltageLevel",
    tooltip="",
    add=[VoltageLevel],
    move=[VoltageLevel],
    icon_path=IMAGE_PATH)

OperatingShare_TreeNode = TreeNode(
    node_for=[OperatingShare],
        tooltip="Specifies the contract relationship between a PowerSystemResource and a contract participant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BasicIntervalSchedule_TreeNode = TreeNode(
    node_for=[BasicIntervalSchedule],
    label="name",
    tooltip="Schedule of values at points in time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CurveData_TreeNode = TreeNode(
    node_for=[CurveData],
        tooltip="Data point values for defining a curve or schedule",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Equipment_TreeNode = TreeNode(
    node_for=[Equipment],
    label="name",
    tooltip="The parts of a power system that are physical devices, electronic or mechanical",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Equipment_OperationalLimitSet_TreeNode = TreeNode(
    node_for=[Equipment],
    children="OperationalLimitSet",
    label="=OperationalLimitSet",
    tooltip="",
    add=[OperationalLimitSet],
    move=[OperationalLimitSet],
    icon_path=IMAGE_PATH)
Equipment_ContingencyEquipment_TreeNode = TreeNode(
    node_for=[Equipment],
    children="ContingencyEquipment",
    label="=ContingencyEquipment",
    tooltip="",
    add=[ContingencyEquipment],
    move=[ContingencyEquipment],
    icon_path=IMAGE_PATH)

RegularIntervalSchedule_TreeNode = TreeNode(
    node_for=[RegularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RegularIntervalSchedule_TimePoints_TreeNode = TreeNode(
    node_for=[RegularIntervalSchedule],
    children="TimePoints",
    label="=TimePoints",
    tooltip="A RegularTimePoint belongs to a RegularIntervalSchedule.",
    add=[RegularTimePoint],
    move=[RegularTimePoint],
    icon_path=IMAGE_PATH)

IrregularIntervalSchedule_TreeNode = TreeNode(
    node_for=[IrregularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them varies.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

IrregularIntervalSchedule_TimePoints_TreeNode = TreeNode(
    node_for=[IrregularIntervalSchedule],
    children="TimePoints",
    label="=TimePoints",
    tooltip="An IrregularTimePoint belongs to an IrregularIntervalSchedule.",
    add=[IrregularTimePoint],
    move=[IrregularTimePoint],
    icon_path=IMAGE_PATH)

Bay_TreeNode = TreeNode(
    node_for=[Bay],
    label="name",
    tooltip="A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RegularTimePoint_TreeNode = TreeNode(
    node_for=[RegularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Terminal_TreeNode = TreeNode(
    node_for=[Terminal],
    label="name",
    tooltip="An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Terminal_TieFlow_TreeNode = TreeNode(
    node_for=[Terminal],
    children="TieFlow",
    label="=TieFlow",
    tooltip="A terminal may participate in zero, one, or two control areas as a tie flow.",
    add=[TieFlow],
    move=[TieFlow],
    icon_path=IMAGE_PATH)
Terminal_OperationalLimitSet_TreeNode = TreeNode(
    node_for=[Terminal],
    children="OperationalLimitSet",
    label="=OperationalLimitSet",
    tooltip="",
    add=[OperationalLimitSet],
    move=[OperationalLimitSet],
    icon_path=IMAGE_PATH)
Terminal_BranchGroupTerminal_TreeNode = TreeNode(
    node_for=[Terminal],
    children="BranchGroupTerminal",
    label="=BranchGroupTerminal",
    tooltip="",
    add=[BranchGroupTerminal],
    move=[BranchGroupTerminal],
    icon_path=IMAGE_PATH)
Terminal_RegulatingControl_TreeNode = TreeNode(
    node_for=[Terminal],
    children="RegulatingControl",
    label="=RegulatingControl",
    tooltip="",
    add=[RegulatingControl],
    move=[RegulatingControl],
    icon_path=IMAGE_PATH)
Terminal_Measurements_TreeNode = TreeNode(
    node_for=[Terminal],
    children="Measurements",
    label="=Measurements",
    tooltip="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)

SubGeographicalRegion_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    label="name",
    tooltip="A subset of a geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SubGeographicalRegion_Lines_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    children="Lines",
    label="=Lines",
    tooltip="A Line can be contained by a SubGeographical Region.",
    add=[Line],
    move=[Line],
    icon_path=IMAGE_PATH)
SubGeographicalRegion_Substations_TreeNode = TreeNode(
    node_for=[SubGeographicalRegion],
    children="Substations",
    label="=Substations",
    tooltip="The association is used in the naming hierarchy.",
    add=[Substation],
    move=[Substation],
    icon_path=IMAGE_PATH)

PowerSystemResource_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    label="name",
    tooltip="A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PowerSystemResource_OperatedBy_Companies_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="OperatedBy_Companies",
    label="=OperatedBy_Companies",
    tooltip="A power system resource may be part of one or more companies",
    add=[Company],
    move=[Company],
    icon_path=IMAGE_PATH)
PowerSystemResource_ReportingGroup_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="ReportingGroup",
    label="=ReportingGroup",
    tooltip="",
    add=[ReportingGroup],
    move=[ReportingGroup],
    icon_path=IMAGE_PATH)
PowerSystemResource_OperatingShare_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="OperatingShare",
    label="=OperatingShare",
    tooltip="",
    add=[OperatingShare],
    move=[OperatingShare],
    icon_path=IMAGE_PATH)
PowerSystemResource_PsrLists_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="PsrLists",
    label="=PsrLists",
    tooltip="",
    add=[PsrList],
    move=[PsrList],
    icon_path=IMAGE_PATH)
PowerSystemResource_Contains_Measurements_TreeNode = TreeNode(
    node_for=[PowerSystemResource],
    children="Contains_Measurements",
    label="=Contains_Measurements",
    tooltip="Measurement-PSR defines the measurements in the naming hierarchy.",
    add=[Measurement],
    move=[Measurement],
    icon_path=IMAGE_PATH)

BasePower_TreeNode = TreeNode(
    node_for=[BasePower],
    label="name",
    tooltip="The BasePower class defines the base power used in the per unit calculations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


PSRType_TreeNode = TreeNode(
    node_for=[PSRType],
    label="name",
    tooltip="Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PSRType_PowerSystemResource_TreeNode = TreeNode(
    node_for=[PSRType],
    children="PowerSystemResource",
    label="=PowerSystemResource",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

PsrList_TreeNode = TreeNode(
    node_for=[PsrList],
    label="name",
    tooltip="Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

PsrList_PowerSystemResources_TreeNode = TreeNode(
    node_for=[PsrList],
    children="PowerSystemResources",
    label="=PowerSystemResources",
    tooltip="",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

Company_TreeNode = TreeNode(
    node_for=[Company],
    label="name",
    tooltip="A company is a legal entity that owns and operates power system resources and is a party to interchange and transmission contracts.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Company_Operates_PSRs_TreeNode = TreeNode(
    node_for=[Company],
    children="Operates_PSRs",
    label="=Operates_PSRs",
    tooltip="A power system resource may be part of one or more companies",
    add=[PowerSystemResource],
    move=[PowerSystemResource],
    icon_path=IMAGE_PATH)

IdentifiedObject_TreeNode = TreeNode(
    node_for=[IdentifiedObject],
    label="name",
    tooltip="This is a root class to provide common naming attributes for all classes needing naming attributes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


Contingency_TreeNode = TreeNode(
    node_for=[Contingency],
    label="name",
    tooltip="An event threatening system reliability, consisting of one or more contingency elements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

Contingency_ContingencyElement_TreeNode = TreeNode(
    node_for=[Contingency],
    children="ContingencyElement",
    label="=ContingencyElement",
    tooltip="",
    add=[ContingencyElement],
    move=[ContingencyElement],
    icon_path=IMAGE_PATH)

ContingencyEquipment_TreeNode = TreeNode(
    node_for=[ContingencyEquipment],
    label="name",
    tooltip="A equipment to which the in service status is to change such as a power transformer or AC line segment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ContingencyElement_TreeNode = TreeNode(
    node_for=[ContingencyElement],
    label="name",
    tooltip="An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ClearanceTagType_TreeNode = TreeNode(
    node_for=[ClearanceTagType],
    label="name",
    tooltip="Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ClearanceTagType_ClearanceTags_TreeNode = TreeNode(
    node_for=[ClearanceTagType],
    children="ClearanceTags",
    label="=ClearanceTags",
    tooltip="",
    add=[ClearanceTag],
    move=[ClearanceTag],
    icon_path=IMAGE_PATH)

SwitchingOperation_TreeNode = TreeNode(
    node_for=[SwitchingOperation],
    label="name",
    tooltip="A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

SwitchingOperation_Switches_TreeNode = TreeNode(
    node_for=[SwitchingOperation],
    children="Switches",
    label="=Switches",
    tooltip="A switch may be operated by many schedules.",
    add=[Switch],
    move=[Switch],
    icon_path=IMAGE_PATH)

OutageSchedule_TreeNode = TreeNode(
    node_for=[OutageSchedule],
    label="name",
    tooltip="The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OutageSchedule_SwitchingOperations_TreeNode = TreeNode(
    node_for=[OutageSchedule],
    children="SwitchingOperations",
    label="=SwitchingOperations",
    tooltip="An OutageSchedule may operate many switches.",
    add=[SwitchingOperation],
    move=[SwitchingOperation],
    icon_path=IMAGE_PATH)

ClearanceTag_TreeNode = TreeNode(
    node_for=[ClearanceTag],
    label="name",
    tooltip="A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RemotePoint_TreeNode = TreeNode(
    node_for=[RemotePoint],
    label="name",
    tooltip="For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RemoteControl_TreeNode = TreeNode(
    node_for=[RemoteControl],
    label="name",
    tooltip="Remote controls are ouputs that are sent by the remote unit to actuators in the process.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RemoteSource_TreeNode = TreeNode(
    node_for=[RemoteSource],
    label="name",
    tooltip="Remote sources are state variables that are telemetered or calculated within the remote unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CommunicationLink_TreeNode = TreeNode(
    node_for=[CommunicationLink],
    label="name",
    tooltip="The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

CommunicationLink_Contain_RemoteUnits_TreeNode = TreeNode(
    node_for=[CommunicationLink],
    children="Contain_RemoteUnits",
    label="=Contain_RemoteUnits",
    tooltip="RTUs may be attached to communication links.",
    add=[RemoteUnit],
    move=[RemoteUnit],
    icon_path=IMAGE_PATH)

RemoteUnit_TreeNode = TreeNode(
    node_for=[RemoteUnit],
    label="name",
    tooltip="A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

RemoteUnit_MemberOf_CommunicationLinks_TreeNode = TreeNode(
    node_for=[RemoteUnit],
    children="MemberOf_CommunicationLinks",
    label="=MemberOf_CommunicationLinks",
    tooltip="RTUs may be attached to communication links.",
    add=[CommunicationLink],
    move=[CommunicationLink],
    icon_path=IMAGE_PATH)
RemoteUnit_Contains_RemotePoints_TreeNode = TreeNode(
    node_for=[RemoteUnit],
    children="Contains_RemotePoints",
    label="=Contains_RemotePoints",
    tooltip="",
    add=[RemotePoint],
    move=[RemotePoint],
    icon_path=IMAGE_PATH)

OperationalLimit_TreeNode = TreeNode(
    node_for=[OperationalLimit],
    label="name",
    tooltip="A value associated with a specific kind of limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BranchGroup_TreeNode = TreeNode(
    node_for=[BranchGroup],
    label="name",
    tooltip="A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BranchGroup_BranchGroupTerminal_TreeNode = TreeNode(
    node_for=[BranchGroup],
    children="BranchGroupTerminal",
    label="=BranchGroupTerminal",
    tooltip="",
    add=[BranchGroupTerminal],
    move=[BranchGroupTerminal],
    icon_path=IMAGE_PATH)

OperationalLimitType_TreeNode = TreeNode(
    node_for=[OperationalLimitType],
        tooltip="A type of limit.  The meaning of a specific limit is described in this class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperationalLimitType_OperationalLimit_TreeNode = TreeNode(
    node_for=[OperationalLimitType],
    children="OperationalLimit",
    label="=OperationalLimit",
    tooltip="",
    add=[OperationalLimit],
    move=[OperationalLimit],
    icon_path=IMAGE_PATH)

ActivePowerLimit_TreeNode = TreeNode(
    node_for=[ActivePowerLimit],
    label="name",
    tooltip="Limit on active power flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


CurrentLimit_TreeNode = TreeNode(
    node_for=[CurrentLimit],
    label="name",
    tooltip="Operational limit on current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


OperationalLimitSet_TreeNode = TreeNode(
    node_for=[OperationalLimitSet],
    label="name",
    tooltip="A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

OperationalLimitSet_OperationalLimitValue_TreeNode = TreeNode(
    node_for=[OperationalLimitSet],
    children="OperationalLimitValue",
    label="=OperationalLimitValue",
    tooltip="",
    add=[OperationalLimit],
    move=[OperationalLimit],
    icon_path=IMAGE_PATH)

VoltageLimit_TreeNode = TreeNode(
    node_for=[VoltageLimit],
    label="name",
    tooltip="Operational limit applied to voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


BranchGroupTerminal_TreeNode = TreeNode(
    node_for=[BranchGroupTerminal],
        tooltip="A specific directed terminal flow for a branch group.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ApparentPowerLimit_TreeNode = TreeNode(
    node_for=[ApparentPowerLimit],
    label="name",
    tooltip="Apparent power limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[ControlAreaGeneratingUnit],
        tooltip="A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlAreaGeneratingUnit_AltGeneratingUnitMeas_TreeNode = TreeNode(
    node_for=[ControlAreaGeneratingUnit],
    children="AltGeneratingUnitMeas",
    label="=AltGeneratingUnitMeas",
    tooltip="",
    add=[AltGeneratingUnitMeas],
    move=[AltGeneratingUnitMeas],
    icon_path=IMAGE_PATH)

ControlArea_TreeNode = TreeNode(
    node_for=[ControlArea],
    label="name",
    tooltip="A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ControlArea_BusNameMarker_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="BusNameMarker",
    label="=BusNameMarker",
    tooltip="",
    add=[BusNameMarker],
    move=[BusNameMarker],
    icon_path=IMAGE_PATH)
ControlArea_TopologicalNode_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="TopologicalNode",
    label="=TopologicalNode",
    tooltip="",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)
ControlArea_ControlAreaGeneratingUnit_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="ControlAreaGeneratingUnit",
    label="=ControlAreaGeneratingUnit",
    tooltip="",
    add=[ControlAreaGeneratingUnit],
    move=[ControlAreaGeneratingUnit],
    icon_path=IMAGE_PATH)
ControlArea_TieFlow_TreeNode = TreeNode(
    node_for=[ControlArea],
    children="TieFlow",
    label="=TieFlow",
    tooltip="",
    add=[TieFlow],
    move=[TieFlow],
    icon_path=IMAGE_PATH)

AltGeneratingUnitMeas_TreeNode = TreeNode(
    node_for=[AltGeneratingUnitMeas],
        tooltip="A prioritized measurement to be used for the generating unit in the control area specificaiton.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TieFlow_TreeNode = TreeNode(
    node_for=[TieFlow],
        tooltip="A flow specification in terms of location and direction for a control area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TieFlow_AltTieMeas_TreeNode = TreeNode(
    node_for=[TieFlow],
    children="AltTieMeas",
    label="=AltTieMeas",
    tooltip="",
    add=[AltTieMeas],
    move=[AltTieMeas],
    icon_path=IMAGE_PATH)

AltTieMeas_TreeNode = TreeNode(
    node_for=[AltTieMeas],
        tooltip="A prioritized measurement to be used for the tie flow as part of the control area specification.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentBranch_TreeNode = TreeNode(
    node_for=[EquivalentBranch],
    label="name",
    tooltip="The class represents equivalent branches.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentShunt_TreeNode = TreeNode(
    node_for=[EquivalentShunt],
    label="name",
    tooltip="The class represents equivalent shunts.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


EquivalentNetwork_TreeNode = TreeNode(
    node_for=[EquivalentNetwork],
    label="name",
    tooltip="A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

EquivalentNetwork_EquivalentEquipments_TreeNode = TreeNode(
    node_for=[EquivalentNetwork],
    children="EquivalentEquipments",
    label="=EquivalentEquipments",
    tooltip="",
    add=[EquivalentEquipment],
    move=[EquivalentEquipment],
    icon_path=IMAGE_PATH)

EquivalentEquipment_TreeNode = TreeNode(
    node_for=[EquivalentEquipment],
    label="name",
    tooltip="The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


TopologicalNode_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    label="name",
    tooltip="A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TopologicalNode_ConnectivityNodes_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    children="ConnectivityNodes",
    label="=ConnectivityNodes",
    tooltip="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)
TopologicalNode_Terminal_TreeNode = TreeNode(
    node_for=[TopologicalNode],
    children="Terminal",
    label="=Terminal",
    tooltip="",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)

TopologicalIsland_TreeNode = TreeNode(
    node_for=[TopologicalIsland],
    label="name",
    tooltip="An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

TopologicalIsland_TopologicalNodes_TreeNode = TreeNode(
    node_for=[TopologicalIsland],
    children="TopologicalNodes",
    label="=TopologicalNodes",
    tooltip="A topological node belongs to a topological island",
    add=[TopologicalNode],
    move=[TopologicalNode],
    icon_path=IMAGE_PATH)

ConnectivityNode_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    label="name",
    tooltip="Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ConnectivityNode_Terminals_TreeNode = TreeNode(
    node_for=[ConnectivityNode],
    children="Terminals",
    label="=Terminals",
    tooltip="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.",
    add=[Terminal],
    move=[Terminal],
    icon_path=IMAGE_PATH)

BusNameMarker_TreeNode = TreeNode(
    node_for=[BusNameMarker],
    label="name",
    tooltip="Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

BusNameMarker_ConnectivityNode_TreeNode = TreeNode(
    node_for=[BusNameMarker],
    children="ConnectivityNode",
    label="=ConnectivityNode",
    tooltip="",
    add=[ConnectivityNode],
    move=[ConnectivityNode],
    icon_path=IMAGE_PATH)

SynchrocheckRelay_TreeNode = TreeNode(
    node_for=[SynchrocheckRelay],
    label="name",
    tooltip="A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


ProtectionEquipment_TreeNode = TreeNode(
    node_for=[ProtectionEquipment],
    label="name",
    tooltip="An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)

ProtectionEquipment_Operates_Breakers_TreeNode = TreeNode(
    node_for=[ProtectionEquipment],
    children="Operates_Breakers",
    label="=Operates_Breakers",
    tooltip="Circuit breakers may be operated by protection relays.",
    add=[ProtectedSwitch],
    move=[ProtectedSwitch],
    icon_path=IMAGE_PATH)
ProtectionEquipment_ConductingEquipments_TreeNode = TreeNode(
    node_for=[ProtectionEquipment],
    children="ConductingEquipments",
    label="=ConductingEquipments",
    tooltip="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.",
    add=[ConductingEquipment],
    move=[ConductingEquipment],
    icon_path=IMAGE_PATH)

CurrentRelay_TreeNode = TreeNode(
    node_for=[CurrentRelay],
    label="name",
    tooltip="A device that checks current flow values in any direction or designated direction",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)


RecloseSequence_TreeNode = TreeNode(
    node_for=[RecloseSequence],
    label="name",
    tooltip="A reclose sequence (open and close) is defined for each possible reclosure of a breaker.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"),
    icon_path=IMAGE_PATH)



#------------------------------------------------------------------------------
#  Tree node list:
#------------------------------------------------------------------------------


tree_nodes = [
    Root_TreeNode,
    Model_TreeNode,
    Model_Contains_TreeNode,
    IEC61970CIMVersion_TreeNode,
    MutualCoupling_TreeNode,
    Quality61850_TreeNode,
    MeasurementValueQuality_TreeNode,
    Analog_TreeNode,
    Analog_Contain_MeasurementValues_TreeNode,
    Analog_LimitSets_TreeNode,
    AccumulatorValue_TreeNode,
    Season_TreeNode,
    Season_SeasonDayTypeSchedules_TreeNode,
    IrregularTimePoint_TreeNode,
    OperatingShare_TreeNode,
    CurveData_TreeNode,
    RegularTimePoint_TreeNode,
    IdentifiedObject_TreeNode,
    Contingency_TreeNode,
    Contingency_ContingencyElement_TreeNode,
    ContingencyElement_TreeNode,
    ClearanceTagType_TreeNode,
    ClearanceTagType_ClearanceTags_TreeNode,
    SwitchingOperation_TreeNode,
    SwitchingOperation_Switches_TreeNode,
    ClearanceTag_TreeNode,
    RemotePoint_TreeNode,
    RemoteControl_TreeNode,
    RemoteSource_TreeNode,
    OperationalLimit_TreeNode,
    BranchGroup_TreeNode,
    BranchGroup_BranchGroupTerminal_TreeNode,
    OperationalLimitType_TreeNode,
    OperationalLimitType_OperationalLimit_TreeNode,
    ActivePowerLimit_TreeNode,
    CurrentLimit_TreeNode,
    OperationalLimitSet_TreeNode,
    OperationalLimitSet_OperationalLimitValue_TreeNode,
    VoltageLimit_TreeNode,
    BranchGroupTerminal_TreeNode,
    ApparentPowerLimit_TreeNode,
    ControlAreaGeneratingUnit_TreeNode,
    ControlAreaGeneratingUnit_AltGeneratingUnitMeas_TreeNode,
    AltGeneratingUnitMeas_TreeNode,
    TieFlow_TreeNode,
    TieFlow_AltTieMeas_TreeNode,
    AltTieMeas_TreeNode,
    TopologicalNode_TreeNode,
    TopologicalNode_ConnectivityNodes_TreeNode,
    TopologicalNode_Terminal_TreeNode,
    TopologicalIsland_TreeNode,
    TopologicalIsland_TopologicalNodes_TreeNode,
    ConnectivityNode_TreeNode,
    ConnectivityNode_Terminals_TreeNode,
    BusNameMarker_TreeNode,
    BusNameMarker_ConnectivityNode_TreeNode,
    RecloseSequence_TreeNode,
    GroundDisconnector_TreeNode,
    WireType_TreeNode,
    WireType_WireArrangements_TreeNode,
    ProtectedSwitch_TreeNode,
    ProtectedSwitch_OperatedBy_ProtectionEquipments_TreeNode,
    ProtectedSwitch_RecloseSequences_TreeNode,
    Jumper_TreeNode,
    WireArrangement_TreeNode,
    Fuse_TreeNode,
    WindingTest_TreeNode,
    Disconnector_TreeNode,
    ConductorType_TreeNode,
    ConductorType_Conductors_TreeNode,
    ConductorType_WireArrangements_TreeNode,
    ReactiveCapabilityCurve_TreeNode,
    ReactiveCapabilityCurve_SynchronousMachines_TreeNode,
    ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_TreeNode,
    NuclearGeneratingUnit_TreeNode,
    StartIgnFuelCurve_TreeNode,
    HydroGeneratingEfficiencyCurve_TreeNode,
    TargetLevelSchedule_TreeNode,
    GrossToNetActivePowerCurve_TreeNode,
    IncrementalHeatRateCurve_TreeNode,
    HeatInputCurve_TreeNode,
    StartRampCurve_TreeNode,
    ShutdownCurve_TreeNode,
    StartupModel_TreeNode,
    EmissionCurve_TreeNode,
    GenUnitOpCostCurve_TreeNode,
    HydroGeneratingUnit_TreeNode,
    HydroGeneratingUnit_HydroGeneratingEfficiencyCurves_TreeNode,
    HydroGeneratingUnit_TailbayLossCurve_TreeNode,
    LevelVsVolumeCurve_TreeNode,
    ThermalGeneratingUnit_TreeNode,
    ThermalGeneratingUnit_FuelAllocationSchedules_TreeNode,
    ThermalGeneratingUnit_EmissionCurves_TreeNode,
    ThermalGeneratingUnit_EmmissionAccounts_TreeNode,
    ThermalGeneratingUnit_FossilFuels_TreeNode,
    FossilFuel_TreeNode,
    FossilFuel_FuelAllocationSchedule_TreeNode,
    FuelAllocationSchedule_TreeNode,
    EmissionAccount_TreeNode,
    TailbayLossCurve_TreeNode,
    PenstockLossCurve_TreeNode,
    StartMainFuelCurve_TreeNode,
    HeatRateCurve_TreeNode,
    CTTempActivePowerCurve_TreeNode,
    Discrete_TreeNode,
    Discrete_Contain_MeasurementValues_TreeNode,
    Measurement_TreeNode,
    SetPoint_TreeNode,
    Control_TreeNode,
    ControlType_TreeNode,
    ControlType_Controls_TreeNode,
    DiscreteValue_TreeNode,
    Accumulator_TreeNode,
    Accumulator_Contain_MeasurementValues_TreeNode,
    Accumulator_LimitSets_TreeNode,
    LimitSet_TreeNode,
    AnalogLimit_TreeNode,
    MeasurementValue_TreeNode,
    ValueAliasSet_TreeNode,
    ValueAliasSet_Values_TreeNode,
    ValueAliasSet_Commands_TreeNode,
    ValueAliasSet_Measurements_TreeNode,
    StringMeasurementValue_TreeNode,
    Limit_TreeNode,
    MeasurementType_TreeNode,
    MeasurementType_Measurements_TreeNode,
    AccumulatorLimit_TreeNode,
    StringMeasurement_TreeNode,
    StringMeasurement_Contains_MeasurementValues_TreeNode,
    ValueToAlias_TreeNode,
    AnalogValue_TreeNode,
    AnalogValue_AltGeneratingUnit_TreeNode,
    AnalogValue_AltTieMeas_TreeNode,
    MeasurementValueSource_TreeNode,
    MeasurementValueSource_MeasurementValues_TreeNode,
    AccumulatorLimitSet_TreeNode,
    AccumulatorLimitSet_Measurements_TreeNode,
    AccumulatorLimitSet_Limits_TreeNode,
    AnalogLimitSet_TreeNode,
    AnalogLimitSet_Limits_TreeNode,
    AnalogLimitSet_Measurements_TreeNode,
    Command_TreeNode,
    LoadResponseCharacteristic_TreeNode,
    LoadResponseCharacteristic_EnergyConsumer_TreeNode,
    DayType_TreeNode,
    DayType_SeasonDayTypeSchedules_TreeNode,
    LoadGroup_TreeNode,
    NonConformLoadGroup_TreeNode,
    NonConformLoadGroup_NonConformLoadSchedules_TreeNode,
    NonConformLoadGroup_EnergyConsumers_TreeNode,
    EnergyArea_TreeNode,
    InductionMotorLoad_TreeNode,
    Curve_TreeNode,
    Curve_CurveScheduleDatas_TreeNode,
    ReportingGroup_TreeNode,
    ReportingGroup_PowerSystemResource_TreeNode,
    ReportingGroup_BusNameMarker_TreeNode,
    ReportingGroup_TopologicalNode_TreeNode,
    ModelingAuthoritySet_TreeNode,
    ModelingAuthoritySet_IdentifiedObjects_TreeNode,
    OperatingParticipant_TreeNode,
    OperatingParticipant_OperatingShare_TreeNode,
    ReportingSuperGroup_TreeNode,
    ReportingSuperGroup_ReportingGroup_TreeNode,
    GeographicalRegion_TreeNode,
    GeographicalRegion_Regions_TreeNode,
    Unit_TreeNode,
    Unit_Controls_TreeNode,
    Unit_ProtectionEquipments_TreeNode,
    Unit_Measurements_TreeNode,
    ModelingAuthority_TreeNode,
    ModelingAuthority_ModelingAuthoritySets_TreeNode,
    BaseVoltage_TreeNode,
    BaseVoltage_ConductingEquipment_TreeNode,
    BaseVoltage_VoltageLevel_TreeNode,
    BasicIntervalSchedule_TreeNode,
    RegularIntervalSchedule_TreeNode,
    RegularIntervalSchedule_TimePoints_TreeNode,
    IrregularIntervalSchedule_TreeNode,
    IrregularIntervalSchedule_TimePoints_TreeNode,
    Terminal_TreeNode,
    Terminal_TieFlow_TreeNode,
    Terminal_OperationalLimitSet_TreeNode,
    Terminal_BranchGroupTerminal_TreeNode,
    Terminal_RegulatingControl_TreeNode,
    Terminal_Measurements_TreeNode,
    SubGeographicalRegion_TreeNode,
    SubGeographicalRegion_Lines_TreeNode,
    SubGeographicalRegion_Substations_TreeNode,
    PowerSystemResource_TreeNode,
    PowerSystemResource_OperatedBy_Companies_TreeNode,
    PowerSystemResource_ReportingGroup_TreeNode,
    PowerSystemResource_OperatingShare_TreeNode,
    PowerSystemResource_PsrLists_TreeNode,
    PowerSystemResource_Contains_Measurements_TreeNode,
    BasePower_TreeNode,
    PSRType_TreeNode,
    PSRType_PowerSystemResource_TreeNode,
    PsrList_TreeNode,
    PsrList_PowerSystemResources_TreeNode,
    Company_TreeNode,
    Company_Operates_PSRs_TreeNode,
    ContingencyEquipment_TreeNode,
    OutageSchedule_TreeNode,
    OutageSchedule_SwitchingOperations_TreeNode,
    CommunicationLink_TreeNode,
    CommunicationLink_Contain_RemoteUnits_TreeNode,
    RemoteUnit_TreeNode,
    RemoteUnit_MemberOf_CommunicationLinks_TreeNode,
    RemoteUnit_Contains_RemotePoints_TreeNode,
    ControlArea_TreeNode,
    ControlArea_BusNameMarker_TreeNode,
    ControlArea_TopologicalNode_TreeNode,
    ControlArea_ControlAreaGeneratingUnit_TreeNode,
    ControlArea_TieFlow_TreeNode,
    ProtectionEquipment_TreeNode,
    ProtectionEquipment_Operates_Breakers_TreeNode,
    ProtectionEquipment_ConductingEquipments_TreeNode,
    CurrentRelay_TreeNode,
    RegulationSchedule_TreeNode,
    RegulationSchedule_RegulatingControl_TreeNode,
    RegulationSchedule_VoltageControlZones_TreeNode,
    Breaker_TreeNode,
    VoltageControlZone_TreeNode,
    LoadBreakSwitch_TreeNode,
    DCLineSegment_TreeNode,
    TapChanger_TreeNode,
    CompositeSwitch_TreeNode,
    CompositeSwitch_Switches_TreeNode,
    PowerTransformer_TreeNode,
    PowerTransformer_Contains_TransformerWindings_TreeNode,
    ACLineSegment_TreeNode,
    ACLineSegment_HasFirst_MutualCoupling_TreeNode,
    ACLineSegment_HasSecond_MutualCoupling_TreeNode,
    HeatExchanger_TreeNode,
    RegulatingControl_TreeNode,
    RegulatingControl_RegulatingCondEq_TreeNode,
    RegulatingControl_TapChanger_TreeNode,
    GeneratingUnit_TreeNode,
    GeneratingUnit_ControlAreaGeneratingUnit_TreeNode,
    GeneratingUnit_GrossToNetActivePowerCurves_TreeNode,
    GeneratingUnit_Contains_SynchronousMachines_TreeNode,
    GeneratingUnit_GenUnitOpCostCurves_TreeNode,
    AirCompressor_TreeNode,
    CombinedCyclePlant_TreeNode,
    CombinedCyclePlant_Contain_ThermalGeneratingUnits_TreeNode,
    HydroPump_TreeNode,
    HydroPowerPlant_TreeNode,
    HydroPowerPlant_Contain_HydroGeneratingUnits_TreeNode,
    HydroPowerPlant_Contain_HydroPumps_TreeNode,
    CAESPlant_TreeNode,
    InflowForecast_TreeNode,
    SteamSendoutSchedule_TreeNode,
    Reservoir_TreeNode,
    Reservoir_LevelVsVolumeCurve_TreeNode,
    Reservoir_InflowForecast_TreeNode,
    Reservoir_SpillsInto_TreeNode,
    Reservoir_HydroPowerPlants_TreeNode,
    Reservoir_UpstreamFrom_TreeNode,
    HydroPumpOpSchedule_TreeNode,
    GenUnitOpSchedule_TreeNode,
    CogenerationPlant_TreeNode,
    CogenerationPlant_Contain_ThermalGeneratingUnits_TreeNode,
    PrimeMover_TreeNode,
    PrimeMover_Drives_SynchronousMachines_TreeNode,
    CombustionTurbine_TreeNode,
    HydroTurbine_TreeNode,
    SteamSupply_TreeNode,
    SteamSupply_SteamTurbines_TreeNode,
    SubLoadArea_TreeNode,
    SubLoadArea_LoadGroups_TreeNode,
    Load_TreeNode,
    ConformLoadGroup_TreeNode,
    ConformLoadGroup_EnergyConsumers_TreeNode,
    ConformLoadGroup_ConformLoadSchedules_TreeNode,
    LoadArea_TreeNode,
    LoadArea_SubLoadAreas_TreeNode,
    PowerCutZone_TreeNode,
    PowerCutZone_EnergyConsumers_TreeNode,
    CustomerLoad_TreeNode,
    SeasonDayTypeSchedule_TreeNode,
    ConductingEquipment_TreeNode,
    ConductingEquipment_Terminals_TreeNode,
    ConductingEquipment_ProtectionEquipments_TreeNode,
    ConductingEquipment_ClearanceTags_TreeNode,
    ConnectivityNodeContainer_TreeNode,
    ConnectivityNodeContainer_TopologicalNode_TreeNode,
    ConnectivityNodeContainer_ConnectivityNodes_TreeNode,
    EquipmentContainer_TreeNode,
    EquipmentContainer_Contains_Equipments_TreeNode,
    Equipment_TreeNode,
    Equipment_OperationalLimitSet_TreeNode,
    Equipment_ContingencyEquipment_TreeNode,
    Bay_TreeNode,
    EquivalentNetwork_TreeNode,
    EquivalentNetwork_EquivalentEquipments_TreeNode,
    EquivalentEquipment_TreeNode,
    SynchrocheckRelay_TreeNode,
    TransformerWinding_TreeNode,
    TransformerWinding_To_WindingTest_TreeNode,
    TransformerWinding_From_WindingTest_TreeNode,
    TransformerWinding_TapChangers_TreeNode,
    EnergySource_TreeNode,
    SeriesCompensator_TreeNode,
    RegulatingCondEq_TreeNode,
    RegulatingCondEq_Controls_TreeNode,
    Conductor_TreeNode,
    Line_TreeNode,
    Ground_TreeNode,
    ShuntCompensator_TreeNode,
    RectifierInverter_TreeNode,
    EnergyConsumer_TreeNode,
    Switch_TreeNode,
    Switch_SwitchingOperations_TreeNode,
    SynchronousMachine_TreeNode,
    SynchronousMachine_ReactiveCapabilityCurves_TreeNode,
    SynchronousMachine_DrivenBy_PrimeMover_TreeNode,
    Connector_TreeNode,
    StaticVarCompensator_TreeNode,
    Junction_TreeNode,
    Plant_TreeNode,
    SteamTurbine_TreeNode,
    SteamTurbine_SteamSupplys_TreeNode,
    PWRSteamSupply_TreeNode,
    BWRSteamSupply_TreeNode,
    FossilSteamSupply_TreeNode,
    Subcritical_TreeNode,
    ConformLoad_TreeNode,
    ConformLoadSchedule_TreeNode,
    StationSupply_TreeNode,
    NonConformLoadSchedule_TreeNode,
    NonConformLoad_TreeNode,
    VoltageLevel_TreeNode,
    VoltageLevel_Contains_Bays_TreeNode,
    Substation_TreeNode,
    Substation_Contains_VoltageLevels_TreeNode,
    Substation_Contains_Bays_TreeNode,
    EquivalentBranch_TreeNode,
    EquivalentShunt_TreeNode,
    FrequencyConverter_TreeNode,
    BusbarSection_TreeNode,
    Supercritical_TreeNode,
    HeatRecoveryBoiler_TreeNode,
    HeatRecoveryBoiler_CombustionTurbines_TreeNode,
    DrumBoiler_TreeNode,
]
tree_nodes.reverse()

#------------------------------------------------------------------------------
#  CIM13 Tree Editor:
#------------------------------------------------------------------------------

CIM13TreeEditor = TreeEditor(nodes=tree_nodes, editable=True)

#------------------------------------------------------------------------------
#  Begin "CIM13TreeEditor" user region:
#------------------------------------------------------------------------------

class RegionContainer(HasTraits):

#    elements = List( Instance(Root) )
    uri_element_map = Dict(Str, Root)

#    regions = Property(depends_on=["elements", "elements_items"])
    regions = Property(depends_on=["uri_element_map", "uri_element_map_items"])

    def _get_regions(self):
        """ Property getter.
        """
        print "GETTING ELEMENTS"
#        return [e for e in self.elements if isinstance(e, GeographicalRegion)]
        return [e for e in self.uri_element_map.values() \
            if isinstance(e, GeographicalRegion)]

RegionContainerTreeNode = TreeNode(node_for=[RegionContainer],
    label="=Regions", children="regions", view=View())

class TreeRoot(HasTraits):

    # Root element of the model tree.
    root = Instance(HasTraits)

    # Traits view to display.
    view = View(
        Item('root',
            editor=TreeEditor(nodes=[RegionContainerTreeNode] + tree_nodes),
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True,
        buttons   = ["OK", "Cancel"]
    )

    def _root_default(self):
        """ Trait initialiser.
        """
        return RegionContainer(uri_element_map={ "gr1": GeographicalRegion() })

#------------------------------------------------------------------------------
#  End "CIM13TreeEditor" user region:
#------------------------------------------------------------------------------

if __name__ == "__main__":
    root = TreeRoot()
    root.configure_traits()

# EOF -------------------------------------------------------------------------
