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

class DynamicsMetaBlock(CoreIdentifiedObject):

    def __init__(self, blockKind="", proprietary=False, Block=None, MetaBlockSignal=None, MetaBlockReference=None, MetaBlockParameter=None, MetaBlockOutput=None, MetaBlockInput=None, MetaBlockState=None, *args, **kw_args):
        """Initialises a new 'DynamicsMetaBlock' instance.

        @param blockKind: 
        @param proprietary: 
        @param Block: 
        @param MetaBlockSignal: 
        @param MetaBlockReference: 
        @param MetaBlockParameter: 
        @param MetaBlockOutput: 
        @param MetaBlockInput: 
        @param MetaBlockState: 
        """

        self.blockKind = blockKind


        self.proprietary = proprietary

        self._Block = []
        self.Block = [] if Block is None else Block

        self._MetaBlockSignal = []
        self.MetaBlockSignal = [] if MetaBlockSignal is None else MetaBlockSignal

        self._MetaBlockReference = []
        self.MetaBlockReference = [] if MetaBlockReference is None else MetaBlockReference

        self._MetaBlockParameter = []
        self.MetaBlockParameter = [] if MetaBlockParameter is None else MetaBlockParameter

        self._MetaBlockOutput = []
        self.MetaBlockOutput = [] if MetaBlockOutput is None else MetaBlockOutput

        self._MetaBlockInput = []
        self.MetaBlockInput = [] if MetaBlockInput is None else MetaBlockInput

        self._MetaBlockState = []
        self.MetaBlockState = [] if MetaBlockState is None else MetaBlockState

        super(DynamicsMetaBlock, self).__init__(*args, **kw_args)

    _attrs = ["blockKind", "proprietary"]
    _attr_types = {"blockKind": str, "proprietary": bool}
    _defaults = {"blockKind": "", "proprietary": False}
    _enums = {"blockKind": "DynamicsBlockKind"}
    _refs = ["Block", "MetaBlockSignal", "MetaBlockReference", "MetaBlockParameter", "MetaBlockOutput", "MetaBlockInput", "MetaBlockState"]
    _many_refs = ["Block", "MetaBlockSignal", "MetaBlockReference", "MetaBlockParameter", "MetaBlockOutput", "MetaBlockInput", "MetaBlockState"]

    def getBlock(self):
        """
        """
        return self._Block

    def setBlock(self, value):
        for x in self._Block:
            x.MetaBlock = None
        for y in value:
            y._MetaBlock = self
        self._Block = value

    Block = property(getBlock, setBlock)

    def addBlock(self, *Block):
        for obj in Block:
            obj.MetaBlock = self

    def removeBlock(self, *Block):
        for obj in Block:
            obj.MetaBlock = None

    def getMetaBlockSignal(self):
        """
        """
        return self._MetaBlockSignal

    def setMetaBlockSignal(self, value):
        for x in self._MetaBlockSignal:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockSignal = value

    MetaBlockSignal = property(getMetaBlockSignal, setMetaBlockSignal)

    def addMetaBlockSignal(self, *MetaBlockSignal):
        for obj in MetaBlockSignal:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockSignal(self, *MetaBlockSignal):
        for obj in MetaBlockSignal:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockReference(self):
        """
        """
        return self._MetaBlockReference

    def setMetaBlockReference(self, value):
        for x in self._MetaBlockReference:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockReference = value

    MetaBlockReference = property(getMetaBlockReference, setMetaBlockReference)

    def addMetaBlockReference(self, *MetaBlockReference):
        for obj in MetaBlockReference:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockReference(self, *MetaBlockReference):
        for obj in MetaBlockReference:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockParameter(self):
        """
        """
        return self._MetaBlockParameter

    def setMetaBlockParameter(self, value):
        for x in self._MetaBlockParameter:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockParameter = value

    MetaBlockParameter = property(getMetaBlockParameter, setMetaBlockParameter)

    def addMetaBlockParameter(self, *MetaBlockParameter):
        for obj in MetaBlockParameter:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockParameter(self, *MetaBlockParameter):
        for obj in MetaBlockParameter:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockOutput(self):
        """
        """
        return self._MetaBlockOutput

    def setMetaBlockOutput(self, value):
        for x in self._MetaBlockOutput:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockOutput = value

    MetaBlockOutput = property(getMetaBlockOutput, setMetaBlockOutput)

    def addMetaBlockOutput(self, *MetaBlockOutput):
        for obj in MetaBlockOutput:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockOutput(self, *MetaBlockOutput):
        for obj in MetaBlockOutput:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockInput(self):
        """
        """
        return self._MetaBlockInput

    def setMetaBlockInput(self, value):
        for x in self._MetaBlockInput:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockInput = value

    MetaBlockInput = property(getMetaBlockInput, setMetaBlockInput)

    def addMetaBlockInput(self, *MetaBlockInput):
        for obj in MetaBlockInput:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockInput(self, *MetaBlockInput):
        for obj in MetaBlockInput:
            obj.MemberOf_MetaBlock = None

    def getMetaBlockState(self):
        """
        """
        return self._MetaBlockState

    def setMetaBlockState(self, value):
        for x in self._MetaBlockState:
            x.MemberOf_MetaBlock = None
        for y in value:
            y._MemberOf_MetaBlock = self
        self._MetaBlockState = value

    MetaBlockState = property(getMetaBlockState, setMetaBlockState)

    def addMetaBlockState(self, *MetaBlockState):
        for obj in MetaBlockState:
            obj.MemberOf_MetaBlock = self

    def removeMetaBlockState(self, *MetaBlockState):
        for obj in MetaBlockState:
            obj.MemberOf_MetaBlock = None

