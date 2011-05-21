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

"""The IEC 61968 subpackages of the CIM are developed, standardized and maintained by IEC TC57 Working Group 14: interfaces for distribution management (WG14). Currently, normative parts of the model support the needs of information exchange defined in IEC 61968-9 and in IEC 61968-13.
"""

from CIM15.CDPSM.Balanced.Element import Element

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-13/CDPSM/Balanced"
nsPrefix = "balanced"

packageMap = {
    "Element": "CIM15.CDPSM.Balanced",
    "PhaseTapChangerLinear": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "EnergyConsumer": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "ACLineSegment": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "TransformerCoreAdmittance": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "SynchronousMachine": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "PowerTransformerEnd": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "PhaseTapChangerAsymetrical": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "TransformerMeshImpedance": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "ProtectedSwitch": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "PhaseTapChangerNonLinear": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "RatioTapChanger": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "SeriesCompensator": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "PhaseTapChanger": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "TransformerTankEnd": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "DCLineSegment": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "TapChanger": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "PhaseTapChangerSymetrical": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "TransformerStarImpedance": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "PowerTransformer": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "TransformerEnd": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "EnergySource": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "ShuntCompensator": "CIM15.CDPSM.Balanced.IEC61970.Wires",
    "LoadResponseCharacteristic": "CIM15.CDPSM.Balanced.IEC61970.LoadModel",
    "GeneratingUnit": "CIM15.CDPSM.Balanced.IEC61970.Generation.Production",
    "NameType": "CIM15.CDPSM.Balanced.IEC61970.Core",
    "IdentifiedObject": "CIM15.CDPSM.Balanced.IEC61970.Core",
    "Name": "CIM15.CDPSM.Balanced.IEC61970.Core",
}


class Resistance(float):
    """Resistance (real part of impedance).
    """
    pass

class Reactance(float):
    """Reactance (imaginary part of impedance), at rated frequency.
    """
    pass

class PerCent(float):
    """Normally 0 - 100 on a defined base
    """
    pass

class Voltage(float):
    """Electrical voltage.
    """
    pass

class Conductance(float):
    """Factor by which voltage must be multiplied to give corresponding power lost from a circuit. Real part of admittance.
    """
    pass

class AngleDegrees(float):
    """Measurement of angle in degrees
    """
    pass

class VoltagePerReactivePower(float):
    """Voltage variation with reactive power
    """
    pass

class AngleRadians(float):
    """Phase angle in radians
    """
    pass

class ActivePower(float):
    """Product of RMS value of the voltage and the RMS value of the in-phase component of the current
    """
    pass

class ApparentPower(float):
    """Product of the RMS value of the voltage and the RMS value of the current
    """
    pass

class CurrentFlow(float):
    """Electrical current (positive flow is out of the ConductingEquipment into the ConnectivityNode)
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
