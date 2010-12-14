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

from CIM14.Dynamics.MetaBlockConnectable import MetaBlockConnectable

class MetaBlockOutput(MetaBlockConnectable):
    """Output state of a block.   This is a public interface external to the block.    One or more block outputs should be specified in order to link blocks together.    Certain block kinds might require a specific output. For example, an exciter block might require an output called 'Ea'.
    """

    def __init__(self, BlockOutputReference=None, MemberOf_MetaBlock=None, blockUsageOutputReference0=None, blockOutputType0=None, *args, **kw_args):
        """Initialises a new 'MetaBlockOutput' instance.

        @param BlockOutputReference: A block output reference for the block output.  The output of the block is passed to the block output reference which is a block connectable and thus can be connected at the dynamics metadata level to another block.
        @param MemberOf_MetaBlock: The block that contains the output.
        @param blockUsageOutputReference0:
        @param blockOutputType0:
        """
        self._BlockOutputReference = []
        self.BlockOutputReference = [] if BlockOutputReference is None else BlockOutputReference

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        self._blockUsageOutputReference0 = []
        self.blockUsageOutputReference0 = [] if blockUsageOutputReference0 is None else blockUsageOutputReference0

        self._blockOutputType0 = None
        self.blockOutputType0 = blockOutputType0

        super(MetaBlockOutput, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BlockOutputReference", "MemberOf_MetaBlock", "blockUsageOutputReference0", "blockOutputType0"]
    _many_refs = ["BlockOutputReference", "blockUsageOutputReference0"]

    def getBlockOutputReference(self):
        """A block output reference for the block output.  The output of the block is passed to the block output reference which is a block connectable and thus can be connected at the dynamics metadata level to another block.
        """
        return self._BlockOutputReference

    def setBlockOutputReference(self, value):
        for x in self._BlockOutputReference:
            x.metaBlockOutput0 = None
        for y in value:
            y._metaBlockOutput0 = self
        self._BlockOutputReference = value

    BlockOutputReference = property(getBlockOutputReference, setBlockOutputReference)

    def addBlockOutputReference(self, *BlockOutputReference):
        for obj in BlockOutputReference:
            obj.metaBlockOutput0 = self

    def removeBlockOutputReference(self, *BlockOutputReference):
        for obj in BlockOutputReference:
            obj.metaBlockOutput0 = None

    def getMemberOf_MetaBlock(self):
        """The block that contains the output.
        """
        return self._MemberOf_MetaBlock

    def setMemberOf_MetaBlock(self, value):
        if self._MemberOf_MetaBlock is not None:
            filtered = [x for x in self.MemberOf_MetaBlock.MetaBlockOutput if x != self]
            self._MemberOf_MetaBlock._MetaBlockOutput = filtered

        self._MemberOf_MetaBlock = value
        if self._MemberOf_MetaBlock is not None:
            if self not in self._MemberOf_MetaBlock._MetaBlockOutput:
                self._MemberOf_MetaBlock._MetaBlockOutput.append(self)

    MemberOf_MetaBlock = property(getMemberOf_MetaBlock, setMemberOf_MetaBlock)

    def getblockUsageOutputReference0(self):
        
        return self._blockUsageOutputReference0

    def setblockUsageOutputReference0(self, value):
        for x in self._blockUsageOutputReference0:
            x.metaBlockOutput0 = None
        for y in value:
            y._metaBlockOutput0 = self
        self._blockUsageOutputReference0 = value

    blockUsageOutputReference0 = property(getblockUsageOutputReference0, setblockUsageOutputReference0)

    def addblockUsageOutputReference0(self, *blockUsageOutputReference0):
        for obj in blockUsageOutputReference0:
            obj.metaBlockOutput0 = self

    def removeblockUsageOutputReference0(self, *blockUsageOutputReference0):
        for obj in blockUsageOutputReference0:
            obj.metaBlockOutput0 = None

    def getblockOutputType0(self):
        
        return self._blockOutputType0

    def setblockOutputType0(self, value):
        if self._blockOutputType0 is not None:
            filtered = [x for x in self.blockOutputType0.metaBlockOutput0 if x != self]
            self._blockOutputType0._metaBlockOutput0 = filtered

        self._blockOutputType0 = value
        if self._blockOutputType0 is not None:
            if self not in self._blockOutputType0._metaBlockOutput0:
                self._blockOutputType0._metaBlockOutput0.append(self)

    blockOutputType0 = property(getblockOutputType0, setblockOutputType0)

