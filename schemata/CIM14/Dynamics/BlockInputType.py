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

class BlockInputType(IdentifiedObject):

    def __init__(self, slotInput0=None, metaBlockInput0=None, **kw_args):
        """Initializes a new 'BlockInputType' instance.

        @param slotInput0:
        @param metaBlockInput0:
        """
        self._slotInput0 = []
        self.slotInput0 = [] if slotInput0 is None else slotInput0

        self._metaBlockInput0 = []
        self.metaBlockInput0 = [] if metaBlockInput0 is None else metaBlockInput0

        super(BlockInputType, self).__init__(**kw_args)

    def getslotInput0(self):
        
        return self._slotInput0

    def setslotInput0(self, value):
        for x in self._slotInput0:
            x._blockInputType0 = None
        for y in value:
            y._blockInputType0 = self
        self._slotInput0 = value

    slotInput0 = property(getslotInput0, setslotInput0)

    def addslotInput0(self, *slotInput0):
        for obj in slotInput0:
            obj._blockInputType0 = self
            self._slotInput0.append(obj)

    def removeslotInput0(self, *slotInput0):
        for obj in slotInput0:
            obj._blockInputType0 = None
            self._slotInput0.remove(obj)

    def getmetaBlockInput0(self):
        
        return self._metaBlockInput0

    def setmetaBlockInput0(self, value):
        for x in self._metaBlockInput0:
            x._blockInputType0 = None
        for y in value:
            y._blockInputType0 = self
        self._metaBlockInput0 = value

    metaBlockInput0 = property(getmetaBlockInput0, setmetaBlockInput0)

    def addmetaBlockInput0(self, *metaBlockInput0):
        for obj in metaBlockInput0:
            obj._blockInputType0 = self
            self._metaBlockInput0.append(obj)

    def removemetaBlockInput0(self, *metaBlockInput0):
        for obj in metaBlockInput0:
            obj._blockInputType0 = None
            self._metaBlockInput0.remove(obj)

