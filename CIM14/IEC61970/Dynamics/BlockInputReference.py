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

class BlockInputReference(IdentifiedObject):
    """Used at the meta dynamics level. This is how the internal definiton of a block references the input of another block.
    """

    def __init__(self, metaBlockReference0=None, metaBlockInput0=None, BlockConnectable=None, *args, **kw_args):
        """Initialises a new 'BlockInputReference' instance.

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

        super(BlockInputReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["metaBlockReference0", "metaBlockInput0", "BlockConnectable"]
    _many_refs = []

    def getmetaBlockReference0(self):
        
        return self._metaBlockReference0

    def setmetaBlockReference0(self, value):
        if self._metaBlockReference0 is not None:
            filtered = [x for x in self.metaBlockReference0.blockInputReference0 if x != self]
            self._metaBlockReference0._blockInputReference0 = filtered

        self._metaBlockReference0 = value
        if self._metaBlockReference0 is not None:
            if self not in self._metaBlockReference0._blockInputReference0:
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
            if self not in self._metaBlockInput0._blockInputReference0:
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
            if self not in self._BlockConnectable._BlockInputReference:
                self._BlockConnectable._BlockInputReference.append(self)

    BlockConnectable = property(getBlockConnectable, setBlockConnectable)

