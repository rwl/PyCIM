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

class ConnectionFrame(IdentifiedObject):

    def __init__(self, slotConnection0=None, slot0=None, *args, **kw_args):
        """Initialises a new 'ConnectionFrame' instance.

        @param slotConnection0:
        @param slot0:
        """
        self._slotConnection0 = []
        self.slotConnection0 = [] if slotConnection0 is None else slotConnection0

        self._slot0 = []
        self.slot0 = [] if slot0 is None else slot0

        super(ConnectionFrame, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slotConnection0", "slot0"]
    _many_refs = ["slotConnection0", "slot0"]

    def getslotConnection0(self):
        
        return self._slotConnection0

    def setslotConnection0(self, value):
        for x in self._slotConnection0:
            x._connectionFrame0 = None
        for y in value:
            y._connectionFrame0 = self
        self._slotConnection0 = value

    slotConnection0 = property(getslotConnection0, setslotConnection0)

    def addslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj._connectionFrame0 = self
            self._slotConnection0.append(obj)

    def removeslotConnection0(self, *slotConnection0):
        for obj in slotConnection0:
            obj._connectionFrame0 = None
            self._slotConnection0.remove(obj)

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        for x in self._slot0:
            x._connectionFrame0 = None
        for y in value:
            y._connectionFrame0 = self
        self._slot0 = value

    slot0 = property(getslot0, setslot0)

    def addslot0(self, *slot0):
        for obj in slot0:
            obj._connectionFrame0 = self
            self._slot0.append(obj)

    def removeslot0(self, *slot0):
        for obj in slot0:
            obj._connectionFrame0 = None
            self._slot0.remove(obj)

