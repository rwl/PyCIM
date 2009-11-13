#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard Lincoln
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANDABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Defines a map of class names to their module.
"""

cpsm_pkg_map = {
    "Element": "cpsm.element",
    "Model": "cpsm.model",
    "IEC61970CIMVersion": "cpsm.iec61970_cimversion",
    "GrossToNetActivePowerCurve": "cpsm.generation.production.gross_to_net_active_power_curve",
    "HydroGeneratingUnit": "cpsm.generation.production.hydro_generating_unit",
    "ThermalGeneratingUnit": "cpsm.generation.production.thermal_generating_unit",
    "GeneratingUnit": "cpsm.generation.production.generating_unit",
    "OperationalLimit": "cpsm.operational_limits.operational_limit",
    "OperationalLimitSet": "cpsm.operational_limits.operational_limit_set",
    "ActivePowerLimit": "cpsm.operational_limits.active_power_limit",
    "ApparentPowerLimit": "cpsm.operational_limits.apparent_power_limit",
    "VoltageLimit": "cpsm.operational_limits.voltage_limit",
    "CurrentLimit": "cpsm.operational_limits.current_limit",
    "PowerTransformer": "cpsm.wires.power_transformer",
    "Disconnector": "cpsm.wires.disconnector",
    "SynchronousMachine": "cpsm.wires.synchronous_machine",
    "BusbarSection": "cpsm.wires.busbar_section",
    "ShuntCompensator": "cpsm.wires.shunt_compensator",
    "LoadBreakSwitch": "cpsm.wires.load_break_switch",
    "RegulatingCondEq": "cpsm.wires.regulating_cond_eq",
    "EnergyConsumer": "cpsm.wires.energy_consumer",
    "TransformerWinding": "cpsm.wires.transformer_winding",
    "RegulatingControl": "cpsm.wires.regulating_control",
    "RegulationSchedule": "cpsm.wires.regulation_schedule",
    "ACLineSegment": "cpsm.wires.acline_segment",
    "Switch": "cpsm.wires.switch",
    "Conductor": "cpsm.wires.conductor",
    "ReactiveCapabilityCurve": "cpsm.wires.reactive_capability_curve",
    "TapChanger": "cpsm.wires.tap_changer",
    "Line": "cpsm.wires.line",
    "StaticVarCompensator": "cpsm.wires.static_var_compensator",
    "SeriesCompensator": "cpsm.wires.series_compensator",
    "Breaker": "cpsm.wires.breaker",
    "DiscreteValue": "cpsm.meas.discrete_value",
    "Measurement": "cpsm.meas.measurement",
    "MeasurementValue": "cpsm.meas.measurement_value",
    "MeasurementValueSource": "cpsm.meas.measurement_value_source",
    "Analog": "cpsm.meas.analog",
    "AnalogValue": "cpsm.meas.analog_value",
    "MeasurementType": "cpsm.meas.measurement_type",
    "Discrete": "cpsm.meas.discrete",
    "LimitSet": "cpsm.meas.limit_set",
    "NonConformLoadGroup": "cpsm.load_model.non_conform_load_group",
    "ConformLoadSchedule": "cpsm.load_model.conform_load_schedule",
    "CustomerLoad": "cpsm.load_model.customer_load",
    "NonConformLoad": "cpsm.load_model.non_conform_load",
    "DayType": "cpsm.load_model.day_type",
    "Season": "cpsm.load_model.season",
    "Load": "cpsm.load_model.load",
    "StationSupply": "cpsm.load_model.station_supply",
    "SeasonDayTypeSchedule": "cpsm.load_model.season_day_type_schedule",
    "LoadGroup": "cpsm.load_model.load_group",
    "EnergyArea": "cpsm.load_model.energy_area",
    "ConformLoadGroup": "cpsm.load_model.conform_load_group",
    "LoadArea": "cpsm.load_model.load_area",
    "SubLoadArea": "cpsm.load_model.sub_load_area",
    "LoadResponseCharacteristic": "cpsm.load_model.load_response_characteristic",
    "NonConformLoadSchedule": "cpsm.load_model.non_conform_load_schedule",
    "InductionMotorLoad": "cpsm.load_model.induction_motor_load",
    "ConformLoad": "cpsm.load_model.conform_load",
    "EquivalentNetwork": "cpsm.equivalents.equivalent_network",
    "EquivalentShunt": "cpsm.equivalents.equivalent_shunt",
    "EquivalentEquipment": "cpsm.equivalents.equivalent_equipment",
    "EquivalentBranch": "cpsm.equivalents.equivalent_branch",
    "IdentifiedObject": "cpsm.core.identified_object",
    "Terminal": "cpsm.core.terminal",
    "BaseVoltage": "cpsm.core.base_voltage",
    "RegularIntervalSchedule": "cpsm.core.regular_interval_schedule",
    "ConnectivityNodeContainer": "cpsm.core.connectivity_node_container",
    "Unit": "cpsm.core.unit",
    "EquipmentContainer": "cpsm.core.equipment_container",
    "VoltageLevel": "cpsm.core.voltage_level",
    "Bay": "cpsm.core.bay",
    "SubGeographicalRegion": "cpsm.core.sub_geographical_region",
    "RegularTimePoint": "cpsm.core.regular_time_point",
    "Equipment": "cpsm.core.equipment",
    "Substation": "cpsm.core.substation",
    "Curve": "cpsm.core.curve",
    "PowerSystemResource": "cpsm.core.power_system_resource",
    "BasicIntervalSchedule": "cpsm.core.basic_interval_schedule",
    "CurveData": "cpsm.core.curve_data",
    "GeographicalRegion": "cpsm.core.geographical_region",
    "ConductingEquipment": "cpsm.core.conducting_equipment",
    "ControlArea": "cpsm.control_area.control_area",
    "TieFlow": "cpsm.control_area.tie_flow",
    "ControlAreaGeneratingUnit": "cpsm.control_area.control_area_generating_unit",
    "ConnectivityNode": "cpsm.topology.connectivity_node",
}

# EOF -------------------------------------------------------------------------
