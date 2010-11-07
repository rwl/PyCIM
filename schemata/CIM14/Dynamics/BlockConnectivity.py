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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BlockConnectivity(IdentifiedObject):
    """A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.
    """

    def __init__(self, MetaBlockConnectivity=None, Block=None, BlockConnection=None, **kw_args):
        """Initializes a new 'BlockConnectivity' instance.

        @param MetaBlockConnectivity:
        @param Block:
        @param BlockConnection:
        """
        self._MetaBlockConnectivity = None
        self.MetaBlockConnectivity = MetaBlockConnectivity

        self._Block = []
        self.Block = [] if Block is None else Block

        self._BlockConnection = []
        self.BlockConnection = [] if BlockConnection is None else BlockConnection

        super(BlockConnectivity, self).__init__(**kw_args)

    def getMetaBlockConnectivity(self):
        
        return self._MetaBlockConnectivity

    def setMetaBlockConnectivity(self, value):
        if self._MetaBlockConnectivity is not None:
            filtered = [x for x in self.MetaBlockConnectivity.BlockConnectivity if x != self]
            self._MetaBlockConnectivity._BlockConnectivity = filtered

        self._MetaBlockConnectivity = value
        if self._MetaBlockConnectivity is not None:
            self._MetaBlockConnectivity._BlockConnectivity.append(self)

    MetaBlockConnectivity = property(getMetaBlockConnectivity, setMetaBlockConnectivity)

    def getBlock(self):
        
        return self._Block

    def setBlock(self, value):
        for x in self._Block:
            x._MemberOf_BlockConnectivity = None
        for y in value:
            y._MemberOf_BlockConnectivity = self
        self._Block = value

    Block = property(getBlock, setBlock)

    def addBlock(self, *Block):
        for obj in Block:
            obj._MemberOf_BlockConnectivity = self
            self._Block.append(obj)

    def removeBlock(self, *Block):
        for obj in Block:
            obj._MemberOf_BlockConnectivity = None
            self._Block.remove(obj)

    def getBlockConnection(self):
        
        return self._BlockConnection

    def setBlockConnection(self, value):
        for x in self._BlockConnection:
            x._MemberOf_BlockConnectivity = None
        for y in value:
            y._MemberOf_BlockConnectivity = self
        self._BlockConnection = value

    BlockConnection = property(getBlockConnection, setBlockConnection)

    def addBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj._MemberOf_BlockConnectivity = self
            self._BlockConnection.append(obj)

    def removeBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj._MemberOf_BlockConnectivity = None
            self._BlockConnection.remove(obj)

