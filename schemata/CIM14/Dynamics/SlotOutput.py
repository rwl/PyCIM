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

class SlotOutput(IdentifiedObject):

    def __init__(self, slot0=None, slotConnection0=None, blockOutputType0=None, **kw_args):
        """Initializes a new 'SlotOutput' instance.

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

        super(SlotOutput, self).__init__(**kw_args)

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        if self._slot0 is not None:
            filtered = [x for x in self.slot0.slotOutput0 if x != self]
            self._slot0._slotOutput0 = filtered

        self._slot0 = value
        if self._slot0 is not None:
            self._slot0._slotOutput0.append(self)

    slot0 = property(getslot0, setslot0)

    def getslotConnection0(self):
        
        return self._slotConnection0

    def setslotConnection0(self, value):
        for x in self._slotConnection0:
            x._slotOutput0 = None
        for y in value:
            y._slotOutput0 = self
        self._slotConnection0 = value

    slotConnection0 = property(getslotConnection0, setslotConnection0)

    def addslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj._slotOutput0 = self
            self._slotConnection0.append(obj)

    def removeslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj._slotOutput0 = None
            self._slotConnection0.remove(obj)

    def getblockOutputType0(self):
        
        return self._blockOutputType0

    def setblockOutputType0(self, value):
        if self._blockOutputType0 is not None:
            filtered = [x for x in self.blockOutputType0.slotOutput0 if x != self]
            self._blockOutputType0._slotOutput0 = filtered

        self._blockOutputType0 = value
        if self._blockOutputType0 is not None:
            self._blockOutputType0._slotOutput0.append(self)

    blockOutputType0 = property(getblockOutputType0, setblockOutputType0)

