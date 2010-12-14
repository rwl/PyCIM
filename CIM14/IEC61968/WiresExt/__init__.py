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

"""Contains only diagrams to be discussed with WG13, for consolidating T&amp;D models.
"""

nsPrefix = "cimWiresExt"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#WiresExt"

from CIM14.IEC61968.WiresExt.TransformerBank import TransformerBank
from CIM14.IEC61968.WiresExt.PhaseImpedanceData import PhaseImpedanceData
from CIM14.IEC61968.WiresExt.DistributionTapChanger import DistributionTapChanger
from CIM14.IEC61968.WiresExt.PerLengthPhaseImpedance import PerLengthPhaseImpedance
from CIM14.IEC61968.WiresExt.PerLengthSequenceImpedance import PerLengthSequenceImpedance
from CIM14.IEC61968.WiresExt.WindingPiImpedance import WindingPiImpedance
from CIM14.IEC61968.WiresExt.DistributionLineSegment import DistributionLineSegment
from CIM14.IEC61968.WiresExt.DistributionTransformer import DistributionTransformer
from CIM14.IEC61968.WiresExt.DistributionTransformerWinding import DistributionTransformerWinding
