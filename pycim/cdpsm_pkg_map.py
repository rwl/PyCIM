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
