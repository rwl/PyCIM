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

class Slot(IdentifiedObject):

    def __init__(self, blockType0=None, slotReference0=None, slotOutput0=None, connectionFrame0=None, slotInput0=None, *args, **kw_args):
        """Initialises a new 'Slot' instance.

        @param blockType0:
        @param slotReference0:
        @param slotOutput0:
        @param connectionFrame0:
        @param slotInput0:
        """
        self._blockType0 = None
        self.blockType0 = blockType0

        self._slotReference0 = []
        self.slotReference0 = [] if slotReference0 is None else slotReference0

        self._slotOutput0 = []
        self.slotOutput0 = [] if slotOutput0 is None else slotOutput0

        self._connectionFrame0 = None
        self.connectionFrame0 = connectionFrame0

        self._slotInput0 = []
        self.slotInput0 = [] if slotInput0 is None else slotInput0

        super(Slot, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["blockType0", "slotReference0", "slotOutput0", "connectionFrame0", "slotInput0"]
    _many_refs = ["slotReference0", "slotOutput0", "slotInput0"]

    def getblockType0(self):
        
        return self._blockType0

    def setblockType0(self, value):
        if self._blockType0 is not None:
            filtered = [x for x in self.blockType0.slot0 if x != self]
            self._blockType0._slot0 = filtered

        self._blockType0 = value
        if self._blockType0 is not None:
            if self not in self._blockType0._slot0:
                self._blockType0._slot0.append(self)

    blockType0 = property(getblockType0, setblockType0)

    def getslotReference0(self):
        
        return self._slotReference0

    def setslotReference0(self, value):
        for x in self._slotReference0:
            x.slot0 = None
        for y in value:
            y._slot0 = self
        self._slotReference0 = value

    slotReference0 = property(getslotReference0, setslotReference0)

    def addslotReference0(self, *slotReference0):
        for obj in slotReference0:
            obj.slot0 = self

    def removeslotReference0(self, *slotReference0):
        for obj in slotReference0:
            obj.slot0 = None

    def getslotOutput0(self):
        
        return self._slotOutput0

    def setslotOutput0(self, value):
        for x in self._slotOutput0:
            x.slot0 = None
        for y in value:
            y._slot0 = self
        self._slotOutput0 = value

    slotOutput0 = property(getslotOutput0, setslotOutput0)

    def addslotOutput0(self, *slotOutput0):
        for obj in slotOutput0:
            obj.slot0 = self

    def removeslotOutput0(self, *slotOutput0):
        for obj in slotOutput0:
            obj.slot0 = None

    def getconnectionFrame0(self):
        
        return self._connectionFrame0

    def setconnectionFrame0(self, value):
        if self._connectionFrame0 is not None:
            filtered = [x for x in self.connectionFrame0.slot0 if x != self]
            self._connectionFrame0._slot0 = filtered

        self._connectionFrame0 = value
        if self._connectionFrame0 is not None:
            if self not in self._connectionFrame0._slot0:
                self._connectionFrame0._slot0.append(self)

    connectionFrame0 = property(getconnectionFrame0, setconnectionFrame0)

    def getslotInput0(self):
        
        return self._slotInput0

    def setslotInput0(self, value):
        for x in self._slotInput0:
            x.slot0 = None
        for y in value:
            y._slot0 = self
        self._slotInput0 = value

    slotInput0 = property(getslotInput0, setslotInput0)

    def addslotInput0(self, *slotInput0):
        for obj in slotInput0:
            obj.slot0 = self

    def removeslotInput0(self, *slotInput0):
        for obj in slotInput0:
            obj.slot0 = None

