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

class DynamicsBlockParameter(CoreIdentifiedObject):

    def __init__(self, value=0.0, MetaBlockParameter=None, MemberOf_MetaBlockReference=None, MemberOf_Block=None, *args, **kw_args):
        """Initialises a new 'DynamicsBlockParameter' instance.

        @param value: 
        @param MetaBlockParameter:
        @param MemberOf_MetaBlockReference:
        @param MemberOf_Block:
        """

        self.value = value

        self._MetaBlockParameter = None
        self.MetaBlockParameter = MetaBlockParameter

        self._MemberOf_MetaBlockReference = None
        self.MemberOf_MetaBlockReference = MemberOf_MetaBlockReference

        self._MemberOf_Block = None
        self.MemberOf_Block = MemberOf_Block

        super(DynamicsBlockParameter, self).__init__(*args, **kw_args)

    _attrs = ["value"]
    _attr_types = {"value": float}
    _defaults = {"value": 0.0}
    _enums = {}
    _refs = ["MetaBlockParameter", "MemberOf_MetaBlockReference", "MemberOf_Block"]
    _many_refs = []

    def getMetaBlockParameter(self):
        
        return self._MetaBlockParameter

    def setMetaBlockParameter(self, value):
        if self._MetaBlockParameter is not None:
            filtered = [x for x in self.MetaBlockParameter.BlockParameter if x != self]
            self._MetaBlockParameter._BlockParameter = filtered

        self._MetaBlockParameter = value
        if self._MetaBlockParameter is not None:
            if self not in self._MetaBlockParameter._BlockParameter:
                self._MetaBlockParameter._BlockParameter.append(self)

    MetaBlockParameter = property(getMetaBlockParameter, setMetaBlockParameter)

    def getMemberOf_MetaBlockReference(self):
        
        return self._MemberOf_MetaBlockReference

    def setMemberOf_MetaBlockReference(self, value):
        if self._MemberOf_MetaBlockReference is not None:
            filtered = [x for x in self.MemberOf_MetaBlockReference.BlockParameter if x != self]
            self._MemberOf_MetaBlockReference._BlockParameter = filtered

        self._MemberOf_MetaBlockReference = value
        if self._MemberOf_MetaBlockReference is not None:
            if self not in self._MemberOf_MetaBlockReference._BlockParameter:
                self._MemberOf_MetaBlockReference._BlockParameter.append(self)

    MemberOf_MetaBlockReference = property(getMemberOf_MetaBlockReference, setMemberOf_MetaBlockReference)

    def getMemberOf_Block(self):
        
        return self._MemberOf_Block

    def setMemberOf_Block(self, value):
        if self._MemberOf_Block is not None:
            filtered = [x for x in self.MemberOf_Block.BlockParameter if x != self]
            self._MemberOf_Block._BlockParameter = filtered

        self._MemberOf_Block = value
        if self._MemberOf_Block is not None:
            if self not in self._MemberOf_Block._BlockParameter:
                self._MemberOf_Block._BlockParameter.append(self)

    MemberOf_Block = property(getMemberOf_Block, setMemberOf_Block)

