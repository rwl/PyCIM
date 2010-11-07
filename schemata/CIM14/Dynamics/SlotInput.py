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

class SlotInput(IdentifiedObject):

    def __init__(self, blockInputType0=None, slotConnection0=None, slot0=None, **kw_args):
        """Initializes a new 'SlotInput' instance.

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

        super(SlotInput, self).__init__(**kw_args)

    def getblockInputType0(self):
        
        return self._blockInputType0

    def setblockInputType0(self, value):
        if self._blockInputType0 is not None:
            filtered = [x for x in self.blockInputType0.slotInput0 if x != self]
            self._blockInputType0._slotInput0 = filtered

        self._blockInputType0 = value
        if self._blockInputType0 is not None:
            self._blockInputType0._slotInput0.append(self)

    blockInputType0 = property(getblockInputType0, setblockInputType0)

    def getslotConnection0(self):
        
        return self._slotConnection0

    def setslotConnection0(self, value):
        if self._slotConnection0 is not None:
            self._slotConnection0._slotInput0 = None

        self._slotConnection0 = value
        if self._slotConnection0 is not None:
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
            self._slot0._slotInput0.append(self)

    slot0 = property(getslot0, setslot0)

