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

from CDPSM.Connectivity.IEC61970.Wires.Fuse import Fuse
from CDPSM.Connectivity.IEC61970.Wires.EnergyConsumer import EnergyConsumer
from CDPSM.Connectivity.IEC61970.Wires.Switch import Switch
from CDPSM.Connectivity.IEC61970.Wires.Disconnector import Disconnector
from CDPSM.Connectivity.IEC61970.Wires.ACLineSegment import ACLineSegment
from CDPSM.Connectivity.IEC61970.Wires.SynchronousMachine import SynchronousMachine
from CDPSM.Connectivity.IEC61970.Wires.BusbarSection import BusbarSection
from CDPSM.Connectivity.IEC61970.Wires.LoadBreakSwitch import LoadBreakSwitch
from CDPSM.Connectivity.IEC61970.Wires.TransformerTank import TransformerTank
from CDPSM.Connectivity.IEC61970.Wires.GroundDisconnector import GroundDisconnector
from CDPSM.Connectivity.IEC61970.Wires.PowerTransformerEnd import PowerTransformerEnd
from CDPSM.Connectivity.IEC61970.Wires.Junction import Junction
from CDPSM.Connectivity.IEC61970.Wires.SeriesCompensator import SeriesCompensator
from CDPSM.Connectivity.IEC61970.Wires.Breaker import Breaker
from CDPSM.Connectivity.IEC61970.Wires.TransformerTankEnd import TransformerTankEnd
from CDPSM.Connectivity.IEC61970.Wires.Sectionaliser import Sectionaliser
from CDPSM.Connectivity.IEC61970.Wires.DCLineSegment import DCLineSegment
from CDPSM.Connectivity.IEC61970.Wires.Line import Line
from CDPSM.Connectivity.IEC61970.Wires.Conductor import Conductor
from CDPSM.Connectivity.IEC61970.Wires.PowerTransformer import PowerTransformer
from CDPSM.Connectivity.IEC61970.Wires.Ground import Ground
from CDPSM.Connectivity.IEC61970.Wires.TransformerEnd import TransformerEnd
from CDPSM.Connectivity.IEC61970.Wires.ShuntCompensator import ShuntCompensator
from CDPSM.Connectivity.IEC61970.Wires.EnergySource import EnergySource
from CDPSM.Connectivity.IEC61970.Wires.Jumper import Jumper

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-13/CDPSM/Connectivity#Wires"
nsPrefix = "cimWires"

