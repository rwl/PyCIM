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

class MetaBlockConnection(IdentifiedObject):

    def __init__(self, slotname='', MetaBlockConOutput=None, MetaBlockConInput=None, metaBlockConnectivity0=None, BlockConnection=None, MemberOf_MetaBlockConnectivity=None, *args, **kw_args):
        """Initialises a new 'MetaBlockConnection' instance.

        @param slotname: Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections. 
        @param MetaBlockConOutput:
        @param MetaBlockConInput:
        @param metaBlockConnectivity0:
        @param BlockConnection:
        @param MemberOf_MetaBlockConnectivity:
        """
        #: Used for standard connection situations where multiple blocks of same class or same MetaBlock::blockkind have to be connected. The slotnames used are defined in the Reference Manual for Exchanging Standard Power System Dynamic Models. Application: Cross-compound or Combined Cycle connections.
        self.slotname = slotname

        self._MetaBlockConOutput = []
        self.MetaBlockConOutput = [] if MetaBlockConOutput is None else MetaBlockConOutput

        self._MetaBlockConInput = []
        self.MetaBlockConInput = [] if MetaBlockConInput is None else MetaBlockConInput

        self._metaBlockConnectivity0 = None
        self.metaBlockConnectivity0 = metaBlockConnectivity0

        self._BlockConnection = []
        self.BlockConnection = [] if BlockConnection is None else BlockConnection

        self._MemberOf_MetaBlockConnectivity = None
        self.MemberOf_MetaBlockConnectivity = MemberOf_MetaBlockConnectivity

        super(MetaBlockConnection, self).__init__(*args, **kw_args)

    _attrs = ["slotname"]
    _attr_types = {"slotname": str}
    _defaults = {"slotname": ''}
    _enums = {}
    _refs = ["MetaBlockConOutput", "MetaBlockConInput", "metaBlockConnectivity0", "BlockConnection", "MemberOf_MetaBlockConnectivity"]
    _many_refs = ["MetaBlockConOutput", "MetaBlockConInput", "BlockConnection"]

    def getMetaBlockConOutput(self):
        
        return self._MetaBlockConOutput

    def setMetaBlockConOutput(self, value):
        for x in self._MetaBlockConOutput:
            x.MemberOf_MetaBlockConnection = None
        for y in value:
            y._MemberOf_MetaBlockConnection = self
        self._MetaBlockConOutput = value

    MetaBlockConOutput = property(getMetaBlockConOutput, setMetaBlockConOutput)

    def addMetaBlockConOutput(self, *MetaBlockConOutput):
        for obj in MetaBlockConOutput:
            obj.MemberOf_MetaBlockConnection = self

    def removeMetaBlockConOutput(self, *MetaBlockConOutput):
        for obj in MetaBlockConOutput:
            obj.MemberOf_MetaBlockConnection = None

    def getMetaBlockConInput(self):
        
        return self._MetaBlockConInput

    def setMetaBlockConInput(self, value):
        for x in self._MetaBlockConInput:
            x.MemberOf_MetaBlockConnection = None
        for y in value:
            y._MemberOf_MetaBlockConnection = self
        self._MetaBlockConInput = value

    MetaBlockConInput = property(getMetaBlockConInput, setMetaBlockConInput)

    def addMetaBlockConInput(self, *MetaBlockConInput):
        for obj in MetaBlockConInput:
            obj.MemberOf_MetaBlockConnection = self

    def removeMetaBlockConInput(self, *MetaBlockConInput):
        for obj in MetaBlockConInput:
            obj.MemberOf_MetaBlockConnection = None

    def getmetaBlockConnectivity0(self):
        
        return self._metaBlockConnectivity0

    def setmetaBlockConnectivity0(self, value):
        if self._metaBlockConnectivity0 is not None:
            filtered = [x for x in self.metaBlockConnectivity0.metaBlockConnection0 if x != self]
            self._metaBlockConnectivity0._metaBlockConnection0 = filtered

        self._metaBlockConnectivity0 = value
        if self._metaBlockConnectivity0 is not None:
            if self not in self._metaBlockConnectivity0._metaBlockConnection0:
                self._metaBlockConnectivity0._metaBlockConnection0.append(self)

    metaBlockConnectivity0 = property(getmetaBlockConnectivity0, setmetaBlockConnectivity0)

    def getBlockConnection(self):
        
        return self._BlockConnection

    def setBlockConnection(self, value):
        for x in self._BlockConnection:
            x.MetaBlockConnection = None
        for y in value:
            y._MetaBlockConnection = self
        self._BlockConnection = value

    BlockConnection = property(getBlockConnection, setBlockConnection)

    def addBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj.MetaBlockConnection = self

    def removeBlockConnection(self, *BlockConnection):
        for obj in BlockConnection:
            obj.MetaBlockConnection = None

    def getMemberOf_MetaBlockConnectivity(self):
        
        return self._MemberOf_MetaBlockConnectivity

    def setMemberOf_MetaBlockConnectivity(self, value):
        if self._MemberOf_MetaBlockConnectivity is not None:
            filtered = [x for x in self.MemberOf_MetaBlockConnectivity.MetaBlockConnection if x != self]
            self._MemberOf_MetaBlockConnectivity._MetaBlockConnection = filtered

        self._MemberOf_MetaBlockConnectivity = value
        if self._MemberOf_MetaBlockConnectivity is not None:
            if self not in self._MemberOf_MetaBlockConnectivity._MetaBlockConnection:
                self._MemberOf_MetaBlockConnectivity._MetaBlockConnection.append(self)

    MemberOf_MetaBlockConnectivity = property(getMemberOf_MetaBlockConnectivity, setMemberOf_MetaBlockConnectivity)

