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

"""This package models generalized dynamic models. Standard models and user defined dynamics models are included.  In some ways this duplicates the partial modeling that was done in the GenerationDynamics package, but it far exceeds that package in terms of flexibility and extensibility.   This package does not attempt to fully specficfy all possible dynamics models in specific UML, but rather builds a framework in which to exchange standard or custom dyanmics models based on 'well known' block functions.
"""

nsPrefix = "cimDynamics"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Dynamics"

from CIM14.Dynamics.BlockConnection import BlockConnection
from CIM14.Dynamics.RotatingMachine import RotatingMachine
from CIM14.Dynamics.AsynchronousMachine import AsynchronousMachine
from CIM14.Dynamics.BlockUsageInputReference import BlockUsageInputReference
from CIM14.Dynamics.MetaBlockConnectable import MetaBlockConnectable
from CIM14.Dynamics.MetaBlockOutput import MetaBlockOutput
from CIM14.Dynamics.MetaBlockConOutput import MetaBlockConOutput
from CIM14.Dynamics.MetaBlock import MetaBlock
from CIM14.Dynamics.MetaBlockInput import MetaBlockInput
from CIM14.Dynamics.SlotReference import SlotReference
from CIM14.Dynamics.MetaBlockInputReference import MetaBlockInputReference
from CIM14.Dynamics.MetaBlockParameter import MetaBlockParameter
from CIM14.Dynamics.MetaBlockParameterReference import MetaBlockParameterReference
from CIM14.Dynamics.CompositeModel import CompositeModel
from CIM14.Dynamics.BlockInputType import BlockInputType
from CIM14.Dynamics.BlockConnectivity import BlockConnectivity
from CIM14.Dynamics.SlotInput import SlotInput
from CIM14.Dynamics.MetaBlockSignal import MetaBlockSignal
from CIM14.Dynamics.MetaBlockStateReference import MetaBlockStateReference
from CIM14.Dynamics.BlockConstant import BlockConstant
from CIM14.Dynamics.SourceModels import SourceModels
from CIM14.Dynamics.SlotConnection import SlotConnection
from CIM14.Dynamics.Block import Block
from CIM14.Dynamics.ConnectionFrame import ConnectionFrame
from CIM14.Dynamics.MetaBlockConInput import MetaBlockConInput
from CIM14.Dynamics.StaticVarDevice import StaticVarDevice
from CIM14.Dynamics.AttributeBlockParameter import AttributeBlockParameter
from CIM14.Dynamics.UserBlockParameter import UserBlockParameter
from CIM14.Dynamics.MetaBlockConnection import MetaBlockConnection
from CIM14.Dynamics.Slot import Slot
from CIM14.Dynamics.MetaBlockReference import MetaBlockReference
from CIM14.Dynamics.BlockInputReference import BlockInputReference
from CIM14.Dynamics.BlockParameter import BlockParameter
from CIM14.Dynamics.MetaBlockConSignal import MetaBlockConSignal
from CIM14.Dynamics.BlockOutputReference import BlockOutputReference
from CIM14.Dynamics.ExcitationSystemLimiter import ExcitationSystemLimiter
from CIM14.Dynamics.BlockType import BlockType
from CIM14.Dynamics.SlotOutput import SlotOutput
from CIM14.Dynamics.ProtectiveDevice import ProtectiveDevice
from CIM14.Dynamics.MetaBlockState import MetaBlockState
from CIM14.Dynamics.BlockUsageOutputReference import BlockUsageOutputReference
from CIM14.Dynamics.TieToMeasurement import TieToMeasurement
from CIM14.Dynamics.MetaBlockConnectivity import MetaBlockConnectivity
from CIM14.Dynamics.MetaBlockOutputReference import MetaBlockOutputReference
from CIM14.Dynamics.BlockOutputType import BlockOutputType

