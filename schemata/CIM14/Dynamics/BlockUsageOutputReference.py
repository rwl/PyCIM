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

class BlockUsageOutputReference(IdentifiedObject):
    """Used at instance level to tie the input of a referenced block to the output of another referenced block. Note that typically an input is only tied to an output of another block at the same PowerSystemResource, but there is no restriction to do so.   If the output is implicity tied to an input, then the an instance of this class is not required.  The sole purpose of this class is to explicitly tio the input of other blocks at the power system instance level.
    """

    def __init__(self, block0=None, BlockUsageInputReference=None, metaBlockOutput0=None, *args, **kw_args):
        """Initialises a new 'BlockUsageOutputReference' instance.

        @param block0:
        @param BlockUsageInputReference: Can cross BlockUsage objects.
        @param metaBlockOutput0:
        """
        self._block0 = None
        self.block0 = block0

        self._BlockUsageInputReference = []
        self.BlockUsageInputReference = [] if BlockUsageInputReference is None else BlockUsageInputReference

        self._metaBlockOutput0 = None
        self.metaBlockOutput0 = metaBlockOutput0

        super(BlockUsageOutputReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["block0", "BlockUsageInputReference", "metaBlockOutput0"]
    _many_refs = ["BlockUsageInputReference"]

    def getblock0(self):
        
        return self._block0

    def setblock0(self, value):
        if self._block0 is not None:
            filtered = [x for x in self.block0.BlockUsageOutputReference if x != self]
            self._block0._BlockUsageOutputReference = filtered

        self._block0 = value
        if self._block0 is not None:
            self._block0._BlockUsageOutputReference.append(self)

    block0 = property(getblock0, setblock0)

    def getBlockUsageInputReference(self):
        """Can cross BlockUsage objects.
        """
        return self._BlockUsageInputReference

    def setBlockUsageInputReference(self, value):
        for x in self._BlockUsageInputReference:
            x._BlockUsageOutputReference = None
        for y in value:
            y._BlockUsageOutputReference = self
        self._BlockUsageInputReference = value

    BlockUsageInputReference = property(getBlockUsageInputReference, setBlockUsageInputReference)

    def addBlockUsageInputReference(self, *BlockUsageInputReference):
        for obj in BlockUsageInputReference:
            obj._BlockUsageOutputReference = self
            self._BlockUsageInputReference.append(obj)

    def removeBlockUsageInputReference(self, *BlockUsageInputReference):
        for obj in BlockUsageInputReference:
            obj._BlockUsageOutputReference = None
            self._BlockUsageInputReference.remove(obj)

    def getmetaBlockOutput0(self):
        
        return self._metaBlockOutput0

    def setmetaBlockOutput0(self, value):
        if self._metaBlockOutput0 is not None:
            filtered = [x for x in self.metaBlockOutput0.blockUsageOutputReference0 if x != self]
            self._metaBlockOutput0._blockUsageOutputReference0 = filtered

        self._metaBlockOutput0 = value
        if self._metaBlockOutput0 is not None:
            self._metaBlockOutput0._blockUsageOutputReference0.append(self)

    metaBlockOutput0 = property(getmetaBlockOutput0, setmetaBlockOutput0)

