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

""" Defines a graph editor for CPSM.
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

from godot.ui.graph_editor import GraphNode, GraphEditor

from CPSM import *
from CPSM.Generation import *
from CPSM.OperationalLimits import *
from CPSM.Wires import *
from CPSM.Meas import *
from CPSM.LoadModel import *
from CPSM.Equivalents import *
from CPSM.Core import *
from CPSM.ControlArea import *
from CPSM.Domain import *
from CPSM.Topology import *
from CPSM.Generation.Production import *

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
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IEC61970CIMVersion_GraphNode = GraphNode(
    node_for=[IEC61970CIMVersion],
        tooltip="This is the IEC 61970 CIM version number assigned to this UML model file.This is the IEC 61970 CIM version number assigned to this UML model file.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CommonPowerSystemModel_GraphNode = GraphNode(
    node_for=[CommonPowerSystemModel],
        tooltip="",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GrossToNetActivePowerCurve_GraphNode = GraphNode(
    node_for=[GrossToNetActivePowerCurve],
    label="name",
    tooltip="Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.Relationship between the generating unit's gross active power output on the X-axis (measured at the terminals of the machine(s)) and the generating unit's net active power output on the Y-axis (based on utility-defined measurements at the power station). Station service loads, when modeled, should be treated as non-conforming bus loads. There may be more than one curve, depending on the auxiliary equipment that is in service.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

HydroGeneratingUnit_GraphNode = GraphNode(
    node_for=[HydroGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)A generating unit whose prime mover is a hydraulic turbine (e.g., Francis, Pelton, Kaplan)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ThermalGeneratingUnit_GraphNode = GraphNode(
    node_for=[ThermalGeneratingUnit],
    label="name",
    tooltip="A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.A generating unit whose prime mover could be a steam turbine, combustion turbine, or diesel engine.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GeneratingUnit_GraphNode = GraphNode(
    node_for=[GeneratingUnit],
    label="name",
    tooltip="A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.A single or set of synchronous machines for converting mechanical power into alternating-current power. For example, individual machines within a set may be defined for scheduling purposes while a single control signal is derived for the set. In this case there would be a GeneratingUnit for each member of the set and an additional GeneratingUnit corresponding to the set.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperationalLimit_GraphNode = GraphNode(
    node_for=[OperationalLimit],
    label="name",
    tooltip="A value associated with a specific kind of limit.A value associated with a specific kind of limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

OperationalLimitSet_GraphNode = GraphNode(
    node_for=[OperationalLimitSet],
    label="name",
    tooltip="A set of limits associated with equipmnet.A set of limits associated with equipmnet.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ActivePowerLimit_GraphNode = GraphNode(
    node_for=[ActivePowerLimit],
    label="name",
    tooltip="Limit on active power flow.Limit on active power flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ApparentPowerLimit_GraphNode = GraphNode(
    node_for=[ApparentPowerLimit],
    label="name",
    tooltip="Apparent power limit.Apparent power limit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

VoltageLimit_GraphNode = GraphNode(
    node_for=[VoltageLimit],
    label="name",
    tooltip="Operational limit applied to voltage.Operational limit applied to voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CurrentLimit_GraphNode = GraphNode(
    node_for=[CurrentLimit],
    label="name",
    tooltip="OIoeratuibak kimit on current.OIoeratuibak kimit on current.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PowerTransformer_GraphNode = GraphNode(
    node_for=[PowerTransformer],
    label="name",
    tooltip="An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Disconnector_GraphNode = GraphNode(
    node_for=[Disconnector],
    label="name",
    tooltip="A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SynchronousMachine_GraphNode = GraphNode(
    node_for=[SynchronousMachine],
    label="name",
    tooltip="An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BusbarSection_GraphNode = GraphNode(
    node_for=[BusbarSection],
    label="name",
    tooltip="A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ShuntCompensator_GraphNode = GraphNode(
    node_for=[ShuntCompensator],
    label="name",
    tooltip="A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadBreakSwitch_GraphNode = GraphNode(
    node_for=[LoadBreakSwitch],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegulatingCondEq_GraphNode = GraphNode(
    node_for=[RegulatingCondEq],
    label="name",
    tooltip="RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EnergyConsumer_GraphNode = GraphNode(
    node_for=[EnergyConsumer],
    label="name",
    tooltip="Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TransformerWinding_GraphNode = GraphNode(
    node_for=[TransformerWinding],
    label="name",
    tooltip="A winding is associated with each defined terminal of a transformer (or phase shifter).A winding is associated with each defined terminal of a transformer (or phase shifter).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegulatingControl_GraphNode = GraphNode(
    node_for=[RegulatingControl],
    label="name",
    tooltip="Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegulationSchedule_GraphNode = GraphNode(
    node_for=[RegulationSchedule],
    label="name",
    tooltip="A pre-established pattern over time for a controlled variable, e.g., busbar voltage.A pre-established pattern over time for a controlled variable, e.g., busbar voltage.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ACLineSegment_GraphNode = GraphNode(
    node_for=[ACLineSegment],
    label="name",
    tooltip="A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Switch_GraphNode = GraphNode(
    node_for=[Switch],
    label="name",
    tooltip="A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Conductor_GraphNode = GraphNode(
    node_for=[Conductor],
    label="name",
    tooltip="Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ReactiveCapabilityCurve_GraphNode = GraphNode(
    node_for=[ReactiveCapabilityCurve],
    label="name",
    tooltip="Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TapChanger_GraphNode = GraphNode(
    node_for=[TapChanger],
    label="name",
    tooltip="Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Line_GraphNode = GraphNode(
    node_for=[Line],
    label="name",
    tooltip="A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StaticVarCompensator_GraphNode = GraphNode(
    node_for=[StaticVarCompensator],
    label="name",
    tooltip="A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SeriesCompensator_GraphNode = GraphNode(
    node_for=[SeriesCompensator],
    label="name",
    tooltip="A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Breaker_GraphNode = GraphNode(
    node_for=[Breaker],
    label="name",
    tooltip="A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

DiscreteValue_GraphNode = GraphNode(
    node_for=[DiscreteValue],
    label="name",
    tooltip="DiscreteValue represents a discrete MeasurementValue.DiscreteValue represents a discrete MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Measurement_GraphNode = GraphNode(
    node_for=[Measurement],
    label="name",
    tooltip="A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.A Measurement represents any measured, calculated or non-measured non-calculated quantity. Any piece of equipment may contain Measurements, e.g. a substation may have temperature measurements and door open indications, a transformer may have oil temperature and tank pressure measurements, a bay may contain a number of  power flow measurements and a Breaker may contain a switch status measurement.  The PSR - Measurement association is intended to capture this use of Measurement and is included in the naming hierarchy based on EquipmentContainer. The naming hierarchy typically has Measurements as leafs, e.g. Substation-VoltageLevel-Bay-Switch-Measurement. Some Measurements represent quantities related to a particular sensor location in the network, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is not captured in the PSR - Measurement association. Instead it is captured by the Measurement - Terminal association that is used to define the sensing location in the network topology. The location is defined by the connection of the Terminal to ConductingEquipment.  Two possible paths exist: 1) Measurement-Terminal- ConnectivityNode-Terminal-ConductingEquipment 2) Measurement-Terminal-ConductingEquipment Alternative 2 is the only allowed use.  When the sensor location is needed both Measurement-PSR and Measurement-Terminal are used. The Measurement-Terminal association is never used alone.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementValue_GraphNode = GraphNode(
    node_for=[MeasurementValue],
    label="name",
    tooltip="The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.The current state for a measurement. A state value is an instance of a measurement from a specific source. Measurements can be associated with many state values, each representing a different source for the measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementValueSource_GraphNode = GraphNode(
    node_for=[MeasurementValueSource],
    label="name",
    tooltip="MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.MeasurementValueSource describes the alternative sources updating a MeasurementValue. User conventions for how to use the MeasurementValueSource attributes are described in the introduction to IEC 61970-301.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Analog_GraphNode = GraphNode(
    node_for=[Analog],
    label="name",
    tooltip="Analog represents an analog Measurement.Analog represents an analog Measurement.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

AnalogValue_GraphNode = GraphNode(
    node_for=[AnalogValue],
    label="name",
    tooltip="AnalogValue represents an analog MeasurementValue.AnalogValue represents an analog MeasurementValue.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

MeasurementType_GraphNode = GraphNode(
    node_for=[MeasurementType],
    label="name",
    tooltip="Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.Specifies the type of Measurement, e.g. IndoorTemperature, OutDoorTemperature, BusVoltage, GeneratorVoltage, LineFlow etc. The MeasurementType.name shall be unique among all specified types and describe the type. The MeasurementType.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Discrete_GraphNode = GraphNode(
    node_for=[Discrete],
    label="name",
    tooltip="Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.Discrete represents a discrete Measurement, i.e. a Measurement reprsenting discrete values, e.g. a Breaker position.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LimitSet_GraphNode = GraphNode(
    node_for=[LimitSet],
    label="name",
    tooltip="Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.Specifies a set of Limits that are associated with a Measurement. A Measurement may have several LimitSets corresponding to seasonal or other changing conditions. The condition is captured in the name and description attributes. The same LimitSet may be used for several Measurements. In particular percentage limits are used this way.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NonConformLoadGroup_GraphNode = GraphNode(
    node_for=[NonConformLoadGroup],
    label="name",
    tooltip="Loads that do not follow a daily and seasonal load variation pattern.Loads that do not follow a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConformLoadSchedule_GraphNode = GraphNode(
    node_for=[ConformLoadSchedule],
    label="name",
    tooltip="A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.A curve of load  versus time (X-axis) showing the active power values (Y1-axis) and reactive power (Y2-axis) for each unit of the period covered. This curve represents a typical pattern of load over the time period for a given day type and season.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CustomerLoad_GraphNode = GraphNode(
    node_for=[CustomerLoad],
    label="name",
    tooltip="A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.A meter for measuring customer energy consumption. The typeName attribute indicates the type of customer meter.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NonConformLoad_GraphNode = GraphNode(
    node_for=[NonConformLoad],
    label="name",
    tooltip="NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.NonConformLoad represent loads that do not follow a daily load change pattern and changes are not correlated with the daily load change pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

DayType_GraphNode = GraphNode(
    node_for=[DayType],
    label="name",
    tooltip="Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2Group of similar days, e.g., Mon/Tue/Wed, Thu/Fri, Sat/Sun, Holiday1, Holiday2",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Season_GraphNode = GraphNode(
    node_for=[Season],
    label="name",
    tooltip="A specified time period of the year, e.g., Spring, Summer, Fall, WinterA specified time period of the year, e.g., Spring, Summer, Fall, Winter",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Load_GraphNode = GraphNode(
    node_for=[Load],
    label="name",
    tooltip="A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.A generic equivalent for an energy consumer on a transmission or distribution voltage level. It may be under load management and also has cold load pick up characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

StationSupply_GraphNode = GraphNode(
    node_for=[StationSupply],
    label="name",
    tooltip="Station supply with load derived from the station output.Station supply with load derived from the station output.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SeasonDayTypeSchedule_GraphNode = GraphNode(
    node_for=[SeasonDayTypeSchedule],
    label="name",
    tooltip="The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.The schedule specialize RegularIntervalSchedule with type curve data for a specific type of day and season. This means that curves of this type cover a 24 hour period.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadGroup_GraphNode = GraphNode(
    node_for=[LoadGroup],
    label="name",
    tooltip="The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the third level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EnergyArea_GraphNode = GraphNode(
    node_for=[EnergyArea],
    label="name",
    tooltip="The class describes an area having energy production or consumption. The class is the basis for further specialization.The class describes an area having energy production or consumption. The class is the basis for further specialization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConformLoadGroup_GraphNode = GraphNode(
    node_for=[ConformLoadGroup],
    label="name",
    tooltip="Load that follows a daily and seasonal load variation pattern.Load that follows a daily and seasonal load variation pattern.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadArea_GraphNode = GraphNode(
    node_for=[LoadArea],
    label="name",
    tooltip="The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the root or first level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SubLoadArea_GraphNode = GraphNode(
    node_for=[SubLoadArea],
    label="name",
    tooltip="The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.The class is the second level in a hierarchical structure for grouping of loads for the purpose of load flow load scaling.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

LoadResponseCharacteristic_GraphNode = GraphNode(
    node_for=[LoadResponseCharacteristic],
    label="name",
    tooltip="Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.Models the characteristic response of the load demand due to to changes in system conditions such as voltage and frequency. This is not related to demand response.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

NonConformLoadSchedule_GraphNode = GraphNode(
    node_for=[NonConformLoadSchedule],
    label="name",
    tooltip="An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)An active power (Y1-axis) and reactive power (Y2-axis) schedule (curves) versus time (X-axis) for non-conforming loads, e.g., large industrial load or power station service (where modeled)",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

InductionMotorLoad_GraphNode = GraphNode(
    node_for=[InductionMotorLoad],
    label="name",
    tooltip="Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).Large three phase induction motor load. The typeName attribute indicates the type of induction motor (1 = wound rotor) (2 = squirrel cage).",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConformLoad_GraphNode = GraphNode(
    node_for=[ConformLoad],
    label="name",
    tooltip="ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.ConformLoad represent loads that follow a daily load change pattern where the pattern can be used to scale the load with a system load.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentNetwork_GraphNode = GraphNode(
    node_for=[EquivalentNetwork],
    label="name",
    tooltip="A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentShunt_GraphNode = GraphNode(
    node_for=[EquivalentShunt],
    label="name",
    tooltip="The class represents equivalent shunts.The class represents equivalent shunts.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentEquipment_GraphNode = GraphNode(
    node_for=[EquivalentEquipment],
    label="name",
    tooltip="The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquivalentBranch_GraphNode = GraphNode(
    node_for=[EquivalentBranch],
    label="name",
    tooltip="The class represents equivalent branches.The class represents equivalent branches.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

IdentifiedObject_GraphNode = GraphNode(
    node_for=[IdentifiedObject],
    label="name",
    tooltip="This is a root class to provide common naming attributes for all classes needing naming attributesThis is a root class to provide common naming attributes for all classes needing naming attributes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Terminal_GraphNode = GraphNode(
    node_for=[Terminal],
    label="name",
    tooltip="An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.An electrical connection point to a piece of conducting equipment. Terminals are connected at physical connection points called 'connectivity nodes'.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BaseVoltage_GraphNode = GraphNode(
    node_for=[BaseVoltage],
    label="name",
    tooltip="Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.Collection of BaseVoltages which is used to verify that the BusbarSection.BaseVoltage and other voltage attributes in the CIM are given a value existing in the collection.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegularIntervalSchedule_GraphNode = GraphNode(
    node_for=[RegularIntervalSchedule],
    label="name",
    tooltip="The schedule has TimePoints where the time between them is constant.The schedule has TimePoints where the time between them is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConnectivityNodeContainer_GraphNode = GraphNode(
    node_for=[ConnectivityNodeContainer],
    label="name",
    tooltip="A base class for all objects that may contain ConnectivityNodes.A base class for all objects that may contain ConnectivityNodes.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Unit_GraphNode = GraphNode(
    node_for=[Unit],
    label="name",
    tooltip="Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

EquipmentContainer_GraphNode = GraphNode(
    node_for=[EquipmentContainer],
    label="name",
    tooltip="A modeling construct to provide a root class for all Equipment classesA modeling construct to provide a root class for all Equipment classes",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

VoltageLevel_GraphNode = GraphNode(
    node_for=[VoltageLevel],
    label="name",
    tooltip="A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.A collection of equipment at one common system voltage forming a switchgear. The equipment typically consist of breakers, busbars, instrumentation, control, regulation and protection devices as well as assemblies of all these.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Bay_GraphNode = GraphNode(
    node_for=[Bay],
    label="name",
    tooltip="A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.A collection of power system resources (within a given substation) including conducting equipment, protection relays, measurements, and telemetry.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

SubGeographicalRegion_GraphNode = GraphNode(
    node_for=[SubGeographicalRegion],
    label="name",
    tooltip="A subset of a geographical region of a power system network model.A subset of a geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

RegularTimePoint_GraphNode = GraphNode(
    node_for=[RegularTimePoint],
        tooltip="TimePoints for a schedule where the time between the points is constant.TimePoints for a schedule where the time between the points is constant.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Equipment_GraphNode = GraphNode(
    node_for=[Equipment],
    label="name",
    tooltip="The parts of a power system that are physical devices, electronic or mechanicalThe parts of a power system that are physical devices, electronic or mechanical",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Substation_GraphNode = GraphNode(
    node_for=[Substation],
    label="name",
    tooltip="A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

Curve_GraphNode = GraphNode(
    node_for=[Curve],
    label="name",
    tooltip="Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.Relationship between an independent variable (X-axis) and one or two dependent  variables (Y1-axis and Y2-axis). Curves can also serve as schedules.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

PowerSystemResource_GraphNode = GraphNode(
    node_for=[PowerSystemResource],
    label="name",
    tooltip="A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.A power system resource can be an item of equipment such as a Switch, an EquipmentContainer containing many individual items of equipment such as a  Substation, or an organisational entity such as Company or SubControlArea.  This provides for the nesting of collections of PowerSystemResources within other PowerSystemResources. For example, a Switch could be a member of a Substation and a Substation could be a member of a division of a Company.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

BasicIntervalSchedule_GraphNode = GraphNode(
    node_for=[BasicIntervalSchedule],
    label="name",
    tooltip="Schedule of values at points in time.Schedule of values at points in time.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

CurveData_GraphNode = GraphNode(
    node_for=[CurveData],
        tooltip="Data point values for defining a curve or scheduleData point values for defining a curve or schedule",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

GeographicalRegion_GraphNode = GraphNode(
    node_for=[GeographicalRegion],
    label="name",
    tooltip="A geographical region of a power system network model.A geographical region of a power system network model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConductingEquipment_GraphNode = GraphNode(
    node_for=[ConductingEquipment],
    label="name",
    tooltip="The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.The parts of the power system that are designed to carry current or that are conductively connected therewith. ConductingEquipment is contained within an EquipmentContainer that may be a Substation, or a VoltageLevel or a Bay within a Substation.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ControlArea_GraphNode = GraphNode(
    node_for=[ControlArea],
    label="name",
    tooltip="A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

TieFlow_GraphNode = GraphNode(
    node_for=[TieFlow],
        tooltip="A flow specification in terms of location and direction for a control area.A flow specification in terms of location and direction for a control area.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ControlAreaGeneratingUnit_GraphNode = GraphNode(
    node_for=[ControlAreaGeneratingUnit],
        tooltip="A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

ConnectivityNode_GraphNode = GraphNode(
    node_for=[ConnectivityNode],
    label="name",
    tooltip="Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.Connectivity nodes are points where terminals of conducting equipment are connected together with zero impedance.",
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal"))

#------------------------------------------------------------------------------
#  Graph edges:
#------------------------------------------------------------------------------

#CommonPowerSystemModel_Elements_GraphEdge = GraphEdge(
#    edge_for=[CommonPowerSystemModel],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Elements",
#    tooltip="")

#GeneratingUnit_Contains_SynchronousMachines_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_SynchronousMachines",
#    tooltip="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit")

#GeneratingUnit_GrossToNetActivePowerCurves_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=GrossToNetActivePowerCurves",
#    tooltip="A generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unitA generating unit may have a gross active power to net active power curve, describing the losses and auxiliary power requirements of the unit")

#GeneratingUnit_ControlAreaGeneratingUnit_GraphEdge = GraphEdge(
#    edge_for=[GeneratingUnit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ControlAreaGeneratingUnit",
#    tooltip="ControlArea specifications for this generating unit.ControlArea specifications for this generating unit.")

#OperationalLimitSet_OperationalLimitValue_GraphEdge = GraphEdge(
#    edge_for=[OperationalLimitSet],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperationalLimitValue",
#    tooltip="Values of equipment limits.Values of equipment limits.")

#PowerTransformer_Contains_TransformerWindings_GraphEdge = GraphEdge(
#    edge_for=[PowerTransformer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_TransformerWindings",
#    tooltip="A transformer has windingsA transformer has windings")

#TransformerWinding_TapChangers_GraphEdge = GraphEdge(
#    edge_for=[TransformerWinding],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TapChangers",
#    tooltip="A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.")

#RegulatingControl_TapChanger_GraphEdge = GraphEdge(
#    edge_for=[RegulatingControl],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TapChanger",
#    tooltip="copy from reg conduting eqcopy from reg conduting eq")

#RegulatingControl_RegulatingCondEq_GraphEdge = GraphEdge(
#    edge_for=[RegulatingControl],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RegulatingCondEq",
#    tooltip="copy from reg cond eqcopy from reg cond eq")

#RegulationSchedule_RegulatingControl_GraphEdge = GraphEdge(
#    edge_for=[RegulationSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RegulatingControl",
#    tooltip="Regulating controls that have this Schedule.Regulating controls that have this Schedule.")

#ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_GraphEdge = GraphEdge(
#    edge_for=[ReactiveCapabilityCurve],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=InitiallyUsedBySynchronousMachine",
#    tooltip="Synchronous machines using this curve as default.Synchronous machines using this curve as default.")

#MeasurementValueSource_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[MeasurementValueSource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=MeasurementValues",
#    tooltip="The MeasurementValues updated by the sourceThe MeasurementValues updated by the source")

#Analog_Contain_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[Analog],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_MeasurementValues",
#    tooltip="The values connected to this measurement.The values connected to this measurement.")

#MeasurementType_Measurements_GraphEdge = GraphEdge(
#    edge_for=[MeasurementType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="The measurements associated with the TypeThe measurements associated with the Type")

#Discrete_Contain_MeasurementValues_GraphEdge = GraphEdge(
#    edge_for=[Discrete],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contain_MeasurementValues",
#    tooltip="The values connected to this measurement.The values connected to this measurement.")

#NonConformLoadGroup_NonConformLoadSchedules_GraphEdge = GraphEdge(
#    edge_for=[NonConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=NonConformLoadSchedules",
#    tooltip="The NonConformLoadSchedules in the NonConformLoadGroup.The NonConformLoadSchedules in the NonConformLoadGroup.")

#NonConformLoadGroup_EnergyConsumers_GraphEdge = GraphEdge(
#    edge_for=[NonConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumers",
#    tooltip="Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.")

#DayType_SeasonDayTypeSchedules_GraphEdge = GraphEdge(
#    edge_for=[DayType],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SeasonDayTypeSchedules",
#    tooltip="Schedules that use this DayType.Schedules that use this DayType.")

#Season_SeasonDayTypeSchedules_GraphEdge = GraphEdge(
#    edge_for=[Season],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SeasonDayTypeSchedules",
#    tooltip="Schedules that use this Season.Schedules that use this Season.")

#ConformLoadGroup_EnergyConsumers_GraphEdge = GraphEdge(
#    edge_for=[ConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumers",
#    tooltip="Conform loads assigned to this ConformLoadGroup.Conform loads assigned to this ConformLoadGroup.")

#ConformLoadGroup_ConformLoadSchedules_GraphEdge = GraphEdge(
#    edge_for=[ConformLoadGroup],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConformLoadSchedules",
#    tooltip="The ConformLoadSchedules in the ConformLoadGroup.The ConformLoadSchedules in the ConformLoadGroup.")

#LoadArea_SubLoadAreas_GraphEdge = GraphEdge(
#    edge_for=[LoadArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=SubLoadAreas",
#    tooltip="The SubLoadAreas in the LoadArea.The SubLoadAreas in the LoadArea.")

#SubLoadArea_LoadGroups_GraphEdge = GraphEdge(
#    edge_for=[SubLoadArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=LoadGroups",
#    tooltip="The Loadgroups in the SubLoadArea.The Loadgroups in the SubLoadArea.")

#LoadResponseCharacteristic_EnergyConsumer_GraphEdge = GraphEdge(
#    edge_for=[LoadResponseCharacteristic],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EnergyConsumer",
#    tooltip="The set of loads that have the response characteristics.The set of loads that have the response characteristics.")

#EquivalentNetwork_EquivalentEquipments_GraphEdge = GraphEdge(
#    edge_for=[EquivalentNetwork],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=EquivalentEquipments",
#    tooltip="The associated reduced equivalents.The associated reduced equivalents.")

#Terminal_Measurements_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.One or more measurements may be associated with a terminal in the network. Measurement-Terminal defines where the measurement is placed in the network topology. Some Measurements represent quantities related to a particular sensor position, e.g. a voltage transformer (PT) at a busbar or a current transformer (CT) at the bar between a breaker and an isolator. The sensing position is captured by the Measurement - Terminal association that makes it possible to place the sensing position at a  well defined place. The place is defined by the connection of the Terminal to ConductingEquipment.")

#Terminal_RegulatingControl_GraphEdge = GraphEdge(
#    edge_for=[Terminal],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=RegulatingControl",
#    tooltip="The terminal is regulated by a control.The terminal is regulated by a control.")

#BaseVoltage_ConductingEquipment_GraphEdge = GraphEdge(
#    edge_for=[BaseVoltage],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConductingEquipment",
#    tooltip="Use association to ConductingEquipment only when there is no VoltageLevel container used.Use association to ConductingEquipment only when there is no VoltageLevel container used.")

#BaseVoltage_VoltageLevel_GraphEdge = GraphEdge(
#    edge_for=[BaseVoltage],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=VoltageLevel",
#    tooltip="The VoltageLevels having this BaseVoltage.The VoltageLevels having this BaseVoltage.")

#RegularIntervalSchedule_TimePoints_GraphEdge = GraphEdge(
#    edge_for=[RegularIntervalSchedule],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TimePoints",
#    tooltip="The point data values that define a curveThe point data values that define a curve")

#ConnectivityNodeContainer_ConnectivityNodes_GraphEdge = GraphEdge(
#    edge_for=[ConnectivityNodeContainer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ConnectivityNodes",
#    tooltip="Connectivity nodes contained by this container.Connectivity nodes contained by this container.")

#Unit_Measurements_GraphEdge = GraphEdge(
#    edge_for=[Unit],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Measurements",
#    tooltip="The Measurements having the UnitThe Measurements having the Unit")

#EquipmentContainer_Contains_Equipments_GraphEdge = GraphEdge(
#    edge_for=[EquipmentContainer],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Equipments",
#    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

#VoltageLevel_Contains_Bays_GraphEdge = GraphEdge(
#    edge_for=[VoltageLevel],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Bays",
#    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

#SubGeographicalRegion_Lines_GraphEdge = GraphEdge(
#    edge_for=[SubGeographicalRegion],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Lines",
#    tooltip="A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.")

#SubGeographicalRegion_Substations_GraphEdge = GraphEdge(
#    edge_for=[SubGeographicalRegion],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Substations",
#    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

#Equipment_OperationalLimitSet_GraphEdge = GraphEdge(
#    edge_for=[Equipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=OperationalLimitSet",
#    tooltip="The equipment limit sets associated with the equipment.The equipment limit sets associated with the equipment.")

#Substation_Contains_VoltageLevels_GraphEdge = GraphEdge(
#    edge_for=[Substation],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_VoltageLevels",
#    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

#Curve_CurveScheduleDatas_GraphEdge = GraphEdge(
#    edge_for=[Curve],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=CurveScheduleDatas",
#    tooltip="The point data values that define a curveThe point data values that define a curve")

#PowerSystemResource_Contains_Measurements_GraphEdge = GraphEdge(
#    edge_for=[PowerSystemResource],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Contains_Measurements",
#    tooltip="The Measurements that are included in the naming hierarchy where the PSR is the containing objectThe Measurements that are included in the naming hierarchy where the PSR is the containing object")

#GeographicalRegion_Regions_GraphEdge = GraphEdge(
#    edge_for=[GeographicalRegion],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Regions",
#    tooltip="The association is used in the naming hierarchy.The association is used in the naming hierarchy.")

#ConductingEquipment_Terminals_GraphEdge = GraphEdge(
#    edge_for=[ConductingEquipment],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Terminals",
#    tooltip="ConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodesConductingEquipment has 1 or 2 terminals that may be connected to other ConductingEquipment terminals via ConnectivityNodes")

#ControlArea_ControlAreaGeneratingUnit_GraphEdge = GraphEdge(
#    edge_for=[ControlArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=ControlAreaGeneratingUnit",
#    tooltip="The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.")

#ControlArea_TieFlow_GraphEdge = GraphEdge(
#    edge_for=[ControlArea],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=TieFlow",
#    tooltip="The tie flows associated with the control area.The tie flows associated with the control area.")

#ConnectivityNode_Terminals_GraphEdge = GraphEdge(
#    edge_for=[ConnectivityNode],
#    head_nodes=[],
#    tail_nodes=[],
#    head_label="=Terminals",
#    tooltip="Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.Terminals interconnect with zero impedance at a node.  Measurements on a node apply to all of its terminals.")

#------------------------------------------------------------------------------
#  Graph node list:
#------------------------------------------------------------------------------


graph_nodes = [
    Element_GraphNode,
    CommonPowerSystemModel_GraphNode,
    IEC61970CIMVersion_GraphNode,
    Season_GraphNode,
    IdentifiedObject_GraphNode,
    Terminal_GraphNode,
    BaseVoltage_GraphNode,
    Unit_GraphNode,
    SubGeographicalRegion_GraphNode,
    RegularTimePoint_GraphNode,
    Curve_GraphNode,
    PowerSystemResource_GraphNode,
    BasicIntervalSchedule_GraphNode,
    CurveData_GraphNode,
    GeographicalRegion_GraphNode,
    ControlArea_GraphNode,
    TieFlow_GraphNode,
    ControlAreaGeneratingUnit_GraphNode,
    ConnectivityNode_GraphNode,
    GrossToNetActivePowerCurve_GraphNode,
    HydroGeneratingUnit_GraphNode,
    ThermalGeneratingUnit_GraphNode,
    OperationalLimit_GraphNode,
    OperationalLimitSet_GraphNode,
    ActivePowerLimit_GraphNode,
    ApparentPowerLimit_GraphNode,
    VoltageLimit_GraphNode,
    CurrentLimit_GraphNode,
    RegulatingControl_GraphNode,
    ReactiveCapabilityCurve_GraphNode,
    TapChanger_GraphNode,
    Measurement_GraphNode,
    MeasurementValue_GraphNode,
    MeasurementValueSource_GraphNode,
    Analog_GraphNode,
    AnalogValue_GraphNode,
    MeasurementType_GraphNode,
    Discrete_GraphNode,
    LimitSet_GraphNode,
    DayType_GraphNode,
    LoadGroup_GraphNode,
    EnergyArea_GraphNode,
    ConformLoadGroup_GraphNode,
    LoadArea_GraphNode,
    SubLoadArea_GraphNode,
    LoadResponseCharacteristic_GraphNode,
    RegularIntervalSchedule_GraphNode,
    ConnectivityNodeContainer_GraphNode,
    EquipmentContainer_GraphNode,
    VoltageLevel_GraphNode,
    Bay_GraphNode,
    Equipment_GraphNode,
    Substation_GraphNode,
    ConductingEquipment_GraphNode,
    GeneratingUnit_GraphNode,
    PowerTransformer_GraphNode,
    BusbarSection_GraphNode,
    RegulatingCondEq_GraphNode,
    EnergyConsumer_GraphNode,
    TransformerWinding_GraphNode,
    RegulationSchedule_GraphNode,
    Switch_GraphNode,
    Conductor_GraphNode,
    Line_GraphNode,
    StaticVarCompensator_GraphNode,
    SeriesCompensator_GraphNode,
    Breaker_GraphNode,
    DiscreteValue_GraphNode,
    NonConformLoadGroup_GraphNode,
    CustomerLoad_GraphNode,
    NonConformLoad_GraphNode,
    Load_GraphNode,
    StationSupply_GraphNode,
    SeasonDayTypeSchedule_GraphNode,
    NonConformLoadSchedule_GraphNode,
    InductionMotorLoad_GraphNode,
    ConformLoad_GraphNode,
    EquivalentNetwork_GraphNode,
    EquivalentEquipment_GraphNode,
    EquivalentBranch_GraphNode,
    Disconnector_GraphNode,
    SynchronousMachine_GraphNode,
    ShuntCompensator_GraphNode,
    LoadBreakSwitch_GraphNode,
    ACLineSegment_GraphNode,
    ConformLoadSchedule_GraphNode,
    EquivalentShunt_GraphNode,
]
graph_nodes.reverse()

#graph_edges = [
#    CommonPowerSystemModel_Elements_GraphEdge,
#    Season_SeasonDayTypeSchedules_GraphEdge,
#    Terminal_Measurements_GraphEdge,
#    Terminal_RegulatingControl_GraphEdge,
#    BaseVoltage_ConductingEquipment_GraphEdge,
#    BaseVoltage_VoltageLevel_GraphEdge,
#    Unit_Measurements_GraphEdge,
#    SubGeographicalRegion_Lines_GraphEdge,
#    SubGeographicalRegion_Substations_GraphEdge,
#    Curve_CurveScheduleDatas_GraphEdge,
#    PowerSystemResource_Contains_Measurements_GraphEdge,
#    GeographicalRegion_Regions_GraphEdge,
#    ControlArea_ControlAreaGeneratingUnit_GraphEdge,
#    ControlArea_TieFlow_GraphEdge,
#    ConnectivityNode_Terminals_GraphEdge,
#    OperationalLimitSet_OperationalLimitValue_GraphEdge,
#    RegulatingControl_TapChanger_GraphEdge,
#    RegulatingControl_RegulatingCondEq_GraphEdge,
#    ReactiveCapabilityCurve_InitiallyUsedBySynchronousMachine_GraphEdge,
#    MeasurementValueSource_MeasurementValues_GraphEdge,
#    Analog_Contain_MeasurementValues_GraphEdge,
#    MeasurementType_Measurements_GraphEdge,
#    Discrete_Contain_MeasurementValues_GraphEdge,
#    DayType_SeasonDayTypeSchedules_GraphEdge,
#    ConformLoadGroup_EnergyConsumers_GraphEdge,
#    ConformLoadGroup_ConformLoadSchedules_GraphEdge,
#    LoadArea_SubLoadAreas_GraphEdge,
#    SubLoadArea_LoadGroups_GraphEdge,
#    LoadResponseCharacteristic_EnergyConsumer_GraphEdge,
#    RegularIntervalSchedule_TimePoints_GraphEdge,
#    ConnectivityNodeContainer_ConnectivityNodes_GraphEdge,
#    EquipmentContainer_Contains_Equipments_GraphEdge,
#    VoltageLevel_Contains_Bays_GraphEdge,
#    Equipment_OperationalLimitSet_GraphEdge,
#    Substation_Contains_VoltageLevels_GraphEdge,
#    ConductingEquipment_Terminals_GraphEdge,
#    GeneratingUnit_Contains_SynchronousMachines_GraphEdge,
#    GeneratingUnit_GrossToNetActivePowerCurves_GraphEdge,
#    GeneratingUnit_ControlAreaGeneratingUnit_GraphEdge,
#    PowerTransformer_Contains_TransformerWindings_GraphEdge,
#    TransformerWinding_TapChangers_GraphEdge,
#    RegulationSchedule_RegulatingControl_GraphEdge,
#    NonConformLoadGroup_NonConformLoadSchedules_GraphEdge,
#    NonConformLoadGroup_EnergyConsumers_GraphEdge,
#    EquivalentNetwork_EquivalentEquipments_GraphEdge,
#]
#graph_edges.reverse()

#------------------------------------------------------------------------------
#  CPSM Graph Editor:
#------------------------------------------------------------------------------

CPSMGraphEditor = GraphEditor(nodes=graph_nodes)

# EOF -------------------------------------------------------------------------
