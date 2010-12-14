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

class MetaBlockParameterReference(IdentifiedObject):
    """References a parameter of a block used in the internal representation of a block.
    """

    def __init__(self, StandardControlBlock_MetaBlockConnectable=None, MetaBlockConnectable=None, MemberOf_MetaBlockReference=None, *args, **kw_args):
        """Initialises a new 'MetaBlockParameterReference' instance.

        @param StandardControlBlock_MetaBlockConnectable:
        @param MetaBlockConnectable:
        @param MemberOf_MetaBlockReference:
        """
        self._StandardControlBlock_MetaBlockConnectable = None
        self.StandardControlBlock_MetaBlockConnectable = StandardControlBlock_MetaBlockConnectable

        self._MetaBlockConnectable = None
        self.MetaBlockConnectable = MetaBlockConnectable

        self._MemberOf_MetaBlockReference = None
        self.MemberOf_MetaBlockReference = MemberOf_MetaBlockReference

        super(MetaBlockParameterReference, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["StandardControlBlock_MetaBlockConnectable", "MetaBlockConnectable", "MemberOf_MetaBlockReference"]
    _many_refs = []

    def getStandardControlBlock_MetaBlockConnectable(self):
        
        return self._StandardControlBlock_MetaBlockConnectable

    def setStandardControlBlock_MetaBlockConnectable(self, value):
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            filtered = [x for x in self.StandardControlBlock_MetaBlockConnectable.StandardControlBlock_MetaBlockParameterReference if x != self]
            self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockParameterReference = filtered

        self._StandardControlBlock_MetaBlockConnectable = value
        if self._StandardControlBlock_MetaBlockConnectable is not None:
            if self not in self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockParameterReference:
                self._StandardControlBlock_MetaBlockConnectable._StandardControlBlock_MetaBlockParameterReference.append(self)

    StandardControlBlock_MetaBlockConnectable = property(getStandardControlBlock_MetaBlockConnectable, setStandardControlBlock_MetaBlockConnectable)

    def getMetaBlockConnectable(self):
        
        return self._MetaBlockConnectable

    def setMetaBlockConnectable(self, value):
        if self._MetaBlockConnectable is not None:
            filtered = [x for x in self.MetaBlockConnectable.MetaBlockParameterReference if x != self]
            self._MetaBlockConnectable._MetaBlockParameterReference = filtered

        self._MetaBlockConnectable = value
        if self._MetaBlockConnectable is not None:
            if self not in self._MetaBlockConnectable._MetaBlockParameterReference:
                self._MetaBlockConnectable._MetaBlockParameterReference.append(self)

    MetaBlockConnectable = property(getMetaBlockConnectable, setMetaBlockConnectable)

    def getMemberOf_MetaBlockReference(self):
        
        return self._MemberOf_MetaBlockReference

    def setMemberOf_MetaBlockReference(self, value):
        if self._MemberOf_MetaBlockReference is not None:
            filtered = [x for x in self.MemberOf_MetaBlockReference.MetaBlockParameterReference if x != self]
            self._MemberOf_MetaBlockReference._MetaBlockParameterReference = filtered

        self._MemberOf_MetaBlockReference = value
        if self._MemberOf_MetaBlockReference is not None:
            if self not in self._MemberOf_MetaBlockReference._MetaBlockParameterReference:
                self._MemberOf_MetaBlockReference._MetaBlockParameterReference.append(self)

    MemberOf_MetaBlockReference = property(getMemberOf_MetaBlockReference, setMemberOf_MetaBlockReference)

