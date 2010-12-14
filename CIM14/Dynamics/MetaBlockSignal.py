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

class MetaBlockSignal(IdentifiedObject):

    def __init__(self, metaBlockSignal1=None, metaBlockSignal=None, MemberOf_MetaBlock=None, From=None, To=None, *args, **kw_args):
        """Initialises a new 'MetaBlockSignal' instance.

        @param metaBlockSignal1:
        @param metaBlockSignal:
        @param MemberOf_MetaBlock:
        @param From:
        @param To:
        """
        self._metaBlockSignal1 = []
        self.metaBlockSignal1 = [] if metaBlockSignal1 is None else metaBlockSignal1

        self._metaBlockSignal = []
        self.metaBlockSignal = [] if metaBlockSignal is None else metaBlockSignal

        self._MemberOf_MetaBlock = None
        self.MemberOf_MetaBlock = MemberOf_MetaBlock

        self._From = None
        self.From = From

        self._To = None
        self.To = To

        super(MetaBlockSignal, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["metaBlockSignal1", "metaBlockSignal", "MemberOf_MetaBlock", "From", "To"]
    _many_refs = ["metaBlockSignal1", "metaBlockSignal"]

    def getmetaBlockSignal1(self):
        
        return self._metaBlockSignal1

    def setmetaBlockSignal1(self, value):
        for p in self._metaBlockSignal1:
            filtered = [q for q in p.metaBlockSignal if q != self]
            self._metaBlockSignal1._metaBlockSignal = filtered
        for r in value:
            if self not in r._metaBlockSignal:
                r._metaBlockSignal.append(self)
        self._metaBlockSignal1 = value

    metaBlockSignal1 = property(getmetaBlockSignal1, setmetaBlockSignal1)

    def addmetaBlockSignal1(self, *metaBlockSignal1):
        for obj in metaBlockSignal1:
            if self not in obj._metaBlockSignal:
                obj._metaBlockSignal.append(self)
            self._metaBlockSignal1.append(obj)

    def removemetaBlockSignal1(self, *metaBlockSignal1):
        for obj in metaBlockSignal1:
            if self in obj._metaBlockSignal:
                obj._metaBlockSignal.remove(self)
            self._metaBlockSignal1.remove(obj)

    def getmetaBlockSignal(self):
        
        return self._metaBlockSignal

    def setmetaBlockSignal(self, value):
        for p in self._metaBlockSignal:
            filtered = [q for q in p.metaBlockSignal1 if q != self]
            self._metaBlockSignal._metaBlockSignal1 = filtered
        for r in value:
            if self not in r._metaBlockSignal1:
                r._metaBlockSignal1.append(self)
        self._metaBlockSignal = value

    metaBlockSignal = property(getmetaBlockSignal, setmetaBlockSignal)

    def addmetaBlockSignal(self, *metaBlockSignal):
        for obj in metaBlockSignal:
            if self not in obj._metaBlockSignal1:
                obj._metaBlockSignal1.append(self)
            self._metaBlockSignal.append(obj)

    def removemetaBlockSignal(self, *metaBlockSignal):
        for obj in metaBlockSignal:
            if self in obj._metaBlockSignal1:
                obj._metaBlockSignal1.remove(self)
            self._metaBlockSignal.remove(obj)

    def getMemberOf_MetaBlock(self):
        
        return self._MemberOf_MetaBlock

    def setMemberOf_MetaBlock(self, value):
        if self._MemberOf_MetaBlock is not None:
            filtered = [x for x in self.MemberOf_MetaBlock.MetaBlockSignal if x != self]
            self._MemberOf_MetaBlock._MetaBlockSignal = filtered

        self._MemberOf_MetaBlock = value
        if self._MemberOf_MetaBlock is not None:
            if self not in self._MemberOf_MetaBlock._MetaBlockSignal:
                self._MemberOf_MetaBlock._MetaBlockSignal.append(self)

    MemberOf_MetaBlock = property(getMemberOf_MetaBlock, setMemberOf_MetaBlock)

    def getFrom(self):
        
        return self._From

    def setFrom(self, value):
        if self._From is not None:
            self._From._MetaBlockSignal = None

        self._From = value
        if self._From is not None:
            self._From.MetaBlockSignal = None
            self._From._MetaBlockSignal = self

    From = property(getFrom, setFrom)

    def getTo(self):
        
        return self._To

    def setTo(self, value):
        if self._To is not None:
            filtered = [x for x in self.To.MetaBlockSignal if x != self]
            self._To._MetaBlockSignal = filtered

        self._To = value
        if self._To is not None:
            if self not in self._To._MetaBlockSignal:
                self._To._MetaBlockSignal.append(self)

    To = property(getTo, setTo)

