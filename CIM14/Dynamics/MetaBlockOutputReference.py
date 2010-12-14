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

class MetaBlockOutputReference(IdentifiedObject):

    def __init__(self, MetaBlockConnectable=None, MemberOf_MetaBlockReference=None, MetaBlockSignal=None, StandardControlBlock_MetaBlockConnectable=None, *args, **kw_args):
        """Initialises a new 'MetaBlockOutputReference' instance.

        @param MetaBlockConnectable:
        @param MemberOf_MetaBlockReference:
        @param MetaBlockSignal:
        @param StandardControlBlock_MetaBlockConnectable:
        """
        self._MetaBlockConnectable = None
        self.MetaBlockConnectable = MetaBlockConnectable

        self._MemberOf_MetaBlockReference = None
        self.MemberOf_MetaBlockReference = MemberOf_MetaBlockReference

        self._MetaBlockSignal = []
        self.MetaBlockSignal = [] if MetaBlockSignal is None else MetaBlockSignal

        self._StandardControlBlock_MetaBlockConnectable = None
        self.StandardControlBlock_MetaBlockConnectable = StandardControlBlock_MetaBlockConnectable

        super(MetaBlockOutputReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MetaBlockConnectable", "MemberOf_MetaBlockReference", "MetaBlockSignal", "StandardControlBlock_MetaBlockConnectable"]
    _many_refs = ["MetaBlockSignal"]

    def getMetaBlockConnectable(self):
        
        return self._MetaBlockConnectable

    def setMetaBlockConnectable(self, value):
        if self._MetaBlockConnectable is not None:
            filtered = [x for x in self.MetaBlockConnectable.MetaBlockOutputReference if x != self]
            self._MetaBlockConnectable._MetaBlockOutputReference = filtered

        self._MetaBlockConnectable = value
        if self._MetaBlockConnectable is not None:
            if self not in self._MetaBlockConnectable._MetaBlockOutputReference:
                self._MetaBlockConnectable._MetaBlockOutputReference.append(self)

    MetaBlockConnectable = property(getMetaBlockConnectable, setMetaBlockConnectable)

    def getMemberOf_MetaBlockReference(self):
        
        return self._MemberOf_MetaBlockReference

    def setMemberOf_MetaBlockReference(self, value):
        if self._MemberOf_MetaBlockReference is not None:
            filtered = [x for x in self.MemberOf_MetaBlockReference.MetaBlockOutputReference if x != self]
            self._MemberOf_MetaBlockReference._MetaBlockOutputReference = filtered

        self._MemberOf_MetaBlockReference = value
        if self._MemberOf_MetaBlockReference is not None:
            if self not in self._MemberOf_MetaBlockReference._MetaBlockOutputReference:
                self._MemberOf_MetaBlockReference._MetaBlockOutputReference.append(self)

    MemberOf_MetaBlockReference = property(getMemberOf_MetaBlockReference, setMemberOf_MetaBlockReference)

    def getMetaBlockSignal(self):
        
        return self._MetaBlockSignal

    def setMetaBlockSignal(self, value):
        for x in self._MetaBlockSignal:
            x.To = None
        for y in value:
            y._To = self
        self._MetaBlockSignal = value

    MetaBlockSignal = property(getMetaBlockSignal, setMetaBlockSignal)

    def addMetaBlockSignal(self, *MetaBlockSignal):
        for obj in MetaBlockSignal:
            obj.To = self

    def removeMetaBlockSignal(self, *MetaBlockSignal):
        for obj in MetaBlockSignal:
            obj.To = None

    def getStandardControlBlock_MetaBlockConnectable(self):
        
        return self._StandardControlBlock_MetaBlockConnectable

    def setStandardControlBlock_MetaBlockConnectable(self, value):
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            filtered = [x for x in self.StandardControlBlock_MetaBlockConnectable.StandardControlBlock_MetaBlockOutputReference if x != self]
            self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockOutputReference = filtered

        self._StandardControlBlock_MetaBlockConnectable = value
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            if self not in self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockOutputReference:
                self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockOutputReference.append(self)

    StandardControlBlock_MetaBlockConnectable = property(getStandardControlBlock_MetaBlockConnectable, setStandardControlBlock_MetaBlockConnectable)

