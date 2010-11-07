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

class BlockInputReference(IdentifiedObject):
    """Used at the meta dynamics level. This is how the internal definiton of a block references the input of another block.
    """

    def __init__(self, metaBlockReference0=None, metaBlockInput0=None, BlockConnectable=None, **kw_args):
        """Initializes a new 'BlockInputReference' instance.

        @param metaBlockReference0:
        @param metaBlockInput0: References the idenfiied input for the block reference.
        @param BlockConnectable: Each block reference input is usually tied to one (sometimes zero for optional inputs) external block inputs or internal block reference outputs.
        """
        self._metaBlockReference0 = None
        self.metaBlockReference0 = metaBlockReference0

        self._metaBlockInput0 = None
        self.metaBlockInput0 = metaBlockInput0

        self._BlockConnectable = None
        self.BlockConnectable = BlockConnectable

        super(BlockInputReference, self).__init__(**kw_args)

    def getmetaBlockReference0(self):
        
        return self._metaBlockReference0

    def setmetaBlockReference0(self, value):
        if self._metaBlockReference0 is not None:
            filtered = [x for x in self.metaBlockReference0.blockInputReference0 if x != self]
            self._metaBlockReference0._blockInputReference0 = filtered

        self._metaBlockReference0 = value
        if self._metaBlockReference0 is not None:
            self._metaBlockReference0._blockInputReference0.append(self)

    metaBlockReference0 = property(getmetaBlockReference0, setmetaBlockReference0)

    def getmetaBlockInput0(self):
        """References the idenfiied input for the block reference.
        """
        return self._metaBlockInput0

    def setmetaBlockInput0(self, value):
        if self._metaBlockInput0 is not None:
            filtered = [x for x in self.metaBlockInput0.blockInputReference0 if x != self]
            self._metaBlockInput0._blockInputReference0 = filtered

        self._metaBlockInput0 = value
        if self._metaBlockInput0 is not None:
            self._metaBlockInput0._blockInputReference0.append(self)

    metaBlockInput0 = property(getmetaBlockInput0, setmetaBlockInput0)

    def getBlockConnectable(self):
        """Each block reference input is usually tied to one (sometimes zero for optional inputs) external block inputs or internal block reference outputs.
        """
        return self._BlockConnectable

    def setBlockConnectable(self, value):
        if self._BlockConnectable is not None:
            filtered = [x for x in self.BlockConnectable.BlockInputReference if x != self]
            self._BlockConnectable._BlockInputReference = filtered

        self._BlockConnectable = value
        if self._BlockConnectable is not None:
            self._BlockConnectable._BlockInputReference.append(self)

    BlockConnectable = property(getBlockConnectable, setBlockConnectable)

