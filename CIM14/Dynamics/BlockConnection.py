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

class BlockConnection(IdentifiedObject):
    """A meta-dyanamics model connectivity specification.
    """

    def __init__(self, MetaBlockConnection=None, MemberOf_BlockConnectivity=None, Block=None, *args, **kw_args):
        """Initialises a new 'BlockConnection' instance.

        @param MetaBlockConnection:
        @param MemberOf_BlockConnectivity:
        @param Block:
        """
        self._MetaBlockConnection = None
        self.MetaBlockConnection = MetaBlockConnection

        self._MemberOf_BlockConnectivity = None
        self.MemberOf_BlockConnectivity = MemberOf_BlockConnectivity

        self._Block = None
        self.Block = Block

        super(BlockConnection, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConnection", "MemberOf_BlockConnectivity", "Block"]
    _many_refs = []

    def getMetaBlockConnection(self):
        
        return self._MetaBlockConnection

    def setMetaBlockConnection(self, value):
        if self._MetaBlockConnection is not None:
            filtered = [x for x in self.MetaBlockConnection.BlockConnection if x != self]
            self._MetaBlockConnection._BlockConnection = filtered

        self._MetaBlockConnection = value
        if self._MetaBlockConnection is not None:
            if self not in self._MetaBlockConnection._BlockConnection:
                self._MetaBlockConnection._BlockConnection.append(self)

    MetaBlockConnection = property(getMetaBlockConnection, setMetaBlockConnection)

    def getMemberOf_BlockConnectivity(self):
        
        return self._MemberOf_BlockConnectivity

    def setMemberOf_BlockConnectivity(self, value):
        if self._MemberOf_BlockConnectivity is not None:
            filtered = [x for x in self.MemberOf_BlockConnectivity.BlockConnection if x != self]
            self._MemberOf_BlockConnectivity._BlockConnection = filtered

        self._MemberOf_BlockConnectivity = value
        if self._MemberOf_BlockConnectivity is not None:
            if self not in self._MemberOf_BlockConnectivity._BlockConnection:
                self._MemberOf_BlockConnectivity._BlockConnection.append(self)

    MemberOf_BlockConnectivity = property(getMemberOf_BlockConnectivity, setMemberOf_BlockConnectivity)

    def getBlock(self):
        
        return self._Block

    def setBlock(self, value):
        if self._Block is not None:
            filtered = [x for x in self.Block.BlockConnection if x != self]
            self._Block._BlockConnection = filtered

        self._Block = value
        if self._Block is not None:
            if self not in self._Block._BlockConnection:
                self._Block._BlockConnection.append(self)

    Block = property(getBlock, setBlock)

