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

"""This package contains the information classes that extend IEC61970::Wires package with power system resources required for distribution network modelling, including unbalanced networks.
"""

ns_prefix = "cimWiresExt"
ns_uri = "http://iec.ch/TC57/CIM-generic#WiresExt"

from CIM14v13.IEC61968.WiresExt.PerLengthPhaseImpedance import PerLengthPhaseImpedance
from CIM14v13.IEC61968.WiresExt.DistributionTransformerWinding import DistributionTransformerWinding
from CIM14v13.IEC61968.WiresExt.WindingPiImpedance import WindingPiImpedance
from CIM14v13.IEC61968.WiresExt.DistributionTransformer import DistributionTransformer
from CIM14v13.IEC61968.WiresExt.DistributionLineSegment import DistributionLineSegment
from CIM14v13.IEC61968.WiresExt.PerLengthSequenceImpedance import PerLengthSequenceImpedance
from CIM14v13.IEC61968.WiresExt.TransformerBank import TransformerBank
from CIM14v13.IEC61968.WiresExt.DistributionTapChanger import DistributionTapChanger
from CIM14v13.IEC61968.WiresExt.PhaseImpedanceData import PhaseImpedanceData
