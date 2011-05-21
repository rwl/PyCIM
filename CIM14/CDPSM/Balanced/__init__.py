# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""
"""

from CIM14.CDPSM.Balanced.Element import Element

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile/CDPSM/Balanced"
nsPrefix = "bal"

packageMap = {
    "Element": "CIM14.CDPSM.Balanced",
    "DistributionTransformerWinding": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "DistributionLineSegment": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "WindingPiImpedance": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "DistributionTapChanger": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "PerLengthSequenceImpedance": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "TransformerBank": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "PerLengthPhaseImpedance": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "DistributionTransformer": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "PhaseImpedanceData": "CIM14.CDPSM.Balanced.IEC61968.WiresExt",
    "TransformerInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "ToWindingSpec": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "WireArrangement": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "CableInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "OpenCircuitTest": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "ConcentricNeutralCableInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "ConductorInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "DistributionWindingTest": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "WireType": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "WindingInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "OverheadConductorInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "TapeShieldCableInfo": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "ShortCircuitTest": "CIM14.CDPSM.Balanced.IEC61968.AssetModels",
    "GeoLocation": "CIM14.CDPSM.Balanced.IEC61968.Common",
    "Location": "CIM14.CDPSM.Balanced.IEC61968.Common",
    "PositionPoint": "CIM14.CDPSM.Balanced.IEC61968.Common",
    "IEC61970CIMVersion": "CIM14.CDPSM.Balanced.IEC61970",
    "BusbarSection": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "LoadBreakSwitch": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "TapChanger": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Fuse": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Junction": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "ACLineSegment": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Disconnector": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "EnergySource": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "SynchronousMachine": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "RatioTapChanger": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "EnergyConsumer": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Switch": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Line": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "ShuntCompensator": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Breaker": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "Conductor": "CIM14.CDPSM.Balanced.IEC61970.Wires",
    "ConnectivityNodeContainer": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "VoltageLevel": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "Bay": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "Equipment": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "BaseVoltage": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "PSRType": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "EquipmentContainer": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "IdentifiedObject": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "Substation": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "ConductingEquipment": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "SubGeographicalRegion": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "Terminal": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "GeographicalRegion": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "PowerSystemResource": "CIM14.CDPSM.Balanced.IEC61970.Core",
    "GeneratingUnit": "CIM14.CDPSM.Balanced.IEC61970.Generation.Production",
    "LoadResponseCharacteristic": "CIM14.CDPSM.Balanced.IEC61970.LoadModel",
    "SvTapStep": "CIM14.CDPSM.Balanced.IEC61970.StateVariables",
    "ConnectivityNode": "CIM14.CDPSM.Balanced.IEC61970.Topology",
}


class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
    """
    pass

class Conductance(float):
    """Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.
    """
    pass

class Impedance(float):
    """Ratio of voltage to current.
    """
    pass

class Susceptance(float):
    """Imaginary part of admittance.
    """
    pass

class ReactivePower(float):
    """Product of RMS value of the voltage and the RMS value of the quadrature component of the current.
    """
    pass

class CurrentFlow(float):
    """Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)
    """
    pass

class AngleDegrees(float):
    """Measurement of angle in degrees
    """
    pass

class ActivePower(float):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current
    """
    pass

class KWActivePower(float):
    """Active power in kilowatts.
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class Length(float):
    """Unit of length.
    """
    pass

class Resistance(float):
    """Resistance (real part of impedance).
    """
    pass

class AngleRadians(float):
    """Phase angle in radians
    """
    pass

class PerCent(float):
    """Normally 0 - 100 on a defined base
    """
    pass

class Reactance(float):
    """Reactance (imaginary part of impedance), at rated frequency.
    """
    pass

class Seconds(float):
    """Time, in seconds
    """
    pass

class Temperature(float):
    """Value of temperature in degrees Celsius.
    """
    pass

class CIMTime(str):
    pass

class CIMDateTime(str):
    pass

class CIMDuration(str):
    pass

class CIMGYear(str):
    pass

class CIMDate(str):
    pass

class CIMGMonthDay(str):
    pass

class CIMGMonth(str):
    pass

class CIMGDay(str):
    pass

class CIMGYearMonth(str):
    pass
