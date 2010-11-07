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

class BlockOutputType(IdentifiedObject):

    def __init__(self, metaBlockOutput0=None, slotOutput0=None, **kw_args):
        """Initializes a new 'BlockOutputType' instance.

        @param metaBlockOutput0:
        @param slotOutput0:
        """
        self._metaBlockOutput0 = []
        self.metaBlockOutput0 = [] if metaBlockOutput0 is None else metaBlockOutput0

        self._slotOutput0 = []
        self.slotOutput0 = [] if slotOutput0 is None else slotOutput0

        super(BlockOutputType, self).__init__(**kw_args)

    def getmetaBlockOutput0(self):
        
        return self._metaBlockOutput0

    def setmetaBlockOutput0(self, value):
        for x in self._metaBlockOutput0:
            x._blockOutputType0 = None
        for y in value:
            y._blockOutputType0 = self
        self._metaBlockOutput0 = value

    metaBlockOutput0 = property(getmetaBlockOutput0, setmetaBlockOutput0)

    def addmetaBlockOutput0(self, *metaBlockOutput0):
        for obj in metaBlockOutput0:
            obj._blockOutputType0 = self
            self._metaBlockOutput0.append(obj)

    def removemetaBlockOutput0(self, *metaBlockOutput0):
        for obj in metaBlockOutput0:
            obj._blockOutputType0 = None
            self._metaBlockOutput0.remove(obj)

    def getslotOutput0(self):
        
        return self._slotOutput0

    def setslotOutput0(self, value):
        for x in self._slotOutput0:
            x._blockOutputType0 = None
        for y in value:
            y._blockOutputType0 = self
        self._slotOutput0 = value

    slotOutput0 = property(getslotOutput0, setslotOutput0)

    def addslotOutput0(self, *slotOutput0):
        for obj in slotOutput0:
            obj._blockOutputType0 = self
            self._slotOutput0.append(obj)

    def removeslotOutput0(self, *slotOutput0):
        for obj in slotOutput0:
            obj._blockOutputType0 = None
            self._slotOutput0.remove(obj)

