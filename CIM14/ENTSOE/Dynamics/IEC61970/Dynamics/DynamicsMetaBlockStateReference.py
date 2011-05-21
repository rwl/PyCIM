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

class DynamicsMetaBlockStateReference(CoreIdentifiedObject):

    def __init__(self, positiveFlowIn=False, MetaBlockConnectable=None, StandardControlBlock_MetaBlockConnectable=None, MemberOf_MetaBlockReference=None, *args, **kw_args):
        """Initialises a new 'DynamicsMetaBlockStateReference' instance.

        @param positiveFlowIn: 
        @param MetaBlockConnectable:
        @param StandardControlBlock_MetaBlockConnectable:
        @param MemberOf_MetaBlockReference:
        """

        self.positiveFlowIn = positiveFlowIn

        self._MetaBlockConnectable = None
        self.MetaBlockConnectable = MetaBlockConnectable

        self._StandardControlBlock_MetaBlockConnectable = None
        self.StandardControlBlock_MetaBlockConnectable = StandardControlBlock_MetaBlockConnectable

        self._MemberOf_MetaBlockReference = None
        self.MemberOf_MetaBlockReference = MemberOf_MetaBlockReference

        super(DynamicsMetaBlockStateReference, self).__init__(*args, **kw_args)

    _attrs = ["positiveFlowIn"]
    _attr_types = {"positiveFlowIn": bool}
    _defaults = {"positiveFlowIn": False}
    _enums = {}
    _refs = ["MetaBlockConnectable", "StandardControlBlock_MetaBlockConnectable", "MemberOf_MetaBlockReference"]
    _many_refs = []

    def getMetaBlockConnectable(self):
        
        return self._MetaBlockConnectable

    def setMetaBlockConnectable(self, value):
        if self._MetaBlockConnectable is not None:
            filtered = [x for x in self.MetaBlockConnectable.MetaBlockStateReference if x != self]
            self._MetaBlockConnectable._MetaBlockStateReference = filtered

        self._MetaBlockConnectable = value
        if self._MetaBlockConnectable is not None:
            if self not in self._MetaBlockConnectable._MetaBlockStateReference:
                self._MetaBlockConnectable._MetaBlockStateReference.append(self)

    MetaBlockConnectable = property(getMetaBlockConnectable, setMetaBlockConnectable)

    def getStandardControlBlock_MetaBlockConnectable(self):
        
        return self._StandardControlBlock_MetaBlockConnectable

    def setStandardControlBlock_MetaBlockConnectable(self, value):
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            filtered = [x for x in self.StandardControlBlock_MetaBlockConnectable.StandardControlBlock_MetaBlockStateReference if x != self]
            self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockStateReference = filtered

        self._StandardControlBlock_MetaBlockConnectable = value
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            if self not in self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockStateReference:
                self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockStateReference.append(self)

    StandardControlBlock_MetaBlockConnectable = property(getStandardControlBlock_MetaBlockConnectable, setStandardControlBlock_MetaBlockConnectable)

    def getMemberOf_MetaBlockReference(self):
        
        return self._MemberOf_MetaBlockReference

    def setMemberOf_MetaBlockReference(self, value):
        if self._MemberOf_MetaBlockReference is not None:
            filtered = [x for x in self.MemberOf_MetaBlockReference.MetaBlockStateReference if x != self]
            self._MemberOf_MetaBlockReference._MetaBlockStateReference = filtered

        self._MemberOf_MetaBlockReference = value
        if self._MemberOf_MetaBlockReference is not None:
            if self not in self._MemberOf_MetaBlockReference._MetaBlockStateReference:
                self._MemberOf_MetaBlockReference._MetaBlockStateReference.append(self)

    MemberOf_MetaBlockReference = property(getMemberOf_MetaBlockReference, setMemberOf_MetaBlockReference)

