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

class DynamicsMetaBlockReference(CoreIdentifiedObject):

    def __init__(self, equationType='', MetaBlockStateReference=None, MemberOf_MetaBlock=None, MetaBlockInputReference=None, BlockParameter=None, MetaBlock=None, MetaBlockOutputReference=None, MetaBlockParameterReference=None, *args, **kw_args):
        """Initialises a new 'DynamicsMetaBlockReference' instance.

        @param equationType: 
        @param MetaBlockStateReference: 
        @param MemberOf_MetaBlock:
        @param MetaBlockInputReference: 
        @param BlockParameter: 
        @param MetaBlock:
        @param MetaBlockOutputReference: 
        @param MetaBlockParameterReference: 
        """

        self.equationType = equationType

        self._MetaBlockStateReference = []
        self.MetaBlockStateReference = [] if MetaBlockStateReference is None else MetaBlockStateReference

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        self._MetaBlockInputReference = []
        self.MetaBlockInputReference = [] if MetaBlockInputReference is None else MetaBlockInputReference

        self._BlockParameter = []
        self.BlockParameter = [] if BlockParameter is None else BlockParameter

        self.MetaBlock = [] if MetaBlock is None else MetaBlock

        self._MetaBlockOutputReference = []
        self.MetaBlockOutputReference = [] if MetaBlockOutputReference is None else MetaBlockOutputReference

        self._MetaBlockParameterReference = []
        self.MetaBlockParameterReference = [] if MetaBlockParameterReference is None else MetaBlockParameterReference

        super(DynamicsMetaBlockReference, self).__init__(*args, **kw_args)

    _attrs = ["equationType"]
    _attr_types = {"equationType": str}
    _defaults = {"equationType": ''}
    _enums = {}
    _refs = ["MetaBlockStateReference", "MemberOf_MetaBlock", "MetaBlockInputReference", "BlockParameter", "MetaBlock", "MetaBlockOutputReference", "MetaBlockParameterReference"]
    _many_refs = ["MetaBlockStateReference", "MetaBlockInputReference", "BlockParameter", "MetaBlock", "MetaBlockOutputReference", "MetaBlockParameterReference"]

    def getMetaBlockStateReference(self):
        """
        """
        return self._MetaBlockStateReference

    def setMetaBlockStateReference(self, value):
        for x in self._MetaBlockStateReference:
            x.MemberOf_MetaBlockReference = None
        for y in value:
            y._MemberOf_MetaBlockReference = self
        self._MetaBlockStateReference = value

    MetaBlockStateReference = property(getMetaBlockStateReference, setMetaBlockStateReference)

    def addMetaBlockStateReference(self, *MetaBlockStateReference):
        for obj in MetaBlockStateReference:
            obj.MemberOf_MetaBlockReference = self

    def removeMetaBlockStateReference(self, *MetaBlockStateReference):
        for obj in MetaBlockStateReference:
            obj.MemberOf_MetaBlockReference = None

    def getMemberOf_MetaBlock(self):
        
        return self._MemberOf_MetaBlock

    def setMemberOf_MetaBlock(self, value):
        if self._MemberOf_MetaBlock is not None:
            filtered = [x for x in self.MemberOf_MetaBlock.MetaBlockReference if x != self]
            self._MemberOf_MetaBlock._MetaBlockReference = filtered

        self._MemberOf_MetaBlock = value
        if self._MemberOf_MetaBlock is not None:
            if self not in self._MemberOf_MetaBlock._MetaBlockReference:
                self._MemberOf_MetaBlock._MetaBlockReference.append(self)

    MemberOf_MetaBlock = property(getMemberOf_MetaBlock, setMemberOf_MetaBlock)

    def getMetaBlockInputReference(self):
        """
        """
        return self._MetaBlockInputReference

    def setMetaBlockInputReference(self, value):
        for x in self._MetaBlockInputReference:
            x.MemberOf_MetaBlockReference = None
        for y in value:
            y._MemberOf_MetaBlockReference = self
        self._MetaBlockInputReference = value

    MetaBlockInputReference = property(getMetaBlockInputReference, setMetaBlockInputReference)

    def addMetaBlockInputReference(self, *MetaBlockInputReference):
        for obj in MetaBlockInputReference:
            obj.MemberOf_MetaBlockReference = self

    def removeMetaBlockInputReference(self, *MetaBlockInputReference):
        for obj in MetaBlockInputReference:
            obj.MemberOf_MetaBlockReference = None

    def getBlockParameter(self):
        """
        """
        return self._BlockParameter

    def setBlockParameter(self, value):
        for x in self._BlockParameter:
            x.MemberOf_MetaBlockReference = None
        for y in value:
            y._MemberOf_MetaBlockReference = self
        self._BlockParameter = value

    BlockParameter = property(getBlockParameter, setBlockParameter)

    def addBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj.MemberOf_MetaBlockReference = self

    def removeBlockParameter(self, *BlockParameter):
        for obj in BlockParameter:
            obj.MemberOf_MetaBlockReference = None

    def add_MetaBlock(self, *MetaBlock):
        for obj in MetaBlock:
            self.MetaBlock.append(obj)

    def remove_MetaBlock(self, *MetaBlock):
        for obj in MetaBlock:
            self.MetaBlock.remove(obj)

    def getMetaBlockOutputReference(self):
        """
        """
        return self._MetaBlockOutputReference

    def setMetaBlockOutputReference(self, value):
        for x in self._MetaBlockOutputReference:
            x.MemberOf_MetaBlockReference = None
        for y in value:
            y._MemberOf_MetaBlockReference = self
        self._MetaBlockOutputReference = value

    MetaBlockOutputReference = property(getMetaBlockOutputReference, setMetaBlockOutputReference)

    def addMetaBlockOutputReference(self, *MetaBlockOutputReference):
        for obj in MetaBlockOutputReference:
            obj.MemberOf_MetaBlockReference = self

    def removeMetaBlockOutputReference(self, *MetaBlockOutputReference):
        for obj in MetaBlockOutputReference:
            obj.MemberOf_MetaBlockReference = None

    def getMetaBlockParameterReference(self):
        """
        """
        return self._MetaBlockParameterReference

    def setMetaBlockParameterReference(self, value):
        for x in self._MetaBlockParameterReference:
            x.MemberOf_MetaBlockReference = None
        for y in value:
            y._MemberOf_MetaBlockReference = self
        self._MetaBlockParameterReference = value

    MetaBlockParameterReference = property(getMetaBlockParameterReference, setMetaBlockParameterReference)

    def addMetaBlockParameterReference(self, *MetaBlockParameterReference):
        for obj in MetaBlockParameterReference:
            obj.MemberOf_MetaBlockReference = self

    def removeMetaBlockParameterReference(self, *MetaBlockParameterReference):
        for obj in MetaBlockParameterReference:
            obj.MemberOf_MetaBlockReference = None

