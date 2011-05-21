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

"""This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.The Dynamics package isn't officially part of IEC 61970.
"""

from CIM14.IEC61970.Dynamics.BlockConnection import BlockConnection
from CIM14.IEC61970.Dynamics.RotatingMachine import RotatingMachine
from CIM14.IEC61970.Dynamics.AsynchronousMachine import AsynchronousMachine
from CIM14.IEC61970.Dynamics.BlockUsageInputReference import BlockUsageInputReference
from CIM14.IEC61970.Dynamics.MetaBlockConnectable import MetaBlockConnectable
from CIM14.IEC61970.Dynamics.MetaBlockOutput import MetaBlockOutput
from CIM14.IEC61970.Dynamics.MetaBlockConOutput import MetaBlockConOutput
from CIM14.IEC61970.Dynamics.MetaBlock import MetaBlock
from CIM14.IEC61970.Dynamics.MetaBlockInput import MetaBlockInput
from CIM14.IEC61970.Dynamics.SlotReference import SlotReference
from CIM14.IEC61970.Dynamics.MetaBlockInputReference import MetaBlockInputReference
from CIM14.IEC61970.Dynamics.MetaBlockParameter import MetaBlockParameter
from CIM14.IEC61970.Dynamics.MetaBlockParameterReference import MetaBlockParameterReference
from CIM14.IEC61970.Dynamics.CompositeModel import CompositeModel
from CIM14.IEC61970.Dynamics.BlockInputType import BlockInputType
from CIM14.IEC61970.Dynamics.BlockConnectivity import BlockConnectivity
from CIM14.IEC61970.Dynamics.SlotInput import SlotInput
from CIM14.IEC61970.Dynamics.MetaBlockSignal import MetaBlockSignal
from CIM14.IEC61970.Dynamics.MetaBlockStateReference import MetaBlockStateReference
from CIM14.IEC61970.Dynamics.BlockConstant import BlockConstant
from CIM14.IEC61970.Dynamics.SourceModels import SourceModels
from CIM14.IEC61970.Dynamics.SlotConnection import SlotConnection
from CIM14.IEC61970.Dynamics.Block import Block
from CIM14.IEC61970.Dynamics.ConnectionFrame import ConnectionFrame
from CIM14.IEC61970.Dynamics.MetaBlockConInput import MetaBlockConInput
from CIM14.IEC61970.Dynamics.StaticVarDevice import StaticVarDevice
from CIM14.IEC61970.Dynamics.AttributeBlockParameter import AttributeBlockParameter
from CIM14.IEC61970.Dynamics.UserBlockParameter import UserBlockParameter
from CIM14.IEC61970.Dynamics.MetaBlockConnection import MetaBlockConnection
from CIM14.IEC61970.Dynamics.Slot import Slot
from CIM14.IEC61970.Dynamics.MetaBlockReference import MetaBlockReference
from CIM14.IEC61970.Dynamics.BlockInputReference import BlockInputReference
from CIM14.IEC61970.Dynamics.BlockParameter import BlockParameter
from CIM14.IEC61970.Dynamics.MetaBlockConSignal import MetaBlockConSignal
from CIM14.IEC61970.Dynamics.BlockOutputReference import BlockOutputReference
from CIM14.IEC61970.Dynamics.ExcitationSystemLimiter import ExcitationSystemLimiter
from CIM14.IEC61970.Dynamics.BlockType import BlockType
from CIM14.IEC61970.Dynamics.SlotOutput import SlotOutput
from CIM14.IEC61970.Dynamics.ProtectiveDevice import ProtectiveDevice
from CIM14.IEC61970.Dynamics.MetaBlockState import MetaBlockState
from CIM14.IEC61970.Dynamics.BlockUsageOutputReference import BlockUsageOutputReference
from CIM14.IEC61970.Dynamics.TieToMeasurement import TieToMeasurement
from CIM14.IEC61970.Dynamics.MetaBlockConnectivity import MetaBlockConnectivity
from CIM14.IEC61970.Dynamics.MetaBlockOutputReference import MetaBlockOutputReference
from CIM14.IEC61970.Dynamics.BlockOutputType import BlockOutputType

nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Dynamics"
nsPrefix = "cimDynamics"


class BlockKind(str):
    """Values are: powerSystemStabilizer, automaticVoltageControl, turbine, govenor, dotDotDot, energySource, exciter
    """
    pass
