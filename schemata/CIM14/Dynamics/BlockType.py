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

class BlockType(IdentifiedObject):
    """This is the kind of a block used to specify what kind of blocks could fit into a particular slot.    For example, only blocks of type 'pss' would fit into a 'pss' type block.  Though a cross compound generator configuration would possibly have multple pss blocks playing specific roles such as pss1 and pss2..
    """

    def __init__(self, slot0=None, metaBlock0=None, **kw_args):
        """Initializes a new 'BlockType' instance.

        @param slot0:
        @param metaBlock0:
        """
        self._slot0 = []
        self.slot0 = [] if slot0 is None else slot0

        self._metaBlock0 = []
        self.metaBlock0 = [] if metaBlock0 is None else metaBlock0

        super(BlockType, self).__init__(**kw_args)

    def getslot0(self):
        
        return self._slot0

    def setslot0(self, value):
        for x in self._slot0:
            x._blockType0 = None
        for y in value:
            y._blockType0 = self
        self._slot0 = value

    slot0 = property(getslot0, setslot0)

    def addslot0(self, *slot0):
        for obj in slot0:
            obj._blockType0 = self
            self._slot0.append(obj)

    def removeslot0(self, *slot0):
        for obj in slot0:
            obj._blockType0 = None
            self._slot0.remove(obj)

    def getmetaBlock0(self):
        
        return self._metaBlock0

    def setmetaBlock0(self, value):
        for x in self._metaBlock0:
            x._blockType0 = None
        for y in value:
            y._blockType0 = self
        self._metaBlock0 = value

    metaBlock0 = property(getmetaBlock0, setmetaBlock0)

    def addmetaBlock0(self, *metaBlock0):
        for obj in metaBlock0:
            obj._blockType0 = self
            self._metaBlock0.append(obj)

    def removemetaBlock0(self, *metaBlock0):
        for obj in metaBlock0:
            obj._blockType0 = None
            self._metaBlock0.remove(obj)

