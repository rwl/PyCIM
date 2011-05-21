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

class BlockUsageInputReference(IdentifiedObject):
    """Used at instance level to tie the input of a referenced block to the output of another referenced block. Note that typically an input is only tied to an output of another block at the same PowerSystemResource, but there is no restriction to do so.
    """

    def __init__(self, block0=None, BlockUsageOutputReference=None, metaBlockInput0=None, *args, **kw_args):
        """Initialises a new 'BlockUsageInputReference' instance.

        @param block0:
        @param BlockUsageOutputReference: Can cross BlockUsage objects.
        @param metaBlockInput0:
        """
        self._block0 = None
        self.block0 = block0

        self._BlockUsageOutputReference = None
        self.BlockUsageOutputReference = BlockUsageOutputReference

        self._metaBlockInput0 = None
        self.metaBlockInput0 = metaBlockInput0

        super(BlockUsageInputReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["block0", "BlockUsageOutputReference", "metaBlockInput0"]
    _many_refs = []

    def getblock0(self):
        
        return self._block0

    def setblock0(self, value):
        if self._block0 is not None:
            filtered = [x for x in self.block0.blockUsageInputReference0 if x != self]
            self._block0._blockUsageInputReference0 = filtered

        self._block0 = value
        if self._block0 is not None:
            if self not in self._block0._blockUsageInputReference0:
                self._block0._blockUsageInputReference0.append(self)

    block0 = property(getblock0, setblock0)

    def getBlockUsageOutputReference(self):
        """Can cross BlockUsage objects.
        """
        return self._BlockUsageOutputReference

    def setBlockUsageOutputReference(self, value):
        if self._BlockUsageOutputReference is not None:
            filtered = [x for x in self.BlockUsageOutputReference.BlockUsageInputReference if x != self]
            self._BlockUsageOutputReference._BlockUsageInputReference = filtered

        self._BlockUsageOutputReference = value
        if self._BlockUsageOutputReference is not None:
            if self not in self._BlockUsageOutputReference._BlockUsageInputReference:
                self._BlockUsageOutputReference._BlockUsageInputReference.append(self)

    BlockUsageOutputReference = property(getBlockUsageOutputReference, setBlockUsageOutputReference)

    def getmetaBlockInput0(self):
        
        return self._metaBlockInput0

    def setmetaBlockInput0(self, value):
        if self._metaBlockInput0 is not None:
            filtered = [x for x in self.metaBlockInput0.blockUsageInputReference0 if x != self]
            self._metaBlockInput0._blockUsageInputReference0 = filtered

        self._metaBlockInput0 = value
        if self._metaBlockInput0 is not None:
            if self not in self._metaBlockInput0._blockUsageInputReference0:
                self._metaBlockInput0._blockUsageInputReference0.append(self)

    metaBlockInput0 = property(getmetaBlockInput0, setmetaBlockInput0)

