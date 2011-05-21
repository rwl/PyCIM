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

"""An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

from CIM15.CDPSM.Balanced.IEC61970.Wires.PhaseTapChangerLinear import PhaseTapChangerLinear
from CIM15.CDPSM.Balanced.IEC61970.Wires.EnergyConsumer import EnergyConsumer
from CIM15.CDPSM.Balanced.IEC61970.Wires.ACLineSegment import ACLineSegment
from CIM15.CDPSM.Balanced.IEC61970.Wires.TransformerCoreAdmittance import TransformerCoreAdmittance
from CIM15.CDPSM.Balanced.IEC61970.Wires.SynchronousMachine import SynchronousMachine
from CIM15.CDPSM.Balanced.IEC61970.Wires.PowerTransformerEnd import PowerTransformerEnd
from CIM15.CDPSM.Balanced.IEC61970.Wires.PhaseTapChangerAsymetrical import PhaseTapChangerAsymetrical
from CIM15.CDPSM.Balanced.IEC61970.Wires.TransformerMeshImpedance import TransformerMeshImpedance
from CIM15.CDPSM.Balanced.IEC61970.Wires.ProtectedSwitch import ProtectedSwitch
from CIM15.CDPSM.Balanced.IEC61970.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear
from CIM15.CDPSM.Balanced.IEC61970.Wires.RatioTapChanger import RatioTapChanger
from CIM15.CDPSM.Balanced.IEC61970.Wires.SeriesCompensator import SeriesCompensator
from CIM15.CDPSM.Balanced.IEC61970.Wires.PhaseTapChanger import PhaseTapChanger
from CIM15.CDPSM.Balanced.IEC61970.Wires.TransformerTankEnd import TransformerTankEnd
from CIM15.CDPSM.Balanced.IEC61970.Wires.DCLineSegment import DCLineSegment
from CIM15.CDPSM.Balanced.IEC61970.Wires.TapChanger import TapChanger
from CIM15.CDPSM.Balanced.IEC61970.Wires.PhaseTapChangerSymetrical import PhaseTapChangerSymetrical
from CIM15.CDPSM.Balanced.IEC61970.Wires.TransformerStarImpedance import TransformerStarImpedance
from CIM15.CDPSM.Balanced.IEC61970.Wires.PowerTransformer import PowerTransformer
from CIM15.CDPSM.Balanced.IEC61970.Wires.TransformerEnd import TransformerEnd
from CIM15.CDPSM.Balanced.IEC61970.Wires.EnergySource import EnergySource
from CIM15.CDPSM.Balanced.IEC61970.Wires.ShuntCompensator import ShuntCompensator

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-13/CDPSM/Balanced#Wires"
nsPrefix = "cimWires"


class WindingType(str):
    """Values are: tertiary, primary, secondary, quaternary
    """
    pass

class SynchronousMachineType(str):
    """Values are: condenser, generator_or_condenser, generator
    """
    pass

class PhaseTapChangerKind(str):
    """Values are: unknown, asymmetrical, symmetrical
    """
    pass

class SynchronousMachineOperatingMode(str):
    """Values are: condenser, generator
    """
    pass

class TransformerControlMode(str):
    """Values are: reactive, volt
    """
    pass

class WindingConnection(str):
    """Values are: Z, A, Yn, Y, Zn, D, I
    """
    pass

class TapChangerKind(str):
    """Values are: voltageAndPhaseControl, phaseControl, fixed, voltageControl
    """
    pass
