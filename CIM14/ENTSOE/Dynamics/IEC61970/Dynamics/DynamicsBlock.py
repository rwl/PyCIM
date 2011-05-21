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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CorePowerSystemResource import CorePowerSystemResource

class DynamicsBlock(CorePowerSystemResource):

    def __init__(self, inService=False, positiveFlowIn=False, BlockParameter=None, PowerSystemResource=None, BlockConnection=None, MemberOf_BlockConnectivity=None, MetaBlock=None, *args, **kw_args):
        """Initialises a new 'DynamicsBlock' instance.

        @param inService: 
        @param positiveFlowIn: 
        @param BlockParameter: 
        @param PowerSystemResource:
        @param BlockConnection: 
        @param MemberOf_BlockConnectivity:
        @param MetaBlock:
        """

        self.inService = inService


        self.positiveFlowIn = positiveFlowIn

        self._BlockParameter = []
        self.BlockParameter = [] if BlockParameter is None else BlockParameter

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._BlockConnection = []
        self.BlockConnection = [] if BlockConnection is None else BlockConnection

        self._MemberOf_BlockConnectivity = None
        self.MemberOf_BlockConnectivity = MemberOf_BlockConnectivity

        self._MetaBlock = None
        self.MetaBlock = MetaBlock

        super(DynamicsBlock, self).__init__(*args, **kw_args)

    _attrs = ["inService", "positiveFlowIn"]
    _attr_types = {"inService": bool, "positiveFlowIn": bool}
    _defaults = {"inService": False, "positiveFlowIn": False}
    _enums = {}
    _refs = ["BlockParameter", "PowerSystemResource", "BlockConnection", "MemberOf_BlockConnectivity", "MetaBlock"]
    _many_refs = ["BlockParameter", "BlockConnection"]

    def getBlockParameter(self):
        """
        """
        return self._BlockParameter

    def setBlockParameter(self, value):
        for x in self._BlockParameter:
            x.MemberOf_Block = None
        for y in value:
            y._MemberOf_Block = self
        self._BlockParameter = value

    BlockParameter = property(getBlockParameter, setBlockParameter)

    def addBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj.MemberOf_Block = self

    def removeBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj.MemberOf_Block = None

    def getPowerSystemResource(self):
        
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.Block if x != self]
            self._PowerSystemResource._Block = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            if self not in self._PowerSystemResource._Block:
                self._PowerSystemResource._Block.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getBlockConnection(self):
        """
        """
        return self._BlockConnection

    def setBlockConnection(self, value):
        for x in self._BlockConnection:
            x.Block = None
        for y in value:
            y._Block = self
        self._BlockConnection = value

    BlockConnection = property(getBlockConnection, setBlockConnection)

    def addBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj.Block = self

    def removeBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj.Block = None

    def getMemberOf_BlockConnectivity(self):
        
        return self._MemberOf_BlockConnectivity

    def setMemberOf_BlockConnectivity(self, value):
        if self._MemberOf_BlockConnectivity is not None:
            filtered = [x for x in self.MemberOf_BlockConnectivity.Block if x != self]
            self._MemberOf_BlockConnectivity._Block = filtered

        self._MemberOf_BlockConnectivity = value
        if self._MemberOf_BlockConnectivity is not None:
            if self not in self._MemberOf_BlockConnectivity._Block:
                self._MemberOf_BlockConnectivity._Block.append(self)

    MemberOf_BlockConnectivity = property(getMemberOf_BlockConnectivity, setMemberOf_BlockConnectivity)

    def getMetaBlock(self):
        
        return self._MetaBlock

    def setMetaBlock(self, value):
        if self._MetaBlock is not None:
            filtered = [x for x in self.MetaBlock.Block if x != self]
            self._MetaBlock._Block = filtered

        self._MetaBlock = value
        if self._MetaBlock is not None:
            if self not in self._MetaBlock._Block:
                self._MetaBlock._Block.append(self)

    MetaBlock = property(getMetaBlock, setMetaBlock)

