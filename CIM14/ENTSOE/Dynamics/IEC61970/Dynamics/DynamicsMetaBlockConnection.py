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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject

class DynamicsMetaBlockConnection(CoreIdentifiedObject):

    def __init__(self, MetaBlockConOutput=None, MemberOf_MetaBlockConnectivity=None, BlockConnection=None, MetaBlockConInput=None, *args, **kw_args):
        """Initialises a new 'DynamicsMetaBlockConnection' instance.

        @param MetaBlockConOutput: 
        @param MemberOf_MetaBlockConnectivity:
        @param BlockConnection: 
        @param MetaBlockConInput: 
        """
        self._MetaBlockConOutput = []
        self.MetaBlockConOutput = [] if MetaBlockConOutput is None else MetaBlockConOutput

        self._MemberOf_MetaBlockConnectivity = None
        self.MemberOf_MetaBlockConnectivity = MemberOf_MetaBlockConnectivity

        self._BlockConnection = []
        self.BlockConnection = [] if BlockConnection is None else BlockConnection

        self._MetaBlockConInput = []
        self.MetaBlockConInput = [] if MetaBlockConInput is None else MetaBlockConInput

        super(DynamicsMetaBlockConnection, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConOutput", "MemberOf_MetaBlockConnectivity", "BlockConnection", "MetaBlockConInput"]
    _many_refs = ["MetaBlockConOutput", "BlockConnection", "MetaBlockConInput"]

    def getMetaBlockConOutput(self):
        """
        """
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

    def getBlockConnection(self):
        """
        """
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

    def getMetaBlockConInput(self):
        """
        """
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

