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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class Block(PowerSystemResource):
    """A specific usage of a dynamics block, supplied with parameters and any linkages to the power system static model that are required.     Sometimes a block is used to simply specify a location of input or output from dyanmics equations to the static model.
    """

    def __init__(self, positiveFlowIn=False, inService=False, Terminal=None, MemberOf_BlockConnectivity=None, blockUsageInputReference0=None, BlockUsageOutputReference=None, PowerSystemResource=None, slotReference0=None, tieToMeasurement0=None, MetaBlock=None, BlockConnection=None, BlockParameter=None, **kw_args):
        """Initializes a new 'Block' instance.

        @param positiveFlowIn: If true then any flows associated with a terminal are referenced as positive into the device. 
        @param inService: 
        @param Terminal: The optional terminal to which the block applies.  This is used to link a specific terminal flow to the dynamics block.
        @param MemberOf_BlockConnectivity:
        @param blockUsageInputReference0:
        @param BlockUsageOutputReference:
        @param PowerSystemResource: The power system resource associated with the dyanmics block instance.   This is optional because sometimes no linkage is needed, yet parameters must be specified.  Also the linkage to Terminal can be used instead of the linkage to PowerSystemResource.
        @param slotReference0:
        @param tieToMeasurement0:
        @param MetaBlock:
        @param BlockConnection:
        @param BlockParameter:
        """
        #: If true then any flows associated with a terminal are referenced as positive into the device.
        self.positiveFlowIn = positiveFlowIn


        self.inService = inService

        self._Terminal = None
        self.Terminal = Terminal

        self._MemberOf_BlockConnectivity = None
        self.MemberOf_BlockConnectivity = MemberOf_BlockConnectivity

        self._blockUsageInputReference0 = []
        self.blockUsageInputReference0 = [] if blockUsageInputReference0 is None else blockUsageInputReference0

        self._BlockUsageOutputReference = []
        self.BlockUsageOutputReference = [] if BlockUsageOutputReference is None else BlockUsageOutputReference

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._slotReference0 = None
        self.slotReference0 = slotReference0

        self._tieToMeasurement0 = []
        self.tieToMeasurement0 = [] if tieToMeasurement0 is None else tieToMeasurement0

        self._MetaBlock = None
        self.MetaBlock = MetaBlock

        self._BlockConnection = []
        self.BlockConnection = [] if BlockConnection is None else BlockConnection

        self._BlockParameter = []
        self.BlockParameter = [] if BlockParameter is None else BlockParameter

        super(Block, self).__init__(**kw_args)

    def getTerminal(self):
        """The optional terminal to which the block applies.  This is used to link a specific terminal flow to the dynamics block.
        """
        return self._Terminal

    def setTerminal(self, value):
        if self._Terminal is not None:
            filtered = [x for x in self.Terminal.Block if x != self]
            self._Terminal._Block = filtered

        self._Terminal = value
        if self._Terminal is not None:
            self._Terminal._Block.append(self)

    Terminal = property(getTerminal, setTerminal)

    def getMemberOf_BlockConnectivity(self):
        
        return self._MemberOf_BlockConnectivity

    def setMemberOf_BlockConnectivity(self, value):
        if self._MemberOf_BlockConnectivity is not None:
            filtered = [x for x in self.MemberOf_BlockConnectivity.Block if x != self]
            self._MemberOf_BlockConnectivity._Block = filtered

        self._MemberOf_BlockConnectivity = value
        if self._MemberOf_BlockConnectivity is not None:
            self._MemberOf_BlockConnectivity._Block.append(self)

    MemberOf_BlockConnectivity = property(getMemberOf_BlockConnectivity, setMemberOf_BlockConnectivity)

    def getblockUsageInputReference0(self):
        
        return self._blockUsageInputReference0

    def setblockUsageInputReference0(self, value):
        for x in self._blockUsageInputReference0:
            x._block0 = None
        for y in value:
            y._block0 = self
        self._blockUsageInputReference0 = value

    blockUsageInputReference0 = property(getblockUsageInputReference0, setblockUsageInputReference0)

    def addblockUsageInputReference0(self, *blockUsageInputReference0):
        for obj in blockUsageInputReference0:
            obj._block0 = self
            self._blockUsageInputReference0.append(obj)

    def removeblockUsageInputReference0(self, *blockUsageInputReference0):
        for obj in blockUsageInputReference0:
            obj._block0 = None
            self._blockUsageInputReference0.remove(obj)

    def getBlockUsageOutputReference(self):
        
        return self._BlockUsageOutputReference

    def setBlockUsageOutputReference(self, value):
        for x in self._BlockUsageOutputReference:
            x._block0 = None
        for y in value:
            y._block0 = self
        self._BlockUsageOutputReference = value

    BlockUsageOutputReference = property(getBlockUsageOutputReference, setBlockUsageOutputReference)

    def addBlockUsageOutputReference(self, *BlockUsageOutputReference):
        for obj in BlockUsageOutputReference:
            obj._block0 = self
            self._BlockUsageOutputReference.append(obj)

    def removeBlockUsageOutputReference(self, *BlockUsageOutputReference):
        for obj in BlockUsageOutputReference:
            obj._block0 = None
            self._BlockUsageOutputReference.remove(obj)

    def getPowerSystemResource(self):
        """The power system resource associated with the dyanmics block instance.   This is optional because sometimes no linkage is needed, yet parameters must be specified.  Also the linkage to Terminal can be used instead of the linkage to PowerSystemResource.
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.Block if x != self]
            self._PowerSystemResource._Block = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            self._PowerSystemResource._Block.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getslotReference0(self):
        
        return self._slotReference0

    def setslotReference0(self, value):
        if self._slotReference0 is not None:
            filtered = [x for x in self.slotReference0.block0 if x != self]
            self._slotReference0._block0 = filtered

        self._slotReference0 = value
        if self._slotReference0 is not None:
            self._slotReference0._block0.append(self)

    slotReference0 = property(getslotReference0, setslotReference0)

    def gettieToMeasurement0(self):
        
        return self._tieToMeasurement0

    def settieToMeasurement0(self, value):
        for x in self._tieToMeasurement0:
            x._block0 = None
        for y in value:
            y._block0 = self
        self._tieToMeasurement0 = value

    tieToMeasurement0 = property(gettieToMeasurement0, settieToMeasurement0)

    def addtieToMeasurement0(self, *tieToMeasurement0):
        for obj in tieToMeasurement0:
            obj._block0 = self
            self._tieToMeasurement0.append(obj)

    def removetieToMeasurement0(self, *tieToMeasurement0):
        for obj in tieToMeasurement0:
            obj._block0 = None
            self._tieToMeasurement0.remove(obj)

    def getMetaBlock(self):
        
        return self._MetaBlock

    def setMetaBlock(self, value):
        if self._MetaBlock is not None:
            filtered = [x for x in self.MetaBlock.Block if x != self]
            self._MetaBlock._Block = filtered

        self._MetaBlock = value
        if self._MetaBlock is not None:
            self._MetaBlock._Block.append(self)

    MetaBlock = property(getMetaBlock, setMetaBlock)

    def getBlockConnection(self):
        
        return self._BlockConnection

    def setBlockConnection(self, value):
        for x in self._BlockConnection:
            x._Block = None
        for y in value:
            y._Block = self
        self._BlockConnection = value

    BlockConnection = property(getBlockConnection, setBlockConnection)

    def addBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj._Block = self
            self._BlockConnection.append(obj)

    def removeBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj._Block = None
            self._BlockConnection.remove(obj)

    def getBlockParameter(self):
        
        return self._BlockParameter

    def setBlockParameter(self, value):
        for x in self._BlockParameter:
            x._MemberOf_Block = None
        for y in value:
            y._MemberOf_Block = self
        self._BlockParameter = value

    BlockParameter = property(getBlockParameter, setBlockParameter)

    def addBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj._MemberOf_Block = self
            self._BlockParameter.append(obj)

    def removeBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj._MemberOf_Block = None
            self._BlockParameter.remove(obj)

