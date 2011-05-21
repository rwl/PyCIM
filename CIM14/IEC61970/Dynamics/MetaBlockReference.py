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

class MetaBlockReference(IdentifiedObject):
    """References a control block at the internal meta dynamics model level.    These references are contained in other blocks and reference the single instance of the meta model that defines a particular block definition. One would not expect to see bock references contained within a primitive block.
    """

    def __init__(self, equationType='', blockInputReference0=None, MemberOf_MetaBlock=None, MetaBlock=None, blockOutputReference0=None, MetaBlockStateReference=None, MetaBlockInputReference=None, MetaBlockOutputReference=None, BlockParameter=None, MetaBlockParameterReference=None, *args, **kw_args):
        """Initialises a new 'MetaBlockReference' instance.

        @param equationType: should be enum, initial conditions vs. simulation equations 
        @param blockInputReference0:
        @param MemberOf_MetaBlock:
        @param MetaBlock:
        @param blockOutputReference0:
        @param MetaBlockStateReference:
        @param MetaBlockInputReference:
        @param MetaBlockOutputReference:
        @param BlockParameter:
        @param MetaBlockParameterReference:
        """
        #: should be enum, initial conditions vs. simulation equations
        self.equationType = equationType

        self._blockInputReference0 = []
        self.blockInputReference0 = [] if blockInputReference0 is None else blockInputReference0

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        self.MetaBlock = MetaBlock

        self._blockOutputReference0 = []
        self.blockOutputReference0 = [] if blockOutputReference0 is None else blockOutputReference0

        self._MetaBlockStateReference = []
        self.MetaBlockStateReference = [] if MetaBlockStateReference is None else MetaBlockStateReference

        self._MetaBlockInputReference = []
        self.MetaBlockInputReference = [] if MetaBlockInputReference is None else MetaBlockInputReference

        self._MetaBlockOutputReference = []
        self.MetaBlockOutputReference = [] if MetaBlockOutputReference is None else MetaBlockOutputReference

        self._BlockParameter = []
        self.BlockParameter = [] if BlockParameter is None else BlockParameter

        self._MetaBlockParameterReference = []
        self.MetaBlockParameterReference = [] if MetaBlockParameterReference is None else MetaBlockParameterReference

        super(MetaBlockReference, self).__init__(*args, **kw_args)

    _attrs = ["equationType"]
    _attr_types = {"equationType": str}
    _defaults = {"equationType": ''}
    _enums = {}
    _refs = ["blockInputReference0", "MemberOf_MetaBlock", "MetaBlock", "blockOutputReference0", "MetaBlockStateReference", "MetaBlockInputReference", "MetaBlockOutputReference", "BlockParameter", "MetaBlockParameterReference"]
    _many_refs = ["blockInputReference0", "blockOutputReference0", "MetaBlockStateReference", "MetaBlockInputReference", "MetaBlockOutputReference", "BlockParameter", "MetaBlockParameterReference"]

    def getblockInputReference0(self):
        
        return self._blockInputReference0

    def setblockInputReference0(self, value):
        for x in self._blockInputReference0:
            x.metaBlockReference0 = None
        for y in value:
            y._metaBlockReference0 = self
        self._blockInputReference0 = value

    blockInputReference0 = property(getblockInputReference0, setblockInputReference0)

    def addblockInputReference0(self, *blockInputReference0):
        for obj in blockInputReference0:
            obj.metaBlockReference0 = self

    def removeblockInputReference0(self, *blockInputReference0):
        for obj in blockInputReference0:
            obj.metaBlockReference0 = None

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

    MetaBlock = None

    def getblockOutputReference0(self):
        
        return self._blockOutputReference0

    def setblockOutputReference0(self, value):
        for p in self._blockOutputReference0:
            filtered = [q for q in p.metaBlockReference0 if q != self]
            self._blockOutputReference0._metaBlockReference0 = filtered
        for r in value:
            if self not in r._metaBlockReference0:
                r._metaBlockReference0.append(self)
        self._blockOutputReference0 = value

    blockOutputReference0 = property(getblockOutputReference0, setblockOutputReference0)

    def addblockOutputReference0(self, *blockOutputReference0):
        for obj in blockOutputReference0:
            if self not in obj._metaBlockReference0:
                obj._metaBlockReference0.append(self)
            self._blockOutputReference0.append(obj)

    def removeblockOutputReference0(self, *blockOutputReference0):
        for obj in blockOutputReference0:
            if self in obj._metaBlockReference0:
                obj._metaBlockReference0.remove(self)
            self._blockOutputReference0.remove(obj)

    def getMetaBlockStateReference(self):
        
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

    def getMetaBlockInputReference(self):
        
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

    def getMetaBlockOutputReference(self):
        
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

    def getBlockParameter(self):
        
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

    def getMetaBlockParameterReference(self):
        
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

