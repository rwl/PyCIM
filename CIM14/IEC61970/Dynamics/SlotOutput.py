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

class SlotOutput(IdentifiedObject):

    def __init__(self, slot0=None, slotConnection0=None, blockOutputType0=None, *args, **kw_args):
        """Initialises a new 'SlotOutput' instance.

        @param slot0:
        @param slotConnection0:
        @param blockOutputType0:
        """
        self._slot0 = None
        self.slot0 = slot0

        self._slotConnection0 = []
        self.slotConnection0 = [] if slotConnection0 is None else slotConnection0

        self._blockOutputType0 = None
        self.blockOutputType0 = blockOutputType0

        super(SlotOutput, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slot0", "slotConnection0", "blockOutputType0"]
    _many_refs = ["slotConnection0"]

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        if self._slot0 is not None:
            filtered = [x for x in self.slot0.slotOutput0 if x != self]
            self._slot0._slotOutput0 = filtered

        self._slot0 = value
        if self._slot0 is not None:
            if self not in self._slot0._slotOutput0:
                self._slot0._slotOutput0.append(self)

    slot0 = property(getslot0, setslot0)

    def getslotConnection0(self):
        
        return self._slotConnection0

    def setslotConnection0(self, value):
        for x in self._slotConnection0:
            x.slotOutput0 = None
        for y in value:
            y._slotOutput0 = self
        self._slotConnection0 = value

    slotConnection0 = property(getslotConnection0, setslotConnection0)

    def addslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj.slotOutput0 = self

    def removeslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj.slotOutput0 = None

    def getblockOutputType0(self):
        
        return self._blockOutputType0

    def setblockOutputType0(self, value):
        if self._blockOutputType0 is not None:
            filtered = [x for x in self.blockOutputType0.slotOutput0 if x != self]
            self._blockOutputType0._slotOutput0 = filtered

        self._blockOutputType0 = value
        if self._blockOutputType0 is not None:
            if self not in self._blockOutputType0._slotOutput0:
                self._blockOutputType0._slotOutput0.append(self)

    blockOutputType0 = property(getblockOutputType0, setblockOutputType0)

