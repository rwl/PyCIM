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

from CIM14.CDPSM.Balanced.IEC61970.Wires.BusbarSection import BusbarSection
from CIM14.CDPSM.Balanced.IEC61970.Wires.LoadBreakSwitch import LoadBreakSwitch
from CIM14.CDPSM.Balanced.IEC61970.Wires.TapChanger import TapChanger
from CIM14.CDPSM.Balanced.IEC61970.Wires.Fuse import Fuse
from CIM14.CDPSM.Balanced.IEC61970.Wires.Junction import Junction
from CIM14.CDPSM.Balanced.IEC61970.Wires.ACLineSegment import ACLineSegment
from CIM14.CDPSM.Balanced.IEC61970.Wires.Disconnector import Disconnector
from CIM14.CDPSM.Balanced.IEC61970.Wires.EnergySource import EnergySource
from CIM14.CDPSM.Balanced.IEC61970.Wires.SynchronousMachine import SynchronousMachine
from CIM14.CDPSM.Balanced.IEC61970.Wires.RatioTapChanger import RatioTapChanger
from CIM14.CDPSM.Balanced.IEC61970.Wires.EnergyConsumer import EnergyConsumer
from CIM14.CDPSM.Balanced.IEC61970.Wires.Switch import Switch
from CIM14.CDPSM.Balanced.IEC61970.Wires.Line import Line
from CIM14.CDPSM.Balanced.IEC61970.Wires.ShuntCompensator import ShuntCompensator
from CIM14.CDPSM.Balanced.IEC61970.Wires.Breaker import Breaker
from CIM14.CDPSM.Balanced.IEC61970.Wires.Conductor import Conductor

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#Wires"
nsPrefix = "cimWires"


class TransformerControlMode(str):
    """Values are: reactive, volt
    """
    pass

class WindingConnection(str):
    """Values are: I, Z, Yn, Y, A, D, Zn
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
