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

"""This package contains the information classes that extend IEC61970::Wires package with power system resources required for distribution network modelling, including unbalanced networks.
"""

from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.DistributionTransformerWinding import DistributionTransformerWinding
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.DistributionLineSegment import DistributionLineSegment
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.WindingPiImpedance import WindingPiImpedance
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.DistributionTapChanger import DistributionTapChanger
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.PerLengthSequenceImpedance import PerLengthSequenceImpedance
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.TransformerBank import TransformerBank
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.PerLengthPhaseImpedance import PerLengthPhaseImpedance
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.DistributionTransformer import DistributionTransformer
from CIM14.CDPSM.Unbalanced.IEC61968.WiresExt.PhaseImpedanceData import PhaseImpedanceData

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14?profile=http://iec.ch/TC57/2007/profile#WiresExt"
nsPrefix = "cimWiresExt"

