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

class SlotReference(IdentifiedObject):
    """The specific role the block usage is playing in a connection frame. This allows connections to be established at the meta dynamics level and not at the instance level.
    """

    def __init__(self, slot0=None, block0=None, compositeModel0=None, *args, **kw_args):
        """Initialises a new 'SlotReference' instance.

        @param slot0:
        @param block0:
        @param compositeModel0:
        """
        self._slot0 = None
        self.slot0 = slot0

        self._block0 = []
        self.block0 = [] if block0 is None else block0

        self._compositeModel0 = []
        self.compositeModel0 = [] if compositeModel0 is None else compositeModel0

        super(SlotReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["slot0", "block0", "compositeModel0"]
    _many_refs = ["block0", "compositeModel0"]

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        if self._slot0 is not None:
            filtered = [x for x in self.slot0.slotReference0 if x != self]
            self._slot0._slotReference0 = filtered

        self._slot0 = value
        if self._slot0 is not None:
            self._slot0._slotReference0.append(self)

    slot0 = property(getslot0, setslot0)

    def getblock0(self):
        
        return self._block0

    def setblock0(self, value):
        for x in self._block0:
            x._slotReference0 = None
        for y in value:
            y._slotReference0 = self
        self._block0 = value

    block0 = property(getblock0, setblock0)

    def addblock0(self, *block0):
        for obj in block0:
            obj._slotReference0 = self
            self._block0.append(obj)

    def removeblock0(self, *block0):
        for obj in block0:
            obj._slotReference0 = None
            self._block0.remove(obj)

    def getcompositeModel0(self):
        
        return self._compositeModel0

    def setcompositeModel0(self, value):
        for p in self._compositeModel0:
            filtered = [q for q in p.slotReference0 if q != self]
            self._compositeModel0._slotReference0 = filtered
        for r in value:
            if self not in r._slotReference0:
                r._slotReference0.append(self)
        self._compositeModel0 = value

    compositeModel0 = property(getcompositeModel0, setcompositeModel0)

    def addcompositeModel0(self, *compositeModel0):
        for obj in compositeModel0:
            if self not in obj._slotReference0:
                obj._slotReference0.append(self)
            self._compositeModel0.append(obj)

    def removecompositeModel0(self, *compositeModel0):
        for obj in compositeModel0:
            if self in obj._slotReference0:
                obj._slotReference0.remove(self)
            self._compositeModel0.remove(obj)

