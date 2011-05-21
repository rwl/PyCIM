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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class BlockConnectivity(IdentifiedObject):
    """A instance definition of connectivity of BlockUsage objects as defined in a a BlockConnection within the dyanmics-meta-model.
    """

    def __init__(self, MetaBlockConnectivity=None, Block=None, BlockConnection=None, *args, **kw_args):
        """Initialises a new 'BlockConnectivity' instance.

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

        super(BlockConnectivity, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConnectivity", "Block", "BlockConnection"]
    _many_refs = ["Block", "BlockConnection"]

    def getMetaBlockConnectivity(self):
        
        return self._MetaBlockConnectivity

    def setMetaBlockConnectivity(self, value):
        if self._MetaBlockConnectivity is not None:
            filtered = [x for x in self.MetaBlockConnectivity.BlockConnectivity if x != self]
            self._MetaBlockConnectivity._BlockConnectivity = filtered

        self._MetaBlockConnectivity = value
        if self._MetaBlockConnectivity is not None:
            if self not in self._MetaBlockConnectivity._BlockConnectivity:
                self._MetaBlockConnectivity._BlockConnectivity.append(self)

    MetaBlockConnectivity = property(getMetaBlockConnectivity, setMetaBlockConnectivity)

    def getBlock(self):
        
        return self._Block

    def setBlock(self, value):
        for x in self._Block:
            x.MemberOf_BlockConnectivity = None
        for y in value:
            y._MemberOf_BlockConnectivity = self
        self._Block = value

    Block = property(getBlock, setBlock)

    def addBlock(self, *Block):
        for obj in Block:
            obj.MemberOf_BlockConnectivity = self

    def removeBlock(self, *Block):
        for obj in Block:
            obj.MemberOf_BlockConnectivity = None

    def getBlockConnection(self):
        
        return self._BlockConnection

    def setBlockConnection(self, value):
        for x in self._BlockConnection:
            x.MemberOf_BlockConnectivity = None
        for y in value:
            y._MemberOf_BlockConnectivity = self
        self._BlockConnection = value

    BlockConnection = property(getBlockConnection, setBlockConnection)

    def addBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj.MemberOf_BlockConnectivity = self

    def removeBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj.MemberOf_BlockConnectivity = None

