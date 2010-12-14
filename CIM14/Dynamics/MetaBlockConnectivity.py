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

class MetaBlockConnectivity(IdentifiedObject):

    def __init__(self, BlockConnectivity=None, MetaBlockConSignal=None, metaBlockConnection0=None, metaBlockConSignal0=None, MetaBlockConnection=None, *args, **kw_args):
        """Initialises a new 'MetaBlockConnectivity' instance.

        @param BlockConnectivity:
        @param MetaBlockConSignal:
        @param metaBlockConnection0:
        @param metaBlockConSignal0:
        @param MetaBlockConnection:
        """
        self._BlockConnectivity = []
        self.BlockConnectivity = [] if BlockConnectivity is None else BlockConnectivity

        self._MetaBlockConSignal = []
        self.MetaBlockConSignal = [] if MetaBlockConSignal is None else MetaBlockConSignal

        self._metaBlockConnection0 = []
        self.metaBlockConnection0 = [] if metaBlockConnection0 is None else metaBlockConnection0

        self._metaBlockConSignal0 = []
        self.metaBlockConSignal0 = [] if metaBlockConSignal0 is None else metaBlockConSignal0

        self._MetaBlockConnection = []
        self.MetaBlockConnection = [] if MetaBlockConnection is None else MetaBlockConnection

        super(MetaBlockConnectivity, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["BlockConnectivity", "MetaBlockConSignal", "metaBlockConnection0", "metaBlockConSignal0", "MetaBlockConnection"]
    _many_refs = ["BlockConnectivity", "MetaBlockConSignal", "metaBlockConnection0", "metaBlockConSignal0", "MetaBlockConnection"]

    def getBlockConnectivity(self):
        
        return self._BlockConnectivity

    def setBlockConnectivity(self, value):
        for x in self._BlockConnectivity:
            x.MetaBlockConnectivity = None
        for y in value:
            y._MetaBlockConnectivity = self
        self._BlockConnectivity = value

    BlockConnectivity = property(getBlockConnectivity, setBlockConnectivity)

    def addBlockConnectivity(self, *BlockConnectivity):
        for obj in BlockConnectivity:
            obj.MetaBlockConnectivity = self

    def removeBlockConnectivity(self, *BlockConnectivity):
        for obj in BlockConnectivity:
            obj.MetaBlockConnectivity = None

    def getMetaBlockConSignal(self):
        
        return self._MetaBlockConSignal

    def setMetaBlockConSignal(self, value):
        for x in self._MetaBlockConSignal:
            x.MemberOf_MetaBlockConnectivity = None
        for y in value:
            y._MemberOf_MetaBlockConnectivity = self
        self._MetaBlockConSignal = value

    MetaBlockConSignal = property(getMetaBlockConSignal, setMetaBlockConSignal)

    def addMetaBlockConSignal(self, *MetaBlockConSignal):
        for obj in MetaBlockConSignal:
            obj.MemberOf_MetaBlockConnectivity = self

    def removeMetaBlockConSignal(self, *MetaBlockConSignal):
        for obj in MetaBlockConSignal:
            obj.MemberOf_MetaBlockConnectivity = None

    def getmetaBlockConnection0(self):
        
        return self._metaBlockConnection0

    def setmetaBlockConnection0(self, value):
        for x in self._metaBlockConnection0:
            x.metaBlockConnectivity0 = None
        for y in value:
            y._metaBlockConnectivity0 = self
        self._metaBlockConnection0 = value

    metaBlockConnection0 = property(getmetaBlockConnection0, setmetaBlockConnection0)

    def addmetaBlockConnection0(self, *metaBlockConnection0):
        for obj in metaBlockConnection0:
            obj.metaBlockConnectivity0 = self

    def removemetaBlockConnection0(self, *metaBlockConnection0):
        for obj in metaBlockConnection0:
            obj.metaBlockConnectivity0 = None

    def getmetaBlockConSignal0(self):
        
        return self._metaBlockConSignal0

    def setmetaBlockConSignal0(self, value):
        for x in self._metaBlockConSignal0:
            x.metaBlockConnectivity0 = None
        for y in value:
            y._metaBlockConnectivity0 = self
        self._metaBlockConSignal0 = value

    metaBlockConSignal0 = property(getmetaBlockConSignal0, setmetaBlockConSignal0)

    def addmetaBlockConSignal0(self, *metaBlockConSignal0):
        for obj in metaBlockConSignal0:
            obj.metaBlockConnectivity0 = self

    def removemetaBlockConSignal0(self, *metaBlockConSignal0):
        for obj in metaBlockConSignal0:
            obj.metaBlockConnectivity0 = None

    def getMetaBlockConnection(self):
        
        return self._MetaBlockConnection

    def setMetaBlockConnection(self, value):
        for x in self._MetaBlockConnection:
            x.MemberOf_MetaBlockConnectivity = None
        for y in value:
            y._MemberOf_MetaBlockConnectivity = self
        self._MetaBlockConnection = value

    MetaBlockConnection = property(getMetaBlockConnection, setMetaBlockConnection)

    def addMetaBlockConnection(self, *MetaBlockConnection):
        for obj in MetaBlockConnection:
            obj.MemberOf_MetaBlockConnectivity = self

    def removeMetaBlockConnection(self, *MetaBlockConnection):
        for obj in MetaBlockConnection:
            obj.MemberOf_MetaBlockConnectivity = None

