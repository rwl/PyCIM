# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

"""An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

nsPrefix = "cimWires"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Wires"

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
