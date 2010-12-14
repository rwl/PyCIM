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

