# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

pkg_map = {
    "Element": "entsoe",
    "IEC61970CIMVersion": "entsoe",
    "Model": "entsoe",
    "SvVoltage": "entsoe.state_variables",
    "SvShuntCompensatorSections": "entsoe.state_variables",
    "StateVariable": "entsoe.state_variables",
    "SvTapStep": "entsoe.state_variables",
    "SvPowerFlow": "entsoe.state_variables",
    "Curve": "entsoe.core",
    "ConnectivityNodeContainer": "entsoe.core",
    "VoltageLevel": "entsoe.core",
    "Equipment": "entsoe.core",
    "BaseVoltage": "entsoe.core",
    "EquipmentContainer": "entsoe.core",
    "IdentifiedObject": "entsoe.core",
    "Substation": "entsoe.core",
    "ConductingEquipment": "entsoe.core",
    "SubGeographicalRegion": "entsoe.core",
    "Terminal": "entsoe.core",
    "GeographicalRegion": "entsoe.core",
    "CurveData": "entsoe.core",
    "ControlArea": "entsoe.control_area",
    "ControlAreaGeneratingUnit": "entsoe.control_area",
    "TieFlow": "entsoe.control_area",
    "WindGeneratingUnit": "entsoe.generation.production",
    "GeneratingUnit": "entsoe.generation.production",
    "FossilFuel": "entsoe.generation.production",
    "NuclearGeneratingUnit": "entsoe.generation.production",
    "HydroGeneratingUnit": "entsoe.generation.production",
    "ThermalGeneratingUnit": "entsoe.generation.production",
    "HydroPump": "entsoe.generation.production",
    "LoadResponseCharacteristic": "entsoe.load_model",
    "TopologicalNode": "entsoe.topology",
    "TopologicalIsland": "entsoe.topology",
    "EquivalentEquipment": "entsoe.equivalents",
    "BusbarSection": "entsoe.wires",
    "TapChanger": "entsoe.wires",
    "TransformerWinding": "entsoe.wires",
    "RegulatingControl": "entsoe.wires",
    "ReactiveCapabilityCurve": "entsoe.wires",
    "ACLineSegment": "entsoe.wires",
    "PhaseTapChanger": "entsoe.wires",
    "MutualCoupling": "entsoe.wires",
    "SynchronousMachine": "entsoe.wires",
    "RatioTapChanger": "entsoe.wires",
    "PowerTransformer": "entsoe.wires",
    "EnergyConsumer": "entsoe.wires",
    "Switch": "entsoe.wires",
    "RegulatingCondEq": "entsoe.wires",
    "VoltageControlZone": "entsoe.wires",
    "Line": "entsoe.wires",
    "ShuntCompensator": "entsoe.wires",
    "Conductor": "entsoe.wires",
    "CurrentLimit": "entsoe.operational_limits",
    "VoltageLimit": "entsoe.operational_limits",
    "OperationalLimit": "entsoe.operational_limits",
    "OperationalLimitSet": "entsoe.operational_limits",
    "OperationalLimitType": "entsoe.operational_limits",
}
