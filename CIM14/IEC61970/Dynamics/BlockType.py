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

class BlockType(IdentifiedObject):
    """This is the kind of a block used to specify what kind of blocks could fit into a particular slot.    For example, only blocks of type 'pss' would fit into a 'pss' type block.  Though a cross compound generator configuration would possibly have multple pss blocks playing specific roles such as pss1 and pss2..
    """

    def __init__(self, slot0=None, metaBlock0=None, *args, **kw_args):
        """Initialises a new 'BlockType' instance.

        @param slot0:
        @param metaBlock0:
        """
        self._slot0 = []
        self.slot0 = [] if slot0 is None else slot0

        self._metaBlock0 = []
        self.metaBlock0 = [] if metaBlock0 is None else metaBlock0

        super(BlockType, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slot0", "metaBlock0"]
    _many_refs = ["slot0", "metaBlock0"]

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        for x in self._slot0:
            x.blockType0 = None
        for y in value:
            y._blockType0 = self
        self._slot0 = value

    slot0 = property(getslot0, setslot0)

    def addslot0(self, *slot0):
        for obj in slot0:
            obj.blockType0 = self

    def removeslot0(self, *slot0):
        for obj in slot0:
            obj.blockType0 = None

    def getmetaBlock0(self):
        
        return self._metaBlock0

    def setmetaBlock0(self, value):
        for x in self._metaBlock0:
            x.blockType0 = None
        for y in value:
            y._blockType0 = self
        self._metaBlock0 = value

    metaBlock0 = property(getmetaBlock0, setmetaBlock0)

    def addmetaBlock0(self, *metaBlock0):
        for obj in metaBlock0:
            obj.blockType0 = self

    def removemetaBlock0(self, *metaBlock0):
        for obj in metaBlock0:
            obj.blockType0 = None

