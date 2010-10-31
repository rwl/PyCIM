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


""" Defines a map of class names to their module.
"""

cdpsm_pkg_map = {
    "Element": "cdpsm",
    "Model": "cdpsm",
    "DistributionTransformerWinding": "cdpsm.iec61968.wires_ext",
    "DistributionLineSegment": "cdpsm.iec61968.wires_ext",
    "WindingPiImpedance": "cdpsm.iec61968.wires_ext",
    "DistributionTapChanger": "cdpsm.iec61968.wires_ext",
    "PerLengthSequenceImpedance": "cdpsm.iec61968.wires_ext",
    "TransformerBank": "cdpsm.iec61968.wires_ext",
    "PerLengthPhaseImpedance": "cdpsm.iec61968.wires_ext",
    "DistributionTransformer": "cdpsm.iec61968.wires_ext",
    "PhaseImpedanceData": "cdpsm.iec61968.wires_ext",
    "TransformerInfo": "cdpsm.iec61968.asset_models",
    "ToWindingSpec": "cdpsm.iec61968.asset_models",
    "WireArrangement": "cdpsm.iec61968.asset_models",
    "CableInfo": "cdpsm.iec61968.asset_models",
    "OpenCircuitTest": "cdpsm.iec61968.asset_models",
    "ConcentricNeutralCableInfo": "cdpsm.iec61968.asset_models",
    "ConductorInfo": "cdpsm.iec61968.asset_models",
    "DistributionWindingTest": "cdpsm.iec61968.asset_models",
    "WireType": "cdpsm.iec61968.asset_models",
    "WindingInfo": "cdpsm.iec61968.asset_models",
    "OverheadConductorInfo": "cdpsm.iec61968.asset_models",
    "TapeShieldCableInfo": "cdpsm.iec61968.asset_models",
    "ShortCircuitTest": "cdpsm.iec61968.asset_models",
    "GeoLocation": "cdpsm.iec61968.common",
    "Location": "cdpsm.iec61968.common",
    "PositionPoint": "cdpsm.iec61968.common",
    "IEC61970CIMVersion": "cdpsm.iec61970",
    "BusbarSection": "cdpsm.iec61970.wires",
    "LoadBreakSwitch": "cdpsm.iec61970.wires",
    "TapChanger": "cdpsm.iec61970.wires",
    "Fuse": "cdpsm.iec61970.wires",
    "Junction": "cdpsm.iec61970.wires",
    "ACLineSegment": "cdpsm.iec61970.wires",
    "Disconnector": "cdpsm.iec61970.wires",
    "EnergySource": "cdpsm.iec61970.wires",
    "SynchronousMachine": "cdpsm.iec61970.wires",
    "RatioTapChanger": "cdpsm.iec61970.wires",
    "EnergyConsumer": "cdpsm.iec61970.wires",
    "Switch": "cdpsm.iec61970.wires",
    "Line": "cdpsm.iec61970.wires",
    "ShuntCompensator": "cdpsm.iec61970.wires",
    "Breaker": "cdpsm.iec61970.wires",
    "Conductor": "cdpsm.iec61970.wires",
    "ConnectivityNodeContainer": "cdpsm.iec61970.core",
    "VoltageLevel": "cdpsm.iec61970.core",
    "Bay": "cdpsm.iec61970.core",
    "Equipment": "cdpsm.iec61970.core",
    "BaseVoltage": "cdpsm.iec61970.core",
    "PSRType": "cdpsm.iec61970.core",
    "EquipmentContainer": "cdpsm.iec61970.core",
    "IdentifiedObject": "cdpsm.iec61970.core",
    "Substation": "cdpsm.iec61970.core",
    "ConductingEquipment": "cdpsm.iec61970.core",
    "SubGeographicalRegion": "cdpsm.iec61970.core",
    "Terminal": "cdpsm.iec61970.core",
    "GeographicalRegion": "cdpsm.iec61970.core",
    "PowerSystemResource": "cdpsm.iec61970.core",
    "GeneratingUnit": "cdpsm.iec61970.generation.production",
    "LoadResponseCharacteristic": "cdpsm.iec61970.load_model",
    "SvTapStep": "cdpsm.iec61970.state_variables",
    "ConnectivityNode": "cdpsm.iec61970.topology",
}
