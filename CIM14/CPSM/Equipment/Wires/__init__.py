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

from CIM14.CPSM.Equipment.Wires.LoadBreakSwitch import LoadBreakSwitch
from CIM14.CPSM.Equipment.Wires.TransformerWinding import TransformerWinding
from CIM14.CPSM.Equipment.Wires.SwitchSchedule import SwitchSchedule
from CIM14.CPSM.Equipment.Wires.PhaseVariationCurve import PhaseVariationCurve
from CIM14.CPSM.Equipment.Wires.RegulatingControl import RegulatingControl
from CIM14.CPSM.Equipment.Wires.ACLineSegment import ACLineSegment
from CIM14.CPSM.Equipment.Wires.PhaseTapChanger import PhaseTapChanger
from CIM14.CPSM.Equipment.Wires.SeriesCompensator import SeriesCompensator
from CIM14.CPSM.Equipment.Wires.PowerTransformer import PowerTransformer
from CIM14.CPSM.Equipment.Wires.EnergyConsumer import EnergyConsumer
from CIM14.CPSM.Equipment.Wires.Switch import Switch
from CIM14.CPSM.Equipment.Wires.RegulationSchedule import RegulationSchedule
from CIM14.CPSM.Equipment.Wires.ShuntCompensator import ShuntCompensator
from CIM14.CPSM.Equipment.Wires.Conductor import Conductor
from CIM14.CPSM.Equipment.Wires.BusbarSection import BusbarSection
from CIM14.CPSM.Equipment.Wires.TapChanger import TapChanger
from CIM14.CPSM.Equipment.Wires.ImpedanceVariationCurve import ImpedanceVariationCurve
from CIM14.CPSM.Equipment.Wires.ReactiveCapabilityCurve import ReactiveCapabilityCurve
from CIM14.CPSM.Equipment.Wires.Disconnector import Disconnector
from CIM14.CPSM.Equipment.Wires.RatioVariationCurve import RatioVariationCurve
from CIM14.CPSM.Equipment.Wires.TapSchedule import TapSchedule
from CIM14.CPSM.Equipment.Wires.MutualCoupling import MutualCoupling
from CIM14.CPSM.Equipment.Wires.SynchronousMachine import SynchronousMachine
from CIM14.CPSM.Equipment.Wires.RatioTapChanger import RatioTapChanger
from CIM14.CPSM.Equipment.Wires.RegulatingCondEq import RegulatingCondEq
from CIM14.CPSM.Equipment.Wires.Line import Line
from CIM14.CPSM.Equipment.Wires.StaticVarCompensator import StaticVarCompensator
from CIM14.CPSM.Equipment.Wires.Breaker import Breaker

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Wires"
nsPrefix = "cimWires"


class WindingType(str):
    """Values are: tertiary, primary, secondary
    """
    pass

class WindingConnection(str):
    """Values are: I, Yn, Z, Y, A, D, Zn
    """
    pass

class TransformerControlMode(str):
    """Values are: reactive, volt
    """
    pass

class RegulatingControlModeKind(str):
    """Values are: reactivePower, timeScheduled, voltage, activePower, currentFlow, fixed, temperature, powerFactor, admittance
    """
    pass

class SVCControlMode(str):
    """Values are: voltage, reactivePower, off
    """
    pass

class SynchronousMachineType(str):
    """Values are: condenser, generator_or_condenser, generator
    """
    pass

class SynchronousMachineOperatingMode(str):
    """Values are: condenser, generator
    """
    pass

class PhaseTapChangerKind(str):
    """Values are: asymmetrical, symmetrical, unknown
    """
    pass
