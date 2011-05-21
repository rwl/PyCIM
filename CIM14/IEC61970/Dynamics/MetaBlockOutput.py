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

from CIM14.IEC61970.Dynamics.MetaBlockConnectable import MetaBlockConnectable

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

