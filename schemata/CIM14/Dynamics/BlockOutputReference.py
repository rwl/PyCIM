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

from CIM14.Dynamics.MetaBlockConnectable import MetaBlockConnectable

class BlockOutputReference(MetaBlockConnectable):
    """References output from another block at the meta dynamics level. The other block must be a BlockReference in containing block.
    """

    def __init__(self, metaBlockOutput0=None, metaBlockReference0=None, **kw_args):
        """Initializes a new 'BlockOutputReference' instance.

        @param metaBlockOutput0:
        @param metaBlockReference0:
        """
        self._metaBlockOutput0 = None
        self.metaBlockOutput0 = metaBlockOutput0

        self._metaBlockReference0 = []
        self.metaBlockReference0 = [] if metaBlockReference0 is None else metaBlockReference0

        super(BlockOutputReference, self).__init__(**kw_args)

    def getmetaBlockOutput0(self):
        
        return self._metaBlockOutput0

    def setmetaBlockOutput0(self, value):
        if self._metaBlockOutput0 is not None:
            filtered = [x for x in self.metaBlockOutput0.BlockOutputReference if x != self]
            self._metaBlockOutput0._BlockOutputReference = filtered

        self._metaBlockOutput0 = value
        if self._metaBlockOutput0 is not None:
            self._metaBlockOutput0._BlockOutputReference.append(self)

    metaBlockOutput0 = property(getmetaBlockOutput0, setmetaBlockOutput0)

    def getmetaBlockReference0(self):
        
        return self._metaBlockReference0

    def setmetaBlockReference0(self, value):
        for p in self._metaBlockReference0:
            filtered = [q for q in p.blockOutputReference0 if q != self]
            self._metaBlockReference0._blockOutputReference0 = filtered
        for r in value:
            if self not in r._blockOutputReference0:
                r._blockOutputReference0.append(self)
        self._metaBlockReference0 = value

    metaBlockReference0 = property(getmetaBlockReference0, setmetaBlockReference0)

    def addmetaBlockReference0(self, *metaBlockReference0):
        for obj in metaBlockReference0:
            if self not in obj._blockOutputReference0:
                obj._blockOutputReference0.append(self)
            self._metaBlockReference0.append(obj)

    def removemetaBlockReference0(self, *metaBlockReference0):
        for obj in metaBlockReference0:
            if self in obj._blockOutputReference0:
                obj._blockOutputReference0.remove(self)
            self._metaBlockReference0.remove(obj)

