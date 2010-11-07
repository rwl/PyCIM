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

class MetaBlockConSignal(IdentifiedObject):

    def __init__(self, MetaBlockConInput=None, MemberOf_MetaBlockConnectivity=None, MetaBlockConOutput=None, metaBlockConnectivity0=None, **kw_args):
        """Initializes a new 'MetaBlockConSignal' instance.

        @param MetaBlockConInput:
        @param MemberOf_MetaBlockConnectivity:
        @param MetaBlockConOutput:
        @param metaBlockConnectivity0:
        """
        self._MetaBlockConInput = None
        self.MetaBlockConInput = MetaBlockConInput

        self._MemberOf_MetaBlockConnectivity = None
        self.MemberOf_MetaBlockConnectivity = MemberOf_MetaBlockConnectivity

        self._MetaBlockConOutput = None
        self.MetaBlockConOutput = MetaBlockConOutput

        self._metaBlockConnectivity0 = None
        self.metaBlockConnectivity0 = metaBlockConnectivity0

        super(MetaBlockConSignal, self).__init__(**kw_args)

    def getMetaBlockConInput(self):
        
        return self._MetaBlockConInput

    def setMetaBlockConInput(self, value):
        if self._MetaBlockConInput is not None:
            self._MetaBlockConInput._MetaBlockConSignal = None

        self._MetaBlockConInput = value
        if self._MetaBlockConInput is not None:
            self._MetaBlockConInput._MetaBlockConSignal = self

    MetaBlockConInput = property(getMetaBlockConInput, setMetaBlockConInput)

    def getMemberOf_MetaBlockConnectivity(self):
        
        return self._MemberOf_MetaBlockConnectivity

    def setMemberOf_MetaBlockConnectivity(self, value):
        if self._MemberOf_MetaBlockConnectivity is not None:
            filtered = [x for x in self.MemberOf_MetaBlockConnectivity.MetaBlockConSignal if x != self]
            self._MemberOf_MetaBlockConnectivity._MetaBlockConSignal = filtered

        self._MemberOf_MetaBlockConnectivity = value
        if self._MemberOf_MetaBlockConnectivity is not None:
            self._MemberOf_MetaBlockConnectivity._MetaBlockConSignal.append(self)

    MemberOf_MetaBlockConnectivity = property(getMemberOf_MetaBlockConnectivity, setMemberOf_MetaBlockConnectivity)

    def getMetaBlockConOutput(self):
        
        return self._MetaBlockConOutput

    def setMetaBlockConOutput(self, value):
        if self._MetaBlockConOutput is not None:
            filtered = [x for x in self.MetaBlockConOutput.MetaBlockConSignal if x != self]
            self._MetaBlockConOutput._MetaBlockConSignal = filtered

        self._MetaBlockConOutput = value
        if self._MetaBlockConOutput is not None:
            self._MetaBlockConOutput._MetaBlockConSignal.append(self)

    MetaBlockConOutput = property(getMetaBlockConOutput, setMetaBlockConOutput)

    def getmetaBlockConnectivity0(self):
        
        return self._metaBlockConnectivity0

    def setmetaBlockConnectivity0(self, value):
        if self._metaBlockConnectivity0 is not None:
            filtered = [x for x in self.metaBlockConnectivity0.metaBlockConSignal0 if x != self]
            self._metaBlockConnectivity0._metaBlockConSignal0 = filtered

        self._metaBlockConnectivity0 = value
        if self._metaBlockConnectivity0 is not None:
            self._metaBlockConnectivity0._metaBlockConSignal0.append(self)

    metaBlockConnectivity0 = property(getmetaBlockConnectivity0, setmetaBlockConnectivity0)

