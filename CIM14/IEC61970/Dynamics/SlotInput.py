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

class SlotInput(IdentifiedObject):

    def __init__(self, blockInputType0=None, slotConnection0=None, slot0=None, *args, **kw_args):
        """Initialises a new 'SlotInput' instance.

        @param blockInputType0:
        @param slotConnection0:
        @param slot0:
        """
        self._blockInputType0 = None
        self.blockInputType0 = blockInputType0

        self._slotConnection0 = None
        self.slotConnection0 = slotConnection0

        self._slot0 = None
        self.slot0 = slot0

        super(SlotInput, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["blockInputType0", "slotConnection0", "slot0"]
    _many_refs = []

    def getblockInputType0(self):
        
        return self._blockInputType0

    def setblockInputType0(self, value):
        if self._blockInputType0 is not None:
            filtered = [x for x in self.blockInputType0.slotInput0 if x != self]
            self._blockInputType0._slotInput0 = filtered

        self._blockInputType0 = value
        if self._blockInputType0 is not None:
            if self not in self._blockInputType0._slotInput0:
                self._blockInputType0._slotInput0.append(self)

    blockInputType0 = property(getblockInputType0, setblockInputType0)

    def getslotConnection0(self):
        
        return self._slotConnection0

    def setslotConnection0(self, value):
        if self._slotConnection0 is not None:
            self._slotConnection0._slotInput0 = None

        self._slotConnection0 = value
        if self._slotConnection0 is not None:
            self._slotConnection0.slotInput0 = None
            self._slotConnection0._slotInput0 = self

    slotConnection0 = property(getslotConnection0, setslotConnection0)

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        if self._slot0 is not None:
            filtered = [x for x in self.slot0.slotInput0 if x != self]
            self._slot0._slotInput0 = filtered

        self._slot0 = value
        if self._slot0 is not None:
            if self not in self._slot0._slotInput0:
                self._slot0._slotInput0.append(self)

    slot0 = property(getslot0, setslot0)

