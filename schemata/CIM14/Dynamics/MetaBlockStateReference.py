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

class MetaBlockStateReference(IdentifiedObject):

    def __init__(self, positiveFlowIn=False, StandardControlBlock_MetaBlockConnectable=None, MetaBlockConnectable=None, MemberOf_MetaBlockReference=None, **kw_args):
        """Initializes a new 'MetaBlockStateReference' instance.

        @param positiveFlowIn: If true then any flows associated with a terminal are referenced as positive from the system into the device. 
        @param StandardControlBlock_MetaBlockConnectable:
        @param MetaBlockConnectable:
        @param MemberOf_MetaBlockReference:
        """
        #: If true then any flows associated with a terminal are referenced as positive from the system into the device.
        self.positiveFlowIn = positiveFlowIn

        self._StandardControlBlock_MetaBlockConnectable = None
        self.StandardControlBlock_MetaBlockConnectable = StandardControlBlock_MetaBlockConnectable

        self._MetaBlockConnectable = None
        self.MetaBlockConnectable = MetaBlockConnectable

        self._MemberOf_MetaBlockReference = None
        self.MemberOf_MetaBlockReference = MemberOf_MetaBlockReference

        super(MetaBlockStateReference, self).__init__(**kw_args)

    def getStandardControlBlock_MetaBlockConnectable(self):
        
        return self._StandardControlBlock_MetaBlockConnectable

    def setStandardControlBlock_MetaBlockConnectable(self, value):
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            filtered = [x for x in self.StandardControlBlock_MetaBlockConnectable.StandardControlBlock_MetaBlockStateReference if x != self]
            self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockStateReference = filtered

        self._StandardControlBlock_MetaBlockConnectable = value
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockStateReference.append(self)

    StandardControlBlock_MetaBlockConnectable = property(getStandardControlBlock_MetaBlockConnectable, setStandardControlBlock_MetaBlockConnectable)

    def getMetaBlockConnectable(self):
        
        return self._MetaBlockConnectable

    def setMetaBlockConnectable(self, value):
        if self._MetaBlockConnectable is not None:
            filtered = [x for x in self.MetaBlockConnectable.MetaBlockStateReference if x != self]
            self._MetaBlockConnectable._MetaBlockStateReference = filtered

        self._MetaBlockConnectable = value
        if self._MetaBlockConnectable is not None:
            self._MetaBlockConnectable._MetaBlockStateReference.append(self)

    MetaBlockConnectable = property(getMetaBlockConnectable, setMetaBlockConnectable)

    def getMemberOf_MetaBlockReference(self):
        
        return self._MemberOf_MetaBlockReference

    def setMemberOf_MetaBlockReference(self, value):
        if self._MemberOf_MetaBlockReference is not None:
            filtered = [x for x in self.MemberOf_MetaBlockReference.MetaBlockStateReference if x != self]
            self._MemberOf_MetaBlockReference._MetaBlockStateReference = filtered

        self._MemberOf_MetaBlockReference = value
        if self._MemberOf_MetaBlockReference is not None:
            self._MemberOf_MetaBlockReference._MetaBlockStateReference.append(self)

    MemberOf_MetaBlockReference = property(getMemberOf_MetaBlockReference, setMemberOf_MetaBlockReference)

