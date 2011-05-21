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

