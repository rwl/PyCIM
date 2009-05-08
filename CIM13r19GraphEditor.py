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

""" Defines a graph editor for CIM13r19.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Str, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group

from enthought.traits.ui.menu \
    import Action, Menu

from godot.graph_editor import GraphNode, GraphEditor

from CIM13r19 import *
from CIM13r19.Wires import *
from CIM13r19.Generation import *
from CIM13r19.Meas import *
from CIM13r19.LoadModel import *
from CIM13r19.Core import *
from CIM13r19.Contingency import *
from CIM13r19.Outage import *
from CIM13r19.SCADA import *
from CIM13r19.Domain import *
from CIM13r19.OperationalLimits import *
from CIM13r19.ControlArea import *
from CIM13r19.Equivalents import *
from CIM13r19.Topology import *
from CIM13r19.Protection import *
from CIM13r19.Generation.Production import *
from CIM13r19.Generation.GenerationDynamics import *

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------
# <<< constants
# @generated
IMAGE_PATH = ""
# >>> constants

#------------------------------------------------------------------------------
#  Graph nodes:
#------------------------------------------------------------------------------

Element_GraphNode = GraphNode(
    node_for=[Element],
        tooltip="Base class for Common Information Model elements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CommonInformationModel_GraphNode = GraphNode(
    node_for=[CommonInformationModel],
        tooltip="Defines a container of model elements conforming to IEC standard 61970.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IEC61970CIMVersion_GraphNode = GraphNode(
    node_for=[IEC61970CIMVersion],
        tooltip="This is the IEC 61970 CIM version number assigned to this UML model file.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegulationSchedule_GraphNode = GraphNode(
    node_for=[RegulationSchedule],
    label="name",
    tooltip="A pre-established pattern over time for a controlled variable, e.g., busbar voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GroundDisconnector_GraphNode = GraphNode(
    node_for=[GroundDisconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TransformerWinding_GraphNode = GraphNode(
    node_for=[TransformerWinding],
    label="name",
    tooltip="A winding is associated with each defined terminal of a transformer (or phase shifter).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EnergySource_GraphNode = GraphNode(
    node_for=[EnergySource],
    label="name",
    tooltip="A generic equivalent for an energy supplier on a transmission or distribution voltage level.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SeriesCompensator_GraphNode = GraphNode(
    node_for=[SeriesCompensator],
    label="name",
    tooltip="A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

WireType_GraphNode = GraphNode(
    node_for=[WireType],
    label="name",
    tooltip="Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Breaker_GraphNode = GraphNode(
    node_for=[Breaker],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

VoltageControlZone_GraphNode = GraphNode(
    node_for=[VoltageControlZone],
    label="name",
    tooltip="An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

FrequencyConverter_GraphNode = GraphNode(
    node_for=[FrequencyConverter],
    label="name",
    tooltip="A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegulatingCondEq_GraphNode = GraphNode(
    node_for=[RegulatingCondEq],
    label="name",
    tooltip="RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Conductor_GraphNode = GraphNode(
    node_for=[Conductor],
    label="name",
    tooltip="Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadBreakSwitch_GraphNode = GraphNode(
    node_for=[LoadBreakSwitch],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ProtectedSwitch_GraphNode = GraphNode(
    node_for=[ProtectedSwitch],
    label="name",
    tooltip="A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Line_GraphNode = GraphNode(
    node_for=[Line],
    label="name",
    tooltip="A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Ground_GraphNode = GraphNode(
    node_for=[Ground],
    label="name",
    tooltip="A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Jumper_GraphNode = GraphNode(
    node_for=[Jumper],
    label="name",
    tooltip="A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

DCLineSegment_GraphNode = GraphNode(
    node_for=[DCLineSegment],
    label="name",
    tooltip="A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TapChanger_GraphNode = GraphNode(
    node_for=[TapChanger],
    label="name",
    tooltip="Mechanism for changing transformer winding tap positions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CompositeSwitch_GraphNode = GraphNode(
    node_for=[CompositeSwitch],
    label="name",
    tooltip="A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

WireArrangement_GraphNode = GraphNode(
    node_for=[WireArrangement],
    label="name",
    tooltip="Identification, spacing and configuration of the wires of a ConductorType, with reference to their type.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PowerTransformer_GraphNode = GraphNode(
    node_for=[PowerTransformer],
    label="name",
    tooltip="An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BusbarSection_GraphNode = GraphNode(
    node_for=[BusbarSection],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ACLineSegment_GraphNode = GraphNode(
    node_for=[ACLineSegment],
    label="name",
    tooltip="A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MutualCoupling_GraphNode = GraphNode(
    node_for=[MutualCoupling],
        tooltip="This class represents the zero sequence line mutual coupling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ShuntCompensator_GraphNode = GraphNode(
    node_for=[ShuntCompensator],
    label="name",
    tooltip="A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Fuse_GraphNode = GraphNode(
    node_for=[Fuse],
    label="name",
    tooltip="An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RectifierInverter_GraphNode = GraphNode(
    node_for=[RectifierInverter],
    label="name",
    tooltip="Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HeatExchanger_GraphNode = GraphNode(
    node_for=[HeatExchanger],
    label="name",
    tooltip="Equipment for the cooling of electrical equipment and the extraction of heat",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EnergyConsumer_GraphNode = GraphNode(
    node_for=[EnergyConsumer],
    label="name",
    tooltip="Generic user of energy - a  point of consumption on the power system model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Switch_GraphNode = GraphNode(
    node_for=[Switch],
    label="name",
    tooltip="A generic device designed to close, or open, or both, one or more electric circuits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SynchronousMachine_GraphNode = GraphNode(
    node_for=[SynchronousMachine],
    label="name",
    tooltip="An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegulatingControl_GraphNode = GraphNode(
    node_for=[RegulatingControl],
    label="name",
    tooltip="Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Connector_GraphNode = GraphNode(
    node_for=[Connector],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StaticVarCompensator_GraphNode = GraphNode(
    node_for=[StaticVarCompensator],
    label="name",
    tooltip="A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Junction_GraphNode = GraphNode(
    node_for=[Junction],
    label="name",
    tooltip="A point where one or more conducting equipments are connected with zero resistance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

WindingTest_GraphNode = GraphNode(
    node_for=[WindingTest],
    label="name",
    tooltip="Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Disconnector_GraphNode = GraphNode(
    node_for=[Disconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConductorType_GraphNode = GraphNode(
    node_for=[ConductorType],
    label="name",
    tooltip="Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Plant_GraphNode = GraphNode(
    node_for=[Plant],
    label="name",
    tooltip="A Plant is a collection of equipment for purposes of generation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ReactiveCapabilityCurve_GraphNode = GraphNode(
    node_for=[ReactiveCapabilityCurve],
    label="name",
    tooltip="Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NuclearGeneratingUnit_GraphNode = GraphNode(
    node_for=[NuclearGeneratingUnit],
    label="name",
    tooltip="A nuclear generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GeneratingUnit_GraphNode = GraphNode(
    node_for=[GeneratingUnit],
    label="name",
    tooltip="A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StartIgnFuelCurve_GraphNode = GraphNode(
    node_for=[StartIgnFuelCurve],
    label="name",
    tooltip="The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroGeneratingEfficiencyCurve_GraphNode = GraphNode(
    node_for=[HydroGeneratingEfficiencyCurve],
    label="name",
    tooltip="Relationship between unit efficiency in percent and unit output active power for a given net head in meters. The relationship between efficiency, discharge, head, and power output is expressed as follows:   E =KP/HQ Where:  (E=percentage)  (P=active power)  (H=height)  (Q=volume/time unit)  (K=constant) For example, a curve instance for a given net head could relate efficiency (Y-axis) versus active power output (X-axis) or versus discharge on the X-axis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TargetLevelSchedule_GraphNode = GraphNode(
    node_for=[TargetLevelSchedule],
    label="name",
    tooltip="Reservoir water level targets from advanced studies or 'rule curves'. Typically in one hour increments for up to 10 days",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GrossToNetActivePowerCurve_GraphNode = GraphNode(
    node_for=[GrossToNetActivePowerCurve],
    label="name",
    tooltip="Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IncrementalHeatRateCurve_GraphNode = GraphNode(
    node_for=[IncrementalHeatRateCurve],
    label="name",
    tooltip="Relationship between unit incremental heat rate in (delta energy/time) per (delta active power) and unit output in active power. The IHR curve represents the slope of the HeatInputCurve. Note that the 'incremental heat rate' and the 'heat rate' have the same engineering units.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HeatInputCurve_GraphNode = GraphNode(
    node_for=[HeatInputCurve],
    label="name",
    tooltip="Relationship between unit heat input in energy per time for main fuel (Y1-axis) and supplemental fuel (Y2-axis) versus unit output in active power (X-axis). The quantity of main fuel used to sustain generation at this output level is prorated for throttling between definition points. The quantity of supplemental fuel used at this output level is fixed and not prorated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StartRampCurve_GraphNode = GraphNode(
    node_for=[StartRampCurve],
    label="name",
    tooltip="Rate in gross active power/minute (Y-axis) at which a unit can be loaded versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AirCompressor_GraphNode = GraphNode(
    node_for=[AirCompressor],
    label="name",
    tooltip="Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ShutdownCurve_GraphNode = GraphNode(
    node_for=[ShutdownCurve],
    label="name",
    tooltip="Relationship between the rate in gross active power/minute (Y-axis) at which a unit should be shutdown and its present gross MW output (X-axis)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CombinedCyclePlant_GraphNode = GraphNode(
    node_for=[CombinedCyclePlant],
    label="name",
    tooltip="A set of combustion turbines and steam turbines where the exhaust heat from the combustion turbines is recovered to make steam for the steam turbines, resulting in greater overall plant efficiency",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StartupModel_GraphNode = GraphNode(
    node_for=[StartupModel],
    label="name",
    tooltip="Unit start up characteristics depending on how long the unit has been off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroPump_GraphNode = GraphNode(
    node_for=[HydroPump],
    label="name",
    tooltip="A synchronous motor-driven pump, typically associated with a pumped storage plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EmissionCurve_GraphNode = GraphNode(
    node_for=[EmissionCurve],
    label="name",
    tooltip="Relationship between the unit's emission rate in units of mass per hour (Y-axis) and output active power (X-axis) for a given type of emission. This curve applies when only one type of fuel is being burned.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GenUnitOpCostCurve_GraphNode = GraphNode(
    node_for=[GenUnitOpCostCurve],
    label="name",
    tooltip="Relationship between unit operating cost (Y-axis) and unit output active power (X-axis). The operating cost curve for thermal units is derived from heat input and fuel costs. The operating cost curve for hydro units is derived from water flow rates and equivalent water costs.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroPowerPlant_GraphNode = GraphNode(
    node_for=[HydroPowerPlant],
    label="name",
    tooltip="A hydro power station which can generate or pump. When generating, the generator turbines receive there water from an upper reservoir. When pumping, the pumps receive their water from a lower reservoir.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroGeneratingUnit_GraphNode = GraphNode(
    node_for=[HydroGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CAESPlant_GraphNode = GraphNode(
    node_for=[CAESPlant],
    label="name",
    tooltip="Compressed air energy storage plant",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LevelVsVolumeCurve_GraphNode = GraphNode(
    node_for=[LevelVsVolumeCurve],
    label="name",
    tooltip="Relationship between reservoir volume and reservoir level. The  volume is at the y-axis and the reservoir level at the x-axis.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

InflowForecast_GraphNode = GraphNode(
    node_for=[InflowForecast],
    label="name",
    tooltip="Natural water inflow to a reservoir, usually forecasted from predicted rain and snowmelt. Typically in one hour increments for up to 10 days. The forecast is given in average cubic meters per second over the time increment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SteamSendoutSchedule_GraphNode = GraphNode(
    node_for=[SteamSendoutSchedule],
    label="name",
    tooltip="The cogeneration plant's steam sendout schedule in volume per time unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ThermalGeneratingUnit_GraphNode = GraphNode(
    node_for=[ThermalGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

FossilFuel_GraphNode = GraphNode(
    node_for=[FossilFuel],
    label="name",
    tooltip="The fossil fuel consumed by the non-nuclear thermal generating units, e.g., coal, oil, gas",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

FuelAllocationSchedule_GraphNode = GraphNode(
    node_for=[FuelAllocationSchedule],
    label="name",
    tooltip="The amount of fuel of a given type which is allocated for consumption over a specified period of time",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EmissionAccount_GraphNode = GraphNode(
    node_for=[EmissionAccount],
    label="name",
    tooltip="Accounts for tracking emissions usage and credits for thermal generating units. A unit may have zero or more emission accounts, and will typically have one for tracking usage and one for tracking credits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TailbayLossCurve_GraphNode = GraphNode(
    node_for=[TailbayLossCurve],
    label="name",
    tooltip="Relationship between tailbay head loss hight (y-axis) and the total discharge into the power station's tailbay volume per time unit (x-axis) . There could be more than one curve depending on the level of the tailbay reservoir or river level",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PenstockLossCurve_GraphNode = GraphNode(
    node_for=[PenstockLossCurve],
    label="name",
    tooltip="Relationship between penstock head loss (in meters) and  total discharge through the penstock (in cubic meters per second). One or more turbines may be connected to the same penstock.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StartMainFuelCurve_GraphNode = GraphNode(
    node_for=[StartMainFuelCurve],
    label="name",
    tooltip="The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power consumed versus the number of hours (X-axis) the unit was off line",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Reservoir_GraphNode = GraphNode(
    node_for=[Reservoir],
    label="name",
    tooltip="A water storage facility within a hydro system, including: ponds, lakes, lagoons, and rivers. The storage is usually behind some type of dam.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroPumpOpSchedule_GraphNode = GraphNode(
    node_for=[HydroPumpOpSchedule],
    label="name",
    tooltip="The hydro pump's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses.The unit's operating schedule status is typically given as: (0=unavailable)  (1=avilable to startup or shutdown)  (2=must pump)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HeatRateCurve_GraphNode = GraphNode(
    node_for=[HeatRateCurve],
    label="name",
    tooltip="Relationship between unit heat rate per active power (Y-axis) and  unit output (X-axis). The heat input is from all fuels.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GenUnitOpSchedule_GraphNode = GraphNode(
    node_for=[GenUnitOpSchedule],
    label="name",
    tooltip="The generating unit's Operator-approved current operating schedule (or plan), typically produced with the aid of unit commitment type analyses. The X-axis represents absolute time. The Y1-axis represents the status (0=off-line and unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.). The Y2-axis represents the must run fixed power value where required.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CogenerationPlant_GraphNode = GraphNode(
    node_for=[CogenerationPlant],
    label="name",
    tooltip="A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Supercritical_GraphNode = GraphNode(
    node_for=[Supercritical],
    label="name",
    tooltip="Once-through supercritical boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SteamTurbine_GraphNode = GraphNode(
    node_for=[SteamTurbine],
    label="name",
    tooltip="Steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CTTempActivePowerCurve_GraphNode = GraphNode(
    node_for=[CTTempActivePowerCurve],
    label="name",
    tooltip="Relationship between the combustion turbine's power output rating in gross active power (X-axis) and the ambient air temperature (Y-axis)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PrimeMover_GraphNode = GraphNode(
    node_for=[PrimeMover],
    label="name",
    tooltip="The machine used to develop mechanical energy used to drive a generator.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PWRSteamSupply_GraphNode = GraphNode(
    node_for=[PWRSteamSupply],
    label="name",
    tooltip="Pressurized water reactor used as a steam supply to a steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CombustionTurbine_GraphNode = GraphNode(
    node_for=[CombustionTurbine],
    label="name",
    tooltip="A prime mover that is typically fueled by gas or light oil",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HeatRecoveryBoiler_GraphNode = GraphNode(
    node_for=[HeatRecoveryBoiler],
    label="name",
    tooltip="The heat recovery system associated with combustion turbines in order to produce steam for combined cycle plants",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BWRSteamSupply_GraphNode = GraphNode(
    node_for=[BWRSteamSupply],
    label="name",
    tooltip="Boiling water reactor used as a steam supply to a steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroTurbine_GraphNode = GraphNode(
    node_for=[HydroTurbine],
    label="name",
    tooltip="A water driven prime mover. Typical turbine types are: Francis, Kaplan, and Pelton.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

DrumBoiler_GraphNode = GraphNode(
    node_for=[DrumBoiler],
    label="name",
    tooltip="Drum boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

FossilSteamSupply_GraphNode = GraphNode(
    node_for=[FossilSteamSupply],
    label="name",
    tooltip="Fossil fueled boiler (e.g., coal, oil, gas)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Subcritical_GraphNode = GraphNode(
    node_for=[Subcritical],
    label="name",
    tooltip="Once-through subcritical boiler",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SteamSupply_GraphNode = GraphNode(
    node_for=[SteamSupply],
    label="name",
    tooltip="Steam supply for steam turbine",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Discrete_GraphNode = GraphNode(
    node_for=[Discrete],
    label="name",
    tooltip="Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Measurement_GraphNode = GraphNode(
    node_for=[Measurement],
    label="name",
    tooltip="A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SetPoint_GraphNode = GraphNode(
    node_for=[SetPoint],
    label="name",
    tooltip="A SetPoint is an analog control used for supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Control_GraphNode = GraphNode(
    node_for=[Control],
    label="name",
    tooltip="Control is used for supervisory/device control. It represents control outputs that are used to change the state in a process, e.g. close or open breaker, a set point value or a raise lower command.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ControlType_GraphNode = GraphNode(
    node_for=[ControlType],
    label="name",
    tooltip="Specifies the type of Control, e.g. BreakerOn/Off, GeneratorVoltageSetPoint, TieLineFlow etc. The ControlType.name shall be unique among all specified types and describe the type. The ControlType.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

DiscreteValue_GraphNode = GraphNode(
    node_for=[DiscreteValue],
    label="name",
    tooltip="DiscreteValue represents a discrete MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Accumulator_GraphNode = GraphNode(
    node_for=[Accumulator],
    label="name",
    tooltip="Accumulator represents a accumulated (counted) Measurement, e.g. an energy value.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LimitSet_GraphNode = GraphNode(
    node_for=[LimitSet],
    label="name",
    tooltip="Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AnalogLimit_GraphNode = GraphNode(
    node_for=[AnalogLimit],
    label="name",
    tooltip="Limit values for Analog measurements",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementValue_GraphNode = GraphNode(
    node_for=[MeasurementValue],
    label="name",
    tooltip="The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ValueAliasSet_GraphNode = GraphNode(
    node_for=[ValueAliasSet],
    label="name",
    tooltip="Describes the translation of a set of values into a name and is intendend to facilitate cusom translations. Each ValueAliasSet has a name, description etc. A specific Measurement may represent a discrete state like Open, Closed, Intermediate etc. This requires a translation from the MeasurementValue.value number to a string, e.g. 0->'Invalid', 1->'Open', 2->'Closed', 3->'Intermediate'. Each ValueToAlias member in ValueAliasSet.Value describe a mapping for one particular value to a name.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StringMeasurementValue_GraphNode = GraphNode(
    node_for=[StringMeasurementValue],
    label="name",
    tooltip="StringMeasurementValue represents a measurement value of type string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Quality61850_GraphNode = GraphNode(
    node_for=[Quality61850],
        tooltip="Quality flags in this class are as defined in IEC 61850, except for estimatorReplaced, which has been included in this class for convenience.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Limit_GraphNode = GraphNode(
    node_for=[Limit],
    label="name",
    tooltip="Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementType_GraphNode = GraphNode(
    node_for=[MeasurementType],
    label="name",
    tooltip="Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AccumulatorLimit_GraphNode = GraphNode(
    node_for=[AccumulatorLimit],
    label="name",
    tooltip="Limit values for Accumulator measurements",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StringMeasurement_GraphNode = GraphNode(
    node_for=[StringMeasurement],
    label="name",
    tooltip="StringMeasurement represents a measurement with values of type string.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ValueToAlias_GraphNode = GraphNode(
    node_for=[ValueToAlias],
    label="name",
    tooltip="Describes the translation of one particular value into a name, e.g. 1->'Open'",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AnalogValue_GraphNode = GraphNode(
    node_for=[AnalogValue],
    label="name",
    tooltip="AnalogValue represents an analog MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementValueQuality_GraphNode = GraphNode(
    node_for=[MeasurementValueQuality],
        tooltip="Measurement quality flags. Bits 0-10 are defined for substation automation in draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that document. Bits 16-31 are reserved for EMS applications.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementValueSource_GraphNode = GraphNode(
    node_for=[MeasurementValueSource],
    label="name",
    tooltip="MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AccumulatorLimitSet_GraphNode = GraphNode(
    node_for=[AccumulatorLimitSet],
    label="name",
    tooltip="An AccumulatorLimitSet specifies a set of Limits that are associated with an Accumulator measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AnalogLimitSet_GraphNode = GraphNode(
    node_for=[AnalogLimitSet],
    label="name",
    tooltip="An AnalogLimitSet specifies a set of Limits that are associated with an Analog measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Command_GraphNode = GraphNode(
    node_for=[Command],
    label="name",
    tooltip="A Command is a discrete control used for supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Analog_GraphNode = GraphNode(
    node_for=[Analog],
    label="name",
    tooltip="Analog represents an analog Measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AccumulatorValue_GraphNode = GraphNode(
    node_for=[AccumulatorValue],
    label="name",
    tooltip="AccumulatorValue represents a accumulated (counted) MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SubLoadArea_GraphNode = GraphNode(
    node_for=[SubLoadArea],
    label="name",
    tooltip="The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Load_GraphNode = GraphNode(
    node_for=[Load],
    label="name",
    tooltip="A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadResponseCharacteristic_GraphNode = GraphNode(
    node_for=[LoadResponseCharacteristic],
    label="name",
    tooltip="Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Season_GraphNode = GraphNode(
    node_for=[Season],
    label="name",
    tooltip="A specified time period of the year, e.g., Spring, Summer, Fall, Winter",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConformLoadGroup_GraphNode = GraphNode(
    node_for=[ConformLoadGroup],
    label="name",
    tooltip="Load that follows a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConformLoad_GraphNode = GraphNode(
    node_for=[ConformLoad],
    label="name",
    tooltip="ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadArea_GraphNode = GraphNode(
    node_for=[LoadArea],
    label="name",
    tooltip="The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PowerCutZone_GraphNode = GraphNode(
    node_for=[PowerCutZone],
    label="name",
    tooltip="An area or zone of the power system which is used for load shedding purposes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConformLoadSchedule_GraphNode = GraphNode(
    node_for=[ConformLoadSchedule],
    label="name",
    tooltip="A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StationSupply_GraphNode = GraphNode(
    node_for=[StationSupply],
    label="name",
    tooltip="Station supply with load derived from the station output.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

DayType_GraphNode = GraphNode(
    node_for=[DayType],
    label="name",
    tooltip="Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NonConformLoadSchedule_GraphNode = GraphNode(
    node_for=[NonConformLoadSchedule],
    label="name",
    tooltip="An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CustomerLoad_GraphNode = GraphNode(
    node_for=[CustomerLoad],
    label="name",
    tooltip="A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadGroup_GraphNode = GraphNode(
    node_for=[LoadGroup],
    label="name",
    tooltip="The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NonConformLoadGroup_GraphNode = GraphNode(
    node_for=[NonConformLoadGroup],
    label="name",
    tooltip="Loads that do not follow a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EnergyArea_GraphNode = GraphNode(
    node_for=[EnergyArea],
    label="name",
    tooltip="The class describes an area having energy production or consumption. The class is the basis for further specialization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SeasonDayTypeSchedule_GraphNode = GraphNode(
    node_for=[SeasonDayTypeSchedule],
    label="name",
    tooltip="The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NonConformLoad_GraphNode = GraphNode(
    node_for=[NonConformLoad],
    label="name",
    tooltip="NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

InductionMotorLoad_GraphNode = GraphNode(
    node_for=[InductionMotorLoad],
    label="name",
    tooltip="Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Curve_GraphNode = GraphNode(
    node_for=[Curve],
    label="name",
    tooltip="Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

VoltageLevel_GraphNode = GraphNode(
    node_for=[VoltageLevel],
    label="name",
    tooltip="A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ReportingGroup_GraphNode = GraphNode(
    node_for=[ReportingGroup],
    label="name",
    tooltip="A reporting group is used for various ad-hoc groupings used for reporting.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ModelingAuthoritySet_GraphNode = GraphNode(
    node_for=[ModelingAuthoritySet],
    label="name",
    tooltip="A Modeling Authority Set is a group of objects in a network model where the data is supplied and maintained by the same Modeling Authority.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperatingParticipant_GraphNode = GraphNode(
    node_for=[OperatingParticipant],
    label="name",
    tooltip="An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ReportingSuperGroup_GraphNode = GraphNode(
    node_for=[ReportingSuperGroup],
    label="name",
    tooltip="A reporting super group, groups reporting groups for a higher level report.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Substation_GraphNode = GraphNode(
    node_for=[Substation],
    label="name",
    tooltip="A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConductingEquipment_GraphNode = GraphNode(
    node_for=[ConductingEquipment],
    label="name",
    tooltip="The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IrregularTimePoint_GraphNode = GraphNode(
    node_for=[IrregularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points varies.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConnectivityNodeContainer_GraphNode = GraphNode(
    node_for=[ConnectivityNodeContainer],
    label="name",
    tooltip="A base class for all objects that may contain ConnectivityNodes or TopologicalNodes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GeographicalRegion_GraphNode = GraphNode(
    node_for=[GeographicalRegion],
    label="name",
    tooltip="A geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Unit_GraphNode = GraphNode(
    node_for=[Unit],
    label="name",
    tooltip="Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquipmentContainer_GraphNode = GraphNode(
    node_for=[EquipmentContainer],
    label="name",
    tooltip="A modeling construct to provide a root class for all Equipment classes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ModelingAuthority_GraphNode = GraphNode(
    node_for=[ModelingAuthority],
    label="name",
    tooltip="A Modeling Authority is an entity responsible for supplying and maintaining the data defining a specific set of objects in a network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BaseVoltage_GraphNode = GraphNode(
    node_for=[BaseVoltage],
    label="name",
    tooltip="Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperatingShare_GraphNode = GraphNode(
    node_for=[OperatingShare],
        tooltip="Specifies the contract relationship between a PowerSystemResource and a contract participant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BasicIntervalSchedule_GraphNode = GraphNode(
    node_for=[BasicIntervalSchedule],
    label="name",
    tooltip="Schedule of values at points in time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CurveData_GraphNode = GraphNode(
    node_for=[CurveData],
        tooltip="Data point values for defining a curve or schedule",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Equipment_GraphNode = GraphNode(
    node_for=[Equipment],
    label="name",
    tooltip="The parts of a power system that are physical devices, electronic or mechanical",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegularIntervalSchedule_GraphNode = GraphNode(
    node_for=[RegularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IrregularIntervalSchedule_GraphNode = GraphNode(
    node_for=[IrregularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them varies.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Bay_GraphNode = GraphNode(
    node_for=[Bay],
    label="name",
    tooltip="A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegularTimePoint_GraphNode = GraphNode(
    node_for=[RegularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Terminal_GraphNode = GraphNode(
    node_for=[Terminal],
    label="name",
    tooltip="An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SubGeographicalRegion_GraphNode = GraphNode(
    node_for=[SubGeographicalRegion],
    label="name",
    tooltip="A subset of a geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PowerSystemResource_GraphNode = GraphNode(
    node_for=[PowerSystemResource],
    label="name",
    tooltip="A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BasePower_GraphNode = GraphNode(
    node_for=[BasePower],
    label="name",
    tooltip="The BasePower class defines the base power used in the per unit calculations.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PSRType_GraphNode = GraphNode(
    node_for=[PSRType],
    label="name",
    tooltip="Classifying instances of the same class, e.g. overhead and underground ACLineSegments. This classification mechanism is intended to provide flexibility outside the scope of this standard, i.e. provide customisation that is non standard.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PsrList_GraphNode = GraphNode(
    node_for=[PsrList],
    label="name",
    tooltip="Arbitrary list of PowerSystemResources. Can be used for various purposes, including grouping for report generation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Company_GraphNode = GraphNode(
    node_for=[Company],
    label="name",
    tooltip="A company is a legal entity that owns and operates power system resources and is a party to interchange and transmission contracts.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IdentifiedObject_GraphNode = GraphNode(
    node_for=[IdentifiedObject],
    label="name",
    tooltip="This is a root class to provide common naming attributes for all classes needing naming attributes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Contingency_GraphNode = GraphNode(
    node_for=[Contingency],
    label="name",
    tooltip="An event threatening system reliability, consisting of one or more contingency elements.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ContingencyEquipment_GraphNode = GraphNode(
    node_for=[ContingencyEquipment],
    label="name",
    tooltip="A equipment to which the in service status is to change such as a power transformer or AC line segment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ContingencyElement_GraphNode = GraphNode(
    node_for=[ContingencyElement],
    label="name",
    tooltip="An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ClearanceTagType_GraphNode = GraphNode(
    node_for=[ClearanceTagType],
    label="name",
    tooltip="Type of ClearanceTag. Could indicate the type of work to be performed and/or the type of supervisory control.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SwitchingOperation_GraphNode = GraphNode(
    node_for=[SwitchingOperation],
    label="name",
    tooltip="A SwitchingOperation is used to define individual switch operations for an OutageSchedule. This OutageSchedule may be associated with another item of Substation such as a Transformer, Line, or Generator; or with the Switch itself as a PowerSystemResource. A Switch may be referenced by many OutageSchedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OutageSchedule_GraphNode = GraphNode(
    node_for=[OutageSchedule],
    label="name",
    tooltip="The period of time that a piece of equipment is out of service, for example, for maintenance or testing; including the equipment's active power rating while under maintenance. The X-axis represents absolute time and the Y-axis represents the equipment's available rating while out of service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ClearanceTag_GraphNode = GraphNode(
    node_for=[ClearanceTag],
    label="name",
    tooltip="A clearance tag that is used to authorize and schedule work on conducting equipment in the field. Tagged equipment is not available for commercial service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RemotePoint_GraphNode = GraphNode(
    node_for=[RemotePoint],
    label="name",
    tooltip="For a RTU remote points correspond to telemetered values or control outputs. Other units (e.g. control centers) usually also contain calculated values.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RemoteControl_GraphNode = GraphNode(
    node_for=[RemoteControl],
    label="name",
    tooltip="Remote controls are ouputs that are sent by the remote unit to actuators in the process.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RemoteSource_GraphNode = GraphNode(
    node_for=[RemoteSource],
    label="name",
    tooltip="Remote sources are state variables that are telemetered or calculated within the remote unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CommunicationLink_GraphNode = GraphNode(
    node_for=[CommunicationLink],
    label="name",
    tooltip="The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RemoteUnit_GraphNode = GraphNode(
    node_for=[RemoteUnit],
    label="name",
    tooltip="A remote unit can be a RTU, IED, substation control system, control center etc. The communication with the remote unit can be through various standard protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP, RP570 etc.). A remote unit contain remote data points that might be telemetered, collected or calculated. The RemoteUnit class inherit PowerSystemResource. The intention is to allow RemotUnits to have Measurements. These Measurements can be used to model unit status as operational, out of service, unit failure etc.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperationalLimit_GraphNode = GraphNode(
    node_for=[OperationalLimit],
    label="name",
    tooltip="A value associated with a specific kind of limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BranchGroup_GraphNode = GraphNode(
    node_for=[BranchGroup],
    label="name",
    tooltip="A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperationalLimitType_GraphNode = GraphNode(
    node_for=[OperationalLimitType],
        tooltip="A type of limit.  The meaning of a specific limit is described in this class.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ActivePowerLimit_GraphNode = GraphNode(
    node_for=[ActivePowerLimit],
    label="name",
    tooltip="Limit on active power flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CurrentLimit_GraphNode = GraphNode(
    node_for=[CurrentLimit],
    label="name",
    tooltip="Operational limit on current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperationalLimitSet_GraphNode = GraphNode(
    node_for=[OperationalLimitSet],
    label="name",
    tooltip="A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

VoltageLimit_GraphNode = GraphNode(
    node_for=[VoltageLimit],
    label="name",
    tooltip="Operational limit applied to voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BranchGroupTerminal_GraphNode = GraphNode(
    node_for=[BranchGroupTerminal],
        tooltip="A specific directed terminal flow for a branch group.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ApparentPowerLimit_GraphNode = GraphNode(
    node_for=[ApparentPowerLimit],
    label="name",
    tooltip="Apparent power limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ControlAreaGeneratingUnit_GraphNode = GraphNode(
    node_for=[ControlAreaGeneratingUnit],
        tooltip="A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ControlArea_GraphNode = GraphNode(
    node_for=[ControlArea],
    label="name",
    tooltip="A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AltGeneratingUnitMeas_GraphNode = GraphNode(
    node_for=[AltGeneratingUnitMeas],
        tooltip="A prioritized measurement to be used for the generating unit in the control area specificaiton.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TieFlow_GraphNode = GraphNode(
    node_for=[TieFlow],
        tooltip="A flow specification in terms of location and direction for a control area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AltTieMeas_GraphNode = GraphNode(
    node_for=[AltTieMeas],
        tooltip="A prioritized measurement to be used for the tie flow as part of the control area specification.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentBranch_GraphNode = GraphNode(
    node_for=[EquivalentBranch],
    label="name",
    tooltip="The class represents equivalent branches.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentShunt_GraphNode = GraphNode(
    node_for=[EquivalentShunt],
    label="name",
    tooltip="The class represents equivalent shunts.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentNetwork_GraphNode = GraphNode(
    node_for=[EquivalentNetwork],
    label="name",
    tooltip="A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentEquipment_GraphNode = GraphNode(
    node_for=[EquivalentEquipment],
    label="name",
    tooltip="The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of different types.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TopologicalNode_GraphNode = GraphNode(
    node_for=[TopologicalNode],
    label="name",
    tooltip="A set of connectivity nodes that, in the current network state, are connected together through any type of closed switches, including  jumpers. Topological nodes can change as the current network state changes (i.e., switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TopologicalIsland_GraphNode = GraphNode(
    node_for=[TopologicalIsland],
    label="name",
    tooltip="An electrically connected subset of the network. Topological islands can change as the current network state changes (i.e., disconnect switches, breakers, etc. change state).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConnectivityNode_GraphNode = GraphNode(
    node_for=[ConnectivityNode],
    label="name",
    tooltip="Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BusNameMarker_GraphNode = GraphNode(
    node_for=[BusNameMarker],
    label="name",
    tooltip="Used to apply user standard names to topology buses. Typically used for 'bus/branch' case generation. Associated with one or more ConnectivityNodes that are normally a part of the bus name.    The associated ConnectivityNodes are to be connected by non-retained switches. For a ring bus station configuration, all busbar connectivity nodes in the ring are typically associated.   For a breaker and a half scheme, both busbars would be associated.  For a ring bus, all busbars would be associated.  For a 'straight' busbar configuration, only the main connectivity node at the busbar would be associated.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SynchrocheckRelay_GraphNode = GraphNode(
    node_for=[SynchrocheckRelay],
    label="name",
    tooltip="A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ProtectionEquipment_GraphNode = GraphNode(
    node_for=[ProtectionEquipment],
    label="name",
    tooltip="An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CurrentRelay_GraphNode = GraphNode(
    node_for=[CurrentRelay],
    label="name",
    tooltip="A device that checks current flow values in any direction or designated direction",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RecloseSequence_GraphNode = GraphNode(
    node_for=[RecloseSequence],
    label="name",
    tooltip="A reclose sequence (open and close) is defined for each possible reclosure of a breaker.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

#------------------------------------------------------------------------------
#  Graph edges:
#------------------------------------------------------------------------------

#CommonInformationModel_Elements_GraphEdge = GraphEdge(
#    edge_for=[CommonInformationModel],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Elements",
#    tooltip="")

#RegulationSchedule_RegulatingControl_GraphEdge = GraphEdge(
#    edge_for=[RegulationSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RegulatingControl",
#    tooltip="")

#RegulationSchedule_VoltageControlZones_GraphEdge = GraphEdge(
#    edge_for=[RegulationSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=VoltageControlZones",
#    tooltip="A VoltageControlZone may have a  voltage regulation schedule.")

#TransformerWinding_To_WindingTest_GraphEdge = GraphEdge(
#    edge_for=[TransformerWinding],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=To_WindingTest",
#    tooltip="The winding to which the test was conducted")

#TransformerWinding_From_WindingTest_GraphEdge = GraphEdge(
#    edge_for=[TransformerWinding],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=From_WindingTest",
#    tooltip="The winding from which the test was conducted")

#TransformerWinding_TapChangers_GraphEdge = GraphEdge(
#    edge_for=[TransformerWinding],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TapChangers",
#    tooltip="A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.")

#WireType_WireArrangements_GraphEdge = GraphEdge(
#    edge_for=[WireType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=WireArrangements",
#    tooltip="A WireType is mounted at a specified place in a WireArrangement.")

#RegulatingCondEq_Controls_GraphEdge = GraphEdge(
#    edge_for=[RegulatingCondEq],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Controls",
#    tooltip="The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.")

#ProtectedSwitch_OperatedBy_ProtectionEquipments_GraphEdge = GraphEdge(
#    edge_for=[ProtectedSwitch],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperatedBy_ProtectionEquipments",
#    tooltip="Circuit breakers may be operated by protection relays.")

#ProtectedSwitch_RecloseSequences_GraphEdge = GraphEdge(
#    edge_for=[ProtectedSwitch],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RecloseSequences",
#    tooltip="A breaker may have zero or more automatic reclosures after a trip occurs.")

#CompositeSwitch_Switches_GraphEdge = GraphEdge(
#    edge_for=[CompositeSwitch],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Switches",
#    tooltip="")

#PowerTransformer_Contains_TransformerWindings_GraphEdge = GraphEdge(
#    edge_for=[PowerTransformer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_TransformerWindings",
#    tooltip="A transformer has windings")

#ACLineSegment_HasFirst_MutualCoupling_GraphEdge = GraphEdge(
#    edge_for=[ACLineSegment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=HasFirst_MutualCoupling",
#    tooltip="")

#ACLineSegment_HasSecond_MutualCoupling_GraphEdge = GraphEdge(
#    edge_for=[ACLineSegment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=HasSecond_MutualCoupling",
#    tooltip="")

#Switch_SwitchingOperations_GraphEdge = GraphEdge(
#    edge_for=[Switch],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SwitchingOperations",
#    tooltip="A switch may be operated by many schedules.")

#SynchronousMachine_ReactiveCapabilityCurves_GraphEdge = GraphEdge(
#    edge_for=[SynchronousMachine],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ReactiveCapabilityCurves",
#    tooltip="")

#SynchronousMachine_DrivenBy_PrimeMover_GraphEdge = GraphEdge(
#    edge_for=[SynchronousMachine],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=DrivenBy_PrimeMover",
#    tooltip="")

#RegulatingControl_RegulatingCondEq_GraphEdge = GraphEdge(
#    edge_for=[RegulatingControl],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RegulatingCondEq",
#    tooltip="")

#RegulatingControl_TapChanger_GraphEdge = GraphEdge(
#    edge_for=[RegulatingControl],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TapChanger",
#    tooltip="")

#ConductorType_Conductors_GraphEdge = GraphEdge(
#    edge_for=[ConductorType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Conductors",
#    tooltip="Sections of conductor are physically described by a conductor type")

#ConductorType_WireArrangements_GraphEdge = GraphEdge(
#    edge_for=[ConductorType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=WireArrangements",
#    tooltip="A ConductorType is made up of wires that can be configured in several ways.")

#ReactiveCapabilityCurve_SynchronousMachines_GraphEdge = GraphEdge(
#    edge_for=[ReactiveCapabilityCurve],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SynchronousMachines",
#    tooltip="")

#ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_GraphEdge = GraphEdge(
#    edge_for=[ReactiveCapabilityCurve],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=InitiallyUsedBySynchronousMachine",
#    tooltip="Defines the default MVArCapabilityCurve for use by a SynchronousMachine.")

#GeneratingUnit_ControlAreaGeneratingUnit_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ControlAreaGeneratingUnit",
#    tooltip="")

#GeneratingUnit_GrossToNetActivePowerCurves_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=GrossToNetActivePowerCurves",
#    tooltip="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit")

#GeneratingUnit_Contains_SynchronousMachines_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_SynchronousMachines",
#    tooltip="A synchronous machine may operate as a generator and as such becomes a member of a generating unit")

#GeneratingUnit_GenUnitOpCostCurves_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=GenUnitOpCostCurves",
#    tooltip="A generating unit may have one or more cost curves, depending upon fuel mixture and fuel cost.")

#CombinedCyclePlant_Contain_ThermalGeneratingUnits_GraphEdge = GraphEdge(
#    edge_for=[CombinedCyclePlant],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_ThermalGeneratingUnits",
#    tooltip="A thermal generating unit may be a member of a combined cycle plant")

#HydroPowerPlant_Contain_HydroGeneratingUnits_GraphEdge = GraphEdge(
#    edge_for=[HydroPowerPlant],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_HydroGeneratingUnits",
#    tooltip="The hydro generating unit belongs to a hydro power plant")

#HydroPowerPlant_Contain_HydroPumps_GraphEdge = GraphEdge(
#    edge_for=[HydroPowerPlant],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_HydroPumps",
#    tooltip="The hydro pump may be a member of a pumped storage plant or a pump for distributing water")

#HydroGeneratingUnit_HydroGeneratingEfficiencyCurves_GraphEdge = GraphEdge(
#    edge_for=[HydroGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=HydroGeneratingEfficiencyCurves",
#    tooltip="A hydro generating unit has an efficiency curve")

#HydroGeneratingUnit_TailbayLossCurve_GraphEdge = GraphEdge(
#    edge_for=[HydroGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TailbayLossCurve",
#    tooltip="A hydro generating unit has a tailbay loss curve")

#ThermalGeneratingUnit_FuelAllocationSchedules_GraphEdge = GraphEdge(
#    edge_for=[ThermalGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=FuelAllocationSchedules",
#    tooltip="A thermal generating unit may have one or more fuel allocation schedules")

#ThermalGeneratingUnit_EmissionCurves_GraphEdge = GraphEdge(
#    edge_for=[ThermalGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EmissionCurves",
#    tooltip="A thermal generating unit may have  one or more emission curves")

#ThermalGeneratingUnit_EmmissionAccounts_GraphEdge = GraphEdge(
#    edge_for=[ThermalGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EmmissionAccounts",
#    tooltip="A thermal generating unit may have one or more emission allowance accounts")

#ThermalGeneratingUnit_FossilFuels_GraphEdge = GraphEdge(
#    edge_for=[ThermalGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=FossilFuels",
#    tooltip="A thermal generating unit may have one or more fossil fuels")

#FossilFuel_FuelAllocationSchedule_GraphEdge = GraphEdge(
#    edge_for=[FossilFuel],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=FuelAllocationSchedule",
#    tooltip="A fuel allocation schedule must have a fossil fuel")

#Reservoir_LevelVsVolumeCurve_GraphEdge = GraphEdge(
#    edge_for=[Reservoir],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=LevelVsVolumeCurve",
#    tooltip="A reservoir may have a level versus volume relationship.")

#Reservoir_InflowForecast_GraphEdge = GraphEdge(
#    edge_for=[Reservoir],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=InflowForecast",
#    tooltip="A reservoir may have a 'natural' inflow forecast.")

#Reservoir_SpillsInto_GraphEdge = GraphEdge(
#    edge_for=[Reservoir],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SpillsInto",
#    tooltip="A reservoir may spill into a downstream reservoir")

#Reservoir_HydroPowerPlants_GraphEdge = GraphEdge(
#    edge_for=[Reservoir],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=HydroPowerPlants",
#    tooltip="Generators discharge water to or pumps are supplied water from a downstream reservoir")

#Reservoir_UpstreamFrom_GraphEdge = GraphEdge(
#    edge_for=[Reservoir],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=UpstreamFrom",
#    tooltip="Generators are supplied water from or pumps discharge water to an upstream reservoir")

#CogenerationPlant_Contain_ThermalGeneratingUnits_GraphEdge = GraphEdge(
#    edge_for=[CogenerationPlant],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_ThermalGeneratingUnits",
#    tooltip="A thermal generating unit may be a member of a cogeneration plant")

#SteamTurbine_SteamSupplys_GraphEdge = GraphEdge(
#    edge_for=[SteamTurbine],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SteamSupplys",
#    tooltip="Steam turbines may have steam supplied by a steam supply")

#PrimeMover_Drives_SynchronousMachines_GraphEdge = GraphEdge(
#    edge_for=[PrimeMover],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Drives_SynchronousMachines",
#    tooltip="")

#HeatRecoveryBoiler_CombustionTurbines_GraphEdge = GraphEdge(
#    edge_for=[HeatRecoveryBoiler],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=CombustionTurbines",
#    tooltip="A combustion turbine may have a heat recovery boiler for making steam")

#SteamSupply_SteamTurbines_GraphEdge = GraphEdge(
#    edge_for=[SteamSupply],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SteamTurbines",
#    tooltip="Steam turbines may have steam supplied by a steam supply")

#Discrete_Contain_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[Discrete],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_MeasurementValues",
#    tooltip="")

#ControlType_Controls_GraphEdge = GraphEdge(
#    edge_for=[ControlType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Controls",
#    tooltip="")

#Accumulator_Contain_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[Accumulator],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_MeasurementValues",
#    tooltip="")

#Accumulator_LimitSets_GraphEdge = GraphEdge(
#    edge_for=[Accumulator],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=LimitSets",
#    tooltip="A measurement may have zero or more limit ranges defined for it.")

#ValueAliasSet_Values_GraphEdge = GraphEdge(
#    edge_for=[ValueAliasSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Values",
#    tooltip="")

#ValueAliasSet_Commands_GraphEdge = GraphEdge(
#    edge_for=[ValueAliasSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Commands",
#    tooltip="")

#ValueAliasSet_Measurements_GraphEdge = GraphEdge(
#    edge_for=[ValueAliasSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="")

#MeasurementType_Measurements_GraphEdge = GraphEdge(
#    edge_for=[MeasurementType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="A measurement has a measurement type.")

#StringMeasurement_Contains_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[StringMeasurement],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_MeasurementValues",
#    tooltip="")

#AnalogValue_AltGeneratingUnit_GraphEdge = GraphEdge(
#    edge_for=[AnalogValue],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=AltGeneratingUnit",
#    tooltip="")

#AnalogValue_AltTieMeas_GraphEdge = GraphEdge(
#    edge_for=[AnalogValue],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=AltTieMeas",
#    tooltip="")

#MeasurementValueSource_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[MeasurementValueSource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=MeasurementValues",
#    tooltip="")

#AccumulatorLimitSet_Measurements_GraphEdge = GraphEdge(
#    edge_for=[AccumulatorLimitSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="A measurement may have zero or more limit ranges defined for it.")

#AccumulatorLimitSet_Limits_GraphEdge = GraphEdge(
#    edge_for=[AccumulatorLimitSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Limits",
#    tooltip="")

#AnalogLimitSet_Limits_GraphEdge = GraphEdge(
#    edge_for=[AnalogLimitSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Limits",
#    tooltip="")

#AnalogLimitSet_Measurements_GraphEdge = GraphEdge(
#    edge_for=[AnalogLimitSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="A measurement may have zero or more limit ranges defined for it.")

#Analog_Contain_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[Analog],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_MeasurementValues",
#    tooltip="")

#Analog_LimitSets_GraphEdge = GraphEdge(
#    edge_for=[Analog],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=LimitSets",
#    tooltip="A measurement may have zero or more limit ranges defined for it.")

#SubLoadArea_LoadGroups_GraphEdge = GraphEdge(
#    edge_for=[SubLoadArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=LoadGroups",
#    tooltip="")

#LoadResponseCharacteristic_EnergyConsumer_GraphEdge = GraphEdge(
#    edge_for=[LoadResponseCharacteristic],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumer",
#    tooltip="")

#Season_SeasonDayTypeSchedules_GraphEdge = GraphEdge(
#    edge_for=[Season],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SeasonDayTypeSchedules",
#    tooltip="Load demand models can be based on seasons")

#ConformLoadGroup_EnergyConsumers_GraphEdge = GraphEdge(
#    edge_for=[ConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumers",
#    tooltip="Consumers may be assigned to a load area.")

#ConformLoadGroup_ConformLoadSchedules_GraphEdge = GraphEdge(
#    edge_for=[ConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConformLoadSchedules",
#    tooltip="")

#LoadArea_SubLoadAreas_GraphEdge = GraphEdge(
#    edge_for=[LoadArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SubLoadAreas",
#    tooltip="The SubLoadAreas in the LoadArea.")

#PowerCutZone_EnergyConsumers_GraphEdge = GraphEdge(
#    edge_for=[PowerCutZone],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumers",
#    tooltip="An energy consumer is assigned to a power cut zone")

#DayType_SeasonDayTypeSchedules_GraphEdge = GraphEdge(
#    edge_for=[DayType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SeasonDayTypeSchedules",
#    tooltip="Load demand models can be based on day type")

#NonConformLoadGroup_NonConformLoadSchedules_GraphEdge = GraphEdge(
#    edge_for=[NonConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=NonConformLoadSchedules",
#    tooltip="")

#NonConformLoadGroup_EnergyConsumers_GraphEdge = GraphEdge(
#    edge_for=[NonConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumers",
#    tooltip="")

#Curve_CurveScheduleDatas_GraphEdge = GraphEdge(
#    edge_for=[Curve],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=CurveScheduleDatas",
#    tooltip="The point data values that define a curve")

#VoltageLevel_Contains_Bays_GraphEdge = GraphEdge(
#    edge_for=[VoltageLevel],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Bays",
#    tooltip="The association is used in the naming hierarchy.")

#ReportingGroup_PowerSystemResource_GraphEdge = GraphEdge(
#    edge_for=[ReportingGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=PowerSystemResource",
#    tooltip="")

#ReportingGroup_BusNameMarker_GraphEdge = GraphEdge(
#    edge_for=[ReportingGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=BusNameMarker",
#    tooltip="")

#ReportingGroup_TopologicalNode_GraphEdge = GraphEdge(
#    edge_for=[ReportingGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TopologicalNode",
#    tooltip="")

#ModelingAuthoritySet_IdentifiedObjects_GraphEdge = GraphEdge(
#    edge_for=[ModelingAuthoritySet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=IdentifiedObjects",
#    tooltip="An IdentifiedObject belongs to a Modeling Authority Set for purposes of defining a group of data maintained by the same Modeling Authority.")

#OperatingParticipant_OperatingShare_GraphEdge = GraphEdge(
#    edge_for=[OperatingParticipant],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperatingShare",
#    tooltip="")

#ReportingSuperGroup_ReportingGroup_GraphEdge = GraphEdge(
#    edge_for=[ReportingSuperGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ReportingGroup",
#    tooltip="")

#Substation_Contains_VoltageLevels_GraphEdge = GraphEdge(
#    edge_for=[Substation],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_VoltageLevels",
#    tooltip="The association is used in the naming hierarchy.")

#Substation_Contains_Bays_GraphEdge = GraphEdge(
#    edge_for=[Substation],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Bays",
#    tooltip="The association is used in the naming hierarchy.")

#ConductingEquipment_Terminals_GraphEdge = GraphEdge(
#    edge_for=[ConductingEquipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Terminals",
#    tooltip="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

#ConductingEquipment_ProtectionEquipments_GraphEdge = GraphEdge(
#    edge_for=[ConductingEquipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ProtectionEquipments",
#    tooltip="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.")

#ConductingEquipment_ClearanceTags_GraphEdge = GraphEdge(
#    edge_for=[ConductingEquipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ClearanceTags",
#    tooltip="Conducting equipment may have multiple clearance tags for authorized field work")

#ConnectivityNodeContainer_TopologicalNode_GraphEdge = GraphEdge(
#    edge_for=[ConnectivityNodeContainer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TopologicalNode",
#    tooltip="")

#ConnectivityNodeContainer_ConnectivityNodes_GraphEdge = GraphEdge(
#    edge_for=[ConnectivityNodeContainer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConnectivityNodes",
#    tooltip="")

#GeographicalRegion_Regions_GraphEdge = GraphEdge(
#    edge_for=[GeographicalRegion],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Regions",
#    tooltip="The association is used in the naming hierarchy.")

#Unit_Controls_GraphEdge = GraphEdge(
#    edge_for=[Unit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Controls",
#    tooltip="")

#Unit_ProtectionEquipments_GraphEdge = GraphEdge(
#    edge_for=[Unit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ProtectionEquipments",
#    tooltip="The Protection Equipments having the Unit.")

#Unit_Measurements_GraphEdge = GraphEdge(
#    edge_for=[Unit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="")

#EquipmentContainer_Contains_Equipments_GraphEdge = GraphEdge(
#    edge_for=[EquipmentContainer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Equipments",
#    tooltip="The association is used in the naming hierarchy.")

#ModelingAuthority_ModelingAuthoritySets_GraphEdge = GraphEdge(
#    edge_for=[ModelingAuthority],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ModelingAuthoritySets",
#    tooltip="A Modeling Authority set supplies and maintains the data for the objects in a Modeling Authority Set.")

#BaseVoltage_ConductingEquipment_GraphEdge = GraphEdge(
#    edge_for=[BaseVoltage],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConductingEquipment",
#    tooltip="Use association to ConductingEquipment only when there is no VoltageLevel container used.")

#BaseVoltage_VoltageLevel_GraphEdge = GraphEdge(
#    edge_for=[BaseVoltage],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=VoltageLevel",
#    tooltip="")

#Equipment_OperationalLimitSet_GraphEdge = GraphEdge(
#    edge_for=[Equipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperationalLimitSet",
#    tooltip="")

#Equipment_ContingencyEquipment_GraphEdge = GraphEdge(
#    edge_for=[Equipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ContingencyEquipment",
#    tooltip="")

#RegularIntervalSchedule_TimePoints_GraphEdge = GraphEdge(
#    edge_for=[RegularIntervalSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TimePoints",
#    tooltip="A RegularTimePoint belongs to a RegularIntervalSchedule.")

#IrregularIntervalSchedule_TimePoints_GraphEdge = GraphEdge(
#    edge_for=[IrregularIntervalSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TimePoints",
#    tooltip="An IrregularTimePoint belongs to an IrregularIntervalSchedule.")

#Terminal_TieFlow_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TieFlow",
#    tooltip="A terminal may participate in zero, one, or two control areas as a tie flow.")

#Terminal_OperationalLimitSet_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperationalLimitSet",
#    tooltip="")

#Terminal_BranchGroupTerminal_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=BranchGroupTerminal",
#    tooltip="")

#Terminal_RegulatingControl_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RegulatingControl",
#    tooltip="")

#Terminal_Measurements_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.")

#SubGeographicalRegion_Lines_GraphEdge = GraphEdge(
#    edge_for=[SubGeographicalRegion],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Lines",
#    tooltip="A Line can be contained by a SubGeographical Region.")

#SubGeographicalRegion_Substations_GraphEdge = GraphEdge(
#    edge_for=[SubGeographicalRegion],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Substations",
#    tooltip="The association is used in the naming hierarchy.")

#PowerSystemResource_OperatedBy_Companies_GraphEdge = GraphEdge(
#    edge_for=[PowerSystemResource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperatedBy_Companies",
#    tooltip="A power system resource may be part of one or more companies")

#PowerSystemResource_ReportingGroup_GraphEdge = GraphEdge(
#    edge_for=[PowerSystemResource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ReportingGroup",
#    tooltip="")

#PowerSystemResource_OperatingShare_GraphEdge = GraphEdge(
#    edge_for=[PowerSystemResource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperatingShare",
#    tooltip="")

#PowerSystemResource_PsrLists_GraphEdge = GraphEdge(
#    edge_for=[PowerSystemResource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=PsrLists",
#    tooltip="")

#PowerSystemResource_Contains_Measurements_GraphEdge = GraphEdge(
#    edge_for=[PowerSystemResource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Measurements",
#    tooltip="Measurement-PSR defines the measurements in the naming hierarchy.")

#PSRType_PowerSystemResource_GraphEdge = GraphEdge(
#    edge_for=[PSRType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=PowerSystemResource",
#    tooltip="")

#PsrList_PowerSystemResources_GraphEdge = GraphEdge(
#    edge_for=[PsrList],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=PowerSystemResources",
#    tooltip="")

#Company_Operates_PSRs_GraphEdge = GraphEdge(
#    edge_for=[Company],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Operates_PSRs",
#    tooltip="A power system resource may be part of one or more companies")

#Contingency_ContingencyElement_GraphEdge = GraphEdge(
#    edge_for=[Contingency],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ContingencyElement",
#    tooltip="")

#ClearanceTagType_ClearanceTags_GraphEdge = GraphEdge(
#    edge_for=[ClearanceTagType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ClearanceTags",
#    tooltip="")

#SwitchingOperation_Switches_GraphEdge = GraphEdge(
#    edge_for=[SwitchingOperation],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Switches",
#    tooltip="A switch may be operated by many schedules.")

#OutageSchedule_SwitchingOperations_GraphEdge = GraphEdge(
#    edge_for=[OutageSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SwitchingOperations",
#    tooltip="An OutageSchedule may operate many switches.")

#CommunicationLink_Contain_RemoteUnits_GraphEdge = GraphEdge(
#    edge_for=[CommunicationLink],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_RemoteUnits",
#    tooltip="RTUs may be attached to communication links.")

#RemoteUnit_MemberOf_CommunicationLinks_GraphEdge = GraphEdge(
#    edge_for=[RemoteUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=MemberOf_CommunicationLinks",
#    tooltip="RTUs may be attached to communication links.")

#RemoteUnit_Contains_RemotePoints_GraphEdge = GraphEdge(
#    edge_for=[RemoteUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_RemotePoints",
#    tooltip="")

#BranchGroup_BranchGroupTerminal_GraphEdge = GraphEdge(
#    edge_for=[BranchGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=BranchGroupTerminal",
#    tooltip="")

#OperationalLimitType_OperationalLimit_GraphEdge = GraphEdge(
#    edge_for=[OperationalLimitType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperationalLimit",
#    tooltip="")

#OperationalLimitSet_OperationalLimitValue_GraphEdge = GraphEdge(
#    edge_for=[OperationalLimitSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperationalLimitValue",
#    tooltip="")

#ControlAreaGeneratingUnit_AltGeneratingUnitMeas_GraphEdge = GraphEdge(
#    edge_for=[ControlAreaGeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=AltGeneratingUnitMeas",
#    tooltip="")

#ControlArea_BusNameMarker_GraphEdge = GraphEdge(
#    edge_for=[ControlArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=BusNameMarker",
#    tooltip="")

#ControlArea_TopologicalNode_GraphEdge = GraphEdge(
#    edge_for=[ControlArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TopologicalNode",
#    tooltip="")

#ControlArea_ControlAreaGeneratingUnit_GraphEdge = GraphEdge(
#    edge_for=[ControlArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ControlAreaGeneratingUnit",
#    tooltip="")

#ControlArea_TieFlow_GraphEdge = GraphEdge(
#    edge_for=[ControlArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TieFlow",
#    tooltip="")

#TieFlow_AltTieMeas_GraphEdge = GraphEdge(
#    edge_for=[TieFlow],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=AltTieMeas",
#    tooltip="")

#EquivalentNetwork_EquivalentEquipments_GraphEdge = GraphEdge(
#    edge_for=[EquivalentNetwork],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EquivalentEquipments",
#    tooltip="")

#TopologicalNode_ConnectivityNodes_GraphEdge = GraphEdge(
#    edge_for=[TopologicalNode],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConnectivityNodes",
#    tooltip="Several ConnectivityNode(s) may combine together to form a single TopologicalNode, depending on the current state of the network.")

#TopologicalNode_Terminal_GraphEdge = GraphEdge(
#    edge_for=[TopologicalNode],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Terminal",
#    tooltip="")

#TopologicalIsland_TopologicalNodes_GraphEdge = GraphEdge(
#    edge_for=[TopologicalIsland],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TopologicalNodes",
#    tooltip="A topological node belongs to a topological island")

#ConnectivityNode_Terminals_GraphEdge = GraphEdge(
#    edge_for=[ConnectivityNode],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Terminals",
#    tooltip="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

#BusNameMarker_ConnectivityNode_GraphEdge = GraphEdge(
#    edge_for=[BusNameMarker],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConnectivityNode",
#    tooltip="")

#ProtectionEquipment_Operates_Breakers_GraphEdge = GraphEdge(
#    edge_for=[ProtectionEquipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Operates_Breakers",
#    tooltip="Circuit breakers may be operated by protection relays.")

#ProtectionEquipment_ConductingEquipments_GraphEdge = GraphEdge(
#    edge_for=[ProtectionEquipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConductingEquipments",
#    tooltip="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.")

#------------------------------------------------------------------------------
#  Graph node list:
#------------------------------------------------------------------------------


graph_nodes = [
    Element_GraphNode,
    CommonInformationModel_GraphNode,
    IEC61970CIMVersion_GraphNode,
    MutualCoupling_GraphNode,
    Quality61850_GraphNode,
    MeasurementValueQuality_GraphNode,
    Analog_GraphNode,
    AccumulatorValue_GraphNode,
    Season_GraphNode,
    IrregularTimePoint_GraphNode,
    OperatingShare_GraphNode,
    CurveData_GraphNode,
    RegularTimePoint_GraphNode,
    IdentifiedObject_GraphNode,
    Contingency_GraphNode,
    ContingencyElement_GraphNode,
    ClearanceTagType_GraphNode,
    SwitchingOperation_GraphNode,
    ClearanceTag_GraphNode,
    RemotePoint_GraphNode,
    RemoteControl_GraphNode,
    RemoteSource_GraphNode,
    OperationalLimit_GraphNode,
    BranchGroup_GraphNode,
    OperationalLimitType_GraphNode,
    ActivePowerLimit_GraphNode,
    CurrentLimit_GraphNode,
    OperationalLimitSet_GraphNode,
    VoltageLimit_GraphNode,
    BranchGroupTerminal_GraphNode,
    ApparentPowerLimit_GraphNode,
    ControlAreaGeneratingUnit_GraphNode,
    AltGeneratingUnitMeas_GraphNode,
    TieFlow_GraphNode,
    AltTieMeas_GraphNode,
    TopologicalNode_GraphNode,
    TopologicalIsland_GraphNode,
    ConnectivityNode_GraphNode,
    BusNameMarker_GraphNode,
    RecloseSequence_GraphNode,
    GroundDisconnector_GraphNode,
    WireType_GraphNode,
    ProtectedSwitch_GraphNode,
    Jumper_GraphNode,
    WireArrangement_GraphNode,
    Fuse_GraphNode,
    WindingTest_GraphNode,
    Disconnector_GraphNode,
    ConductorType_GraphNode,
    ReactiveCapabilityCurve_GraphNode,
    NuclearGeneratingUnit_GraphNode,
    StartIgnFuelCurve_GraphNode,
    HydroGeneratingEfficiencyCurve_GraphNode,
    TargetLevelSchedule_GraphNode,
    GrossToNetActivePowerCurve_GraphNode,
    IncrementalHeatRateCurve_GraphNode,
    HeatInputCurve_GraphNode,
    StartRampCurve_GraphNode,
    ShutdownCurve_GraphNode,
    StartupModel_GraphNode,
    EmissionCurve_GraphNode,
    GenUnitOpCostCurve_GraphNode,
    HydroGeneratingUnit_GraphNode,
    LevelVsVolumeCurve_GraphNode,
    ThermalGeneratingUnit_GraphNode,
    FossilFuel_GraphNode,
    FuelAllocationSchedule_GraphNode,
    EmissionAccount_GraphNode,
    TailbayLossCurve_GraphNode,
    PenstockLossCurve_GraphNode,
    StartMainFuelCurve_GraphNode,
    HeatRateCurve_GraphNode,
    CTTempActivePowerCurve_GraphNode,
    Discrete_GraphNode,
    Measurement_GraphNode,
    SetPoint_GraphNode,
    Control_GraphNode,
    ControlType_GraphNode,
    DiscreteValue_GraphNode,
    Accumulator_GraphNode,
    LimitSet_GraphNode,
    AnalogLimit_GraphNode,
    MeasurementValue_GraphNode,
    ValueAliasSet_GraphNode,
    StringMeasurementValue_GraphNode,
    Limit_GraphNode,
    MeasurementType_GraphNode,
    AccumulatorLimit_GraphNode,
    StringMeasurement_GraphNode,
    ValueToAlias_GraphNode,
    AnalogValue_GraphNode,
    MeasurementValueSource_GraphNode,
    AccumulatorLimitSet_GraphNode,
    AnalogLimitSet_GraphNode,
    Command_GraphNode,
    LoadResponseCharacteristic_GraphNode,
    DayType_GraphNode,
    LoadGroup_GraphNode,
    NonConformLoadGroup_GraphNode,
    EnergyArea_GraphNode,
    InductionMotorLoad_GraphNode,
    Curve_GraphNode,
    ReportingGroup_GraphNode,
    ModelingAuthoritySet_GraphNode,
    OperatingParticipant_GraphNode,
    ReportingSuperGroup_GraphNode,
    GeographicalRegion_GraphNode,
    Unit_GraphNode,
    ModelingAuthority_GraphNode,
    BaseVoltage_GraphNode,
    BasicIntervalSchedule_GraphNode,
    RegularIntervalSchedule_GraphNode,
    IrregularIntervalSchedule_GraphNode,
    Terminal_GraphNode,
    SubGeographicalRegion_GraphNode,
    PowerSystemResource_GraphNode,
    BasePower_GraphNode,
    PSRType_GraphNode,
    PsrList_GraphNode,
    Company_GraphNode,
    ContingencyEquipment_GraphNode,
    OutageSchedule_GraphNode,
    CommunicationLink_GraphNode,
    RemoteUnit_GraphNode,
    ControlArea_GraphNode,
    ProtectionEquipment_GraphNode,
    CurrentRelay_GraphNode,
    RegulationSchedule_GraphNode,
    Breaker_GraphNode,
    VoltageControlZone_GraphNode,
    LoadBreakSwitch_GraphNode,
    DCLineSegment_GraphNode,
    TapChanger_GraphNode,
    CompositeSwitch_GraphNode,
    PowerTransformer_GraphNode,
    ACLineSegment_GraphNode,
    HeatExchanger_GraphNode,
    RegulatingControl_GraphNode,
    GeneratingUnit_GraphNode,
    AirCompressor_GraphNode,
    CombinedCyclePlant_GraphNode,
    HydroPump_GraphNode,
    HydroPowerPlant_GraphNode,
    CAESPlant_GraphNode,
    InflowForecast_GraphNode,
    SteamSendoutSchedule_GraphNode,
    Reservoir_GraphNode,
    HydroPumpOpSchedule_GraphNode,
    GenUnitOpSchedule_GraphNode,
    CogenerationPlant_GraphNode,
    PrimeMover_GraphNode,
    CombustionTurbine_GraphNode,
    HydroTurbine_GraphNode,
    SteamSupply_GraphNode,
    SubLoadArea_GraphNode,
    Load_GraphNode,
    ConformLoadGroup_GraphNode,
    LoadArea_GraphNode,
    PowerCutZone_GraphNode,
    CustomerLoad_GraphNode,
    SeasonDayTypeSchedule_GraphNode,
    ConductingEquipment_GraphNode,
    ConnectivityNodeContainer_GraphNode,
    EquipmentContainer_GraphNode,
    Equipment_GraphNode,
    Bay_GraphNode,
    EquivalentNetwork_GraphNode,
    EquivalentEquipment_GraphNode,
    SynchrocheckRelay_GraphNode,
    TransformerWinding_GraphNode,
    EnergySource_GraphNode,
    SeriesCompensator_GraphNode,
    RegulatingCondEq_GraphNode,
    Conductor_GraphNode,
    Line_GraphNode,
    Ground_GraphNode,
    ShuntCompensator_GraphNode,
    RectifierInverter_GraphNode,
    EnergyConsumer_GraphNode,
    Switch_GraphNode,
    SynchronousMachine_GraphNode,
    Connector_GraphNode,
    StaticVarCompensator_GraphNode,
    Junction_GraphNode,
    Plant_GraphNode,
    SteamTurbine_GraphNode,
    PWRSteamSupply_GraphNode,
    BWRSteamSupply_GraphNode,
    FossilSteamSupply_GraphNode,
    Subcritical_GraphNode,
    ConformLoad_GraphNode,
    ConformLoadSchedule_GraphNode,
    StationSupply_GraphNode,
    NonConformLoadSchedule_GraphNode,
    NonConformLoad_GraphNode,
    VoltageLevel_GraphNode,
    Substation_GraphNode,
    EquivalentBranch_GraphNode,
    EquivalentShunt_GraphNode,
    FrequencyConverter_GraphNode,
    BusbarSection_GraphNode,
    Supercritical_GraphNode,
    HeatRecoveryBoiler_GraphNode,
    DrumBoiler_GraphNode,
]
graph_nodes.reverse()

#graph_edges = [
#    CommonInformationModel_Elements_GraphEdge,
#    Analog_Contain_MeasurementValues_GraphEdge,
#    Analog_LimitSets_GraphEdge,
#    Season_SeasonDayTypeSchedules_GraphEdge,
#    Contingency_ContingencyElement_GraphEdge,
#    ClearanceTagType_ClearanceTags_GraphEdge,
#    SwitchingOperation_Switches_GraphEdge,
#    BranchGroup_BranchGroupTerminal_GraphEdge,
#    OperationalLimitType_OperationalLimit_GraphEdge,
#    OperationalLimitSet_OperationalLimitValue_GraphEdge,
#    ControlAreaGeneratingUnit_AltGeneratingUnitMeas_GraphEdge,
#    TieFlow_AltTieMeas_GraphEdge,
#    TopologicalNode_ConnectivityNodes_GraphEdge,
#    TopologicalNode_Terminal_GraphEdge,
#    TopologicalIsland_TopologicalNodes_GraphEdge,
#    ConnectivityNode_Terminals_GraphEdge,
#    BusNameMarker_ConnectivityNode_GraphEdge,
#    WireType_WireArrangements_GraphEdge,
#    ProtectedSwitch_OperatedBy_ProtectionEquipments_GraphEdge,
#    ProtectedSwitch_RecloseSequences_GraphEdge,
#    ConductorType_Conductors_GraphEdge,
#    ConductorType_WireArrangements_GraphEdge,
#    ReactiveCapabilityCurve_SynchronousMachines_GraphEdge,
#    ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_GraphEdge,
#    HydroGeneratingUnit_HydroGeneratingEfficiencyCurves_GraphEdge,
#    HydroGeneratingUnit_TailbayLossCurve_GraphEdge,
#    ThermalGeneratingUnit_FuelAllocationSchedules_GraphEdge,
#    ThermalGeneratingUnit_EmissionCurves_GraphEdge,
#    ThermalGeneratingUnit_EmmissionAccounts_GraphEdge,
#    ThermalGeneratingUnit_FossilFuels_GraphEdge,
#    FossilFuel_FuelAllocationSchedule_GraphEdge,
#    Discrete_Contain_MeasurementValues_GraphEdge,
#    ControlType_Controls_GraphEdge,
#    Accumulator_Contain_MeasurementValues_GraphEdge,
#    Accumulator_LimitSets_GraphEdge,
#    ValueAliasSet_Values_GraphEdge,
#    ValueAliasSet_Commands_GraphEdge,
#    ValueAliasSet_Measurements_GraphEdge,
#    MeasurementType_Measurements_GraphEdge,
#    StringMeasurement_Contains_MeasurementValues_GraphEdge,
#    AnalogValue_AltGeneratingUnit_GraphEdge,
#    AnalogValue_AltTieMeas_GraphEdge,
#    MeasurementValueSource_MeasurementValues_GraphEdge,
#    AccumulatorLimitSet_Measurements_GraphEdge,
#    AccumulatorLimitSet_Limits_GraphEdge,
#    AnalogLimitSet_Limits_GraphEdge,
#    AnalogLimitSet_Measurements_GraphEdge,
#    LoadResponseCharacteristic_EnergyConsumer_GraphEdge,
#    DayType_SeasonDayTypeSchedules_GraphEdge,
#    NonConformLoadGroup_NonConformLoadSchedules_GraphEdge,
#    NonConformLoadGroup_EnergyConsumers_GraphEdge,
#    Curve_CurveScheduleDatas_GraphEdge,
#    ReportingGroup_PowerSystemResource_GraphEdge,
#    ReportingGroup_BusNameMarker_GraphEdge,
#    ReportingGroup_TopologicalNode_GraphEdge,
#    ModelingAuthoritySet_IdentifiedObjects_GraphEdge,
#    OperatingParticipant_OperatingShare_GraphEdge,
#    ReportingSuperGroup_ReportingGroup_GraphEdge,
#    GeographicalRegion_Regions_GraphEdge,
#    Unit_Controls_GraphEdge,
#    Unit_ProtectionEquipments_GraphEdge,
#    Unit_Measurements_GraphEdge,
#    ModelingAuthority_ModelingAuthoritySets_GraphEdge,
#    BaseVoltage_ConductingEquipment_GraphEdge,
#    BaseVoltage_VoltageLevel_GraphEdge,
#    RegularIntervalSchedule_TimePoints_GraphEdge,
#    IrregularIntervalSchedule_TimePoints_GraphEdge,
#    Terminal_TieFlow_GraphEdge,
#    Terminal_OperationalLimitSet_GraphEdge,
#    Terminal_BranchGroupTerminal_GraphEdge,
#    Terminal_RegulatingControl_GraphEdge,
#    Terminal_Measurements_GraphEdge,
#    SubGeographicalRegion_Lines_GraphEdge,
#    SubGeographicalRegion_Substations_GraphEdge,
#    PowerSystemResource_OperatedBy_Companies_GraphEdge,
#    PowerSystemResource_ReportingGroup_GraphEdge,
#    PowerSystemResource_OperatingShare_GraphEdge,
#    PowerSystemResource_PsrLists_GraphEdge,
#    PowerSystemResource_Contains_Measurements_GraphEdge,
#    PSRType_PowerSystemResource_GraphEdge,
#    PsrList_PowerSystemResources_GraphEdge,
#    Company_Operates_PSRs_GraphEdge,
#    OutageSchedule_SwitchingOperations_GraphEdge,
#    CommunicationLink_Contain_RemoteUnits_GraphEdge,
#    RemoteUnit_MemberOf_CommunicationLinks_GraphEdge,
#    RemoteUnit_Contains_RemotePoints_GraphEdge,
#    ControlArea_BusNameMarker_GraphEdge,
#    ControlArea_TopologicalNode_GraphEdge,
#    ControlArea_ControlAreaGeneratingUnit_GraphEdge,
#    ControlArea_TieFlow_GraphEdge,
#    ProtectionEquipment_Operates_Breakers_GraphEdge,
#    ProtectionEquipment_ConductingEquipments_GraphEdge,
#    RegulationSchedule_RegulatingControl_GraphEdge,
#    RegulationSchedule_VoltageControlZones_GraphEdge,
#    CompositeSwitch_Switches_GraphEdge,
#    PowerTransformer_Contains_TransformerWindings_GraphEdge,
#    ACLineSegment_HasFirst_MutualCoupling_GraphEdge,
#    ACLineSegment_HasSecond_MutualCoupling_GraphEdge,
#    RegulatingControl_RegulatingCondEq_GraphEdge,
#    RegulatingControl_TapChanger_GraphEdge,
#    GeneratingUnit_ControlAreaGeneratingUnit_GraphEdge,
#    GeneratingUnit_GrossToNetActivePowerCurves_GraphEdge,
#    GeneratingUnit_Contains_SynchronousMachines_GraphEdge,
#    GeneratingUnit_GenUnitOpCostCurves_GraphEdge,
#    CombinedCyclePlant_Contain_ThermalGeneratingUnits_GraphEdge,
#    HydroPowerPlant_Contain_HydroGeneratingUnits_GraphEdge,
#    HydroPowerPlant_Contain_HydroPumps_GraphEdge,
#    Reservoir_LevelVsVolumeCurve_GraphEdge,
#    Reservoir_InflowForecast_GraphEdge,
#    Reservoir_SpillsInto_GraphEdge,
#    Reservoir_HydroPowerPlants_GraphEdge,
#    Reservoir_UpstreamFrom_GraphEdge,
#    CogenerationPlant_Contain_ThermalGeneratingUnits_GraphEdge,
#    PrimeMover_Drives_SynchronousMachines_GraphEdge,
#    SteamSupply_SteamTurbines_GraphEdge,
#    SubLoadArea_LoadGroups_GraphEdge,
#    ConformLoadGroup_EnergyConsumers_GraphEdge,
#    ConformLoadGroup_ConformLoadSchedules_GraphEdge,
#    LoadArea_SubLoadAreas_GraphEdge,
#    PowerCutZone_EnergyConsumers_GraphEdge,
#    ConductingEquipment_Terminals_GraphEdge,
#    ConductingEquipment_ProtectionEquipments_GraphEdge,
#    ConductingEquipment_ClearanceTags_GraphEdge,
#    ConnectivityNodeContainer_TopologicalNode_GraphEdge,
#    ConnectivityNodeContainer_ConnectivityNodes_GraphEdge,
#    EquipmentContainer_Contains_Equipments_GraphEdge,
#    Equipment_OperationalLimitSet_GraphEdge,
#    Equipment_ContingencyEquipment_GraphEdge,
#    EquivalentNetwork_EquivalentEquipments_GraphEdge,
#    TransformerWinding_To_WindingTest_GraphEdge,
#    TransformerWinding_From_WindingTest_GraphEdge,
#    TransformerWinding_TapChangers_GraphEdge,
#    RegulatingCondEq_Controls_GraphEdge,
#    Switch_SwitchingOperations_GraphEdge,
#    SynchronousMachine_ReactiveCapabilityCurves_GraphEdge,
#    SynchronousMachine_DrivenBy_PrimeMover_GraphEdge,
#    SteamTurbine_SteamSupplys_GraphEdge,
#    VoltageLevel_Contains_Bays_GraphEdge,
#    Substation_Contains_VoltageLevels_GraphEdge,
#    Substation_Contains_Bays_GraphEdge,
#    HeatRecoveryBoiler_CombustionTurbines_GraphEdge,
#]
#graph_edges.reverse()

#------------------------------------------------------------------------------
#  CIM13r19 Graph Editor:
#------------------------------------------------------------------------------

CIM13r19GraphEditor = GraphEditor(nodes=graph_nodes)

# EOF -------------------------------------------------------------------------
