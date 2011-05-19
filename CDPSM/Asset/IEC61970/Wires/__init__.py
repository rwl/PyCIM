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

from CDPSM.Asset.IEC61970.Wires.PerLengthSequenceImpedance import PerLengthSequenceImpedance
from CDPSM.Asset.IEC61970.Wires.ACLineSegment import ACLineSegment
from CDPSM.Asset.IEC61970.Wires.TransformerCoreAdmittance import TransformerCoreAdmittance
from CDPSM.Asset.IEC61970.Wires.TransformerTank import TransformerTank
from CDPSM.Asset.IEC61970.Wires.TransformerTankEnd import TransformerTankEnd
from CDPSM.Asset.IEC61970.Wires.TransformerStarImpedance import TransformerStarImpedance
from CDPSM.Asset.IEC61970.Wires.PerLengthPhaseImpedance import PerLengthPhaseImpedance
from CDPSM.Asset.IEC61970.Wires.TransformerEnd import TransformerEnd

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15?profile=http://iec.ch/TC57/2011/iec61968-4/CDPSM/Asset#Wires"
nsPrefix = "cimWires"


class WindingConnection(str):
    """Values are: Z, A, Yn, Y, Zn, D, I
    """
    pass
