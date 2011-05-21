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

from CIM14.IEC61970.Wires.PowerTransformer import PowerTransformer
from CIM14.IEC61970.Wires.RegulatingCondEq import RegulatingCondEq
from CIM14.IEC61970.Wires.FrequencyConverter import FrequencyConverter
from CIM14.IEC61970.Wires.ShuntCompensator import ShuntCompensator
from CIM14.IEC61970.Wires.HeatExchanger import HeatExchanger
from CIM14.IEC61970.Wires.RegulatingControl import RegulatingControl
from CIM14.IEC61970.Wires.ReactiveCapabilityCurve import ReactiveCapabilityCurve
from CIM14.IEC61970.Wires.Line import Line
from CIM14.IEC61970.Wires.Connector import Connector
from CIM14.IEC61970.Wires.Junction import Junction
from CIM14.IEC61970.Wires.Ground import Ground
from CIM14.IEC61970.Wires.Conductor import Conductor
from CIM14.IEC61970.Wires.TransformerWinding import TransformerWinding
from CIM14.IEC61970.Wires.SynchronousMachine import SynchronousMachine
from CIM14.IEC61970.Wires.EnergyConsumer import EnergyConsumer
from CIM14.IEC61970.Wires.TapChanger import TapChanger
from CIM14.IEC61970.Wires.RatioTapChanger import RatioTapChanger
from CIM14.IEC61970.Wires.Switch import Switch
from CIM14.IEC61970.Wires.ProtectedSwitch import ProtectedSwitch
from CIM14.IEC61970.Wires.LoadBreakSwitch import LoadBreakSwitch
from CIM14.IEC61970.Wires.ACLineSegment import ACLineSegment
from CIM14.IEC61970.Wires.Plant import Plant
from CIM14.IEC61970.Wires.RegulationSchedule import RegulationSchedule
from CIM14.IEC61970.Wires.WindingTest import WindingTest
from CIM14.IEC61970.Wires.PhaseVariationCurve import PhaseVariationCurve
from CIM14.IEC61970.Wires.MutualCoupling import MutualCoupling
from CIM14.IEC61970.Wires.Disconnector import Disconnector
from CIM14.IEC61970.Wires.SeriesCompensator import SeriesCompensator
from CIM14.IEC61970.Wires.GroundDisconnector import GroundDisconnector
from CIM14.IEC61970.Wires.RatioVariationCurve import RatioVariationCurve
from CIM14.IEC61970.Wires.Resistor import Resistor
from CIM14.IEC61970.Wires.CompositeSwitch import CompositeSwitch
from CIM14.IEC61970.Wires.PhaseTapChanger import PhaseTapChanger
from CIM14.IEC61970.Wires.RectifierInverter import RectifierInverter
from CIM14.IEC61970.Wires.StaticVarCompensator import StaticVarCompensator
from CIM14.IEC61970.Wires.TapSchedule import TapSchedule
from CIM14.IEC61970.Wires.VoltageControlZone import VoltageControlZone
from CIM14.IEC61970.Wires.EnergySource import EnergySource
from CIM14.IEC61970.Wires.Fuse import Fuse
from CIM14.IEC61970.Wires.Jumper import Jumper
from CIM14.IEC61970.Wires.ImpedanceVariationCurve import ImpedanceVariationCurve
from CIM14.IEC61970.Wires.DCLineSegment import DCLineSegment
from CIM14.IEC61970.Wires.SwitchSchedule import SwitchSchedule
from CIM14.IEC61970.Wires.Breaker import Breaker
from CIM14.IEC61970.Wires.BusbarSection import BusbarSection

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Wires"
nsPrefix = "cimWires"


class PhaseTapChangerKind(str):
    """The construction type of the phase shifting tap changer.
    Values are: asymmetrical, unknown, symmetrical
    """
    pass

class RegulatingControlModeKind(str):
    """The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.
    Values are: fixed, voltage, timeScheduled, currentFlow, admittance, powerFactor, activePower, reactivePower, temperature
    """
    pass

class TapChangerKind(str):
    """Transformer tap changer type. Indicates the capabilities of the tap changer independent of the operating mode.
    Values are: voltageControl, phaseControl, fixed, voltageAndPhaseControl
    """
    pass

class CoolantType(str):
    """Method of cooling a machine.
    Values are: air, hydrogenGas, water
    """
    pass

class SynchronousMachineType(str):
    """Synchronous machine type.
    Values are: generator_or_condenser, generator, condenser
    """
    pass

class WindingType(str):
    """Winding type.
    Values are: primary, quaternary, secondary, tertiary
    """
    pass

class SVCControlMode(str):
    """Static VAr Compensator control mode.
    Values are: reactivePower, off, voltage
    """
    pass

class WindingConnection(str):
    """Winding connection type.
    Values are: Yn, Y, D, I, Z, A, Zn
    """
    pass

class TransformerControlMode(str):
    """Control modes for a transformer.
    Values are: volt, reactive
    """
    pass

class SynchronousMachineOperatingMode(str):
    """Synchronous machine operating mode.
    Values are: condenser, generator
    """
    pass

class CompositeSwitchType(str):
    """An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    """
    pass

class OperatingMode(str):
    """Textual name for an operating mode
    """
    pass
